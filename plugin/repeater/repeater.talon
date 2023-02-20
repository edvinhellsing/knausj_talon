# -1 because we are repeating, so the initial command counts as one
#<user.ordinals>: core.repeat_command(ordinals-1)
<number_small> times$: core.repeat_command(number_small-1)
<number_small> slow times$: user.repeat_command_wrapper(number_small-1)
(repeat it | twice)$: core.repeat_command(1)
thrice$: core.repeat_command(2)

^<number_small> times: core.repeat_command(number_small)
^<number_small> slow times: user.repeat_command_wrapper(number_small)
^(repeat it | twice): core.repeat_command(2)
^thrice: core.repeat_command(3)

again: core.repeat_command(1)

^repeat it <number_small> [times]: core.repeat_command(number_small)

^repeat phrase <number_small> [times]: core.repeat_phrase(number_small)