@echo off
setlocal ENABLEEXTENSIONS
pushd ..
set "MapSrcDir=%CD%\SDKContent\MapSrc"
set "WcRegistry=HKCU\Software\Troika\Hammer"
popd

:recentfix	-TEMPORARY!
set "FileCount=0"
if exist "%MapSrcDir%\*.vmf" (
	for /f "delims=" %%a in ('sfk.exe list -old -notime "%MapSrcDir%" .vmf') do (
		call :recentproc "%%~a"
	)
)

:runhammer
start wc.exe
exit

:recentproc
	set /A "FileCount=%FileCount%+1"
	reg add "%WcRegistry%\Recent File List" /v "File%FileCount%" /t REG_SZ /d "%~1" /f
exit /b
