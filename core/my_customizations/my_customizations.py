from talon import Module, Context, actions, imgui, scope

#Below is for the talon_relaunch()
from talon import ui, app
import os

from talon_plugins import eye_mouse


@imgui.open(x=700, y=0)
def gui_select(gui: imgui.GUI):
    gui.text(f"Select mode:")
    gui.line()
    if gui.button("End selection"):
        actions.user.select_continous(0)

modifier = ""
@imgui.open(x=700, y=0)
def gui_hold_modifier(gui: imgui.GUI):
    gui.text(f"Modifier held:")
    gui.line()
    if gui.button("Lift " + modifier):
        actions.key(modifier + ":up")
        actions.user.gui_hold_modifier_toggle(0, modifier)


mod = Module()

@mod.action_class
class Actions:
    def repeat_slowly(rep: int):
        """Repeats the command rep times with wait times in between each repetition"""

    def toggle_talon_microphone():
        """Toggle the Talon microphone on/off using talon_HUD actions (please note: talon_HUD must be installed in the talon user folder for this function to work)"""

    def open_specific_tab(browser: str, search_str: str):
        """This function requires that the searched for tab actually is open in the browser"""

    def open_browser_profile_switcher(browser: str):
        """sdf"""

    def open_specific_profile(browser: str):
        """sdf"""

    def gui_hold_modifier_toggle(flag: int, key_str: str):
        """sdf"""

    def put_computer_to_sleep():
        """Puts computer into sleep mode"""

    def talon_relaunch():
        """Quit and relaunch the Talon app"""

    def start_stop_dictation():
        """Start dictation on both Windows and macOS"""

    def toggle_dictation_voice_command():
        """Start dictation on both Windows and macOS using a voice command"""

    def toggle_dictation_key_switch():
        """Start dictation on both Windows and macOS using a physical key"""

    def close_program():
        """Uses the OS built-in keyboard shortcut to close the program"""
        
    def slack_system_wide_leave_huddle():
        """sdf"""



    def select_continous(run: int):
        """sdf"""

    def select_continous_end():
        """sdf"""

ctx=Context()

