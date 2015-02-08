@echo off
setlocal ENABLEEXTENSIONS

:vars
pushd "%~dp0"
set "JarFile=%cd%\%~2"
set "MsgBox=%cd%\..\..\msgbox.exe"
set "ErrorMsg=Java Runtime Environment must be installed on your system to run this program. Would you like to download and install it now?"

:changeworkdir
if exist "..\..\..\Vampire\maps" (pushd "..\..\..\Vampire\maps") else (pushd "..\..\..")

:checkjava
for %%M in (
	"%SystemRoot%\system32"
	"%SystemRoot%\syswow64"
	"%ProgramFiles%\Java\jre6\bin"
	"%ProgramW6432%\Java\jre6\bin"
	"%ProgramFiles%\Java\jre7\bin"
	"%ProgramW6432%\Java\jre7\bin"
) do if exist "%%~M\java.exe" (
	start /b "java" "%%~M\java.exe" %1 "%JarFile%" %3 %4 %5 %6 %7 %8 %9
	exit
)

:ifnotfound
start /w "message" "%MsgBox%" %ErrorMsg% /c:Error /t:MB_ICONSTOP,MB_YESNO

if "%ErrorLevel%"=="6" (start "url" "http://www.java.com/getjava")
exit
