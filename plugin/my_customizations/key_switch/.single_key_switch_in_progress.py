import time
from talon import Module, Context, actions, cron

mod = Module()

current_state = False
last_state = False
continuous_firing = False
has_fired = False


#fires continuously if continuous_firing is set to true and then calls call_up() once when the key is released
def on_interval():
    global current_state
    global last_state
    global continuous_firing
    global has_fired
    # Key is pressed down
    if current_state and (continuous_firing == False) and (has_fired == False):
        last_state = True
        has_fired = True
        call_down()
    elif current_state and continuous_firing:
        last_state = True
        call_down()
        actions.sleep("100ms")
    # Key is released
    elif (current_state == False) and last_state:
        last_state = False
        has_fired = False
        call_up()

def call_up():
    actions.user.key_selected_up()

def call_down():
    actions.user.key_selected_down()

cron.interval("10ms", on_interval)


@mod.action_class
class Actions:
    def key_state_down():
        """Key down event"""
        current_state = True

    def key_state_up():
        """Key up event"""
        current_state = False
    
    def key_selected_down():
        """sdf"""

    def key_selected_up():
        """sdf"""


# Default implementation
ctx = Context()

#test actions
#actions.user.play_pause()
#actions.user.stop_scroll()

@ctx.action_class("user")
class UserActions:
    def key_selected_down():
        actions.speech.disable()
        actions.key("super-h")

    def key_selected_up():
        actions.key("super-h")
        actions.user.talon_mode()
   