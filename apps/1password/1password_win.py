from talon import Context, actions

ctx = Context()

# i don't see a need to restrict the app here, this just defines the actions
# each app can support appropriate voice commands as needed
# the below are for 1password, redefine as needed
ctx.matches = r"""
os: windows
app: chrome
app: microsoft_edge
app: firefox
app: opera_browser
app: brave
app: bitwarden
"""


#https://bitwarden.com/help/keyboard-shortcuts/
@ctx.action_class("user")
class UserActions:
    def password_fill():
        #Bitwarden
        actions.key("ctrl-shift-Y")

    def password_show():
        actions.key("alt-ctrl-\\\\")

    def password_new():
        #Bitwarden
        actions.key("ctrl-shift-9")
        actions.user.hud_add_log('success', 'Generated password copied to clipboard')

    def password_duplicate():
        actions.key("ctrl-d")

    def password_edit():
        actions.key("ctrl-e")

    def password_delete():
        actions.key("ctrl-delete")
