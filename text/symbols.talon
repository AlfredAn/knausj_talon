ellipsis: "..."
spamma: ", "
nanna:
    ","
    key(enter)
spolon: ": "
nolon:
    ":"
    key(enter)
double dash: "--"
triple quote: "'''"
(triple grave | triple back tick | gravy):
    insert("```")
(dot dot | dotdot): ".."
ellipses: "..."
arrow: "->"
dub arrow: "=>"
new line: "\\n"
carriage return: "\\r"
line feed: "\\r\\n"
empty string: user.insert_between('"', '"')
empty escaped string: user.insert_between('\\"', '\\"')
empty prime string: user.insert_between("'", "'")
empty escaped prime string: user.insert_between("\\'", "\\'")
inside bears: user.insert_between("(", ")")
inside squares: user.insert_between("[", "]")
inside braces: user.insert_between("{", "}")
inside angles: user.insert_between("<", ">")
inside percent: user.insert_between("%", "%")
inside primes: user.insert_between("'", "'")
inside quotes: user.insert_between('"', '"')
inside (graves | back ticks): user.insert_between("`", "`")
inside pipes: user.insert_between("|", "|")
angle that:
    text = edit.selected_text()
    user.paste("<{text}>")
square that:
    text = edit.selected_text()
    user.paste("[{text}]")
brace that:
    text = edit.selected_text()
    user.paste("{{{text}}}")
bear that:
    text = edit.selected_text()
    user.paste("({text})")
percent that:
    text = edit.selected_text()
    user.paste("%{text}%")
quote that:
    text = edit.selected_text()
    user.paste('"{text}"')
prime that:
    text = edit.selected_text()
    user.paste("'{text}'")
(grave | back tick) that:
    text = edit.selected_text()
    user.paste('`{text}`')
