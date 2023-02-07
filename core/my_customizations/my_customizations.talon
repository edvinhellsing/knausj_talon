#A general advice if I may, try to find a quite idiomatic way for short commands because you risk to have difficulty to remember them when you would have 50 of them. Personally i use a y suffix for most of my short commands: lessy, listy, movy, taily, awky and so forth

#Question. In knausj_talon what is the difference between edit.find() and user.find()?
#If you find them in actions.list() they should both have descriptions

#Otherwise, you should check out events.tail() in the repl to see what's happening behind the scenes for specific commands

#Question: Is there a way to execute a system command in a Talon script file or do I need to create a Python module?
#Answer: user.system_command_nb() 
#And obviously just put the command as a string in the function call

#test select start: user.select_continous(1)
#test select end: user.select_continous(0)

insert {user.additional_words}: auto_insert(additional_words) 
website {user.website}: auto_insert(website)
system path <user.system_path>: auto_insert(system_path)

em phrase: "Mm, "
hem phrase: "Hmm, "
ah phrase: "Aa, "
(I get it | I understand) phrase: "Aha, "
ha ha phrase: "Haha "
ha ha ha phrase: "Hahaha "
#oh phrase: "Oh, "
no phrase: "Nä, "

(signature phrase | insert signature): 
    "Best regards"
    edit.line_insert_down()
    "Joel"

(signature phrase swedish | insert signature swedish): 
    "Med vänlig hälsning"
    edit.line_insert_down()
    "Joel"

(mic | Mike | microphone) off: user.toggle_talon_microphone()
key(scroll_lock): user.toggle_talon_microphone()

(end ten | ten enter): key(enter)

profile switcher open: user.open_browser_profile_switcher("chrome")

talon hood (configure | reset):
    user.engine_mimic("head up show")
    sleep(300ms)
    user.engine_mimic("event log show")
    sleep(300ms)
    user.engine_mimic("status bar show")
    sleep(300ms)
    #Reset the status bar icons by first removing them
    user.engine_mimic("status bar remove microphone")
    sleep(300ms)
    user.engine_mimic("status bar remove mode indicator")
    sleep(300ms)
    #And then add them again
    user.engine_mimic("status bar add microphone")
    sleep(300ms)
    user.engine_mimic("status bar add mode indicator")

program (close | quit): user.close_program()

#slack (huddle | call) (leave | close): user.slack_system_wide_leave_huddle()

#This works when `control mouse (zoom)` is active
#key(f13): tracking.zoom()