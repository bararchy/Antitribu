@echo off
if "%~1"=="" exit /b

:======== VTF Files =========
REG ADD "HKCR\.vtf" /f /ve  /t REG_SZ /d "Wunderboy.ShellExtensions.VTFFile"
REG ADD "HKCR\Wunderboy.ShellExtensions.VTFFile" /f /ve  /t REG_SZ /d "Valve Texture Format"
REG ADD "HKCR\Wunderboy.ShellExtensions.VTFFile" /f /v "EditFlags" /t REG_DWORD /d 0
REG ADD "HKCR\Wunderboy.ShellExtensions.VTFFile" /f /v "BrowserFlags" /t REG_DWORD /d 8
REG ADD "HKCR\Wunderboy.ShellExtensions.VTFFile\shell\open\command" /f /ve /t REG_SZ /d "\"%SDKRoot%\tools\TTZView\VTFEdit.exe\" \"%%1\""
REG ADD "HKCR\Wunderboy.ShellExtensions.VTFFile\DefaultIcon" /f /ve /t REG_SZ /d "%FAPath%\icon_vtf.ico,0"

:======== TTZ Files =========
REG ADD "HKCR\.ttz" /f /ve /t REG_SZ /d "TTZFile"
REG ADD "HKCR\TTZFile" /f /ve /t REG_SZ /d "Troika Texture Format"
REG ADD "HKCR\TTZFile" /f /v "EditFlags" /t REG_DWORD /d 0
REG ADD "HKCR\TTZFile" /f /v "BrowserFlags" /t REG_DWORD /d 8
REG ADD "HKCR\TTZFile\shell" /f /ve                 /t REG_SZ /d "View"
REG ADD "HKCR\TTZFile\shell\View" /f /ve            /t REG_SZ /d "View"
REG ADD "HKCR\TTZFile\shell\Convert" /f /ve         /t REG_SZ /d "Convert to VTF..."
REG ADD "HKCR\TTZFile\shell\View\command" /f /ve    /t REG_SZ /d "\"%SDKRoot%\tools\TTZView\TTZView.exe\" \"%%1\""
REG ADD "HKCR\TTZFile\shell\Convert\command" /f /ve /t REG_SZ /d "\"%SDKRoot%\tools\TTZView\TTZView.exe\" \"%%1\" -convert"
REG ADD "HKCR\TTZFile\DefaultIcon" /f /ve /t REG_SZ /d "%FAPath%\icon_ttz.ico,0"

:======== VMT Files =========
REG ADD "HKCR\.vmt" /f /ve /t REG_SZ /d "VMTFile"
REG ADD "HKCR\VMTFile" /f /ve  /t REG_SZ /d "Valve Material File"
REG ADD "HKCR\VMTFile" /f /v "EditFlags" /t REG_DWORD /d 0
REG ADD "HKCR\VMTFile" /f /v "BrowserFlags" /t REG_DWORD /d 8
REG ADD "HKCR\VMTFile\shell" /f /ve  /t REG_SZ /d "Open"
REG ADD "HKCR\VMTFile\shell\Open\command" /f /ve  /t REG_SZ /d "Notepad.exe \"%%1\""
REG ADD "HKCR\VMTFile\DefaultIcon" /f /ve /t REG_SZ /d "%FAPath%\icon_vmt.ico,0"

:======== VMF Files =========
REG ADD "HKCR\.vmf" /f /ve  /t REG_SZ /d "VMFFile"
REG ADD "HKCR\VMFFile" /f /ve  /t REG_SZ /d "Valve Map File"
REG ADD "HKCR\VMFFile" /f /v "EditFlags" /t REG_DWORD /d 0
REG ADD "HKCR\VMFFile" /f /v "BrowserFlags" /t REG_DWORD /d 8
REG ADD "HKCR\VMFFile\shell\Notepad" /f /ve /t REG_SZ /d "Open with Notepad"
REG ADD "HKCR\VMFFile\shell\Notepad\command" /f /ve  /t REG_SZ /d "notepad.exe \"%%1\""
REG ADD "HKCR\VMFFile\DefaultIcon" /f /ve /t REG_SZ /d "%FAPath%\icon_vmf.ico,0"

