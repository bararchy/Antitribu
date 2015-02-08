///////////////////////////////////////////////////////////
// Tracker scheme resource file
//
// sections:
//		Colors			- all the colors used by the scheme
//		BaseSettings	- contains settings for app to use to draw controls
//		Fonts			- list of all the fonts used by app
//		Borders			- description of all the borders
//
// hit ctrl-alt-shift-R in the app to reload this file
//
///////////////////////////////////////////////////////////
Scheme
{
	//////////////////////// COLORS ///////////////////////////
	// color details
	// this is a list of all the colors used by the scheme
	Colors
	{
		// base colors
		"BaseText"		"216 222 211 255"		// used in text windows, lists
		"BrightBaseText" "255 255 255 255"	// brightest text
		"DimBaseText"	"150 159 142 255"		// dim base text
		
		"LabelDimText"	"160 170 149 255"		// slight modification on above, used for info text
												// could be just removed and use DimBaseText?
		
		"ControlText"	"216 222 211 255"		// used in all text controls
//		"BrightControlText"	"196 181 80 255"	// use for selected controls
/////		"BrightControlText"	"0 210 255 255"	// use for selected controls
/////		"BrightControlText"	"125 167 217 255"	// use for selected controls
"BrightControlText"	"109 207 246 255"	// use for selected controls
		"DisabledText1"	"117 128 111 255"		// disabled text
		"DisabledText2"	"30 30 30 255"		// overlay color for disabled text (to give that inset look)

		// background colors
//		"ControlBG"		"76 88 68 255"		// background color of controls
//		"ControlDarkBG" "90 106 80 255"		// darker background color; used for background of scrollbars
//		"WindowBG"		"62 70 55 255"		// background color of text edit panes (chat, text entries, etc.)
//		"SelectionBG"	"149 136 49 255"		// background color of any selected text or menu item

// Ghosted version...
//"ControlBG"		"76 88 68 96"		// background color of controls
//"ControlDarkBG" "90 106 80 96"		// darker background color; used for background of scrollbars
//"WindowBG"		"62 70 55 96"		// background color of text edit panes (chat, text entries, etc.)
//"SelectionBG"	"149 136 49 96"		// background color of any selected text or menu item

// Black version
"ControlBG"		"0 0 0 255"		// background color of controls
"ControlDarkBG" "0 0 0 255"		// darker background color; used for background of scrollbars
"WindowBG"		"0 0 0 255"		// background color of text edit panes (chat, text entries, etc.)
"SelectionBG"	"0 0 0 255"		// background color of any selected text or menu item

// Red version
//"ControlBG"		"255 0 0 255"		// background color of controls
//"ControlDarkBG" "0 0 0 255"		// darker background color; used for background of scrollbars
//"WindowBG"		"255 0 0 255"		// background color of text edit panes (chat, text entries, etc.)
//"SelectionBG"	"0 0 0 255"		// background color of any selected text or menu item

		"VSelectedText"		"255 210 0 255"
//		"GhostControlBG"		"76 88 68 96"		// background color of controls
//		"GhostControlDarkBG" "90 106 80 96"		// darker background color; used for background of scrollbars
//		"GhostWindowBG"		"62 70 55 96"		// background color of text edit panes (chat, text entries, etc.)
//		"GhostSelectionBG"	"149 136 49 96"		// background color of any selected text or menu item
		"GhostControlBG"		"0 0 0 0"		// background color of controls
		"GhostControlDarkBG"	"0 0 0 0"		// darker background color; used for background of scrollbars
		"GhostWindowBG"			"0 0 0 0"		// background color of text edit panes (chat, text entries, etc.)
		"GhostSelectionBG"		"0 0 0 0"		// background color of any selected text or menu item

		// title colors
//		"TitleText"		"255 255 255 255"
		"TitleText"		"255 5 5 96"
		"TitleDimText"	"120 132 114 255"
		"TitleBG"		"76 88 68 0"
		"TitleDimBG"	"76 88 68 0"

		// border colors
		"BorderBright"	"232 208 167 255"		// the lit side of a control
		"BorderDark"	"202 178 137 255"		// the dark/unlit side of a control
		"BorderSelection"	"0 0 0 255"		// the additional border color for displaying the default/selected button
	}

	///////////////////// BASE SETTINGS ////////////////////////
	//
	// default settings for all panels
	// controls use these to determine their settings
	BaseSettings
	{
		"FgColor"			"ControlText"
		"BgColor"			"ControlBG"
		"LabelBgColor"		"ControlBG"
		"SubPanelBgColor"	"ControlBG"

		"DisabledFgColor1"		"DisabledText1" 
		"DisabledFgColor2"		"DisabledText2"		// set this to the BgColor if you don't want it to draw

		"TitleBarFgColor"			"TitleText"
		"TitleBarDisabledFgColor"	"TitleDimText"
		"TitleBarBgColor"			"TitleBG"
		"TitleBarDisabledBgColor"	"TitleDimBG"

//		"TitleBarIcon"				"resource/icon_steam"
//		"TitleBarDisabledIcon"		"resource/icon_steam_disabled"
		"TitleBarIcon"				"resource/icon_hlicon1"
		"TitleBarDisabledIcon"		"resource/icon_hlicon2"

		"TitleButtonFgColor"			"BorderBright"
		"TitleButtonBgColor"			"ControlBG"
		"TitleButtonDisabledFgColor"	"TitleDimText"
		"TitleButtonDisabledBgColor"	"TitleDimBG"

		"TextCursorColor"			"BaseText"		// color of the blinking text cursor in text entries
		"URLTextColor"				"BrightBaseText"		// color that URL's show up in chat window

		Menu
		{
			"FgColor"			"DimBaseText"
			"BgColor"			"ControlBG"
			"ArmedFgColor"		"BrightBaseText"
			"ArmedBgColor"		"SelectionBG"
			"DividerColor"		"BorderDark"

			"TextInset"			"6"
		}

		MenuButton	  // the little arrow on the side of boxes that triggers drop down menus
		{
			"ButtonArrowColor"	"DimBaseText"	// color of arrows
		   	"ButtonBgColor"		"WindowBG"	// bg color of button. same as background color of text edit panes 
			
			"ArmedArrowColor"		"BrightBaseText" // color of arrow when mouse is over button
			"ArmedBgColor"		"DimBaseText"  // bg color of button when mouse is over button
		}

		Slider
		{
			"SliderFgColor"		"ControlBG"		// handle with which the slider is grabbed
			"SliderBgColor"		"ControlDarkBG"		// area behind handle
		}

		ScrollBarSlider
		{
			"BgColor"			"ControlBG"		// this isn't really used

			"ScrollBarSliderFgColor"		"ControlBG"		// handle with which the slider is grabbed
			"ScrollBarSliderBgColor"		"ControlDarkBG"		// area behind handle

			"ButtonFgColor"		"DimBaseText"	// color of arrows
		}


		// text edit windows
		"WindowFgColor"				"BaseText"		// off-white
		"WindowBgColor"				"WindowBG"
		"WindowDisabledFgColor"		"DimBaseText"
		"WindowDisabledBgColor"		"66 80 60 255"		// background of chat conversation

		"SelectionFgColor"			"255 255 255 255"		// fg color of selected text
		"SelectionBgColor"			"SelectionBG"
		"ListSelectionFgColor"		"255 255 255 255"			// 

		"ListBgColor"				"80 65 47 255"	// background of server browser control, etc
		"BuddyListBgColor"			"80 65 47 255"	// background of buddy list pane
		
		// App-specific stuff
		"ChatBgColor"				"WindowBgColor"

		// status selection
		"StatusSelectFgColor"		"BrightBaseText"
		"StatusSelectFgColor2"		"BrightControlText"		// this is the color of the friends status

		// checkboxes
		"CheckButtonBorder1"   		"BorderDark" 		// the left checkbutton border
		"CheckButtonBorder2"   		"BorderBright"		// the right checkbutton border
		"CheckButtonCheck"			"0 0 0 255"				// color of the check itself
		"CheckBgColor"				"158 168 150 255"

		// buttons (default fg/bg colors are used if these are not set)
//		"ButtonArmedFgColor"
//		"ButtonArmedBgColor"
//		"ButtonDepressedFgColor"	"BrightControlText"
//		"ButtonDepressedBgColor"

		// buddy buttons
		BuddyButton
		{
			"FgColor1"		"ControlText"
			"FgColor2"		"117 134 102 255"

			"ArmedFgColor1"	"BrightBaseText"
			"ArmedFgColor2"	"BrightBaseText"
			"ArmedBgColor"	"SelectionBG"
		}

		Chat
		{
			"TextColor"				"BrightControlText"
			"SelfTextColor"			"BaseText"
			"SeperatorTextColor"	"DimBaseText"
		}

		"SectionTextColor"		"BrightControlText"		// text color for IN-GAME, ONLINE, OFFLINE sections of buddy list
		"SectionDividerColor"	"BorderDark"		// color of line that runs under section name in buddy list

		// TF2 HUD
		"HudStatusBgColor"			"0 0 0 64"
		"HudStatusSelectedBgColor"	"0 0 0 192"
	}

	//
	//////////////////////// FONTS /////////////////////////////
	//
	// describes all the fonts
	Fonts
	{
		// fonts are used in order that they are listed
		// fonts listed later in the order will only be used if they fulfill a range not already filled
		// if a font fails to load then the subsequent fonts will replace
		"Default"
		{
			"1"
			{
				"name"		"Tahoma"
//				"name"		"Percolator Expert"
				"tall"		"16"
				"weight"	"500"
//				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
			"2"
			{
				"name"		"Arial Unicode MS"
//				"name"		"Percolator Expert"
				"tall"		"16"
				"weight"	"500"
//				"range"		"0x0000 0xFFFF"	//	all
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}
		"DefaultUnderline"
		{
			"1"
			{
				"name"		"Tahoma"
				"tall"		"16"
				"weight"	"500"
				"underline" "1"
//				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
			"2"
			{
				"name"		"Arial Unicode MS"
				"tall"		"16"
				"weight"	"500"
				"underline" "1"
//				"range"		"0x0000 0xFFFF"	//	all
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}
		"DefaultSmall"
		{
			"1"
			{
				"name"		"Tahoma"
				"tall"		"13"
				"weight"	"0"
//				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
			"2"
			{
				"name"		"Arial Unicode MS"
				"tall"		"13"
				"weight"	"0"
//				"range"		"0x0000 0xFFFF"	//	all
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}
		"DefaultVerySmall"
		{
			"1"
			{
				"name"		"Tahoma"
				"tall"		"12"
				"weight"	"0"
//				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
			"2"
			{
				"name"		"Arial Unicode MS"
				"tall"		"12"
				"weight"	"0"
//				"range"		"0x0000 0xFFFF"	//	all
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"DefaultLarge"
		{
			"1"
			{
				"name"		"Tahoma"
				"tall"		"18"
				"weight"	"0"
//				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
			"2"
			{
				"name"		"Arial Unicode MS"
				"tall"		"18"
				"weight"	"0"
//				"range"		"0x0000 0xFFFF"	//	all
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		// this is the symbol font
		"Marlett"
		{
			"1"
			{
				"name"		"Marlett"
				"tall"		"14"
				"weight"	"0"
				"symbol"	"1"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"Trebuchet24"
		{
			"1"
			{
				"name"		"Trebuchet MS"
				"tall"		"24"
				"weight"	"900"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}


		"Trebuchet20"
		{
			"1"
			{
				"name"		"Trebuchet MS"
				"tall"		"20"
				"weight"	"900"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

		"Trebuchet18"
		{
			"1"
			{
				"name"		"Trebuchet MS"
				"tall"		"18"
				"weight"	"900"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}

// Vampire Fonts
		"PercolatorMedium"
		{
			"1"
			{
				"name"		"Percolator Expert"
				"tall"		"35"
				"weight"	"1000"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}
		"PercolatorSmall"
		{
			"1"
			{
				"name"		"Percolator Expert"
				"tall"		"26"
				"weight"	"1000"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}
		"Copperplate"
		{
			"1"
			{
				"name"		"Copperplate Gothic BT"
				"tall"		"18"
				"weight"	"1000"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}
		"Dominican"
		{
			"1"
			{
				"name"		"Dominican"
//				"tall"		"19"
				"tall"		"22"
				"weight"	"1000"
//				"range"		"0x0000 0x007F"	//	Basic Latin
				"range"		"0x0000 0x00ff" //	Vampire fonts should be ANSI-1252 compliant
			}
		}
	}

	//
	//////////////////// BORDERS //////////////////////////////
	//
	// describes all the border types
	Borders
	{
		BaseBorder
		{
			"inset" "0 0 1 1"
			Left
			{
				"1"
				{
//					"color" "BorderDark"
					"color" "BorderBright"
					"offset" "0 1"
				}
			}

			Right
			{
				"1"
				{
					"color" "BorderBright"
					"offset" "1 0"
				}
			}

			Top
			{
				"1"
				{
//					"color" "BorderDark"
					"color" "BorderBright"
					"offset" "0 0"
				}
			}

			Bottom
			{
				"1"
				{
					"color" "BorderBright"
					"offset" "0 0"
				}
			}
		}
		
		TitleButtonBorder
		{
			"inset" "0 0 1 1"
			Left
			{
				"1"
				{
					"color" "BorderBright"
					"offset" "0 1"
				}
			}

			Right
			{
				"1"
				{
					"color" "BorderDark"
					"offset" "1 0"
				}
			}

			Top
			{
				"4"
				{
					"color" "BorderBright"
					"offset" "0 0"
				}
			}

			Bottom
			{
				"1"
				{
					"color" "BorderDark"
					"offset" "0 0"
				}
			}
		}

		TitleButtonDisabledBorder
		{
			"inset" "0 0 1 1"
			Left
			{
				"1"
				{
					"color" "BgColor"
					"offset" "0 1"
				}
			}

			Right
			{
				"1"
				{
					"color" "BgColor"
					"offset" "1 0"
				}
			}
			Top
			{
				"1"
				{
					"color" "BgColor"
					"offset" "0 0"
				}
			}

			Bottom
			{
				"1"
				{
					"color" "BgColor"
					"offset" "0 0"
				}
			}
		}

		TitleButtonDepressedBorder
		{
			"inset" "1 1 1 1"
			Left
			{
				"1"
				{
					"color" "BorderDark"
					"offset" "0 1"
				}
			}

			Right
			{
				"1"
				{
					"color" "BorderBright"
					"offset" "1 0"
				}
			}

			Top
			{
				"1"
				{
					"color" "BorderDark"
					"offset" "0 0"
				}
			}

			Bottom
			{
				"1"
				{
					"color" "BorderBright"
					"offset" "0 0"
				}
			}
		}

		ScrollBarButtonBorder
		{
			"inset" "2 2 0 0"
			Left
			{
				"1"
				{
					"color" "BorderBright"
					"offset" "0 1"
				}
			}

			Right
			{
				"1"
				{
					"color" "BorderDark"
					"offset" "1 0"
				}
			}

			Top
			{
				"1"
				{
					"color" "BorderBright"
					"offset" "0 0"
				}
			}

			Bottom
			{
				"1"
				{
					"color" "BorderDark"
					"offset" "0 0"
				}
			}
		}

		ButtonBorder2
		{
			"inset" "0 0 1 1"
			Left
			{
			}
			Right
			{
			}

			Top
			{
			}

			Bottom
			{
			}
		}

		OldButtonBorder
		{
			"inset" "0 0 1 1"
			Left
			{
				"1"
				{
					"color" "BorderBright"
					"offset" "0 1"
				}
			}

			Right
			{
				"1"
				{
					"color" "BorderDark"
					"offset" "0 0"
				}
			}

			Top
			{
				"1"
				{
					"color" "BorderBright"
					"offset" "0 1"
				}
			}

			Bottom
			{
				"1"
				{
					"color" "BorderDark"
					"offset" "0 0"
				}
			}
		}

		TabBorder
		{
			"inset" "0 0 1 1"
			Left
			{
			}

			Right
			{
			}

			Top
			{
			}

			Bottom
			{
			}
		}

		OldTabBorder
		{
			"inset" "0 0 1 1"
			Left
			{
				"1"
				{
					"color" "BorderBright"
					"offset" "0 1"
				}
			}

			Right
			{
				"1"
				{
					"color" "BorderDark"
					"offset" "1 0"
				}
			}

			Top
			{
				"1"
				{
					"color" "BorderBright"
					"offset" "0 0"
				}
			}

			Bottom
			{
				"1"
				{
					"color" "BorderBright"
					"offset" "0 0"
				}
			}
		}

		TabActiveBorder
		{
			"inset" "0 0 1 0"
			Left
			{
			}

			Right
			{
			}

			Top
			{
			}

			Bottom
			{
			}
		}


		OldTabActiveBorder
		{
			"inset" "0 0 1 0"
			Left
			{
				"1"
				{
					"color" "BorderBright"
					"offset" "0 0"
				}
			}

			Right
			{
				"1"
				{
					"color" "BorderDark"
					"offset" "1 0"
				}
			}

			Top
			{
				"1"
				{
					"color" "BorderBright"
					"offset" "0 0"
				}
			}

			Bottom
			{
				"1"
				{
					"color" "ControlBG"
					"offset" "6 2"
				}
			}
		}


		ToolTipBorder
		{
			"inset" "0 0 1 0"
			Left
			{
				"1"
				{
					"color" "BorderDark"
					"offset" "0 0"
				}
			}

			Right
			{
				"1"
				{
					"color" "BorderDark"
					"offset" "1 0"
				}
			}

			Top
			{
				"1"
				{
					"color" "BorderDark"
					"offset" "0 0"
				}
			}

			Bottom
			{
				"1"
				{
					"color" "BorderDark"
					"offset" "0 0"
				}
			}
		}

		OldButtonKeyFocusBorder2
		{
			"inset" "0 0 1 1"
			Left
			{
			}
			Right
			{
			}

			Top
			{
			}

			Bottom
			{
			}
		}

		// this is the border used for default buttons (the button that gets pressed when you hit enter)
		OldButtonKeyFocusBorder
		{
			"inset" "0 0 1 1"
			Left
			{
				"1"
				{
					"color" "BorderSelection"
					"offset" "0 0"
				}
				"2"
				{
					"color" "BorderBright"
					"offset" "0 1"
				}
			}
			Top
			{
				"1"
				{
					"color" "BorderSelection"
					"offset" "0 0"
				}
				"2"
				{
					"color" "BorderBright"
					"offset" "1 0"
				}
			}
			Right
			{
				"1"
				{
					"color" "BorderSelection"
					"offset" "0 0"
				}
				"2"
				{
					"color" "BorderDark"
					"offset" "1 0"
				}
			}
			Bottom
			{
				"1"
				{
					"color" "BorderSelection"
					"offset" "0 0"
				}
				"2"
				{
					"color" "BorderDark"
					"offset" "0 0"
				}
			}
		}

		ButtonDepressedBorder
		{
			"inset" "0 0 1 1"
			Left
			{
			}
			Right
			{
			}

			Top
			{
			}

			Bottom
			{
			}
		}

		OldButtonDepressedBorder
		{
			"inset" "2 1 1 1"
			Left
			{
				"1"
				{
					"color" "BorderDark"
					"offset" "0 1"
				}
			}

			Right
			{
				"1"
				{
					"color" "BorderBright"
					"offset" "1 0"
				}
			}

			Top
			{
				"1"
				{
					"color" "BorderDark"
					"offset" "0 0"
				}
			}

			Bottom
			{
				"1"
				{
					"color" "BorderDark"
					"offset" "0 0"
				}
			}
		}

		ButtonDepressedBorder2
		{
//			"inset" "2 1 1 1"
//			"inset" "5 1 1 1"
			"inset" "6 6 6 6"
			Left
			{
				"1"
				{
///					"color" "BorderDark"
"color" "BrightBaseText"
					"offset" "0 1"
				}
				"2"
				{
///					"color" "BorderDark"
"color" "BrightBaseText"
					"offset" "0 1"
				}
				"3"
				{
///					"color" "BorderDark"
"color" "BorderSelection"
					"offset" "0 1"
				}
				"4"
				{
///					"color" "BorderDark"
"color" "BrightBaseText"
					"offset" "4 4"
				}
				"5"
				{
///					"color" "BorderDark"
"color" "BrightBaseText"
					"offset" "5 5"
				}
			}

			Right
			{
				"1"
				{
//					"color" "BorderBright"
"color" "BrightBaseText"
					"offset" "1 0"
				}
				"2"
				{
///					"color" "BorderDark"
"color" "BrightBaseText"
					"offset" "1 0"
				}
				"3"
				{
///					"color" "BorderDark"
"color" "BorderSelection"
					"offset" "1 0"
				}
				"4"
				{
///					"color" "BorderDark"
"color" "BrightBaseText"
					"offset" "4 4"
				}
				"5"
				{
///					"color" "BorderDark"
"color" "BrightBaseText"
					"offset" "5 5"
				}
			}

			Top
			{
				"1"
				{
//					"color" "BorderDark"
"color" "BrightBaseText"
					"offset" "0 0"
				}
				"2"
				{
///					"color" "BorderDark"
"color" "BrightBaseText"
					"offset" "1 1"
				}
				"3"
				{
///					"color" "BorderDark"
"color" "BorderSelection"
					"offset" "2 2"
				}
				"4"
				{
///					"color" "BorderDark"
"color" "BrightBaseText"
					"offset" "3 3"
				}
				"5"
				{
///					"color" "BorderDark"
"color" "BrightBaseText"
					"offset" "4 4"
				}
			}

			Bottom
			{
				"1"
				{
///					"color" "BorderDark"
"color" "BrightBaseText"
					"offset" "0 0"
				}
				"2"
				{
///					"color" "BorderDark"
"color" "BrightBaseText"
					"offset" "1 1"
				}
				"3"
				{
///					"color" "BorderDark"
"color" "BorderSelection"
					"offset" "2 2"
				}
				"4"
				{
///					"color" "BorderDark"
"color" "BrightBaseText"
					"offset" "3 3"
				}
				"5"
				{
///					"color" "BorderDark"
"color" "BrightBaseText"
					"offset" "4 4"
				}
			}
		}

		ComboBoxBorder
		{
			"inset" "0 0 1 1"
			Left
			{
				"1"
				{
					"color" "BorderDark"
					"offset" "0 1"
				}
			}

			Right
			{
				"1"
				{
					"color" "BorderBright"
					"offset" "1 0"
				}
			}

			Top
			{
				"1"
				{
					"color" "BorderDark"
					"offset" "0 0"
				}
			}

			Bottom
			{
				"1"
				{
					"color" "BorderBright"
					"offset" "0 0"
				}
			}
		}

		MenuBorder
		{
			"inset" "1 1 1 1"
			Left
			{
				"1"
				{
					"color" "BorderBright"
					"offset" "0 1"
				}
			}

			Right
			{
				"1"
				{
					"color" "BorderDark"
					"offset" "1 0"
				}
			}

			Top
			{
				"1"
				{
					"color" "BorderBright"
					"offset" "0 0"
				}
			}

			Bottom
			{
				"1"
				{
					"color" "BorderDark"
					"offset" "0 0"
				}
			}
		}


// Vampire
		InfoWinBorder
		{
//			"inset" "2 1 1 1"
//			"inset" "5 1 1 1"
			"inset" "6 6 6 6"
			Left
			{
				"1"
				{
					"color" "BrightBaseText"
					"offset" "0 1"
				}
				"2"
				{
					"color" "BrightBaseText"
					"offset" "0 1"
				}
				"3"
				{
					"color" "BorderSelection"
					"offset" "0 1"
				}
				"4"
				{
					"color" "BrightBaseText"
					"offset" "4 4"
				}
				"5"
				{
					"color" "BrightBaseText"
					"offset" "5 5"
				}
			}

			Right
			{
				"1"
				{
					"color" "BrightBaseText"
					"offset" "1 0"
				}
				"2"
				{
					"color" "BrightBaseText"
					"offset" "1 0"
				}
				"3"
				{
					"color" "BorderSelection"
					"offset" "1 0"
				}
				"4"
				{
					"color" "BrightBaseText"
					"offset" "4 4"
				}
				"5"
				{
					"color" "BrightBaseText"
					"offset" "5 5"
				}
			}

			Top
			{
				"1"
				{
					"color" "BrightBaseText"
					"offset" "0 0"
				}
				"2"
				{
					"color" "BrightBaseText"
					"offset" "1 1"
				}
				"3"
				{
					"color" "BorderSelection"
					"offset" "2 2"
				}
				"4"
				{
					"color" "BrightBaseText"
					"offset" "3 3"
				}
				"5"
				{
					"color" "BrightBaseText"
					"offset" "4 4"
				}
			}

			Bottom
			{
				"1"
				{
					"color" "BrightBaseText"
					"offset" "0 0"
				}
				"2"
				{
					"color" "BrightBaseText"
					"offset" "1 1"
				}
				"3"
				{
					"color" "BorderSelection"
					"offset" "2 2"
				}
				"4"
				{
					"color" "BrightBaseText"
					"offset" "3 3"
				}
				"5"
				{
					"color" "BrightBaseText"
					"offset" "4 4"
				}
			}
		}

		InfoWinFilledBorder
		{
			"inset" "6 6 6 6"
			Left
			{
				"1"
				{
					"color" "BorderBright"
					"offset" "0 1"
				}
				"2"
				{
					"color" "BorderBright"
					"offset" "0 1"
				}
				"3"
				{
					"color" "BorderBright"
					"offset" "0 1"
				}
			}

			Right
			{
				"1"
				{
					"color" "BorderBright"
					"offset" "1 0"
				}
				"2"
				{
					"color" "BorderBright"
					"offset" "1 0"
				}
				"3"
				{
					"color" "BorderBright"
					"offset" "1 0"
				}
			}

			Top
			{
				"1"
				{
					"color" "BorderBright"
					"offset" "0 0"
				}
				"2"
				{
					"color" "BorderBright"
					"offset" "1 1"
				}
				"3"
				{
					"color" "BorderBright"
					"offset" "2 2"
				}
			}

			Bottom
			{
				"1"
				{
					"color" "BorderBright"
					"offset" "0 0"
				}
				"2"
				{
					"color" "BorderBright"
					"offset" "1 1"
				}
				"3"
				{
					"color" "BorderBright"
					"offset" "2 2"
				}
			}
		}


		DropDownHighlightBorder
		{
			"inset" "2 1 1 1"
			Left
			{
				"1"
				{
					"color" "BorderBright"
					"offset" "0 1"
				}
			}

			Right
			{
				"1"
				{
					"color" "BorderBright"
					"offset" "1 0"
				}
			}

			Top
			{
				"1"
				{
					"color" "BorderBright"
					"offset" "0 0"
				}
			}

			Bottom
			{
				"1"
				{
					"color" "BorderBright"
					"offset" "0 0"
				}
			}
		}

		InfoWinBorder2
		{
			"inset" "0 0 1 1"
			Left
			{
				"1"
				{
					"color" "BorderBright"
					"offset" "0 1"
				}
				"2"
				{
					"color" "BorderBright"
					"offset" "0 1"
				}
				"3"
				{
					"color" "BorderSelection"
					"offset" "0 1"
				}
				"4"
				{
					"color" "BorderBright"
					"offset" "0 1"
				}
				"5"
				{
					"color" "BorderBright"
					"offset" "0 1"
				}
			}

			Right
			{
				"1"
				{
					"color" "BorderBright"
					"offset" "1 0"
				}
				"2"
				{
					"color" "BorderBright"
					"offset" "1 0"
				}
				"3"
				{
					"color" "BorderSelection"
					"offset" "1 0"
				}
				"4"
				{
					"color" "BorderBright"
					"offset" "1 0"
				}
				"5"
				{
					"color" "BorderBright"
					"offset" "1 0"
				}
			}

			Top
			{
				"1"
				{
					"color" "BorderDark"
					"offset" "0 0"
				}
			}

			Bottom
			{
				"1"
				{
					"color" "BorderBright"
					"offset" "0 0"
				}
			}
		}
	}
}