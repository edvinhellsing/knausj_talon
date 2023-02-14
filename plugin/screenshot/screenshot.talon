#^grab screen$: user.screenshot()
^grab screen$: 
    user.engine_mimic("event log clear logs")
    key(super-printscr)             
#^grab screen <number_small>$: user.screenshot(number_small)
#^grab window$: user.screenshot_window()
#^grab screen selection$: user.screenshot_selection() #commented out in favor for setup in gamen_computer.talon
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
