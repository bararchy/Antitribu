-------------------
Bloodlines SDK 
-------------------

This is an unofficial software developer's kit (SDK) for Vampire - The Masquerade: Bloodlines, the greatest game of all time developed by Troika Games in 2004. Unfortunately, the company quickly went bust, and the official toolkits have not been released, thus leaving modmakers with nothing. As recently a lot of tech-information of the game became available, a team of enthusiasts decided to revive the modmakers movement, by developing this devkit.

-------------------

Installation:

The "SDKBinaries", "SDKContent", "Vampire" dirs and "BloodlinesSDK.exe" file must be placed inside the directory where the main "Vampire.exe" file is.
If you run the SDK for the first time, it will be configured automatically. 
After this, you can choose to unpack your game's content (to be visible in the SDK), this procedure is automatic too. 
Now the SDK is ready. Just run "BloodlinesSDK.exe" to start your works.
If you have problems with game configuration and editor display settings, run the "Reset SDK Configuration" procedure from the main menu.
You also may override the standard game subdirectory path - use "Change Path to Game Dir" option from the SDK main menu.

-------------------

At this moment the project is not fully completed, but already it can be used to do the following (with some limitations): 

* Create, edit and compile your own maps.
* Create, view and compile game models (animations are still not supported properly).
* Decompile game maps and models for editing.
* View, manage, extract and create game archives (.vpk files).
* View and convert game textures between tth/ttz, vtf, tga and dds formats.
* Edit game dialogues (lipsync files are not supported yet).
* Manage entity data in existing BSP map files (paste, delete and change entity properties).
* Validate misc game resources.

-------------------

This SDK includes various third-party tools, in particular:

