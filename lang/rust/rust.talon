tag: user.rust
-
tag(): user.code_imperative
tag(): user.code_object_oriented
tag(): user.code_comment_line
tag(): user.code_comment_block_c_like
tag(): user.code_comment_documentation
tag(): user.code_data_bool
tag(): user.code_functions
tag(): user.code_functions_gui
tag(): user.code_libraries
tag(): user.code_libraries_gui
tag(): user.code_operators_array
tag(): user.code_operators_assignment
tag(): user.code_operators_bitwise
tag(): user.code_operators_math
tag(): user.code_operators_pointer

settings():
    user.code_private_function_formatter = "SNAKE_CASE"
    user.code_protected_function_formatter = "SNAKE_CASE"
    user.code_public_function_formatter = "SNAKE_CASE"
    user.code_private_variable_formatter = "SNAKE_CASE"
    user.code_public_variable_formatter = "SNAKE_CASE"

<user.rust_lifetime>:
    user.insert_no_format("{rust_lifetime}")

<user.rust_let>:
    user.insert_no_format("{rust_let}")

state unsafe: "unsafe "

state struct <user.text>:
    insert("struct ")
    insert(user.formatted_text(text, "PUBLIC_CAMEL_CASE"))

state enum <user.text>:
    insert("enum ")
    insert(user.formatted_text(text, "PUBLIC_CAMEL_CASE"))

state trait <user.text>:
    insert("trait ")
    insert(user.formatted_text(text, "PUBLIC_CAMEL_CASE"))

toggle use: user.code_toggle_libraries()

state pub: "pub "
state pub crate: "pub(crate) "
state dyn: "dyn "
state imp: "impl "
state let mute: "let mut "
state let: "let "
state mute: "mut "
state ref mute: "ref mut "
state ref: "ref "
state trait: "trait "
state match: "match "
state use: "use "
state const: "const "
state where: "where "
state where slap: "where\n\t"
state crate: "crate::"
state some:
    "Some()"
    key(left)
state none: "None"

do arrow: " -> "
do dub arrow: " => "

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

use <user.code_libraries>:
    user.code_insert_library(code_libraries, "")
    key(semicolon enter)

as {user.code_type}: insert(" as {code_type}")

print display:
    insert("println!(\"{}\", );")
    key(left:2)

print debug:
    insert("println!(\"{{:?}}\", );")
    key(left:2)
