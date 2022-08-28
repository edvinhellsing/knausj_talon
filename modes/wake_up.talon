#defines the commands that sleep/wake Talon
#mode: all
mode: sleep
mode: dictation
mode: command
not mode: user.no_action_mode
-
^(talon sleep)$:
    user.switcher_hide_running()
    user.history_disable()
    user.homophones_hide()
    user.help_hide()
    user.mouse_sleep()
    speech.disable()
    user.engine_sleep()
^(talon wake | wake)$:
    user.mouse_wake()
    user.talon_mode()
^drowse$: speech.disable()
