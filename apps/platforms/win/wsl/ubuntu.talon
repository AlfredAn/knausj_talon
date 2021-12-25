app: ubuntu
app: windows_terminal
and win.title: /Ubuntu/
-
tag(): terminal
tag(): user.file_manager
tag(): user.generic_unix_shell
tag(): user.git
tag(): user.kubectl

^go <user.letter>$: user.file_manager_open_volume("/mnt/{letter}")

sudo: insert("sudo ")
apt: insert("apt ")
apt install: insert("apt install ")
apt update: insert("apt update ")
apt upgrade: insert("apt upgrade ")
apt list: insert("apt list ")
(ssh | s s h): insert("ssh ")
python: insert("python ")
python three: insert("python3 ")
v env | venv: insert("venv")
flask: insert("flask ")
flask run: insert("flask run ")
systemctl: insert("systemctl ")
nano: insert("nano ")
export flask app: insert("export FLASK_APP=")
etcetera: insert("etc")
nginx: insert("nginx ")

paste it: user.insert_clipboard()
