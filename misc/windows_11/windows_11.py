from talon import Module, actions, Context


mod = Module()

@mod.action_class
class Actions:
    def put_computer_to_sleep():
        """Puts computer into sleep mode"""
        

ctx=Context()

@ctx.action_class("user")
class UserActions:
    def put_computer_to_sleep():
        """Puts computer into sleep mode"""
        actions.key("super-x")
        actions.sleep("200ms")
        actions.key("u")
        actions.sleep("200ms")
        actions.key("s")