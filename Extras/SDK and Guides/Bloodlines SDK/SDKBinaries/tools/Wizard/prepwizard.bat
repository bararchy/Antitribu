@echo off
setlocal ENABLEEXTENSIONS
set "PATH=%SystemRoot%\System32;%SystemRoot%;%SystemRoot%\System32\Wbem"
set "PATHEXT=.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC"
title Content Preparation Wizard
pushd "%~dp0"
set "MsgBox=..\..\MsgBox.exe"

:checklaunch
if /i "%~1"=="-rungame" (goto RunGame) else (
if /i "%~1"=="-extractvpk" (goto ExtractVPK) else (
if /i "%~1"=="-decompress" (goto DecompMDLs) else (
if /i "%~1"=="-int" (goto FirstRun) else (
	exit
))))

:FirstRun
"%MsgBox%" This is the first launch of the Bloodlines SDK. Since the current version doesn't support content packed into .VPK archives, they need to be unpacked for the correct work of some SDK applications. The extracted resources will go into "SDKContent\Vampire\" (default) directory which will be available to Hammer Editor and other SDK tools.  The original game content and folders won't be touched or modified, nevertheless, your compiled maps will read these resources when you are running them in game.  Extracting may take some time and requires about 2Gb of disk space.  If you don't need tools like the "Hammer Editor" and don't plan to create own maps, an extraction is not necessary.  Start extracting now? /t:MB_SYSTEMMODAL,MB_ICONEXCLAMATION,MB_YESNO /c:Note
if not "%ErrorLevel%"=="6" (
	"%MsgBox%" You may always do the extraction later using the option "ReExtract VPK content" in the Bloodlines SDK main menu. /t:MB_SYSTEMMODAL,MB_ICONINFORMATION /c:Tip
	exit
)

:=======================================================================
:ExtractVPK
taskkill /f /im vextract*.exe
if exist "vextract_error.log" del /a /q "vextract_error.log"
if /i "%~1"=="-extractvpk" (
	start /w VExtract.bat -sep) else (
	start /w VExtract.bat -int
)

if exist "vextract_error.txt" exit
if /i "%~1"=="-extractvpk" exit

:=======================================================================
:DecompMDLs
..\..\MdlDecompress.exe
if /i "%~1"=="-decompress" exit

:=======================================================================
:PrepFinish
"%MsgBox%" All preparations are finished. Bloodlines SDK is configured and ready to work. Have fun! ;) /t:MB_SYSTEMMODAL,MB_ICONINFORMATION /c:Note
exit

:=======================================================================
:RunGame
set CMDLine=-dev
for /f "usebackq delims== tokens=1,*" %%a in ("..\..\GameCfg.ini") do (
	if /i "%%~a"=="GameExe" (set "GameExe=%%~b")
	if /i "%%~a"=="GameExeDir" (set "GameExeDir=%%~b")
)
pushd "%GameExeDir%"
start "game" "%GameExe%" %CMDLine%
exit
