from talon import Module, actions, Context

ctx=Context()
ctx.matches = r"""
os: windows
os: linux
app: Notepad.exe
"""

#Added to make the tabs management work on the new Windows 11 notepad (which now support tabs).
ctx.tags = ["user.tabs"]