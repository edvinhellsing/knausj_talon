from talon import Module, Context

mod = Module()
ctx = Context()

mod.list("power_mode_alphabet", desc="Alphabet to use when in power mode")

ctx.lists["self.power_mode_alphabet"] = {
    "a": "a",
    "b": "b",
    "c": "c",
    "d": "d",
    "e": "e",
    "f": "f",
    "g": "g",
    "h": "h",
    "i": "i",
    "j": "j",
    "k": "k",
    "l": "l",
    "m": "m",
    "n": "n",
    "o": "o",
    "p": "p",
    "cue": "q",
    "r": "r",
    "s": "s",
    "tee": "t",
    "u": "u",
    "v": "v",
    "w": "w",
    "x": "x",
    "y": "y",
    "z": "z",
    "onyx": "å",
    "elk": "ä",
    "eagle": "ö",
}

#default_alphabet_dictate = "air b c d each f g h i j k l m n o p q r s tee u vest whale x yank zip".split(
#    " "
#)