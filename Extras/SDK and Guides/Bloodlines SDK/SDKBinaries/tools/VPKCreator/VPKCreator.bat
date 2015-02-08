:: written by: psycho-a
:: program version: 1.7
:: build date: 09.12.13

@echo off
setlocal ENABLEEXTENSIONS
title Vampire Bloodlines' VPK Creator
color 03

:==============================================================================
:Readme
:==============================================================================

cls
echo.
echo     This tool allows you to create your own VPK archives
echo     from specified directories or entire game.
echo.
echo     Press any key to enter the program menu...
echo.

pause > nul

:==============================================================================
:Vars1

pushd "%~dp0"
set ViewReadme=start "" "%cd%\Readme.txt"
set "GameDir=Vampire"
set "GameExe=Vampire.exe"
set "PackOut=PACKED"
set "PackVals=pack_values.txt"
set "PackDirs=pack_dirs.txt"

:==============================================================================
:Detect

if exist "..\..\GameCfg.ini" (
for /f "usebackq delims== tokens=1,*" %%a in ("..\..\GameCfg.ini") do (
	if /i "%%~a"=="GameExe" (set "GameExe=%%~b")
	if /i "%%~a"=="GameDir" (set "GameDir=%%~b")
	if /i "%%~a"=="GameExeDir" (set "PackOutFull=%%~b\%PackOut%")
)) else (
	pushd ..\..\..\
)

for %%M in ("%GameDir%" "%GameExe%") do (
if not exist "%%~M" (
	color 0c
	cls
	echo.
	echo     ERROR: "%%~M" not found.
	echo.
	echo     Cannot proceed.
	echo.
	pause > nul
	pause > nul
	exit
))



:==============================================================================
:StartMenu
:==============================================================================

cls
echo.
echo     What action you want to do?
echo.
echo     1. Pack the specific folders;
echo     2. Pack all game content (default);
echo     3. Pack all game content (new mode);
echo     4. Build vpk-header (dir tree);
echo     5. View the program readme file;
echo     6. Quit the program.
echo.

set "Choice="
set /p "Choice=>   Your choice: "

if "%Choice%"=="1" (goto PackSingle)
if "%Choice%"=="2" (goto PackAllOld)
if "%Choice%"=="3" (goto PackAllNew)
if "%Choice%"=="4" (goto PackDrTree)
if "%Choice%"=="5" (%ViewReadme%)
if "%Choice%"=="6" (exit)
goto StartMenu












:========================================================================================================
:PackSingle
:========================================================================================================

cls
echo.
echo     Enter the directory name you want to be packed.
echo     Subfolders are supported too.
echo.
echo     You can define up to 10 dirs simultaneously.
echo     When you finish, just leave that field empty and press "Enter".
echo.

set DirToPack0=
set /p "DirToPack0=>   Directory 1: "
if "%DirToPack0%"=="" (
	goto PackSingle) else (
	set "WDirToPack0=echo %DirToPack0%"
)
set DirToPack1=
set /p "DirToPack1=>   Directory 2: "
if "%DirToPack1%"=="" (
	set "WDirToPack1=echo."
	goto PackSingleStart) else (
	set "WDirToPack1=echo %DirToPack1%"
)
set DirToPack2=
set /p "DirToPack2=>   Directory 3: "
if "%DirToPack2%"=="" (
	set "WDirToPack2=echo."
	goto PackSingleStart) else (
	set "WDirToPack2=echo %DirToPack2%"
)
set DirToPack3=
set /p "DirToPack3=>   Directory 4: "
if "%DirToPack3%"=="" (
	set "WDirToPack3=echo."
	goto PackSingleStart) else (
	set "WDirToPack3=echo %DirToPack3%"
)
set DirToPack4=
set /p "DirToPack4=>   Directory 5: "
if "%DirToPack4%"=="" (
	set "WDirToPack4=echo."
	goto PackSingleStart) else (
	set "WDirToPack4=echo %DirToPack4%"
)
set DirToPack5=
set /p "DirToPack5=>   Directory 6: "
if "%DirToPack5%"=="" (
	set "WDirToPack5=echo."
	goto PackSingleStart) else (
	set "WDirToPack5=echo %DirToPack5%"
)
set DirToPack6=
set /p "DirToPack6=>   Directory 7: "
if "%DirToPack6%"=="" (
	set "WDirToPack6=echo."
	goto PackSingleStart) else (
	set "WDirToPack6=echo %DirToPack6%"
)
set DirToPack7=
set /p "DirToPack7=>   Directory 8: "
if "%DirToPack7%"=="" (
	set "WDirToPack7=echo."
	goto PackSingleStart) else (
	set "WDirToPack7=echo %DirToPack7%"
)
set DirToPack8=
set /p "DirToPack8=>   Directory 9: "
if "%DirToPack8%"=="" (
	set "WDirToPack8=echo."
	goto PackSingleStart) else (
	set "WDirToPack8=echo %DirToPack8%"
)
set DirToPack9=
set /p "DirToPack9=>   Directory 10: "
if "%DirToPack9%"=="" (
	set "WDirToPack9=echo."
	goto PackSingleStart) else (
	set "WDirToPack9=echo %DirToPack9%"
)


