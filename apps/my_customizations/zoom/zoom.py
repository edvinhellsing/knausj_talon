from talon import Module, actions, Context

ctx_avc=Context()
ctx_avc.matches = r"""
os: windows
os: linux
app: zoom meetings
"""

ctx_avc.tags = ["user.avc"]

#https://support.zoom.us/hc/en-us/articles/205683899-Hot-keys-and-keyboard-shortcuts
@ctx_avc.action_class("user")
class AvcActions:
    def avc_toggle_mute():
        actions.key("alt-a")

    def avc_toggle_video():
        actions.key("alt-v")

    def avc_toggle_screensharing():
        actions.key("alt-s")

    def avc_raise_hand():
        actions.key("alt-y")

    def avc_toggle_chat_window():
        actions.key("alt-h")

    def avc_push_to_talk():
        pass

    def avc_toggle_participants():
        actions.key("alt-u")

    #PageUp: View previous 25 participants videos in gallery view
    def avc_increase_participants_tiles():
        actions.key("pageup")

    #PageDown: View next 25 participants videos in gallery view
    def avc_decrease_participants_tiles():
        actions.key("pagedown")

    def avc_invite_participants():
        actions.key("alt-i")

    def avc_leave_call():
        actions.key("alt-q")
        #actions.app.window_close()

    def avc_keyboard_shortcuts():
        pass
