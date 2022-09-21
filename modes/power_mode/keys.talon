mode: user.power_mode
-
# go <user.arrow_keys>: user.move_cursor(arrow_keys)
# <user.letter>: key(letter)
# (ship | uppercase) <user.letters> [(lowercase | sunk)]:
#     user.insert_formatted(letters, "ALL_CAPS")
# <user.symbol_key>: key(symbol_key)
# <user.function_key>: key(function_key)
# <user.special_key>: key(special_key)
# <user.modifiers> <user.unmodified_key>: key("{modifiers}-{unmodified_key}")
# for key combos consisting only of modifiers, eg. `press super`.
# press <user.modifiers>: key(modifiers)
# for consistency with dictation mode and explicit arrow keys if you need them.
#press <user.keys>: key(keys)

#Custom for power_mode

# enter: key(enter)
# at sign: key(@)
# clear: key(backspace)
# delete: key(delete)

press <user.modifiers>: key(modifiers)
press <user.symbol_key>: key(symbol_key)
press <user.function_key>: key(function_key)
press <user.special_key>: key(special_key)

go left: key(left)
go right: key(right)
go up: key(up)
go down: key(down)

press {user.power_mode_alphabet}: "{power_mode_alphabet}"