:======== VPK Files =========
REG ADD "HKCR\.vpk" /f /ve  /t REG_SZ /d "VPKFile"
REG ADD "HKCR\VPKFile" /f /ve  /t REG_SZ /d "Vampire Pack File"
REG ADD "HKCR\VPKFile" /f /v "EditFlags" /t REG_DWORD /d 0
REG ADD "HKCR\VPKFile" /f /v "BrowserFlags" /t REG_DWORD /d 8
REG ADD "HKCR\VPKFile\shell" /f /ve /t REG_SZ /d "VPKTool"
REG ADD "HKCR\VPKFile\shell\VPKTool\command" /f /ve /t REG_SZ /d "\"%SDKRoot%\tools\VPKTool\VPKTool.exe\" V \"%%1\""
REG ADD "HKCR\VPKFile\DefaultIcon" /f /ve /t REG_SZ /d "%FAPath%\icon_pak.ico,0"

:======== CFG Files =========
REG ADD "HKCR\.cfg" /f /ve  /t REG_SZ /d "inifile"

:======== QC Files =========
REG ADD "HKCR\.qc" /f /ve  /t REG_SZ /d "QCFile"
REG ADD "HKCR\QCFile" /f /ve  /t REG_SZ /d "Model Compile Parameters"
REG ADD "HKCR\QCFile" /f /v "EditFlags" /t REG_DWORD /d 0
REG ADD "HKCR\QCFile" /f /v "BrowserFlags" /t REG_DWORD /d 8
REG ADD "HKCR\QCFile\shell" /f /ve  /t REG_SZ /d "open"
REG ADD "HKCR\QCFile\shell\open" /f /ve  /t REG_SZ /d "Open"
REG ADD "HKCR\QCFile\shell\open\command" /f /ve  /t REG_SZ /d "NOTEPAD.EXE \"%%1\""
REG ADD "HKCR\QCFile\DefaultIcon" /f /ve /t REG_SZ /d "shell32.dll,69"

:======== SMD Files =========
REG ADD "HKCR\.smd" /f /ve  /t REG_SZ /d "txtfile"

:======== RAD Files =========
REG ADD "HKCR\.rad" /f /ve  /t REG_SZ /d "VRADFile"
REG ADD "HKCR\VRADFile" /f /ve  /t REG_SZ /d "Lighting Parameters"
REG ADD "HKCR\VRADFile" /f /v "EditFlags" /t REG_DWORD /d 0
REG ADD "HKCR\VRADFile" /f /v "BrowserFlags" /t REG_DWORD /d 8
REG ADD "HKCR\VRADFile\shell" /f /ve  /t REG_SZ /d "open"
REG ADD "HKCR\VRADFile\shell\open" /f /ve /t REG_SZ /d "Open"
REG ADD "HKCR\VRADFile\shell\open\command" /f /ve  /t REG_SZ /d "NOTEPAD.EXE \"%%1\""
REG ADD "HKCR\VRADFile\DefaultIcon" /f /ve /t REG_SZ /d "shell32.dll,69"

:======== VBSP Files =========
REG ADD "HKCR\.vbsp" /f /ve /t REG_SZ /d "VBSPFile"
REG ADD "HKCR\VBSPFile" /f /ve /t REG_SZ /d "World Detail Parameters"
REG ADD "HKCR\VBSPFile" /f /v "EditFlags" /t REG_DWORD /d 0
REG ADD "HKCR\VBSPFile" /f /v "BrowserFlags" /t REG_DWORD /d 8
REG ADD "HKCR\VBSPFile\shell" /f /ve /t REG_SZ /d "open"
REG ADD "HKCR\VBSPFile\shell\open" /f /ve /t REG_SZ /d "Open"
REG ADD "HKCR\VBSPFile\shell\open\command" /f /ve  /t REG_SZ /d "NOTEPAD.EXE \"%%1\""
REG ADD "HKCR\VBSPFile\DefaultIcon" /f /ve /t REG_SZ /d "shell32.dll,69"

:======== FGD Files =========
REG ADD "HKCR\.fgd" /f /ve /t REG_SZ /d "FGDFile"
REG ADD "HKCR\FGDFile" /f /ve /t REG_SZ /d "Game Definition File"
REG ADD "HKCR\FGDFile" /f /v "EditFlags" /t REG_DWORD /d 0
REG ADD "HKCR\FGDFile" /f /v "BrowserFlags" /t REG_DWORD /d 8
REG ADD "HKCR\FGDFile\shell" /f /ve  /t REG_SZ /d "open"
REG ADD "HKCR\FGDFile\shell\open" /f /ve /t REG_SZ /d "Open"
REG ADD "HKCR\FGDFile\shell\open\command" /f /ve  /t REG_SZ /d "NOTEPAD.EXE \"%%1\""
REG ADD "HKCR\FGDFile\DefaultIcon" /f /ve /t REG_SZ /d "shell32.dll,69"

exit /b