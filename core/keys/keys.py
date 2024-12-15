from talon import Context, Module, app

from ..user_settings import get_list_from_csv

#http://www.yougowords.com/start-with-e/1-syllables
#https://syllablewords.net/1-syllable-words-starting-with-o?page=1
#near <- why didn't near work?
#eel elk eagle
#onyx adder oesten
#spun
#urge is often misrecognized as args
#red is a color so better to use ram
#pink is a color so better to use perk
#each is often misrecognized as ice
#bat is often misrecognized as whale/dot/it/space and many more commands... Trying out `batch` and `bill` instead
#east is a little cumbersome to say, tryin `eat` instead
#batch -> bin
#urn -> urge (will remove the voice command `args`)
#urge -> earn (so one can say `ship earn` and get `U` and not `Earn`)
#eagle -> urge (as it resembles the sound of the letter better)
#bin is often misrecognized as bang (!)
#sun -> sit (sun is often misrecognized as one, home, end and words like it)
#ice -> ivy (ice is misinterpreted as space)
#eat -> each (now that we're using "ivy" instead of "ice" we can switch back to using "each" instead of "eat". The problem with "eat" is that it too closely resembles "it")
#odd -> orange/oak because odd is often misrecognized as one/word the/...
#urge -> urging -> eagle for the letter `ö`

# TODO: Perhaps modif alphabet in csv file
def setup_default_alphabet():
    """set up common default alphabet.

    no need to modify this here, change your alphabet using alphabet.csv"""
    initial_default_alphabet = "air batch cap drum east fine gust harp ice judge crunch look made net odd perk quench ram sun trap urn vest whale x yank zip onyx elk eagle".split() #JW: air bat cap drum each fine gust harp sit jury crunch look made near odd pit quench red sun trap urge vest whale plex yank zip onyx elk eagle
    initial_letters_string = "abcdefghijklmnopqrstuvwxyzåäö"
    initial_default_alphabet_dict = dict(
        zip(initial_default_alphabet, initial_letters_string)
    )

    return initial_default_alphabet_dict


alphabet_list = get_list_from_csv(
    "alphabet.csv", ("Letter", "Spoken Form"), setup_default_alphabet()
)

# used for number keys & function keys respectively
digits = "zero one two three four five six seven eight nine".split()
f_digits = "one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty".split()

# default_alphabet = "air batch cap drum east fine gust harp ice judge crunch look made net odd perk quench ram sun trap urn vest whale x yank zip onyx elk eagle".split(
#     " "
# )
# letters_string = "abcdefghijklmnopqrstuvwxyzåäö"

# default_digits = "zero one two three four five six seven eight nine".split(" ")
# numbers = [str(i) for i in range(10)]
# default_f_digits = (
#     "one two three four five six seven eight nine ten eleven twelve".split(" ")
# )

mod = Module()
mod.list("letter", desc="The spoken phonetic alphabet")
mod.list("symbol_key", desc="All symbols from the keyboard")
mod.list("arrow_key", desc="All arrow keys")
mod.list("number_key", desc="All number keys")
mod.list("modifier_key", desc="All modifier keys")
mod.list("function_key", desc="All function keys")
mod.list("special_key", desc="All special keys")
mod.list("punctuation", desc="words for inserting punctuation into text")

@mod.capture(rule="{self.modifier_key}+")
def modifiers(m) -> str:
    "One or more modifier keys"
    return "-".join(m.modifier_key_list)


@mod.capture(rule="{self.arrow_key}")
def arrow_key(m) -> str:
    "One directional arrow key"
    return m.arrow_key


@mod.capture(rule="<self.arrow_key>+")
def arrow_keys(m) -> str:
    "One or more arrow keys separated by a space"
    return str(m)


@mod.capture(rule="{self.number_key}")
def number_key(m) -> str:
    "One number key"
    return m.number_key


@mod.capture(rule="{self.letter}")
def letter(m) -> str:
    "One letter key"
    return m.letter


@mod.capture(rule="{self.special_key}")
def special_key(m) -> str:
    "One special key"
    return m.special_key


@mod.capture(rule="{self.symbol_key}")
def symbol_key(m) -> str:
    "One symbol key"
    return m.symbol_key


@mod.capture(rule="{self.function_key}")
def function_key(m) -> str:
    "One function key"
    return m.function_key


@mod.capture(rule="( <self.letter> | <self.number_key> | <self.symbol_key> )")
def any_alphanumeric_key(m) -> str:
    "any alphanumeric key"
    return str(m)


@mod.capture(
    rule="( <self.letter> | <self.number_key> | <self.symbol_key> "
    "| <self.arrow_key> | <self.function_key> | <self.special_key> )"
)
def unmodified_key(m) -> str:
    "A single key with no modifiers"
    return str(m)


@mod.capture(rule="{self.modifier_key}* <self.unmodified_key>")
def key(m) -> str:
    "A single key with optional modifiers"
    try:
        mods = m.modifier_key_list
    except AttributeError:
        mods = []
    return "-".join(mods + [m.unmodified_key])


@mod.capture(rule="<self.key>+")
def keys(m) -> str:
    "A sequence of one or more keys with optional modifiers"
    return " ".join(m.key_list)

@mod.capture(rule="{self.letter}+")
def letters(m) -> str:
    "Multiple letter keys"
    return "".join(m.letter_list)

