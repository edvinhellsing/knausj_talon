import time
from talon import Module, Context, actions, cron

mod = Module()

current_state = [False]
last_state = [False]
continuous_firing = [False]
has_fired = [False]


#fires call down and call up only once
# def on_interval():
#     for key in range(4):
#         if current_state[key] != last_state[key]:
#             last_state[key] = current_state[key]
#             # Key is pressed downi
#             if current_state[key]:
#                 call_down(key)
#             # Key is released
#             else:
#                 last_state[key] = current_state[key]
#                 call_up(key)


#fires continuously if continuous_firing is set to true and then calls call_up() once when the key is released

def on_interval():
    for key in range(1):
        # Key is pressed down
        if (current_state[key]) and (continuous_firing[key] == False) and (has_fired[key] == False):
            last_state[key] = True
            has_fired[key] = True
            call_down(key)
        elif (current_state[key]) and (continuous_firing[key] == True):
            last_state[key] = True
            call_down(key)
            actions.sleep("100ms")
        # Key is released
        elif (current_state[key] == False) and (last_state[key] == True):
            last_state[key] = False
            has_fired[key] = False
            call_up(key)


cron.interval("10ms", on_interval)


@mod.action_class
class Actions:
    def key_down(key: int):
        """Key down event"""
        current_state[key] = True

    def key_up(key: int):
        """Key up event"""
        current_state[key] = False
    
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
        actions.core.repeat_command(1)

    def key_selected_up():
        pass


def call_down(key: int):
    if key == 0:
        actions.user.key_selected_down()


def call_up(key: int):
    if key == 0:
        actions.user.key_selected_up()

   