:=======================================
:PackSingleStart

(echo pack_folder = ..\%PackOut%
 echo max_size = 1024
 echo skip = scc vpk vmf map pyc pk sav hl1 hl2 hl3 bat cmd tmp bak old dt db csv wc
 echo localized_file = %PackDirs%
)> "%GameDir%\%PackVals%"

(%WDirToPack0%
 %WDirToPack1%
 %WDirToPack2%
 %WDirToPack3%
 %WDirToPack4%
 %WDirToPack5%
 %WDirToPack6%
 %WDirToPack7%
 %WDirToPack8%
 %WDirToPack9%
)> "%GameDir%\%PackDirs%"

:=======================================

call :StartEngine -localizedpack
del /f /q "%GameDir%\%PackVals%" "%GameDir%\%PackDirs%" > nul

for %%D in ("%PackOutFull%\*.vpk") do (if exist "%%~D" (if %%~zD LEQ 20 (del /f /q "%%~D" > nul)))
call :CheckVpkExist

:=======================================
:ProcessFiles

if exist "%GameDir%\*.vpk" (
	for %%V in ("%GameDir%\pack0*.vpk") do (
		call :ProcessNames "%%~nV"
		set "TargetDir=%GameDir%"
	)
) else (
	for %%V in ("%PackOutFull%\*.vpk") do (
		set "FinalPackName=%%~nxV"
		set "TargetDir=%PackOutFull%"
	)
)

if exist "%GameDir%\*.vpk" (
	move /y "%PackOutFull%\*.vpk" "%GameDir%\%FinalPackName%" > nul
	rd /s /q "%PackOutFull%" > nul
)

:=======================================
:PackSingleFinalize

cls
echo.
echo     Pack with selected dirs was succesfully created
echo     and placed into "%TargetDir%" folder as "%FinalPackName%".
echo     Delete unpacked versions of these directories?
echo.
echo     1 - Yes; 2 - No (keep it and back to menu).
echo.

set "Choice="
set /p "Choice=>   Your choice: "

cls
echo.
if "%Choice%"=="2" (goto StartMenu)
if "%Choice%"=="1" (for %%M in (
	"%DirToPack0%"
	"%DirToPack1%"
	"%DirToPack2%"
	"%DirToPack3%"
	"%DirToPack4%"
	"%DirToPack5%"
	"%DirToPack6%"
	"%DirToPack7%"
	"%DirToPack8%"
	"%DirToPack9%"
	) do (
	if not "%%~M"=="" (
	if exist "%GameDir%\%%~M" (
		echo     Deleting "%%~M"...
		rd /s /q "%GameDir%\%%~M" > nul
	)))

	cls
	echo.
	echo     All selected directories deleted.
	echo.
	pause > nul
	pause > nul
	goto StartMenu
)

goto PackSingleFinalize














:========================================================================================================
:PackAllOld
:========================================================================================================

call :FullPackWarning
if /i "%return%"=="true" (goto StartMenu)

