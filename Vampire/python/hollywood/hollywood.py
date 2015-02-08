print "loading hollywood level script"
import __main__
import consoleutil

from __main__ import G

Find = __main__.FindEntityByName
Finds = __main__.FindEntitiesByName

# added by wesp
def civilianDeath():
    pc = __main__.FindPlayer()
    if(pc.humanity >= 3):
        pc.HumanityAdd( -1 )

#609: hides events that may break with obfuscate
def malkNosCatchAll():
    firstRunner = Find("studiodoor1-trigger_event")
    secondRunner = Find("door_bash-trigger_failsafe")
    thirdRunner = Find("inigo_trigger")
    # Changed By CompMod
    # if (__main__.IsClan(__main__.FindPlayer(), "Nosferatu") or __main__.IsClan(__main__.FindPlayer(), "Malkavian")):    
    pc=__main__.FindPlayer()
    c1=__main__.FindEntityByName("companion1")
    c2=__main__.FindEntityByName("companion2")
    hasObfuscate=0
    if pc.IsClan("Nosferatu") or pc.IsClan("Malkavian"): hasObfuscate=1
    if c1:
        if c1.IsClan("Nosferatu") or c1.IsClan("Malkavian"): hasObfuscate=1
    if c2:
        if c2.IsClan("Nosferatu") or c2.IsClan("Malkavian"): hasObfuscate=1    
    if hasObfuscate:
        if firstRunner: firstRunner.ScriptHide()
        print "first runner hidden"
        if secondRunner: secondRunner.ScriptHide()
        print "second runner hidden"
        if thirdRunner: thirdRunner.ScriptHide()
        print "third runner hidden"

#609: update quest log after Andrei dies
def andreiDead():
    __main__.FindPlayer().SetQuest("Kings Way", 2)

#ASPHOLE: called to swap ash and lookalike clothes
def ashClothingSwap():
    ash = Find("Ash")
    lookalike = Find("ash_lookalike")
    ash.SetModel("models/character/npc/unique/Hollywood/Ash_Lookalike/ash_Lookalike.mdl")
    lookalike.SetModel("models/character/npc/unique/Hollywood/Ash/Ash.mdl")

#ASPHOLE: determines the results of dialog with ash, changed by wesp
def ashDialog():
    if(G.Ash_Switch==1):
        print "ash_switch ==1"
        lookalike = Find("Ash_lookalike")
        lookalike.WillTalk(1)
    elif(G.Ash_Fake):
        print "ash should go to bathroom"
        ashconvo = Find("ash_convo_01")
        ashbath = Find("ash_bathroom_spot")
        ash = Find("Ash")
        ashconvo.Disable()
        ashbath.Enable()
        ash.WillTalk(0)
        ash.ChangeSchedule("-")
        hunter = Find("Hunter")
        hunter.ScriptUnhide()
        relay = Find("fake_ash_staked_relay")
        relay.Enable()
        pc = __main__.FindPlayer()
        if(pc.humanity >= 3 and G.Patch_Plus == 1):
            pc.HumanityAdd( -1 )

#ASPHOLE: sets the ash lookalike's disposition to dead
def ashLookalikeDead():
    fakeAsh = Find("Ash_lookalike")
    fakeAsh.SetDisposition("Dead", 1)
    fakeAsh.WillTalk(0)
    fakeAsh.TweakParam("vision 0")
    fakeAsh.TweakParam("hearing 0")

#ASPHOLE: determines whether Ash is in the Asphole, along with his lookalike, changed by Wesp
def ashSituation():
    ash = Find("Ash")
    lookalike = Find("Ash_lookalike")
    hunter = Find("Hunter")
    if(G.Ash_Know != 1):
        if(lookalike):
            lookalike.WillTalk(0)
    if(G.Ash_Sewers):
        if(ash):
            ash.Kill()
        if(hunter):
            hunter.Kill()
    if(G.Ash_Fake or G.Story_State > 65):
        if(ash):
            ash.Kill()
        if(lookalike):
            lookalike.Kill()
        if(hunter):
            hunter.Kill()

#ASPHOLE: determines whether Ash and lookalike have privacy.
def ashBathswitch():
    print "ashBathswitch called"
    if(G.Ash_Bathswitch == 1):
        print "Ash in bathroom. Triggering logic_relay."
        logswitch = Find ("bathroom-logic")
        logswitch.Trigger()

#ASPHOLE: determines results of talking to the lookalike
def lookalikeDialog():
    if(G.Ash_Switch == 2):
        spot = Find("lookalike_bathroom_spot")
        spot.Enable()
        lookalike = Find("Ash_lookalike")
        lookalike.WillTalk(0)
        lookalike.UseInteresting(1)
        lookalike.ChangeSchedule("-")

#TJP - 04/08/04
#ASPHOLE: sends the player to the sewers if Ash is ready to go
def toSewers():
    if(G.Ash_Sewers == 1):
        __main__.ChangeMap(2.5, "AspHole4", "AspHoleTeleportSewers")

#CHINESE THEATER: set quest on gargoyle death, changed by wesp
def SetGargoyleQuestState():
    pc = __main__.FindPlayer()
    state = pc.GetQuestState("Gargoyle")
    if state > 0 and state != 2 and state != 5:
        pc.SetQuest("Gargoyle", 3)
    if state == 2:
        pc.SetQuest("Gargoyle", 6)
    if state == 5:
        pc.SetQuest("Gargoyle", 7)

#JEWELRY: Isaac dialog end
def IsaacDialogEnd():
    #changed by dan_upright 04/12/04
    #if G.Isaac_Kingstart == 1:
    #    __main__.ChangeMap(2.5, "jewelry_mark", "trig_transition")
    #    G.Isaac_Kingstart = 2
    if(G.Isaac_Show == 1):
        #changes end
        video = Find("start_snuff")
        video.Trigger()
    elif(G.Isaac_Movie == 1):
        video = Find("start_half_snuff")
        video.Trigger()

#JEWELRY: Isaac gift, added by wesp
def IsaacGift():
    if(G.Isaac_Gift == 1):
        G.Isaac_Gift = 2

#LUCKYSTAR:  called when the player tries to exit the map
def luckyStarExit():
    if(G.Story_State < 100):
        __main__.ChangeMap(2.5, "luckystar1", "luckystarTeleport1")
    else:
        __main__.ChangeMap(2.5, "caine_landmark", "luckystarCaine")

#LUCKYSTAR: Called when the player grabs the business card, changed by wesp
def junkyardCardPickup():
    if(__main__.FindPlayer().GetQuestState("Serial") < 7):
        __main__.FindPlayer().SetQuest("Serial", 7)

#LUCKYSTAR: called when the killer gets away
def killerEscape():
    __main__.FindPlayer().SetQuest("Serial", 6)
    __main__.FindPlayer().SetQuest("Muddy", 4)
    G.Muddy_Dead = 1

