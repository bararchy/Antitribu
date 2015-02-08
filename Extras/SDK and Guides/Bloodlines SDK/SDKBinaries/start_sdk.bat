@echo off
setlocal ENABLEEXTENSIONS
set "PATH=%SystemRoot%\System32;%SystemRoot%;%SystemRoot%\System32\Wbem"
set "PATHEXT=.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC"
if "%~1"=="" exit
title Bloodlines SDK launcher
pushd "%~dp0..\"

:: Variables
set "GameRoot=%cd%"
set "GameDir=%GameRoot%\Vampire"
set "ModDir=%GameRoot%\SDKContent\Vampire"
set "SDKRoot=%cd%\SDKBinaries"
set "WcRegistry=HKCU\Software\Troika\Hammer"
set "MapSrcDir=%GameRoot%\SDKContent\MapSrc"

:vproject
set "VPROJECT=%ModDir%"
reg add "HKCU\Environment" /v "VProject" /t REG_SZ /d "%ModDir%" /f
setx VPROJECT "%ModDir%"

:checkconfig
pushd "%SDKRoot%"
if exist "GameCfg.ini" (
	for /f "usebackq delims== tokens=1,*" %%a in ("GameCfg.ini") do (
		for %%p in (GameData0 BSP Vis Light ModDir) do (
		if /i "%%~a"=="%%~p" (if not exist "%%~b" (
			MsgBox.exe Some paths of the current configuration are invalid: "%%~b" ^(%%~a^). SDK will be reset to its defaults. /c:Bloodlines SDK - Warning! /t:MB_SYSTEMMODAL,MB_ICONWARNING
			goto autoconfig
		)))
	)
	goto checkgamedir
)

:autoconfig
start MsgBox.exe Automatic setup, please wait... /c:Bloodlines SDK /t:MB_SYSTEMMODAL,MB_ICONINFORMATION
if not exist "%MapSrcDir%" (md "%MapSrcDir%")

:defgamecfg
(sfk echo "[Configs]"
 sfk echo "NumConfigs=1"
 echo.
 sfk echo "[GameConfig0]"
 sfk echo "Name=Vampire: Bloodlines"
 sfk echo "GameData0=%SDKRoot%\vampire.fgd"
 sfk echo "TextureFormat=5"
 sfk echo "MapFormat=4"
 sfk echo "DefaultTextureScale=0.25"
 sfk echo "DefaultLightmapScale=16"
 sfk echo "GameExe=%GameRoot%\Vampire.exe"
 sfk echo "DefaultSolidEntity=func_detail"
 sfk echo "DefaultPointEntity=info_player_start"
 sfk echo "BSP=%SDKRoot%\vbsp.exe"
 sfk echo "Vis=%SDKRoot%\vvis.exe"
 sfk echo "Light=%SDKRoot%\vrad.exe"
 sfk echo "GameExeDir=%GameRoot%"
 sfk echo "MapDir=%MapSrcDir%"
 sfk echo "BSPDir=%GameDir%\maps"
 sfk echo "ModDir=%ModDir%"
 sfk echo "GameDir=%GameDir%"
 sfk echo "CordonTexture=tools/toolsskybox"
 sfk echo "MaterialExcludeCount=16"
 sfk echo "-MaterialExcludeDir0=console"
 sfk echo "-MaterialExcludeDir1=detail"
 sfk echo "-MaterialExcludeDir2=engine"
 sfk echo "-MaterialExcludeDir3=envmap"
 sfk echo "-MaterialExcludeDir4=fonts"
 sfk echo "-MaterialExcludeDir5=hlmv"
 sfk echo "-MaterialExcludeDir6=hud"
 sfk echo "-MaterialExcludeDir7=interface"
 sfk echo "-MaterialExcludeDir8=launcher"
 sfk echo "-MaterialExcludeDir9=maps"
 sfk echo "-MaterialExcludeDir10=models"
 sfk echo "-MaterialExcludeDir11=particle"
 sfk echo "-MaterialExcludeDir12=shadertest"
 sfk echo "-MaterialExcludeDir13=vgui"
 sfk echo "-MaterialExcludeDir14=voice"
 sfk echo "-MaterialExcludeDir15=worldcraft"
)> "GameCfg.ini"

