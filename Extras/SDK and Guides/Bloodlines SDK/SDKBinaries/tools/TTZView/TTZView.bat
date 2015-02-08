@echo off
setlocal ENABLEEXTENSIONS

:check
if "%~1"=="" (
	start ..\..\MsgBox.exe Idle launch mode works with VTF format only. To view TTZ files, doubleclick on them in the Windows Explorer. To convert edited VTF to TTh+TTz, use VPKTool from the SDK menu. /c:TTZView - Warning /t:MB_SYSTEMMODAL,MB_ICONWARNING
	VTFEdit.exe
	exit
)

for %%m in (tth ttz) do (
if not exist "%~dpn1.%%m" (
	start ..\..\MsgBox.exe This file cannot be opened. /c:Error /t:MB_ICONWARNING
	exit
))

:convert
ttz2vtf.exe "%~dpn1.ttz"
if /i "%~2"=="-convert" exit

:check2
if not exist "%~dpn1.vtf" (
	start ..\..\MsgBox.exe Error opening file. /c:Error /t:MB_ICONERROR
	exit
)

:view
VTFEdit.exe "%~dpn1.vtf"

:finish
del /a /q "%~dpn1.vtf"
exit
