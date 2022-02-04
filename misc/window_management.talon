window (new|open): app.window_open()
window next: app.window_next()
window last: app.window_previous()
window close: app.window_close()
focus <user.running_applications>$: user.switcher_focus(running_applications)
# following only works on windows. Can't figure out how to make it work for mac. No idea what the equivalent for linux would be.
focus$: user.switcher_menu()
running list: user.switcher_toggle_running()
launch <user.launch_applications>$: user.switcher_launch(launch_applications)
running close: user.switcher_hide_running()

snap <user.window_snap_position>: user.snap_window(window_snap_position)
snap next [screen]: user.move_window_next_screen()
snap last [screen]: user.move_window_previous_screen()
snap screen <number>: user.move_window_to_screen(number)
snap <user.running_applications> <user.window_snap_position>:
    user.snap_app(running_applications, window_snap_position)
snap <user.running_applications> [screen] <number>:
    user.move_app_to_screen(running_applications, number)

launch cura [arachne]: user.switcher_launch("C:\\Program Files\\Ultimaker Cura Arachne_engine_beta_2 99.10.0\\Cura.exe")
launch vscode: user.switcher_launch("C:\\Users\\Alfred\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
launch cadquery [editor]:
    user.switcher_launch("Microsoft.AutoGenerated.{{EF7FDCBC-680F-8861-0117-A16F61CE82F3}}")
    sleep(3)
    insert("cq-editor\n")
launch super slicer: user.switcher_launch("C:\\Users\\Alfred\\AppData\\Roaming\\SuperSlicer\\run.bat")
launch dolphin: user.switcher_launch("C:\\Users\\Alfred\\programs\\Dolphin-x64\\Dolphin.exe")
launch GlovePIE: user.switcher_launch("C:\\Users\\Alfred\\programs\\GlovePIE\\GlovePIE-0.45\\PIEFree.exe")
