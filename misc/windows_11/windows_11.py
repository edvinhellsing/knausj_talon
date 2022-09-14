from talon import Module, actions, Context

#Below is for the talon_relaunch()
from talon import ui, app
import os


mod = Module()

@mod.action_class
class Actions:
    def put_computer_to_sleep():
        """Puts computer into sleep mode"""

    def talon_relaunch():
        """Quit and relaunch the Talon app"""


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

    # From here:
    # https://github.com/nriley/knausj_talon/blob/ed7b1c1e/code/talon_helpers.py#L161
    def talon_relaunch():
        """Quit and relaunch the Talon app"""
        talon_app = ui.apps(pid=os.getpid())[0]
        if app.platform == "mac":
            from shlex import quote
            from subprocess import Popen

            talon_app_path = quote(talon_app.path)
            Popen(
                [
                    "/bin/sh",
                    "-c",
                    f"/usr/bin/open -W {talon_app_path} ; /usr/bin/open {talon_app_path}",
                ],
                start_new_session=True,
            )
            talon_app.quit()
        elif app.platform == "windows":
            os.startfile(talon_app.exe)
            talon_app.quit()    