from talon import Module, Context, actions, ui, imgui, settings

mod = Module()

ctx = Context()
ctx.matches = r'''
mode: user.rust
mode: user.auto_lang
and code.language: rust
'''

ctx.lists['user.code_libraries'] = {
    'eye oh': 'std::io',
    'file system': 'std::fs',
    'envy': 'std::env',
    'collections': 'std::collections',
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
    'boolean': 'bool',
    'string': 'str',
    'owned strign': 'String',
}

@ctx.action_class('user')
class UserActions:
    def code_operator_lambda():
        actions.insert('|| ')

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
