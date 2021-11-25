app: windows_explorer
app: windows_file_browser
-
tag(): user.file_manager
^go <user.letter>$: user.file_manager_open_volume("{letter}:")
go app data: user.file_manager_open_directory("%AppData%")
go program files: user.file_manager_open_directory("%programfiles%")
go this pc:
    user.file_manager_open_volume("C:")
    sleep(250ms)
    user.file_manager_open_parent()
go torrents: user.file_manager_open_directory("D:\Torrents\\")
