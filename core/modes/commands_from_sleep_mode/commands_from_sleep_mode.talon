mode: sleep
-

^listen <phrase>$: user.momentary()

#What <phrase>: skip() does is that it recognizes every phrase that is not a command you have defined, and skips it. It reduces the number of false positives, but unfortunately adds false negatives
<phrase>: skip()
#I've had some problems with talon waking up from sleep due to unintelligible speech (e.g. when the mic barely picks up a youtube video playing on speakers). I think I found a trick to significantly reduce these occurrences. In addition to <phrase>: skip(), add <number>: skip(). I think it's that when talon doesn't know what is being said, everything has roughly equal probability, and a command like "talon wake" gets preferred over "<phrase>". By adding more non-dictation commands, the probability of talon choosing the wake up command drops. b108 has a tendency to associate unclear speech with numbers, so a <number> command works particularly well for this purpose.
<number>: skip()

^dictate <phrase>: 
    mode.disable('sleep')
    mode.disable('command')
    mode.disable('user.power_mode')
    mode.enable('dictation')
    sleep(500ms)
    user.try_to_mimic("{phrase}")
    mode.disable('dictation')
    mode.enable('sleep')  
    
stop listening: 
    user.start_stop_dictation_voice_command()

#sluta lyssna
(slut Alister | slut alisa | slut dart listener):
    user.start_stop_dictation_voice_command()
