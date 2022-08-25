from talon import Context, Module, actions

mod = Module()
ctx = Context()

mod.apps.opera_browser = """
os: windows
and app.name: opera.exe
os: windows
and app.name: Opera Internet Browser
os: windows
and app.exe: opera.exe
"""

ctx.matches = r"""
app: opera_browser
"""


@ctx.action_class("browser")
class BrowserActions:
    def go(url: str):
        actions.browser.focus_address()
        actions.sleep("50ms")
        actions.insert(url)
        actions.key("enter")
