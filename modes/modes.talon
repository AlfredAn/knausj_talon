not mode: sleep
and not mode: swedish
-
^dictation mode$:
    mode.disable("sleep")
    mode.disable("command")
    mode.disable("user.pop")
    mode.enable("dictation")
    user.code_clear_language_mode()
    mode.disable("user.gdb")
^command mode$:
    mode.disable("sleep")
    mode.disable("dictation")
    mode.disable("user.pop")
    mode.enable("command")
