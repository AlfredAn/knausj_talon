app: ubuntu
app: windows_terminal
and win.title: /Ubuntu/
-
tag(): terminal
tag(): user.file_manager
tag(): user.generic_unix_shell
tag(): user.git
tag(): user.kubectl

sudo: insert("sudo ")
apt: insert("apt ")
apt install: insert("apt install ")
apt update: insert("apt update ")
apt upgrade: insert("apt upgrade ")
apt list: insert("apt list ")
v env | venv: insert("venv")
flask: insert("flask ")
flask run: insert("flask run ")
systemctl: insert("systemctl ")
nano: insert("nano ")
export flask app: insert("export FLASK_APP=")
etcetera: insert("etc")
nginx: insert("nginx ")
docker: insert("docker ")
systemctl: insert("systemctl ")
systemctl status: insert("systemctl status ")
systemctl start: insert("systemctl start ")
systemctl restart: insert("systemctl restart ")
systemctl stop: insert("systemctl stop ")
systemctl enable: insert("systemctl enable ")
systemctl disable: insert("systemctl disable ")
systemctl daemon reload: insert("systemctl daemon-reload ")
my sequel: insert("mysql ")
ffmpeg: insert("ffmpeg ")

paste it: user.insert_clipboard()
