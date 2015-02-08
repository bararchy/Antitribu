print "Loading Giovani Level Script..."

import __main__

from __main__ import G
from random import Random
from time import time

Find = __main__.FindEntityByName
Finds = __main__.FindEntitiesByName

# added by wesp
def civilianDeath():
    pc = __main__.FindPlayer()
    if(pc.humanity >= 3):
        pc.HumanityAdd( -1 )

#sp_giovanni_1: set all to gone outside the house
def gio1_KillAllOutside():
    print ( "***************** Starting to Remove NPCs ******************" )
    spawner = Find( "maker_guard_north" )
    if (spawner):
        print ( "************* Killed Spawner North ****************" )
        spawner.Kill()
    else:
        print ( "************* Couldnt Find Spawner North ****************" )

    spawner = Find( "maker_guard_east" )
    if (spawner):
        print ( "************* Killed Spawner East ****************" )
        spawner.Kill()
    else:
        print ( "************* Couldnt Find Spawner East ****************" )

    spawner = Find( "maker_guard_west" )
    if (spawner):
        print ( "************* Killed Spawner West ****************" )
        spawner.Kill()
    else:
        print ( "************* Couldnt Find Spawner West ****************" )

    guard4 = Find( "guard_patrol4" )
    if (guard4):
        print ( "************* Killed Guard 4 ****************" )
        guard4.Kill()
    else:
        print ( "************* Couldnt Find Guard 4 ****************" )

    guards = Finds( "guard_spawned" )
    for guard in guards:
        if (guard):
            print ( "************* Killed Guard guard_spawned ****************" )
            guard.Kill()
        else:
            print ( "************* Couldnt Find Guard Spawned ****************" )

    guard6 = Find( "guard_patrol6" )
    if (guard6):
        print ( "************* Killed Guard 6 ****************" )
        guard6.Kill()
    else:
        print ( "************* Couldnt Find Guard 6 ****************" )

    guard5 = Find( "guard_patrol5" )
    if (guard5):
        guard5.Kill()
        print ( "************* Killed Guard P5 ****************" )
    else:
        print ( "************* Couldnt Find Guard P5 ****************" )

    guard5_b = Find( "guard_patrol5_backyard" )
    if (guard5_b):
        print ( "************* Killed Guard P5_B ****************" )
        guard5_b.Kill()
    else:
        print ( "************* Couldnt Find Guard P5_B ****************" )

    guard3 = Find( "guard_patrol3" )
    if (guard3):
        print ( "************* Killed Guard P3 ****************" )
        guard3.Kill()
    else:
        print ( "************* Couldnt Find Guard P3 ****************" )

    guards = Finds( "guard" )
    for guard in guards:
        if (guard):
            print ( "************* Killed Guard ****************" )
            guard.Kill()
        else:
            print ( "************* Couldnt Find Guard ****************" )

    partygoers = Finds( "partygoer" )
    for partygoer in partygoers:
        if partygoer:
            print ( "************* Killed Partygoer ****************" )
            partygoer.Kill()
        else:
            print ( "************* Couldnt Find Partygoer ****************" )

    luca = Find( "Luca" )
    if (luca):
        print ( "************* Killed Luca 4 ****************" )
        luca.Kill()
    else:
        print ( "************* Couldnt Find Luca****************" )

    victor = Find( "Victor" )
    if (victor):
        print ( "************* Killed Victor ****************" )
        victor.Kill()
    else:
        print ( "************* Couldnt Find Victor ****************" )

    maria = Find( "Maria" )
    if (maria):
        maria.Kill()
        print ( "************* Killed Maria ****************" )
    else:
        print ( "************* Couldnt Find Maria ****************" )
    print ( "******************* Done Removing NPCs *****************" )

#sp_giovanni_1: check for loading sarcophagus into truck cutscene
def cutscene():
    print ( "******************** Starting Cut Scene ********************" )
    logic = Find("logic_scene")
    logic.Trigger()
    world = Find("world")
    world.SetNoFrenzyArea(1)
    G.Giovanni_Open = 0

#Opens Front Doors
def gio1_openFront():
    open = Find("Relay_Open_Front_Door")
    open.Trigger()

