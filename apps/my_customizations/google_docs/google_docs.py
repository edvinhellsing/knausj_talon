from talon import Module, actions, Context, app


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


"""Comment out this part as it currently doesn't seem to work using Google's own dictation for some reason
ctx_native_dictation.tags = ["user.docs"]

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