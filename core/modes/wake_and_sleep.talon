#defines the commands that sleep/wake Talon
mode: all
-
#Note: The function user.hud_toggle_mode() uses the voice commands "talon sleep" and "talon wake"
^(talon sleep | tell and sleep)$:
    user.switcher_hide_running()
    user.history_disable()
    user.homophones_hide()
    user.help_hide()
    user.mouse_sleep()
    speech.disable()
    mode.disable("user.power_mode")
    user.engine_sleep()
^(talon wake | tell and wake)$:
    user.mouse_wake()
    user.talon_mode()
#^drowse$: speech.disable()
^only mouse mode$: speech.disable()
