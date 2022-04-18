#defines the commands that sleep/wake Talon
not mode: swedish
-
sleep [<phrase>]$:
    user.switcher_hide_running()
    user.history_disable()
    user.homophones_hide()
    user.help_hide()
    user.mouse_sleep()
    speech.disable()
    user.engine_sleep()

^wake up$: speech.enable()
