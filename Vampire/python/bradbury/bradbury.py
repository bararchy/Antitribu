print "loading bradbury level script"

import __main__

from __main__ import G
from random import Random
from time import time

__main__.Level = __name__

Find = __main__.FindEntityByName
FindList = __main__.FindEntitiesByName
FindClass = __main__.FindEntitiesByClass


# added by wesp
def civilianDeath():
    pc = __main__.FindPlayer()
    if(pc.humanity >= 3 and G.Patch_Plus == 1):
        pc.HumanityAdd( -1 )

#fired when andrei found
def andreiFound():
    __main__.FindPlayer().SetQuest("Shangrila", 2)

#fired when andrei dies
def andreiDeath():
    __main__.FindPlayer().SetQuest("Shangrila", 3)

#checks the shadows for inhabitants
def checkShadows():
    i = 0
    while(i < 5):
        trigger = Find("shadow_check_%i" % i)
        trigger.Enable()
        __main__.ScheduleTask(1.0, "__main__.FindEntityByName(\"shadow_check_%i\" % i).Disable()")
        i = i + 1

#chooses a shadow to send this Lasombra to, based upon which are occupied.
def chooseDestinationShadow():
    R = Random( time() )
    Index = R.randint(0, 4)
    shadowFree = 0
    while(shadowFree != 1):
        if(Index == 4):
            Index = 0
        else:
            Index = Index + 1
        #spot = Find("shadow_trigger_%i" % (Index)).GetOrigin()
        #if(isUnoccupied(spot)):
        #    shadowFree = 1
        if(G.shadowList[Index] == 0):
            shadowFree = 1
    #script = Find("go_to_shadow_%i" % (Index))
    #script.BeginSequence()
    chooser = Find("shadow_chooser")
    IndexString = "%i" % (Index)
    print "choosing shadow " + IndexString
    chooser.InValue(IndexString)
    #G.shadowList = [0, 0, 0, 0, 0]

#counts the number of dead lasombra, and causes the level to continue
#after they are all dead
def deadLasombra():
    G.deadShadowMages = G.deadShadowMages + 1
    if(G.deadShadowMages == 3):
        relay = Find("Lasombra_dead_relay")
        relay.Trigger()

#Enables the appropriate encounter based upon whether or not the player 
#has kept Heather as a ghoul, changed by Wesp
def heatherCheck():
    if(G.Heather_Drank == 1 and G.Heather_Gone == 0 and G.Heather_Kill == 0 and G.Heather_Indoors == 0 and not __main__.IsDead("Heather")):
        #Heather gets to die now
        print "incoming heather"
        heather = Find("Heather")
        relay = Find("heather_scene_unhider")
        relay.Trigger()
        if(G.Heather_Clothes and heather):
            if(G.Heather_Outfit == 0):
                heather.SetModel("models/character/npc/unique/Santa_Monica/Heather/Heather_goth.mdl")
            elif(G.Heather_Outfit == 1):
                heather.SetModel("models/character/npc/unique/Santa_Monica/Heather/Heather_3.mdl")
            else:
                heather.SetModel("models/character/npc/unique/Santa_Monica/Heather/Heather.mdl")
    else:
        #normal encounter
        print "no heather"
        relay = Find("non_heather_scene_unhider")
        relay.Trigger()

#Heather screams for the first time
def heatherScream1():
    heather = Find("Heather")
    if heather:
        heather.PlayDialogFile("\Character\dlg\Main Characters\Heather\line901_col_e.mp3")

#Heather screams for the first time, changed by wesp
def heatherCry():
    heather = Find("Heather")
    if heather:
        heather.PlayDialogFile("\Character\dlg\Main Characters\Heather\line921_col_e.mp3")

#Heather screams for the first time
def heatherScream2():
    heather = Find("Heather")
    if heather:
        heather.PlayDialogFile("\Character\dlg\Main Characters\Heather\line911_col_e.mp3")

#Heather screams for the first time
def heatherDie():
    heather = Find("Heather")
    if heather:
        heather.PlayDialogFile("\Character\dlg\Main Characters\Heather\line931_col_e.mp3")        

