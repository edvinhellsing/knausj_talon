from talon import Module, actions, Context, scope

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

    def start_stop_dictation():
        """Start dictation on both Windows and macOS"""

    def start_stop_dictation_voice_command():
        """Start dictation on both Windows and macOS using a voice command"""


ctx=Context()

@ctx.action_class("user")
class UserActions:
    def put_computer_to_sleep():
        """Puts computer into sleep mode"""
        if app.platform == "windows":
            actions.key("super-x")
            actions.sleep("200ms")
            actions.key("u")
            actions.sleep("200ms")
            actions.key("s")

    # From this repo:
    # https://github.com/nriley/knausj_talon/blob/ed7b1c1e/code/talon_helpers.py#L161
    def talon_relaunch():
        """Quit and relaunch the Talon app"""
        talon_app = ui.apps(pid=os.getpid())[0]
        if app.platform == "windows":
            os.startfile(talon_app.exe)
            talon_app.quit()  
        elif app.platform == "mac":
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

    def start_stop_dictation():
        """Start dictation on both Windows and macOS"""
        if app.platform == "windows":
            actions.key("super-h")
        elif app.platform == "mac":
            actions.key("ctrl")
            actions.sleep("50ms")
            actions.key("ctrl")

    def start_stop_dictation_voice_command():
        """Start dictation on both Windows and macOS using a voice command"""
        if "command" in scope.get("mode"):
            actions.user.mouse_sleep()
            actions.speech.toggle()
            actions.user.start_stop_dictation()
        elif "user.power_mode" in scope.get("mode"):
            actions.user.mouse_sleep()
            actions.speech.toggle()
            actions.mode.disable("user.power_mode")
            actions.user.start_stop_dictation()
        elif "sleep" in scope.get("mode"):
            #add some sleep time to make sure talon doesn't pick up any speech
            actions.sleep("500ms")
            actions.speech.toggle()
            actions.user.mouse_wake()