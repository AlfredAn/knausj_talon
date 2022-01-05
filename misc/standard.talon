#(jay son | jason ): "json"
#(http | htp): "http"
#tls: "tls"
#M D five: "md5"
#word (regex | rejex): "regex"
#word queue: "queue"
#word eye: "eye"
#word iter: "iter"
#word no: "NULL"
#word cmd: "cmd"
#word dup: "dup"
#word shell: "shell".
zoom in: edit.zoom_in()
zoom out: edit.zoom_out()
scroll up: edit.page_up()
scroll down: edit.page_down()
copy it: edit.copy()
cut it: edit.cut()
paste it: edit.paste()
undo: edit.undo()
redo it: edit.redo()
paste match: edit.paste_match_style()
file save: edit.save()
wipe: key(backspace)    
padding: 
	insert("  ") 
	key(left)
slap: edit.line_insert_down()