ctx = Context()
modifier_keys = {
    # If you find 'alt' is often misrecognized, try using 'alter'.
    #"alt": "alt",  
    "control": "ctrl",  #'troll':   'ctrl',
    "shift": "shift",  #'sky':     'shift',
    "super": "super",
    #"win": "super", #win is often misrepresented as wheel so I'm opting out of this one
    #My additions
    'alt key': 'alt',
    'option': 'alt',
    'option key': 'alt',
    "control key": "ctrl",
    "shift key": "shift",
    #"win": "super", #win is often misrecognized as wheel
    'win key': 'super',
}
if app.platform == "mac":
    modifier_keys["command"] = "cmd"
    modifier_keys["option"] = "alt"
ctx.lists["self.modifier_key"] = modifier_keys
ctx.lists["self.letter"] = alphabet_list

# `punctuation_words` is for words you want available BOTH in dictation and as key names in command mode.
# `symbol_key_words` is for key names that should be available in command mode, but NOT during dictation.
punctuation_words = {
    # TODO: I'm not sure why we need these, I think it has something to do with
    # Dragon. Possibly it has been fixed by later improvements to talon? -rntz
    "`": "`",
    ",": ",",  # <== these things
    "back tick": "`",
    "comma": ",",
    # Workaround for issue with conformer b-series; see #946
    "coma": ",",
    "period": ".",
    "full stop": ".",
    "semicolon": ";",
    "colon": ":",
    "forward slash": "/",
    "question mark": "?",
    "exclamation mark": "!",
    "exclamation": "!",
    #"exclamation point": "!",
    "asterisk": "*",
    "hash sign": "#",
    "number sign": "#",
    "percent sign": "%",
    "at sign": "@",
    "and sign": "&",
    "ampersand": "&",
    "amper sign": "&",
    # Currencies
    "dollar sign": "$",
    "pound sign": "£",
    "hyphen": "-",
    "L paren": "(",
    "left paren": "(",
    "R paren": ")",
    "right paren": ")",

    #My additions
    "dash sign": "-",
    "euro sign": "€",
}
symbol_key_words = {
    "dot": ".",
    "point": ".",
    "quote": "'",
    "quest": "?",    
    "question": "?",
    "apostrophe": "'",
    "L square": "[",
    "left square": "[",
    "brack": "[",
    "bracket": "[",
    "left bracket": "[",
    "square": "[",
    "R square": "]",
    "right square": "]",
    "r brack": "]",
    "r bracket": "]",
    "right bracket": "]",
    "slash": "/",
    "backslash": "\\",
    "minus": "-",
    "dash": "-",
    "emdash": "–",
    "equals": "=",
    "plus": "+",
    "grave": "`",
    "tilde": "~",
    "bang": "!",
    "exclamation": "!",
    "down score": "_",
    "underscore": "_",
    "paren": "(",
    "brace": "{",
    "left brace": "{",
    "curly": "{",
    "left curly": "{",    
    #"curly bracket": "{",
    #"left curly bracket": "{",
    "r brace": "}",
    "right brace": "}",
    "r curly": "}",
    "right curly": "}",
    #"r curly bracket": "}",
    #"right curly bracket": "}",
    "angle": "<",
    "left angle": "<",
    #"less than": "<",
    "rangle": ">",
    "R angle": ">",
    "right angle": ">",
    #"greater than": ">",
    #"star": "*",
    #"hash": "#", #removed this one as it was often misinterpreted as `dash`
    "percent": "%",
    #"caret": "^",
    "caret sign": "^",
    #"amper": "&",
    "pipe": "|",
    "dub quote": '"',
    "double quote": '"',
    # Currencies
    #"dollar": "$",
    #"pound": "£",

    #My additions
    #"semistack": ";",
    #"stack": ":",
    #"drip": ",",
    "vest ten": "?",
    #"vest one": "?",
    "vest ram": "?",
    "and dash": "–",
    "em dash": "—",
}

# make punctuation words also included in {user.symbol_keys}
symbol_key_words.update(punctuation_words)
ctx.lists["self.punctuation"] = punctuation_words
ctx.lists["self.symbol_key"] = symbol_key_words
ctx.lists["self.number_key"] = {name: str(i) for i, name in enumerate(digits)}
ctx.lists["self.arrow_key"] = {
    "down": "down",
    "left": "left",
    "right": "right",
    "up": "up",
}

simple_keys = [
    #"end",
    "enter",
    "escape",
    "home",
    "insert",
    "pagedown",
    "pageup",
    "space",
    #"tab",
]

alternate_keys = {
    #"wipe": "backspace",
    #"delete": "backspace",
    #'junk': 'backspace',
    #"forward delete": "delete",
    "page up": "pageup",
    "page down": "pagedown",

    #My additions
    "void": "space",
    "blank": "space",
    "slap": "enter",
    "clear": "backspace",
    #"chuck": "backspace",
    "delete": "delete",
    "end key": "end",
    "home key": "home",
    "tab key": "tab",
}
# mac apparently doesn't have the menu key.
if app.platform in ("windows", "linux"):
    alternate_keys["menu key"] = "menu"
    alternate_keys["print screen"] = "printscr"

special_keys = {k: k for k in simple_keys}
special_keys.update(alternate_keys)
ctx.lists["self.special_key"] = special_keys
ctx.lists["self.function_key"] = {
    f"F {name}": f"f{i}" for i, name in enumerate(f_digits, start=1)
}