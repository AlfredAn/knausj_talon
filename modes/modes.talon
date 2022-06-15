not mode: sleep
and not mode: swedish
-
^dictation mode$:
    user.clear_modes()
    mode.enable("dictation")

^(command | come on) mode$:
    user.clear_modes()
    mode.enable("command")

^mixed mode$:
    user.clear_modes()
    mode.enable("command")
    mode.enable("dictation")
