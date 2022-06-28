tag: user.code_operators_math
-

# math operators
do (minus | subtract): user.code_operator_subtraction()
do (plus | add): user.code_operator_addition()
do (times | multiply): user.code_operator_multiplication()
do divide: user.code_operator_division()
do (mod | modulo): user.code_operator_modulo()
(do exponent | to the power [of]): user.code_operator_exponent()

# comparison operators
is equal: user.code_operator_equal()
is not equal: user.code_operator_not_equal()
is (greater | more) [than]: user.code_operator_greater_than()
is less [than]: user.code_operator_less_than()
is (greater | more) [than] or equal: user.code_operator_greater_than_or_equal_to()
is less [than] or equal: user.code_operator_less_than_or_equal_to()

# logical operators
(do | [do] logical) and: user.code_operator_and()
(do | [do] logical) or: user.code_operator_or()

# set operators
(op | is) in: user.code_operator_in()
(op | is) not in: user.code_operator_not_in()

# TODO: This operator should either be abstracted into a function or removed.
(do | pad) colon: " : "
