@echo off
setlocal ENABLEEXTENSIONS
set "PATH=%SystemRoot%\System32;%SystemRoot%;%SystemRoot%\System32\Wbem"
set "PATHEXT=.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC"
title Run Map Launcher
color 07
pushd "%~dp0"
set "RMCfg=rm_config.ini"


:========================================================================
:DefineTasks
:========================================================================

:exec_stage
 if "%~1"=="" (exit)
 if /i "%~1"=="-executejob" (goto ExecuteJob)

:prep_stage
 if /i "%~1 %~2"=="set game" (
	echo [Base]
	echo RunTask	=	True
	echo GameDir	=	"%~3")>"%RMCfg%"
 if /i "%~1 %~2"=="set map" (
	echo MapFile	=	"%~3"
	echo MapName	=	"%~n3")>>"%RMCfg%"
 if /i "%~1 %~3"=="pause window" (
	echo PauseWin	=	True)>>"%RMCfg%"

:vbsp_stage
 if /i "%~1 %~n2"=="exec vbsp" (
	echo.
	echo [VBSP]
	echo RunVbsp	=	True
	echo VbspCmd	=	"%3 %4 %5 %6 %7 %8 %9"
	if /i "%~3"=="-onlyents" (
	echo OnlyEnts	=	True))>>"%RMCfg%"

:vvis_stage
 if /i "%~1 %~n2"=="exec vvis" (
	echo.
	echo [VVIS]
	echo RunVvis	=	True
	echo VvisCmd	=	"%3 %4 %5 %6 %7 %8 %9")>>"%RMCfg%"

:vrad_stage
 if /i "%~1 %~n2"=="exec vrad" (
	echo.
	echo [VRAD]
	echo RunVrad	=	True
	echo VradCmd	=	"%3 %4 %5 %6 %7 %8 %9")>>"%RMCfg%"

:copy_stage
 if /i "%~1 %~2 %~3 %~4"=="put compiled bsp to" (
	echo.
	echo [File]
	echo CopyBSP	=	True
	echo DestDir	=	"%~5")>>"%RMCfg%"

:game_stage
 if /i "%~1 %~x2"=="run .exe" (
	echo.
	echo [Engine]
	echo RunGame	=	True
	echo ExeFull	=	"%~2"
	echo ExePath	=	"%~dp2"
	echo ExeFile	=	"%~nx2"
	echo ExeExtn	=	"%~x2"
	echo GameCmd	=	"%3 %4 %5 %6 %7 %8 %9")>>"%RMCfg%"

exit



:========================================================================
:ExecuteJob
:========================================================================

:check_files
for %%f in (
	"@"
	"execute"
	"vbsp.exe"
	"vvis.exe"
	"vrad.exe"
	"rm_config.ini"
	"rm_fontset.reg"
	"rm_launch.bat"
	"sfk.exe"
) do if not exist "%%~f" (
	color 0c
	echo.
	echo   Error: Missing file: "%%~f". Cannot proceed.
	pause>nul
	goto quit
)

set "MapFile="
set "textcolor=sfk.exe color"
for /f "usebackq eol=# tokens=1,* delims=	=" %%a in ("%RMCfg%") do set "%%~a=%%~b"
del /f /q "%RMCfg%"> nul

:prepare
if /i not "%RunTask%"=="True" (
	color 0c
	echo.
	echo   Error: No game dir specified!
	pause>nul
	goto quit
)
if not defined MapFile (
	color 0c
	echo.
	echo   Error: No map file specified!
	pause>nul
	goto quit
)


call :get_starttime
%textcolor% blue
echo ###############################################################################
echo #                                                                             #
echo #                             Preparing script                                #
echo #                                                                             #
echo ###############################################################################
%textcolor% grey
echo.
echo Game Directory: "%GameDir%".
echo Compiling Map:  "%MapFile%.vmf".

(echo ================ Log started [%date%, %time:~0,-3%] =================
 echo.
 echo Game Directory: "%GameDir%".
 echo Current Map: "%MapFile%.vmf".
)>"%MapFile%.log"

echo Deleting previous compilation dumps...
if exist "%MapFile%.bsp" (
if /i not "%OnlyEnts%"=="True" (
	del /f /q "%MapFile%.bsp"> nul
	echo>>"%MapFile%.log" Deleted old compilation: "%MapName%.bsp".
)) else (if /i "%OnlyEnts%"=="True" (
	if exist "%DestDir%\%MapName%.bsp" (
	copy /y "%DestDir%\%MapName%.bsp" "%MapFile%.bsp"> nul)
))
if exist "%MapFile%.prt" (
	del /f /q "%MapFile%.prt"> nul
	echo>>"%MapFile%.log" Deleted old compilation: "%MapName%.prt".
)
echo.>>"%MapFile%.log"
echo.
echo.


