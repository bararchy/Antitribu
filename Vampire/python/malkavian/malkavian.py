print "loading malkavian level script"

import __main__

from __main__ import G

__main__.Level = __name__

Find = __main__.FindEntityByName
FindList = __main__.FindEntitiesByName

import consoleutil

#
def LoadMap12():
    __main__.ChangeMap(1, "malkext", "malkentranceteleport")

def LoadMap34():
    __main__.ChangeMap(1, "bedroom_landmark", "tobedroom")

def malk2_MapLoad_start():
    Find("ghoul_entryway_c_1").SetModel("models/character/npc/unique/malkavian_mansion/stalker_female/stalker_female_orig.mdl")
    Find("ghoul_entrance_c_1").SetModel("models/character/npc/unique/malkavian_mansion/stalker_female/stalker_female_orig.mdl")
    Find("ghoul_entrance_c_2").SetModel("models/character/npc/unique/malkavian_mansion/stalker_female/stalker_female_orig.mdl")
    Find("ghoul_great_hall_c_1").SetModel("models/character/npc/unique/malkavian_mansion/stalker_female/stalker_female_orig.mdl")
    Find("ghoul_great_hall_c_2").SetModel("models/character/npc/unique/malkavian_mansion/stalker_female/stalker_female_orig.mdl")
    Find("ghoul_great_hall_c_3").SetModel("models/character/npc/unique/malkavian_mansion/stalker_female/stalker_female_orig.mdl")
    Find("ghoul_great_hall_c_4").SetModel("models/character/npc/unique/malkavian_mansion/stalker_female/stalker_female_orig.mdl")
    Find("ghoul_trophy_room_c_1").SetModel("models/character/npc/unique/malkavian_mansion/stalker_female/stalker_female_orig.mdl")
    Find("ghoul_dining_hall_c_1").SetModel("models/character/npc/unique/malkavian_mansion/stalker_female/stalker_female_orig.mdl")
    Find("ghoul_dining_hall_c_2").SetModel("models/character/npc/unique/malkavian_mansion/stalker_female/stalker_female_orig.mdl")
    Find("ghoul_dining_hall_c_3").SetModel("models/character/npc/unique/malkavian_mansion/stalker_female/stalker_female_orig.mdl")
    Find("ghoul_dining_hall_s_4").SetModel("models/character/npc/unique/malkavian_mansion/stalker_female/stalker_female_orig.mdl")
    Find("ghoul_dining_hall_s_5").SetModel("models/character/npc/unique/malkavian_mansion/stalker_female/stalker_female_orig.mdl")
    Find("ghouls_parlor_c_1").SetModel("models/character/npc/unique/malkavian_mansion/stalker_female/stalker_female_orig.mdl")
    Find("ghouls_parlor_c_2").SetModel("models/character/npc/unique/malkavian_mansion/stalker_female/stalker_female_orig.mdl")
    Find("ghouls_parlor_c_3").SetModel("models/character/npc/unique/malkavian_mansion/stalker_female/stalker_female_orig.mdl")
    Find("ghouls_parlor_c_4").SetModel("models/character/npc/unique/malkavian_mansion/stalker_female/stalker_female_orig.mdl")
    Find("ghouls_parlor_c_5").SetModel("models/character/npc/unique/malkavian_mansion/stalker_female/stalker_female_orig.mdl")

