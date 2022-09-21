mode: sleep
-

^listen <phrase>$: user.momentary()

<phrase>: skip()

^dictate <phrase>: 
    mode.disable('sleep')
    mode.disable('command')
    mode.disable('user.power_mode')
    mode.enable('dictation')
    sleep(500ms)
    user.try_to_mimic("{phrase}")
    mode.disable('dictation')
    mode.enable('sleep')  

start listening: 
    #set keyboard to English
    key(alt-shift-2)
    user.start_stop_dictation_voice_command()

(burial listener | burial alister): 
    #set keyboard to Swedish
    key(alt-shift-1)
    user.start_stop_dictation_voice_command()
    
stop listening: 
    user.start_stop_dictation_voice_command()

(slut Alister | slut alisa | slut dart listener):
    user.start_stop_dictation_voice_command()
