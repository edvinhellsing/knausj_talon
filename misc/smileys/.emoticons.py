from talon import Module, Context

mod = Module()
ctx = Context()

mod.list("emoticon2", desc="List of emoticons")

ctx.lists["self.emoticon2"] = {
    "smile": ":-)",
    "wink": ";-)",
    "sad": ":-(",
    "unsure": ":/",
    "grin": ":D",
    "gasp": ":o",
    "tongue": ":P",
}
