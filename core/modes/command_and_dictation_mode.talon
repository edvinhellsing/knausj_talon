mode: command
mode: dictation
-
^dictation mode$:
    mode.disable("sleep")
    mode.disable("command")
    mode.enable("dictation")
    user.code_clear_language_mode()
    user.gdb_disable()
^(command mode | come on mode)$:
    mode.disable("sleep")
    mode.disable("dictation")
    mode.enable("command")
^power mode$:
    mode.disable("sleep")
    mode.disable("command")
    mode.disable("dictation")