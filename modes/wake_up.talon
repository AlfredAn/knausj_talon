#defines the commands that sleep/wake Talon
mode: all
-
^sleep all$:
    user.switcher_hide_running()
    user.history_disable()
    user.homophones_hide()
    user.help_hide()
    user.mouse_sleep()
    speech.disable()
    user.engine_sleep()
sleep+ yes*$: speech.disable()
^(wake up)+$: speech.enable()
