print "loading ventrue level script"

import __main__
import random
random.seed()

from __main__ import G

__main__.Level = __name__

Find = __main__.FindEntityByName
FindList = __main__.FindEntitiesByName
FindClass = __main__.FindEntitiesByClass

#PRINCE'S CHAMBERS:  Checks story state and unhides correct events, changed by wesp
def setupChamber():
    princeStart = Find("prince1")
    princeEnd = Find("prince2")

    # Changed By CompMod
    # if (__main__.IsClan(__main__.FindPlayer(), "Nosferatu")):
    if (5 == __main__.G._pcinfo["clan"]):
        taxi = Find("taxi")
        if taxi: taxi.Kill()
        cabbie = Find("cabbie")
        if cabbie: cabbie.Kill()

    if(princeStart):
        princeStart.SetDefaultDialogCamera("DialogDefault")

    # check for specific Story State events
    if(G.Story_State == 10):
        princeStart.SetDefaultDialogCamera("Dynamic3")
    elif (G.Story_State == 15):
        # Changed by CompMod
        # if (__main__.IsClan(__main__.FindPlayer(), "Ventrue")):
        if (8 == __main__.G._pcinfo["clan"]):
            torryPrim = Find("toreador_unhide")
            torryPrim.Trigger()
        else:
            ventPrim = Find("ventrue_unhide")
            ventPrim.Trigger()
    elif (G.Story_State == 60):
        actCoffin = Find("coffin_state")
        actCoffin.Trigger()

    # check to make sure the correct Prince is active
    if (G.Story_State < 30):
        princeStart.ScriptUnhide()
        princeEnd.ScriptHide()
    elif (G.Story_State == 30):
        princeEnd.ScriptUnhide()
        if(princeStart):
            princeStart.Kill()
        window = Find("prince_window")
        window.BeginSequence()
    elif (G.Story_State > 30):
        princeEnd.ScriptUnhide()
        if(princeStart):
            princeStart.Kill()

    # check to see if Beckett should be gone from Venture Tower
    if(G.Story_State >= 80):
        beckett = Find("beckett")
        if(beckett):
            beckett.Kill()

    if(G.Story_State == 110):
        relay = Find("exits_lock_relay")
        relay.Trigger()

#PRINCE'S CHAMBERS: turn prince around on Prince2, line 21
def turnPrinceAround():
    turn = Find("turn_around")
    turn.BeginSequence()

#PRINCE'S CHAMBERS:  pick which prince dialogue should be active
def pickAPrince():
    princeStart = Find("prince1")
    princeEnd = Find("prince2")
    if (G.Story_State < 30):
        princeStart.ScriptUnhide()
        princeEnd.ScriptHide()
    elif (G.Story_State >= 30):
        princeEnd.ScriptUnhide()
        princeStart.ScriptHide()

#PRINCE'S CHAMBERS:  fade out on map change
def changeVent():
    # Changed By CompMod
    # if (__main__.IsClan(__main__.FindPlayer(), "Nosferatu")):
    if (5 == __main__.G._pcinfo["clan"]):
        nosPort = Find("nos_teleport")
        nosPort.Trigger()
    else:
        othersPort = Find("others_teleport")
        othersPort.Trigger()

#PRINCE'S CHAMBERS:  choose which quest to send the player on
def princeQuests():
    if (G.Prince_Refuse == 1):
        G.Prince_Refuse = 0
        Find("lock_nos_out").Test()
        escort = Find("sheriff_escort")
        escort.BeginSequence()
        changeVent()
    elif (G.Wolf_Ending == 1):
        wereWolf = Find("teen_wolf_trigger")
        wereWolf.Trigger()
        print "YOU DANCING FOOL!!!"
    elif (G.Story_State == 65):
    #changed yet again by dan_upright 09/12/04
        if (G.move_to_sarcophagus_flag == 1):
            print "not doing the move thing"
        else:
            print "doing the move thing"
            relay = Find("move_to_sarcophagus")
            relay.Trigger()
            G.move_to_sarcophagus_flag = 1
    #changes end
    elif (G.Prince_Givekey == 1):
        Find("Start_Give_Prince_Key").Trigger()
    elif (G.Prince_Keepkey == 1):
        Find("Start_PC_Open_Sarc").Trigger()
    elif (G.Prince_Decision == 1):
        Find("Start_Prince_Beatdown").Trigger()
    elif(G.Prince_Regent == 1):
        Find("Start_Prince_Beatdown").Trigger()
    if(G.Prince_Ending):
        relay = Find("exits_unlock_relay")
        relay.Trigger()

