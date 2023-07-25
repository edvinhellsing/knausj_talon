hostname: Gamen
-
#Windows key + Ctrl + (number). Switch to the last active window of the app pinned to the taskbar in the position indicated by the number.
#focus <number_small>: key("super-ctrl-{number_small}")
focus [file] explorer: key(super-ctrl-2)
focus chrome: key(super-ctrl-3)
focus notes: user.switcher_focus("Opera Internet Browser")
focus (slack | lack | like): user.switcher_focus("Slack")

focus outlook: user.open_specific_tab("Google Chrome", "outlook.live.com")
focus google calendar: user.open_specific_tab("Google Chrome", "calendar.google.com")
#focus notes: user.open_specific_tab("Google Chrome", "iCloud-anteckningar")
focus gmail [joel] [at so tobe dot com]: user.open_specific_tab("Microsoft Edge", "joel@zutobi")
focus gmail support [at so tobe dot com]: user.open_specific_tab("Microsoft Edge", "support@zutobi")
focus gmail hello [at so tobe dot com]: user.open_specific_tab("Microsoft Edge", "hello@zutobi")
focus gmail partnership [at so tobe dot com]: user.open_specific_tab("Microsoft Edge", "partnership@zutobi")

^grab screen selection$:
    user.toggle_talon_microphone()
    user.engine_mimic("event log clear logs")
    key(super-alt-7)
    sleep(300ms)
    key(down:2)
    sleep(300ms)
    key(enter)