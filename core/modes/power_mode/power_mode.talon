mode: user.power_mode
-
#What <phrase>: skip() does is that it recognizes every phrase that is not a command you have defined, and skips it. It reduces the number of false positives, but unfortunately adds false negatives
<phrase>: skip()
#I've had some problems with talon waking up from sleep due to unintelligible speech (e.g. when the mic barely picks up a youtube video playing on speakers). I think I found a trick to significantly reduce these occurrences. In addition to <phrase>: skip(), add <number>: skip(). I think it's that when talon doesn't know what is being said, everything has roughly equal probability, and a command like "talon wake" gets preferred over "<phrase>". By adding more non-dictation commands, the probability of talon choosing the wake up command drops. b108 has a tendency to associate unclear speech with numbers, so a <number> command works particularly well for this purpose.
<number>: skip()