os: windows
-
windows search: key(super-s)

#(start | stop) dictation: user.start_stop_dictation()

start listening: 
    #set keyboard to English
    key(alt-shift-1)
    user.toggle_dictation_voice_command()

#börja lyssna
(burial listener | burial alister): 
    #set keyboard to Swedish
    key(alt-shift-2)
    user.toggle_dictation_voice_command()
    
(lang | language) change: key(alt-shift)
#https://www.digitalcitizen.life/keyboard-language-shortcut/
(lang | language) english: key(alt-shift-1)
(lang | language) swedish: key(alt-shift-2)

insert (emo | emoji): key(super-.)

virtual keyboard: key(super-ctrl-o)
#Check if there are better options of virtual keyboards than the Microsoft built in
#https://www.makeuseof.com/windows-best-virtual-keyboards/
#Maybe it's possible to launch the eye control keyboard with a keyboard shortcut
#https://support.microsoft.com/en-us/windows/eye-control-basics-in-windows-97d68837-b993-8462-1f9d-3c957117b1cf
#https://blakewatson.com/journal/writing-and-coding-with-the-macos-accessibility-keyboard/

#The line below doesn't work for some reason. Instead of locking the computer an L is inserted.
#computer lock: key(super-l)
#The line below doesn't work for some reason. Instead of locking the computer it opens Windows search and enter an L.
#computer lock: key(super l)

computer sleep: user.put_computer_to_sleep()

talon (relaunch | restart): user.talon_relaunch()