:run_vbsp
if /i not "%RunVbsp%"=="True" (goto run_vvis)
set "VbspCmdInfo=%VbspCmd%"
if "%VbspCmd%"=="      " set "VbspCmdInfo=[Default]"
%textcolor% blue
echo ###############################################################################
echo #                                                                             #
echo #                        Starting VBSP compilation                            #
echo #                                                                             #
echo ###############################################################################
%textcolor% grey
echo Params: %VbspCmdInfo%
echo.

(echo.
 echo.
 echo ============ Started VBSP compilation [%date%, %time:~0,-3%] =============
 echo Parameters: %VbspCmdInfo%
)>>"%MapFile%.log"

vbsp.exe %VbspCmd% "%MapFile%"
if ErrorLevel 1 (goto if_error)
if not exist "%MapFile%.bsp" (goto if_error)
echo.>>"%MapFile%.log"
echo.
echo.


:run_vvis
if /i not "%RunVvis%"=="True" (goto run_vrad)
set "VvisCmdInfo=%VvisCmd%"
if "%VvisCmd%"=="      " set "VvisCmdInfo=[Default]"
%textcolor% blue
echo ###############################################################################
echo #                                                                             #
echo #                        Starting VVIS compilation                            #
echo #                                                                             #
echo ###############################################################################
%textcolor% grey
echo Params: %VvisCmdInfo%
echo.

(echo.
 echo.
 echo ============ Started VVIS compilation [%date%, %time:~0,-3%] =============
 echo Parameters: %VvisCmdInfo%
)>>"%MapFile%.log"

vvis.exe %VvisCmd% "%MapFile%"
if ErrorLevel 1 (goto if_error)
if not exist "%MapFile%.prt" (goto if_error)
echo.>>"%MapFile%.log"
echo.
echo.


:run_vrad
if /i not "%RunVrad%"=="True" (goto copy_file)
set "VradCmdInfo=%VradCmd%"
if "%VradCmd%"=="      " set "VradCmdInfo=[Default]"
%textcolor% blue
echo ###############################################################################
echo #                                                                             #
echo #                        Starting VRAD compilation                            #
echo #                                                                             #
echo ###############################################################################
%textcolor% grey
echo Params: %VradCmdInfo%
echo.

(echo.
 echo.
 echo ============ Started VRAD compilation [%date%, %time:~0,-3%] ============
 echo Parameters: %VradCmdInfo%
)>>"%MapFile%.log"

vrad.exe %VradCmd% "%MapFile%"
if ErrorLevel 1 (goto if_error)
echo.>>"%MapFile%.log"
echo.
echo.


:copy_file
if /i not "%CopyBSP%"=="True" (goto run_game)
%textcolor% blue
echo ###############################################################################
echo #                                                                             #
echo #                    Copying BSP file to game directory                       #
echo #                                                                             #
echo ###############################################################################
%textcolor% grey
echo.
echo Source path: "%MapFile%.bsp"
echo Destination: "%DestDir%\"
if not exist "%DestDir%" (md "%DestDir%">nul)

(echo.
 echo.
 echo ============ Managing compiled files [%date%, %time:~0,-3%] =============
 echo.
)>>"%MapFile%.log"

echo.
echo Deleting previous compilation...
echo>>"%MapFile%.log" Deleting previous compilation...
if exist "%DestDir%\%MapName%.bsp" (
	del /f /q "%DestDir%\%MapName%.bsp"> nul
	echo>>"%MapFile%.log" - Deleted: "%DestDir%\%MapName%.bsp".
) else (
	echo>>"%MapFile%.log" - Nothing to delete.
	echo.
)

echo Placing file to BSP directory...
(echo Placing file to BSP directory...
 echo - Source path: "%MapFile%.bsp"
 echo - Destination: "%DestDir%\"
)>>"%MapFile%.log"
if exist "%MapFile%.bsp" (
	copy /y "%MapFile%.bsp" "%DestDir%\"> nul
	echo>>"%MapFile%.log" - File succesfully copied.
) else (
	echo Error: File "%MapFile%.bsp" not found.
	echo>>"%MapFile%.log" - Error: File "%MapFile%.bsp" not found.
	echo.
)

echo Deleting compilation dumps...
echo>>"%MapFile%.log" Deleting compilation dumps...
if exist "%MapFile%.prt" (
	del /f /q "%MapFile%.prt"> nul
	echo>>"%MapFile%.log" - Deleted: "%MapFile%.prt".
) else (
	echo>>"%MapFile%.log" - No prt file exist.
)
if exist "%MapFile%.bsp" (
	del /f /q "%MapFile%.bsp"> nul
	echo>>"%MapFile%.log" - Deleted: "%MapFile%.bsp".
) else (
	echo>>"%MapFile%.log" - No bsp file exist.
)
echo.
echo.


