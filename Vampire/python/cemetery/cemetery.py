print "loading cemetery level script..."

import __main__

from __main__ import G

c = __main__.ccmd

Find = __main__.FindEntityByName
Finds = __main__.FindEntitiesByName

#-------------------------------------------------------------------------
# Used by Antitribu Mod
# Triggers the End of the Quest
def NecromancerMinionCheck():
    G.NecroMinion_Death = G.NecroMinion_Death + 1
    
    if(G.NecroMinion_Death == 5):
       __main__.ScheduleTask(3.00,'c.fadeout()')
       __main__.ScheduleTask(5.05,'Find("Necro_quest_end_relay").Trigger()')
       __main__.ScheduleTask(6.00,'Find("Necro_quest_end_relay2").Trigger()')
       __main__.ScheduleTask(6.00,'c.fadein()')

def NecromancerSetQuest():
     __main__.FindPlayer().SetQuest("Necromancer",2)
     G.Necromancer_Quest_Finished = 1

    
#    elif (G.Necromancer_Quest == 1 & G.FinishedCemetery == 0):
#         print ( "===  Necromancer not present  ===" )
#    elif (G.Necromancer_Quest == 0 & G.FinishedCemetery == 1):
#         print ( "===  Necromancer not present  ===" )
#    elif (G.Necromancer_Quest == 0 & G.FinishedCemetery == 0):
#         print ( "===  Necromancer not present  ===" )
#    else:
#         print ( "===  Necromancer has been defeated  ===" )

def NecromancerCheck():
    if (G.Necromancer_battle_start == 1):
        return
    else:
        Find("Necromancer_appear").Trigger()

def SkKnightTurn():      
       Find("sk_knight_timer").Show()
       Find("sk_knight_timer").RestartTimer()
       Find("minion_3").MakeInvincible(1)
       Find("minion_3").SetBossMonster(0)
       Find("sk_3").ScriptHide()
       Find("sk_knight_transform").BeginSequence()
       Find("minion_3").PlayDialogFile("disciplines/necromancy/level1/Activate1.wav")
       Find("minion_3").SetModel("models/weapons/disciplines/Necromancy/lvl5/ghost_female.mdl")

def SkKnightDead():      
       Find("minion_3").Kill()
       Find("sk_3").Kill()
       Find("barmitza3").Kill()
       Find("chainmail3").Kill()
       Find("gardbrace3").Kill()
       Find("hammer3").Kill()
       Find("Dead_relay").Trigger()
       __main__.ScheduleTask(3.00,'c.fadeout()')
       __main__.ScheduleTask(5.05,'Find("Necro_quest_end_relay").Trigger()')
       __main__.ScheduleTask(6.00,'Find("Necro_quest_end_relay2").Trigger()')
       __main__.ScheduleTask(6.00,'c.fadein()')

#-------------------------------------------------------------------------
#CEMETERY: removes all zombies and disables spawners
def destroyAllZombies():
    print ( "***********  All Zombies removed and disabled   ***********" )
    relay = Find( "Relay_Waves_End" )
    relay.Trigger()
    zombies = Finds( "zombie" )
    for zombie in zombies:
        zombie.Kill()

#CEMETERY:  Setup cemetery quest on map Load, changed by wesp
def checkCemeteryQuest():
    print ( "************** Running Check CemeteryQuest *****************" )
    destroyAllZombies()
    pc = __main__.FindPlayer()
    state = pc.GetQuestState("Romero")
    if G.Romero_Whore == 3:
        prostsound = Find( "Sound_Fun" )
        if prostsound: prostsound.Kill()

    if (state > 1):
        print ( "***********  General Setup For Map Post Romero Quest *************" )
        relaygates = Find("Relay_Gates_Post_Quest")
        if (G.Patch_Plus == 0):
            romero = Find( "romero" )
            if romero: romero.Kill()
        else:
            sequence = Find("romero_seq1")
            if sequence:
                print ("Found Couch After Sequence")
                sequence.BeginSequence()
    if (state < 2):
        print ( "***********  Map in Default State *************" )
        if G.Romero_Whore < 1:
            ammoRefill()
        sequence = Find("romero_seq1")
        if sequence:
            print ("Found Couch Sequence")
            sequence.BeginSequence()
        relay = Find("Relay_Prostitute_Gone")
        if relay:
            print ("Open Doors")
            relay.Trigger()


#CEMETERY:  Checks on entering Romero Shack
def runRomeroSeq():
    if ( G.CemeteryBoched == 1 ):
        romeroseq1 = Find("romero_seq1")
        romeroseq1.CancelSequence()
        return
    pc = __main__.FindPlayer()
    state = pc.GetQuestState("Romero")
    if (((state < 1) and (G.Romero_Offer == 0)) or (G.Romero_Whore == 2)):
        print ( "***********  Romoro Init Dialogue *************" )
        control = Find ("Player_control")
        control.CreateControllerNPC()
        playerseq = Find("player_control_seq")
        playerseq.BeginSequence()
        romeroseq1 = Find("romero_seq1")
        romeroseq1.CancelSequence()
        romeroseq2 = Find("romero_seq_stand")
        romeroseq2.BeginSequence()

#CEMETERY:  fade the player back to HW after failing zombies.
def leaveCemetery():
    __main__.ChangeMap(2.5, "hollywood", "cem_hollywood")

