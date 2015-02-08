print "loading warrens level script"
#function's comments indicate what map they are called on
import __main__

from __main__ import G

__main__.Level = __name__

Find = __main__.FindEntityByName
FindList = __main__.FindEntitiesByName
FindClass = __main__.FindEntitiesByClass

#unlocks drain controls if key present
def checkForPasskey():
    pc = __main__.FindPlayer()
    control = Find("control")
    if ( pc.HasItem("item_g_warrens4_passkey") ):
        control.Unlock()
    #changed by dan_upright 04/12/04
    elif ( pc.CalcFeat("inspection") < 5 ):
        sparklies = __main__.CreateEntityNoSpawn("inspection_node", point, (0, 0, 0))
        sparklies.SetParent("PassKey")
        __main__.CallEntitySpawn(sparklies)
#changes end

#Warrens: checks if mitnicks quest is active, changed by wesp
def mitnicksCheckQuest():
    pc = __main__.FindPlayer()
    state = pc.GetQuestState("Mitnick")
    if (state > 0):
        mitnicks = Find("Mitnick")
        if mitnicks: mitnicks.ScriptHide()
    if G.Patch_Plus == 1:
        durations = Find("Occult_Passive_Durations")
        durationsnode = Find("Occult_Passive_Durationi")
        if durations: durations.ScriptHide()
        if durationsnode: durationsnode.ScriptHide()
        pack = Find("pack")
        packnode = Find("packnode")
        if pack: pack.ScriptUnhide()
        if packnode: packnode.ScriptUnhide()

#Warrens: checks if imalias quest is active
def imaliaCheckQuest():
    pc = __main__.FindPlayer()
    state = pc.GetQuestState("Imalia")
    #changed by dan_upright 09/12/04
    if ( state == 3 and G.Tawni_Dead == 0 and G.Tawni_Boy_Dead == 0 and G.Tawni_Spotted == 0 ):
    #changes end
        newspaper = Find("Imalias_Newspaper")
        if newspaper: newspaper.ScriptUnhide()
    #changed by dan_upright 07/12/04
        highlight = Find("Imalias_Newspaper_Inspect")
        highlight.ScriptUnhide()
    else:
        highlight = Find("Imalias_Newspaper_Inspect")
        if highlight: highlight.ScriptHide()
    #changes end

#Warrens: Fires the relay that unlocks the door in Gary's room
def garyInteractionEnd():
    relay = Find("Relay_Gary_Interaction_End")
    relay.Trigger()

#Gary Scripts
def garyAppear():
    relay = Find( "Gary_Appear" )
    relay.Trigger()

def garyDisappear():
    relay = Find( "Gary_Disappear" )
    relay.Trigger()
    G.Prince_Gary = G.Prince_Gary + 1

#gary camera scripts
def talkGaryLeft():
    gary = Find("Gary")
    gary.SetSoundOverrideEnt("gary_left")
    cam = Find("cam_gary_left")
    cam.StartShot()

def talkGaryRight():
    gary = Find("Gary")
    gary.SetSoundOverrideEnt("gary_right")
    cam = Find("cam_gary_right")
    cam.StartShot()

def talkGaryUp():
    gary = Find("Gary")
    gary.SetSoundOverrideEnt("gary_up")
    cam = Find("cam_gary_up")
    cam.StartShot()

def talkGaryMiddle():
    gary = Find("Gary")
    gary.SetSoundOverrideEnt("gary_middle")
    cam = Find("cam_gary_middle")
    cam.StartShot()

def talkGaryBack():
    gary = Find("Gary")
    gary.SetSoundOverrideEnt("gary_back")
    cam = Find("cam_gary_back")
    cam.StartShot()

#HW_WARRENS_5: Imalia and Mitnick need to turn around in dialog
def ImaliaTurn():
    turn = Find("imalia_turn")
    turn.BeginSequence()

def MitnickTurn():
    turn = Find("mitnick_turn")
    turn.BeginSequence()

#--------------------------------------
#HW_WARRENS_1:  PC setup bomb for explode walkway
def War1spawnBomb():
    bomb = FindClass("item_g_astrolite")
    center = bomb[0].GetOrigin()
    angles = bomb[0].GetAngles()
    bomb[0].Kill()
    bombProp = Find("bomb_prop")
    #bombProp.SetOrigin(center)
    #bombProp.SetAngles(angles)
    bombProp.ScriptUnhide()
#----------------------------------------------------------------------------------
#HW_WARRENS_2: tzimisce punk1 explode
def War2Tzpunk1boom():
    Find("tzpk1_explosion").SetOrigin(Find("tzim_punk1").GetOrigin())
    __main__.ScheduleTask(0.1,"War2Tzpunk1boom1()")
    __main__.ScheduleTask(0.05,"War2Tzpunk1boom2()")