# TJP - 01/28/04
#LUCKYSTAR: Determines what state the luckystar hotel is in
def luckyState():
    print ("luckyState called")
    if(G.Story_State >= 115):
        print ("Anarchs present")
        anarchs = Find("luckystate-Anarchs_Present")
        anarchs.Trigger()
        # Added by Dheu for CompMod
        if 1 == __main__.G.Damsel_WasComp:
            __main__.ScheduleTask(4.0,"__main__.FindEntityByName('Damsel').ScriptHide()")
    if(G.Killer_Key == 1):
        # Updated by CompMod
        pc = __main__.FindPlayer()
        state = pc.GetQuestState("Muddy")
        if 3 == state:
            if not pc.HasItem("item_k_lucky_star_murder_key"):
                pc.GiveItem("item_k_lucky_star_murder_key")
            print ("Killer present")
            killer = Find("luckystate-Killer_Present")
            killer.Trigger()
    if(G.Lucky_Blood == 1):
        print ("Tape event present")
        tape = Find("luckystate-Horrortape_event")
        tape.Trigger()
        #else:
        #    print ("Default Map State")
        #    default = Find("luckystate-Default")
        #    default.Trigger()

# TJP - 03/19/04
#LUCKYSTAR: useless, really
def lsww():
    print ("wait for it")
    if (G.LSWW > 32):
        print ("yup")
        ww = Find("werewolf")
        ww.ScriptUnhide()

#LUCKYSTAR: on hatter's death, set quest state, changed by wesp
def onHatterDeath():
    pc = __main__.FindPlayer()
    if pc.GetQuestState("Writer") == 1:
        G.Hatter_Dead = 1
        pc.SetQuest("Writer", 4)
        hatter = Find("DHatter")
        center = hatter.GetCenter()
        point = (center[0] + 25, center[1] + 25, center[2])
        script = __main__.CreateEntityNoSpawn("item_g_Hatters_Screenplay", point, (0,0,0) )
        __main__.CallEntitySpawn(script)

#LUCKYSTAR: on pickup of netcafe key, set quest state
def OnNetcafeKeyPickup():
    pc = __main__.FindPlayer()
    if pc.GetQuestState("Tape") > 0:
        pc.SetQuest("Tape", 7)

#LUCKYSTAR:  called to look at the werewolf head
def werewolfHeadCamera():
    camera = Find("werewolf_head_camera")
    camera.StartShot()

#METALHEAD: Set Mitnick quest to 10, because Worldcraft doesn't like commas, changed by wesp
def failMitnick():
    pc = __main__.FindPlayer()
    pc.SetQuest("Mitnick", 10)
    G.Shubs_Act = 5

# TJP - 02/06/04
#NETCAFE: Determines if headrunners are present, changed by wesp
def netcafeState():
    # print ("Netcafe function called")
    if G.Lucky_Blood == 1:    #("G.Netcafe_Key == 1"):
        # print ("Tape Event map state")
        # logic = Find("logic_kill_safe_state")
        # if logic: logic.Trigger()
        logic = Find("logic_enable_combat_state")
        if logic: logic.Trigger()
    if G.Patch_Plus < 2:
        frag = Find("frag")
        fragnode = Find("fragnode")
        if frag: frag.ScriptUnhide()
        if fragnode: fragnode.ScriptUnhide()

#NETCAFE: Set quest state after picking up tape
def SetTapeQuestState():
    pc = __main__.FindPlayer()
    if pc.GetQuestState("Tape") > 0:
        pc.SetQuest("Tape", 4)

#NETCAFE: courier's e-mail
def OnCourierEmail():
    G.Courier_QuickBuck = 1
    pc = __main__.FindPlayer()
    if pc.GetQuestState("Courier")== 1:
        pc.SetQuest("Courier", 2)

#NETCAFE: player has found out about Ginger Swan's crypt
def OnGingerSwanEntry():
    pc = __main__.FindPlayer()
    state = pc.GetQuestState("Courier")
    if state == 3:
        pc.SetQuest("Courier", 4)
        #changed by dan_upright 02/12/04
    else:
        G.GingerSwanKnowledge = 1
        #changes end

#REDSPOT:called to choose a float line for spicoli
def spicoliFloat():
    from random import Random
    from time import time
    R = Random( time() )
    Index = R.randint(2,8)
    spicoli = Find("Spicoli")
    if(spicoli):
        spicoli.PlayDialogFile(("\Character\dlg\Hollywood\Spicoli\line%i_col_e.mp3" % Index))

#REDSPOT:called to see if Slater and Spicoli are alive, added by wesp
def slaterAlive():
    slater = Find("Slater")
    spicoli = Find("Spicoli")
    if(__main__.IsDead("Slater")):
        if(slater):
            slater.Kill()
    if(__main__.IsDead("Spicoli")):
        if(spicoli):
            spicoli.Kill()
    if G.Patch_Plus == 1:
        toy = Find("toy")
        toynode = Find("toynode")
        if toy: toy.ScriptUnhide()
        if toynode: toynode.ScriptUnhide()

#--------------------------------------------------------------------------
def SetSewerNPCs():
    npc = Find("Ash")
    npc.WillTalk(1)

    npcs = Finds("hunter_1") + Finds("hunter_4") + Finds("hunter_4_vision") + Finds("hunter_5") + Finds("hunter_2_vision") + Finds("hunter_5a") + Finds("hunter_3") + Finds("hunter_3_vision") + Finds("hunter_2") + Finds("hunter_5b")
    for npc in npcs:
        npc.SetRelationship("Ash D_HT 5")

#SEWERS (ASH): end sewers Ash Dialog
def AshDialogEnd():
    npc = Find("Ash")
    npc.WillTalk(0)
    leave = Find("sAsh_leave")
    leave.BeginSequence()
    __main__.ChangeMap(0.0, "sewer_map_landmark", "trig_transition_sewer")

#--------------------------------------------------------------------------
#SEWERS (ASH): end sewers trigger
def AshDeathCheck():
    if (G.Ash_Dead == 1):
        __main__.FindPlayer().SetQuest("Hunters", 5)
        __main__.FindPlayer().HumanityAdd( -1 )
	__main__.ChangeMap(5.0, "sewer_map_landmark", "trig_transition_sewer")
    else:
        Find("new_trig_end").Trigger()

#--------------------------------------------------------------------------
# TJP - 01/27/04 update 04/08/04
#SINBIN: Determines if Chastity goes aggro
def checkChastity():
    print ("checkChastity called")
    if (G.Chastity_Attack == 1):
        trigger = Find("Chastity_go_hostile-trigger")
        trigger.Enable()

# TJP - 01/27/04
#SINBIN: Determines when Kerri goes where
def kerriBiz():
    print ("kerriBiz called")
    if (G.Kerri_Nos == 1):
        print ("kerri frightened by nos")
        gotonos = Find("kerri-logic_nos")
        gotonos.Trigger()
    elif(G.Kerri_Mesmerize == 1):
        G.Kerri_Biz = 1
        print ("kerri mesmerized")
        gotomez = Find("Kerri-logic_mesmerized")
        gotomez.Trigger()
    elif(G.Kerri_Biz == 1):
        print ("kerri going to back room")
        gotoroom = Find("Kerri-logic_to_backroom")
        gotoroom.Trigger()
    kerri = Find("Kerri")
    if kerri: kerri.WillTalk(0)

