# -1 because we are repeating, so the initial command counts as one
#<user.ordinals>: core.repeat_command(ordinals-1)
<number_small> times: core.repeat_command(number_small-1)
(repeat it|twice): core.repeat_command(1)
thrice: core.repeat_command(2)
repeat it <number_small> [times]: core.repeat_command(number_small)