#this makes me sad, changed by wesp
def initVars():
    G.shadowList = [1, 1, 0, 0, 1]
    G.deadShadowMages = 0
    if G.Patch_Plus == 1:
        flame = Find("thrower")
        flamenode = Find("throwernode")
        if flame: flame.ScriptHide()
        if flamenode: flamenode.ScriptHide()
        blade = Find("rablade")
        bladenode = Find("rabladenode")
        if blade: blade.ScriptHide()
        if bladenode: bladenode.ScriptHide()

#returns true if the shadow is not occupied
def isUnoccupied(spot):
    L1Spot = Find("Lasombra").GetOrigin()
    if L1Spot:
        if(__main__.distanceSquared(L1Spot, spot) < 100000):
            return 0
    L2Spot = Find("Lasombra_2").GetOrigin()
    if L2Spot:
        if(__main__.distanceSquared(L2Spot, spot) < 100000):
            return 0
    L3Spot = Find("Lasombra_3").GetOrigin()
    if L3Spot:
        if(__main__.distanceSquared(L3Spot, spot) < 100000):
            return 0
    return 1

#tries to figure out which Lasombra is in the given shadow
def leaveShadow(number):
    trigger = Find("shadow_trigger_%i" % number)
    trigger.Enable()

#tells the game that the given shadow is now free for use
def shadowFree(number):
    G.shadowList[number] = 0
    print "shadowList [%i, %i, %i, %i, %i]" % (G.shadowList[0], G.shadowList[1], G.shadowList[2], G.shadowList[3], G.shadowList[4])
 
#tells the game that the given shadow is now occupied by a Lasombra
def shadowOccupied(number):
    shadowList[number] = 1
    print "shadowList [%i, %i, %i, %i, %i]" % (G.shadowList[0], G.shadowList[1], G.shadowList[2], G.shadowList[3], G.shadowList[4])


#----------------------------------------------------------
#starts the BloodDoll on a random line
def Dog1Random():
    RandomLine([1, 5, 10])

def RandomLine( NumList ):
    R = Random( time() )
    Index = R.randint(0, len(NumList)-1)
    return NumList[Index]

#----------------------------------------------------------------------------------
#la_bradbury_2: tzimisce punk1 explode
def War2Tzpunk1boom():
    Find("tzpk1_explosion").SetOrigin(Find("f2_m_protean_2").GetOrigin())
    __main__.ScheduleTask(0.1,"War2Tzpunk1boom1()")
    __main__.ScheduleTask(0.05,"War2Tzpunk1boom2()")

def War2Tzpunk1boom1():
    Find("tzpk1_explosion").Explode()

def War2Tzpunk1boom2():
    punkBody=__main__.CreateEntityNoSpawn("prop_physics",Find("f2_m_protean_2").GetOrigin(),Find("f2_m_protean_2").GetAngles())
    punkBody.SetName("punkBody")
    punkBody.SetModel("models/gibs/hgibstorso_prop.mdl")
    __main__.CallEntitySpawn(punkBody)
    punkBodya=__main__.CreateEntityNoSpawn("prop_physics",Find("f2_m_protean_2").GetOrigin(),Find("f2_m_protean_2").GetAngles())
    punkBodya.SetName("punkBodya")
    punkBodya.SetModel("models/gibs/hgibslleg_prop.mdl")
    __main__.CallEntitySpawn(punkBodya)
    punkBodyb=__main__.CreateEntityNoSpawn("prop_physics",Find("f2_m_protean_2").GetOrigin(),Find("f2_m_protean_2").GetAngles())
    punkBodyb.SetName("punkBodyb")
    punkBodyb.SetModel("models/gibs/hgibslarm_prop.mdl")
    __main__.CallEntitySpawn(punkBodyb)
    punkBodyc=__main__.CreateEntityNoSpawn("prop_physics",Find("f2_m_protean_2").GetOrigin(),Find("f2_m_protean_2").GetAngles())
    punkBodyc.SetName("punkBodyc")
    punkBodyc.SetModel("models/gibs/hgibsskull_prop.mdl")
    __main__.CallEntitySpawn(punkBodyc)
