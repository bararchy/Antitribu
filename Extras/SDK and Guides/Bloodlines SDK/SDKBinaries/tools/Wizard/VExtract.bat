@echo off
setlocal ENABLEEXTENSIONS
set "PATH=%SystemRoot%\System32;%SystemRoot%;%SystemRoot%\System32\Wbem"
set "PATHEXT=.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC"
color 06
title Bloodlines VPK Extractor
if "%~1"=="" exit
pushd "%~dp0..\..\"
set "MsgBox=%cd%\MsgBox.exe"
set "SfkTool=%cd%\Sfk.exe"
popd

:=======================================================================
:prepare
echo Starting...
if not exist "..\..\GameCfg.ini" (
	echo - No "GameCfg.ini" found.>>"VExtract_error.log"
	"%MsgBox%" No "GameCfg.ini" found in SDK binaries directory. Cannot detect valid game paths. Exiting... /c:ERROR! /t:MB_ICONSTOP
	exit
)

set TargetDir=
for /f "usebackq delims== tokens=1,*" %%i in ("..\..\GameCfg.ini") do (
	if /i "%%~i"=="GameDir" (
		if exist "%%~j\sound\*" (
			if exist "%%~j\*.vpk" (
				set "SourceDir=%%~j"
			) else (
				echo - Incorrect GameDir specified.>>"VExtract_error.log"
				"%MsgBox%" No valid game files found at "%%~j\". Please, define the correct "GameDir" path in "GameCfg.ini" using "Change Path to GameDir" option in the SDK main menu or using Hammer Editor's configuration. /c:ERROR! /t:MB_ICONSTOP
				exit
			)
		) else (
			echo - No VPK archives found.>>"VExtract_error.log"
			"%MsgBox%" No VPK archives found at "%%~j\". Maybe your game has already been extracted? If so, set the "ModDir" path to be the same as the "GameDir" one. /c:ERROR! /t:MB_ICONSTOP
			exit
		)
	)
	if /i "%%~i"=="ModDir" (
		set "TargetDir=%%~j"
		if not exist "%%~j\" md "%%~j"
	)
)

if not defined TargetDir (
	echo - No ModDir specified.>>"VExtract_error.log"
	"%MsgBox%" No "ModDir" specified in "GameCfg.ini" file. This folder is needed to extract the VPK contents into. Please, define the correct "ModDir" path using Hammer Editor's configuration. You can also get the default one by running "Reset SDK Configuration" procedure from the SDK main menu. /c:ERROR! /t:MB_ICONSTOP
	exit
)

echo Source Directory [GameDir]: 
echo   "%SourceDir%"
echo Target Directory [Content]: 
echo   "%TargetDir%"
echo.

if /i "%~1"=="-sep" (
	"%MsgBox%" Extracting content from original VPK archives needed for correct SDK-applications work because its current version doesn't support VPK file-system. The extracted resources will go into directory which will be available to the Hammer Editor and other SDK tools.  The original game content and folders won't be touched or modified, nevertheless, your compiled maps will read these resources when you are running them in game.  Extracting may take some time and requires about 2Gb of disk space.  If you don't need tools like the Hammer Editor and don't plan to create own maps, an extraction is not necessary.  Start extracting now? /t:MB_ICONEXCLAMATION,MB_YESNO /c:Note
)
if "%ErrorLevel%"=="7" (
	echo Cancelled.
	exit
)

start "" "%MsgBox%" Content will be extracted into directory "%TargetDir%". First, the basic content (textures, models and sounds) will be extracted. See console window for current progress. Don't close it! /c:Note /t:MB_ICONASTERISK


:=======================================================================
:fixloosefiles
echo Preparing...
for %%m in (02 03 04 05 06 07 08 09 10) do (
	if not exist "%SourceDir%\pack1%%~m.vpk" (
	copy "empty.vpk" "%SourceDir%\pack1%%~m.vpk"> nul
))

:buildindex
if exist "%TEMP%\vpkindex.*" del /a /q "%TEMP%\vpkindex.*"> nul
vextract0.exe -d "%SourceDir%" -o "%TargetDir%" -i -q
vextract1.exe -d "%SourceDir%" -o "%TargetDir%" -i -q

