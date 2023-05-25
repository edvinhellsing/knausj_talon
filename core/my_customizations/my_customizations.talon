#A general advice if I may, try to find a quite idiomatic way for short commands because you risk to have difficulty to remember them when you would have 50 of them. Personally i use a y suffix for most of my short commands: lessy, listy, movy, taily, awky and so forth

#Question. In knausj_talon what is the difference between edit.find() and user.find()?
#If you find them in actions.list() they should both have descriptions

#Otherwise, you should check out events.tail() in the repl to see what's happening behind the scenes for specific commands

#Question: Is there a way to execute a system command in a Talon script file or do I need to create a Python module?
#Answer: user.system_command_nb() 
#And obviously just put the command as a string in the function call

# Bitwarden  
#https://bitwarden.com/help/keyboard-shortcuts/
Bitwarden activate: key(ctrl-shift-Y)
[Bitwarden] password fill: key(ctrl-shift-L)
[Bitwarden] password generate: key(ctrl-shift-9)

# 1pass


#test select start: user.select_continous(1)
#test select end: user.select_continous(0)

insert {user.additional_words}: auto_insert(additional_words) 
website {user.website}: auto_insert(website)
system path <user.system_path>: auto_insert(system_path)

em phrase: "Mm, "
hem phrase: "Hm, "
ah phrase: "Aa, "
(I get it | I understand) phrase: "Aha, "
ha ha phrase: "Haha"
ha ha ha phrase: "Hahaha"

signature phrase: 
    "Best regards"
    edit.line_insert_down()
    "Edvin"

# Control mouse and eyetracking - f13 to switch mic and eyetracking on and off, earlier scroll_lock
(mic | Mike | microphone) off: user.toggle_talon_microphone()
key(f13): user.toggle_talon_microphone()

# Control mouse - f14 to switch control mouse on and off
(mouse) off: user.toggle_control_mouse()
key(f14): user.toggle_control_mouse()

# Pick item from a dropdown
pick [down] <number_small>: key("down:{number_small} enter")
pick up <number_small>: key("up:{number_small} enter")
#dropdown <number_small>: key("down:{number_small-1} enter") 
#drop up <number_small>: key("up:{number_small} enter")

(end ten | ten enter): key(enter)

profile switcher open: user.open_browser_profile_switcher("chrome")

talon hood (configure | reset):
    user.engine_mimic("head up show")
    sleep(300ms)
    user.engine_mimic("event log show")
    sleep(300ms)
    user.engine_mimic("status bar show")
    sleep(300ms)
    # not able to add microphone if not first removed
    user.engine_mimic("status bar remove microphone")
    sleep(300ms)
    user.engine_mimic("status bar add microphone")
    sleep(300ms)
    # not able to add mode indicator if not first removed
    user.engine_mimic("status bar remove mode indicator")
    sleep(300ms)
    user.engine_mimic("status bar add mode indicator")

program (close | quit): user.close_program()

code (comment): user.comment()

code (uncomment): user.uncomment()

(chrome open bookmarks): user.open_chrome_bookmarks()