#--------------------------------------
#la_bradbury_2: tzimisce punk2 explode
def War2Tzpunk2boom():
    Find("tzpk2_explosion").SetOrigin(Find("f2_m_ghoul_1").GetOrigin())
    __main__.ScheduleTask(0.1,"War2Tzpunk2boom1()")
    __main__.ScheduleTask(0.05,"War2Tzpunk2boom2()")

def War2Tzpunk2boom1():
    Find("tzpk2_explosion").Explode()

def War2Tzpunk2boom2():
    punk2Body=__main__.CreateEntityNoSpawn("prop_physics",Find("f2_m_ghoul_1").GetOrigin(),Find("f2_m_ghoul_1").GetAngles())
    punk2Body.SetName("punk2Body")
    punk2Body.SetModel("models/gibs/hgibstorso_prop.mdl")
    __main__.CallEntitySpawn(punk2Body)
    punk2Bodya=__main__.CreateEntityNoSpawn("prop_physics",Find("f2_m_ghoul_1").GetOrigin(),Find("f2_m_ghoul_1").GetAngles())
    punk2Bodya.SetName("punk2Bodya")
    punk2Bodya.SetModel("models/gibs/hgibslleg_prop.mdl")
    __main__.CallEntitySpawn(punk2Bodya)
    punk2Bodyb=__main__.CreateEntityNoSpawn("prop_physics",Find("f2_m_ghoul_1").GetOrigin(),Find("f2_m_ghoul_1").GetAngles())
    punk2Bodyb.SetName("punk2Bodyb")
    punk2Bodyb.SetModel("models/gibs/hgibslarm_prop.mdl")
    __main__.CallEntitySpawn(punk2Bodyb)
    punk2Bodyc=__main__.CreateEntityNoSpawn("prop_physics",Find("f2_m_ghoul_1").GetOrigin(),Find("f2_m_ghoul_1").GetAngles())
    punk2Bodyc.SetName("punk2Bodyc")
    punk2Bodyc.SetModel("models/gibs/hgibsskull_prop.mdl")
    __main__.CallEntitySpawn(punk2Bodyc)

#--------------------------------------
#la_bradbury_2: tzimisce punk3 explode
def War3Tzpunk3boom():
    Find("tzpk3_explosion").SetOrigin(Find("f2_m_ghoul_5").GetOrigin())
    __main__.ScheduleTask(0.1,"War3Tzpunk3boom1()")
    __main__.ScheduleTask(0.05,"War3Tzpunk3boom2()")

def War3Tzpunk3boom1():
    Find("tzpk3_explosion").Explode()

def War3Tzpunk3boom2():
    punk3Body=__main__.CreateEntityNoSpawn("prop_physics",Find("f2_m_ghoul_5").GetOrigin(),Find("f2_m_ghoul_5").GetAngles())
    punk3Body.SetName("punk3Body")
    punk3Body.SetModel("models/gibs/hgibstorso_prop.mdl")
    __main__.CallEntitySpawn(punk3Body)
    punk3Bodya=__main__.CreateEntityNoSpawn("prop_physics",Find("f2_m_ghoul_5").GetOrigin(),Find("f2_m_ghoul_5").GetAngles())
    punk3Bodya.SetName("punk3Bodya")
    punk3Bodya.SetModel("models/gibs/hgibslleg_prop.mdl")
    __main__.CallEntitySpawn(punk3Bodya)
    punk3Bodyb=__main__.CreateEntityNoSpawn("prop_physics",Find("f2_m_ghoul_5").GetOrigin(),Find("f2_m_ghoul_5").GetAngles())
    punk3Bodyb.SetName("punk3Bodyb")
    punk3Bodyb.SetModel("models/gibs/hgibslarm_prop.mdl")
    __main__.CallEntitySpawn(punk3Bodyb)
    punk3Bodyc=__main__.CreateEntityNoSpawn("prop_physics",Find("f2_m_ghoul_5").GetOrigin(),Find("f2_m_ghoul_5").GetAngles())
    punk3Bodyc.SetName("punk3Bodyc")
    punk3Bodyc.SetModel("models/gibs/hgibsskull_prop.mdl")
    __main__.CallEntitySpawn(punk3Bodyc)