#SINBIN:  Won't let Kerri talk to the player unless there is Biz
def kerriBizCheck():
    if(G.Kerri_Biz == 1):
        kerri = Find("Kerri")
        if kerri: kerri.WillTalk(1)

# TJP - 01/22/04
#SINBIN: Controls what map state the sin bin is in, depending on if you are on VVs quest or not
def sinbinMapstate():
    print("sinbinMapstate called")
    kerri = Find("Kerri")
    if kerri: kerri.WillTalk(0)
    if(G.Velvet_Quest <> 1 or G.Hunter_Dead == 1):
        noquest = Find("mapstate_not_on_VV_quest")
        noquest.Trigger()
    elif(G.Velvet_Quest == 1):
        quest = Find("mapstate_on_VV_quest")
        quest.Trigger()

# TJP - 01/21/04
#SINBIN: Controls whether Peeper_1 deposits coins or goes to get more
def windowIncrement():
    if(G.Window_Count == 3):
        getchange = Find("change_machine-ss")
        coinfeed = Find("Peeper_1-ss_feed_coins")
        coinfeed.CancelSequence()
        getchange.BeginSequence()
        G.Window_Count = 0
    elif(G.Window_Count < 3):
        coinfeed = Find("Peeper_1-ss_feed_coins")
        coinfeed.BeginSequence()
        G.Window_Count = G.Window_Count + 1

# TJP - 01/21/04
#SINBIN: Controls whether Peeper_1 gets change or leaves, depending on what state the change machine is in
def changeMachine():
    print("changeMachine function called")
    if(G.Change_Machine == 0):
        print("G.Change_Machine == 0")
        getchange = Find("get_change-ss")
        #coinfeed = Find("Peeper_1-ss_feed_coins")
        getchange.BeginSequence()
        #coinfeed.Enable()
    elif(G.Change_Machine == 1):
        print("G.Change_Machine == 1")
        G.Sin_Peeper1 = 1
        broken = Find("no_change-ss")
        broken.BeginSequence()

# TJP - 01/23/04
#SINBIN: If both patrons leave the peep booths, the dancers go on break.
def dancersState():
    print("dancersState called")
    if(G.Sin_Peeper1 == 1 and G.Sin_Peeper3 == 1):
        changedancers = Find("Dancers-logic_int_place_state")
        changedancers.Trigger()
        kerri = Find("Kerri")
        if kerri: kerri.WillTalk(1)
    else:
        print("not all patrons out yet")

#SINBIN:  Update "Strip to Hunt" quest state after Chastity is killed.
def chastityKilled():
    G.Chastity_Dead = 1
    if (G.Hunter_Dead == 1 and G.Sin_Innocent == 1):
        __main__.FindPlayer().SetQuest("Strip", 2)
    elif (G.Hunter_Dead == 1):
        __main__.FindPlayer().SetQuest("Strip", 2)
        __main__.FindPlayer().AwardExperience("Strip03")
    world = Find("world")
    world.SetSafeArea(1)

#SINBIN: hacked flynn's computer, got secret message, set flag, quest state.
def gotSecretMessage():
    G.Flynn_Message = 1
    pc = __main__.FindPlayer()
    state = pc.GetQuestState("Tape")
    if  (state == 1):
        pc.SetQuest("Tape", 3)

#SINBIN: checks to see if the player can afford to open the window, and removes his money
def windowCheck(int):
    pc = __main__.FindPlayer()
    if(pc.CurrentMoney() >= 5):
        pc.MoneyRemove(5)
        window = Find("peepshw%i" % int)
        window.Open()
    else:
        rejectSound = Find("reject_sound_%i" % int)
        rejectSound.PlaySound()

# TJP - 01/28/04
#VESUVIUS: Determines if Charming Stripper Misti goes to the private room or not. I hope she does!
def mistiState():
    print("mistiState called")
    if(G.Misti_Follow == 1):
        print("shes going!")
        mistigo = Find("Misti-logic_walk_back")
        mistigo.Trigger()
    else:
        print("G.Misti_Follow <> 1")
        misti_floor = Find("misti_floor")
        misti_floor.Trigger()

# TJP - 01/12/04
#VESUVIUS: enables trigger that tells VV to walk upstairs
def velvetRelocate():
    if(G.Velvet_Stairs == 1):
        triggerone = Find("VV_failsafe_1")
        triggertwo = Find("VV_failsafe_2")
        triggerone.Enable()
        triggertwo.Enable()
    if(G.Velvet_Quest == 2):
        trigger = Find("vv_give_quest_2_trigger")
        trigger.ScriptUnhide()
    if(G.Velvet_Quest > 2):
        trigger = Find("vv_give_quest_2_trigger")
        if trigger: trigger.Kill()

#VESUVIUS:  Puts VV on stage dancing after all her quests are done
def velvetDance():
    # CompMod : Delay dance till after complete Hallowbrook.
    # if (G.Velvet_Quest >= 4):
    if (G.Velvet_Quest >= 4 and G.Story_State > 80 and 0 == G.VV_WasComp):
        vv_dance_relay = Find("vv_dance_relay")
        vv_dance_relay.Trigger()

# TJP - 01/13/04
#VESUVIUS: decides which VV appears, the upstairs instance or the downstairs one
def velvetLocate():
    if(G.Velvet_Stairs > 0 and G.Velvet_Quest < 4):
        teleporter = Find("VV2")
        trigger = Find("VV_forcedlg-trigger")
        teleporter.Teleport()
        if trigger: trigger.Kill()

# TJP - 01/15/04
#VESUVIUS: randomizes guys sitting around
def randomSitters():
    from random import Random
    from time import time
    R = Random( time() )
    Index = R.randint(0,1)
    if(Index == 0):
        stateone = Find("club_state_1")
        stateone.Trigger()
    elif(Index == 1):
        statetwo = Find("club_state_2")
        statetwo.Trigger()

# TJP - 01/15/04
#VESUVIUS: randomizes state of Vesuvius
def randomClubstate():
    from random import Random
    from time import time
    R = Random( time() )
    Index = R.randint(0,1)
    if(Index == 0):
        stateone = Find("club_state_1")
        stateone.Trigger()
    elif(Index == 1):
        statetwo = Find("club_state_2")
        statetwo.Trigger()

# TJP - 01/15/04
#VESUVIUS: randomizes Vesuvius random events, changed by wesp
def randomClubevents():
    from random import Random
    from time import time
    R = Random( time() )
    Index = R.randint(0,10)
    eventone = Find("stripper_from_dressing_room-logic_disable")
    eventtwo = Find("stripper_off_work-logic_disable")
    eventthree = Find("disable_bj_event")
    if(Index < 5):
        eventtwo.Trigger()
        eventthree.Trigger()
        offwork = Find("stripper_off_work")
        if offwork: offwork.Kill()
    elif(Index < 10):
        eventone.Trigger()
        eventthree.Trigger()
    elif(Index == 10):
        eventone.Trigger()
        eventtwo.Trigger()

