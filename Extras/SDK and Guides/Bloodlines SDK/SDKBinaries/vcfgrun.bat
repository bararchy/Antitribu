@echo off
setlocal ENABLEEXTENSIONS
set "PATH=%SystemRoot%\System32;%SystemRoot%;%SystemRoot%\System32\Wbem"
set "PATHEXT=.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC"
if "%~1"=="" exit

:: Translate Config
if exist "GameCfg.ini" (
	for %%m in ("GameCfg.ini") do (set "CfgSizePre=%%~zm")
	for /f "usebackq delims== tokens=1,*" %%a in ("GameCfg.ini") do (
		if /i "%%~a"=="GameDir" (
			set "GameDir=%%~b"
			echo "Configs"
			echo {
			echo 	"Games"
			echo 	{
			echo 		"Vampire: Bloodlines"
			echo 		{
			echo 			"GameDir"		"%%~b"
			echo 		}
			echo 	}
			echo 	"SDKVersion"		"5"
			echo }
		)> "GameCfg.tmp"
	)
) else (
	call "start_sdk.bat" -int
)

:RunVConfig
if "%ErrorLevel%"=="2" (
	if exist "FirstRun.ini" (
	del /a /q "FirstRun.ini")
	goto Finalize
)
reg delete "HKCU\Software\Troika\VampSdk" /v "GameDir" /f
vconfig.exe

:: ReTranslate Changes
for /f "usebackq tokens=1,*" %%a in ("GameCfg.tmp") do (
	if /i "%%~a"=="GameDir" (call :ProcessGameDir "%%~b")
)

:Finalize
del /a /q "GameCfg.tmp"
reg add "HKCU\Software\Tools\PackfileExplorer" /v "LastPath"  /t REG_SZ /d "%GameDir%" /f
for %%m in ("GameCfg.ini") do (if "%%~zm"=="%CfgSizePre%" exit)
MsgBox.exe Game directory changed to "%GameDir%". /c:Bloodlines SDK /t:MB_SYSTEMMODAL,MB_ICONINFORMATION
exit



::==============================================
:: Functions
::==============================================

:ProcessGameDir
	if not exist "%~1\dlls\*" (if not exist "%~1\models\scenery\*" (
	if not exist "%~1\pack*.vpk" (if not exist "%~1\materials\models\scenery\*" (
		MsgBox.exe Invalid game directory. Please, choose a correct one! /c:Bloodlines SDK - Error! /t:MB_SYSTEMMODAL,MB_ICONERROR,MB_OKCANCEL
		goto RunVConfig
		exit /b
	))))

	set "GameDir=%~1"
	pushd "%~1\.."
	set "GameRoot=%cd%"
	popd

	sfk.exe filter "GameCfg.ini" -where "GameExeDir=" -rep "|GameExeDir=*|GameExeDir=%GameRoot%|" -write -yes
	sfk.exe filter "GameCfg.ini" -where "GameExe=" -rep "|GameExe=*|GameExe=%GameRoot%\Vampire.exe|" -write -yes
	sfk.exe filter "GameCfg.ini" -where "BSPDir=" -rep "|BSPDir=*|BSPDir=%GameDir%\maps|" -write -yes
	sfk.exe filter "GameCfg.ini" -where "GameDir=" -rep "|GameDir=*|GameDir=%GameDir%|" -write -yes
exit /b
