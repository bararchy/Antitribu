print "loading chinatown level script"
#function's comments indicate what map they are called on
import __main__

from __main__ import G

__main__.Level = __name__

Find = __main__.FindEntityByName
Finds = __main__.FindEntitiesByName

import consoleutil

RandomLine = __main__.RandomLine


# added by wesp
def civilianDeath():
    pc = __main__.FindPlayer()
    if(pc.humanity >= 3):
        pc.HumanityAdd( -1 )

# added by wesp
#KAMIKAZE ZEN: Turns timer off and light on
def checkTimer():
    timer = Find("virus_timer")
    power = Find("poweron")
    if (G.Shubs_Act == 4):
        power.Trigger()
        if timer: timer.Kill()

#CHINATOWN HUB:  activate the Ramen Shop events
def ramenSetup():
    fireEvents = Find("ramen_events")
    if (G.WongHo_Kiki == 1):
        fireEvents.Trigger()

#CHINATOWN HUB: Gary calls pay phone outside Fu syndicate
def SetGaryPhone():
    if G.Story_State == 55 and G.Gary_Know == 0:
        logic = Find("logic_garyphone")
        logic.Trigger()
    else:
        phone = Find("Garyphone")
        phone.WillTalk(0)

#CHINATOWN HUB: set yukie next to fishmarket
def SetYukie():
    state = __main__.FindPlayer().GetQuestState("Yukie")
    yukie = Find("Yukie")
    if yukie:
        if state == 4:
            yukie.ScriptUnhide()
        elif state > 4:
            yukie.Kill()
        else:
            yukie.ScriptHide()

#CHINATOWN HUB: Set Ricky running away with Kiki
def SetTongKiki():
    if G.Ming_Met == 1:
        logic = Find("logic_tongkiki")
        if logic: logic.Trigger()
        cop = Find("beat_cop")
        if cop: cop.ScriptHide()
    else:
        cop = Find("beat_cop")
        if cop: cop.ScriptUnhide()

#CHINATOWN HUB: Set Glaze doors
def SetGlaze():
    if __main__.FindPlayer().GetQuestState("Gangster") > 1:
        fakes = Finds("glaze_keypad_fake")
        for fake in fakes:
            fake.Kill()
        keypads = Finds("glaze_keypad")
        for keypad in keypads:
            keypad.ScriptUnhide()

#CHINATOWN HUB: Set Lotus Blossum doors
def SetLotusBlossum():
    if __main__.FindPlayer().GetQuestState("Kiki") == 1:
        door = Find("lotusdra")
        door.Unlock()
        door = Find("lotusdrb")
        door.Unlock()
        door = Find("lotusdrc")
        door.Unlock()

#CHINATOWN HUB: Set Fishmarket doors
def SetFishmarket():
    if __main__.FindPlayer().GetQuestState("Yukie") == 4:
        door = Find("fishmarket_door")
        door.Unlock()
    else:
        door = Find("fishmarket_door")
        door.Lock()

#CHINATOWN HUB: Set Zhaos doors, changed by wesp
def SetZhaos():
    pc = __main__.FindPlayer()
    state = pc.GetQuestState("Gangster")
    knob = Find("outside_door")
    if (state == 1):
        knob.Unlock()
    elif (state == 2):
        if G.Zhao_Dead == 1:
            pc.SetQuest("Gangster", 3)
        else:
            pc.SetQuest("Gangster", 4)
##        knob.Lock()

#CHINATOWN HUB: Set White Cloud doors, changed by Wesp
def SetWhiteCloud():
##    if __main__.FindPlayer().GetQuestState("Kiki") == 3:
    door = Find("whiteclouddr")
    door.Unlock()

#CHINATOWN HUB: UnsetCabbie
def UnsetCabbie():
    # Changed for CompMod
    # if (__main__.IsClan(__main__.FindPlayer(), "Nosferatu")):
    if 5 == __main__.G._pcinfo["clan"]:
        logic = Find("logic_kill_cab")
        if logic: logic.Trigger()
        map = Find("sewer_map")
        if map: map.Unlock()