#HOLLYWOOD: determines if the sweeper is on the streets and going to talk to the player, changed by wesp
def sweeperPlacement():
    if G.Isaac_Know:
        sweeper = Find("Sweeper")
        if sweeper:
            sweeper.Kill()
            trig = Find("trig_kill_sweeper")
            trig.Kill()
    else:
        __main__.ScheduleTask(3.0, "__main__.FindEntityByName(\"Sweeper\").StartPlayerDialog(256)")

#HOLLYWOOD: hides/unhides Samantha
def SetSamantha():
    # Changed By CompMod
    # if __main__.IsClan(__main__.FindPlayer(), "Nosferatu"):
    if 5 == __main__.G._pcinfo["clan"]:
        sam = Find("Samantha")
        if sam: sam.Kill()
        # Changed By CompMod
        # elif G.Isaac_Know == 1 and not G.Samantha_Know == 1:
    elif G.Isaac_Know == 1 and not G.Samantha_Know == 1 and __main__.FindPlayer().IsPC():
        sam = Find("Samantha")
        sam.ScriptUnhide()
        sam_trig = Find("trig_samantha")
        sam_trig.Enable()
    elif G.Samantha_Stopped or G.Samantha_FinishedCall:
        sam = Find("Samantha")
        if sam: sam.Kill()

#HOLLYWOOD: hides/unhides Courier
def SetCourier():
    if G.Courier_QuickBuck == 1:
        courier = Find("Courier")
        if courier:
            courier.ScriptUnhide()
            courier.MakeInvincible(1)

#HOLLYWOOD: sets Anonymous Caller
def SetAnonCaller():
    npc = Find("Anoncaller")
    npc.WillTalk(0)

    if G.Lucky_Blood == 1:
        timer = Find("timer_anoncaller")
        if timer: timer.Kill()

    elif G.Flynn_Message == 1:
        trig = Find("trig_anoncaller")
        if trig: trig.Enable()

#HOLLYWOOD: checks state of Anonymous Caller
def AnonCallerDialogEnd():
    npc = Find("Anoncaller")
    npc.WillTalk(0)

    timer = Find("timer_anoncaller")
    if timer:
        if G.Lucky_Blood == 1:
            timer.Kill()
        else:
            timer.Enable()

#HOLLYWOOD: sets Tommy at cafe
def SetTommy():
    tommy = Find("Tommy")
    state = __main__.FindPlayer().GetQuestState("Tommy")
    if tommy:
        if state == 1:
            tommy.ScriptUnhide()
            stuffs = Finds("tommy_table")
            for stuff in stuffs:
                stuff.ScriptUnhide()
        elif state == 2 or state == 3:
            tommy.Kill()
            stuffs = Finds("tommy_table")
            for stuff in stuffs:
                stuff.Kill()
        else:
            tommy.ScriptHide()

#HOLLYWOOD: kills taxi if player is nosferatu
def SetTaxi():
    # Changed By CompMod
    # if __main__.IsClan(__main__.FindPlayer(), "Nosferatu"):
    if 5 == __main__.G._pcinfo["clan"]:
        logic = Find("logic_kill_taxi")
        if logic: logic.Trigger()
        map = Find("sewer_map")
        if map: map.Unlock()

#HOLLYWOOD: cleans up after courier's death
def UnsetCourierBlood():
    if __main__.FindPlayer().GetQuestState("Courier") > 4:
        bloods = Finds("courier_blood")
        for blood in bloods:
            blood.Kill()
        arm = Find("courier_arm")
        if arm: arm.Kill()

#HOLLYWOOD: places NPCs
def SetNPCs():
    sweeperPlacement()
    SetSamantha()
    SetCourier()
    SetAnonCaller()
    SetTommy()
    SetTaxi()
    UnsetCourierBlood()

#HOLLYWOOD: on Tommy's death, set quest state
def OnTommyDeath():
    pc = __main__.FindPlayer()
    if pc.GetQuestState("Tommy") > 0:
        pc.SetQuest("Tommy", 3)

#HOLLYWOOD: change sam's interesting places
def SetSamBusIPs():
    ips = Finds("ip_sam_phone")
    for ip in ips:
        ip.Disable()
    ips = Finds("ip_sam_bus")
    for ip in ips:
        ip.Enable()

#HOLLYWOOD: on sam's dialogue, check flags
def OnSamEndDialog():
    sam = Find("Samantha")
    sam.UseInteresting(1)
    if G.Samantha_Phone == 0:
        SetSamBusIPs()

    if G.Samantha_Dominated or G.Samantha_Dementated or G.Samantha_Persuaded or G.Samantha_Threat:
        sam.WillTalk(0)
        G.Samantha_Stopped = 1

#HOLLYWOOD: use right sam float for player
def PlaySamCall():
##    sam = Find("Samantha")
    if __main__.FindPlayer().IsMale():
##        sam.PlayDialogFile("Character/dlg/Hollywood/Samantha/line151_col_e.mp3")
        logic = Find("sound_sam_call_m")
        logic.Start()
    else:
##        sam.PlayDialogFile("Character/dlg/Hollywood/Samantha/line151_col_f.mp3")
        logic = Find("sound_sam_call_f")
        logic.Start()

#HOLLYWOOD: stop right sam float for player
def StopSamCall():
    if not G.Samantha_Stopped:
        if __main__.FindPlayer().IsMale():
            sound = Find("sound_sam_call_m")
            sound.Cancel()
        else:
            sound = Find("sound_sam_call_f")
            sound.Cancel()
        SetSamBusIPs()
        G.Samantha_Stopped = 1
        if not G.Samantha_FinishedCall:
            __main__.FindPlayer().ChangeMasqueradeLevel(-1)
            logic = Find("logic_sam_masq")
            if logic: logic.Kill()
        sam = Find("Samantha")
        if sam: sam.WillTalk(0)

#HOLLYWOOD: if player leaves map before stopping samantha,
# player gets masquerade violation
def CheckSamMasqViolation():
    if G.Samantha_Phone and not G.Samantha_Stopped:
        __main__.FindPlayer().ChangeMasqueradeLevel(1)
        logic = Find("logic_sam_masq")
        if logic: logic.Kill()
        sam = Find("Samantha")
        if sam: sam.Kill()

#HOLLYWOOD: set sam post-call behavior
def SetSamPostCall():
    sam = Find("Samantha")
    if sam:
        if not G.Samantha_Stopped:
            sam.SetFollowerBoss("!player")
            __main__.FindPlayer().ChangeMasqueradeLevel(1)
            logic = Find("logic_sam_masq")
            if logic: logic.Kill()
            ips = Finds("ip_sam_phone")
            for ip in ips:
                ip.Kill()
            if sam: sam.WillTalk(1)
            G.Samantha_FinishedCall = 1
        else:
            SetSamBusIPs()

#TAWNIS PLACE: Checks to see if all cameras have been placed, changed by wesp
def placeCam():
    pc = __main__.FindPlayer()
    if ( pc.HasItem( "item_g_wireless_camera_1" ) ):
        pc.RemoveItem( "item_g_wireless_camera_1" )
    if G.Tawni_Spotted == 0:
        G.Imalia_Cam = G.Imalia_Cam + 1
        if G.Imalia_Cam == 3:
            __main__.FindPlayer().SetQuest("Imalia", 2)

