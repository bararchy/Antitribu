print "loading downtown level script"

import __main__
import consoleutil

from __main__ import G

__main__.Level = __name__

Find = __main__.FindEntityByName
FindList = __main__.FindEntitiesByName
FindClass = __main__.FindEntitiesByClass

import random
random.seed()

#ABANDONED BUILDING: Called to enable the murder scene in the abandoned building, changed by wesp
def abandonedBuildingMurder():
    pc = __main__.FindPlayer()
    state = pc.GetQuestState("Muddy")
    if(state == 2):
        relay = Find("murder_scene_unhider")
        relay.Trigger()
        if ( pc.CalcFeat("inspection") > 3 ):
            sparklies = __main__.CreateEntityNoSpawn("inspection_node", 0, (0, 0, 0))
            sparklies.SetParent("stereo")
            __main__.CallEntitySpawn(sparklies)

#ABANDONED BUILDING: called when the player spots the corpse
def headlessCorpseSpotted():
    pc = __main__.FindPlayer()
    state = pc.GetQuestState("Serial")
    if(state == 0):
        pc.SetQuest("Serial", 4)
    elif(state == 1 or state == 2):
        pc.SetQuest("Serial", 5)

#ABANDONED BUILDING: called when the player gets the key
def luckyStarKeyPickup():
    __main__.FindPlayer().SetQuest("Muddy", 3)
    G.Killer_Key = 1

#ABANDONED BUILDING: Called to determine results of talking with the bum
def bumDialog():
    if(G.Bum_Leave == 1):
        script = Find("bum_flee_relay")
        script.Trigger()

#CHANTRY: called on chantry exit
def leaveChantry():
    if(G.Story_State < 100):
        __main__.ChangeMap(2.5, "chantry", "chantry_interior_trigger")
    else:
        __main__.ChangeMap(2.5, "caine_landmark", "chantry_caine_trigger")

#CHANTRY: Called on the regent's dialogue
def regentDialog():
    if(G.Regent_Family == 3):
        door = Find("chantryhavendr")
        door.Unlock()
        mailbox = Find("mailbox_haven_locked")
        mailbox.ScriptHide()
        mailbox = Find("mailbox_haven")
        mailbox.ScriptUnhide()

#CONFESSION:  Makes the cages move
#Commented out, no longer used - RobinHood70
#def ConfessionCages():
#    nNumCages = 12
#    from random import Random
#    from time import time
#    R = Random( time() )
#    for n in range(1, nNumCages+1):
#        E = Find("cagedancer_%d"%n)
#        if(G.Confession_Crime == 0):
#            E.SetAnimation("dance0%d" % R.randint(1,3))
#        else:
#            cowerNumber = R.randint(1,3)
#            if(cowerNumber == 1):
#                E.SetAnimation("cower_idle")
#            else:
#                E.SetAnimation("cower%d_idle" % cowerNumber)
#        #COMMENTED OUT BECAUSE THE DANCERS DON'T ANIMATE RIGHT IF THE CAGES SWING
#        #E = Find("cageimpact_%d"%n)
#        #fScale = 0.5 + R.random()
#        #E.scale(fScale)    #WHY DOES THIS CRASH?
#        #E.Activate()

#CONFESSION: Called if Patty dies, changed by wesp
def pattyDeath():
    pc = __main__.FindPlayer()
    state = pc.GetQuestState("Junky")
    if state == 1 or state == 7:
        pc.SetQuest("Junky", 2)
    elif state == 5:
        pc.SetQuest("Junky", 6)
    state = pc.GetQuestState("Danielle")
    if state == 4:
        pc.SetQuest("Danielle", 5)
        G.Vandal_Quest = 1
#        pc.ChangeMasqueradeLevel(-1)

#CONFESSION: Called upon talking to Patty, changed by wesp
def pattyDialog():
    patty = Find("Patty")
    if(G.Patty_Alley or G.Patty_SD or G.Patty_Pisha or G.Patty_SM):
        script = Find("patty_to_door")
        patty.WillTalk(0)
        script.BeginSequence()
    if(G.Patty_Pissed):
        patty.WillTalk(0)

#CONFESSION: Called to determine if Patty is still there or not, changed by wesp
def pattyGone():
    patty = Find("Patty")
    if patty:
        if(G.Patty_Alley or G.Patty_SD or G.Patty_Pisha or G.Patty_SM or __main__.IsDead("Patty")):
            patty.Kill()
        if(G.Skelter_Quest == 3):
            patty.WillTalk(1)
    venus = Find("Venus")   
    if(__main__.IsDead("Venus")):
        if venus: venus.Kill()
        goon = Find("Goon")
        if goon: goon.ScriptUnhide()

#CONFESSION: Called if venus is killed
def venusDeath():
    pc = __main__.FindPlayer()
    state = pc.GetQuestState("Confession")
    if(state > 0 and state < 5):
        pc.SetQuest("Confession", 6)
    state = pc.GetQuestState("Venus")
    if(state > 0 and state != 4):
        pc.SetQuest("Venus", 5)
    state = pc.GetQuestState("Kill Venus")
    if(state == 1):
        pc.SetQuest("Kill Venus", 2)

#CONFESSION: Called after talking to Venus
def venusDialog():
    if(G.Venus_Office and G.Venus_In_Office == 0):
        G.Venus_In_Office = 1
        camera = Find("venus_camera")
        camera.StartShot()
        script = Find("venus_to_office")
        script.BeginSequence()
        trigger = Find("venus_fade_trigger")
        trigger.Enable()

#CONFESSION: Called to teleport venus back down to the bar
def venusToBar():
    G.Venus_In_Office = 0
    if(G.Venus_Office):
        teleport = Find("venus_to_bar")
        teleport.Teleport()
        G.Venus_Office = 0

#DOWNTOWN: called if the player feeds on a diseased bum
def fedOnPlagueBum():
    pc = __main__.FindPlayer()
    state = pc.GetQuestState("Plague")
    if(state == 0):
        pc.SetQuest("Plague", 15)

#DOWNTOWN: set gangs to hate each other, changed by RobinHood70
def SetGangs():
    sharks = ["shark_1", "shark_2", "shark_3"]
    jets = ["jet_1", "jet_2", "jet_3", "jet_4"]

    for i in range(0, len(sharks)):
        shark = Find(sharks[i])
        if shark:
            for j in range(0, len(jets)):
                jet = Find(jets[j])
                if jet:
                    shark.SetRelationship("%s D_HT 10" %jets[j])

    for j in range(0, len(jets)):
        jet = Find(jets[j])
        if jet:
            for i in range(0, len(sharks)):
                shark = Find(sharks[i])
                if shark:
                    jet.SetRelationship("%s D_HT 10" %sharks[i])

#DOWNTOWN: set bum name for VO
def SetBumName(name):
    G.Bum_Name = name
    bum = Find(name)
    if bum: bum.SetName("Bum_disease_male")
    return 0

