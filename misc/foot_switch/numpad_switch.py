import time
from talon import Module, Context, actions, cron

mod = Module()
mod.tag("av")

#10 numpad keys
#refactor this later
current_state = [False, False, False, False, False, False, False, False, False, False]
last_state = [False, False, False, False, False, False, False, False, False, False]
continuous_firing = [False, False, True, False, False, False, False, False, True, False]
has_fired = [False, False, False, False, False, False, False, False, False, False]


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


# #fires continuously and then calls call_up only once
# def on_interval():
#     for key in range(4):
#         # Key is pressed down
#         if current_state[key]:
#             last_state[key] = True
#             call_down(key)
#         # Key is released
#         elif (current_state[key] == False) and (last_state[key] == True):
#             last_state[key] = False
#             call_up(key)


#fires continuously if continuous_firing is set to true and then calls call_up() once when the key is released
def on_interval():
    for key in range(10):
        # Key is pressed down
        if (current_state[key]) and (continuous_firing[key] == False) and (has_fired[key] == False):
            last_state[key] = True
            has_fired[key] = True
            call_down(key)
        elif (current_state[key]) and (continuous_firing[key] == True):
            last_state[key] = True
            call_down(key)
            actions.sleep("40ms")
        # Key is released
        elif (current_state[key] == False) and (last_state[key] == True):
            last_state[key] = False
            has_fired[key] = False
            call_up(key)


#the on_interval() below implementation below doesn't support call_up(key)
# def on_interval():
#     for key in range(4):
#         if current_state[key]:
#             # Key is pressed down
#             call_down(key)


cron.interval("10ms", on_interval)


@mod.action_class
class Actions:
    def keypad_down(key: int):
        """Keypad key down event"""
        current_state[key] = True

    def keypad_up(key: int):
        """Keypad key up event"""
        current_state[key] = False
    
    def keypad_0_down():
        """sdf"""

    def keypad_0_up():
        """sdf"""

    def keypad_1_down():
        """sdf"""

    def keypad_1_up():
        """sdf"""

    def keypad_2_down():
        """sdf"""

    def keypad_2_up():
        """sdf"""

    def keypad_3_down():
        """sdf"""

    def keypad_3_up():
        """sdf"""

    def keypad_4_down():
        """sdf"""

    def keypad_4_up():
        """sdf"""

    def keypad_5_down():
        """sdf"""

    def keypad_5_up():
        """sdf"""

    def keypad_6_down():
        """sdf"""

    def keypad_6_up():
        """sdf"""

    def keypad_7_down():
        """sdf"""

    def keypad_7_up():
        """sdf"""

    def keypad_8_down():
        """sdf"""

    def keypad_8_up():
        """sdf"""

    def keypad_9_down():
        """sdf"""

    def keypad_9_up():
        """sdf"""

# Default implementation
ctx = Context()


#test actions
#actions.user.play_pause()
#actions.user.stop_scroll()

@ctx.action_class("user")
class UserActions:
    def keypad_0_down():
        actions.user.engine_mimic("dictation mode")
        actions.key("super-h")

    def keypad_0_up():
        actions.key("super-h")
        actions.user.engine_mimic("command mode")

    def keypad_1_down():
        actions.key("super-h")

    def keypad_1_up():
        pass

    def keypad_2_down():
        actions.user.mouse_scroll_down()

    def keypad_2_up():
        actions.user.stop_scroll()

    def keypad_3_down():
        actions.core.repeat_command(1)

    def keypad_3_up():
        pass

    def keypad_4_down():
        pass

    def keypad_4_up():
        pass

    def keypad_5_down():
        pass

    def keypad_5_up():
        pass

    def keypad_6_down():
        pass

    def keypad_6_up():
        pass

    def keypad_7_down():
        pass

    def keypad_7_up():
        pass

    def keypad_8_down():
        actions.user.mouse_scroll_up()

    def keypad_8_up():
        actions.user.stop_scroll()

    def keypad_9_down():
        pass

    def keypad_9_up():
        pass


# Audio / Video conferencing
ctx_av = Context()
ctx_av.matches = r"""
tag: user.av
"""


@ctx_av.action_class("user")
class AvActions:
    def keypad_3_down():
        actions.user.mute_microphone()

    def keypad_3_up():
        actions.user.mute_microphone()


# Mouse zoom mode
ctx_zoom = Context()
ctx_zoom.matches = r"""
tag: user.zoom_mouse
"""


@ctx_zoom.action_class("user")
class ZoomActions:
    def keypad_0_down():
        actions.user.zoom_mouse_click("triple")

    def keypad_0_up():
        pass

    def keypad_1_down():
        actions.user.zoom_mouse_click("middle")

    def keypad_1_up():
        pass

    def keypad_2_down():
        actions.user.zoom_mouse_click("double")

    def keypad_2_up():
        pass

    def keypad_3_down():
        actions.user.zoom_mouse_click("right")

    def keypad_3_up():
        pass


def call_down(key: int):
    if key == 0:
        actions.user.keypad_0_down()
    elif key == 1:
        actions.user.keypad_1_down()
    elif key == 2:
        actions.user.keypad_2_down()
    elif key == 3:
        actions.user.keypad_3_down()
    elif key == 4:
        actions.user.keypad_4_down()
    elif key == 5:
        actions.user.keypad_5_down()
    elif key == 6:
        actions.user.keypad_6_down()
    elif key == 7:
        actions.user.keypad_7_down()
    elif key == 8:
        actions.user.keypad_8_down()
    elif key == 9:
        actions.user.keypad_9_down()


def call_up(key: int):
    if key == 0:
        actions.user.keypad_0_up()
    elif key == 1:
        actions.user.keypad_1_up()
    elif key == 2:
        actions.user.keypad_2_up()
    elif key == 3:
        actions.user.keypad_3_up()
    elif key == 4:
        actions.user.keypad_4_up()
    elif key == 5:
        actions.user.keypad_5_up()
    elif key == 6:
        actions.user.keypad_6_up()
    elif key == 7:
        actions.user.keypad_7_up()
    elif key == 8:
        actions.user.keypad_8_up()
    elif key == 9:
        actions.user.keypad_9_up()

   