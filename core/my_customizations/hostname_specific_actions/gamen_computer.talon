hostname: Gamen
-
#Windows key + Ctrl + (number) – Switch to the last active window of the app pinned to the taskbar in the position indicated by the number.
focus [file] explorer: key(super-ctrl-2)
focus chrome: key(super-ctrl-3)
focus work: key(super-ctrl-4) #focuses on the joel@zutobi.com chrome profile browser window
focus edge: key(super-ctrl-5)
focus notes: key(super-ctrl-6)
focus (slack | lack | like): key(super-ctrl-7)

focus outlook: user.open_specific_tab("chrome", "outlook.live.com")
focus google calendar: user.open_specific_tab("chrome", "calendar.google.com")
#focus notes: user.open_specific_tab("chrome", "iCloud-anteckningar")

focus gmail: user.open_specific_tab("edge", "mail.google.com joel@zutobi")
focus gmail zero: user.open_specific_tab("edge", "mail.google.com joel@zutobi")
focus gmail one: user.open_specific_tab("edge", "mail.google.com support@zutobi")
focus gmail two: user.open_specific_tab("edge", "mail.google.com hello@zutobi")
focus gmail three: user.open_specific_tab("edge", "mail.google.com lalurran@gmail")

^grab screen selection$:
    key(super-alt-8)
    sleep(300ms)
    key(enter)