#DOWNTOWN: revert bum name for non-VO
def ResetBumName():
    bum = Find("Bum_disease_male")
    if bum: bum.SetName(G.Bum_Name)

#DOWNTOWN: set bums to stop talking if one has talked
def SetBumsNotTalk():
    if(G.TinCanBill_Know == 1 or G.TinCanBill_Nos == 1):
        bums = FindList("Bum_disease_male_*") + FindList("Bum_disease_female")
        for bum in bums:
            bum.WillTalk(0)

#DOWNTOWN: set bums to talk if quest set
def SetBumsTalk():
##    print "SetBumsTalk()"
    if(G.Damsel_Quest > 0):
        bTalk = 1
    else:
        bTalk = 0
    bums = FindList("Bum_disease_mal*")
    n = 1
##    print 'renaming'
    for bum in bums:
##        print bum.GetName()
        bum.SetName("Bum_disease_male_%d"%n)
        n = n+1
    bums = FindList("Bum_disease_male_*") + FindList("Bum_disease_female")
##    print 'will talking'
    for bum in bums:
##        print bum.GetName()
        bum.WillTalk(bTalk)

    SetBumsNotTalk()

#DOWNTOWN: unhide Tin Can Bill
def SetTinCanBill():
    if(G.TinCanBill_Heard == 1 or G.TinCanBill_Know == 1 or G.TinCanBill_Nos == 1):
        bill = Find("Tin_Can_Bill")
        if bill: bill.ScriptUnhide()

        trigs = FindList("trig_tincanbill")
        for trig in trigs:
            trig.Kill()

        truck = Find("truckblock")
        if truck: truck.Kill()
        clip = Find("truckclip")
        if clip: clip.Kill()

#DOWNTOWN: end bill's dialog
def BillDialogEnd():
    if(G.Bill_Dead == 1):
        bill = Find("Tin_Can_Bill")
        bill.TakeDamage(100)

#DOWNTOWN: unhide Igor
def SetIgor():
    igor = Find("Igor")
    buddy1 = Find("igor_buddy_1")
    buddy2 = Find("igor_buddy_2")
    if(G.Venus_Quest == 1):
        if igor: igor.ScriptUnhide()
        if buddy1: buddy1.ScriptUnhide()
        if buddy2: buddy2.ScriptUnhide()
        guard = Find("parking_guard")
        if guard: guard.ScriptHide()
    elif(__main__.FindPlayer().GetQuestState("Confession") == 5):
        if igor: igor.Kill()
        if buddy1: buddy1.Kill()
        if buddy2: buddy2.Kill()

#DOWNTOWN: set igorbuddy to hate if igor hates
def IgorEndDialog():
    if (G.Igor_Dominated != 1 and G.Igor_Dementated != 1):
        ## hope dialog doesn't change and assume igor then hates player.
        logic = Find("logic_IgorHate")
        if logic: logic.Trigger()
    elif G.Igor_Dementated:
        logic = Find("logic_IgorDementate")
        if logic: logic.Trigger()
        logic = Find("logic_IgorHate")
        if logic: logic.Kill()
        igor = Find("Igor")
        if igor: igor.WillTalk(0)

#DOWNTOWN: fail traffik on larry's death
def larryDeath():
    player = __main__.FindPlayer()
    if player.GetQuestState("Traffik") in [1, 2]:
        player.SetQuest("Traffik", 4)

#DOWNTOWN: called when talking to Patty in the alley
def pattyAlleyDialog():
    if(G.Patty_Alley == 3):
        patty = Find("Patty")
        if patty: patty.WillTalk(0)

#DOWNTOWN: set Patty in alley by Confession, changed by wesp, RobinHood70
def SetPatty():
    patty = Find("Patty")
    if patty:
        if __main__.IsDead("Patty"):
            patty.Kill()
        else:
            if (G.Patty_Alley == 1):
                patty.ScriptUnhide()
                patty.WillTalk(0)
##        trig = Find("trig_patty_alley")
##        trig.Enable()

#DOWNTOWN: set Heather in front of Ventrue
def SetHeather():
    heather = Find("Heather")
    if heather:
        if(G.Heather_Drank == 1 and G.Story_State == 15 and G.Heather_Haven == 0):
            heather.ScriptUnhide()
            trig = Find("trig_heather")
            if trig: trig.Enable()
        elif(G.Heather_Haven == 1):
            # Changed for CompMod
            # if __main__.IsClan(__main__.FindPlayer(), "Nosferatu"):
            if(5 == __main__.G._pcinfo["clan"]):
                heather.WillTalk(1)
                teleport = Find("Heather_teleport")
                teleport.Teleport()
            else:
                heather.Kill()
        elif(G.Story_State > 15):
            heather.Kill()
        else:
            heather.ScriptHide()

#DOWNTOWN: set MingXiao in front of Bradbury
def SetMingXiao():
    __main__.FindPlayer().ClearActiveDisciplines()
    npc = Find("MingXiao2")
    npc.ScriptUnhide()

#DOWNTOWN: set Beckett on the way to the Last Round
def SetBeckettTalk():
    if(G.Story_State == 85):
        trig = Find("trig_beckett_talk")
        if trig: trig.ScriptUnhide()

#DOWNTOWN: set stop sign
def SetStopSign():
    trig = Find("trig_stop_sign")
    if __main__.IsClan(__main__.FindPlayer(), "Malkavian"):
        if trig: trig.Enable()
    else:
        sign = Find("Stop")
        if sign: sign.Kill()
        if trig: trig.Kill()

#DOWNTOWN: remove CDC guys after completion of quest, changed by wesp
def UnsetCDC():
    if(G.Damsel_Quest > 2 or G.Regent_QuestPestilence > 3):
        logic = Find("kill_cdc")
        if logic: logic.Trigger()

#DOWNTOWN: remove cab if player is nosferatu, changed by wesp
## and enable sewer travel if nosferatu
def UnsetCabbie():
    # Changed for CompMod
    # if __main__.IsClan(__main__.FindPlayer(), "Nosferatu"):
    if(5 == __main__.G._pcinfo["clan"]):
        logic = Find("logic_cab_kill")
        if logic: logic.Trigger()
        grate = Find("ventrue_sewer_grate")
        if grate: grate.Kill()
        grate = Find("nos_ventrue_sewer_grate")
        if grate: grate.ScriptUnhide()
        map = Find("sewer_map")
        if map: map.Unlock()
        map = Find("sewer_map_2")
        if map: map.Unlock()

#DOWNTOWN: Set ventrue tower debris, changed by wesp
def SetVentrueExplosion():
    if (G.Story_State >= 70 and G.Clean_Rubble == 0):
        logic = Find("logic_ventrue_explosion")
        if logic: logic.Trigger()
    elif (G.Story_State >= 70 and G.Clean_Rubble == 1):
        logic = Find("logic_ventrue_cleanup")
        if logic: logic.Trigger()

