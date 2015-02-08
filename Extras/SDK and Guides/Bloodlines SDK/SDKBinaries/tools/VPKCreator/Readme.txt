 Vampire Bloodlines' VPK Creator
--------------------------------

This command-line utility was written by me in order to facilitate the packaging of its own game content into the VPK game archives and to minimize dancing with a tambourine that many at the same time there were (and maybe at all, not many people have tried to do this because of the relative complexity of packing settings, or lack of packaging setting-files in defective pirate game versions). In this case, you can easily create your own patches and localizations in a convenient form, allowing to keep the original content and prevent it from being overwritten (for example, it is helpful in restoring game to the original version without having to dig through a pile of unpacked stuff).

Features:
* The program interface is intuitive: to select a particular action you should enter the number corresponding to it, and then follow the screen instructions.
* No file operations pack_values.txt required (you can completely forget about its existence): the program could then choose the desired settings for a particular mode of operation.
* When you select "Pack all game content (<mode>)", it packs full uncompressed content, while also copied all non-packable but required game files. That is, after all the procedures over, we have the finished, compressed version of the game.
* All generated files are placed into the "PACKED" dir near to Vampire.exe (for later viewing, selecting the desired name and/or moving it to game dir). If you select "Pack the Specific folders", but the "Vampire" dir already has some VPK-file, then the generated file is placed next to them, with a larger (per unit) archive number.
* When you created an archive, you can delete unzipped content version (by program built-in feature), since they no longer needed in game.

Note:
This tool will launch the game engine and send the different commands to this, so you should to wait when process finished.

Engine reading order:
If there are the files with same names in different VPK-archives, the game engine will read these files from .vpk that have larger number. That is, "pack011.vpk" file will have a higher priority than "pack003.vpk". The archives with "1xx" numbers vice-versa have a lower priority versus "0xx", so it's not recommended to use them anyway.
When a user extracts a resource from the .vpk file and places it within the Vampires installation directory (directory structure intact), the game engine will load the users uncompress version on startup instead of the one in the VPK file. While this design allows user mods, the downside is that it only allows 1 User Mod to be installed at a time.

// written by psycho-a