#PRINCE'S CHAMBERS:  sends you to society after talking to Beckett, disabled by wesp
def beckettQuest():
#    if (G.Society_Open == 1):
    if 0:
        changeVent()
        #__main__.ChangeMap(1.5, "society_mark", "society_change")

#PRINCE'S CHAMBERS: Chooses models to use for Camarilla Part1 Ending
def chooseCamarilla():
    # Changed By CompMod
    if(6 == __main__.G._pcinfo["clan"]):
        # if(__main__.IsClan(__main__.FindPlayer(), "Toreador")):
        change = Find("Regent_Guard_1")
        change.SetModel("models/character/pc/male/nosferatu/armor0/Nosferatu.mdl")
    elif(7 == __main__.G._pcinfo["clan"]):
        # elif(__main__.IsClan(__main__.FindPlayer(), "Tremere")):
        change = Find("Regent_Guard_2")
        change.SetModel("models/character/pc/male/nosferatu/armor0/Nosferatu.mdl")
    elif(3 == __main__.G._pcinfo["clan"]):
        # elif(__main__.IsClan(__main__.FindPlayer(), "Gangrel")):
        change = Find("Regent_Guard_3")
        change.SetModel("models/character/pc/male/nosferatu/armor0/Nosferatu.mdl")

#PRINCE'S CHAMBERS: Selects the correct ending to transition to from Give Prince Key ending
def checkEnding():
    if(G.Story_State == 125):
        Find("lonewolf_change").ScriptUnhide()
    else:
        Find("epilogue_change").ScriptUnhide()

#VENTRUETOWER:  Called after talking to Chunk, opening the elevator to the Prince, changed by wesp
def chunkResults():
    chunk = Find("Chunk2")
    killSafeArea = Find("setcombat")
    if(G.Chunk_Run == 1):
        cower = Find("chunk_cowers_run_1")
        cower.BeginSequence()
        killSafeArea.Trigger()
        chunk.SetRelationship("player D_FR 5")
        Find("base_elev_down_a").Unlock()
    elif(G.Chunk_Attack == 1):
        attack = Find("chunk_attacks_run_1")
        attack.BeginSequence()
        killSafeArea.Trigger()
        chunk.SetRelationship("player D_HT 5")
        Find("base_elev_down_a").Unlock()
    elif(G.Chunk_Open > 0 and G.Story_State != 65):
        chunkRelay   = Find("chunkRelay")
        chunkRelay.Trigger()

#VENTRUETOWER: Called when the player leaves the level
def leaveVentrue():
    if(G.Story_State == 110):
        __main__.ChangeMap(2.5, "caine_landmark", "VentrueTower_caine")
    else:
        __main__.ChangeMap(2.5, "VentrueTower_mark", "VentrueTower_hub")

#VENTRUETOWER: Called when the player leaves the level
def leaveVentrueNos():
    if(G.Story_State == 110):
        __main__.ChangeMap(2.5, "caine_nos_landmark", "VentrueTower_caine")
    else:
        __main__.ChangeMap(2.5, "ventrue_nosferatu_entrance", "ventrue_sewers")

