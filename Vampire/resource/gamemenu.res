"GameMenu"
{
	"1"
	{
		"label" "#GameUI_GameMenu_NewGame"
		"command" "OpenNewGameDialog"
	}
	"2"
	{
		"label" "#GameUI_GameMenu_LoadGame"
		"command" "OpenLoadGameDialog"
	}
	"3"
	{
		"name" "SaveGame"
		"label" "#GameUI_GameMenu_SaveGame"
		"command" "OpenSaveGameDialog"
	}
	"4"
	{
		"label" "#GameUI_GameMenu_Multiplayer"
		"SubMenu"
		{
			"1"
			{
				"label" "#GameUI_GameMenu_FindServers"
				"command" "OpenServerBrowser"
			}
			"2"
			{
				"label" "#GameUI_GameMenu_Customize"
				"command" "OpenMultiplayerCustomizeDialog"
			}
			"3"
			{
				"label" "#GameUI_GameMenu_CreateServer"
				"command" "OpenCreateMultiplayerGameDialog"
			}
		}
	}
	"5"
	{
		"label" "#GameUI_GameMenu_Options"
		"command" "OpenOptionsDialog"
	}
	"6"
	{
		"label" "#GameUI_GameMenu_Quit"
		"command" "Quit"
	}
}