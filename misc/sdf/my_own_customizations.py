from talon import Module, actions, Context


mod = Module()

@mod.action_class
class Actions:
    def repeat_slowly(rep: int):
        """Repeats the command rep times with wait times in between each repetition"""


ctx=Context()

@ctx.action_class("user")
class UserActions:
    def repeat_slowly(rep: int):
        """Repeats the command rep times with wait times in between each repetition"""
        for i in range(rep):
            actions.core.repeat_command(1)
            actions.sleep("150ms")
