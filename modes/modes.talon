not mode: sleep
and not mode: swedish
-
^dictation mode$:
    mode.disable("sleep")
    mode.disable("command")
    mode.disable("user.pop")
    mode.disable("user.chess")
    mode.disable("user.civ5")
    mode.enable("dictation")
    user.code_clear_language_mode()
    mode.disable("user.gdb")

^command mode$:
    mode.disable("sleep")
    mode.disable("dictation")
    mode.disable("user.pop")
    mode.disable("user.chess")
    mode.disable("user.civ5")
    mode.enable("command")

^mixed mode$:
    mode.disable("sleep")
    mode.disable("user.pop")
    mode.disable("user.chess")
    mode.disable("user.civ5")
    mode.enable("command")
    mode.enable("dictation")
