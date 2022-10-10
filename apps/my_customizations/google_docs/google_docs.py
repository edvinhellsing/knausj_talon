from talon import Module, actions, Context, app


# mod = Module()

# @mod.action_class
# class Actions:
#     def docs_start_stop_dictation():
#         """Start native docs dictation on both Windows and macOS"""


ctx_avc=Context()
ctx_avc.matches = r"""
os: windows
os: linux
tag: browser
browser.host: docs.google.com
"""

ctx_avc.tags = ["user.docs"]

@ctx_avc.action_class("user")
class DocsActions:
    def start_stop_dictation():
        if app.platform == "windows":
            actions.key("ctrl-shift-s")
        elif app.platform == "mac":
            actions.key("cmd-shift-s")