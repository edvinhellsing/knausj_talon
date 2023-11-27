hostname: Gamen
-
#the carrot "^" indicates there is nothing before and the dollar "$" that nothing comes after it, so if you say "copy copy" it won't trigger the voice command "^copy$: edit.copy()"

#Windows key + Ctrl + (number). Switch to the last active window of the app pinned to the taskbar in the position indicated by the number.
#^focus <number_small>: key("super-ctrl-{number_small}")
^focus [file] explorer: key(super-ctrl-2)
^focus chrome: key(super-ctrl-3)
^focus edge: key(super-ctrl-4)
^focus notes: user.switcher_focus("Opera Internet Browser")
#^focus (slack | lack | like): user.switcher_focus("Slack")
^focus (slack | lack | like): key(super-ctrl-6)

^focus outlook: user.open_specific_tab("Google Chrome", "outlook.live.com")
^focus google calendar: user.open_specific_tab("Google Chrome", "calendar.google.com")
#focus notes: user.open_specific_tab("Google Chrome", "iCloud-anteckningar")
^focus gmail [joel] [at so tobe dot com]: user.open_specific_tab("Microsoft Edge", "joel@zutobi")
^focus gmail support [at so tobe dot com]: user.open_specific_tab("Microsoft Edge", "support@zutobi")
^focus gmail hello [at so tobe dot com]: user.open_specific_tab("Microsoft Edge", "hello@zutobi")
^focus gmail partnership [at so tobe dot com]: user.open_specific_tab("Microsoft Edge", "partnership@zutobi")

#Can improve this voice command by first checking if the snipping tool is in focus, and if it is just run key(ctrl-n) 
^grab screen selection$:
    user.toggle_talon_microphone()
    user.engine_mimic("event log clear logs")
    key(super-ctrl-1)
    sleep(300ms)
    key(ctrl-n)

^use both eyes$:
    key(super-b)
    key(right)
    key(enter)
    key(up:6)
    key(enter)
    key(up:3)
    key(enter)

^use only left eye$:
    key(super-b)
    key(right)
    key(enter)
    key(up:6)
    key(enter)
    key(up:2)
    key(enter)