#TAWNIS PLACE: Advance quest to state after activating cams, changed by wesp

def setSpotted():
    if (G.Imalia_Quest > 0 and G.Imalia_Quest < 4):
        G.Tawni_Spotted = 1
        __main__.FindPlayer().SetQuest("Imalia", 7)

def setComp():
    __main__.FindPlayer().SetQuest("Imalia", 3)
    G.Imalia_Quest = 3

def setTawniDead():
    __main__.FindPlayer().SetQuest("Imalia", 4)
    G.Tawni_Dead = 1

#--------------------------------------Ultra hunter scene------------------------------------------
#ULTRA HUNTER scene: start scene on load map hw_609_1
def UltraHunterScene():
        uh1 = Find("ultra_hunter_1")
        uh1.PlayDialogFile("character/boss/ulta_hunter_1/line1_col_e.wav")
#        __main__.ScheduleTask(0.1,"UltraHunterScene1a()")

def UltraHunterScene1a():
        uh1 = Find("ultra_hunter_1")
        uh1.PlayDialogFile("character/boss/ulta_hunter_1/line11_col_e.wav")
        __main__.ScheduleTask(5.6,"UltraHunterScene1()")

def UltraHunterScene1():
        uh1 = Find("ultra_hunter_1")
        uh1.PlayDialogFile("character/boss/ulta_hunter_1/line21_col_e.wav")
        Find("uh_cross").ScriptUnhide()
        Find("go3_uhunter_1").BeginSequence()
        Find("pc_fear_1").BeginSequence()
        __main__.ScheduleTask(0.92,"UltraHunterScene2a()")

def UltraHunterScene2a():
        uh1 = Find("ultra_hunter_1")
        uh1.PlayDialogFile("character/boss/ulta_hunter_1/holy_lights.wav")
#        Find("sound_pc_holy_lights_1").PlaySound()
        __main__.ScheduleTask(1.5,"UltraHunterScene2()")

def UltraHunterScene2():
        uh1 = Find("ultra_hunter_1")
        uh1.PlayDialogFile("character/boss/ulta_hunter_1/line31_col_e.wav")
        __main__.ScheduleTask(10.75,"UltraHunterScene3()")

def UltraHunterScene3():
        Find("uh_cross").ScriptHide()
        Find("pc_fear_end").BeginSequence()
        __main__.ScheduleTask(2.5,"UltraHunterScene4()")

def UltraHunterScene4():
        Find("ultra_hunter_1").SetRelationship( "player D_HT 5")
        Find("elite_hunter_1").SetRelationship( "player D_HT 5")
        Find("elite_hunter_2").SetRelationship( "player D_HT 5")
        Find("elite_hunter_3").SetRelationship( "player D_HT 5")
        Find("average_hunter_1").SetRelationship( "player D_HT 5")
        Find("average_hunter_2").SetRelationship( "player D_HT 5")

#------------------------------------------Ultra hunter scene end--------------------------------------
#--------------------------------------Ultra hunter cast holylights------------------------------------------
#ULTRA HUNTER: casts holy lights
def UhunterCastHolylights():
    pc=__main__.FindPlayer()
    uh1 = Find("ultra_hunter_1")
    if(G.uhunter_1_dead == 1):
        pc=__main__.FindPlayer()
        pc.Bloodloss(0)
    else:
	__main__.ScheduleTask(0.1,"UhunterCastHolylights1()")

def UhunterCastHolylights1():
    uh1 = Find("ultra_hunter_1")
    uh1.PlayDialogFile("character/boss/ulta_hunter_1/holy_lights2.wav")
    Find("uh_cross").ScriptUnhide()
    Find("uhunter_1_cast_holylights").BeginSequence()
    __main__.ScheduleTask(2.80,"UhunterCastHolylights4()")
    if(not G.Player_Ashes_Form == 1):
        __main__.ScheduleTask(0.1,"UhunterCastHolylights2()")

def UhunterCastHolylights2():
    Find("pc_holylights_1").BeginSequence()
    __main__.ScheduleTask(0.1,"UhunterCastHolylights2a()")

def UhunterCastHolylights2a():
    Find("pc_holylights_1a").BeginSequence()
    __main__.ScheduleTask(2.75,"UhunterCastHolylights3()")

def UhunterCastHolylights3():
    Find("pc_holylights_2").BeginSequence()
    #__main__.ScheduleTask(2.5,"UhunterCastHolylights4()")

def UhunterCastHolylights4():
    Find("uh_cross").ScriptHide()
    pevents = __main__.FindEntitiesByClass("events_player")
    pevents[0].RemoveControllerNPC()

#------------------------------------------Ultra hunter casts holy lights end--------------------------------------
#-------------------------------TREMERE ANTITRIBU--------------------------------------------
#TREMERE ANTITRIBU: tremere antitribu cast blood purge...       
def TremereAntitribuCast():
    pc=__main__.FindPlayer()
    tremerea1 = Find("tremere_antitribu_1")
    if(G.tremere_antitribu_1_anger == 1):
        Find("tremere_antitribu_blood_purge_1").BeginSequence()
	__main__.ScheduleTask(0.1,"TremereAntitribuCastBloodPurge1()")

def TremereAntitribuCastBloodPurge1():
    Find("sound5_tremere_antitribu_1").PlaySound() 
    Find("sound6_tremere_antitribu_1").PlaySound()
    __main__.ScheduleTask(3.05,"TremereAntitribuCastBloodPurge4()")
    if(not G.Player_Ashes_Form == 1):
        __main__.ScheduleTask(0.1,"TremereAntitribuCastBloodPurge2()")

def TremereAntitribuCastBloodPurge2():
    Find("tremere_antitribu_blood_purge_start").BeginSequence()
    __main__.FindPlayer().Bloodloss(2)
    __main__.ScheduleTask(4.0,"TremereAntitribuCastBloodPurge3()")

def TremereAntitribuCastBloodPurge3():
    Find("tremere_antitribu_blood_purge_end").BeginSequence()

def TremereAntitribuCastBloodPurge4():
    __main__.ScheduleTask(5.0,"TremereAntitribuspellhelper1()")
    pevents = __main__.FindEntitiesByClass("events_player")
    pevents[0].RemoveControllerNPC()

#-----------------
#TREMERE ANTITRIBU: tremere antitribu cast theft of vitae....
def TremereAntitribuTheftofVitae():
    pc=__main__.FindPlayer()
    samedi1 = Find("samedi_1")
    if(G.tremere_antitribu_1_dead == 1):
        __main__.FindPlayer().Bloodloss(0)
    else:
        Find("tremere_antitribu_cast_1").BeginSequence()
	__main__.ScheduleTask(0.1,"TremereAntitribuCasthelper1()")

def TremereAntitribuCasthelper1():
    Find("sound1_tremere_antitribu_1").PlaySound()
    Find("sound2_tremere_antitribu_1").PlaySound()
    if(G.Player_Ashes_Form == 1):
        __main__.ScheduleTask(0.15,"TremereAntitribuCasthelper4()")
    else:
        __main__.ScheduleTask(0.1,"TremereAntitribuCasthelper2()")