#CHINATOWN HUB: Set doors
def SetHubDoors():
    SetGlaze()
    SetLotusBlossum()
    SetFishmarket()
    SetZhaos()
    SetWhiteCloud()
    UnsetCabbie()
    # Updated by CompMod
    if G.Shubs_Email_Read == 4:
        pc = __main__.FindPlayer()
        if pc.GetQuestState("Mitnick") == 8:
            if not pc.HasItem("item_k_shrekhub_four_key"):
                pc.GiveItem("item_k_shrekhub_four_key")

#CHINATOWN HUB: Set quest states for Ji's death, changed by wesp
def SetJiDeathQuestState():
    G.Ji_Killed = 1
    pc = __main__.FindPlayer()
    state = pc.GetQuestState("Hitman")
    if G.Lu_Offer > 0 and state < 7 and G.Lu_Killed == 0:
        pc.SetQuest("Hitman", 4)
    elif state > 0 and G.Lu_Killed == 1 and state < 7:
        pc.SetQuest("Hitman", 9)

    # spawn quest item
    ji = Find("ji")
    center = ji.GetCenter()
    point = (center[0] - 25, center[1] - 25, center[2])
    key = __main__.CreateEntityNoSpawn("item_k_hitman_ji_key", point, (0,0,0))
    key.SetName("ji_key")
    __main__.CallEntitySpawn(key)
    sparklies = __main__.CreateEntityNoSpawn("inspection_node", point, (0,0,0))
    sparklies.SetParent("ji_key")
    __main__.CallEntitySpawn(sparklies)

#CHINATOWN HUB:  Open Zhaos and set state of quest.
def ogGangsterQuestState():
    pc = __main__.FindPlayer()
    state = pc.GetQuestState("Gangster")
    knob = Find("zhao_doorknob")
    if (state == 1):
        knob.Unlock()
    elif (state == 2):
##        pc.SetQuest("Gangster", 3), removed by wesp
        knob.Lock()

#CLOUD: Ox quest states, Ox.OnDeath, changed by wesp
def SetOxDeathQuestState():
    pc = __main__.FindPlayer()
    state = pc.GetQuestState("Ox")
    if state > 0 and state < 4:
        pc.SetQuest("Ox", 6)
    state = pc.GetQuestState("Eyes")
    if state > 0 and state < 3:
        pc.SetQuest("Eyes", 4)

#FISHMARKET: hide yukie after battle is over
def OnFishmarketEnter():
    if __main__.FindPlayer().GetQuestState("Yukie") > 4:
        Find("Relay_Clean_Yukie").Trigger()

#FISHMARKET: float yukie line during combat
def YukieFloat(n):
    yukie = Find("Yukie")
    if yukie: yukie.PlayDialogFile("Character/dlg/Chinatown/yukie/line%d_col_e.mp3" %n)

#GLAZE: synch up upper level patrolling guards
def WaitForPartner(i):
    g1 = Find("gangster_up_1")
    g2 = Find("gangster_up_2")

    if (not g1):
        G.Glaze_Guard1 = 1
    elif (not g2):
        G.Glaze_Guard2 = 1

    if (i == 1):
        G.Glaze_Guard1 = 1
    elif (i == 2):
        G.Glaze_Guard2 = 1

    if (G.Glaze_Guard1 and G.Glaze_Guard2):
        g1 = Find("gangster_up_1")
        g2 = Find("gangster_up_2")
        g1.SetupPatrolType("2 0 FOLLOW_PATROL_PATH_WALK")
        g2.SetupPatrolType("2 0 FOLLOW_PATROL_PATH_WALK")
        g1.FollowPatrolPath("A1 A2 A3 A4")
        g2.FollowPatrolPath("A3 A4 A1 A2")

        G.Glaze_Guard1 = 0
        G.Glaze_Guard2 = 0

#GLAZE: control access to upstairs area
def ControlUpstairsAccess():
    if (not G.Johnny_Permission):
        deny = Find("logic_deny_access")
        deny.Trigger()

#GLAZE: set upstairs guards to hate the player
def SetUpstairsGuardsHate():
    t = Find("logic_set_guards_hate")
    t.Trigger()

#GLAZE: set upstairs guards to not hate the player
def SetUpstairsGuardsNeutral():
    t = Find("logic_set_guards_neutral")
    t.Trigger()

