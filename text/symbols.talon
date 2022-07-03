ellipsis: "..."
spamma: ", "
nanna:
    ","
    key(enter)
spolon: ": "
nolon:
    ":"
    key(enter)
question [mark]: "?"
double dash: "--"
triple quote: "'''"
(triple grave | triple back tick | gravy):
    insert("```")
(dot dot | dotdot): ".."
ellipses: "..."
plus: "+"
arrow: "->"
dub arrow: "=>"
new line: "\\n"
carriage return: "\\r"
line feed: "\\r\\n"
empty string:
    '""'
    key(left)
empty escaped string:
    '\\"\\"'
    key(left)
    key(left)
empty pie string:
    "''"
    key(left)
empty escaped pie string:
    "\\'\\'"
    key(left)
    key(left)
inside bears:
	insert("()")
	key(left)
inside squares:
	insert("[]")
	key(left)
inside braces:
	insert("{}")
	key(left)
inside angles:
    insert("<>")
    key(left)
inside percent:
	insert("%%")
	key(left)
inside primes:
	insert("''")
	key(left)
inside quotes:
    insert('""')
	key(left)
inside (graves | back ticks):
	insert("``")
	key(left)
inside pipes:
    insert("||")
    key(left)
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
