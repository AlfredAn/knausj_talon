tag: user.code_operators
-
#pointer operators
do dereference: user.code_operator_indirection()
do address of: user.code_operator_address_of()
do struct deref: user.code_operator_structure_dereference()

#lambda
do lambda: user.code_operator_lambda()

#subscript
do subscript: user.code_operator_subscript()

#assignment
do (equals | assign): user.code_operator_assignment()

#math operators
do (minus | subtract): user.code_operator_subtraction()
do (minus | subtract) equals: user.code_operator_subtraction_assignment()
do (plus | add): user.code_operator_addition()
do (plus | add) equals: user.code_operator_addition_assignment()
do (times | multiply): user.code_operator_multiplication()
do (times | multiply) equals: user.code_operator_multiplication_assignment()
do divide: user.code_operator_division()
do divide equals: user.code_operator_division_assignment()
do (mod | modulo): user.code_operator_modulo()
do (mod | modulo) equals: user.code_operator_modulo_assignment()
(do (power | exponent) | to the power [of]): user.code_operator_exponent()

#comparison operators
is equal: user.code_operator_equal()
is not equal: user.code_operator_not_equal()
is (greater | more) [than]: user.code_operator_greater_than()
is less [than]: user.code_operator_less_than()
is (greater | more) [than] or equal: user.code_operator_greater_than_or_equal_to()
is less [than] or equal: user.code_operator_less_than_or_equal_to()
is in: user.code_operator_in()

#logical operators
(do | [do] logical) and: user.code_operator_and()
(do | [do] logical) or: user.code_operator_or()

#bitwise operators
[do] bitwise and: user.code_operator_bitwise_and()
[do] bitwise or: user.code_operator_bitwise_or()
(do | [do] (logical | bitwise)) ((ex | exclusive) or | xor): user.code_operator_bitwise_exclusive_or()
(do | [do] (logical | bitwise)) (left shift | shift left): user.code_operator_bitwise_left_shift()
(do | [do] (logical | bitwise)) (right shift | shift right): user.code_operator_bitwise_right_shift()
(do | [do] (logical | bitwise)) ((ex | exclusive) or | xor) equals: user.code_operator_bitwise_exclusive_or_equals()
[(do | [do] (logical | bitwise))] (left shift | shift left) equals: user.code_operator_bitwise_left_shift_equals()
[(do | [do] (logical | bitwise))] (left right | shift right) equals: user.code_operator_bitwise_right_shift_equals()

#tbd
(do | pad) colon: " : "