#DOWNTOWN: hide/unhide npcs
def SetNPCs():
    SetTinCanBill()
    SetIgor()
    SetPatty()
    SetHeather()
    SetGangs()
    SetBumsTalk()
    SetBeckettTalk()
    SetStopSign()
    UnsetCDC()
    UnsetCabbie()
    SetNinesCutscene()
    SetVentrueExplosion()
    SetRat()

#Appears to be useless, as "rat" model doesn't exist, but wondering if this is from the ratmaker, so left it in - RobinHood70
#DOWNTOWN:  kill the rat!!!!!
def SetRat():
    rat = Find("rat")
    if rat: rat.Kill()

#DOWNTOWN: set bradbury accessibility
def SetBradbury():
    washer = Find("bradwndwwshr")
    if washer:
        if(G.Story_State < 75 or G.Story_State >= 80):
            washer.SetPosition(1.0)
        else:
            washer.SetPosition(0.0)

#DOWNTOWN: set parking garage accessibility
def SetParkingGarage():
    gate = Find("garagegate_closed")
    if gate:
        state = __main__.FindPlayer().GetQuestState("Traffik")
        if(G.Larry_Quest == 1 and state < 3):
            gate.ScriptHide()
        else:
            gate.ScriptUnhide()

#DOWNTOWN: go to ventrue tower combat map
def SetVentrueTransition():
    ## 110 = siding with prince
    if(G.Story_State in [100, 115, 120, 125]):
        oneBs = FindList("trigger_ventrue_combat") + FindList("trig_LA_to_1b")
        ones = FindList("VentrueTower_interior_trigger") + FindList("trig_LA_to_1")
        for one in ones:
            one.Kill()
        for oneB in oneBs:
            oneB.ScriptUnhide()

#DOWNTOWN: open/close Tremere chantry
def SetChantryDoors():
    if (G.Regent_Pissed == 3 or G.Isaac_Please == 1):
        knobs = FindList("chantryknob")
        for knob in knobs:
            knob.Lock()
    else:
        knobs = FindList("chantryknob")
        for knob in knobs:
            knob.Unlock()

#DOWNTOWN: lock/unlock doors
def SetDoors():
    SetBradbury()
    SetParkingGarage()
    SetVentrueTransition()
    SetChantryDoors()

#DOWNTOWN: change ming xiao to nines.
def ChangeMingXiaoToNines():
##    mx = Find("MingXiao2")
##    if mx: mx.TransformModel()
    fade = Find("fade_white")
    fade.Fade()
    __main__.ScheduleTask(0.75, "__main__.FindEntityByName(\"MingXiao2\").SetModel(\"models/character/npc/unique/Downtown/Nines/Nines.mdl\")")

#DOWNTOWN: change nines to mingxiao.
def ChangeNinesToMingXiao():
    fade = Find("fade_white")
    fade.Fade()
    __main__.ScheduleTask(0.75, "__main__.FindEntityByName(\"MingXiao2\").SetModel(\"models/character/npc/unique/Chinatown/Ming_Xiao/MingXiao.mdl\")")

#DOWNTOWN: set quest state on Igor's death
def igorDeath():
    pc = __main__.FindPlayer()
    state = pc.GetQuestState("Confession")
    if(state > 0 and state < 4 and state != 3):
        pc.SetQuest("Confession", 4)

#DOWNTOWN: set state on Nines cutscene
def OnNinesCutscene():
    if(G.Story_State == 5):
        G.Story_State = 10
    pc = __main__.FindPlayer()
    state = pc.GetQuestState("Morphine")
    if(state == 1 or state == 2):
        pc.SetQuest("Morphine", 4)

    G.Ninesintro_Open = 0
    G.Downtown_Open = 1

#DOWNTOWN / SEWER: show cutscene only if story state is 5.
def SetNinesCutscene():
    if(G.Story_State == 5):
        trigs = FindList("trig_nines_cutscene")
        for trig in trigs:
            trig.Enable()

#DOWNTOWN: random sound effect (dogs/cats fight)
def Alley1():
    if not random.randrange(3):
        a = Find("logic_alley1")
        if a: a.Trigger()

#DOWNTOWN: random sound effect (parking garage)
def Alley2():
    if not random.randrange(4):
        a = Find("logic_alley2")
        if a: a.Trigger()

#EMPIRE: Boris calls this when he dies
def borisDeath():
    pc = __main__.FindPlayer()
    state = pc.GetQuestState("Venus")
    if(not __main__.IsDead("Venus") and state > 0 and state != 6):
        pc.SetQuest("Venus", 3)
    state = pc.GetQuestState("Kill Venus")
    if(state > 0 and state != 3):
        pc.SetQuest("Kill Venus", 4)

#EMPIRE: Called afer dialog with Boris, changed by wesp
def borisDialog():
    dema = Find("Dema")
    if dema: dema.WillTalk(0)
    if(G.Dema_Leave == 1):
        #NEED DIALOG CHANGE TO MAKE THIS COOLER
        if dema: dema.ScriptHide()
    if(G.Boris_Hostile == 1):
        __main__.ScheduleTask(10.0, "__main__.FindEntityByName(\"Dema\").SetRelationship(\"player D_HT 5\")")
    elif(G.Boris_Hostile == 2):
        __main__.ScheduleTask(0.5, "__main__.FindEntityByName(\"Dema\").SetRelationship(\"player D_HT 5\")")
    elif(G.Boris_Dementated):
        boris = Find("Boris")
        boris.SetRelationship("Dema D_HT 5")
        __main__.ScheduleTask(10.0, "__main__.FindEntityByName(\"Dema\").SetRelationship(\"Boris D_HT 5\")")

#EMPIRE: Called when opening Boris' office door to see if anyone gets mad, changed by wesp
def borisDoorOpen():
    if(not __main__.IsDead("Dema") and (G.Dema_Go != 1) and (G.Dema_Dominated != 1) and (G.Dema_Dementated != 1)):
        dema = Find("Dema")
        dema.SetRelationship("player D_HT 5")
        boris = Find("Boris")
        boris.SetRelationship("player D_HT 5")
    if(__main__.IsDead("Dema") and (G.Boris_Talk == 0) and (G.Boris_Hostile == 0)):
        pc = Find("dema_controller")
        pc.CreateControllerNPC()
        script = Find("player_to_boris")
        script.BeginSequence()

#EMPIRE: Called to check if the player is on the jezebel quest, changed by wesp
def cardPrinterEnable():
    if(G.Hannah_Jezebel == 1 and G.Patch_Plus == 0):
        printer = Find("card_printer")
        printer.ScriptUnhide()
    if(G.Patch_Plus == 1):
        printernote = Find("printernote")
        printernote.ScriptUnhide()

#EMPIRE: Called to check if the player is on the jezebel quest, added by wesp
def cardPrinterEnablePlus():
    if(G.Hannah_Jezebel == 1 and G.Patch_Plus == 1):
        printer = Find("card_printer")
        printer.ScriptUnhide()

