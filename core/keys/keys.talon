go <user.arrow_keys>: user.move_cursor(arrow_keys)
<user.letter>: key(letter)
(ship | uppercase) <user.letters> [(sunk | lowercase | over)]:
    user.insert_formatted(letters, "ALL_CAPS")
<user.symbol_key>: key(symbol_key)
<user.function_key>: key(function_key)
<user.special_key>: key(special_key)
<user.modifiers> <user.unmodified_key>: key("{modifiers}-{unmodified_key}")
# for key combos consisting only of modifiers, eg. `press super`.
press <user.modifiers>: key(modifiers)
# for consistency with dictation mode and explicit arrow keys if you need them.
press <user.keys>: key(keys)
# press and hold a modifier
hold <user.modifiers>:
    key("{modifiers}:down")
    user.gui_hold_modifier_toggle(1, "{modifiers}")
(lift | unhold) <user.modifiers>:
    key("{modifiers}:up")
    user.gui_hold_modifier_toggle(0, "{modifiers}")

#f-keys
#f5
(fork five | four five):
    key(f5)
#f10
(fork ten | four ten):
    key(f10)
#f11
(fork eleven | four eleven):
    key(f11)
#f12
(fork twelve | four twelve):
    key(f12)