#GLAZE: check to see if guards should hate player if upstairs, changed by wesp
def CheckGoingUpstairs():
    if (not G.Johnny_Permission):
        SetUpstairsGuardsHate()
    else:
        pc = __main__.FindPlayer()
        if G.Glaze_Kill == 0:
            pc.AwardExperience("Johnny02")

#GLAZE: if player is going back downstairs, set upstairs back to
#       neutral if undetected/combat not begun
def CheckGoingDownstairs():
    SetUpstairsGuardsNeutral()

#GLAZE: enable scripting in office if valid.
def EnableOfficeScripts():
    if (not G.Johnny_Dead):
        logic = Find("logic_office_pc")
        if logic:
            logic.Enable()
        logic = Find("logic_office_move")
        if logic:
            logic.Enable()

#GLAZE: set gangsters to hate player
def SetGlazeGuysToHate():
    guys = []
    guys.append(Find("Ricky"))
    guys.append(Find("gangster_up_1"))
    guys.append(Find("gangster_up_2"))
    guys.append(Find("Barry_R"))
    guys.append(Find("gangster_bodyguard"))
    guys.append(Find("gangster_bar"))
    guys.append(Find("gangster_2"))
    guys = guys + Finds("gangster") + Finds("gangster_up")

    for guy in guys:
        if guy:
            guy.SetRelationship("player D_HT 5")

#GLAZE: set gangsters to hate player
def SetGlazeGuysToNeutral():
    guys = []
    guys.append(Find("Ricky"))
    guys.append(Find("gangster_up_1"))
    guys.append(Find("gangster_up_2"))
    guys.append(Find("Barry_R"))
    guys.append(Find("gangster_bodyguard"))
    guys.append(Find("gangster_bar"))
    guys.append(Find("gangster_2"))
    guys = guys + Finds("gangster") + Finds("gangster_up")

    for guy in guys:
        if guy:
            guy.SetRelationship("player D_NU 0")

#GLAZE: clear innocents out one at a time.
def KillInnocent():
    guys = Finds("innocent")
    if guys:
       guys[0].FleeAndDie()
    else:
        timer = Find("logic_flee_timer")
        timer.Disable()

#GLAZE: Johnny.WillTalk(1)
def SetJohnnyWillTalk():
    j = Find("Johnny")
    if j:
        j.WillTalk(1)
        s = Find("script_J1")
        s.BeginSequence()

#GLAZE: Scripting for Johnny's dialog, changed by wesp
def JohnnyEndDialog():
##    pc = Find("pc")
##    pc.RemoveControllerNPC()
    npc = Find("Johnny")
    if (npc.times_talked > 1):
        __main__.ScheduleTask(1.0, "__main__.FindEntityByName(\"pc\").RemoveControllerNPC()")
        npc.SetRelationship("player D_HT 5")
    else:
        npc.SetRelationship("player D_HT 5")
        script = Find("script_J2")
        script.BeginSequence()

#GLAZE: set quest state on johnny's death, changed by wesp
def SetJohnnyQuest():
    SetGlazeGuysToHate()
    KillInnocent()
    pc = __main__.FindPlayer()
    if pc.GetQuestState("Johnny") > 0:
        pc.SetQuest("Johnny", 3)

#GLAZE: turn mandarin's tv on
def MandarinTVOn():
    tv = Find("monitor")
    tv.ScriptUnhide()

#RAMEN SHOP:  make the thugs aggresive to Kiki
def thugvsKiki():
    thug_1 = Find("badguy_1")
    thug_2 = Find("badguy_2")
    thug_3 = Find("badguy_3")
    thug_4 = Find("badguy_4")
    kiki = Find("Kiki")
    thug_1.SetRelationship("Kiki D_HT 10")
    thug_2.SetRelationship("Kiki D_HT 10")
    thug_3.SetRelationship("Kiki D_HT 10")
    thug_4.SetRelationship("Kiki D_HT 10")

#RAMEN SHOP:  setup shop depending on flag.
def ramenShop():
    if (G.WongHo_Kiki == 1):
        thug_1 = Find("badguy_1")
        thug_2 = Find("badguy_2")
        thug_3 = Find("badguy_3")
        thug_4 = Find("badguy_4")
        yukie = Find("Yukie")
        thug_1.ScriptUnhide()
        thug_2.ScriptUnhide()
        thug_3.ScriptUnhide()
        thug_4.ScriptUnhide()
        if yukie: yukie.ScriptUnhide()