#EMPIRE:  Called to check if the player is on the mafia quest, changed by wesp
def checkMafiaState():
    if(G.Venus_Quest == 3 and not G.Russians_Here):
        G.Russians_Here = 1
        door1 = Find("Door_F5")
        door1.Unlock()
        door2 = Find("Door_F6")
        door2.Unlock()
        dude = Find("patrol_guy")
        dude.ScriptUnhide()
        dude = Find("random_guard_a")
        dude.ScriptUnhide()
        dudes = __main__.FindEntitiesByName("ballroom_guys*")
        for dude in dudes:
            dude.ScriptUnhide()
        dude = Find("computer_guy")
        dude.ScriptUnhide()
        dude = Find("tv_guy")
        dude.ScriptUnhide()
        dude = Find("Boris")
        dude.ScriptUnhide()
        dude = Find("Dema")
        dude.ScriptUnhide()
    if(G.Boris_Hostile or G.Dema_Hostile or G.Dema_Go == 2):
        dude = Find("patrol_guy")
        if dude: dude.SetRelationship("player D_HT 5")
        dude = Find("random_guard_a")
        if dude: dude.SetRelationship("player D_HT 5")
        dudes = __main__.FindEntitiesByName("ballroom_guys*")
        for dude in dudes:
            dude.SetRelationship("player D_HT 5")
        dude = Find("computer_guy")
        if dude: dude.SetRelationship("player D_HT 5")
        dude = Find("tv_guy")
        if dude: dude.SetRelationship("player D_HT 5")

#EMPIRE: Called upon talking to Dema, Boris' guard
def demaDialog():
    if(G.Dema_Go == 1):
        script = Find("dema_escort_player")
        script.BeginSequence()
        pc = Find("dema_controller")
        pc.CreateControllerNPC()
        script = Find("player_move")
        script.BeginSequence()
    elif(G.Dema_Go == 2):
        __main__.ScheduleTask(10.0, "__main__.FindEntityByName(\"Dema\").SetRelationship(\"player D_HT 5\")")
    elif(G.Dema_Dominated == 1 or G.Dema_Dementated == 1):
        script = Find("dema_dominated")
        script.BeginSequence()
    elif(G.Dema_Hostile):
        boris = Find("Boris")
        if boris: boris.SetRelationship("player D_HT 5")
    if(G.Dema_Go == 2 or G.Dema_Hostile):
        dema = Find("Dema")
        dema.WillTalk(0)

#EMPIRE: called when Jezebel Dies, changed by wesp
def jezebelDeath():
    G.Jezebel_Dead = 1
    pc = __main__.FindPlayer()

    if pc.GetQuestState("Regent") > 0 and pc.GetQuestState("Regent") < 4:
        pc.SetQuest("Regent", 3)

    # first person redeems masquerade, second person drops flyer
    if G.Kanker_Dead:
        flyer = Find("flyer")
        sparklies = Find("flyer_sparklies")
        if flyer: flyer.ScriptUnhide()
        if sparklies: sparklies.ScriptUnhide()
    else:
        pc.ChangeMasqueradeLevel(-1)

    allPlagueState = pc.GetQuestState("AllPlague")
    if pc.GetQuestState("Plague") > 0 and pc.GetQuestState("Plague") != 10 and pc.GetQuestState("Plague") != 9:
        if G.Kanker_Dead:
            pc.SetQuest("Plague", 11)
        else:
            pc.SetQuest("Plague", 13)
    elif allPlagueState != 0 and allPlagueState != 5:
        pc.SetQuest("AllPlague", 13)

#EMPIRE: on brotherhood flyer pickup
# see OnFlyerPickup under plaguesewer

#EMPIRE: called when the player gets Jezebel's key
def jezebelKeyPickup():
    __main__.FindPlayer().AwardExperience("Plague02")

#EXHAUST PIPE:  Called as the player approaches Skelter/Damsel
def approachSkelter():
    skelter = Find("Skelter")
    if(G.Story_State < 20 and G.Skelter_Know == 0):
        skelter.StartPlayerDialog(0)

#EXHAUST PIPE:  Called to determine if any of the various Anarchs are missing from the bar
def populateBar():
    if(G.Story_State >= 20 and G.Story_State <= 90):
        nines = Find("Nines")
        nines.ScriptHide()
    if(G.Story_State >= 80):
        jack = Find("Jack")
        jack.ScriptUnhide()

#HOSPITAL:  Called when the player picks up Milligan's business card, changed by wesp
def milliganCardPickup():
    pc = __main__.FindPlayer()
    state = pc.GetQuestState("Necromantic")
    if(not __main__.IsDead("Milligan") and not __main__.IsDead("Pisha") and state < 2):
        pc.SetQuest("Necromantic", 2)

#HOSPITAL: Called when Milligan dies, added by wesp
def bumDeath():
    pc = __main__.FindPlayer()
    if(pc.humanity >= 3):
        pc.HumanityAdd( -1 )

#HOSPITAL: Called to unhide the business card, added by wesp
def milliganCard():
    world = Find("world")
    world.SetSafeArea(2)
    if(not __main__.IsDead("Milligan")):
        card = Find("card")
        if card: card.ScriptUnhide()
        sparklies = Find("card_sparklies")
        if sparklies: sparklies.ScriptUnhide()

#HOSPITAL: Called to determine if Milligan is scared
def milliganDialog():
    script = Find("milligan_cower")
    if script: script.BeginSequence()
    #milligan = Find("Milligan")
    #milligan.SetDisposition("Fear", 3)

#HOSPITAL: enacts the effects of talking to Pisha
def pishaDialog():
    world = Find("world")
    world.SetSafeArea(0)
    if(G.Pisha_Attack):
        trigger = Find("pisha_fight_relay")
        trigger.Trigger()

#HOSPITAL: called when Pisha Dies
def pishaDeath():
    pc = __main__.FindPlayer()
    state = pc.GetQuestState("Occult")
    if state > 0 and state < 5:
        pc.SetQuest("Occult", 6)
    state = pc.GetQuestState("Necromantic")
    if (state > 0 and state < 4):
        pc.SetQuest("Necromantic", 5)

#HOSPITAL: called when Pisha leaves, added by wesp
def pishaGone():
    if(G.Story_State >= 85):
        pisha = Find("Pisha")
        if pisha: pisha.Kill()
        book = Find("book")
        if book: book.Kill()
        candle = Find("candle")
        if candle: candle.Kill()
        light = Find("light")
        if light: light.Kill()
        fire = Find("fire")
        if fire: fire.Kill()

#NINESINTRO: set nosferatu scene if nosferatu
def PlayNinesChoreo1():
    # Changed for CompMod
    # if __main__.IsClan(__main__.FindPlayer(), "Nosferatu"):
    if(5 == __main__.G._pcinfo["clan"]):
        logic = Find("logic_start_nos_stuff")
        logic.Trigger()
    else:
        logic = Find("logic_start_nonnos_stuff")
        logic.Trigger()

