ellipsis: "..."
spamma: ", "
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
inside pear:
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
inside pie quotes:
	insert("''")
	key(left)
inside quotes:
    insert('""')
	key(left)
inside (graves | back ticks):
	insert("``")
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
pear that:
    text = edit.selected_text()
    user.paste("({text})")
percent that:
    text = edit.selected_text()
    user.paste("%{text}%")
quote that:
    text = edit.selected_text()
    user.paste('"{text}"')
pie quote that:
    text = edit.selected_text()
    user.paste("'{text}'")
(grave | back tick) that:
    text = edit.selected_text()
    user.paste('`{text}`')