#la_malkavian_2: sets up patrol paths, and other entity / flag states
#loads the FIRST time the map is run...
def malk2_MapLoad():
    npc = Find("ghoul_entrance_s_3")
    npc.SetupPatrolType("9999 2 FOLLOW_PATROL_PATH_WALK")
    npc.FollowPatrolPath("hp_a_1 hp_a_2 hp_a_3 hp_a_4 hp_a_5 hp_a_6 hp_a_7 hp_a_5 hp_a_3 hp_a_8")
    npc = Find("ghoul_great_hall_s_5")
    npc.SetupPatrolType("9999 2 FOLLOW_PATROL_PATH_WALK")
    npc.FollowPatrolPath("hp_b_1 hp_b_2 hp_b_3 hp_b_1 hp_b_6 hp_b_5 hp_b_4")
    npc = Find("ghoul_dining_hall_s_4")
    npc.SetupPatrolType("9999 2 FOLLOW_PATROL_PATH_WALK")
    npc.FollowPatrolPath("hp_c_1 hp_c_2 hp_c_3 hp_c_4 hp_c_5 hp_c_6 hp_c_9 hp_c_8 hp_c_7")
    npc = Find("ghoul_dining_hall_s_5")
    npc.SetupPatrolType("9999 2 FOLLOW_PATROL_PATH_WALK")
    npc.FollowPatrolPath("hp_c_8 hp_c_7 hp_c_1 hp_c_9 hp_c_12 hp_c_11 hp_c_10")

    # all the lights / switchs START on....
    G.MalkavianMansion_Library_Lights = [1,1,1,1,1,1,1]

    # change the state of this light so that
    # the puzzle is not solved by the scripted NPC
    libraryLightToggle(2)

    # the lamps upstairs start off....
    libraryLightToggle(4)
    libraryLightToggle(5)
    libraryLightToggle(6)

    #added by wesp
    if G.Patch_Plus == 1:
        dodgebook = Find("book_dodge")
        dodgebooknode = Find("book_dodge_node")
        if dodgebook: dodgebook.ScriptHide()
        if dodgebooknode: dodgebooknode.ScriptHide()
        dodgepower = Find("occult_dodge")
        dodgepowernode = Find("occult_dodge_node")
        if dodgepower: dodgepower.ScriptUnhide()
        if dodgepowernode: dodgepowernode.ScriptUnhide()

# Library downstairs lamps
#
# Updated 09-08-04 by TJP
# Skin swapping for bulbs was busted when I started... and my mucking around didn't miraculously fix it.
#
# The 3 wall lamps/levers toggle the lights on and off.
# Facing, left to right: 1 - 2 - 3
# lamp 1 (eye)  toggles lights 2 and 3 simultaneously- tested and confirmed TJP 09-08-04
# lamp 2 (time) toggles 1 and 3 on alternate pulls- tested and confirmed TJP 09-08-04
# lamp 3 (mind) toggles lights randomly - CORRECT - tested and confirmed TJP 09-08-04

# la_malkavian_2:
def libraryLightToggle( number ):
    #set flags so we know what state things are in. (lame)
    switch = Find("library_light_switch_%d" % number )
    if ( G.MalkavianMansion_Library_Lights[number-1] == 1):
        G.MalkavianMansion_Library_Lights[number-1] = 0
        switch.skin = 0
    else:
        G.MalkavianMansion_Library_Lights[number-1] = 1
        switch.skin = 1
    # Toggle the lights
    lights = FindList( "library_light_%d" % number )
    for light in lights:
        light.Toggle()

# la_malkavian_2:
def libraryLampOne():
        libraryLightToggle(2)
        libraryLightToggle(3)
        libraryLowerLightCheck()

# la_malkavian_2:
def libraryLampTwo():
    if ( G.MalkavianMansion_Library_Lamp_Two == 1 ):
        G.MalkavianMansion_Library_Lamp_Two = 0
        libraryLightToggle(3)
    else:
        G.MalkavianMansion_Library_Lamp_Two = 1
        libraryLightToggle(1)
    libraryLowerLightCheck()

# la_malkavian_2:
def libraryLampThree():
    from random import Random
    from time import time
    R = Random( time() )
    libraryLightToggle( R.randint(1,3) )
    libraryLowerLightCheck()

# la_malkavian_2:
def libraryLowerLightCheck():
    if ( G.MalkavianMansion_Library_Light_Ready and
         G.MalkavianMansion_Library_Lights[0] and
         G.MalkavianMansion_Library_Lights[1] and
         G.MalkavianMansion_Library_Lights[2] ):
        ent = Find("great_hall_door_bar_relay_1")
        ent.Trigger()
        Find("malk1_relay").Trigger()

# Library upstairs lamps
#
# Updated 09-08-04 by TJP
# Skin swapping for bulbs was busted when I started... and my mucking around didn't miraculously fix it.
#
# The 3 wall lamps/levers toggle the lights on and off.
# facing, left to right- 4 - 5 - 6
# lamp 4 (chaos) toggles lights randomly- tested and confirmed TJP 09-08-04
# lamp 5 (key)   toggles 6 and 4 on alternate pulls- tested and confirmed TJP 09-08-04
# lamp 6 (order) toggles lights 5 and 4 simultaneously- tested and confirmed TJP 09-08-04

# la_malkavian_2:
def libraryLampFour():
    from random import Random
    from time import time
    R = Random( time() )
    libraryLightToggle( R.randint(4,6) )
    libraryUpperLightCheck()

