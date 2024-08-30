<<<<<<< HEAD
^grab screen$: 
    user.engine_mimic("event log clear logs")
    user.screenshot()
    #key(super-printscr)
#^grab screen <number_small>$: user.screenshot(number_small)
#^grab window$: user.screenshot_window()
#Commented out the command below in favor for the setup in gamen_computer.talon
#^grab screen selection$: 
    #user.engine_mimic("event log clear logs")
    #user.screenshot_selection()
#The command below can be used instead of `grab screen selection`
^grab selection clip$:
    user.engine_mimic("event log clear logs")
    user.screenshot_selection_clip()
#^grab settings$: user.screenshot_settings()
^grab screen clip$: 
    user.engine_mimic("event log clear logs")
    user.screenshot_clipboard()
^grab screen <number_small> clip$: 
    user.engine_mimic("event log clear logs")
    user.screenshot_clipboard(number_small)
^grab window clip$: 
    user.engine_mimic("event log clear logs")
    user.screenshot_window_clipboard()
=======
not tag: user.screenshot_disabled
-

^grab screen$: user.screenshot()
^grab screen <number_small>$: user.screenshot(number_small)
^grab window$: user.screenshot_window()
^grab selection$: user.screenshot_selection()
^grab selection clip$: user.screenshot_selection_clip()
^grab settings$: user.screenshot_settings()
^grab screen clip$: user.screenshot_clipboard()
^grab screen <number_small> clip$: user.screenshot_clipboard(number_small)
^grab window clip$: user.screenshot_window_clipboard()
>>>>>>> upstream/main
