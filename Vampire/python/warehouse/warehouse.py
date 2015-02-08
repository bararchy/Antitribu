print "****************** loading warehouse level script"

import __main__

from __main__ import G

__main__.Level = __name__

Find = __main__.FindEntityByName
Finds = __main__.FindEntitiesByName

# added by wesp
def bumDeath():
    pc = __main__.FindPlayer()
    if(pc.humanity >= 3 and G.Patch_Plus == 1):
        pc.HumanityAdd( -1 )

def hateSabbat():
    sabbat = Find( "Sabbat1" )
    if (sabbat):
        sabbat.SetRelationship( "Office_Thugs_JDA D_HT 5" )
        sabbat.SetRelationship( "thug_s_office_2 D_HT 5" )
        sabbat.SetRelationship( "thug_s_office_1 D_HT 5" )
        sabbat.SetRelationship( "spawns1 D_HT 5" )
        sabbat.SetRelationship( "spawns2 D_HT 5" )

    print ( "********* Setting Hate **********" )

#WAREHOUSE: called when the beckett cutscene starts
def beckettSceneStart():
    FindByClass = __main__.FindEntitiesByClass
    thugs = FindByClass("npc_VHumanCombatant")
    for thug in thugs:
        thug.Kill()

#WAREHOUSE: sends the player to santa monica after talking to Beckett at the warehouse
def toSantaMonica():
    __main__.ChangeMap(2.5, "warehouselandmark", "santamonicateleport")

#WAREHOUSE: XP bonus for not killing anyone, changed by wesp
def warehouseBonusPoints():
    bum = Find("bum_male")
    if bum: bum.Kill()
    if (G.Warehouse_Kills == 0 and G.Patch_Plus == 0):
        #changes made by dan_upright 02/12/04
        pc = __main__.FindPlayer()
        if pc:
            pc.AwardExperience("Explosive04")
        #changes end
    if (G.Warehouse_Spotted == 0 and G.Patch_Plus == 1):
        pc = __main__.FindPlayer()
        if pc:
            pc.AwardExperience("Explosive06")

#WAREHOUSE: called when warehouse blows up
def finishWarehouseQuest():
    __main__.FindPlayer().SetQuest("Warehouse", 4)

#Set all interior Thugs to flee and die
def fearThugs():
    thugs = Finds( "Thugs_Door_JDA" )
    for thug in thugs:
        if (thug):
            thug.FleeAndDie()
    thug = Find( "door_thug_2jda" )
    if (thug):
        thug.FleeAndDie()
    thugs = Finds( "Thugs_Inside_JDA" )
    for thug in thugs:
        if (thug):
            thug.FleeAndDie()
    thugs = Finds( "Heavy_Freight_Thugs" )
    for thug in thugs:
        if (thug):
            thug.FleeAndDie()
    thug = Find( "thug_second_wave_patrol" )
    if (thug):
        thug.FleeAndDie()
    thug = Find( "thug_interior_2" )
    if (thug):
        thug.FleeAndDie()
    thug = Find( "thug_interior_1" )
    if (thug):
        thug.FleeAndDie()
    thug = Find( "thug_outback" )
    if (thug):
        thug.FleeAndDie()
    thugs = Finds( "Office_Thugs_JDA" )
    for thug in thugs:
        if (thug):
            thug.FleeAndDie()
    thug = Find( "thug_s_office_2" )
    if (thug):
        thug.FleeAndDie()
    thug = Find( "thug_s_office_1" )
    if (thug):
        thug.FleeAndDie()
    thug = Find( "spawns1" )
    if (thug):
        thug.FleeAndDie()
    thug = Find( "spawns2" )
    if (thug):
        thug.FleeAndDie()

    print ( "*********** Fearing all Interior Thugs ************" )

# Remove all outside thugs
def removeOutsideThugs():
    thug = Find( "Truckyard_Guard_2" )
    if (thug):
        thug.Kill()
    thug = Find( "Truckyard_Guard_1" )
    if (thug):
        thug.Kill()
    thug = Find( "jump_guard" )
    if (thug):
        thug.ScriptUnhide()
        thug.Kill()
    thug = Find( "player_1" )
    if (thug):
        thug.Kill()
    thug = Find( "player_2" )
    if (thug):
        thug.Kill()
    thugs = Finds( "thug_row1_lounger" )
    for thug in thugs:
        if (thug):
            thug.Kill()
    thug = Find( "thug_row2_patrol" )
    if (thug):
        thug.Kill()
    thug = Find( "engine_guard" )
    if (thug):
        thug.Kill()
    thug = Find( "thug_parking_lot_patrol" )
    if (thug):
        thug.Kill()
    thug = Find( "thug_station_bathroom" )
    if (thug):
        thug.Kill()
    thug = Find( "maker front" )
    if (thug):
        thug.Kill()
    thug = Find( "maker back" )
    if (thug):
        thug.Kill()
    print ( "*********** Removing all outside Thugs ************" )

