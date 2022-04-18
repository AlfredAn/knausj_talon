from talon import Module, Context, actions, ui, imgui, settings
from pprint import pprint
from inspect import getmembers
from types import FunctionType

mod = Module()

ctx = Context()
ctx.matches = 'tag: user.rust'

def attributes(obj):
    return {
      name: getattr(obj, name) for name in dir(obj) 
        if hasattr(obj, name)}

@mod.capture(rule=f"<user.letters> | <user.text>")
def rust_identifier(m) -> str:
    if hasattr(m, "letters"):
        return m.letters
    else:
        return actions.user.formatted_text(m.text, "SNAKE_CASE")

@mod.capture(rule=f"ref [<user.rust_lifetime>] [mute]")
def rust_reference(m) -> str:
    return str(m) \
        .replace("mute", "mut") \
        .replace("ref ", "&") \
        .replace("ref", "&")

@mod.capture(rule=f"[<user.rust_reference>] <user.rust_identifier>")
def rust_variable(m) -> str:
    if hasattr(m, "rust_reference"):
        if m.rust_reference[-1] == "&":
            return m.rust_reference + m.rust_identifier
        else:
            return m.rust_reference + " " + m.rust_identifier
    else:
        return str(m)

@mod.capture(rule=f"life (<user.letter> | static | auto)")
def rust_lifetime(m) -> str:
    return "'" + (str(m[1]).replace("auto", "_"))

d = {"mute": "mut", "be": "="}

def s(x, d):
    pprint(x)
    if x[0] == x[1]:
        return d.get(str(x[0]), str(x[0]))
    else:
        return str(x[0])

@mod.capture(rule=f"let [mute] <user.rust_variable> [be]")
def rust_let(m) -> str:
    pprint(attributes(m))
    m = " ".join(list(map(lambda x: s(x, d), zip(m, m._capture))))
    if m[-1] == "=":
        m += " "
    return m

@mod.action_class
class UserActions:
    def insert_no_format(s: str):
        """don't format single quotes"""
        s = s.split("'")
        first = True
        for t in s:
            if not first:
                actions.insert("a")
                actions.key("left")
                actions.insert("'")
                actions.key("delete")
            first = False
            actions.insert(t)

ctx.lists['user.code_libraries'] = {
    'eye oh': 'std::io',
    'file system': 'std::fs',
    'envy': 'std::env',
    'collections': 'std::collections',
    'format': 'std::fmt',
}
ctx.lists['user.code_functions'] = {
    'drop': 'drop',
    'print line': 'println!',
    'error line': 'eprintln!',
}

ctx.lists['user.code_type'] = {
    'you eight': 'u8',
    'eye eight': 'i8',
    'you sixteen': 'u16',
    'eye sixteen': 'i16',
    'you thirty two': 'u32',
    'eye thirty two': 'i32',
    'you sixty four': 'u64',
    'eye sixty four': 'i64',
    'you size': 'usize',
    'eye size': 'isize',
    'bool': 'bool',
    'boolean': 'bool',
    'string': 'str',
    'owned string': 'String',
    'self': 'Self',
}

@ctx.action_class('user')
class UserActions:
    def code_operator_lambda():
        actions.insert('|| ')
        actions.edit.left()
        actions.edit.left()

    def code_operator_subscript():
        actions.insert('[]')
        actions.edit.left()

    def code_operator_increment():
        actions.insert(' += 1')

    def code_operator_indirection():
        actions.auto_insert('*')

    def code_operator_address_of():
        actions.auto_insert('&')

    def code_operator_assignment():
        actions.auto_insert(' = ')

    def code_operator_subtraction():
        actions.auto_insert(' - ')

    def code_operator_subtraction_assignment():
        actions.auto_insert(' -= ')

    def code_operator_addition():
        actions.auto_insert(' + ')

    def code_operator_addition_assignment():
        actions.auto_insert(' += ')

    def code_operator_multiplication():
        actions.auto_insert(' * ')

    def code_operator_multiplication_assignment():
        actions.auto_insert(' *= ')

    def code_operator_exponent():
        actions.auto_insert('.pow()');
        actions.edit.left();

    def code_operator_division():
        actions.auto_insert(' / ')

    def code_operator_division_assignment():
        actions.auto_insert(' /= ')

    def code_operator_modulo():
        actions.auto_insert(' % ')

    def code_operator_modulo_assignment():
        actions.auto_insert(' %= ')

    def code_operator_equal():
        actions.auto_insert(' == ')

    def code_operator_not_equal():
        actions.auto_insert(' != ')

    def code_operator_greater_than():
        actions.auto_insert(' > ')

    def code_operator_greater_than_or_equal_to():
        actions.auto_insert(' >= ')

    def code_operator_less_than():
        actions.auto_insert(' < ')

    def code_operator_less_than_or_equal_to():
        actions.auto_insert(' <= ')

    def code_operator_and():
        actions.auto_insert(' && ')

    def code_operator_or():
        actions.auto_insert(' || ')

    def code_operator_bitwise_and():
        actions.auto_insert(' & ')

    def code_operator_bitwise_or():
        actions.auto_insert(' | ')

    def code_operator_bitwise_exclusive_or():
        actions.auto_insert(' ^ ')

    def code_operator_bitwise_left_shift():
        actions.auto_insert(' << ')

    def code_operator_bitwise_left_shift_assignment():
        actions.auto_insert(' <<= ')

    def code_operator_bitwise_right_shift():
        actions.auto_insert(' >> ')

    def code_operator_bitwise_right_shift_assignment():
        actions.auto_insert(' >>= ')

    def code_operator_object_accessor():
        actions.auto_insert('.')

    def code_state_switch():
        actions.insert('match ')

    def code_block():
        actions.auto_insert('{\n\n}')
        actions.edit.left()
        actions.edit.up()
        actions.key('tab')

    def code_import():
        actions.auto_insert('use ')

    def code_comment_line_prefix():
        actions.auto_insert('//')

    def code_comment_documentation():
        actions.auto_insert('/// ')

    def code_self():
        actions.auto_insert('self')

    def code_insert_true():
        actions.auto_insert('true')

    def code_insert_false():
        actions.auto_insert('false')

    def code_state_if():
        actions.insert('if ')

    def code_state_else():
        actions.insert('else ')

    def code_state_else_if():
        actions.insert('else if ')

    def code_state_return():
        actions.insert('return ')

    def code_insert_function(text: str, selection: str):
        actions.user.paste(f'{text}({selection or ""})')
        actions.edit.left()

    def code_private_function(text: str):
        actions.insert('fn ')
        formatter = settings.get('user.code_private_function_formatter')
        function_name = actions.user.formatted_text(text, formatter)
        actions.user.code_insert_function(function_name, None)

    def code_protected_function(text: str):
        actions.insert('pub(crate) fn ')
        formatter = settings.get('user.code_protected_function_formatter')
        function_name = actions.user.formatted_text(text, formatter)
        actions.user.code_insert_function(function_name, None)

    def code_public_function(text: str):
        actions.insert('pub fn ')
        formatter = settings.get('user.code_public_function_formatter')
        function_name = actions.user.formatted_text(text, formatter)
        actions.user.code_insert_function(function_name, None)

    def code_default_function(text: str):
        actions.user.code_private_function(text)

    def code_insert_type_annotation(type: str):
        actions.insert(f': {type}')

    def code_insert_return_type(type: str):
        actions.insert(f' -> {type}')

    def code_state_for():
        actions.insert('for ')

    def code_state_return():
        actions.insert('return ')