#VENTRUETOWER: Called to switch which camera is active in the Ventrue security room
def ventrueCameraSwitch():
    G.Ventrue_Camera = G.Ventrue_Camera + 1
    if(G.Ventrue_Camera > 5):
        G.Skyline_Camera = 1
    monitor = Find("monitor_2")
    monitor.SetCamera("camera_%i" % (G.Ventrue_Camera))

#VENTRUETOWER:  Called to change to combat for Nosferatu, changed by wesp
def ventrueCombat():
    combatTrigger = Find("combat_change")
    # Changed by CompMod
    # if (__main__.IsClan(__main__.FindPlayer(), "Nosferatu")):
    if 5 == __main__.G._pcinfo["clan"]:
        if (G.Story_State == 100 or G.Story_State >= 115):
            combatTrigger.Trigger()
            print "Combat Switched"
            # Fixed by Dheu
            __main__.ScheduleTask(1.0, "__main__.FindEntityByName(\"Chunk2\").ScriptUnhide()")
        taxi = Find("taxi")
        if taxi: taxi.Kill()
        cabbie = Find("cabbie")
        if cabbie: cabbie.Kill()

#VENTRUETOWER:  Disables the elevator when the player is not allowed up.
def elevatorStop():
    if (G.Story_State >= 35 and G.Story_State < 60):
        eleButtons = Find("base_elev_down")
        baseButtons = Find("base_btn_up")
        eleButtons.Lock()
        baseButtons.Lock()

#VENTRUETOWER:  Spawns the bomb after the bomb guy dies
def spawnBomb():
    bombGuy = Find("bomberman")
    center = bombGuy.GetCenter()
    point = (center[0] + 25, center[1] + 25, center[2])
    bomb = __main__.CreateEntityNoSpawn("item_g_astrolite", point, (0,0,0) )
    bomb.SetName("astrolite_bomb")
    sparklies = __main__.CreateEntityNoSpawn("inspection_node", point, (0,0,0) )
    sparklies.SetParent("astrolite_bomb")
    __main__.CallEntitySpawn(bomb)
    __main__.CallEntitySpawn(sparklies)

#VENTRUETOWER:  Despawns the bomb after placed
def despawnBomb():
    bomb = FindClass("item_g_astrolite")
    center = bomb[0].GetOrigin()
    angles = bomb[0].GetAngles()
    bomb[0].Kill()
    bombProp = Find("bomb_prop")
    bombProp.SetOrigin(center)
    bombProp.SetAngles(angles)
    bombProp.ScriptUnhide()

#SP_ENDSEQUENCES_B: Sets up players to avoid PC clan models
def setupCamarillaPart2():
    dude1 = Find("Gangrel_Pusher")
    dude2 = Find("Brujah_Pusher")
    dude3 = Find("Toreador_Pusher")
    dude4 = Find("Malkavian_Pusher")
    if (__main__.IsClan(__main__.FindPlayer(), "Gangrel")) :
        dude4.SetName("Regent2")
        dude4.ScriptUnhide()
        dude2.SetName("pusher1")
        dude2.ScriptUnhide()
        dude3.SetName("pusher2")
        dude3.ScriptUnhide()
    elif (__main__.IsClan(__main__.FindPlayer(), "Brujah")) :
        dude1.SetName("Regent2")
        dude1.ScriptUnhide()
        dude3.SetName("pusher1")
        dude3.ScriptUnhide()
        dude4.SetName("pusher2")
        dude4.ScriptUnhide()
    elif (__main__.IsClan(__main__.FindPlayer(), "Toreador")) :
        dude2.SetName("Regent2")
        dude2.ScriptUnhide()
        dude1.SetName("pusher1")
        dude1.ScriptUnhide()
        dude4.SetName("pusher2")
        dude4.ScriptUnhide()
    else :
        dude3.SetName("Regent2")
        dude3.ScriptUnhide()
        dude1.SetName("pusher1")
        dude1.ScriptUnhide()
        dude2.SetName("pusher2")
        dude2.ScriptUnhide()

