from talon import Module, actions, Context, imgui


@imgui.open(x=700, y=0)
def gui_select(gui: imgui.GUI):
    gui.text(f"Select mode:")
    gui.line()
    if gui.button("End selection [stop selection]"):
        actions.user.select_continous(0)


mod = Module()

@mod.action_class
class Actions:
    def repeat_slowly(rep: int):
        """Repeats the command rep times with wait times in between each repetition"""

    def select_continous(run: int):
        """sdf"""

    def select_continous_end():
        """sdf"""


ctx=Context()

@ctx.action_class("user")
class UserActions:
    def repeat_slowly(rep: int):
        """Repeats the command rep times with wait times in between each repetition"""
        for i in range(rep):
            actions.core.repeat_command(1)
            actions.sleep("150ms")

    # Non working prototypes as of now
    def select_continous(run: int):
        """sdf"""

        gui_select.show()
        # Start selection

        # https://stackoverflow.com/questions/3969947/how-can-i-trigger-and-listen-for-events-in-python
        # self.actions.key(left:down).bind("left", actions.edit.extend_word_left())
        # self.actions.key(left:down).bind("right", actions.edit.extend_word_right())

        i = 0
        while run > 0:
            print("I will run forever")
            actions.sleep("75ms")
            # if actions.key(left:down)
            #     actions.edit.extend_word_left()
            #     actions.sleep("75ms")
            # elif actions.key(right:down)
            #     actions.edit.extend_word_right()
            #     actions.sleep("75ms")

    def select_continous_end():
        """sdf"""
        gui_select.hide()