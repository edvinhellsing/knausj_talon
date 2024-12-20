from talon import Context, actions

ctx = Context()
ctx.matches = r"""
os: mac
"""


@ctx.action_class("app")
class AppActions:
    def preferences():
        actions.key("cmd-,")

    def tab_close():
        actions.key("cmd-w")

    # own chrome navigation like used to in win
    def tab_next():
        actions.key("ctrl-tab")
        #actions.key("cmd-alt-right") mac

    def tab_open():
        actions.key("cmd-t")
    
    # own chrome navigation like used to in win
    def tab_previous():
        actions.key("ctrl-shift-tab")
        #actions.key("cmd-alt-left") mac

    def tab_reopen():
        actions.key("cmd-shift-t")

    def window_close():
        actions.key("cmd-w")

    def window_hide():
        actions.key("cmd-m")

    def window_hide_others():
        actions.key("cmd-alt-h")

    def window_open():
        actions.key("cmd-n")

    def window_previous():
        actions.key("cmd-shift-`")

    def window_next():
        actions.key("cmd-`")


@ctx.action_class("user")
class UserActions:
    def switcher_focus_last():
        actions.key("cmd-tab")
