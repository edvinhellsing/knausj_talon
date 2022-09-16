#defines the commands that sleep/wake Talon
mode: all
-
^(talon sleep | sleep | tell and sleep)$:
    user.switcher_hide_running()
    user.history_disable()
    user.homophones_hide()
    user.help_hide()
    user.mouse_sleep()
    speech.disable()
    user.engine_sleep()
^(talon wake | wake | tell and wake)$:
    user.mouse_wake()
    user.talon_mode()
#^drowse$: speech.disable()
^only mouse mode$: speech.disable()
