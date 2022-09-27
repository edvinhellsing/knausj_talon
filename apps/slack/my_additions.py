from talon import Module, actions, Context

mod = Module()

@mod.action_class
class Actions:
    def slack_browse_channels(search_str: str):
        """sdf"""

    def slack_browse_dms(search_str: str):
        """sdf"""


ctx=Context()

#actions.app.notify("test")
@ctx.action_class("user")
class UserActions:
    def slack_browse_channels(search_str: str):
        """sdf"""
        actions.key("ctrl-shift-l")
        actions.sleep("200ms")
        actions.key("escape")
        actions.sleep("200ms")
        actions.auto_insert(search_str)
        actions.sleep("500ms") 
        actions.key("enter")
        #actions.key("down")

    def slack_browse_dms(search_str: str):
        """sdf"""
        actions.key("ctrl-shift-k")
        actions.sleep("200ms")
        actions.auto_insert(search_str)