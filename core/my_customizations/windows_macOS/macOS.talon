os: mac
-

(start | stop) dictation: user.start_stop_dictation()
#(start | stop) dictation: user.start_stop_dictation()

start listening: 
    #set keyboard to English
    #key(alt-shift-1)
    user.toggle_dictation_voice_command()

#börja lyssna
(burial listener | burial alister): 
    #set keyboard to Swedish
    #key(alt-shift-2)
    user.toggle_dictation_voice_command()

talon (relaunch | restart): user.talon_relaunch()