#sp_giovanni_1: set all to hate outside the house
def gio1_aggroOutside():
    G.GioBotchedOutside = 1
    guard4 = Find( "guard_patrol4" )
    if (guard4):
        guard4.SetRelationship( "player D_HT 5" )

    guard6 = Find( "guard_patrol6" )
    if (guard6):
        guard6.SetRelationship( "player D_HT 5" )

    guard5 = Find( "guard_patrol5" )
    if (guard5):
        guard5.SetRelationship( "player D_HT 5" )

    guard5_b = Find( "guard_patrol5_backyard" )
    if (guard5):
        guard5.SetRelationship( "player D_HT 5" )

    guard3 = Find( "guard_patrol3" )
    if (guard3):
        guard3.SetRelationship( "player D_HT 5" )

    guards = Finds( "guard" )
    for guard in guards:
        if (guard):
            guard.SetRelationship( "player D_HT 5" )

    partygoers = Finds( "partygoer" )
    for partygoer in partygoers:
        if partygoer:
            partygoer.SetRelationship( "player D_HT 5" )

    luca = Find( "Luca" )
    if (luca):
        luca.SetRelationship( "player D_HT 5" )

    victor = Find( "Victor" )
    if (victor):
        victor.SetRelationship( "player D_HT 5" )

    maria = Find( "Maria" )
    if (maria):
        maria.SetRelationship( "player D_HT 5" )
        print "********** Set all Outside to Hate **********"

#sp_giovanni_2: set all to hate inside the house
def gio2_aggroInside():
    adam = Find( "Adam" )
    if (adam):
        adam.SetRelationship( "player D_HT 5" )

    guests = Finds( "Guest" )
    for guest in guests:
        if ( guest ):
            guest.SetRelationship( "player D_HT 5" )

    guard1 = Find( "guard_1" )
    if (guard1):
        guard1.SetRelationship( "player D_HT 5" )

    guard2 = Find( "guard_2" )
    if (guard2):
        guard2.SetRelationship( "player D_HT 5" )

    guard3 = Find( "guard_3" )
    if (guard3):
        guard3.SetRelationship( "player D_HT 5" )

    guard3a = Find( "guard_3a" )
    if (guard3a):
        guard3a.SetRelationship( "player D_HT 5" )

    guard4 = Find( "guard_4" )
    if (guard4):
        guard4.SetRelationship( "player D_HT 5" )

    guard5 = Find( "guard_5" )
    if (guard5):
        guard5.SetRelationship( "player D_HT 5" )

    guard6 = Find( "guard_6" )
    if (guard6):
        guard6.SetRelationship( "player D_HT 5" )

    guard7 = Find( "guard_7" )
    if (guard7):
        guard7.SetRelationship( "player D_HT 5" )

    chris = Find( "Christopher" )
    if (chris):
        chris.SetRelationship( "player D_HT 5" )

    mira = Find( "Mira" )
    if (mira):
        mira.SetRelationship( "player D_HT 5" )

    nadia = Find( "Nadia" )
    if (nadia):
        nadia.SetRelationship( "player D_HT 5" )
        print "********** Set all Inside to Hate **********"

#Nosferatu Check
def checkNosferatu():
    print "***************** Checking for NOS *****************"
    if( __main__.IsClan( __main__.FindPlayer(), "Nosferatu" ) ):
        print "********** Is NOS **********"
        gio1_aggroOutside()
        gio2_aggroInside()
    else:
        print "********** Not NOS **********"

#sp_giovanni_1: set victor and maria to panic
def gio1_panicVictorMaria():
    victor = Find( "Victor" )
    if victor: victor.SetRelationship( "player D_HT 5" )

    mariaSeq = Find( "Sequence_Maria_Panic" )
    mariaSeq.BeginSequence()

#sp_giovanni_2: set all guests inside house to flee and die
def gio2_guestsFlee():
    guest = Find( "Guest" )
    for guest in guests:
        if guest:
            guest.FleeAndDie()

    adam = Find( "Adam" )
    if adam: adam.FleeAndDie()

    chris = Find( "Christopher" )
    if chris: chris.FleeAndDie()

    mira = Find( "Mira" )
    if mira: mira.FleeAndDie()

    nadia = Find( "Nadia" )
    if nadia: nadia.FleeAndDie()

#Starts Nadia leading the PC
def gio2_nadiaLead():
    lead = Find("Relay_FollowMe_1")
    lead.Trigger()

#Starts Nadia pissed at the PC and leaves, changed by wesp
def nadiaLeave():
    if (G.Nadia_Leave == 1):
        print ( "***************** leave *****************" )
        leave = Find("Relay_Nadia_Leaves")
        leave.Trigger()