def War2Tzpunk1boom1():
    Find("tzpk1_explosion").Explode()

def War2Tzpunk1boom2():
    punkBody=__main__.CreateEntityNoSpawn("prop_physics",Find("tzim_punk1").GetOrigin(),Find("tzim_punk1").GetAngles())
    punkBody.SetName("punkBody")
    punkBody.SetModel("models/gibs/hgibstorso_prop.mdl")
    __main__.CallEntitySpawn(punkBody)
    punkBodya=__main__.CreateEntityNoSpawn("prop_physics",Find("tzim_punk1").GetOrigin(),Find("tzim_punk1").GetAngles())
    punkBodya.SetName("punkBodya")
    punkBodya.SetModel("models/gibs/hgibslleg_prop.mdl")
    __main__.CallEntitySpawn(punkBodya)
    punkBodyb=__main__.CreateEntityNoSpawn("prop_physics",Find("tzim_punk1").GetOrigin(),Find("tzim_punk1").GetAngles())
    punkBodyb.SetName("punkBodyb")
    punkBodyb.SetModel("models/gibs/hgibslarm_prop.mdl")
    __main__.CallEntitySpawn(punkBodyb)
    punkBodyc=__main__.CreateEntityNoSpawn("prop_physics",Find("tzim_punk1").GetOrigin(),Find("tzim_punk1").GetAngles())
    punkBodyc.SetName("punkBodyc")
    punkBodyc.SetModel("models/gibs/hgibsskull_prop.mdl")
    __main__.CallEntitySpawn(punkBodyc)
#--------------------------------------
#HW_WARRENS_2: tzimisce punk2 explode
def War2Tzpunk2boom():
    Find("tzpk2_explosion").SetOrigin(Find("tzim_punk2").GetOrigin())
    __main__.ScheduleTask(0.1,"War2Tzpunk2boom1()")
    __main__.ScheduleTask(0.05,"War2Tzpunk2boom2()")

def War2Tzpunk2boom1():
    Find("tzpk2_explosion").Explode()

def War2Tzpunk2boom2():
    punk2Body=__main__.CreateEntityNoSpawn("prop_physics",Find("tzim_punk2").GetOrigin(),Find("tzim_punk2").GetAngles())
    punk2Body.SetName("punk2Body")
    punk2Body.SetModel("models/gibs/hgibstorso_prop.mdl")
    __main__.CallEntitySpawn(punk2Body)
    punk2Bodya=__main__.CreateEntityNoSpawn("prop_physics",Find("tzim_punk2").GetOrigin(),Find("tzim_punk2").GetAngles())
    punk2Bodya.SetName("punk2Bodya")
    punk2Bodya.SetModel("models/gibs/hgibslleg_prop.mdl")
    __main__.CallEntitySpawn(punk2Bodya)
    punk2Bodyb=__main__.CreateEntityNoSpawn("prop_physics",Find("tzim_punk2").GetOrigin(),Find("tzim_punk2").GetAngles())
    punk2Bodyb.SetName("punk2Bodyb")
    punk2Bodyb.SetModel("models/gibs/hgibslarm_prop.mdl")
    __main__.CallEntitySpawn(punk2Bodyb)
    punk2Bodyc=__main__.CreateEntityNoSpawn("prop_physics",Find("tzim_punk2").GetOrigin(),Find("tzim_punk2").GetAngles())
    punk2Bodyc.SetName("punk2Bodyc")
    punk2Bodyc.SetModel("models/gibs/hgibsskull_prop.mdl")
    __main__.CallEntitySpawn(punk2Bodyc)

#--------------------------------------
#HW_WARRENS_3: tzimisce punk3 explode
def War3Tzpunk3boom():
    Find("tzpk3_explosion").SetOrigin(Find("tzim_punk3").GetOrigin())
    __main__.ScheduleTask(0.1,"War3Tzpunk3boom1()")
    __main__.ScheduleTask(0.05,"War3Tzpunk3boom2()")

def War3Tzpunk3boom1():
    Find("tzpk3_explosion").Explode()