* Source SDK GUI (developed by Valve Software, customized by Psycho-A)
* PackFile Explorer v3.9 (developed by Dave Gaunt)
* MDL 2 SMD Beta (developed by Daedalus from Bloodlines Revival project - http://bloodlinesresurgencemod.com)
* BSPSource v1.3.14 (VMEx modification, developed by Barracuda - http://ata4.info/bspsrc/about.html)
* BSPInfo v1.3.14 (BSPSrc extension, developed by Barracuda - http://ata4.info/bspsrc/about.html)
* VPKTool v3.9a (Quick and dirty Bloodlines Tools, developed by Turvy)
* Bloodlines Dialogue Editor (developed by Raptor for Paradise#77 - http://go.to/paradise77)
* EntSpy v0.8 (developed by Rof - http://bagthorpe.org/bob/cofrdrbob/entspy.html)
* BSPEdit v1.09 (developed by Robert Morley - http://www.rob.patcroteau.com)
* BSPDetail v1.00 (developed by DDLullu - http://planet-vampire.net/forum/index.php?action=profile;u=3672)
* VTMBedit Tool (developed by David Arneson [xatmos])
* VExtract (developed by Daedalus from Bloodlines Revival project - http://bloodlinesresurgencemod.com)
* VPK Creator (developed by Psycho-A - http://planet-vampire.net/forum/index.php?action=profile;u=5456)
* StudioMDL Compiler GUI (developed by InterWave Studios)
* MDLDecompressor (developed by DDLullu - http://planet-vampire.net/forum/index.php?action=profile;u=3672)
* Hammer Run Map Launcher (custom compile dialog, written by Psycho-A)
* kHED v1.1.5, low-poly model editor (developed by JDPhU - http://khed.glsl.ru)

-------------------

Additional tools (for advanced users):

* vview.exe - map viewer (opengl)
* glview.exe - map visleafs viewer (opengl)
* bspzip.exe - program for un/packing files sewn on the map
* vbspinfo.exe - program for getting information about the map

-------------------

The following tools required Java Runtime Environment (http://java.com/download) to be installed on your system:

* Model Decompiler
* BSPSource Decompiler
* BSPInfo Tool
* EntSpy BSP Tool
* PakRat Tool

-------------------

Usage limitations:

* The SDK requires the unpacked version of the game for now (maybe support for VPKs will be added later...)

<Advanced info>
* No Type 1 and 2 model support, without pre-fixing they load into Hammer or Model Viewer incorrectly (but will be OK inside the game).
* No correct animation support in multi-bone models - it means that we can't handle the animations in the Editor when creating maps.
* No full-featured model compiler and decompiler - only Type 0 models with no animations can be compiled.
* Not finalized FGD file (Hammer entity data) - there are still a lot of imprecisions and lack of info on some entity parameters.

-------------------

Project Developers:

* Fire64 (Programming, project CEO) [no support anymore].
* Psycho-A (Beta-testing, building, all successive works).

-------------------

Official project pages:

* Planet-Vampire Community: 
  http://planet-vampire.net/modules/files/view.php?id=759
  http://planet-vampire.net/forum/index.php?topic=5797.msg119400#msg119400
* V-Bloodlines.info (Russian Community):
  http://forum.v-bloodlines.info/topic8100.html

-------------------

For Programmers:
If you are interested in further project developing, please, read notes in the source code ("SRC") directory.

-- Psycho-A


-------------------
Version History:
-------------------

0.5:
- First public release.

0.55:
- Fixed generation of collision physics.
- Added generation of shadows for static models.
- Fixed handling of dynamic and physical models.
- Added program to view prop models.

0.57:
- In HLMV added partial support for models with a few bones (only for prop models, so far).
- Added model displaying to the Vampire Map Editor.
- Fixed function of copying maps.

0.7:
- Fixed construction of the skeleton of models with few bones.
- Fixed distortion vertices due to improper tension on the mesh skeleton.
- Fixed crash of high polygon models and models with flex animations.
- Model can be rotated in HLMV on all 3 axes now.
- Model in the Editor has static angles and does not change the position on moving the camera.
- Added FGD file with the entity VTMB.
- Added BAT file to automatically configure the editor.

0.78:
- Added Source SDK menu for easy access to all SDK utilities.
- Added completed FGD file for access to all game entities.
- Replaced VampEd with newer and better PackFile Explorer 3.9.
- Added "MDL 2 SMD" model decompiler by CodenameV.
- Replaced "VMEx" with new advanced "BSPSource" map decompiler.
- Fixed conflicts between Vampire Hammer and new Valve's ones (need to run "AutoConfig.bat" to reconfigure).
- Added Studiomodel compiler for compiling custom models (doesn't work properly - use $scale 250 to get the correct model dimensions).
- Fixed freezing in Hammer on rendering some models.
- Fixed cubemap's building on map compiling ('buildcubemaps' not available yet).
- Fixed hardware rendering of model skins in HLMV (now one can load almost all of the npc models).
- Added support for models with bone count of more than 128.
- Added full support for models having vertex format type 2.
- Added skeletal animation initial support (works crooked for now).

0.79:
- Reworked and improved SDK main menu (uncompatible with older versions - delete "VampireSDK\bin" folder before installation.
- Updated model compiler - fixed sizes and collision/hitboxes compilation (limitations: just 1 bone and 1 frame per model allowed).
- Added StudioMDL Compiler GUI for easy compiling of your models.
- Added VTMBedit Tool for managing and validating the misc game resources.
- Added VPK Creator utility for packing your content into .vpk game archives.
- Added EntSpy BSP editor for managing entity data on the maps.
- Added BSPEdit tool to edit specific entities like static props.
- Adapted to be included into Wesp5's Unofficial Patch.
- Added misc game-related community links.
- Added detailed readme file (the file you read now).
- Fixed some errors in FGD file.

0.79.2:
- Removed black background in Model Viewer.
- Removed error message on loading models with vertex type 2.
- In VBSP service VMT commands were added that allow to use specific game tooltextures.

0.8:
- Fixed multiple dirs support: now you can have two (extracted/original) game versions connected to SDK.
- Renamed "VampireSDK" folder to "SDKBinaries", and your maps and extracted content go to "SDKContent" folder.
- Renamed "Vampire SDK.exe" launcher to "BloodlinesSDK.exe" to be match new naming and avoid confusing with Redemption.
- Added MDLDecompressor to fix Type 1/2 models (and NPCs) after extraction, so they may be correctly loaded in Hammer.
- Added automatized Wizard (runs when you start SDK first) that allows to extract game's VPK and then run MDLDecompressor to fix models.
- Solved problem with 'spaces' in paths: The legacy compile commands/dialog were replaced with advanced custom one (in "Expert" mode).
- Fixed VProject's path detection in all SDK apps (now only GameCfg.ini settings considered) - no more errors on compiling maps.
- Added "BSPDetail" v1.0 utility (it places/edits detail props in maps) for SDK GUI access (Hammer can do that too :)).
- Updated "BSPSource" to version 1.3.13 with adding graphical "BSPInfo" tool to view various map features and configuration.
- Added modified version of "VTFEdit" tool for quick viewing of VTF and TTH textures, converting TTH to VTF and editing VTFs.
- Fixed all "editor" models (playerstart, nodes, etc.) to be correctly displayed as point entities in Hammer Editor.
- Added Launch Game, Extract VPKs, Decompress Models and Full SDK State Reset procedures accessable from the main menu.
- Optimized SDK launcher and service tools codes for better compatiblity with Windows 7 and filepaths with special symbols.
- Added auto-patching for apps' registry path and VProject on first SDK launch [for the future version SRC-compile(R)s].
- Fixed (partially) Hammer crash after compiling map when map was opened via Open Windows dialog (see "Known bugs" note).
- Default compile mode in Hammer turned to "Expert", so, more options are available now, and no more errors with Spaces on paths.
- Packfile Explorer now always uses GameDir (your game folder) as the default root directory.
- Added Explorer associations with main game/engine file types like TTH/VMT/VMF etc. TTH-s are now viewable by doubleckick.
- Improved SDK main menu interface: Since we have many tools, they are sorted by categories.
- Fixed "Planet-Vampire" and "Bloodlines Resurgence" links and removed "Team Camarilla" link (does not use this SDK).
- Updated the SDK readme.txt file; added information for future coders.

0.81:
- Optimized for Wesp5's Unofficial Patch including no more false warnings of Anti-viruses programs ;).
- Added kHED v1.1.5 low-poly model editor to create your own models (.vtf textures and .smd meshes are supported).
- Added ability to run the SDK from another (not Vampire's root) directories and added interface to specify the custom game paths.
- Improved wrong configuration detection on launching: now it causes a warning message and the full settings reset.
- Re-sorted tools on the SDK main menu to be the more convenient and removed still unused "Face Poser" program link.
- Removed models' broken animation enabled in Hammer 3D-View by default.
- Moved MDLDecompressor tool to "SDKBinaries" dir because it doesn't support dirs with tree depth more than 8 levels.
- Fixed "Launch Game" function in the main menu to be able to run the game from custom-defined paths.
- Updated "VPK Creator" tool to be able to work with games from custom-defined paths.
- Restored missing PakRat tool's JAR file in "Java-Based" dir.
- Minor interface fixes and tweaks.

0.82:
- Fixed patches being hardcoded before: VProject detection, Registry paths, Compile process window etc.
- Hammer: Finaly added full Python scripts support in "Outputs" section (read+write) - no more need to manually edit entity data!
- Hammer: Removed "Normal" compiile mode as an unnecessary and buggy, and removed an obsolete process window.
- Hammer, HLMV: Actualized all text data, removed all HL' crap and added actual Web-links to game's and mapping communities.
- Hammer, FGD file: Restored some unused in-game item classes that may be used in some advanced directions.
- FGD file: Fixed some entity inconsistencies and defects, and added some new parameters.
- Fixed setting-up 'ModDir' path as VProject path, and changed 'Game Directory' to Game's subdirecoty in some text mentions.
- Removed some unused content from the SDK binaries folder and decreased the target SDK distributive size.
- Updated VView.exe utility - increased window size, turned back control by hotkeys, etc.
- Restored ZLib.dll library that was missing in TTZViewer tool.
- Restored GLView.exe tool to view portal files (.prt) of compiling maps.
- Added SDK's source code target directory and programmer's notes document inside (includes code download links and user's guide).
- Updated readme: added links to official project pages and moved programmer's info to separate note in the source code subfolder.
- Corrected some SDK user interface issues, re-sorted maim menu programs and renamed title to "Bloodlines SDK".
- Fixed typo caused error on VPKs extraction in previous build.
- Other minor fixes and tweaks.

Known Bugs (see also programmer's notes):
- If you loaded a map file via standard "Open..." dialog, Hammer may crash after compiling the map on some machines. 
  To avoid this, you must open the map from Recent Files list. If map is not shown, open map once, do your works and then restart Hammer.
- Models of Type 1 and Type 2 (compressed) will be correctly managed in Editor and model browser after decompression only (see above).