#Fires on Giovanni2a Load, changed by wesp
def onGio1Load():
    print ( "***************** Running Gio1 Loading Script *****************" )
    G.GioGuard = 0
    print ( "***************** Reset Guard DLGs *****************" )
    if ( G.Story_State == 60 ):
        gio1_KillAllOutside()
        cutscene()
        print ( "***************** Playing Loading Movie *****************" )
        return
    checkNosferatu()
    if ( G.BochedGio == 1 ):
        print ( "***************** Botched Setting Hostile *****************" )
        relay = Find( "Relay_Boched_Level" )
        relay.Trigger()
    else:
        return

#Fires on Giovanni2a Load, changed by wesp
def onGio2aLoad():
    G.BeenToGioParty = 1
    pc = __main__.FindPlayer()
    state = pc.GetQuestState("Giovanni")
    if (state < 2):
        pc.SetQuest("Giovanni", 2)
        print ( "************* Infiltrated the Giovanni Mansion ****************" )
    if (G.Nadia_G3 == 1):
        Nadia = Find("Nadia")
        if Nadia: Nadia.ScriptHide()
        float = Find("Choreo_FollowMe")
        if float: float.ScriptHide()

def onGio2bLoad():
    pc = __main__.FindPlayer()
    state = pc.GetQuestState("Giovanni")
    if (state < 2):
        pc.SetQuest("Giovanni", 2)
        print ( "************* Infiltrated the Giovanni Mansion ****************" )

#Checks to see if zombies are hostile when Nadia takes damage
def damCheck():
    if ( G.zombies_hate == 1):
        flee = Find("Relay_Nadia_Flees")
        flee.Trigger()

#sp_giovanni_3: check if allzombies dead, set nadia
def gio3_checkAllZombieDeadAndZone():
    counter = 0
    if ( G.gio_2_nadia_pt == 1 ):
        zombies = Finds( "Zombie_Spawned" )
        for zombie in zombies:
            if ( zombie.IsAlive() ):
                counter = counter + 1

        if counter > 0:
            print "sp_giovanni_3: zoning without nadia! kill her!"
            G.gio_3_startzombies = 0
            G.gio_2_nadia_pt = 0
            Nadia = Find( "Nadia" )
            if Nadia:
                Nadia.Kill()

#sp_giovanni_3: check if all zombies dead, set nadia
def gio3_checkAllZombieDead():
    G.ZombiesDead = ( G.ZombiesDead + 1 )
    counter = 0
    zombies = Finds( "Zombie_Spawned" )
    for zombie in zombies:
        if ( zombie.IsAlive() ):
            counter = counter + 1
            G.Zombies = ( counter )
    if counter == 0:
        relay = Find( "Relay_Zombies_Dead" )
        relay.Trigger()
    else:
        print( "******************** Still More Zombies to Kill ************************" )

#sp_giovanni_3: check if nadia should run from zombies yet
def gio3_checkNadiaRunZombie():
    if ( G.gio_3_startzombies == 1 ):
        print "sp_giovanni_3: zombie attack!"
        seq = Find( "seq_nadia2" )
        if seq:
            seq.BeginSequence()
        zombies = Finds( "zombie_1" )
        for zombie in zombies:
            if zombie:
                zombie.ScriptUnhide()

#Giovanni 3 Progress Nadia to sequence 2b
def nadiaTo2b():
    relayTo2b = Find( "Relay_Nadia_to_2b" )
    relayTo2b.Trigger()

#sp_giovanni_3: unhide begin nadia dialog, changed by wesp
def gio3_checkNadiaUnhide():
    if ( G.gio_2_nadia_pt == 1 ):
        Nadia = Find( "Nadia" )
        Nadia.ScriptUnhide()
        G.Nadia_G3 = 1
    else:
        Relay = Find("Relay_Nadia_Flees")
        if Relay: Relay.Kill()
        Relay1 = Find("Relay_Nadia_Escapes")
        if Relay1: Relay1.Kill()
        float = Find("choreo_TooMuch")
        if float: float.ScriptHide()
        float = Find("choreo_Comon")
        if float: float.ScriptHide()
        float = Find("choreo_ThisWay")
        if float: float.ScriptHide()
        float = Find("choreo_InHere")
        if float: float.ScriptHide()
        float = Find("choreo_PointRight1")

#sp_giovanni_3: keep door open, added by wesp
def changeLevelCheck():
    if ( G.Nadia_Fright == 1 ):
        print ( "********* cleaning up *************" )
        door = Find("door_fake")
        door.ScriptHide()
        block = Find("door_block")
        block.ScriptHide()
        float = Find("Nadia_Motioning1")
        float.ScriptHide()
        float = Find("choreo_thisway")
        float.ScriptHide()
        float = Find("choreo_comon")
        float.ScriptHide()
        Nadia = Find("Nadia")
        Nadia.ScriptHide()
    else:
        door = Find("door_fake")
        door.ScriptUnhide()
        block = Find("door_block")
        block.ScriptUnhide()