#LA_VENTRUETOWER_1: functions for displaying Dominate effect
def dominatePlayer():
    __main__.FindPlayer().PlayHUDParticle("D_Dominate_HUD_Cast_emitter2")

def stopDominatePlayer():
    __main__.FindPlayer().StopHUDParticle(2)

#LA_VENTRUETOWER_1: LaCroix needs to float a line in a cutscene
def LaCroixCutsceneFloat():
    prince = Find("prince1")
    prince.PlayDialogFile("Character/dlg/Downtown LA/prince2/line1278_col_e.mp3")

#SP_ENSEQUENCES_B: Debug printing to find out of sync cameras
def DBprintname(x):
    print x

#-------------------------------------------------------ANTITRIBU---------------------------
#LA_VENTRUETOWER_1B:  Swat squad 1 die     
def SwatDie():
    if(G.Swat1_1Death == 1):
        if(G.Swat1_2Death == 1):
            if(G.Swat1_3Death == 1):
    		return
            else:
        	Find("floor_3_thug_6").PlayDialogFile("character/swat/swat3/swat3_4.wav")
    	else:
            Find("floor_3_thug_5").PlayDialogFile("character/swat/swat2/swat2_4.wav")
    else:
        Find("floor_3_thug_4").PlayDialogFile("character/swat/swat1/swat1_17.wav")

#--------------------------
#LA_VENTRUETOWER_1B:  Swat squad 1 battle cry
def SwatBattleCry():
        if(G.Swat1_1Death == 1 and G.Swat1_2Death == 1):
            if(G.Swat1_3Death == 1):
    		Find("swat1_battlecry_timer").Disable()
            else:
        	Find("swat3_battlecry").PickRandom()
        elif(G.Swat1_1Death == 1 and G.Swat1_3Death == 1):
            if(G.Swat1_2Death == 1):
    		Find("swat1_battlecry_timer").Disable()
            else:
        	Find("swat2_battlecry").PickRandom()
        elif(G.Swat1_2Death == 1 and G.Swat1_3Death == 1):
            if(G.Swat1_1Death == 1):
    		Find("swat1_battlecry_timer").Disable()
            else:
        	Find("swat1_battlecry").PickRandom()
        elif(G.Swat1_1Death == 1):
            Find("swat23_battlecry").PickRandom()
        elif(G.Swat1_2Death == 1):
            Find("swat13_battlecry").PickRandom()
        elif(G.Swat1_3Death == 1):
            Find("swat12_battlecry").PickRandom()
        else:
            Find("swat123_battlecry").PickRandom()

#-------------------------
#LA_VENTRUETOWER_1B:   Swat squad 2 die    
def Swat2Die():
    if(G.Swat2_1Death == 1):
        if(G.Swat2_2Death == 1):
            if(G.Swat2_3Death == 1):
    		return
            else:
        	Find("floor_4_thug_2").PlayDialogFile("character/swat/swat3/swat3_4.wav")
    	else:
            Find("floor_4_thug_3").PlayDialogFile("character/swat/swat2/swat2_4.wav")
    else:
        Find("floor_4_thug_10").PlayDialogFile("character/swat/swat1/swat1_17.wav")

#--------------------------
#LA_VENTRUETOWER_1B:  Swat squad 2 battle cry
def Swat2BattleCry():
        if(G.Swat2_1Death == 1 and G.Swat2_2Death == 1):
            if(G.Swat2_3Death == 1):
    		Find("swat2_battlecry_timer").Disable()
            else:
        	Find("swat3_battlecry2").PickRandom()
        elif(G.Swat2_1Death == 1 and G.Swat2_3Death == 1):
            if(G.Swat2_2Death == 1):
    		Find("swat2_battlecry_timer").Disable()
            else:
        	Find("swat2_battlecry2").PickRandom()
        elif(G.Swat2_2Death == 1 and G.Swat2_3Death == 1):
            if(G.Swat2_1Death == 1):
    		Find("swat2_battlecry_timer").Disable()
            else:
        	Find("swat1_battlecry2").PickRandom()
        elif(G.Swat2_1Death == 1):
            Find("swat23_battlecry2").PickRandom()
        elif(G.Swat2_2Death == 1):
            Find("swat13_battlecry2").PickRandom()
        elif(G.Swat2_3Death == 1):
            Find("swat12_battlecry2").PickRandom()
        else:
            Find("swat123_battlecry2").PickRandom()

