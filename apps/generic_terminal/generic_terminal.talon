tag: terminal
-
# tags should be activated for each specific terminal in the respective talon file

lisa:
    user.terminal_list_directories()
lisa all:
    user.terminal_list_all_directories()
katie [<user.text>]: user.terminal_change_directory(text or "")
katie root: user.terminal_change_directory_root()
go <user.system_path>: insert("cd \"{system_path}\"\n")
clear screen: user.terminal_clear_screen()
run last: user.terminal_run_last()
rerun [<user.text>]: user.terminal_rerun_search(text or "")
rerun search: user.terminal_rerun_search("")
kill all: user.terminal_kill_all()

copy paste:
    edit.copy()
    sleep(50ms)
    edit.paste()

pip: insert("pip ")
pip install: insert("pip install ")

sage: insert("ssh ")
sage pi: insert("ssh pi ")
sage pi two: insert("ssh pi2 ")
sage server: insert("ssh server ")
sage router: insert("ssh router ")

python: insert("python ")
python three: insert("python3 ")

choco: insert("choco ")

git: insert("git ")

cargo: insert("cargo ")
cargo build: insert("cargo build\n")
cargo run: insert("cargo run\n")

rustup: insert("rustup ")