#RAMEN SHOP: if killed yukie, set yukie quest state, changed by wesp
def onYukieDeath():
    pc = __main__.FindPlayer()
    if(pc.humanity >= 3):
        pc.HumanityAdd( -1 )
    state = pc.GetQuestState("Yukie")
    if state > 0 and state < 5:
        pc.SetQuest("Yukie", 6)

#RAMEN SHOP: if threatening yukie, added by wesp
def onYukieThreat():
    sword = __main__.Find("sword")
    if(G.Yukie_Threat == 1):
        if(sword):
            sword.Kill()

#RAMEN SHOP: if take eyes, set eyes quest
def onTakeEyes():
    pc = __main__.FindPlayer()
    state = pc.GetQuestState("Eyes")
    if state > 0 and state < 2:
        pc.SetQuest("Eyes", 2)

#RAMEN SHOP: check if Yukie is supposed to be in the shop, changed by wesp
def isYukieVisible():
    pc = __main__.FindPlayer()
    state1 = pc.GetQuestState("Eyes")
    state2 = pc.GetQuestState("Yukie")
    yukie = Find("Yukie")
    sword = Find("sword")
    if((state1 > 0 and state1 < 3) or state2 >= 4):
        if yukie: yukie.ScriptHide()
        sword.ScriptHide()
        thug_1 = Find("badguy_1")
        thug_1.ScriptUnhide()
        thug_3 = Find("badguy_3")
        thug_3.ScriptUnhide()
        Find("badguy_2").ScriptUnhide()
    else:
        if yukie: yukie.ScriptUnhide()
        sword.ScriptUnhide()

#RED DRAGON:  call after hostess dialogue.
def callElevator():
    elevator = Find("dragonelevator")
    if (G.Hostess_Elevator == 1):
        elevator.GotoFloor(1)

#RED DRAGON:  float in elevator, added by wesp
def floatElevator():
    hos = Find("Hostess")
    if (G.Story_State < 65 and not __main__.IsDead("Hostess")):
        if (G.Hos_Float == 0):
            if (__main__.IsClan(__main__.FindPlayer(), "Malkavian")):
                hos.PlayDialogFile("Character/dlg/Chinatown/hostess/line1_col_n.mp3")
            else:
                hos.PlayDialogFile("Character/dlg/Chinatown/hostess/line1_col_e.mp3")
        if (G.Hos_Float == 1):
            if (__main__.IsClan(__main__.FindPlayer(), "Malkavian")):
                hos.PlayDialogFile("Character/dlg/Chinatown/hostess/line2_col_n.mp3")
            else:
                hos.PlayDialogFile("Character/dlg/Chinatown/hostess/line2_col_e.mp3")
        if (G.Hos_Float == 2):
            if (__main__.IsClan(__main__.FindPlayer(), "Malkavian")):
                hos.PlayDialogFile("Character/dlg/Chinatown/hostess/line3_col_n.mp3")
            else:
                hos.PlayDialogFile("Character/dlg/Chinatown/hostess/line3_col_e.mp3")
        if (G.Hos_Float == 3):
            if (__main__.IsClan(__main__.FindPlayer(), "Malkavian")):
                hos.PlayDialogFile("Character/dlg/Chinatown/hostess/line4_col_n.mp3")
            else:
                hos.PlayDialogFile("Character/dlg/Chinatown/hostess/line4_col_e.mp3")
        G.Hos_Float = G.Hos_Float + 1

#RED DRAGON:  check for nosferatu, changed by Wesp
def nosCheck():
    hostessMark = Find("hostess_nos")
    if(G.Story_State >= 65):
        host = Find("Hostess")
        if host: host.Kill()
        wong = Find("WongHo")
        if wong: wong.Kill()
    elif (__main__.IsClan(__main__.FindPlayer(), "Nosferatu")):
        hostessMark.BeginSequence()

