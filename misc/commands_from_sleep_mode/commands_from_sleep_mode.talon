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

(start | stop) dictation: 
    user.start_stop_dictation()



