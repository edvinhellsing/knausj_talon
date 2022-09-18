from talon import Module, actions, Context


mod = Module()
#mod.mode("mode_custom")
#actions.mode.enable("user.mode_custom")

@mod.action_class
class Actions:
    def paste_plain():
        """Pastes plain text"""
        actions.key("ctrl-shift-v")

#actions.user.paste_plain()


ctx=Context()
ctx.matches="""
os:windows
mode:user.mode_custom
"""

@ctx.action_class("user")
class UserActions:
#@ctx.action_class("custom")
#class CustomActions:
    def paste_plain():
        """Pastes plain text"""
        actions.key("ctrl-shift-v")
        #print("this is being printed into the log")
        #actions.next()

#actions.user.paste_plain()
#actions.custom.paste_plain()