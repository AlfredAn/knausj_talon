# NOTE: to use these commands you will need to activate the tag below in whatever contexts you
# choose.
#
# do this in a separate .talon file or via python. for example, if you use windows terminal for
# wsl then you might do this:
#
#    os: windows
#    app: windows_terminal
#    -
#    tag(): user.wsl
#
# however, if you also use windows terminal for other things (powershell), you will want something
# more specific...like this:
#
#    os: windows
#    app: windows_terminal
#    title: /^WSL:/
#    -
#    tag(): user.wsl
#
# then, you will need to find a way to set the window title accordingly. for example, to match
# the title pattern above, you can set the prompt in your .bashrc file like this:
#
#    PS1="\[\e]0;${debian_chroot:+($debian_chroot)}WSL:${WSL_DISTRO_NAME} \u@\h: \w\a\]$PS1"
#
# ALSO: if you do populate your window title with your distro name, make sure the 'wsl_title_regex'
# value in wsl.py is set accordingly.
tag: user.wsl
-

tag(): terminal
tag(): user.file_manager
tag(): user.generic_unix_shell
tag(): user.git

^go <user.letter>$: user.file_manager_open_volume("/mnt/{letter}")

(wsl|weasel) reset path detection: user.wsl_reset_path_detection()
(wsl|weasel) speak: user.wsl_speak()

sudo: insert("sudo ")
apt: insert("apt ")
apt install: insert("apt install ")
apt update: insert("apt update ")
apt upgrade: insert("apt upgrade ")
apt list: insert("apt list ")
sage: insert("ssh ")
python: insert("python ")
python three: insert("python3 ")
v env | venv: insert("venv")
flask: insert("flask ")
flask run: insert("flask run ")
nano: insert("nano ")
export flask app: insert("export FLASK_APP=")
etcetera: insert("etc")
nginx: insert("nginx ")
docker: insert("docker ")
systemctl: insert("systemctl ")
systemctl status: insert("systemctl status ")
systemctl start: insert("systemctl start ")
systemctl stop: insert("systemctl stop ")
systemctl enable: insert("systemctl enable ")
systemctl disable: insert("systemctl disable ")
my sequel: insert("mysql ")

paste it: user.insert_clipboard()
