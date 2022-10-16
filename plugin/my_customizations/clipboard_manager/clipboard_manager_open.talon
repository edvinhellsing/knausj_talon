mode: user.clipboard_manager
-

clipboard stay:
    user.clipboard_manager_toggle_sticky()

clipboard update:
    user.clipboard_manager_update()

clipboard clear:
    user.clipboard_manager_remove()

clipboard chuck <number_small> [and <number_small>]*:
    user.clipboard_manager_remove(number_small_list)

clipboard split <number_small> [and <number_small>]*:
    user.clipboard_manager_split(number_small_list)

clipboard copy <number_small> [and <number_small>]*:
    user.clipboard_manager_copy(number_small_list)