def TremereAntitribuCasthelper2():
    __main__.FindPlayer().Bloodloss(3)
    consoleutil.console("vdmg 20")
    Find("tremere_antitribu_theft_start").BeginSequence()
    __main__.ScheduleTask(3.25,"TremereAntitribuCasthelper3()")

def TremereAntitribuCasthelper3():
    Find("tremere_antitribu_theft_end").BeginSequence()

def TremereAntitribuCasthelper4():
    pevents = __main__.FindEntitiesByClass("events_player")
    pevents[0].RemoveControllerNPC()

#-----------------
#TREMERE ANTITRIBU: tremere antitribu cast blood shield....
def TremereAntitribuspellhelper1():
    Find("tremere_antitribu_blood_shield_1").BeginSequence()
    __main__.ScheduleTask(1.05,"TremereAntitribuspellhelper2()")

def TremereAntitribuspellhelper2():
    tremer1 = Find("tremere_antitribu_1")
    castsound4 = Find("sound4_tremere_antitribu_1")
    castsound4.PlaySound()
    tremer1.MakeInvincible(1)
    tremer1.SetModel("models/character/npc/common/tremere_antitribu/tremere_antitribu_blood_shield.mdl")
    __main__.ScheduleTask(5.0,"TremereAntitribuspellhelper3()")

def TremereAntitribuspellhelper3():
    tremer1 = Find("tremere_antitribu_1")
    tremer1.MakeInvincible(0)
    tremer1.SetModel("models/character/npc/common/tremere_antitribu/tremere_antitribu.mdl")
    __main__.ScheduleTask(5.0,"TremereAntitribuTheftofVitae()")

#-------------------------------TREMERE ANTITRIBU END--------------------------------------------
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
#--------------------------------------Ultra hunter 2 cast holylights (ash sewer)------------------------------------------
#(ash sewer) ULTRA HUNTER2: casts holy lights
def Uhunter2CastHolylights():
    uh2 = Find("ultra_hunter_2")
    if(G.uhunter_2_dead == 1):
	return
    else:
        uh2.MakeInvincible(1)
	__main__.ScheduleTask(0.25,"Uhunter2CastHolylights1()")

def Uhunter2CastHolylights1():
    Find("ultra_hunter_2").PlayDialogFile("character/boss/ulta_hunter_1/holy_lights3.wav")
    Find("uh2_cross").ScriptUnhide()
    Find("uhunter_2_cast_holylights").BeginSequence()
    __main__.ScheduleTask(0.1,"Uhunter2CastHolylights2()")

def Uhunter2CastHolylights2():
    __main__.ScheduleTask(0.1,"Uhunter2CastHolylights3a()")
    __main__.ScheduleTask(1.55,"Uhunter2CastHolylights4a()")
    if(not G.Player_Ashes_Form == 1):
        __main__.ScheduleTask(0.1,"Uhunter2CastHolylights3()")

def Uhunter2CastHolylights3():
    Find("pc_uh2_1").BeginSequence()
    consoleutil.console("vdmg 15")
    __main__.ScheduleTask(1.25,"Uhunter2CastHolylights4()")

def Uhunter2CastHolylights4():
    Find("pc_uh2_2").BeginSequence()
    #__main__.ScheduleTask(0.25,"Uhunter2CastHolylights4a()")

def Uhunter2CastHolylights4a():
    Find("ultra_hunter_2").MakeInvincible(0)
    Find("uh2_cross").ScriptHide()
    pevents = __main__.FindEntitiesByClass("events_player")
    pevents[0].RemoveControllerNPC()

def Uhunter2CastHolylights3a():
    if(not G.Ash_Dead == 1):
        Find("ash_holylights").BeginSequence()
        Find("Ash").TakeDamage(50)

def Uhunter2Dead():
    __main__.FindPlayer().AwardExperience("Hunters02")

#------------------------------------------Ultra hunter 2 casts holy lights end (ash sewer)--------------------------------------
#------------------------------------------RED SPOT robbery in CQM ( burgermeister01 )--------------------------------------
#RED SPOT: Used to setup the red spot robbery in CQM.
def setupRobbery():
    robbery_npcs = ["robber1","robber2","robber3","robbery_victim"]
    clerk = Find("Slater")
           
    if(not clerk or __main__.FindPlayer().GetQuestState("afoot") > 1): return
         
    __main__.FindPlayer().SetQuest("afoot",1)
    world = Find("world")
    
    if(world):
        world.SetCopWaitArea(0)    
    for npc in robbery_npcs:
        ent = Find(npc)
        if(ent):
            ent.ScriptUnhide()		
    ent = Find("Spicoli")  
    if(ent):
        ent.ScriptHide()    
    ent = Find("Chick")
    if(ent):
        ent.ScriptHide()   
    ent = Find("spicoli_float_timer")
    if(ent):
        ent.Disable()

#RED SPOT: tweak robbers params
def robbersTweak():
    robbers = ["robber1","robber2","robber3"]  
    for robber in robbers:
        r = Find(robber)   
        if(r): 
	    r.SetRelationship("player D_HT 5")
            r.TweakParam("vision 400")
            r.TweakParam("hearing 50")
        
#RED SPOT: Used in the red spot robbery for CQM
def robbersAttack():
    robbers = ["robber1","robber2","robber3"]  
    for robber in robbers:
        r = Find(robber)   
        if(r): r.SetRelationship("player D_HT 5")
    r = Find("robber3")
    if(r):
        r.SetRelationship("robbery_victim D_HT 10")    
    seqs = ["chick_cower", "slater_cower"]
    for seq in seqs:
        s = __main__.Find(seq) 
        if(s):
            s.BeginSequence()       
      
def robberTally():
    G.redspot_robbery_death = G.redspot_robbery_death + 1 
    if(G.redspot_robbery_death == 3):
        if(not __main__.IsDead("robbery_victim")):
            __main__.FindPlayer().SetQuest("afoot",2)
        else:
            __main__.FindPlayer().SetQuest("afoot",3)
        world = Find("world")
    	G.robbery_success = 1
        if(world): 
            world.SetCopWaitArea(1)  
        seqs = ["chick_cower", "slater_cower"]
	for seq in seqs:
	    s = __main__.Find(seq)
	    if(s):
		s.Kill()

#RED SPOT: Used as part of the cut scene. 
def moveRobbery():
    person = __main__.Find("robbery_victim")
    if(person):
        person.SetOrigin((52.156269073486328,-383.88790893554687,0.03125))
        person.SetAngles((0.0,6.1468505859375,0.0))
    person = __main__.Find("robber3")
    if(person):
        person.SetOrigin((98.30377197265625, -378.91793823242187, 0.03125))
        person.SetAngles((0.0, -171.826171875, 0.0))  
    person = __main__.Find("robber2")
    if(person):
        person.SetAngles((0.0, -129.078369140625, 0.0))
    
#RED SPOT: Gets rid of the robbers and the hostage.
def robberyCleanUp():
    if(__main__.FindPlayer().GetQuestState("afoot") > 0):
        ents = ["robbery_victim", "robber1", "robber2", "robber3"]
        for ent in ents:
            e = __main__.Find(ent) 
            if(e):
                e.Kill()