#NINESINTRO: play foot stomp sound
def PlayNinesintroStomp():
    if(__main__.FindPlayer().IsMale()):
        sound = Find("stomp_m")
        if sound: sound.PlaySound()
    else:
        sound = Find("stomp_f")
        if sound: sound.PlaySound()

#NINESINTRO: fade out at end
def OnNinesintroEnd():
    #__main__.ChangeMap(3.0, "nines_mark", "trig_to_LA")
    if(G.Nines_anger == 1):
        __main__.ChangeMap(3.0, "nines_mark", "trig_to_LA")
    else:
        __main__.ChangeMap(5.5, "nines_mark", "trig_to_LA")
        __main__.FindPlayer().AwardExperience("NinesHepl01")

#PARKINGGARAGE: called when the player gets the briefcase
def briefcasePickup():
    __main__.FindPlayer().SetQuest("Traffik", 2)
    if(G.ParkingGarageSpotted == 0):
        __main__.FindPlayer().AwardExperience("Traffik03")

#PARKING GARAGE
def survivorsFlee():
    survivors = __main__.FindEntitiesByClass("npc_VHumanCombatant")
    for survivor in survivors:
        survivor.SetupPatrolType("0 2 FOLLOW_PATROL_PATH")
        survivor.FollowPatrolPath("flee")

#PLAGUE SEWER, changed by wesp
def kankerDeath():
    G.Kanker_Dead = 1
    pc = __main__.FindPlayer()

    if pc.GetQuestState("Regent") > 0 and pc.GetQuestState("Regent") < 4:
        pc.SetQuest("Regent", 3)

    # first person redeems masquerade, second person drops flyer
    if (G.Jezebel_Dead):
        flyer = Find("flyer")
        sparklies = Find("flyer_sparklies")
        if flyer: flyer.ScriptUnhide()
        if sparklies: sparklies.ScriptUnhide()
    else:
        pc.ChangeMasqueradeLevel(-1)
        ## allow player to leave
        brush = Find("switch_brush")
        if brush: brush.Kill()
        switch = Find("switch")
        switch.Unlock()

    allPlagueState = pc.GetQuestState("AllPlague")
    if pc.GetQuestState("Plague") > 0 and pc.GetQuestState("Plague") != 10 and pc.GetQuestState("Plague") != 9:
        if G.Jezebel_Dead:
            pc.SetQuest("Plague", 11)
        else:
            pc.SetQuest("Plague", 12)
    elif allPlagueState != 0 and allPlagueState != 5:
        pc.SetQuest("AllPlague", 13)

#PLAGUESEWER and EMPIRE:
def OnFlyerPickup():
    pc = __main__.FindPlayer()
    pc.AwardExperience("AllPlague01")
    allPlagueState = pc.GetQuestState("AllPlague")
    if allPlagueState == 0 and pc.GetQuestState("Plague") > 0:
        pc.SetQuest("Plague", 14)
    elif allPlagueState != 0 and allPlagueState != 5:
        pc.SetQuest("AllPlague", 12)

#SEWER: malks no longer get sewer map. ;_;
def malkSewer():
    npc = Find("CabbieSewer")
##    if(__main__.IsClan(__main__.FindPlayer(), "Malkavian") and not random.randrange(4)):
##        if npc: npc.ScriptUnhide()
##    else:
##        if npc: npc.ScriptHide()

#SEWER:  Gives the nos player his haven if he should have it, changed by wesp
def sewerHavenCheck():
    if(G.Story_State >= 10):
        door = Find("havendoor")
        door.Unlock()
        mailbox = Find("locked_haven_mailbox")
        mailbox.ScriptHide()
        mailbox = Find("mailbox_haven")
        mailbox.ScriptUnhide()

#SEWER: Called to see if the player needs to go to Caine
def sewerToCaine():
    if(G.Story_State >= 100):
        __main__.ChangeMap(2.5, "caine_landmark", "sewer_caine")

#SKYLINE: Called after talking to Hannah, changed by wesp
def hannahDialog():
    G.Hannah_Dead = 1
    hannah = Find("Hannah")
    hannah.WillTalk(0)
    hannah.SetDisposition("Dead", 1)
    hannah.TakeDamage(100)

#SKYLINE: called to see if the player took her journal
def hannahsBookPickup():
    if(G.Hannah_Jezebel < 1):
        pc = __main__.FindPlayer()
        #if(pc.HasItem("item_g_hannahs_appt_book") and not G.Hannah_Jezebel):
        G.Hannah_Jezebel = 1
        state = pc.GetQuestState("AllPlague")
        if(state == 0):
           pc.SetQuest("Plague", 4)
        else:
            pc.SetQuest("AllPlague", 9)

#SKYLINE: called when the player listens to hannah's message
def hannahMessageHeard():
#    __main__.FindPlayer().SetQuest("Plague", 3)
    pc = __main__.FindPlayer()
    state = pc.GetQuestState("AllPlague")
    if state != 0 and state != 5:
        pc.SetQuest("AllPlague", 8)
    else:
        pc.SetQuest("Plague", 3)

#SKYLINE: called when the player listens to the Killer's message
def killerMessageHeard():
    pc = __main__.FindPlayer()
    state = pc.GetQuestState("Muddy")
    if(state == 1):
        pc.SetQuest("Muddy", 2)

#SKYLINE: called when Milligan dies (might be called in #HOSPITAL too)
def milliganDeath():
    pc = __main__.FindPlayer()
    state = pc.GetQuestState("Necromantic")
    if(state == 1 or state == 2):
        pc.SetQuest("Necromantic", 3)
        pc.ChangeMasqueradeLevel(-1)

#SKYLINE: called after talking to milligan at the skyline, changed by wesp
def milliganSkylineDialog():
    if(G.Mill_Dementated or G.Mill_Loose or G.Mill_Persuaded or G.Mill_Dominated or G.Mill_Intimidate):
        relay = Find("Milligan_leaves_relay")
        relay.Trigger()

