app: windows_explorer
app: windows_file_browser
-
tag(): user.file_manager
^go to <user.letter>$: user.file_manager_open_volume("{letter}:")
go to app data: user.file_manager_open_directory("%AppData%")
go to program files: user.file_manager_open_directory("%programfiles%")