@ctx.action_class("user")
class UserActions:
    def repeat_slowly(rep: int):
        """Repeats the command rep times with wait times in between each repetition"""
        for i in range(rep):
            actions.core.repeat_command(1)
            actions.sleep("200ms")
  
    """
    def toggle_talon_microphone():
        current_microphone = actions.sound.active_microphone()
        if current_microphone == "None":
            #https://github.com/chaosparrot/talon_hud/blob/master/CUSTOMIZATION.md#log-messages
            actions.user.hud_add_log('success', 'Mic and eye tracking enabled')
            actions.user.hud_toggle_microphone()
        else:
            actions.user.hud_add_log('error', 'Mic and eye tracking disabled')
            actions.user.hud_toggle_microphone()
        
        if eye_mouse.tracker is not None and eye_mouse.config.control_mouse:
            actions.user.mouse_sleep()
        elif eye_mouse.tracker is not None and not eye_mouse.config.control_mouse and not "sleep" in scope.get("mode"):
            actions.user.mouse_wake()
    """

    def toggle_talon_microphone():
        current_microphone = actions.sound.active_microphone()
        if current_microphone == "None":
            #https://github.com/chaosparrot/talon_hud/blob/master/CUSTOMIZATION.md#log-messages
            actions.user.hud_add_log('success', 'Mic and eye tracking enabled')
            actions.user.hud_toggle_microphone()
            actions.user.mouse_wake()
        else:
            actions.user.hud_add_log('error', 'Mic and eye tracking disabled')
            actions.user.hud_toggle_microphone()
            actions.user.mouse_sleep()

    def open_specific_tab(browser: str, search_str: str):
        """This function requires that the searched for tab actually is open in the browser"""
        actions.user.engine_mimic("focus " + browser)
        actions.sleep("400ms")
        actions.key("ctrl-shift-a")
        actions.sleep("400ms")
        actions.auto_insert(search_str)
        actions.sleep("400ms")
        actions.key("enter")

    def open_browser_profile_switcher(browser: str):
        actions.user.engine_mimic("focus " + browser)
        actions.sleep("200ms")
        actions.key("ctrl-shift-m")
        actions.sleep("200ms")
        actions.key("shift-tab")
        actions.sleep("200ms")
        actions.key("enter")

    def gui_hold_modifier_toggle(flag: int, key_str: str):
        global modifier
        modifier = key_str
        if flag:
            gui_hold_modifier.show()
        else:
            gui_hold_modifier.hide()

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

    """
    def toggle_dictation_voice_command():
        #if the microphone has been disabled through talon_hud then we just start the dictation without putting Talon to sleep
        current_microphone = actions.sound.active_microphone()
        if current_microphone == "None":
            actions.user.start_stop_dictation()
        #if not we must take other actions before we start the dictation
        elif "command" in scope.get("mode"):
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
    """

    """
    def toggle_dictation_key_switch():
        #if the microphone has been disabled through talon_hud then we just start the dictation without putting Talon to sleep
        current_microphone = actions.sound.active_microphone()
        if current_microphone == "None":
            actions.user.start_stop_dictation()
        #if not we must take other actions before we start the dictation
        elif "command" in scope.get("mode"):
            actions.user.mouse_sleep()
            actions.speech.toggle()
            actions.user.start_stop_dictation()
        elif "dictation" in scope.get("mode"):
            actions.user.mouse_sleep()
            actions.speech.toggle()
            actions.user.start_stop_dictation()
        elif "user.power_mode" in scope.get("mode"):
            actions.user.mouse_sleep()
            actions.speech.toggle()
            actions.mode.disable("user.power_mode")
            actions.user.start_stop_dictation()
        elif "sleep" in scope.get("mode"):
            actions.user.start_stop_dictation()
            actions.speech.toggle()
            actions.user.mouse_wake()
    """

    def toggle_dictation_voice_command():
        current_microphone = actions.sound.active_microphone()
        if current_microphone == "None":
            #add some sleep time to make sure talon doesn't pick up any speech
            actions.sleep("500ms")
            actions.user.mouse_wake()
        else:
            actions.user.mouse_sleep()
            actions.user.toggle_talon_microphone()
            actions.user.start_stop_dictation()

    def toggle_dictation_key_switch():
        current_microphone = actions.sound.active_microphone()
        if current_microphone == "None":

            actions.user.mouse_wake()
            actions.user.toggle_talon_microphone()
            actions.user.start_stop_dictation()
        else:
            actions.user.mouse_sleep()
            actions.user.toggle_talon_microphone()
            actions.user.start_stop_dictation()

    def close_program():
        """Uses the OS built-in keyboard shortcut to close the program"""
        if app.platform == "windows":
            actions.key("alt-f4")
        elif app.platform == "mac":
            actions.key("cmd-q")
    
    #System wide leave huddle voice command
    def slack_system_wide_leave_huddle():
        actions.user.engine_mimic("focus slack")
        actions.sleep("300ms")
        actions.key("ctrl-shift-h")



    # Non working prototypes as of now
    def select_continous(run: int):

        gui_select.show()
        # Start selection

        # https://stackoverflow.com/questions/3969947/how-can-i-trigger-and-listen-for-events-in-python
        # self.actions.key(left:down).bind("left", actions.edit.extend_word_left())
        # self.actions.key(left:down).bind("right", actions.edit.extend_word_right())

        i = 0
        while run > 0:
            print("I will run forever")
            actions.sleep("75ms")
            # if actions.key(left:down)
            #     actions.edit.extend_word_left()
            #     actions.sleep("75ms")
            # elif actions.key(right:down)
            #     actions.edit.extend_word_right()
            #     actions.sleep("75ms")

    def select_continous_end():
        """sdf"""
        gui_select.hide()