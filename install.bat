@echo off
set "source_zip=.\kosher_pc.zip"
set "destination_path=C:\kosher_pc"
set "shortcut_name=kosher_pc.lnk"

powershell -command "Expand-Archive -Path '%source_zip%' -DestinationPath '%destination_path%'"

set "shortcut_target=%destination_path%"
set "shortcut_location=%USERPROFILE%\Desktop\%shortcut_name%"
powershell -Command "$WScriptShell = New-Object -ComObject WScript.Shell; $Shortcut = $WScriptShell.CreateShortcut('%shortcut_location%'); $Shortcut.TargetPath = '%shortcut_target%'; $Shortcut.Save()"