:=======================================================================
:content
call :Extract "Textures" "0 1" "materials" "vmt tth ttz"
call :Extract "Models"   "0 1" "models"    "mdl vtx"
call :Extract "Sounds"   "0 1" "sound"     "wav"
echo Basic content extracted.

call :CheckMsgBox
"%MsgBox%" Basic resources extracted. Do you also want to extract the script assets?  Note they are not needed for level design, but may be useful if you wish to add or customize quests, game mechanics or interfaces.  Since Python scripts and MP3 audio are already extracted, they will be left in the original game directory. You can always access it. /c:Information /t:MB_SYSTEMMODAL,MB_ICONQUESTION,MB_YESNO
if not "%ErrorLevel%"=="6" goto finish
echo.

:=======================================================================
:scripts
call :Extract "Dialogues"     "1"   "dlg"           "dlg"
call :Extract "Particles"     "0"   "particles"     "tga txt"
call :Extract "GUI Resources" "0 1" "resource"      "res txt"
call :Extract "GUI Scripts"   "0 1" "scripts"       "txt lst"
call :Extract "Sound Scripts" "0"   "sound/schemes" "txt"
call :Extract "-"             "1"   "sound"         "lip"
call :Extract "VData Scripts" "1"   "vdata"         "txt"
echo Additional content extracted.

:=======================================================================
:finish
echo Deleting temporaries...
if exist "%TEMP%\vpkindex.*" del /a /q "%TEMP%\vpkindex.*"> nul
for %%v in ("%SourceDir%\pack1*.vpk") do (
	if "%%~zv"=="173258" del /a /q "%%~v"> nul
)

"%MsgBox%" Needed assets extracted from the VPKs. Do you also wish to copy the loose content not packed into VPKs?  This is usually added or modded content from unofficial patches or mods, after that it will be available in the Hammer Editor or other tools. /c:Information /t:MB_SYSTEMMODAL,MB_ICONINFORMATION,MB_YESNO
if not "%ErrorLevel%"=="6" goto finalize
echo.

:=======================================================================
:copyunpacks
pushd "%SourceDir%"

call :CopyLoose Textures "materials" ".vmt .tth .ttz" "X\"
call :CopyLoose Models   "models"    ".mdl .vtx"      "X\"
call :CopyLoose Sounds   "sound"     ".wav"           "X\"
echo Basic content copied.

"%MsgBox%" Basic resources copied. Copy also scripted resources? /c:Information /t:MB_SYSTEMMODAL,MB_ICONQUESTION,MB_YESNO
if not "%ErrorLevel%"=="6" goto finalize
echo.

call :CopyLoose "Dialogues"     "dlg"           ".dlg"      "X\"
call :CopyLoose "Particles"     "particles"     ".tga .txt" "X\"
call :CopyLoose "GUI Resources" "resource"      ".res .txt" "X\"
call :CopyLoose "GUI Scripts"   "scripts"       ".txt .lst" "X\"
call :CopyLoose "Sound Scripts" "sound\schemes" ".txt"      "X\sound\"
call :CopyLoose "VData Scripts" "vdata"         ".txt"      "X\"
echo Additional content copied.
popd

:=======================================================================
:finalize
"%MsgBox%" All content transfer operations finished. It's strongly recommended to run the "MDLDecompressor" tool to fix models that are unsupported by the Hammer Editor. /c:Information /t:MB_SYSTEMMODAL,MB_ICONINFORMATION
exit




:=======================================================================
:Functions

:CheckMsgBox
	for /f "tokens=1" %%m in ('tasklist /NH') do (
		if /i "%%~m"=="msgbox.exe" (taskkill /f /im "msgbox.exe"> nul)
	)
exit /b

:Extract
	if not "%~1"=="-" (
		echo Extracting %~1...
	)
	for %%t in (%~2) do (
	for %%e in (%~4) do (
		vextract%%~t.exe "%~3/*.%%~e" -d "%SourceDir%" -o "%TargetDir%" -q
	))
exit /b

:CopyLoose
	echo Copying %~1...
	if exist "%~2\*" (
	for %%e in (%~3) do (
		xcopy>nul /Y /R /H /I /S /Q /C "%~2\*%%~e" "%TargetDir%\%~2\"
	)) else (
		echo   No "%~2" dir presented in your game version.
	)
exit /b