:run_game
if /i not "%RunGame%"=="True" (goto show_time)
set "GameCmdInfo=%GameCmd%"
if "%GameCmd%"=="      " set "GameCmdInfo=[None]"
%textcolor% blue
echo ###############################################################################
echo #                                                                             #
echo #                             Starting Engine                                 #
echo #                                                                             #
echo ###############################################################################
%textcolor% grey
echo.
echo GameDir: "%GameDir%"
echo GameExe: "%ExeFull%"
echo MapFile: "%MapName%.bsp"
echo Params: %GameCmdInfo%
echo.

(echo.
 echo.
 echo ============= Starting map in game [%date%, %time:~0,-3%] ==============
 echo.
 echo GameDir: "%GameDir%"
 echo GameExe: "%ExeFull%"
 echo MapFile: "%MapName%.bsp"
 echo Params:  %GameCmdInfo%
)>>"%MapFile%.log"

if /i not "%ExeExtn%"==".exe" (
	%textcolor% red
	echo Error: Wrong game EXE file specified!
	%textcolor% grey
	(echo.
	 echo Error: Wrong game EXE file specified!
	)>>"%MapFile%.log"
)

call :killproc "%ExeFile%"
pushd "%ExePath%"
start "game" "%ExeFile%" +map "%MapName%" %GameCmd%
popd
echo.


:show_time
for %%m in ("%RunVbsp%" "%RunVvis%" "%RunVrad%") do (if /i "%%~m"=="True" goto show_ok)
goto close_log

:show_ok
echo.>>"%MapFile%.log"
echo.>>"%MapFile%.log"
call :get_elapsedtime
echo.


:close_log
(echo.
 echo.
 echo  ================ Log closed [%date%, %time:~0,-3%] =================
)>>"%MapFile%.log"
%textcolor% green
echo Finished.
%textcolor% grey


:quit
if exist "%RMCfg%" del /a /q "%RMCfg%"> nul
if /i "%PauseWin%"=="True" (pause> nul)
exit


:=======================================================
:if_error
	echo.
	%textcolor% yellow
	echo __________________________________________
	echo.
	%textcolor% red
	echo [-] An error occured during compiling your map.
	echo [-] See console log for more details.
	%textcolor% grey
	(echo.
	 echo.
	 echo  ================ Log closed [%date%, %time:~0,-3%] =================
	)>>"%MapFile%.log"
	pause > nul
	exit
exit /b

:get_starttime
	for /F "tokens=1-4 delims=:.," %%a in ("%time%") do (
	   set /A "startt=(((%%~a*60)+1%%~b %% 100)*60+1%%~c %% 100)*100+1%%~d %% 100"
	)
exit /b

:get_elapsedtime
	:: get end time:
	for /F "tokens=1-4 delims=:.," %%a in ("%time%") do (
	   set /A "endt=(((%%~a*60)+1%%~b %% 100)*60+1%%~c %% 100)*100+1%%~d %% 100"
	)

	:: get elapsed time:
	set /A "elapsedt=endt-startt"

	:: show elapsed time:
	set /A "hh=elapsedt/(60*60*100), rest=elapsedt%%(60*60*100), mm=rest/(60*100), rest%%=60*100, ss=rest/100, cc=rest%%100"

	:: short variant
	rem if %mm% lss 10 set "mm=0%mm%"
	rem if %ss% lss 10 set "ss=0%ss%"
	rem if %cc% lss 10 set "cc=0%cc%"
	rem set "hh=%hh%:"
	rem set "mm=%mm%:"
	
	:: writing variant
	if "%hh%"=="0" (set "hh=") else (if "%hh%"=="1" (set "hh=1 hour ")   else (set "hh=%hh% hours "))
	if "%mm%"=="0" (set "mm=") else (if "%mm%"=="1" (set "mm=1 minute ") else (set "mm=%mm% minutes "))
	if "%hh%%mm%"=="" (set "ss=%ss%,%cc% seconds") else (if "%ss%"=="1" (set "ss=%ss% second") else (set "ss=%ss% seconds")) 
	
	echo __________________________________________
	echo.
	%textcolor% yellow
	echo Total time: %hh%%mm%%ss%.
	%textcolor% grey
	echo __________________________________________
	echo>>"%MapFile%.log" All operations completed.
	echo>>"%MapFile%.log" Total time: %hh%%mm%%ss%.
exit /b

:killproc
	for /f "tokens=1" %%m in ('tasklist /NH') do (
		if /i "%%~m"=="%~1" (taskkill /f /im "%~1"> nul)
	)
exit /b
