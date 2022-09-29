from talon import Module, actions, Context

ctx_avc=Context()
ctx_avc.matches = r"""
os: windows
os: linux
tag: browser
browser.host: meet.google.com
"""

ctx_avc.tags = ["user.avc"]

#https://support.google.com/a/users/answer/9896256?hl=en
@ctx_avc.action_class("user")
class AvcActions:
    def avc_toggle_mute():
        actions.key("ctrl-d")

    def avc_toggle_video():
        actions.key("ctrl-e")

    def avc_toggle_screensharing():
        pass

    def avc_raise_hand():
        actions.key("ctrl-alt-h")

    def avc_toggle_chat_window():
        actions.key("ctrl-alt-c")

    def avc_push_to_talk():
        pass

    def avc_toggle_participants():
        actions.key("ctrl-alt-p")

    def avc_increase_participants_tiles():
        actions.key("ctrl-alt-j")

    def avc_decrease_participants_tiles():
        actions.key("ctrl-alt-k")

    def avc_invite_participants():
        pass

    def avc_leave_call():
        actions.key("ctrl-w")

    def avc_keyboard_shortcuts():
        actions.key("shift-?")