(echo pack_folder = ..\%PackOut%
 echo max_size = 512
 echo exclude = bsp ain loc dll bin py bik ico ttf cur vbsp rad
 echo skip = scc vpk vmf map pyc pk sav hl1 hl2 hl3 bat cmd tmp bak old bin dt db csv wc
 echo separate = wav
 echo localized_file = %PackDirs%
) > "%GameDir%\%PackVals%"

(echo dlg
 echo resource
 echo scripts
 echo vdata
) > "%GameDir%\%PackDirs%"

:=======================================

call :StartEngine +packfiles +wait +quit
call :CheckVpkExist

call :StartEngine -localizedpack
call :CheckVpkExist

:=======================================

for %%M in (
	"%GameDir%\maps\*.bspstats.txt"
	"%GameDir%\%PackVals%"
	"%GameDir%\%PackDirs%"
) do if exist "%%~M" (del /f /q "%%~M" > nul)

:=======================================
:PackAllOldFinalize

cls
echo.
echo     All the game resources have been packed.
echo     Some types of resources were not packed, so that were
echo     copied as is. See "%PackOut%" dir for the details.
echo.
echo     Delete unpacked versions of directories?
echo     They will no longer be used by game.
echo.
echo     1 - Yes; 2 - No (exit program).
echo.

set "Choice="
set /p "Choice=>   Your choice: "

if "%Choice%"=="2" (exit)
if "%Choice%"=="1" (
	cls
	echo.
	echo     Stopping hindering apps...
	echo.
	taskkill /f /im vampire.exe > nul
	taskkill /f /im wc.exe > nul
	taskkill /f /im hammer.exe > nul
	taskkill /f /im hlmv.exe > nul
	taskkill /f /im hlfaceposer.exe > nul

	cls
	echo.
	echo     Deleting folders...
	echo.
	rename "%GameDir%" "%GameDir%_tmp" > nul
	rename "%PackOutFull%" "%GameDir%" > nul
	rd /s /q "%GameDir%_tmp" > nul

	cls
	echo.
	echo     All directories were deleted. 
	echo     Your unpacked game converted into packed one.
	echo.
	pause > nul
	pause > nul
	exit
)

goto PackAllOldFinalize












:========================================================================================================
:PackAllNew
:========================================================================================================

call :FullPackWarning
if /i "%return%"=="true" (goto StartMenu)

if exist "%PackOutFull%" (rd /s /q "%PackOutFull%" > nul)
mkdir "%PackOutFull%\vpk_temp" > nul

:=======================================
:CreateDirTree

(echo pack_folder = ..\%PackOut%
 echo max_size = 1536
 echo skip = scc vpk vmf map pyc pk sav hl1 hl2 hl3 bat cmd tmp bak old dt db xls csv wc
 echo skip = dll exe bin dat
 echo skip = bsp ain loc lmp
 echo skip = vmt tth ttz mdl vtx vvd phy
 echo skip = tga bmp bik
 echo skip = cfg rc scr dlg py
 echo skip = res vdf ttf ani txt lst dsp gam gam~
 echo skip = wav mp3 sfk pk vcd lip
 echo skip = vfe vta vcs vbsp rad
 echo skip = psh vsh fnt
) > "%GameDir%\%PackVals%"

call :MakePakOverall

move "%PackOutFull%\pack000.vpk" "%PackOutFull%\vpk_temp\" > nul

:=======================================
:DefineDirs

(echo pack_folder = ..\%PackOut%
 echo max_size = 1536
 echo skip = scc vpk vmf map pyc pk sav hl1 hl2 hl3 bat cmd tmp bak old dt db csv wc
 echo localized_file = %PackDirs%
) > "%GameDir%\%PackVals%"

:=======================================

(echo cfg
 echo expressions
 echo gfx
 echo particles
 echo shaders
 echo detail.vbsp
 echo lights.rad
)> "%GameDir%\%PackDirs%"
call :MakePakSingle "001"

:=======================================

echo materials> "%GameDir%\%PackDirs%"
call :MakePakSingle "002"

:=======================================

echo models> "%GameDir%\%PackDirs%"
call :MakePakSingle "003"

:=======================================

(echo sound\music
 echo sound\radio
)> "%GameDir%\%PackDirs%"
call :MakePakSingle "004"

