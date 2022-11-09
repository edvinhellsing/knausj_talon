from talon import Module, actions, Context, app, scope


# mod = Module()

# @mod.action_class
# class Actions:
#     def docs_start_stop_dictation():
#         """Start native dictation on both Windows and macOS"""


ctx_native_dictation=Context()
ctx_native_dictation.matches = r"""
os: windows
os: linux
tag: browser
browser.host: docs.google.com
"""

ctx_native_dictation.tags = ["user.docs"]

"""
#Comment out this part as it currently doesn't seem to work using Google's own dictation for some reason
@ctx_native_dictation.action_class("user")
class NativeDictationActions:
    def start_stop_dictation():
        if app.platform == "windows":
            actions.key("ctrl-shift-s")
        elif app.platform == "mac":
            actions.key("cmd-shift-s")
        #https://www.reddit.com/r/firefox/comments/w7tztb/ctrlshifts_on_google_translate_is_hijacked_by/
        #To make it work in Firefox small alterations need to be done in Firefox itself
        #Open about:config from your address bar
        #Set extensions.screenshots.disabled to true
"""

@ctx_native_dictation.action_class("user")
class NativeDictationActions:
    def toggle_dictation_voice_command():
        current_microphone = actions.sound.active_microphone()
        if "command" in scope.get("mode"):
            if current_microphone == "None":
                actions.user.toggle_talon_microphone()
            actions.user.mouse_sleep()
            actions.user.engine_mimic("dictation mode")
        elif "user.power_mode" in scope.get("mode"):
            if current_microphone == "None":
                actions.user.toggle_talon_microphone()
            actions.user.mouse_sleep()
            actions.user.engine_mimic("dictation mode")
        elif "dictation" in scope.get("mode"):
            #Currently power mode is not supported, need to utilize a stack to know which mode to go back to
            actions.user.engine_mimic("command mode")
            actions.user.mouse_wake()

        # current_microphone = actions.sound.active_microphone()
        # if current_microphone == "None":
        #     actions.user.engine_mimic("command mode")
        #     actions.user.mouse_wake()
        # else:
        #     actions.user.mouse_sleep()
        #     actions.user.engine_mimic("dictation mode")
        #     actions.user.toggle_talon_microphone()
        #     actions.user.start_stop_dictation()

    def toggle_dictation_key_switch():
        current_microphone = actions.sound.active_microphone()
        if "command" in scope.get("mode"):
            if current_microphone == "None":
                actions.user.toggle_talon_microphone()
            actions.user.mouse_sleep()
            actions.user.engine_mimic("dictation mode")
        elif "user.power_mode" in scope.get("mode"):
            if current_microphone == "None":
                actions.user.toggle_talon_microphone()
            actions.user.mouse_sleep()
            actions.user.engine_mimic("dictation mode")
        elif "dictation" in scope.get("mode"):
            #Currently power mode is not supported, need to utilize a stack to know which mode to go back to
            actions.user.engine_mimic("command mode")
            actions.user.mouse_wake()