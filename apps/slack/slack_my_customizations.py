from talon import Module, actions, Context

mod = Module()

@mod.action_class
class Actions:
    def slack_browse_channels(search_str: str):
        """sdf"""

    def slack_browse_dms(search_str: str):
        """sdf"""

    def slack_leave_huddle():
        """sdf"""

ctx=Context()

#actions.app.notify("test")
@ctx.action_class("user")
class UserActions:
    def slack_browse_channels(search_str: str):
        actions.key("ctrl-shift-l")
        actions.sleep("200ms")
        actions.key("escape")
        actions.sleep("200ms")
        actions.auto_insert(search_str)
        actions.sleep("500ms") 
        actions.key("enter")
        #actions.key("down")

    def slack_browse_dms(search_str: str):
        actions.key("ctrl-shift-k")
        actions.sleep("200ms")
        actions.auto_insert(search_str)

    #This one is thought to be used in a system wide leave huddle voice command
    def slack_leave_huddle():
        actions.user.engine_mimic("focus slack")
        actions.sleep("200ms")
        actions.key("ctrl-shift-h")


ctx_avc=Context()
ctx_avc.matches = r"""
os: windows
os: linux
win.title: /Slack call/
"""

ctx_avc.tags = ["user.avc"]

@ctx_avc.action_class("user")
class AvcActions:
    def avc_toggle_mute():
        actions.key("m")

    def avc_toggle_video():
        actions.key("v")

    def avc_toggle_screensharing():
        pass

    def avc_raise_hand():
        pass

    def avc_toggle_chat_window():
        pass

    def avc_push_to_talk():
        pass

    def avc_toggle_participants():
        pass

    def avc_increase_participants_tiles():
        pass

    def avc_decrease_participants_tiles():
        pass

    def avc_invite_participants():
        actions.key("a")

    def avc_leave_call():
        actions.app.window_close()

    def avc_keyboard_shortcuts():
        actions.key("ctrl-/")
