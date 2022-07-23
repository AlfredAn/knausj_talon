tag: user.rust
-
tag(): user.code_comment_line
tag(): user.code_comment_block_c_like
tag(): user.code_comment_documentation

tag(): user.code_imperative
tag(): user.code_object_oriented

tag(): user.code_data_bool
tag(): user.code_data_null

tag(): user.code_functions
tag(): user.code_functions_common
tag(): user.code_libraries
tag(): user.code_libraries_gui

tag(): user.code_operators_array
tag(): user.code_operators_assignment
tag(): user.code_operators_bitwise
tag(): user.code_operators_math

settings():
    user.code_private_function_formatter = "SNAKE_CASE"
    user.code_protected_function_formatter = "SNAKE_CASE"
    user.code_public_function_formatter = "SNAKE_CASE"
    user.code_private_variable_formatter = "SNAKE_CASE"
    user.code_protected_variable_formatter = "SNAKE_CASE"
    user.code_public_variable_formatter = "SNAKE_CASE"

<user.rust_lifetime>:
    user.insert_no_format("{rust_lifetime}")

<user.rust_let>:
    user.insert_no_format("{rust_let}")

# rust-specific grammars

## for unsafe rust
state unsafe: "unsafe "
unsafe block: user.code_state_unsafe()

## rust centric struct and enum definitions
state (struct | structure) <user.text>:
    insert("struct ")
    insert(user.formatted_text(text, "PUBLIC_CAMEL_CASE"))

state enum <user.text>:
    insert("enum ")
    insert(user.formatted_text(text, "PUBLIC_CAMEL_CASE"))

state trait <user.text>:
    insert("trait ")
    insert(user.formatted_text(text, "PUBLIC_CAMEL_CASE"))

toggle use: user.code_toggle_libraries()

## Simple aliases
borrow: "&"
borrow mutable: "&mut "
state (a sink | async | asynchronous): "async "
state (pub | public): "pub "
state (pub | public) crate: "pub(crate) "
state (dyn | dynamic): "dyn "
state constant: "const "
state (funk | func | function): "fn "
state (imp | implements): "impl "
state let mute: "let mut "
state let: "let "
state (mute | mutable): "mut "
state (mod | module): "mod "
state ref (mute | mutable): "ref mut "
state ref: "ref "
state trait: "trait "
state const: "const "
state where: "where "
state where slap: "where\n\t"
state crate: "crate::"
state some:
    "Some()"
    key(left)
state none: "None"

do arrow: " -> "
returns: " -> "
do dub arrow: " => "
becomes: " => "

box that:
    "("
    key(left:2)
    "Box::new"

option that:
    "<"
    key(left:2)
    "Option"

some that:
    "("
    key(left:2)
    "Some"

(rc | r c | are see) that:
    "("
    key(left:2)
    "Rc::new"

state match: user.code_state_switch()
state static: "static "
self taught: "self."
state use: user.code_import()

use <user.code_libraries>:
    user.code_insert_library(code_libraries, "")
    key(; enter)

as {user.code_type}: insert(" as {code_type}")

print display:
    insert("println!(\"{}\", );")
    key(left:2)

print debug:
    insert("println!(\"{{:?}}\", );")
    key(left:2)

## specialist flow control
state if let some: user.code_insert_if_let_some()
state if let (ok|okay): user.code_insert_if_let_okay()
state if let error: user.code_insert_if_let_error()

## rust centric synonyms
is some: user.code_insert_is_not_null()

## for implementing
implement (struct | structure): user.code_state_implements()

## for annotating function parameters
is implemented trait {user.code_trait}: user.code_insert_trait_annotation(code_trait)
is implemented trait: ": impl "
returns implemented trait {user.code_trait}: user.code_insert_return_trait(code_trait)
returns implemented trait: " -> impl "

## for generic reference of traits
trait {user.code_trait}: insert("{code_trait}")
implemented trait {user.code_trait}: insert("impl {code_trait}")
dynamic trait {user.code_trait}: insert("dyn {code_trait}")

## for generic reference of macro
macro {user.code_macros}:
    user.code_insert_macro(code_macros, "")
macro wrap {user.code_macros}:
    user.code_insert_macro(code_macros, edit.selected_text())

## rust specific document comments
block dock comment: user.code_comment_documentation_block()
inner dock comment: user.code_comment_documentation_inner()
inner block dock comment: user.code_comment_documentation_block_inner()
