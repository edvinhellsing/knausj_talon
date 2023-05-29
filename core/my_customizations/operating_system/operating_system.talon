^system shutdown$:
    user.system_shutdown()
^system restart$:
    user.system_restart()
^system hibernate$:
    user.toggle_talon_microphone()
    user.system_hibernate()
^system lock$:
    user.toggle_talon_microphone()
    user.system_lock()

#open {user.launch_command}:
#    user.exec(launch_command)