if exist "%GameDir%\sound_tmp" (rd /s /q "%GameDir%\sound_tmp" > nul)
mkdir "%GameDir%\sound_tmp" > nul
for %%M in ("sound\music" "sound\radio") do (move "%GameDir%\%%~M" "%GameDir%\sound_tmp\" > nul)

:=======================================

echo sound\character> "%GameDir%\%PackDirs%"
call :MakePakSingle "005"

for %%M in ("sound\character") do (move "%GameDir%\%%~M" "%GameDir%\sound_tmp\" > nul)

:=======================================

echo sound> "%GameDir%\%PackDirs%"
call :MakePakSingle "006"

for %%M in ("character" "music" "radio") do (move "%GameDir%\sound_tmp\%%~M" "%GameDir%\sound\" > nul)

:=======================================

(echo dlg
 echo resource
 echo scripts
 echo vdata
)> "%GameDir%\%PackDirs%"
call :MakePakSingle "007"

:=======================================
cls
echo.
echo     Deleting temporary files...
echo.

(del /f /s /q "%GameDir%\python\*.pyc"
 del /f /s /q "%GameDir%\maps\*.bspstats.txt"
 rd /s /q  "%GameDir%\save"
 rd /s /q  "%GameDir%\sound_tmp"
 del /f /q "%GameDir%\*.tmp"
 del /f /q "%GameDir%\stats.txt"
 del /f /q "%GameDir%\%PackVals%"
 del /f /q "%GameDir%\%PackDirs%"
 mkdir "%GameDir%\save"
) > nul

:=======================================
cls
echo.
echo     Copying necessary unpacked files...
echo.

(xcopy /y /c /i /e "%GameDir%\cfg"		"%PackOutFull%\cfg"
 xcopy /y /c /i /e "%GameDir%\cl_dlls"	"%PackOutFull%\cl_dlls"
 xcopy /y /c /i /e "%GameDir%\dlls"		"%PackOutFull%\dlls"
 xcopy /y /c /i /e "%GameDir%\maps"		"%PackOutFull%\maps"
 xcopy /y /c /i /e "%GameDir%\media"	"%PackOutFull%\media"
 xcopy /y /c /i /e "%GameDir%\python"	"%PackOutFull%\python"
 xcopy /y /c /i /e "%GameDir%\save" 	"%PackOutFull%\save"
) > nul

move /y "%PackOutFull%\vpk_temp\*.vpk" "%PackOutFull%\" > nul
rd /s /q "%PackOutFull%\vpk_temp" > nul

:=======================================
:PackAllNewFinalize

cls
echo.
echo     All the game resources have been packed.
echo     Some types of resources were not packed, so that were
echo     copied as is. See "%PackOut%" dir for the details.
echo.
echo     Delete unpacked versions of directories?
echo     They will no longer be used by game.
echo.
echo     1 - Yes; 2 - No (exit program).
echo.

set "Choice="
set /p "Choice=>   Your choice: "

if "%Choice%"=="2" (exit)
if "%Choice%"=="1" (
	cls
	echo.
	echo     Stopping hindering apps...
	echo.
	taskkill /f /im vampire.exe > nul
	taskkill /f /im wc.exe > nul
	taskkill /f /im hammer.exe > nul
	taskkill /f /im hlmv.exe > nul
	taskkill /f /im hlfaceposer.exe > nul

	cls
	echo.
	echo     Deleting folders...
	echo.
	rename "%GameDir%" "%GameDir%_tmp" > nul
	rename "%PackOutFull%" "%GameDir%" > nul
	rd /s /q "%GameDir%_tmp" > nul

	cls
	echo.
	echo     All directories were deleted. 
	echo     Your unpacked game converted into packed one.
	echo.
	pause > nul
	pause > nul
	exit
)

goto PackAllNewFinalize














:========================================================================================================
:PackDrTree
:========================================================================================================

cls
echo.
echo     Index building is necessary in case the game directories were
echo     packaged separately (as in point "1" of menu). This creates 
echo     an additional directory index that required for correct work 
echo     of some types of resources.
echo.
echo     Remember that ALL game's directories should have it's 
echo     unpacked versions, otherwise VPK header will not be a full.
echo.
echo     Press any key to start creation...
echo.

pause > nul
pause > nul

if exist "%PackOutFull%" (rd /s /q "%PackOutFull%" > nul)

(echo pack_folder = ..\%PackOut%
 echo max_size = 1536
 echo skip = scc vpk vmf map pyc pk sav hl1 hl2 hl3 bat cmd tmp bak old dt db xls csv wc
 echo skip = dll exe bin dat
 echo skip = bsp ain loc lmp
 echo skip = vmt tth ttz mdl vtx vvd phy
 echo skip = tga bmp bik
 echo skip = cfg rc scr dlg py
 echo skip = res vdf ttf ani txt lst dsp gam gam~
 echo skip = wav mp3 sfk pk vcd lip
 echo skip = vfe vta vcs vbsp rad
 echo skip = psh vsh fnt
) > "%GameDir%\%PackVals%"

call :MakePakOverall

:=======================================
cls
echo.
echo     Directory index was built succesfully.
echo.
pause > nul
pause > nul
exit







:========================================================================================================
:FunctionCalls
:========================================================================================================

:=======================================
:StartEngine
	cls
	echo.
	echo     Starting engine...
	echo     Please wait until the process end.
	echo.
	if exist "%GameDir%\cfg\config.cfg" (move /y "%GameDir%\cfg\config.cfg" "%GameDir%\cfg\config.bak" > nul)
	start /w "engine" "%GameExe%" -dev -sw -console %*
	if exist "%GameDir%\cfg\config.bak" (move /y "%GameDir%\cfg\config.bak" "%GameDir%\cfg\config.cfg" > nul)
exit /b

:=======================================
:CheckVpkExist

if not exist "%PackOutFull%\*.vpk" (
	cls
	color 0c
	echo.
	echo     ERROR: VPK files were not created. 
	echo.
    echo     Maybe an engine error occured or invalid/missing directories specified.
	echo.
	pause > nul
	pause > nul
	exit
)
exit /b

:=======================================
:MakePakSingle
	call :StartEngine -localizedpack
	
	for %%D in ("%PackOutFull%\*.vpk") do (
		if exist "%%~D" (if %%~zD LEQ 20 (del /f /q "%%~D" > nul))
	)
	call :CheckVpkExist

	rename "%PackOutFull%\*.vpk" "pack%~1.vpk" > nul
	move "%PackOutFull%\pack%~1.vpk" "%PackOutFull%\vpk_temp\" > nul
exit /b

:=======================================
:MakePakOverall
	call :StartEngine +packfiles +wait +quit
	
	if exist "%GameDir%\maps\*.bspstats.txt" (del /f /q "%GameDir%\maps\*.bspstats.txt" > nul)
	if exist "%GameDir%\%PackVals%" (del /f /q "%GameDir%\%PackVals%" > nul)

	for %%D in ("%PackOutFull%\*.vpk") do (if exist "%%~D" (if %%~zD LEQ 20 (del /f /q "%%~D" > nul)))
	call :CheckVpkExist

	for %%D in ("%PackOutFull%\*.vpk") do (move /y "%%~D" "%PackOutFull%\pack000.vpk" > nul)
exit /b

:=======================================
:ProcessNames
	set "NameTmp=%~1"
	set "LastNum=%NameTmp:~-2%"
	set /a "ResultNum=%LastNum%+1"
	if %ResultNum% LSS 10 (
		set "ResultNum=00%ResultNum%") else (
		set "ResultNum=0%ResultNum%"
	)
	set "FinalPackName=pack%ResultNum%.vpk"
exit /b

:=======================================
:FullPackWarning
	cls
	echo.
	echo     Warning: before doing this action make sure that ALL of
	echo     your game resources are unpacked. Otherwise, the packed 
    echo     version of game will not be playable. For packing some
    echo     separated content, please use "1" point of main menu.
	echo.
	echo     Press '1' to start or '2' to return...
	echo.

	set "Choice="
	set /p "Choice=>   Your choice: "

	set "return=false"
	if "%Choice%"=="1" (exit /b)
	if "%Choice%"=="2" (
		set "return=true"
		exit /b
	)
	goto FullPackWarning
exit /b
