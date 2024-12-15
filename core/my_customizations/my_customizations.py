from talon import Module, Context, actions, imgui, scope
from talon_plugins import eye_mouse

#Below is for the navigation_text()
import re

#Below is for the talon_relaunch()
from talon import ui, app
import os

#import mouse.py file so I can reach the variable `eye_tracking`
from ...plugin.mouse.mouse import get_eye_tracking_variable
#from ...plugin.mouse.mouse import eye_tracking
#from plugin.mouse.mouse import eye_tracking
#from plugin.mouse.mouse import *
#from plugin.mouse import mouse


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
    def repeat_command_wrapper(rep: int):
        """Repeats the command `rep` times with wait times in between each repetition"""

    def toggle_talon_microphone():
        """Toggle the Talon microphone on/off using talon_HUD actions (please note: talon_HUD must be installed in the talon user folder for this function to work)"""

    def toggle_control_mouse():
        """Toggle the mouse on/off, using talon_HUD actions to control eye tracking and mouse together (please note: talon_HUD must be installed in the talon user folder for this function to work)"""


    def open_specific_tab(browser: str, search_str: str):
        """This function requires that the searched for tab actually is open in the browser"""

    def open_browser_profile_switcher(browser: str):
        """sdf"""

    def open_specific_profile(browser: str):
        """sdf"""

    def gui_hold_modifier_toggle(flag: int, key_str: str):
        """sdf"""

    def talon_relaunch():
        """Quit and relaunch the Talon app"""

    def toggle_talon_microphone():
        """Toggle the Talon microphone on/off using talon_HUD actions (please note: talon_HUD must be installed in the talon user folder for this function to work)"""

    def start_stop_dictation():
        """Start dictation on both Windows and macOS"""

    def toggle_dictation_voice_command():
        """Start dictation on both Windows and macOS using a voice command"""

    def toggle_dictation_key_switch():
        """Start dictation on both Windows and macOS using a physical key"""

    def close_program():
        """Uses the OS built-in keyboard shortcut to close the program"""

    def select_continous(run: int):
        """sdf"""

    def select_continous_end():
        """sdf"""
    
    def comment():
        """Comment out code in Visual Studio"""
    
    def uncomment():
        """Comment in code in Visual Studio"""
    
    def open_chrome_bookmarks():
        """Open bookmarks in Google Chrome on Windows"""
    
    def window():
        """Windows key / start"""

ctx=Context()

