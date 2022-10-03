#A general advice if I may, try to find a quite idiomatic way for short commands because you risk to have difficulty to remember them when you would have 50 of them. Personally i use a y suffix for most of my short commands: lessy, listy, movy, taily, awky and so forth

#Question. In knausj_talon what is the difference between edit.find() and user.find()?
#If you find them in actions.list() they should both have descriptions

#Otherwise, you should check out events.tail() in the repl to see what's happening behind the scenes for specific commands

#https://bitwarden.com/help/keyboard-shortcuts/
#Bitwarden (launch | activate): key(ctrl-shift-Y)
[Bitwarden] (pass | password) fill: key(ctrl-shift-L)
[Bitwarden] (pass | password) generate: key(ctrl-shift-9)

#test select start: user.select_continous(1)
#test select end: user.select_continous(0)

insert {user.additional_words}: auto_insert(additional_words) 
website {user.website}: auto_insert(website)
system path <user.system_path>: auto_insert(system_path)

em phrase: "Mm, "
hem phrase: "Hmm, "
ah phrase: "Aa, "
(I get it | I understand) phrase: "Aha, "
ha ha phrase: "Haha"
ha ha ha phrase: "Hahaha"

(mic | Mike | microphone) off: user.toggle_talon_microphone()
key(scroll_lock): user.toggle_talon_microphone()

focus outlook: user.open_specific_tab("chrome", "outlook.live.com")
focus google calendar: user.open_specific_tab("chrome", "calendar.google.com")
#focus notes: user.open_specific_tab("chrome", "iCloud-anteckningar")

focus gmail: user.open_specific_tab("edge", "mail.google.com joel@zutobi")
focus gmail zero: user.open_specific_tab("edge", "mail.google.com joel@zutobi")
focus gmail one: user.open_specific_tab("edge", "mail.google.com support@zutobi")
focus gmail two: user.open_specific_tab("edge", "mail.google.com hello@zutobi")
focus gmail three: user.open_specific_tab("edge", "mail.google.com lalurran@gmail")

# Pick item from a dropdown
pick [down] <number_small>: key("down:{number_small-1} enter")
pick up <number_small>: key("up:{number_small} enter")
#dropdown <number_small>: key("down:{number_small-1} enter") 
#drop up <number_small>: key("up:{number_small} enter")

(end ten | ten enter): key(enter)

profile switcher open: user.open_browser_profile_switcher("chrome")