# la_malkavian_2:
def libraryLampFive():
    if ( G.MalkavianMansion_Library_Lamp_Five == 0 ):
        G.MalkavianMansion_Library_Lamp_Five = 1
        libraryLightToggle(4)
    else:
        G.MalkavianMansion_Library_Lamp_Five = 0
        libraryLightToggle(6)
    libraryUpperLightCheck()

# la_malkavian_2:
def libraryLampSix():
    libraryLightToggle(4)
    libraryLightToggle(5)
    libraryUpperLightCheck()

# la_malkavian_2:
def libraryUpperLightCheck():
    if ( G.MalkavianMansion_Library_Lights[3] and
         G.MalkavianMansion_Library_Lights[4] and
         G.MalkavianMansion_Library_Lights[5] ):
        ent = Find("library_bookshelf_door")
        ent.Open()
        cam = Find("bookcase_cam")
        if ( cam ):
            tar = Find("bookcase_target")
            pc = Find("playercontroller")
            cam.PlayAsCameraPosition()
            tar.PlayAsCameraTarget()
            pc.ImmobilizePlayer()

# la_malkavian_3: sets up patrol paths, and other entity / flag states
# loads the FIRST time the map is run..., changed by wesp
def malk3_MapLoad():
    npc = Find("ghoul_lab_s_6")
    npc.SetupPatrolType("9999 2 FOLLOW_PATROL_PATH_WALK")
    npc.FollowPatrolPath("hp_d_1 hp_d_2 hp_d_3 hp_d_4 hp_d_5 hp_d_6 hp_d_7")
    npc = Find("ghouls_cells1_s_4")
    npc.SetupPatrolType("9999 2 FOLLOW_PATROL_PATH_WALK")
    npc.FollowPatrolPath("hp_e_1 hp_e_2 hp_e_3")
    npc = Find("ghouls_cells2_s_3")
    npc.SetupPatrolType("9999 2 FOLLOW_PATROL_PATH_WALK")
    npc.FollowPatrolPath("hp_f_1 hp_f_2 hp_f_3")
    npc = Find("ghouls_pits_s_1")
    npc.SetupPatrolType("9999 2 FOLLOW_PATROL_PATH_WALK")
    npc.FollowPatrolPath("hp_g_1 hp_g_2")

def malk1_JournalSeeMingAsNines():
    __main__.FindPlayer().SetQuest( "Grout" , 4 )

def malk2_JournalEnterMap():
    __main__.FindPlayer().SetQuest( "Grout" , 5 )

def malk4_JournalSeeGrout():
    __main__.FindPlayer().SetQuest( "Grout" , 2 )

def malk2_PuzzleExperience():
    __main__.FindPlayer().AwardExperience("Grout03")

def malk2_SanctumExperience():
    __main__.FindPlayer().AwardExperience("Grout04")

#la_malkavian_5: when leaving, if player is nosferatu, return him to sewers.
# else put at taxi_landmark in hub, changed by RobinHood70.
def LeaveMansion():
    pc = __main__.FindPlayer()
    if(pc.HasItem("item_k_malkavian_refrigerator_key")):
        __main__.ScheduleTask(5.00, "__main__.FindPlayer().RemoveItem(\"item_k_malkavian_refrigerator_key\")")
        # Changed by CompMod
        #if __main__.IsClan(__main__.FindPlayer(), "Nosferatu"):
    if 5 == __main__.G._pcinfo["clan"]:
        trig = Find("malk_la")
        trig.ScriptHide()
        trig = Find("malk_la_sewer")
        trig.ScriptUnhide()
    else:
        trig = Find("malk_la_sewer")
        trig.ScriptHide()
        trig = Find("malk_la")
        trig.ScriptUnhide()

def malk3_MapLoad_start():
    Find("ghouls_lab_c_1").SetModel("models/character/npc/unique/malkavian_mansion/stalker_female/stalker_female_orig.mdl")
    Find("ghouls_lab_c_2").SetModel("models/character/npc/unique/malkavian_mansion/stalker_female/stalker_female_orig.mdl")
    Find("ghouls_lab_c_3").SetModel("models/character/npc/unique/malkavian_mansion/stalker_female/stalker_female_orig.mdl")
    Find("ghouls_lab_c_4").SetModel("models/character/npc/unique/malkavian_mansion/stalker_female/stalker_female_orig.mdl")
    Find("ghouls_lab_c_5").SetModel("models/character/npc/unique/malkavian_mansion/stalker_female/stalker_female_orig.mdl")
    Find("ghouls_cells1_c_1").SetModel("models/character/npc/unique/malkavian_mansion/stalker_female/stalker_female_orig.mdl")
    Find("ghouls_cells1_c_2").SetModel("models/character/npc/unique/malkavian_mansion/stalker_female/stalker_female_orig.mdl")
    Find("ghouls_cells1_c_3").SetModel("models/character/npc/unique/malkavian_mansion/stalker_female/stalker_female_orig.mdl")
    Find("ghouls_cells2_c_1").SetModel("models/character/npc/unique/malkavian_mansion/stalker_female/stalker_female_orig.mdl")
    Find("ghouls_cells2_c_2").SetModel("models/character/npc/unique/malkavian_mansion/stalker_female/stalker_female_orig.mdl")
    #Find("ghouls_cells2_s_2").SetModel("models/character/npc/unique/malkavian_mansion/stalker_female/stalker_female_orig.mdl")
    #Find("ghouls_cells2_s_3").SetModel("models/character/npc/unique/malkavian_mansion/stalker_female/stalker_female_orig.mdl")