:hammerfix
 reg delete "%WcRegistry%" /f
 reg add "%WcRegistry%\2D Views"         /v "Crosshairs"       /t REG_DWORD /d "1" /f
 reg add "%WcRegistry%\2D Views"         /v "CenterOnCamera"   /t REG_DWORD /d "1" /f
 reg add "%WcRegistry%\2D Views"         /v "Gridhigh64"       /t REG_DWORD /d "0" /f
 reg add "%WcRegistry%\3D Views"         /v "AnimateModels"    /t REG_DWORD /d "0" /f
 reg add "%WcRegistry%\3D Views"         /v "ModelDistance"    /t REG_DWORD /d "2000" /f
 reg add "%WcRegistry%\3D Views"         /v "BackPlane"        /t REG_DWORD /d "3000" /f
 reg add "%WcRegistry%\3D Views"         /v "Reverse Y"        /t REG_DWORD /d "0" /f
 reg add "%WcRegistry%\3D Views"         /v "ReverseSelection" /t REG_DWORD /d "0" /f
 reg add "%WcRegistry%\Configured"       /v "Configured"       /t REG_DWORD /d "2" /f
 reg add "%WcRegistry%\General"          /v "Autosave Dir"     /t REG_SZ    /d "%MapSrcDir%\Autosaves" /f
 reg add "%WcRegistry%\Texture Browser"  /v "Position"         /t REG_SZ    /d "101 72 1179 756" /f
 reg add "%WcRegistry%\Texture Browser"  /v "ShowSize"         /t REG_DWORD /d "1" /f
:reg add "%WcRegistry%\Run Map"          /v "Game Parms"       /t REG_SZ    /d "-dev" /f
:reg add "%WcRegistry%\Run Map"          /v "Light"            /t REG_DWORD /d "1" /f
:reg add "%WcRegistry%\Run Map"          /v "Vis"              /t REG_DWORD /d "1" /f
:reg add "%WcRegistry%\Run Map"          /v "Mode"             /t REG_DWORD /d "1" /f
 reg add "%WcRegistry%\Splitter"         /v "WindowPlacement"  /t REG_SZ    /d "(-8 -30) (-1 -1) (550 25 849 25) 3" /f
 reg add "%WcRegistry%\Splitter"         /v "DrawType0,0"      /t REG_DWORD /d "7" /f
 reg add "%WcRegistry%\Splitter"         /v "DrawType0,1"      /t REG_DWORD /d "0" /f
 reg add "%WcRegistry%\Splitter"         /v "DrawType1,0"      /t REG_DWORD /d "1" /f
 reg add "%WcRegistry%\Splitter"         /v "DrawType1,1"      /t REG_DWORD /d "2" /f
 reg add "HKCU\Software\Tools\PackfileExplorer" /v "LastPath"  /t REG_SZ    /d "%GameDir%" /f

:fileassoc
set "FAPath=%SDKRoot%\tools\FileAssoc"
call "%FAPath%\RegFiles.bat" -internal

:cleartemp
if exist "*.rf"  del /a /q *.rf
copy /y "CmdSeq.int" "CmdSeq.wc"

:fisrstrun
echo # This file needed to detect SDK first launch and run Wizard.>"FirstRun.ini"
taskkill /f /im "MsgBox.exe"

:checkgamedir
for /f "usebackq delims== tokens=1,*" %%a in ("GameCfg.ini") do (
	if /i "%%~a"=="ModDir" (
	if exist "%%~b\*" (
		set "VProject=%%~b"
		reg add "HKCU\Environment" /v "VProject" /t REG_SZ /d "%%~b" /f
		setx VProject "%%~b"
	))
	if /i "%%~a"=="GameDir" (
	if not exist "%%~b\dlls\*" (if not exist "%%~b\pack*.vpk" (
	if not exist "%%~b\models\scenery\*" (if not exist "%%~b\materials\models\scenery\*" (
		goto runvconfig
	)))))
	for %%p in (GameExeDir GameExe) do (
	if /i "%%~a"=="%%~p" (
	if not exist "%%~b" (
		goto runvconfig
	))))
)
goto startsdk

:runvconfig
MsgBox.exe The currently specified game directory is invalid. Please, choose the correct content location (this usually is game's "vampire" subdirectory). If you don't, not all programs will work correctly. /c:Bloodlines SDK - Error! /t:MB_SYSTEMMODAL,MB_ICONWARNING,MB_OKCANCEL
if "%ErrorLevel%"=="2" (del /a /q "FirstRun.ini") else (VCfgRun.exe -int)

:startsdk
taskkill /f /im SDKLauncher.exe
start SDKLauncher.exe

:wizard
if exist "FirstRun.ini" (
	start tools\wizard\prepwizard.exe -int
	del /a /q "FirstRun.ini"
)
exit