#SKYLINE: Populates the various skyline apartments if their residents are in
def residentCheck():
    #on plaguebearer quest
    if(G.Damsel_Quest and not G.Paul_Placed):
        G.Paul_Placed = 1
        hannah = Find("Hannah")
        if hannah: hannah.ScriptUnhide()
        key = Find("hannahs_safe_key")
        if key: key.ScriptUnhide()
        sparklies = Find("hannahs_key_sparklies")
        if sparklies: sparklies.ScriptUnhide()
        safe = Find("hannahs_safe")
        #safe.AddEntityToContainer("hannahs_book")
        safe.AddEntityToContainer("hannahs_cash")
        book = Find("hannahs_book")
        if book: book.ScriptUnhide()
        sparklies = Find("appointment_book_sparklies")
        if sparklies: sparklies.ScriptUnhide()
        paul = Find("paul")
        if paul: paul.ScriptUnhide()
        constraint = Find("paul_constraint")
        if constraint: constraint.Break()
        door = Find("paul_door")
        door.Unlock()
        answering_machine = Find("paul_answering_machine")
        if answering_machine: answering_machine.ScriptUnhide()
        sparklies = Find("paul_machine_sparklies")
        if sparklies: sparklies.ScriptUnhide()
    #serial killer victim #2, do we need this check here? changed by wesp
    if(G.SK_Downtown and not G.Killer_Message and G.Arthur_Muddy > 2):
        answering_machine = Find("victim_answering_machine")
        if answering_machine: answering_machine.ScriptUnhide()
        sparklies = Find("killer_machine_sparklies")
        if sparklies: sparklies.ScriptUnhide()
    #Milligan
    if(G.Milligan_Skyline and not G.Milligan_SA):
        G.Milligan_SA = 1
        milligan = Find("Milligan")
        if(milligan and not __main__.IsDead("Milligan")):
            milligan.ScriptUnhide()
            __main__.ScheduleTask(1.0, "__main__.FindEntityByName(\"milligan_scared\").BeginSequence()")
    #HANNAH and PAUL gone
    if(G.Hannah_Dead == 1):
        G.Hannah_Dead = 2
        paul = Find("paul")
        if paul: paul.Kill()
        hannah = Find("Hannah")
        if hannah: hannah.Kill()

#SKYLINE: Called to switch which camera is active in the Skyline security room
def skylineCameraSwitch():
    G.Skyline_Camera = G.Skyline_Camera + 1
    if(G.Skyline_Camera > 10):
        G.Skyline_Camera = 1
    monitor = Find("security_monitor")
    monitor.SetCamera("camera_%i" % (G.Skyline_Camera))

#SKYLINE: Called to place the appropriate type of bloodpacks in the player's new haven.
def stockTheFridge():
    fridge = Find("fridge")
    bloodpacks = 3
    while(bloodpacks > 0):
        # Changed By CompMod
        # if(__main__.IsClan(__main__.FindPlayer(), "Ventrue")):
        if(8 == __main__.G._pcinfo["clan"]):
            fridge.SpawnItemInContainer("item_g_bluebloodpack")
        else:
            fridge.SpawnItemInContainer("item_g_bloodpack")
        bloodpacks = bloodpacks - 1

#SKYLINE: called to send the player to the taxi if the story state is right
def toTaxi():
    if(G.Story_State >= 100):
        __main__.ChangeMap(2.5, "caine_landmark", "caine_transition")

#SKYLINE: called to unlock the player's haven, changed by wesp
def unlockHaven():
    if(G.Prince_Skyline == 1):
        G.Prince_Skyline = 2
        stockTheFridge()
        #door = Find("haven_door")
        #door.Unlock()
        vent = Find("havenventcover")
        if vent: vent.Kill()
        oldbox = Find("pre_haven_mailbox")
        if oldbox: oldbox.Kill()
        newbox = Find("mailbox_haven")
        if newbox: newbox.ScriptUnhide()
        trunk = Find("trunk")
        if G.Patch_Plus == 1:
            trunk.SpawnItemInContainer("item_p_occult_passive_durations")

#TJP 4/20/04
#ELIZABETHDANE: Check to see if Dirty Cop goes hostile, and if trigger is enabled.
def dirtyCop():
    print "dirtyCop() function called"
    if (G.Dirtycop_Hostile == 1):
        print "dirty cop should be going hostile."
        failed = Find("Relay_Boched_Stern")
        failed.Trigger()
    if (G.Dirtycop_Radio == 1):
        print "dirty cop should be set to radio the other cop."
        passed = Find("relay_persuaded_Dirty_Cop")
        passed.Trigger()

#TJP 5/04/04
#DANE: Check to see if various stages of the quest are completed, and award XP, changed by wesp.
def daneQuest():
    print "daneQuest() function called"
    if (G.Dane_Manifest == 1):
        print "The player just got manifest (right?)"
        playerevents = Find("playerevents")
        playerevents.AwardExp("Dane01")
        G.Dane_Manifest = 2
    if (G.Dane_Report == 1):
        print "The player just got the report (right?)"
        playerevents = Find("playerevents")
        playerevents.AwardExp("Dane02")
        G.Dane_Report = 2
    if (G.Dane_Scene == 1):
        print "The crimescene was just located (right?)"
        playerevents = Find("playerevents")
        playerevents.AwardExp("Dane03")
        G.Dane_Scene = 2
    if ( G.Dane_Complete == 0 and G.Dane_Manifest == 2 and G.Dane_Report == 2 and G.Dane_Scene == 2 ):
        print "A winner is you"
        __main__.FindPlayer().SetQuest("Dane", 2)
        mapstate = Find("Relay_Goals_Achived")
        mapstate.Trigger()
        G.Story_State = 15
        G.Dane_Complete = 1
        G.Dirtycop_Ending = 4

#DANE: XP bonus for not killing anyone on the dane
def daneBonusPoints():
    if (G.Dane_Kills == 0):
        playerevents = Find("playerevents")
        playerevents.AwardExp("Dane05")

#DANE: Set Cams
def daneSetCams():
    if (G.Dane_Cams == 0):
        G.Dane_Cams = 1
        camson = Find("Relay_Cams_ON")
        camson.Trigger()
    else:
        G.Dane_Cams = 0
        camsoff = Find("Relay_Cams_OFF")
        camsoff.Trigger()

#DANE: Set Locks
def daneSetLocks():
    if (G.Dane_Locks == 0):
        G.Dane_Locks = 1
        lockon = Find("Relay_Locks_UNLOCK")
        lockon.Trigger()
    else:
        G.Dane_Locks = 0
        lockoff = Find("Relay_Locks_LOCK")
        lockoff.Trigger()

#DANE: Set Engines
def daneSetEngines():
    if (G.Dane_Engines == 0):
        G.Dane_Engines = 1
        engineon = Find("Relay_Engines_START")
        engineon.Trigger()
    else:
        G.Dane_Engines = 0
        engineoff = Find("Relay_Engines_STOP")
        engineoff.Trigger()

#DANE: Sound Horn
def daneSoundHorn():
    horn = Find("Relay_Sound_Horn")
    horn.Trigger()

#------------------------------------ANTITRIBU------------------------------
#CHANTRY: Regents blood purge; take from Assamite Quietus of burgermeister.          
def RegentCastSpell():
    if(G.regent_anger == 1):
        Find("Regent_Cast_Spell").BeginSequence()
	__main__.ScheduleTask(0.1,"RegentCastSpellHelper()")

def RegentCastSpellHelper():
        pc=__main__.FindPlayer()
        use="use item_w_fists"
        consoleutil.console(use)
	__main__.ScheduleTask(0.1,"RegentCastSpellHelper1()")