#RED DRAGON: Set quest states for Lu's death, changed by wesp
def SetLuDeathQuestState():
    G.Lu_Killed = 1
    pc = __main__.FindPlayer()
    state = pc.GetQuestState("Hitman")
    if state > 0 and state < 7 and G.Ji_Killed == 0:
        pc.SetQuest("Hitman", 3)
    elif state > 0 and G.Ji_Killed == 1 and state < 7:
        pc.SetQuest("Hitman", 9)
    if(pc.humanity >= 3 and G.Patch_Plus == 1):
        pc.HumanityAdd(-1)
    # spawn quest item
    lu = Find("lufang")
    center = lu.GetCenter()
    point = (center[0], center[1], center[2] + 20)
    key = __main__.CreateEntityNoSpawn("item_k_hitman_lu_key", point, (0,0,0))
    __main__.CallEntitySpawn(key)
    key.SetName("lu_key")
    sparklies = __main__.CreateEntityNoSpawn("inspection_node", point, (0,0,0) )
    sparklies.SetParent("lu_key")
    __main__.CallEntitySpawn(key)
    __main__.CallEntitySpawn(sparklies)

#RED DRAGON: Make special Hostess for Malkavians
def makeMalkHostess():
    if (__main__.IsClan(__main__.FindPlayer(), "Malkavian")):
        host1 = Find("Hostess")
        if host1: host1.Kill()
        host2 = Find("Hostess2")
        host2.ScriptUnhide()
        host2.SetName("Hostess")

#TSENGS: Turn shelves around, changed by wesp
def tsengsShowGuns():
    shelves = Finds("shelf")
    G.Guns_Tseng = 1
    for shelf in shelves:
        shelf.SetAnimation("showguns")

#TSENGS: Turn shelves around, changed by wesp
def tsengsHideGuns():
    if G.Guns_Tseng == 1:
        shelves = Finds("shelf")
        G.Guns_Tseng = 0
        for shelf in shelves:
            shelf.SetAnimation("hideguns")

#ZHAOS WAREHOUSE: set special case camera shot
def zhaoDramaShot():
    pc = __main__.FindPlayer()
    pc.SetCamera("ZhaoFarHigh")

