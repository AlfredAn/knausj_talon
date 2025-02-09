from typing import Set, List

from talon import Context, Module, actions, app
import sys

default_alphabet = "arm bat cap drum each fine gust harp spit jury crunch look made near orc pill quench red sing trap urge vest whale plex yank zip aurora antlion earth".split(
    " "
)
letters_string = "abcdefghijklmnopqrstuvwxyzåäö"

default_digits = "zero one two three four five six seven eight nine".split(" ")
numbers = [str(i) for i in range(10)]
default_f_digits = (
    "one two three four five six seven eight nine ten eleven twelve".split(" ")
)
ext_f_digits = "thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty".split(" ")
ext_f_digits.extend(["twenty one", "twenty two", "twenty three", "twenty four"]) 

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

# `punctuation_words` is for words you want available BOTH in dictation and as key names in command mode.
# `symbol_key_words` is for key names that should be available in command mode, but NOT during dictation.
punctuation_words = {
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
    "asterisk": "*",
    "hash sign": "#",
    "number sign": "#",
    "percent sign": "%",
    "at sign": "@",
    "and sign": "&",
    "ampersand": "&",
    # Currencies
    "dollar sign": "$",
    "pound sign": "£",
}
symbol_key_words = {
    "point": ".",
    "prime": "'",
    "quote": "'",
    "question": "?",
    "square": "[",
    "rare": "]",
    "slash": "/",
    "backer": "\\",
    "minus": "-",
    "dash": "-",
    "equals": "=",
    "plus": "+",
    "tilde": "~",
    "bang": "!",
    "underscore": "_",
    "bear": "(",
    "apple": ")",
    "brace": "{",
    "nose": "}",
    "angle": "<",
    "less than": "<",
    "rangle": ">",
    "more than": ">",
    "greater than": ">",
    "star": "*",
    "hash": "#",
    "percent": "%",
    "caret": "^",
    "amper": "&",
    "pipe": "|",
    "quote": '"',

    # Currencies
    "dollar": "$",
    "pound": "£",
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
    "end key": "end",
    "jump": "tab"
}
# mac apparently doesn't have the menu key.
if app.platform in ("windows", "linux"):
    alternate_keys["menu key"] = "menu"
    alternate_keys["print screen"] = "printscr"

special_keys = {k: k for k in simple_keys}
special_keys.update(alternate_keys)
ctx.lists["self.special_key"] = special_keys

fk = { f"f {default_f_digits[i]}": f"f{i + 1}" for i in range(12) }
fk.update({ f"fun {ext_f_digits[i]}": f"f{i + 13}" for i in range(12) })

ctx.lists["self.function_key"] = fk


@mod.action_class
class Actions:
    def move_cursor(s: str):
        """Given a sequence of directions, eg. 'left left up', moves the cursor accordingly using edit.{left,right,up,down}."""
        for d in s.split():
            if d in ("left", "right", "up", "down"):
                getattr(actions.edit, d)()
            else:
                raise RuntimeError(f"invalid arrow key: {d}")