def War3Tzpunk3boom2():
    punk3Body=__main__.CreateEntityNoSpawn("prop_physics",Find("tzim_punk3").GetOrigin(),Find("tzim_punk3").GetAngles())
    punk3Body.SetName("punk3Body")
    punk3Body.SetModel("models/gibs/hgibstorso_prop.mdl")
    __main__.CallEntitySpawn(punk3Body)
    punk3Bodya=__main__.CreateEntityNoSpawn("prop_physics",Find("tzim_punk3").GetOrigin(),Find("tzim_punk3").GetAngles())
    punk3Bodya.SetName("punk3Bodya")
    punk3Bodya.SetModel("models/gibs/hgibslleg_prop.mdl")
    __main__.CallEntitySpawn(punk3Bodya)
    punk3Bodyb=__main__.CreateEntityNoSpawn("prop_physics",Find("tzim_punk3").GetOrigin(),Find("tzim_punk3").GetAngles())
    punk3Bodyb.SetName("punk3Bodyb")
    punk3Bodyb.SetModel("models/gibs/hgibslarm_prop.mdl")
    __main__.CallEntitySpawn(punk3Bodyb)
    punk3Bodyc=__main__.CreateEntityNoSpawn("prop_physics",Find("tzim_punk3").GetOrigin(),Find("tzim_punk3").GetAngles())
    punk3Bodyc.SetName("punk3Bodyc")
    punk3Bodyc.SetModel("models/gibs/hgibsskull_prop.mdl")
    __main__.CallEntitySpawn(punk3Bodyc)

#--------------------------------------
#HW_WARRENS_3: tzimisce punk4 explode
def War3Tzpunk4boom():
    Find("tzpk4_explosion").SetOrigin(Find("tzim_punk4").GetOrigin())
    __main__.ScheduleTask(0.1,"War3Tzpunk4boom1()")
    __main__.ScheduleTask(0.05,"War3Tzpunk4boom2()")

def War3Tzpunk4boom1():
    Find("tzpk4_explosion").Explode()

def War3Tzpunk4boom2():
    punk4Body=__main__.CreateEntityNoSpawn("prop_physics",Find("tzim_punk4").GetOrigin(),Find("tzim_punk4").GetAngles())
    punk4Body.SetName("punk4Body")
    punk4Body.SetModel("models/gibs/hgibstorso_prop.mdl")
    __main__.CallEntitySpawn(punk4Body)
    punk4Bodya=__main__.CreateEntityNoSpawn("prop_physics",Find("tzim_punk4").GetOrigin(),Find("tzim_punk4").GetAngles())
    punk4Bodya.SetName("punk4Bodya")
    punk4Bodya.SetModel("models/gibs/hgibslleg_prop.mdl")
    __main__.CallEntitySpawn(punk4Bodya)
    punk4Bodyb=__main__.CreateEntityNoSpawn("prop_physics",Find("tzim_punk4").GetOrigin(),Find("tzim_punk4").GetAngles())
    punk4Bodyb.SetName("punk4Bodyb")
    punk4Bodyb.SetModel("models/gibs/hgibslarm_prop.mdl")
    __main__.CallEntitySpawn(punk4Bodyb)
    punk4Bodyc=__main__.CreateEntityNoSpawn("prop_physics",Find("tzim_punk4").GetOrigin(),Find("tzim_punk4").GetAngles())
    punk4Bodyc.SetName("punk4Bodyc")
    punk4Bodyc.SetModel("models/gibs/hgibsskull_prop.mdl")
    __main__.CallEntitySpawn(punk4Bodyc)

#--------------------------------------
#HW_WARRENS_4: tzimisce punk5 explode
def War4Tzpunk5boom():
    Find("tzpk5_explosion").SetOrigin(Find("tzim_punk5").GetOrigin())
    __main__.ScheduleTask(0.1,"War4Tzpunk5boom1()")
    __main__.ScheduleTask(0.05,"War4Tzpunk5boom2()")

def War4Tzpunk5boom1():
    Find("tzpk5_explosion").Explode()

def War4Tzpunk5boom2():
    punk5Body=__main__.CreateEntityNoSpawn("prop_physics",Find("tzim_punk5").GetOrigin(),Find("tzim_punk5").GetAngles())
    punk5Body.SetName("punk5Body")
    punk5Body.SetModel("models/gibs/hgibstorso_prop.mdl")
    __main__.CallEntitySpawn(punk5Body)
    punk5Bodya=__main__.CreateEntityNoSpawn("prop_physics",Find("tzim_punk5").GetOrigin(),Find("tzim_punk5").GetAngles())
    punk5Bodya.SetName("punk5Bodya")
    punk5Bodya.SetModel("models/gibs/hgibslleg_prop.mdl")
    __main__.CallEntitySpawn(punk5Bodya)
    punk5Bodyb=__main__.CreateEntityNoSpawn("prop_physics",Find("tzim_punk5").GetOrigin(),Find("tzim_punk5").GetAngles())
    punk5Bodyb.SetName("punk5Bodyb")
    punk5Bodyb.SetModel("models/gibs/hgibslarm_prop.mdl")
    __main__.CallEntitySpawn(punk5Bodyb)
    punk5Bodyc=__main__.CreateEntityNoSpawn("prop_physics",Find("tzim_punk5").GetOrigin(),Find("tzim_punk5").GetAngles())
    punk5Bodyc.SetName("punk5Bodyc")
    punk5Bodyc.SetModel("models/gibs/hgibsskull_prop.mdl")
    __main__.CallEntitySpawn(punk5Bodyc)