#-------------------------------------------------------------------------------------------
#LUCKYSTAR: battle with hunters on uh-1c
def HunterStart():
    if(G.hunters_riders_dead == 1 or G.battle_run == 1):
	return
    else:
        Find("world").SetSafeArea(0)
        Find("start_uh_relay").Trigger()

def HunterCheck():
    G.Hunter_Death = G.Hunter_Death + 1
    
    if(G.Hunter_Death == 3):
       G.hunters_riders_dead = 1
       #Find("hunter_4").Kill()
       Find("uh_sound").StopSound()
       Find("uh_vf").StopSound()
       Find("uh_explosion").PlaySound()
       Find("fx_boom").TurnOn()
       Find("uh1c_carcas").ScriptHide()
       Find("uh1c_carcas1").ScriptHide()
       Find("uh1c_carcas2").ScriptHide()
       Find("uh1c_carcas3").ScriptHide()
       Find("uh1c_carcas4").ScriptHide()
       Find("uh1c_view2").ScriptUnhide()
       Find("uh_explosion_start").Explode()
       __main__.ScheduleTask(0.5,"UhBoom()")
       if(not G.pilot_dead == 1):
          Find("hunter_4").Kill()

def UhBoom():
       Find("uh1c2_move").MoveForwards()
       __main__.ScheduleTask(3.5,"UhBoom1()")

def UhBoom1():
       __main__.FindPlayer().AwardExperience("Rid01")
       Find("world").SetSafeArea(1)
       __main__.ScheduleTask(1.5,"UhBoom2()")

def UhBoom2():
       Find("uh_explosion").StopSound()

#------------------------------------------------------------------
## ROMERO PROSTITUTE: Unfinished Ho rest prostitute unless going to cemetery (on trig change level), changed by wesp, RobinHood70
def unfinishedHo( s = "") :
    print ( "*************** Reseting Prostitutes ***************" )
    pc = __main__.FindPlayer()
    if ( s == "cemetery" and G.Romero_Whore == 2 ):
        prostitutes = Finds("Prostitute_*")
        for prostitute in prostitutes:
            if(prostitute.classname != "filter_activator_name"):
                if ( prostitute.IsFollowerOf( pc )):
                    if ( "models/character/npc/common/prostitute/prostitute_1/prostitute_1.mdl" == prostitute.GetModelName() ):
                        print ( "**************************** Is Blond ***********************************" )
                        G.Blondie = 1
                    else:
                        print ( "**************************** Is Not Blond ***********************************" )
                prostitute.SetFollowerBoss( "" )

#----------------------------------------------------------------------------------
#NET CAFE: tzimisce punks explode
def boom1():
    xyz1 = Find("tzpunk1").GetOrigin()
    Find("Explosion1").SetOrigin(xyz1)
    __main__.ScheduleTask(0.1,"boom1a()")
    __main__.ScheduleTask(0.05,"boom1b()")

def boom1a():
    Find("Explosion1").Explode()

def boom1b():
    punkBody1a=__main__.CreateEntityNoSpawn("prop_physics",Find("tzpunk1").GetOrigin(),Find("tzpunk1").GetAngles())
    punkBody1a.SetName("punkBody1a")
    punkBody1a.SetModel("models/gibs/hgibslleg_prop.mdl")
    __main__.CallEntitySpawn(punkBody1a)
    punkBody1b=__main__.CreateEntityNoSpawn("prop_physics",Find("tzpunk1").GetOrigin(),Find("tzpunk1").GetAngles())
    punkBody1b.SetName("punkBody1b")
    punkBody1b.SetModel("models/gibs/hgibslarm_prop.mdl")
    __main__.CallEntitySpawn(punkBody1b)
    punkBody1c=__main__.CreateEntityNoSpawn("prop_physics",Find("tzpunk1").GetOrigin(),Find("tzpunk1").GetAngles())
    punkBody1c.SetName("punkBody1c")
    punkBody1c.SetModel("models/gibs/hgibsskull_prop.mdl")
    __main__.CallEntitySpawn(punkBody1c)
    punkBody1d=__main__.CreateEntityNoSpawn("prop_physics",Find("tzpunk1").GetOrigin(),Find("tzpunk1").GetAngles())
    punkBody1d.SetName("punkBody1d")
    punkBody1d.SetModel("models/gibs/hgibstorso_prop.mdl")
    __main__.CallEntitySpawn(punkBody1d)

#----------------
def boom2():
    xyz2 = Find("tzpunk2").GetOrigin()
    Find("Explosion2").SetOrigin(xyz2)
    __main__.ScheduleTask(0.1,"boom2a()")
    __main__.ScheduleTask(0.05,"boom2b()")

def boom2a():
    Find("Explosion2").Explode()

def boom2b():
    punkBody2a=__main__.CreateEntityNoSpawn("prop_physics",Find("tzpunk2").GetOrigin(),Find("tzpunk2").GetAngles())
    punkBody2a.SetName("punkBody2a")
    punkBody2a.SetModel("models/gibs/hgibslleg_prop.mdl")
    __main__.CallEntitySpawn(punkBody2a)
    punkBody2b=__main__.CreateEntityNoSpawn("prop_physics",Find("tzpunk2").GetOrigin(),Find("tzpunk2").GetAngles())
    punkBody2b.SetName("punkBody2b")
    punkBody2b.SetModel("models/gibs/hgibslarm_prop.mdl")
    __main__.CallEntitySpawn(punkBody2b)
    punkBody2c=__main__.CreateEntityNoSpawn("prop_physics",Find("tzpunk2").GetOrigin(),Find("tzpunk2").GetAngles())
    punkBody2c.SetName("punkBody2c")
    punkBody2c.SetModel("models/gibs/hgibsskull_prop.mdl")
    __main__.CallEntitySpawn(punkBody2c)
    punkBody2d=__main__.CreateEntityNoSpawn("prop_physics",Find("tzpunk2").GetOrigin(),Find("tzpunk2").GetAngles())
    punkBody2d.SetName("punkBody2d")
    punkBody2d.SetModel("models/gibs/hgibstorso_prop.mdl")
    __main__.CallEntitySpawn(punkBody2d)

#----------------
def boom3():
    xyz3 = Find("tzpunk3").GetOrigin()
    Find("Explosion3").SetOrigin(xyz3)
    __main__.ScheduleTask(0.1,"boom3a()")
    __main__.ScheduleTask(0.05,"boom3b()")

def boom3a():
    Find("Explosion3").Explode()

