app: windows_explorer
app: windows_file_browser
-
tag(): user.file_manager
go this pc:
    user.file_manager_open_volume("C:")
    sleep(250ms)
    user.file_manager_open_parent()
