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

ctx_native_dictation.tags = ["user.docs"]

@ctx_native_dictation.action_class("user")
class NativeDictationActions:
    def start_stop_dictation():
        if app.platform == "windows":
            actions.key("ctrl-shift-s")
        elif app.platform == "mac":
            actions.key("cmd-shift-s")