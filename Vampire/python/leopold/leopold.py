print "loading leopold level script"

import __main__

from __main__ import G

Find = __main__.FindEntityByName

#added by dan_upright 09/12/04
#this is one of the ugliest hacks i've ever written
def WeDoAThingOfSomekind():
    print "this is radio rentals, open the pod bay doors hal"
    pc = __main__.FindPlayer()
    # Changed By CompMod
    # if (pc.clan == 5):
    if 5 == __main__.G._pcinfo["clan"]:
        taxi_landmark = Find("taxi_landmark")
        taxi_landmark.SetName("sewer_map_landmark")
        __main__.ChangeMap(2.5, "sewer_map_landmark", "escape_transition_nos")
        print "sailing to the sewers"
        return 0
    else:
        __main__.ChangeMap(2.5, "taxi_landmark", "escape_transition")
        print "sailing to the taxi"
        return 1
#changes end

# HTN - 03/10/04
#soc_exterior: if squad1 was in combat, turn on npc_cameras for squad2
def trigShouldEnableCam():
    print "soc_exterior: checking alarm status..."

    if ( G.soc_alarm_on == 1 ):
        print "soc_exterior: alarm triggered from squad1! enabling npc_cam for squad2..."
        cam1 = Find( "guard2cam1" )
        cam1.ScriptUnhide()
        cam2 = Find( "guard2cam2" )
        cam2.ScriptUnhide()

#SOCIETY 1 : turns off boulder so it doesn't do damage while at rest
def TurnOffBoulder():
    boulder = Find("boulder")
    if boulder: boulder.SetCausesImpactDamage(0)

#SOCIETY 4 : Flamethrower
def flameState():
    flame = Find("flamethrower")
    flamenode = Find("flamethrowernode")
    if flame: flame.ScriptUnhide()
    if flamenode: flamenode.ScriptUnhide()

#SOCIETY 4 : store timer for use in sp_soc_3
def storeTimer():
    timer = Find("get_out")
    G.Society_Countdown = timer.remaining_time

#SOCIETY 3 : setup timer to continue from sp_soc_4
def setupEscapeTimer():
    timer = Find("escape_timer")
    timer.count_time = G.Society_Countdown
    timer.RestartTimer()
    timer.StartTimer()
    timer.Show()

#SOCIETY : kill the player and end the game if player does not escape
def deathFromExplosion():
    endgame = Find("death_relay")
    endgame.Trigger()

#SOCIETY 3:  spawns Ash's cell key after guard dies.
def spawnAshKey():
    #if(G.Ash_Leave == 1):
        guard = Find("guard_patrol_5")
        center = guard.GetCenter()
        point = (center[0], center[1], center[2] +5)
        key = __main__.CreateEntityNoSpawn("item_k_ash_cell_key", point, (0,0,0) )
        key.SetName("ash_key")
        sparklies = __main__.CreateEntityNoSpawn("inspection_node", point, (0,0,0) )
        sparklies.SetParent("ash_key")
        __main__.CallEntitySpawn(key)
        __main__.CallEntitySpawn(sparklies)

def SaveJohansen():
    __main__.FindPlayer().HumanityAdd(1)
    __main__.FindPlayer().SetQuest("Johansen", 3)
    #changed by dan_upright 30/11/04
    __main__.FindPlayer().AwardExperience("Society03")
    #changes end
    if (G.Ash_Leave == 1 and G.Ash_Free == 0 and G.Patch_Plus == 1):
        __main__.FindPlayer().SetQuest("Ash", 3)

#added by wesp
def bachDeath():
    G.Bach_Death = 1
    Find("holyblast_timer").Disable()
    if G.Patch_Plus == 1:
        bach = Find("Bach")
        center = bach.GetCenter()
        point = (center[0], center[1], center[2] + 20)
        blade = __main__.CreateEntityNoSpawn("item_w_katana", point, (0,0,0) )
        blade.SetName("katana")
        sparklies = __main__.CreateEntityNoSpawn("inspection_node", point, (0,0,0) )
        sparklies.SetParent("katana")
        __main__.CallEntitySpawn(blade)
        __main__.CallEntitySpawn(sparklies)
        swat = __main__.CreateEntityNoSpawn("item_w_rem_m_700_bach", point, (0,0,0) )
        swat.SetName("rifle")
        sparklies1 = __main__.CreateEntityNoSpawn("inspection_node", point, (0,0,0) )
        sparklies1.SetParent("rifle")
        __main__.CallEntitySpawn(swat)
        __main__.CallEntitySpawn(sparklies1)

def BachDeathSpeak():
    bach = Find("bach_2")
    bach.PlayDialogFile("Character\dlg\MAIN CHARACTERS\BACH\line91_col_e.mp3")
    #changed by dan_upright 30/11/04
    __main__.FindPlayer().AwardExperience("Society01")
    #changes end
#-------------------------------------------------------------------------------
#SOCIETY 2: terminal scripts
def AlllasersOff():
    Find("all_lasers_off").Trigger()

def AlllasersReprogram():
    Find("all_lasers_reprogram").Trigger()

def BotsExplode():
    Find("all_bots_exp").Trigger()

def PulseGunsDisable():
    Find("pulse_1").TurnOff()
    Find("pulse_gun_sound").StopSound()

#SOCIETY 3: Killed ultra hunter
def Uhunter3Dead():
    __main__.FindPlayer().AwardExperience("Hunters02")

#-------------------------------------------------------------------------------
#SOCIETY 4: Bach cast holy blast
def BachCastHolyBlast():
    if(G.Bach_Death == 1):
        return
    else:
    	Find("Bach").MakeInvincible(1)
        __main__.ScheduleTask(0.25,"BachCastHolyBlast1()")

def BachCastHolyBlast1():
    Find("Bach_cast_holyblast").BeginSequence()

def BachHolyBlast():
    pc = __main__.FindPlayer()
    coor = pc.GetOrigin()
    Find("holyblast_explosion").SetOrigin((coor[0],coor[1],coor[2]+40))
    __main__.ScheduleTask(0.75,"BachHolyBlast1()")

def BachHolyBlast1():
    Find("holyblast_explosion").Explode()

#-------------------------------------------------------------------------------
print "leopold levelscript loaded"