def boom3b():
    punkBody3a=__main__.CreateEntityNoSpawn("prop_physics",Find("tzpunk3").GetOrigin(),Find("tzpunk3").GetAngles())
    punkBody3a.SetName("punkBody3a")
    punkBody3a.SetModel("models/gibs/hgibslleg_prop.mdl")
    __main__.CallEntitySpawn(punkBody3a)
    punkBody3b=__main__.CreateEntityNoSpawn("prop_physics",Find("tzpunk3").GetOrigin(),Find("tzpunk3").GetAngles())
    punkBody3b.SetName("punkBody3b")
    punkBody3b.SetModel("models/gibs/hgibslarm_prop.mdl")
    __main__.CallEntitySpawn(punkBody3b)
    punkBody3c=__main__.CreateEntityNoSpawn("prop_physics",Find("tzpunk3").GetOrigin(),Find("tzpunk3").GetAngles())
    punkBody3c.SetName("punkBody3c")
    punkBody3c.SetModel("models/gibs/hgibsskull_prop.mdl")
    __main__.CallEntitySpawn(punkBody3c)
    punkBody3d=__main__.CreateEntityNoSpawn("prop_physics",Find("tzpunk3").GetOrigin(),Find("tzpunk3").GetAngles())
    punkBody3d.SetName("punkBody3d")
    punkBody3d.SetModel("models/gibs/hgibstorso_prop.mdl")
    __main__.CallEntitySpawn(punkBody3d)

#----------------
def boom4():
    xyz4 = Find("tzpunk4").GetOrigin()
    Find("Explosion4").SetOrigin(xyz4)
    __main__.ScheduleTask(0.1,"boom4a()")
    __main__.ScheduleTask(0.05,"boom4b()")

def boom4a():
    Find("Explosion4").Explode()

def boom4b():
    punkBody4a=__main__.CreateEntityNoSpawn("prop_physics",Find("tzpunk4").GetOrigin(),Find("tzpunk4").GetAngles())
    punkBody4a.SetName("punkBody4a")
    punkBody4a.SetModel("models/gibs/hgibslleg_prop.mdl")
    __main__.CallEntitySpawn(punkBody4a)
    punkBody4b=__main__.CreateEntityNoSpawn("prop_physics",Find("tzpunk4").GetOrigin(),Find("tzpunk4").GetAngles())
    punkBody4b.SetName("punkBody4b")
    punkBody4b.SetModel("models/gibs/hgibslarm_prop.mdl")
    __main__.CallEntitySpawn(punkBody4b)
    punkBody4c=__main__.CreateEntityNoSpawn("prop_physics",Find("tzpunk4").GetOrigin(),Find("tzpunk4").GetAngles())
    punkBody4c.SetName("punkBody4c")
    punkBody4c.SetModel("models/gibs/hgibsskull_prop.mdl")
    __main__.CallEntitySpawn(punkBody4c)
    punkBody4d=__main__.CreateEntityNoSpawn("prop_physics",Find("tzpunk4").GetOrigin(),Find("tzpunk4").GetAngles())
    punkBody4d.SetName("punkBody4d")
    punkBody4d.SetModel("models/gibs/hgibstorso_prop.mdl")
    __main__.CallEntitySpawn(punkBody4d)

#----------------
def boom5():
    xyz5 = Find("tzpunk5").GetOrigin()
    Find("Explosion5").SetOrigin(xyz5)
    __main__.ScheduleTask(0.1,"boom5a()")
    __main__.ScheduleTask(0.05,"boom5b()")

def boom5a():
    Find("Explosion5").Explode()

def boom5b():
    punkBody5a=__main__.CreateEntityNoSpawn("prop_physics",Find("tzpunk5").GetOrigin(),Find("tzpunk5").GetAngles())
    punkBody5a.SetName("punkBody5a")
    punkBody5a.SetModel("models/gibs/hgibslleg_prop.mdl")
    __main__.CallEntitySpawn(punkBody5a)
    punkBody5b=__main__.CreateEntityNoSpawn("prop_physics",Find("tzpunk5").GetOrigin(),Find("tzpunk5").GetAngles())
    punkBody5b.SetName("punkBody5b")
    punkBody5b.SetModel("models/gibs/hgibslarm_prop.mdl")
    __main__.CallEntitySpawn(punkBody5b)
    punkBody5c=__main__.CreateEntityNoSpawn("prop_physics",Find("tzpunk5").GetOrigin(),Find("tzpunk5").GetAngles())
    punkBody5c.SetName("punkBody5c")
    punkBody5c.SetModel("models/gibs/hgibsskull_prop.mdl")
    __main__.CallEntitySpawn(punkBody5c)
    punkBody5d=__main__.CreateEntityNoSpawn("prop_physics",Find("tzpunk5").GetOrigin(),Find("tzpunk5").GetAngles())
    punkBody5d.SetName("punkBody5d")
    punkBody5d.SetModel("models/gibs/hgibstorso_prop.mdl")
    __main__.CallEntitySpawn(punkBody5d)

#----------------
def boom6():
    xyz6 = Find("tzpunk6").GetOrigin()
    Find("Explosion6").SetOrigin(xyz6)
    __main__.ScheduleTask(0.1,"boom6a()")
    __main__.ScheduleTask(0.05,"boom6b()")

def boom6a():
    Find("Explosion6").Explode()

def boom6b():
    punkBody6a=__main__.CreateEntityNoSpawn("prop_physics",Find("tzpunk6").GetOrigin(),Find("tzpunk6").GetAngles())
    punkBody6a.SetName("punkBody6a")
    punkBody6a.SetModel("models/gibs/hgibslleg_prop.mdl")
    __main__.CallEntitySpawn(punkBody6a)
    punkBody6b=__main__.CreateEntityNoSpawn("prop_physics",Find("tzpunk6").GetOrigin(),Find("tzpunk6").GetAngles())
    punkBody6b.SetName("punkBody6b")
    punkBody6b.SetModel("models/gibs/hgibslarm_prop.mdl")
    __main__.CallEntitySpawn(punkBody6b)
    punkBody6c=__main__.CreateEntityNoSpawn("prop_physics",Find("tzpunk6").GetOrigin(),Find("tzpunk6").GetAngles())
    punkBody6c.SetName("punkBody6c")
    punkBody6c.SetModel("models/gibs/hgibsskull_prop.mdl")
    __main__.CallEntitySpawn(punkBody6c)
    punkBody6d=__main__.CreateEntityNoSpawn("prop_physics",Find("tzpunk6").GetOrigin(),Find("tzpunk6").GetAngles())
    punkBody6d.SetName("punkBody6d")
    punkBody6d.SetModel("models/gibs/hgibstorso_prop.mdl")
    __main__.CallEntitySpawn(punkBody6d)

#--------------------------------------------------------
#NETCAFE: unlocks netcafe office door if key present
def checkForPasskeyNetcafeOffice():
    pc = __main__.FindPlayer()
    if ( pc.HasItem("item_g_vampyr_apocrypha") ):
        Find("office_doorknob_2").Unlock()
        Find("Passkey_Netcafe_Office_check").Disable()

def OpenNetcafeOfficeDoor():
    Find("logic_enable_combat_state").Trigger()
    __main__.FindPlayer().RemoveItem("item_g_vampyr_apocrypha")

#--------------------------------------------------------
#HUB: unhide sabbat taxi and driver if pc join sabbat
def SabbatJoinCheck():
    pc = __main__.FindPlayer()
    if ( G.Player_Sabbat_Join == 1 ):
        Find("sabbat_cabbie_relay").Trigger()

#--------------------------------------------------------

print "hollywood levelscript loaded"