#CEMETERY:  End of Romero dlg set up, changed by wesp
def setCemQuest():
    print ("running setCemQuest")
    pc = __main__.FindPlayer()
    state = pc.GetQuestState("Romero")
    stateho = pc.GetQuestState("Loser")
    if (G.Romero_Hate == 1):
        print ( "Romero Hates You")
        romero = Find("Romero")
        if romero: romero.SetRelationship("player D_HT 5")
        return
    if (stateho == 5):
        print ( "Delivered the Goods" )
        if G.Romero_Couch == 0:
            prostitute = Find( "ProstituteCem" )
            if prostitute: prostitute.Kill()
            relay = Find( "Relay_Prostitute_Event" )
            relay.Trigger()
            G.Romero_Couch = 1
    if (state == 3):
        if (G.FinishedCemetery == 0):
            print ( "Boched Reaction")
            G.FinishedCemetery = 1
            bochedlevel = Find("Relay_Zombie_Kill_Sequence")
            bochedlevel.Trigger()
        else:
            print ( "Just exit dialogue" )
    elif (state == 2):
        if (G.FinishedCemetery == 0):
            print ( "Success Teleport back to HW")
            G.FinishedCemetery = 1
            __main__.ScheduleTask( 7.5, "leaveCemetery()" )
        else:
            print ( "Just exit dialogue" )
    elif (state == 1):
        print ( "Been given the quest")
        eventStart = Find("quest_accepted")
        eventStart.Trigger()
    elif (state == 0):
        print ( "Denied to do the quest")
        romeroseq1 = Find("romero_seq1")
        romeroseq1.BeginSequence()
    if(G.Romero_Boink == 1):
        relay = Find("romero_boink_relay")
        relay.Trigger()
        G.Romero_Boink = 2

#CEMETERY:  trigger Romero sequence if you fail.
def failureCheck():
    failureRelay = Find("Relay_Zombie_Kill_Sequence")
    failureRelay.Trigger()

#CEMETERY:  Botch Remote
def checkBotch():
    print ( "*********** Is PC chickening out on Romero ***********" )
    pc = __main__.FindPlayer()
    state = pc.GetQuestState("Romero")
    if (state == 1):
        botch = Find("Relay_Chicken_Botch")
        botch.Trigger()

#CEMETERY:  Fill Romero's container, changed by wesp
def ammoRefill():
    player = __main__.FindPlayer()
    container = __main__.Find("romero_container")
    if (container and G.Got_Ammo == 0):
        G.Got_Ammo = 1
        if ( player.HasItem("item_w_thirtyeight") ):
            container.SpawnItemInContainer("item_w_thirtyeight")
            container.SpawnItemInContainer("item_w_thirtyeight")
        if ( player.HasItem("item_w_glock_17c") ):
            container.SpawnItemInContainer("item_w_glock_17c")
            container.SpawnItemInContainer("item_w_glock_17c")
        if ( player.HasItem("item_w_ithaca_m_37") ):
            container.SpawnItemInContainer("item_w_ithaca_m_37")
            container.SpawnItemInContainer("item_w_ithaca_m_37")

#Masqurade Violation: Triggered when gates break
def masquradeViolation():
    pc = __main__.FindPlayer()
    pc.ChangeMasqueradeLevel( 1 )

#CEMETERY: puts tape in Ginger Swan's crypt
def SetGingerSwanTape():
    if __main__.FindPlayer().GetQuestState("Courier") == 4:
        door = Find("swan_door_container")
        door.ScriptUnhide()
        node = Find("swan_inspect")
        node.ScriptUnhide()
        G.Ginger_Swan = 2

#CEMETERY: set quest on tape retrieval
def SetGingerSwanTapeQuestState():
    pc = __main__.FindPlayer()
    state = pc.GetQuestState("Courier")
    if (state > 2 and state < 5):
        pc.SetQuest("Courier", 5)

## CEMETERY: Romero Prostitute disband follower, fade and teleport (from romero dlg)
def endRomero():
    print ( "*************** Cleaning up Loser Quest ***************" )

## CEMETERY:
def startProstituteDlg():
    prostitute = Find("ProstituteCem")
    if prostitute: prostitute.StartPlayerDialog(0)

## CEMETERY: Prostitute inits dialogue in cemetery (on trigger in cemetery), changed by wesp
def prostituteInitCemetery():
    prostitute = Find("ProstituteCem")
    print ( "**************** Looking for Romero Prostitute ********************" )
    if ( prostitute and G.Whore_Follower == 1 and G.In_Cemetery == 0 and G.Romero_Whore == 2 ):
        print ( "************** Have Prostitute for Romero ********************" )
        G.In_Cemetery = 1
        if ( G.Blondie == 1 ):
            prostitute.SetModel( "models/character/npc/common/prostitute/prostitute_1/prostitute_1.mdl" )
            print ( "************** Is Blondie ********************" )
        print ( "***************** Unhide Prostitute ******************" )
        prostitute.ScriptUnhide()
        sequence = Find( "Seq_SetupProstitute" )
        sequence.BeginSequence()
        prostitute.SetFollowerBoss( "!Player" )
        trigger = Find( "Trigger_Pimp" )
        if trigger: trigger.Kill()
        if (G.Whore_Orphans == 1):
            print ( "*************** Whore_Orphans == 1, Should Talk ****************" )
            __main__.ScheduleTask( 2.0, "startProstituteDlg()" )
    else:
        print ( "**************** No Prostitute ********************" )
        if prostitute: prostitute.ScriptHide()

## CEMETERY: Fail Loser Quest when Romero dies, changed by wesp
def failLoser():
    pc = __main__.FindPlayer()
    state = pc.GetQuestState("Loser")
    if (state > 1):
       pc.SetQuest("Loser", 4)
    if(pc.humanity >= 3):
        pc.HumanityAdd( -1 )

def cemeteryFail():
    pc = __main__.FindPlayer()
    pc.SetQuest("Romero", 3)


print "...cemetery levelscript loaded"