#-------------------------
#LA_VENTRUETOWER_2:   Swat squad 3 die    
def Swat3Die():
    if(G.Swat3_1Death == 1):
        if(G.Swat3_2Death == 1):
            if(G.Swat3_3Death == 1):
    		return
            else:
        	Find("thug_4").PlayDialogFile("character/swat/swat3/swat3_4.wav")
    	else:
            Find("thug_3").PlayDialogFile("character/swat/swat2/swat2_4.wav")
    else:
        Find("thug_1").PlayDialogFile("character/swat/swat1/swat1_17.wav")

#--------------------------
#LA_VENTRUETOWER_2:  Swat squad 3 battle cry
def Swat3BattleCry():
        if(G.Swat3_1Death == 1 and G.Swat3_2Death == 1):
            if(G.Swat3_3Death == 1):
    		Find("swat3_battlecry_timer").Disable()
            else:
        	Find("swat3_battlecry3").PickRandom()
        elif(G.Swat3_1Death == 1 and G.Swat3_3Death == 1):
            if(G.Swat3_2Death == 1):
    		Find("swat3_battlecry_timer").Disable()
            else:
        	Find("swat2_battlecry3").PickRandom()
        elif(G.Swat3_2Death == 1 and G.Swat3_3Death == 1):
            if(G.Swat3_1Death == 1):
    		Find("swat3_battlecry_timer").Disable()
            else:
        	Find("swat1_battlecry3").PickRandom()
        elif(G.Swat3_1Death == 1):
            Find("swat23_battlecry3").PickRandom()
        elif(G.Swat3_2Death == 1):
            Find("swat13_battlecry3").PickRandom()
        elif(G.Swat3_3Death == 1):
            Find("swat12_battlecry3").PickRandom()
        else:
            Find("swat123_battlecry3").PickRandom()

#-------------------------
#LA_VENTRUETOWER_2:   Swat squad 4 die    
def Swat4Die():
    if(G.Swat4_1Death == 1):
        if(G.Swat4_2Death == 1):
            if(G.Swat4_3Death == 1):
    		return
            else:
        	Find("thug_12").PlayDialogFile("character/swat/swat3/swat3_4.wav")
    	else:
            Find("thug_10").PlayDialogFile("character/swat/swat2/swat2_4.wav")
    else:
        Find("thug_9").PlayDialogFile("character/swat/swat1/swat1_17.wav")

#--------------------------
#LA_VENTRUETOWER_2:  Swat squad 4 battle cry
def Swat4BattleCry():
        if(G.Swat4_1Death == 1 and G.Swat4_2Death == 1):
            if(G.Swat4_3Death == 1):
    		Find("swat4_battlecry_timer").Disable()
            else:
        	Find("swat3_battlecry4").PickRandom()
        elif(G.Swat4_1Death == 1 and G.Swat4_3Death == 1):
            if(G.Swat4_2Death == 1):
    		Find("swat4_battlecry_timer").Disable()
            else:
        	Find("swat2_battlecry4").PickRandom()
        elif(G.Swat4_2Death == 1 and G.Swat4_3Death == 1):
            if(G.Swat4_1Death == 1):
    		Find("swat4_battlecry_timer").Disable()
            else:
        	Find("swat1_battlecry4").PickRandom()
        elif(G.Swat4_1Death == 1):
            Find("swat23_battlecry4").PickRandom()
        elif(G.Swat4_2Death == 1):
            Find("swat13_battlecry4").PickRandom()
        elif(G.Swat4_3Death == 1):
            Find("swat12_battlecry4").PickRandom()
        else:
            Find("swat123_battlecry4").PickRandom()

