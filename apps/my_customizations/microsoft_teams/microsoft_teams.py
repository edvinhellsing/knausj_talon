from talon import Module, actions, Context

ctx_avc=Context()
ctx_avc.matches = r"""
os: windows
os: linux
app: microsoft teams
"""

ctx_avc.tags = ["user.avc"]

#https://support.microsoft.com/en-us/office/keyboard-shortcuts-for-microsoft-teams-2e8e2a70-e8d8-4a19-949b-4c36dd5292d2
@ctx_avc.action_class("user")
class AvcActions:
    def avc_toggle_mute():
        actions.key("ctrl-shift-m")

    def avc_toggle_video():
        actions.key("ctrl-shift-o")

    def avc_toggle_screensharing():
        actions.key("ctrl-shift-e")

    def avc_raise_hand():
        actions.key("ctrl-shift-k")

    def avc_toggle_chat_window():
        pass

    def avc_push_to_talk():
        actions.key("ctrl-space")

    def avc_toggle_participants():
        pass

    def avc_increase_participants_tiles():
        pass

    def avc_decrease_participants_tiles():
        pass

    def avc_invite_participants():
        pass

    def avc_leave_call():
        actions.key("ctrl-shift-h")

    def avc_keyboard_shortcuts():
        pass