#ZHAOS WAREHOUSE: set Zhao to hate Tongs
def npcZhaoHateTong():
    zhao     = Find( "Zhao" )
    zhaocam  = Find( "zhao_eye_1" )
    zhaocam2 = Find( "zhao_eye_2" )
    zhaocam3 = Find( "zhao_eye_3" )
    zhaocam4 = Find( "zhao_eye_4" )
    zhaocam5 = Find( "zhao_eye_5" )
    zhaocam6 = Find( "zhao_eye_6" )
    zhaocam7 = Find( "zhao_eye_7" )
    print"hate Zhao"
    zhao.SetRelationship( "Tong_1 D_HT 10")
    zhao.SetRelationship( "Tong_2 D_HT 10")
    zhao.SetRelationship( "Tong_3 D_HT 10")
    zhao.SetRelationship( "Tong_4 D_HT 10")
    zhao.SetRelationship( "Tong_5 D_HT 10")
    zhao.SetRelationship( "Tong_6 D_HT 10")
    zhao.SetRelationship( "Tong_7 D_HT 10")
    zhao.SetRelationship( "Tong_Wave2_1 D_HT 10")
    zhao.SetRelationship( "Tong_Wave2_2 D_HT 10")
    zhao.SetRelationship( "Tong_Wave2_3 D_HT 10")
    zhao.SetRelationship( "Tong_Wave2_4 D_HT 10")
    zhao.SetRelationship( "Tong_Wave2_5 D_HT 10")
    zhao.SetRelationship( "Tong_Wave2_6 D_HT 10")
    print"hate Tong"
    zhaocam.SetRelationship( "Tong_1 D_HT 10")
    zhaocam.SetRelationship( "Tong_2 D_HT 10")
    zhaocam.SetRelationship( "Tong_3 D_HT 10")
    zhaocam.SetRelationship( "Tong_4 D_HT 10")
    zhaocam.SetRelationship( "Tong_5 D_HT 10")
    zhaocam.SetRelationship( "Tong_6 D_HT 10")
    zhaocam.SetRelationship( "Tong_7 D_HT 10")
    zhaocam2.SetRelationship( "Tong_1 D_HT 10")
    zhaocam2.SetRelationship( "Tong_2 D_HT 10")
    zhaocam2.SetRelationship( "Tong_3 D_HT 10")
    zhaocam2.SetRelationship( "Tong_4 D_HT 10")
    zhaocam2.SetRelationship( "Tong_5 D_HT 10")
    zhaocam2.SetRelationship( "Tong_6 D_HT 10")
    zhaocam2.SetRelationship( "Tong_7 D_HT 10")
    zhaocam3.SetRelationship( "Tong_1 D_HT 10")
    zhaocam3.SetRelationship( "Tong_2 D_HT 10")
    zhaocam3.SetRelationship( "Tong_3 D_HT 10")
    zhaocam3.SetRelationship( "Tong_4 D_HT 10")
    zhaocam3.SetRelationship( "Tong_5 D_HT 10")
    zhaocam3.SetRelationship( "Tong_6 D_HT 10")
    zhaocam3.SetRelationship( "Tong_7 D_HT 10")
    zhaocam4.SetRelationship( "Tong_1 D_HT 10")
    zhaocam4.SetRelationship( "Tong_2 D_HT 10")
    zhaocam4.SetRelationship( "Tong_3 D_HT 10")
    zhaocam4.SetRelationship( "Tong_4 D_HT 10")
    zhaocam4.SetRelationship( "Tong_5 D_HT 10")
    zhaocam4.SetRelationship( "Tong_6 D_HT 10")
    zhaocam4.SetRelationship( "Tong_7 D_HT 10")
    zhaocam5.SetRelationship( "Tong_1 D_HT 10")
    zhaocam5.SetRelationship( "Tong_2 D_HT 10")
    zhaocam5.SetRelationship( "Tong_3 D_HT 10")
    zhaocam5.SetRelationship( "Tong_4 D_HT 10")
    zhaocam5.SetRelationship( "Tong_5 D_HT 10")
    zhaocam5.SetRelationship( "Tong_6 D_HT 10")
    zhaocam5.SetRelationship( "Tong_7 D_HT 10")
    zhaocam6.SetRelationship( "Tong_1 D_HT 10")
    zhaocam6.SetRelationship( "Tong_2 D_HT 10")
    zhaocam6.SetRelationship( "Tong_3 D_HT 10")
    zhaocam6.SetRelationship( "Tong_4 D_HT 10")
    zhaocam6.SetRelationship( "Tong_5 D_HT 10")
    zhaocam6.SetRelationship( "Tong_6 D_HT 10")
    zhaocam6.SetRelationship( "Tong_7 D_HT 10")
    zhaocam.SetRelationship( "Tong_Wave2_1 D_HT 10")
    zhaocam.SetRelationship( "Tong_Wave2_2 D_HT 10")
    zhaocam.SetRelationship( "Tong_Wave2_3 D_HT 10")
    zhaocam.SetRelationship( "Tong_Wave2_4 D_HT 10")
    zhaocam.SetRelationship( "Tong_Wave2_5 D_HT 10")
    zhaocam.SetRelationship( "Tong_Wave2_6 D_HT 10")
    zhaocam2.SetRelationship( "Tong_Wave2_1 D_HT 10")
    zhaocam2.SetRelationship( "Tong_Wave2_2 D_HT 10")
    zhaocam2.SetRelationship( "Tong_Wave2_3 D_HT 10")
    zhaocam2.SetRelationship( "Tong_Wave2_4 D_HT 10")
    zhaocam2.SetRelationship( "Tong_Wave2_5 D_HT 10")
    zhaocam2.SetRelationship( "Tong_Wave2_6 D_HT 10")
    zhaocam3.SetRelationship( "Tong_Wave2_1 D_HT 10")
    zhaocam3.SetRelationship( "Tong_Wave2_2 D_HT 10")
    zhaocam3.SetRelationship( "Tong_Wave2_3 D_HT 10")
    zhaocam3.SetRelationship( "Tong_Wave2_4 D_HT 10")
    zhaocam3.SetRelationship( "Tong_Wave2_5 D_HT 10")
    zhaocam3.SetRelationship( "Tong_Wave2_6 D_HT 10")
    zhaocam4.SetRelationship( "Tong_Wave2_1 D_HT 10")
    zhaocam4.SetRelationship( "Tong_Wave2_2 D_HT 10")
    zhaocam4.SetRelationship( "Tong_Wave2_3 D_HT 10")
    zhaocam4.SetRelationship( "Tong_Wave2_4 D_HT 10")
    zhaocam4.SetRelationship( "Tong_Wave2_5 D_HT 10")
    zhaocam4.SetRelationship( "Tong_Wave2_6 D_HT 10")
    zhaocam5.SetRelationship( "Tong_Wave2_1 D_HT 10")
    zhaocam5.SetRelationship( "Tong_Wave2_2 D_HT 10")
    zhaocam5.SetRelationship( "Tong_Wave2_3 D_HT 10")
    zhaocam5.SetRelationship( "Tong_Wave2_4 D_HT 10")
    zhaocam5.SetRelationship( "Tong_Wave2_5 D_HT 10")
    zhaocam5.SetRelationship( "Tong_Wave2_6 D_HT 10")
    zhaocam6.SetRelationship( "Tong_Wave2_1 D_HT 10")
    zhaocam6.SetRelationship( "Tong_Wave2_2 D_HT 10")
    zhaocam6.SetRelationship( "Tong_Wave2_3 D_HT 10")
    zhaocam6.SetRelationship( "Tong_Wave2_4 D_HT 10")
    zhaocam6.SetRelationship( "Tong_Wave2_5 D_HT 10")
    zhaocam6.SetRelationship( "Tong_Wave2_6 D_HT 10")