#--------------------------------------
#la_bradbury_2: tzimisce punk4 explode
def War3Tzpunk4boom():
    Find("tzpk4_explosion").SetOrigin(Find("f2_r_auspex_1").GetOrigin())
    __main__.ScheduleTask(0.1,"War3Tzpunk4boom1()")
    __main__.ScheduleTask(0.05,"War3Tzpunk4boom2()")

def War3Tzpunk4boom1():
    Find("tzpk4_explosion").Explode()

def War3Tzpunk4boom2():
    punk4Body=__main__.CreateEntityNoSpawn("prop_physics",Find("f2_r_auspex_1").GetOrigin(),Find("f2_r_auspex_1").GetAngles())
    punk4Body.SetName("punk4Body")
    punk4Body.SetModel("models/gibs/hgibstorso_prop.mdl")
    __main__.CallEntitySpawn(punk4Body)
    punk4Bodya=__main__.CreateEntityNoSpawn("prop_physics",Find("f2_r_auspex_1").GetOrigin(),Find("f2_r_auspex_1").GetAngles())
    punk4Bodya.SetName("punk4Bodya")
    punk4Bodya.SetModel("models/gibs/hgibslleg_prop.mdl")
    __main__.CallEntitySpawn(punk4Bodya)
    punk4Bodyb=__main__.CreateEntityNoSpawn("prop_physics",Find("f2_r_auspex_1").GetOrigin(),Find("f2_r_auspex_1").GetAngles())
    punk4Bodyb.SetName("punk4Bodyb")
    punk4Bodyb.SetModel("models/gibs/hgibslarm_prop.mdl")
    __main__.CallEntitySpawn(punk4Bodyb)
    punk4Bodyc=__main__.CreateEntityNoSpawn("prop_physics",Find("f2_r_auspex_1").GetOrigin(),Find("f2_r_auspex_1").GetAngles())
    punk4Bodyc.SetName("punk4Bodyc")
    punk4Bodyc.SetModel("models/gibs/hgibsskull_prop.mdl")
    __main__.CallEntitySpawn(punk4Bodyc)

#--------------------------------------
#la_bradbury_2: tzimisce punk5 explode
def War4Tzpunk5boom():
    Find("tzpk5_explosion").SetOrigin(Find("f3_m_ghoul_1").GetOrigin())
    __main__.ScheduleTask(0.1,"War4Tzpunk5boom1()")
    __main__.ScheduleTask(0.05,"War4Tzpunk5boom2()")

def War4Tzpunk5boom1():
    Find("tzpk5_explosion").Explode()

def War4Tzpunk5boom2():
    punk5Body=__main__.CreateEntityNoSpawn("prop_physics",Find("f3_m_ghoul_1").GetOrigin(),Find("f3_m_ghoul_1").GetAngles())
    punk5Body.SetName("punk5Body")
    punk5Body.SetModel("models/gibs/hgibstorso_prop.mdl")
    __main__.CallEntitySpawn(punk5Body)
    punk5Bodya=__main__.CreateEntityNoSpawn("prop_physics",Find("f3_m_ghoul_1").GetOrigin(),Find("f3_m_ghoul_1").GetAngles())
    punk5Bodya.SetName("punk5Bodya")
    punk5Bodya.SetModel("models/gibs/hgibslleg_prop.mdl")
    __main__.CallEntitySpawn(punk5Bodya)
    punk5Bodyb=__main__.CreateEntityNoSpawn("prop_physics",Find("f3_m_ghoul_1").GetOrigin(),Find("f3_m_ghoul_1").GetAngles())
    punk5Bodyb.SetName("punk5Bodyb")
    punk5Bodyb.SetModel("models/gibs/hgibslarm_prop.mdl")
    __main__.CallEntitySpawn(punk5Bodyb)
    punk5Bodyc=__main__.CreateEntityNoSpawn("prop_physics",Find("f3_m_ghoul_1").GetOrigin(),Find("f3_m_ghoul_1").GetAngles())
    punk5Bodyc.SetName("punk5Bodyc")
    punk5Bodyc.SetModel("models/gibs/hgibsskull_prop.mdl")
    __main__.CallEntitySpawn(punk5Bodyc)