def RegentCastSpellHelper1():
        pc=__main__.FindPlayer()
        hud="hidehud 1"
        consoleutil.console(hud)
	__main__.ScheduleTask(0.1,"playerVomit()")
          
def playerVomit():

   if not __main__.FindEntityByName("pcClone"):
       pevents = __main__.FindEntitiesByClass("events_player")
       if len(pevents) > 0: pevents[0].ImmobilizePlayer()
       pc=__main__.FindPlayer()
       pc.Bloodloss(2) 
       pcClone=__main__.CreateEntityNoSpawn("npc_VHuman",pc.GetOrigin(),pc.GetAngles())
       pcClone.SetName("pcClone")
       pcClone.SetModel("models/null.mdl")
       __main__.CallEntitySpawn(pcClone)
       pcClone = __main__.FindEntityByName("pcClone")
       if pcClone:
           pcClone.SetParent("!player")
           pcClone.SetOrigin(pc.GetOrigin())
           pcClone.SetAngles(pc.GetAngles())
           pcClone.SetModel(pc.model)
           pc.SetModel("models/null.mdl")
           __main__.ScheduleTask(0.1,"vomitHelper()")
   else:
       print "vomit in progress. Ignoring request"

def vomitHelper(thread=0):

   if 0 == thread:
       __main__.FindEntityByName('pcClone').ChangeSchedule('SCHED_TROIKA_D_PURGE')
       __main__.ScheduleTask(4.0,"vomitHelper(1)")
   elif 1 == thread:
       __main__.FindEntityByName('pcClone').ChangeSchedule('SCHED_TROIKA_DISORIENTED')
       __main__.ScheduleTask(2.0,"vomitHelper(2)")
   elif 2 == thread:
       hud="hidehud 0"
       consoleutil.console(hud)
       __main__.ScheduleTask(0.1,"vomitHelper(3)")
   else:
       pcClone = __main__.FindEntityByName("pcClone")
       pc=__main__.FindPlayer()
       pc.SetModel(pcClone.model)
       pcClone.ClearParent()
       pevents = __main__.FindEntitiesByClass("events_player")
       if len(pevents) > 0: pevents[0].MobilizePlayer()
       pcClone.Kill()

#------------------------------------Blood Brothers------------------------------
#BLOOD BROTHERS: Blood Brothers cast Sanguinus level 2 (borrow organs)..      
def Bro1CastSanguinus1():
    pc=__main__.FindPlayer()
    bro1 = Find("brother_1")
    bro2 = Find("brother_2")
    if(G.bro_1_anger == 1):
        Find("bro_1_anim_sanguinus1").BeginSequence()
	__main__.ScheduleTask(0.1,"Bro1CastSanguinus1Helper1()")

def Bro1CastSanguinus1Helper1():
        bro1 = Find("brother_1")
        bro2 = Find("brother_2")
        bro1.PlayDialogFile("disciplines/sanguinus/d_npc_sanguinus_level2.wav")
        bro2.PlayDialogFile("disciplines/sanguinus/d_npc_sanguinus_level2.wav")
        bro1.MakeInvincible(1)
        bro2.MakeInvincible(1)
        Find("bro_hands").ScriptUnhide()
        bro2.SetModel("models/character/npc/common/blood_brother/blood_brother_null.mdl")
        __main__.ScheduleTask(9.5,"Bro1CastSanguinus1Helper2()")

def Bro1CastSanguinus1Helper2():
        Find("bro_1_anim_end_sanguinus1").BeginSequence()
        __main__.ScheduleTask(0.75,"Bro1CastSanguinus1Helper3()")

def Bro1CastSanguinus1Helper3():
        bro1 = Find("brother_1")
        bro2 = Find("brother_2")
        bro1.MakeInvincible(0)
        bro2.MakeInvincible(0)
        Find("bro_hands").ScriptHide()
        bro2.SetModel("models/character/npc/common/blood_brother/blood_brother.mdl")
        bro2.PlayDialogFile("disciplines/sanguinus/d_npc_sanguinus_level2_end.wav")
        bro1.PlayDialogFile("disciplines/sanguinus/d_npc_sanguinus_level2_end.wav")

#------------------------------------Blood Brothers 2 part------------------------------
def Bro3CastSanguinus1():
    pc=__main__.FindPlayer()
    bro3 = Find("brother_3")
    bro4 = Find("brother_4")
    if(G.bro_3_anger == 1):
        Find("bro_3_anim_sanguinus1").BeginSequence()
	__main__.ScheduleTask(0.1,"Bro3CastSanguinus1Helper1()")

def Bro3CastSanguinus1Helper1():
        bro3 = Find("brother_3")
        bro4 = Find("brother_4")
        bro3.PlayDialogFile("disciplines/sanguinus/d_npc_sanguinus_level2.wav")
        bro4.PlayDialogFile("disciplines/sanguinus/d_npc_sanguinus_level2.wav")
        bro3.MakeInvincible(1)
        bro4.MakeInvincible(1)
        Find("bro3_arms").ScriptUnhide()
        bro4.SetModel("models/character/npc/common/blood_brother/blood_brother_null.mdl")
        __main__.ScheduleTask(9.5,"Bro3CastSanguinus1Helper2()")

def Bro3CastSanguinus1Helper2():
        Find("bro_3_anim_end_sanguinus1").BeginSequence()
        __main__.ScheduleTask(0.75,"Bro3CastSanguinus1Helper3()")

def Bro3CastSanguinus1Helper3():
        bro3 = Find("brother_3")
        bro4 = Find("brother_4")
        bro3.MakeInvincible(0)
        bro4.MakeInvincible(0)
        Find("bro3_arms").ScriptHide()
        bro4.SetModel("models/character/npc/common/blood_brother/blood_brother.mdl")
        bro4.PlayDialogFile("disciplines/sanguinus/d_npc_sanguinus_level2_end.wav")
        bro3.PlayDialogFile("disciplines/sanguinus/d_npc_sanguinus_level2_end.wav")

#------------------------------------Blood Brothers END------------------------------
#------------------------------------Brother Kanker casts------------------------------
#Brother Kanker casts: animalism wolves.         
def BrotherKankerCasts():
    if(G.Kanker_Dead == 1):
        return
    else:
        Find("brother_Kanker_animalism").BeginSequence()
	__main__.ScheduleTask(0.1,"BrotherKankerCasts1()")

def BrotherKankerCasts1():
        kanker = Find("Brother_Kanker")
        wolf = Find("Brother_Kanker_wolf_maker")
        kanker.PlayDialogFile("disciplines/animalism/level5/anm_lvl5_activate.wav")
        wolf.Spawn()
	__main__.ScheduleTask(5.0,"BrotherKankerCasts2()")

#Brother Kanker casts: casts obfuscate.... 
def BrotherKankerCasts2():
        kanker = Find("Brother_Kanker")
        kanker.PlayDialogFile("disciplines/obfuscate/activate.wav")