#-------------------------------------------------------------------
#la_malkavian_2: if malk2 not properly die, open door.          
def Malk2DeathCheck():
    if(G.malk2_death == 1):
        Find("malk2_door").Unlock()
        Find("malk2_dem_timer").Disable()
    else:
        Find("malk2_relay").Trigger()

#la_malkavian_2: malk2 cast demenation.          
def Malk2CastDem():
    pc = __main__.FindPlayer()
    if(G.malk2_death == 1):
        return
    else:
        Find("malk2_cast_dem").BeginSequence()
        if(pc.base_dominate >= 3 or G.Player_Ashes_Form == 1):
	    __main__.ScheduleTask(0.25,"PcResistDemenation()")
        else:
	    __main__.ScheduleTask(0.1,"Malk2CastDemenation()")

def Malk2CastDemenation():
    Find("malkavian2").PlayDialogFile("disciplines/dementation/activate.wav")
    __main__.ScheduleTask(0.1,"Malk2CastDemenation1()")

def Malk2CastDemenation1():
    Find("pc_dem_anim").BeginSequence()

#la_malkavian_2: PC resist demenation.  
def PcResistDemenation():
    __main__.FindPlayer().SpawnTempParticle("dem_particles3")
    Find("pc_demenation").RemoveControllerNPC()
    #__main__.FindPlayer().ClearActiveDisciplines()
    #__main__.ScheduleTask(0.15,"PcResistDemenation1()")

def PcResistDemenation1():
    Find("pc_demenation").RemoveControllerNPC()

#-------------------------------------------------------------------
#la_malkavian_3: Grout wife cast demenation.          
def GroutsWifeCastDem():
    pc = __main__.FindPlayer()
    if(G.GroutsWife_Death == 1):
        return
    else:
        Find("GroutsWife_cast_dem").BeginSequence()
        if(pc.base_dominate >= 3 or G.Player_Ashes_Form == 1):
	    __main__.ScheduleTask(0.25,"PcResistGWDemenation()")
        else:
	    __main__.ScheduleTask(0.1,"GroutsWifeCastDemenation()")

def GroutsWifeCastDemenation():
    Find("GroutsWife").PlayDialogFile("disciplines/dementation/activate.wav")
    __main__.ScheduleTask(0.1,"GroutsWifeCastDemenation1()")

def GroutsWifeCastDemenation1():
    Find("pc_dem_anim").BeginSequence()

#la_malkavian_3: PC resist demenation.  
def PcResistGWDemenation():
    __main__.FindPlayer().SpawnTempParticle("dem_particles3")
    Find("pc_demenation").RemoveControllerNPC()

#la_malkavian_3: Grout wife cast obfuscate.          
def GroutsWifeCastObf():
    if(G.GroutsWife_Death == 1):
        return
    else:
        Find("GroutsWife").SetScriptedDiscipline("obfuscate 4")
        Find("GroutsWife").SetScriptedDiscipline("auspex 0")
	__main__.ScheduleTask(7.5,"GroutsWifeCastObfuscate()")

def GroutsWifeCastObfuscate():
    Find("GroutsWife").SetScriptedDiscipline("obfuscate 0")
    Find("GroutsWife").SetScriptedDiscipline("auspex 3")

#-------------------------------------------------------------------
#la_malkavian_1: Dog1 bite
def Dog1Bite():
    consoleutil.console("vdmg 10")

#-------------------------------------------------------------------
#REAPER: cut scene
def ChangeMapReaper():
    __main__.ChangeMap(1, "taxi_landmark", "malk_la")
#-------------------------------------------------------------------

print "levelscript loaded"
