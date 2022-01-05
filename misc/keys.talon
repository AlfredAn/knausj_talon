go <user.arrow_keys>: key(arrow_keys)
<user.letter>: key(letter)
(ship | uppercase) <user.letters> [(lowercase | sunk)]: 
    user.insert_formatted(letters, "ALL_CAPS")
<user.symbol_key>: key(symbol_key)
<user.function_key>: key(function_key)
<user.special_key>: key(special_key)
<user.modifiers> <user.unmodified_key>: key("{modifiers}-{unmodified_key}")
just <user.modifiers>: key(user.modifiers)
before <user.modifiers> <user.any_alphanumeric_key>:
    key("{modifiers}-{any_alphanumeric_key}")
    key("left")
before <user.any_alphanumeric_key>:
    key("{any_alphanumeric_key}")
    key("left")    
jump: key(tab)
all tab: key(alt-tab)