# Bring on the Sabbat
def bringOnSabbat():
    sabbat = Find( "NPC_Sabbat1" )
    print ( "*********** Unhiding Sabbat1 ************" )
    sabbat.ScriptUnhide()
    print ( "*********** Unhiding Sabbat2 ************" )
    sabbat = Find( "NPC_Sabbat2" )
    sabbat.ScriptUnhide()
    removeOutsideThugs()
    hateSabbat()
    block = Find( "Exit_Block" )
    block.ScriptUnhide()

def testtrigg():
    print ( "******** Triggered **********" )

def explodeBoxes():
    print ( "******************** exploding boxes **********************" )
    box = Find( "truckyard_crush_boxes" )
    box.Break()

def boxExplosion():
    print ( "******************** timeing exploding boxes **********************" )
    __main__.ScheduleTask( 3.7, "explodeBoxes()" )

#------------------------------------Gangrel antitribu------------------------------
# Sabbat1 wolf form transformed: first boss in warehouse
def Sabbat1WolfTransform():
    if(G.Sabbat1_wolfform == 1):
         return
    else:
         Find("NPC_Sabbat1").MakeInvincible(1)
         __main__.ScheduleTask(0.1,"Sabbat1WolfTransform1a()")
	 G.Sabbat1_wolfform = 1

def Sabbat1WolfTransform1a():
    Find("Sabbat1_transform").BeginSequence()

def Sabbat1WolfTransform1():
    Find("NPC_Sabbat1").SetModel("models/weapons/disciplines/animalism/grey_wolf.mdl")
    Find("NPC_Sabbat1").PlayDialogFile("disciplines/animalism/level5/anm_lvl5_activate.wav")
    #Find("NPC_Sabbat1").SetScriptedDiscipline("mind_shield 5")
    #Find("NPC_Sabbat1").SetGesture("sit_outof")
    __main__.ScheduleTask(0.1,"Sabbat1WolfTransform1b()")

def Sabbat1WolfTransform1b():
    Find("NPC_Sabbat1").MakeInvincible(0)

#------------------------------------Blood Brothers------------------------------
#BLOOD BROTHERS:  second bosses in warehouseBlood Brothers cast Sanguinus      
def WHBroCastSanguinus():
    if(G.whbro_death == 1):
        #Find("WHSanguinus_timer").Disable()
        return
    else:
        Find("bro_1_anim_sanguinus1").BeginSequence()
	__main__.ScheduleTask(0.1,"Bro1CastSanguinus1Helper1()")

def Bro1CastSanguinus1Helper1():
        bro1 = Find("NPC_Sabbat2")
        bro2 = Find("NPC_Sabbat3")
        bro1.PlayDialogFile("disciplines/sanguinus/d_npc_sanguinus_level2.wav")
        bro2.PlayDialogFile("disciplines/sanguinus/d_npc_sanguinus_level2.wav")
        bro1.MakeInvincible(1)
        bro2.MakeInvincible(1)
        Find("WHbro_hands").ScriptUnhide()
        bro2.SetModel("models/character/npc/common/blood_brother/blood_brother_null.mdl")
        __main__.ScheduleTask(5.5,"Bro1CastSanguinus1Helper2()")

def Bro1CastSanguinus1Helper2():
        Find("bro_1_anim_end_sanguinus1").BeginSequence()
        __main__.ScheduleTask(0.75,"Bro1CastSanguinus1Helper3()")

def Bro1CastSanguinus1Helper3():
        bro1 = Find("NPC_Sabbat2")
        bro2 = Find("NPC_Sabbat3")
        bro1.MakeInvincible(0)
        bro2.MakeInvincible(0)
        Find("WHbro_hands").ScriptHide()
        bro2.SetModel("models/character/npc/common/blood_brother/blood_brother.mdl")
        bro2.PlayDialogFile("disciplines/sanguinus/d_npc_sanguinus_level2_end.wav")
        bro1.PlayDialogFile("disciplines/sanguinus/d_npc_sanguinus_level2_end.wav")
        __main__.ScheduleTask(7.75,"WHBroCastSanguinus()")

#BLOOD BROTHERS:  check die Blood Brothers 
def BloodBrothersCheck():
    G.WarehouseBB_Death = G.WarehouseBB_Death + 1
    
    if(G.WarehouseBB_Death == 2):
       Find("Exit_Block").ScriptHide()

#------------------------------------Blood Brothers End------------------------------

print "*************levelscript loaded"