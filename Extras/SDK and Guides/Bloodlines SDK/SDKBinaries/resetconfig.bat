@echo off
setlocal ENABLEEXTENSIONS
msgbox.exe Bloodlines SDK will be reset to the initial state and all user configurations (except content) will be deleted. Are you sure you want to continue? /c:Important Info /t:MB_YESNO,MB_ICONWARNING
if "%ErrorLevel%"=="7" exit

taskkill /f /im "sdklauncher.exe"
if exist "GameCfg.ini" del /a /q "GameCfg.ini"
call "start_sdk.bat" -int
exit