#----------------------------------------------------------------------------------
#LA_VENTRUETOWER_2: Bomberman explode
def BombermanBoom():
    Find("bomberman_explosion").SetOrigin(Find("bomberman").GetOrigin())
    __main__.ScheduleTask(0.1,"BombermanBoom1()")
    __main__.ScheduleTask(0.05,"BombermanBoom2()")

def BombermanBoom1():
    Find("bomberman_explosion").Explode()

def BombermanBoom2():
    bbBody=__main__.CreateEntityNoSpawn("prop_physics",Find("bomberman").GetOrigin(),Find("bomberman").GetAngles())
    bbBody.SetName("bbBody")
    bbBody.SetModel("models/gibs/hgibstorso_prop.mdl")
    __main__.CallEntitySpawn(bbBody)
    bbBodya=__main__.CreateEntityNoSpawn("prop_physics",Find("bomberman").GetOrigin(),Find("bomberman").GetAngles())
    bbBodya.SetName("bbBodya")
    bbBodya.SetModel("models/gibs/hgibslleg_prop.mdl")
    __main__.CallEntitySpawn(bbBodya)
    bbBodyb=__main__.CreateEntityNoSpawn("prop_physics",Find("bomberman").GetOrigin(),Find("bomberman").GetAngles())
    bbBodyb.SetName("bbBodyb")
    bbBodyb.SetModel("models/gibs/hgibslarm_prop.mdl")
    __main__.CallEntitySpawn(bbBodyb)
    bbBodyc=__main__.CreateEntityNoSpawn("prop_physics",Find("bomberman").GetOrigin(),Find("bomberman").GetAngles())
    bbBodyc.SetName("bbBodyc")
    bbBodyc.SetModel("models/gibs/hgibsskull_prop.mdl")
    __main__.CallEntitySpawn(bbBodyc)

#--------------------------
#LA_VENTRUETOWER_2: Last ventrue guard cast dominate.          
def VentrueCastDominate():
    pc = __main__.FindPlayer()
    clan = pc.clan
    if(G.Ventrue_guard_death == 1):
        return
    else:
        Find("OfficeGuard1_cast_dom").BeginSequence()
        if(pc.base_dominate >= 4 or G.Player_Ashes_Form == 1):
	    __main__.ScheduleTask(0.1,"PcResistDominate()")
        else:
            if(clan == 13):
	        __main__.ScheduleTask(0.1,"GargoyleDominate()")
            else:
	        __main__.ScheduleTask(0.1,"VentrueCastDominate1()")

def VentrueCastDominate1():
    Find("sound1_dominate").PlaySound()
    Find("sound2_dominate").PlaySound()
    __main__.ScheduleTask(0.1,"VentrueCastDominate2()")

def VentrueCastDominate2():
    Find("pc_fall_sleep").BeginSequence()
    __main__.ScheduleTask(2.1,"VentrueCastDominate3()")

def VentrueCastDominate3():
    Find("pc_sleep_getup").BeginSequence()

#SP_GIOVANNI_2AB: dominate if PC gargoyle.
def GargoyleDominate():
    Find("sound1_dominate").PlaySound()
    Find("sound2_dominate").PlaySound()
    Find("pc_gargoyle_dom").BeginSequence()
    __main__.ScheduleTask(3.75,"GargoyleDominate1()")

def GargoyleDominate1():
    Find("pc_gargoyle_dom2").BeginSequence()

#SP_GIOVANNI_2AB: PC resist dominate.  
def PcResistDominate():
    __main__.FindPlayer().SpawnTempParticle("dom_particles1")
    __main__.FindPlayer().ClearActiveDisciplines()
    __main__.ScheduleTask(1.05,"PcResistDominate1()")

def PcResistDominate1():
    Find("pc_dominate").RemoveControllerNPC()


#--------------------------
print "levelscript loaded"