#--------------------------------------
#la_bradbury_2: tzimisce punk6 explode
def War4Tzpunk6boom():
    Find("tzpk6_explosion").SetOrigin(Find("f3_r_auspex_1").GetOrigin())
    __main__.ScheduleTask(0.1,"War4Tzpunk6boom1()")
    __main__.ScheduleTask(0.05,"War4Tzpunk6boom2()")

def War4Tzpunk6boom1():
    Find("tzpk6_explosion").Explode()

def War4Tzpunk6boom2():
    punk6Body=__main__.CreateEntityNoSpawn("prop_physics",Find("f3_r_auspex_1").GetOrigin(),Find("f3_r_auspex_1").GetAngles())
    punk6Body.SetName("punk6Body")
    punk6Body.SetModel("models/gibs/hgibstorso_prop.mdl")
    __main__.CallEntitySpawn(punk6Body)
    punk6Bodya=__main__.CreateEntityNoSpawn("prop_physics",Find("f3_r_auspex_1").GetOrigin(),Find("f3_r_auspex_1").GetAngles())
    punk6Bodya.SetName("punk6Bodya")
    punk6Bodya.SetModel("models/gibs/hgibslleg_prop.mdl")
    __main__.CallEntitySpawn(punk6Bodya)
    punk6Bodyb=__main__.CreateEntityNoSpawn("prop_physics",Find("f3_r_auspex_1").GetOrigin(),Find("f3_r_auspex_1").GetAngles())
    punk6Bodyb.SetName("punk6Bodyb")
    punk6Bodyb.SetModel("models/gibs/hgibslarm_prop.mdl")
    __main__.CallEntitySpawn(punk6Bodyb)
    punk6Bodyc=__main__.CreateEntityNoSpawn("prop_physics",Find("f3_r_auspex_1").GetOrigin(),Find("f3_r_auspex_1").GetAngles())
    punk6Bodyc.SetName("punk6Bodyc")
    punk6Bodyc.SetModel("models/gibs/hgibsskull_prop.mdl")
    __main__.CallEntitySpawn(punk6Bodyc)

#--------------------------------------
#la_bradbury_1: player killed Jenny
def JennyKilled():
    __main__.FindPlayer().AwardExperience("Sabbatsewer01")

#--------------------------------------
#la_bradbury_1: boiler room scripts
def SabWarLever1Activate():
    __main__.G.SabWar_Lever1 = 1
    Find("pipe1_act_sound").PlaySound()
    if (__main__.G.SabWar_Lever1 == 1 and __main__.G.SabWar_Lever2 == 1 and __main__.G.SabWar_Valve1 == 1 and __main__.G.SabWar_Valve2 == 1):
        Find("lights_off").Trigger()
        Find("valve1_act_sound").StopSound()
        Find("valve2_act_sound").StopSound()
        __main__.G.SabWar_LightsOff = 1

def SabWarLever1Deactivate():
    __main__.G.SabWar_Lever1 = 0
    Find("pipe1_act_sound").StopSound()
#----------
def SabWarLever2Activate():
    __main__.G.SabWar_Lever2 = 1
    Find("pipe2_act_sound").PlaySound()
    if (__main__.G.SabWar_Lever1 == 1 and __main__.G.SabWar_Lever2 == 1 and __main__.G.SabWar_Valve1 == 1 and __main__.G.SabWar_Valve2 == 1):
        Find("lights_off").Trigger()
        Find("valve1_act_sound").StopSound()
        Find("valve2_act_sound").StopSound()
        __main__.G.SabWar_LightsOff = 1

def SabWarLever2Deactivate():
    __main__.G.SabWar_Lever2 = 0
    Find("pipe2_act_sound").StopSound()
#----------
def SabWarValve1Activate():
    __main__.G.SabWar_Valve1 = 1
    Find("valve1_act_sound").PlaySound()
    if (__main__.G.SabWar_Lever1 == 1 and __main__.G.SabWar_Lever2 == 1 and __main__.G.SabWar_Valve1 == 1 and __main__.G.SabWar_Valve2 == 1):
        Find("lights_off").Trigger()
        Find("valve1_act_sound").StopSound()
        Find("valve2_act_sound").StopSound()
        __main__.G.SabWar_LightsOff = 1

def SabWarValve1Deactivate():
    __main__.G.SabWar_Valve1 = 0
    Find("valve1_act_sound").StopSound()