#ZHAO'S WAREHOUSE: Set the Tongs to hate Zhao
def npcTongHateZhao():
    tong1    = Find( "Tong_1" )
    tong2    = Find( "Tong_2" )
    tong3    = Find( "Tong_3" )
    tong4    = Find( "Tong_4" )
    tong5    = Find( "Tong_5" )
    tong6    = Find( "Tong_6" )
    tong7    = Find( "Tong_7" )
    tongcam1  = Find( "tong_cam_1" )
    tongcam2  = Find( "tong_cam_2" )
    tongcam3  = Find( "tong_cam_3" )
    tongcam4  = Find( "tong_cam_4" )
    print"tongs"
    tong1.SetRelationship( "Zhao D_HT 10" )
    tong2.SetRelationship( "Zhao D_HT 10" )
    tong3.SetRelationship( "Zhao D_HT 10" )
    tong4.SetRelationship( "Zhao D_HT 10" )
    tong5.SetRelationship( "Zhao D_HT 10" )
    tong6.SetRelationship( "Zhao D_HT 10" )
    tong7.SetRelationship( "Zhao D_HT 10" )
    tongcam1.SetRelationship( "Zhao D_HT 10" )
    tongcam2.SetRelationship( "Zhao D_HT 10" )
    tongcam3.SetRelationship( "Zhao D_HT 10" )
    tongcam4.SetRelationship( "Zhao D_HT 10" )

#ZHAO'S WAREHOUSE: Set the Tong wave 2 to hate Zhao
def npcTongWave2HateZhao():
    tong1    = Find( "Tong_Wave2_1" )
    tong2    = Find( "Tong_Wave2_2" )
    tong3    = Find( "Tong_Wave2_3" )
    tong4    = Find( "Tong_Wave2_4" )
    tong5    = Find( "Tong_Wave2_5" )
    tong6    = Find( "Tong_Wave2_6" )
    print"tongs wave2"
    tong1.SetRelationship( "Zhao D_HT 10" )
    tong2.SetRelationship( "Zhao D_HT 10" )
    tong3.SetRelationship( "Zhao D_HT 10" )
    tong4.SetRelationship( "Zhao D_HT 10" )
    tong5.SetRelationship( "Zhao D_HT 10" )
    tong6.SetRelationship( "Zhao D_HT 10" )

#ZHAO'S WAREHOUSE: Make Tongs enter during Zhao dialog
def tongEntrance():
    relayEvents = Find( "tong_1_move")
    print "events triggering"
    relayEvents.Trigger()

#LOTUS: Clean up Kiki quest
def cleanLotus():
    state = __main__.FindPlayer().GetQuestState("Kiki")
    if (state == 2 or state == 3):
        clean = Find("Clean_Level")
        clean.Trigger()