#sp_giovanni_1: set alarm state for g_1
def gio1_setAlarm():
    if ( G.gio_1_alarm == 0 ):
        print "sp_giovanni_1: alarm is set! spawner triggers enabled!"
        G.gio_1_alarm = 1

        #unhide spawner triggers
        triggers = Finds( "trig_spawners" )
        for trigger in triggers:
            if trigger:
                trigger.ScriptUnhide()

        #turn on spawners
        gio1_activateSpawners()

#Entrance Check for chooseing to go to 2a or 2b
def entranceFrontCheck():
    if ( G.BeenToGioParty == 1 ):
        __main__.ChangeMap(1, "frontload_landmark", "frontload_a")
        return
    if ( G.GioBotchedOutside == 1 ):
        __main__.ChangeMap(1, "frontload_landmark", "frontload_b")
        return
    else:
        __main__.ChangeMap(1, "frontload_landmark", "frontload_a")

def entranceBackCheck():
    if ( G.BeenToGioParty == 1 ):
        __main__.ChangeMap(1, "backload_landmark", "backload_a")
        return
    if ( G.GioBotchedOutside == 1 ):
        __main__.ChangeMap(1, "backload_landmark", "backload_b")
        return
    else:
        __main__.ChangeMap(1, "backload_landmark", "backload_a")

#sp_giovanni_1: activate guard spawners
def gio1_activateSpawners():
    spawner = Find( "maker_guard_east" )
    spawner.Enable()
    spawner = Find( "maker_guard_west" )
    spawner.Enable()
    spawner = Find( "maker_guard_north" )
    spawner.Enable()

#sp_giovanni_1: deactivate guard spawners
def gio1_deactivateSpawners():
    spawner = Find( "maker_guard_east" )
    spawner.Enable()
    spawner = Find( "maker_guard_west" )
    spawner.Enable()
    spawner = Find( "maker_guard_north" )
    spawner.Enable()

#sp_giovanni_1: happens after killing Victor, changed by wesp
def spawnVictorInvite():
    victor = Find("Victor")
    center = victor.GetCenter()
    point = (center[0], center[1], center[2])
    invitev = __main__.CreateEntityNoSpawn("item_g_giovanni_invitation_victor", point, (0,0,0) )
    invitev.SetName("vic_inv")
    sparklies = __main__.CreateEntityNoSpawn("inspection_node", point, (0,0,0) )
    sparklies.SetParent("vic_inv")
    if G.Victor_Dominate == 0: 
        __main__.CallEntitySpawn(invitev)
        __main__.CallEntitySpawn(sparklies)

#sp_giovanni_1: happens after killing Maria, changed by wesp
def spawnMariaInvite():
    maria = Find("Maria")
    center = maria.GetCenter()
    point = (center[0], center[1], center[2])
    invitem = __main__.CreateEntityNoSpawn("item_g_giovanni_invitation_maria", point, (0,0,0) )
    invitem.SetName("mar_inv")
    sparklies = __main__.CreateEntityNoSpawn("inspection_node", point, (0,0,0) )
    sparklies.SetParent("mar_inv")
    if G.Maria_Dominate == 0:
        __main__.CallEntitySpawn(invitem)
        __main__.CallEntitySpawn(sparklies)

#sp_giovanni_1: happens after threatening Victor or Maria
def gio1_victorMariaFlee():
    victor = Find("Victor")
    if victor: victor.SetRelationship( "player D_HT 5" )

    maria = Find("Maria")
    if maria: maria.SetRelationship( "player D_HT 5" )

    flee = Find("Relay_VictorMariaFlee")
    flee.Trigger()

#Level3 break door look at
def breakDoorLook():
    print ( "********* Triggered Break Look *************" )
    if ( G.ZombiesDead > 5 ):
        print ( "********* Breaking Door *************" )
        relay = Find( "Relay_break_door" )
        relay.Trigger()
    else:
        print ( "********* No Break *************" )

#Level4 Zombie kill counter, changed by wesp
def zombieKillCounter():
    G.ZombieKills = G.ZombieKills + 1
    if(G.ZombieKills >= 7):
        openroom = Find("Relay_UnLock_ZombRoom")
        openroom.Trigger()

