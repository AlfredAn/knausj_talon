from typing import Set, List

from talon import Module, Context, actions, app
import sys

default_alphabet = "air bat cap drum each fine gust harp spit jury crunch look made near orc pill quench red sing trap urge vest whale plex yank zip aurora antlion earth".split(
    " "
)
letters_string = "abcdefghijklmnopqrstuvwxyzåäö"

default_digits = "zero one two three four five six seven eight nine".split(" ")
numbers = [str(i) for i in range(10)]
default_f_digits = "one two three four five six seven eight nine ten eleven twelve".split(
    " "
)

mod = Module()
mod.list("letter", desc="The spoken phonetic alphabet")
mod.list("symbol_key", desc="All symbols from the keyboard")
mod.list("arrow_key", desc="All arrow keys")
mod.list("number_key", desc="All number keys")
mod.list("modifier_key", desc="All modifier keys")
mod.list("function_key", desc="All function keys")
mod.list("special_key", desc="All special keys")
mod.list("punctuation", desc="words for inserting punctuation into text")

modifier_list = [
    ("soup", "super"),
    ("cone", "ctrl"),
    ("alt", "alt"),
    ("shift", "shift"),
]

modifier_keys = {}
mods = "("
for i in range(0, len(modifier_list)):
    modifier_keys[modifier_list[i][0]] = modifier_list[i][1]
    if i > 0:
        mods += ")|"
    mods += f"({modifier_list[i][0]}"
    for j in range(i+1, len(modifier_list)):
        mods += f" [{modifier_list[j][0]}]"
mods += "))"

@mod.capture(rule=f"{mods}")
def modifiers(m) -> str:
    "One or more modifier keys"
    return "-".join(map(lambda x: modifier_keys[x], str(m).split(" ")))


@mod.capture(rule="{self.arrow_key}")
def arrow_key(m) -> str:
    "One directional arrow key"
    return m.arrow_key

def parse_arrow_keys(m: List[str]) -> str:
    result = []
    multiplier = 1
    for x in m:
        if x in ctx.lists["self.arrow_key"]:
            for i in range(multiplier):
                result.append(x)
            multiplier = 1
        else:
            multiplier = x
    return " ".join(result)

@mod.capture(rule="([<number_small>] <self.arrow_key>)+")
def arrow_keys(m) -> str:
    "One or more arrow keys separated by a space"
    return parse_arrow_keys(list(m))


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

@mod.capture(rule="[<self.modifiers>] <self.unmodified_key>")
def key(m) -> str:
    "A single key with optional modifiers"
    return str(m).replace(" ", "-")


@mod.capture(rule="<self.key>+")
def keys(m) -> str:
    "A sequence of one or more keys with optional modifiers"
    return " ".join(m.key_list)


@mod.capture(rule="{self.letter}+")
def letters(m) -> str:
    "Multiple letter keys"
    return "".join(m.letter_list)


ctx = Context()
ctx.lists["self.modifier_key"] = modifier_keys
alphabet = dict(zip(default_alphabet, letters_string))
ctx.lists["self.letter"] = alphabet

# `punctuation_words` is for words you want available BOTH in dictation and as
# key names in command mode. `symbol_key_words` is for key names that should be
# available in command mode, but NOT during dictation.
punctuation_words = {
    # TODO: I'm not sure why we need these, I think it has something to do with
    # Dragon. Possibly it has been fixed by later improvements to talon? -rntz
    "`": "`",
    ",": ",",  # <== these things
    "back tick": "`",
    "grave": "`",
    "comma": ",",
    "period": ".",
    "full stop": ".",
    "semicolon": ";",
    "colon": ":",
    "forward slash": "/",
    "question mark": "?",
    "exclamation mark": "!",
    "exclamation point": "!",
    "dollar sign": "$",
    "asterisk": "*",
    "hash sign": "#",
    "number sign": "#",
    "percent sign": "%",
    "at sign": "@",
    "and sign": "&",
    "ampersand": "&",
}
symbol_key_words = {
    "dot": ".",
    "point": ".",
    "single quote": "'",
    "apostrophe": "'",
    "L square": "[",
    "left square": "[",
    "square": "[",
    "R square": "]",
    "right square": "]",
    "slash": "/",
    "backslash": "\\",
    "minus": "-",
    "dash": "-",
    "equals": "=",
    "plus": "+",
    "tilde": "~",
    "bang": "!",
    "dollar": "$",
    "down score": "_",
    "under score": "_",
    "paren": "(",
    "L paren": "(",
    "left paren": "(",
    "R paren": ")",
    "right paren": ")",
    "unpair": ")",
    "unparen": ")",
    "brace": "{",
    "left brace": "{",
    "R brace": "}",
    "right brace": "}",
    "unbrace": "}",
    "angle": "<",
    "left angle": "<",
    "less than": "<",
    "rangle": ">",
    "R angle": ">",
    "right angle": ">",
    "greater than": ">",
    "unangle": ">",
    "star": "*",
    "pound": "#",
    "hash": "#",
    "percent": "%",
    "caret": "^",
    "amper": "&",
    "pipe": "|",
    "quote": '"',
    "dubquote": '"',
    "double quote": '"',
}

# make punctuation words also included in {user.symbol_keys}
symbol_key_words.update(punctuation_words)
ctx.lists["self.punctuation"] = punctuation_words
ctx.lists["self.symbol_key"] = symbol_key_words
ctx.lists["self.number_key"] = dict(zip(default_digits, numbers))
ctx.lists["self.arrow_key"] = {
    "down": "down",
    "left": "left",
    "right": "right",
    "up": "up",
}

simple_keys = [
    "enter",
    "escape",
    "insert",
    "pagedown",
    "pageup",
    "space",
    "delete",
    "backspace",
    "tab"
]

alternate_keys = {
    "page up": "pageup",
    "page down": "pagedown",
    "home key": "home",
    "end key": "end"
}
# mac apparently doesn't have the menu key.
if app.platform in ("windows", "linux"):
    alternate_keys["menu key"] = "menu"
    alternate_keys["print screen"] = "printscr"

special_keys = {k: k for k in simple_keys}
special_keys.update(alternate_keys)
ctx.lists["self.special_key"] = special_keys
ctx.lists["self.function_key"] = {
    f"Fun {default_f_digits[i]}": f"f{i + 1}" for i in range(12)
}


@mod.action_class
class Actions:
    def get_alphabet() -> dict:
        """Provides the alphabet dictionary"""
        return alphabet

