from talon import Module, actions

mod = Module()


@mod.action_class
class Actions:
    def window_jump(number: int):
        """Jumps to the specified window"""
        if number < 9:
            actions.key(f"super-{number}")