#sp_giovanni_5: happens after chang brothers are killed, changed by wesp
def gio5_changDefeated():
    G.Story_State = 60
    G.Chunk_Open = 4
    __main__.ChangeMap(3, "truckmark", "trig_shortcut")

#Fix way back from 3 to 2 if started combat on 2

#sp_giovanni_1: check for loading sarcophagus into truck cutscene, changed by wesp
def cutscene():
    if G.Story_State == 60:
        pc = Find("playerevents")
        pc.RemoveDisciplinesNow()
##      logic = Find("logic_scene")
##      logic.Trigger()
        __main__.ScheduleTask(1.0, "__main__.FindEntityByName(\'logic_scene\').Trigger()")
        world = Find("world")
        world.SetNoFrenzyArea(1)
        G.Giovanni_Open = 0

#Bodyguard init DLG, changed by wesp
def bodyguardChangeName(name):
    print "changing name from %s to guard_7" % name
    G.Guards_Name = name
    talkguard = Find(name)
    if talkguard: talkguard.SetName("guard_7")

def bodyguardRevertName():
    print "changing name to %s from guard_7" % G.Guards_Name
    talkguard = Find("guard_7")
    if talkguard: talkguard.SetName(G.Guards_Name)

def bodyguardRandResponce():
    R = Random( time() )
    G.GioGuard = R.randint (2, 4)
    bodyguardRevertName()

#Experience for killing Bruno, added by wesp
def brunoD():
    G.Bruno_Killed = 1
    pc = __main__.FindPlayer()
    pc.SetQuest("Sarcophagus", 5)

def foundSarcophagusRoom():
    pc = __main__.FindPlayer()
    state = pc.GetQuestState("Giovanni")
    if (state < 3):
        pc.SetQuest("Giovanni", 3)
        print ( "************* Found the Sarcophagus Room ****************" )

def killedChangs():
    pc = __main__.FindPlayer()
    state = pc.GetQuestState("Giovanni")
    if (state < 4):
        pc.SetQuest("Giovanni", 4)
        print ( "************* Killed the Changs ****************" )

#sp_giovanni_1: Float Line for Victor
def VictorFloatLeave():
    victor = Find("Victor")
    victor.PlayDialogFile("Character\dlg\Giovanni\Victor\line191_col_e.mp3")

#Pisha quest, changed by wesp
def foundGiovanniBook():
    pc = __main__.FindPlayer()
    state = pc.GetQuestState("Occult")
    if state == 2:
        pc.SetQuest("Occult", 4)
        print ( "************* Found Book for Pisha ****************" )
    elif state == 1:
        pc.SetQuest("Occult", 3)
    else:
        print ( "************* Found Giovanni Book ****************" )

#-----------------------------------------------------------------------
#SP_GIOVANNI_2AB: Bruno cast necromancy and dominate.         
def BrunoCast():
    if(G.bruno_cast == 1):
        #return
	__main__.ScheduleTask(9.5,"BrunoCast1()")
    else:
        Find("spell_chooser").PickRandom()
	__main__.ScheduleTask(9.5,"BrunoCast1()")

def BrunoCast1():
    G.bruno_cast = 0
    __main__.ScheduleTask(1.05,"BrunoCast()")

#SP_GIOVANNI_2AB: Bruno cast dominate.          
def BrunoCastDominate():
    pc = __main__.FindPlayer()
    clan = pc.clan
    if(G.bruno_death == 1):
        return
    else:
        Find("Bruno_cast_dom").BeginSequence()
        if(pc.base_dominate >= 4 or G.Player_Ashes_Form == 1):
	    __main__.ScheduleTask(0.1,"PcResistDominate()")
        else:
            if(clan == 13):
	        __main__.ScheduleTask(0.1,"GargoyleDominate()")
            else:
	        __main__.ScheduleTask(0.1,"BrunoCastDominate1()")

def BrunoCastDominate1():
    Find("sound1_dominate").PlaySound()
    Find("sound2_dominate").PlaySound()
    __main__.ScheduleTask(0.1,"BrunoCastDominate2()")

def BrunoCastDominate2():
    Find("pc_fall_sleep").BeginSequence()
    __main__.ScheduleTask(2.1,"BrunoCastDominate3()")

def BrunoCastDominate3():
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
    #__main__.FindPlayer().ClearActiveDisciplines()
    __main__.ScheduleTask(1.05,"PcResistDominate1()")

def PcResistDominate1():
    Find("pc_dominate").RemoveControllerNPC()

#-----------------------------------------------------------------------
print "... Levelscript Loaded"