@ctx.action_class("user")
class UserActions:
    def repeat_command_wrapper(rep: int):
        """Repeats the command rep times with wait times in between each repetition"""
        for i in range(rep):
            actions.core.repeat_command(1)
            actions.sleep("200ms")
  
    def toggle_talon_microphone():
        current_microphone = actions.sound.active_microphone()

        if current_microphone == "None" and eye_mouse.tracker is not None and not eye_mouse.config.control_mouse and not "sleep" in scope.get("mode"):
            #https://github.com/chaosparrot/talon_hud/blob/master/CUSTOMIZATION.md#log-messages
            actions.user.hud_add_log('success', 'Mic and eye tracking enabled')
            actions.user.hud_toggle_microphone()
            actions.user.mouse_wake()
        elif current_microphone == "None" and eye_mouse.tracker is not None and eye_mouse.config.control_mouse and not "sleep" in scope.get("mode"):
            actions.user.hud_add_log('error', 'Mic and eye tracking disabled')
            actions.user.mouse_sleep()
        elif eye_mouse.tracker is not None and not eye_mouse.config.control_mouse and not "sleep" in scope.get("mode"):
            actions.user.hud_add_log('success', 'Eye tracking enabled')
            actions.user.mouse_wake()
        elif eye_mouse.tracker is not None and eye_mouse.config.control_mouse and not "sleep" in scope.get("mode"):
            actions.user.hud_add_log('error', 'Mic and eye tracking disabled')
            actions.user.hud_toggle_microphone()
            actions.user.mouse_sleep()
        
    def toggle_control_mouse():
        current_microphone = actions.sound.active_microphone()

        if current_microphone == "None":
            #https://github.com/chaosparrot/talon_hud/blob/master/CUSTOMIZATION.md#log-messages
            actions.user.hud_add_log('success', 'Mic enabled')
            actions.user.hud_toggle_microphone()
        elif eye_mouse.tracker is not None and eye_mouse.config.control_mouse:
            actions.user.hud_add_log('error', 'Eye tracking disabled')
            actions.user.mouse_sleep()
        else:
            actions.user.hud_add_log('error', 'Mic disabled')
            actions.user.hud_toggle_microphone()

    def open_specific_tab(browser: str, search_str: str):
        """This function requires that the searched for tab actually is open in the browser"""
        if actions.user.current_app(browser) == False:
            actions.user.switcher_focus(browser)
            actions.sleep("400ms")
            #Check that the browser was successfully opened
            if actions.user.current_app(browser) == False:
                #If not, return
                return
        #Using the browser's built-in keyboard shortcuts
        #actions.key("ctrl-shift-a")
        #actions.sleep("400ms")
        #actions.auto_insert(search_str)
        #actions.sleep("400ms")
        #actions.key("enter")
        #Using Rango commands
        actions.user.rango_command_without_target("focusTabByText", search_str)

    def open_browser_profile_switcher(browser: str):
        if actions.user.current_app(browser) == False:
            actions.user.switcher_focus(browser)
            actions.sleep("400ms")
            #Check that the browser was successfully opened
            if actions.user.current_app(browser) == False:
                #If not, return
                return
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
            actions.user.mouse_sleep()
            actions.user.hud_add_log('error', 'Eye tracking disabled')
            actions.user.hud_toggle_microphone()
            actions.user.hud_add_log('error', 'Mic disabled')
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

    """
    #If gaze control should be enabled when using the eye tracker
    def toggle_talon_microphone():
        current_microphone = actions.sound.active_microphone()
        if current_microphone == "None":
            #https://github.com/chaosparrot/talon_hud/blob/master/CUSTOMIZATION.md#log-messages
            actions.user.hud_add_log('success', 'ON') #Mic and eye tracking enabled
            actions.user.hud_toggle_microphone()
            actions.user.mouse_wake()
        elif not actions.tracking.control_enabled():
            actions.user.hud_add_log('success', 'ON') #Eye tracking enabled
            actions.user.mouse_wake()
        else:
            actions.user.hud_add_log('error', 'OFF') #Mic and eye tracking disabled
            actions.user.hud_toggle_microphone()
            actions.user.mouse_sleep()
    """
    """
    #If gaze control should be disabled when using the eye tracker, i.e. using hissing to activate gaze control
    def toggle_talon_microphone():
        current_microphone = actions.sound.active_microphone()
        eye_tracking = get_eye_tracking_variable()
        actions.print(eye_tracking)
        if current_microphone == "None":
            #https://github.com/chaosparrot/talon_hud/blob/master/CUSTOMIZATION.md#log-messages
            actions.user.hud_add_log('success', 'ON') #Mic and eye tracking enabled
            actions.user.hud_toggle_microphone()
            actions.tracking.control_toggle(True)
            actions.tracking.control_gaze_toggle(False)
        elif not actions.tracking.control_enabled():
            actions.user.hud_add_log('success', 'ON') #Eye tracking enabled
            actions.tracking.control_toggle(True)
            actions.tracking.control_gaze_toggle(False)
        else:
            actions.user.hud_add_log('error', 'OFF') #Mic and eye tracking disabled
            actions.user.hud_toggle_microphone()
            actions.user.mouse_sleep()    
    """

    def toggle_talon_microphone():
        current_microphone = actions.sound.active_microphone()
        eye_tracking = get_eye_tracking_variable()
        actions.print(current_microphone)
        actions.print(eye_tracking)
        actions.print(actions.tracking.control_enabled())
        if current_microphone == "None":
            #https://github.com/chaosparrot/talon_hud/blob/master/CUSTOMIZATION.md#log-messages
            actions.user.hud_add_log('success', 'ON') #Mic and eye tracking enabled
            actions.user.hud_toggle_microphone()
            if eye_tracking == "gaze control":
                actions.user.mouse_wake()
            elif eye_tracking == "hiss control":
                actions.tracking.control_toggle(True)
                actions.tracking.control_gaze_toggle(False)
        elif not actions.tracking.control_enabled(): #Eye tracking is currently disabled. Please note: one could end up here because the eye tracker is not connected.
            actions.user.hud_add_log('success', 'ON') #Eye tracking enabled
            if eye_tracking == "gaze control":
                actions.user.mouse_wake()
            elif eye_tracking == "hiss control":
                actions.tracking.control_toggle(True)
                actions.tracking.control_gaze_toggle(False)
        else:
            actions.user.hud_add_log('error', 'OFF') #Mic and eye tracking disabled
            actions.user.hud_toggle_microphone()
            actions.user.mouse_sleep()    


    def start_stop_dictation():
        """Start dictation on both Windows and macOS"""
        if app.platform == "windows":
            actions.key("super-h")
        elif app.platform == "mac":
            actions.key("ctrl")
            actions.sleep("10ms")
            actions.key("ctrl")

    """
    def toggle_dictation_voice_command():
        #if the microphone has been disabled through talon_hud then we just start the dictation without putting Talon to sleep
        current_microphone = actions.sound.active_microphone()
        if current_microphone == "None":
            actions.user.start_stop_dictation()
        #if not we must take other actions before we start the dictation
        elif "command" in scope.get("mode"):
            #actions.user.mouse_sleep()
            actions.speech.toggle()
            actions.user.start_stop_dictation()
        elif "user.power_mode" in scope.get("mode"):
            #actions.user.mouse_sleep()
            actions.speech.toggle()
            actions.mode.disable("user.power_mode")
            actions.user.start_stop_dictation()
        elif "sleep" in scope.get("mode"):
            #add some sleep time to make sure talon doesn't pick up any speech
            actions.sleep("500ms")
            actions.speech.toggle()
            #actions.user.mouse_wake()

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
        elif "sleep" in scope.get("mode"):
            actions.user.start_stop_dictation()
            actions.speech.toggle()
            actions.user.mouse_wake()

    def close_program():
        """Uses the OS built-in keyboard shortcut to close the program"""
        if app.platform == "windows":
            actions.key("alt-f4")
        elif app.platform == "mac":
            actions.key("cmd-q")
    
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

    # Non working prototype as of now
    def select_continous_end():
        """sdf"""
        gui_select.hide()
    
    def comment():
        """Comment out code in Visual Studio both Windows and macOS"""
        if app.platform == "windows":
            actions.key("ctrl-k-c")
        elif app.platform == "mac":
            actions.key("cmd-k-c")
    
    def uncomment():
        """Comment in code in Visual Studio both Windows and macOS"""
        if app.platform == "windows":
            actions.key("ctrl-k-u")
        elif app.platform == "mac":
            actions.key("cmd-k-u")
    
    def open_chrome_bookmarks():
        """Open bookmarks in Google Chrome Windows"""
        if app.platform == "windows":
            actions.key("ctrl-shift-o")
            actions.sleep("1000ms")
            actions.key("tab")
            actions.sleep("100ms")
            actions.key("tab")
            actions.sleep("100ms")
            actions.key("tab")
            actions.sleep("100ms")
            actions.key("tab")
        if app.platform == "mac":
            actions.key("cmd-alt-b")
            actions.sleep("1000ms")
            actions.key("tab")
            actions.sleep("100ms")
            actions.key("tab")
            actions.sleep("100ms")
            actions.key("tab")
    
    def window():
        if app.platform == "windows":
            actions.key("ctrl-esc")