#----------
def SabWarValve2Activate():
    __main__.G.SabWar_Valve2 = 1
    Find("valve2_act_sound").PlaySound()
    if (__main__.G.SabWar_Lever1 == 1 and __main__.G.SabWar_Lever2 == 1 and __main__.G.SabWar_Valve1 == 1 and __main__.G.SabWar_Valve2 == 1):
        Find("lights_off").Trigger()
        Find("valve1_act_sound").StopSound()
        Find("valve2_act_sound").StopSound()
        __main__.G.SabWar_LightsOff = 1

def SabWarValve2Deactivate():
    __main__.G.SabWar_Valve2 = 0
    Find("valve2_act_sound").StopSound()

#-------------------------------------------------------------------------------
#LIBRARY 2: la_library_2 Lich cast blast
def LichCastBlast():
    if(G.Lich_Dead == 1):
        return
    else:
        __main__.ScheduleTask(0.0,"LichCastBlastA()")

def LichCastBlastA():
    if(G.Lich_Transform == 1):
        Find("Lich").MakeInvincible(1)
        __main__.ScheduleTask(0.25,"LichCastBlast1()")
        __main__.ScheduleTask(0.75,"LichCastBlast1a()")
        Find("Lich").SpawnTempParticle("Lich_holy_lights2")
    else:
        __main__.ScheduleTask(0.0,"LichCastBlast1()")
        Find("Lich").SpawnTempParticle("Lich_holy_lights")

def LichCastBlast1():
    Find("Lich_cast_blast").BeginSequence()

def LichCastBlast1a():
    Find("Lich").MakeInvincible(0)

def LichBlast():
    pc = __main__.FindPlayer()
    coor = pc.GetOrigin()
    Find("lichblast_explosion").SetOrigin((coor[0],coor[1],coor[2]+40))
    __main__.ScheduleTask(0.75,"LichBlast1()")

def LichBlast1():
    Find("lichblast_explosion").Explode()

def LichKilled():
    __main__.FindPlayer().AwardExperience("Sabbatlibrary03")


#-------------------------------------------------------------------------------
#LIBRARY 1: la_library_1 tzimisce knight ghoul gibs dead
def KnightGibsSpawn():
    knightBody=__main__.CreateEntityNoSpawn("prop_ragdoll",Find("knight").GetOrigin(),Find("knight").GetAngles())
    knightBody.SetName("knightBody")
    knightBody.SetModel("models/character/npc/common/kain/kain_armor.mdl")
    __main__.CallEntitySpawn(knightBody)
    knightBodya=__main__.CreateEntityNoSpawn("prop_physics",Find("knight").GetOrigin(),Find("knight").GetAngles())
    knightBodya.SetName("knightBodya")
    knightBodya.SetModel("models/gibs/hgibslarm_prop.mdl")
    __main__.CallEntitySpawn(knightBodya)
    knightBodyb=__main__.CreateEntityNoSpawn("prop_physics",Find("knight").GetOrigin(),Find("knight").GetAngles())
    knightBodyb.SetName("knightBodyb")
    knightBodyb.SetModel("models/gibs/hgibslarm_prop.mdl")
    __main__.CallEntitySpawn(knightBodyb)
    knightBodyc=__main__.CreateEntityNoSpawn("prop_physics",Find("knight").GetOrigin(),Find("knight").GetAngles())
    knightBodyc.SetName("knightBodyc")
    knightBodyc.SetModel("models/gibs/hgibsskull_prop.mdl")
    __main__.CallEntitySpawn(knightBodyc)

#--------------------------------------------------------
#LIBRARY 1: unlocks gallery door if key present
def checkForPasskeyGalleryDoor():
    pc = __main__.FindPlayer()
    if ( pc.HasItem("item_g_wireless_camera_3") ):
        Find("gallery_door_a_lock").Unlock()
        Find("gallery_door_b_lock").Unlock()
        Find("gallery_door_check").Disable()

#LIBRARY 1: using library card
def useCard():
    pc = __main__.FindPlayer()
    if(pc.HasItem("item_g_wireless_camera_3")):
        pc.RemoveItem("item_g_wireless_camera_3")
        __main__.G.Card_Inserted = 1

#--------------------------------------