#        kanker.SetScriptedDiscipline("Obfuscate 5")
        Find("brother_Kanker_Obfuscate1").BeginSequence()
#        Find("potence_emitter").TurnOff()
	__main__.ScheduleTask(5.5,"BrotherKankerCasts3()")

def BrotherKankerCasts3():
        kanker = Find("Brother_Kanker")
        kanker.PlayDialogFile("disciplines/obfuscate/deactivate.wav")
#        kanker.SetScriptedDiscipline("Obfuscate 0")
#        Find("potence_emitter").TurnOn()
        Find("brother_Kanker_Obfuscate2").BeginSequence()

#------------------------------------Professional killer------------------------------
#DOWNTOWN: quest Professional killer for old clan tzimisce
def KillerStart():
    if(G.Killer_accepted == 1):
       __main__.FindPlayer().SetQuest("Profkiller", 1)
       __main__.FindPlayer().SetQuest("Oldclanblood", 3)
       Find("Albrecht_container").ScriptUnhide()

def KillerSteady():
    if(G.Killer_combat == 1):
       return
    else:
       Find("killer_starting").Trigger()
       __main__.ScheduleTask(0.75,"KillerSteady1()")

def KillerSteady1():
    Find("pc_killer_controller").CreateControllerNPC()
    Find("player_killer_look").BeginSequence()
    __main__.ScheduleTask(0.1,"KillerSteady2()")
    container = __main__.FindEntityByName("Albrecht_container")
    if container: container.BarterEnd()
    print "killer Steady"

def KillerSteady2():
    pc=__main__.FindPlayer()
    AlbrechtRifle = __main__.FindEntityByName("AlbrechtRifle")
    if(AlbrechtRifle):
       return
    else:
       AlbrechtRifle=__main__.CreateEntityNoSpawn("prop_dynamic_ornament",pc.GetOrigin(),pc.GetAngles())
       AlbrechtRifle.SetName("AlbrechtRifle")
       AlbrechtRifle.SetModel("models/weapons/arsenal_mod/steyrscout/wield/w_m_scout.mdl")
       __main__.CallEntitySpawn(AlbrechtRifle)
       AlbrechtRifle = __main__.FindEntityByName("AlbrechtRifle")
       if AlbrechtRifle: AlbrechtRifle.SetAttached("!player")

def KillerTimerStart():
    G.Killer_combat = 1
    timer = Find("killer_timer")
    timer.RestartTimer()
    timer.Show()
    Find("AlbrechtRifle").ScriptHide()    

def KillerWaepon1Check():
    pc=__main__.FindPlayer()
    if(pc.HasWeaponEquipped("item_w_rem_m_700_bach")):
       Find("victim_1").TakeDamage(85)

def KillerWaepon2Check():
    pc=__main__.FindPlayer()
    if(pc.HasWeaponEquipped("item_w_rem_m_700_bach")):
       Find("victim_2").TakeDamage(85)

def KillerCheck():
    G.Victim_Death = G.Victim_Death + 1
    
    if(G.Victim_Death == 2):
       G.Killer_completed = 1
       __main__.FindPlayer().SetQuest("Profkiller", 2)
       __main__.FindPlayer().SetQuest("Oldclanblood", 4)
       Find("koldunism_timer").Hide()
       print "killer complete"

def KillerFail():
    __main__.FindPlayer().SetQuest("Profkiller", 3)
    print "killer fail"    
#------------------------------------Professional killer end------------------------------
#CHANTRY: Gargoyle quest 
def GargoyleQuest4():
    __main__.FindPlayer().SetQuest("Gargoylequest", 4)
    G.Gargoyle_Quest = 4

#CONFESSION: Gargoyle quest 
def GargoyleQuest5():
    __main__.FindPlayer().SetQuest("Gargoylequest", 5)
    G.Gargoyle_Quest = 5

#EMPIRE: Gargoyle quest 
def GargoyleQuest6():
    __main__.FindPlayer().SetQuest("Gargoylequest", 6)
    G.Gargoyle_Quest = 6

#------------------------------------------------------------------
#DOWNTOWN: mugging steal from burgermeister clan quest mod
def muggerKilledCheck():
    if(G.muggers_killed == 2 and not G.saved_hooker_mugging == 1):
        hooker = Find("mugged_hooker") 
        if(hooker and not __main__.IsDead("mugged_hooker")):
            G.saved_hooker_mugging = 1
            hooker.SetRelationship("mugger1 D_NU 0")
            hooker.SetRelationship("mugger2 D_NU 0")
            hooker.SetRelationship("player D_NU 0")
            hooker.SetDisposition("Neutral",1)
            __main__.FindPlayer().SetQuest("hooker_mugging",2)
           
def hookerKilled():
    if(not G.saved_hooker_mugging == 1 or __main__.FindPlayer().GetQuestState("hooker_mugging") < 3):
        __main__.FindPlayer().SetQuest("hooker_mugging",4)
        
def hookerPlace():
    hooker = __main__.Find("mugged_hooker")
    if(G.saved_hooker_mugging == 1 and hooker and G.hooker_talked_post_mugging == 1):   
        locations = [(2893.94189453125, -967.39410400390625, -7423.96875),\
        	     (2542.4296875, -2252.649169921875, -7423.96875),\
        	     (3768.515869140625, -3997.677734375, -7423.96875),\
        	     (854.39874267578125, 1587.544921875, -7423.96875),\
        	     (3183.53271484375, 2950.16455078125, -7423.96875),\
        	     (794.93603515625, 3669.86962890625, -7423.96875)\
        	    ] 
        angles = [(0, 166.3934326171875, 0),\
        	  (0, 6.6851806640625, 0),\
        	  (0, 10.1788330078125, 0),\
        	  (0, -109.05029296875, 0),\
        	  (0, -172.96875, 0),\
        	  (0, 33.4478759765625, 0)\
        	 ]
            
        num_locations = len(locations)   
        rand_num = random.randrange(0,(num_locations - 1))
        the_location = locations[rand_num]  
        the_angle = angles[rand_num]
        hooker.SetOrigin(the_location)
        hooker.SetAngles(the_angle)
    elif(G.saved_hooker_mugging == 1 and G.hooker_talked_post_mugging == 0 and hooker):   
        hooker.Kill()
    
#------------------------------------------------------------------
#DANE Cam cycle
def daneCameraSwitch():
    G.Dane_Camera = G.Dane_Camera + 1
    if (G.Dane_Camera > 3):
        G.Dane_Camera = 1
    monitor = Find("dane_monitor")
    monitor.skin = G.Dane_Camera
    if (G.Dane_Camera == 3):
        target = Find("Trigger_Look_At_CrimeScene")
        target.ScriptUnhide()
        Find("Kuejin_deepones2").ScriptUnhide()
    else:
        target = Find("look_target")
        target.ScriptHide()

print "levelscript loaded"