#--------------------------------------
#HW_WARRENS_4: tzimisce punk6 explode
def War4Tzpunk6boom():
    Find("tzpk6_explosion").SetOrigin(Find("tzim_punk6").GetOrigin())
    __main__.ScheduleTask(0.1,"War4Tzpunk6boom1()")
    __main__.ScheduleTask(0.05,"War4Tzpunk6boom2()")

def War4Tzpunk6boom1():
    Find("tzpk6_explosion").Explode()

def War4Tzpunk6boom2():
    punk6Body=__main__.CreateEntityNoSpawn("prop_physics",Find("tzim_punk6").GetOrigin(),Find("tzim_punk6").GetAngles())
    punk6Body.SetName("punk6Body")
    punk6Body.SetModel("models/gibs/hgibstorso_prop.mdl")
    __main__.CallEntitySpawn(punk6Body)
    punk6Bodya=__main__.CreateEntityNoSpawn("prop_physics",Find("tzim_punk6").GetOrigin(),Find("tzim_punk6").GetAngles())
    punk6Bodya.SetName("punk6Bodya")
    punk6Bodya.SetModel("models/gibs/hgibslleg_prop.mdl")
    __main__.CallEntitySpawn(punk6Bodya)
    punk6Bodyb=__main__.CreateEntityNoSpawn("prop_physics",Find("tzim_punk6").GetOrigin(),Find("tzim_punk6").GetAngles())
    punk6Bodyb.SetName("punk6Bodyb")
    punk6Bodyb.SetModel("models/gibs/hgibslarm_prop.mdl")
    __main__.CallEntitySpawn(punk6Bodyb)
    punk6Bodyc=__main__.CreateEntityNoSpawn("prop_physics",Find("tzim_punk6").GetOrigin(),Find("tzim_punk6").GetAngles())
    punk6Bodyc.SetName("punk6Bodyc")
    punk6Bodyc.SetModel("models/gibs/hgibsskull_prop.mdl")
    __main__.CallEntitySpawn(punk6Bodyc)

#--------------------------------------
#HW_WARRENS_4: PC use swith panel 1
#unlocks drain controls if key present
def checkForPasskeyNewSwith():
    pc = __main__.FindPlayer()
    if ( pc.HasItem("item_g_warrens4_passkey") ):
        Find("new_switch1").Unlock()

#--------------------------------------
##def testflow(x, y, z):
##    print ( "Time, Flow, Steps" )
##    G.W_Time = x
##    G.W_FlowMax = y
##    G.W_FlowSteps = z
##    G.Flow_Ran = 0
##
##def flowUp():
##    ctrlmdl = Find( "Water_Control_MDL" )
##    flow_ent = Find( "Flow_Push" )
##    flow_ent.SetSpeed(G.flow_amt)
##    if ( G.flow_amt == ( G.flow_amt /5 ) ):
##         ctrlmdl.Skin(1)
##def flowDwn():
##    ctrlmdl = Find( "Water_Control_MDL" )
##    flow_ent = Find( "Flow_Push" )
##    flow_ent.SetSpeed(G.flow_amt)
##    if ( G.flow_amt == ( G.flow_amt /5 ) ):
##         ctrlmdl.Skin(1)
##
##def masterFlow(direction):
##    if ( G.Flow_Ran == 1 ):
##        G.flow_amt =( G.W_FlowMax / G.W_FlowSteps )
##        G.time_inc = G.W_Time / G.W_FlowSteps
##    G.Flow_Ran = 1
##    fanmdl = Find( "Flow_fan_blade" )
##    sndon = Find( "Sound_Flow_ON" )
##    sndoff = Find( "Sound_Flow_OFF" )
##    triggers = Find( "FloodRoom_Triggers" )
##
##    if (direction == UP):
##        G.WarrensPump = 1
##        triggers.ScriptUnhide()
##        fanmdl.Start()
##        sndon.PlaySound()
##        sndoff.StopSound()
##        while ( G.flow_amt < G.W_FlowMax ):
##            __main__.ScheduleTask( G.time_inc, "flowUp()" )
##            G.flow_amt = G.flow_amt + G.flow_amt
##
##    if (direction == DOWN):
##        G.WarrensPump = 0
##        triggers.ScriptHide()
##        fanmdl.Stop()
##        sndoff.PlaySound()
##        sndon.StopSound()
##        while ( G.flow_amt > 0 ):
##            __main__.ScheduleTask( G.time_inc, "flowDwn()" )
##            G.flow_amt = G.flow_amt - G.flow_amt

print "levelscript loaded"