#LOTUS: bad luck farmer quest
def OnLockerEnd():
    locker = Find("locker")
    if locker.HasItem("item_g_badlucktalisman"):
        __main__.FindPlayer().SetQuest("Ox", 2)
        G.Ox_Planted = 1
        logic = Find("logic_locker")
        logic.Trigger()

#LOTUS: bad luck farmer quest
def OnShuDialogEnd():
    shu = Find("Shu")
    shu.WillTalk(0)

    if G.Shu_Sleep == 1:
        shu.Faint()
    elif G.Shu_Frog == 1:
        s = Find("sFrog")
        s.BeginSequence()

#FISHMARKET: Set Quest state for killing Zygaena
def setHunterFive():
    __main__.FindPlayer().SetQuest("Yukie", 5)
    relay = Find( "CleanScripted" )
    relay.Trigger()

#FISHMARKET: Set Quest state for killing Yukie before killing Zygaena
def setHunterSix():
    pc = __main__.FindPlayer()
    state = pc.GetQuestState("Yukie")
    if ( state != 5 ):
        pc.SetQuest("Yukie", 6)

def yukieAttacked():
    print ( "*********************** Check Attacked **************************" )
    yukie = Find( "Yukie" )
    if ( G.Yukie_Leave == 1 ):
        print ( "*********************** Yukie Should Hate **************************" )
        if yukie: yukie.SetRelationship( "player D_HT 5")
    else:
        if yukie: yukie.SetRelationship( "Zygaena D_HT 5")
        print ( "*********************** No Harm **************************" )

#-----------------------------------------------------------------------------------
#TEMPLE 3: Scorpion Check Death
def ScorpionCheckDeath():
    if ( not G.Scorpion_death == 1 ):
        return
    else:
        #Find("kendo_1").TakeDamage(1000)
        Find("scr_*").Disable()
        Find("ScorpionFlamesParticles").TurnOff()
        Find("ScorpionFlamesParticles2").TurnOff()
#------------------------------------------------------------------
#DRAGON: check for start belmont team hunting 
def CheckBelmontHuntStart():
    if (G.BelmontHunt_Start == 1 ):
        return
    else:
        if (G.Kiki_Rescued == 1):
            Find("HuntStart_relay").Trigger()
            G.BelmontHunt_Start = 1

#DRAGON: Belmont commander use explosive_bot 
def BotExplode():
    xyz1 = Find("explosive_bot").GetOrigin()
    Find("BotExplode").SetOrigin(xyz1)
    __main__.ScheduleTask(0.1,"BotExplode1()")

def BotExplode1():
    Find("BotExplode").Explode()

#DRAGON: Belmont commander use explosive_bot 2
def SetExplosiveBot2():
    if (G.Set_Bot2_Dragon == 1 ):
        return
    else:
        Find("commander_set_bot2").BeginSequence()
        Find("Belmont_3").MakeInvincible(1)
        G.Set_Bot2_Dragon = 1
#------
def Bot2Explode():
    xyz2 = Find("explosive_bot2").GetOrigin()
    Find("BotExplode2").SetOrigin(xyz2)
    __main__.ScheduleTask(0.1,"Bot2Explode1()")

def Bot2Explode1():
    Find("BotExplode2").Explode()

#-----------------------------------------------------------------------------------
#LOTUS: Sub zero casts cold wind
def SubZeroCasts():
    if (G.SubZero_Dead == 1):
        #return
        Find("SubZeroDead_relay").Trigger()
    else:
        Find("subzero_cast").BeginSequence()
        __main__.ScheduleTask(1.05,"SubZeroCasts1()")

def SubZeroCasts1():
       consoleutil.console("vdmg 12")

def SubZeroDead():
       Find("SubZeroDead_relay").Trigger()

#-----------------------------------------------------------------------------------
#HUB: check item grenade in car container
def CarTerractCheck():
    container = Find("car3_container")
    if container.HasItem("item_w_grenade_frag"):
	__main__.ScheduleTask(4.0,"CarTerractBoom()")

def CarTerractBoom():
    Find("car3").Break()
#-----------------------------------------------------------------------------------

print "levelscript loaded"
