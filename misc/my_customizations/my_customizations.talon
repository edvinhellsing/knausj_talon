#A general advice if I may, try to find a quite idiomatic way for short commands because you risk to have difficulty to remember them when you would have 50 of them. Personally i use a y suffix for most of my short commands: lessy, listy, movy, taily, awky and so forth

#Question. in knausj_talon what is the difference between edit.find() and user.find()?
#If you find them in actions.list() they should both have descriptions

#Otherwise, you should check out events.tail() in the repl to see what's happening behind the scenes for specific commands


#https://bitwarden.com/help/keyboard-shortcuts/
#Bitwarden (launch | activate): key(ctrl-shift-Y)
[Bitwarden] (pass | password) fill: key(ctrl-shift-L)
[Bitwarden] (pass | password) generate: key(ctrl-shift-9)

#test select start: user.select_continous(1)
#test select end: user.select_continous(0)

website {user.website}: auto_insert(website)
system path <user.system_path>: auto_insert(system_path)

em phrase: "Mm, "
hem phrase: "Hmm, "
ah phrase: "Aa, "
(I get it | I understand) phrase: "Aha, "
ha ha phrase: "Haha "
ha ha ha phrase: "Hahaha "