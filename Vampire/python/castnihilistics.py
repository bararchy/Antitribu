#FILENAME : castnihilistics.py

import __main__
from __main__ import Character

############################

def _TraceCircle(self, radius=50, angleOffset=0):

    from math import pi as _pi
    from math import cos as _cos, sin as _sin

    pos   = self.GetOrigin()
    angle = self.GetAngles()[1] + angleOffset

    xoffset = radius * _cos((angle/(360/(2*_pi))))
    yoffset = radius * _sin((angle/(360/(2*_pi))))

    return (pos[0]+xoffset, pos[1]+yoffset, pos[2])

Character.TraceCircle=_TraceCircle

#-----------------------------------------------Level 1---------------------------
#-----------------------------------------------Level 2---------------------------
def SpawnNihGhosts(entityName, angle, entityType, model, distance ):

    point = __main__.FindPlayer().TraceCircle(distance,angle)
    facing=(0,angle,0)

    entnihl2 = __main__.CreateEntityNoSpawn(entityType, point, facing )
    try:
        entnihl2.SetName(entityName)
        entnihl2.SetRelationship("player D_HT 6")
        entnihl2.pl_investigate=6
        entnihl2.pl_criminal_flee=6
        entnihl2.pl_criminal_attack=6
        entnihl2.pl_supernatural_flee=6
        entnihl2.pl_supernatural_attack=6
        entnihl2.SetInvestigateMode(4)
        entnihl2.SetInvestigateModeCombat(4)
        entnihl2.physdamagescale=1.0
        entnihl2.TweakParam("hearing 1024")
        entnihl2.TweakParam("vision 1024")
        entnihl2.AllowKickHintUse(1)
        entnihl2.LookAtEntityEye("!player")
        entnihl2.SetFollowerType("Default")
        entnihl2.SetFollowerBoss("none")
        entnihl2.SetModel(model)
        entnihl2.PlayDialogFile("disciplines/nihilistics/lvl2/loop.wav")
    except:
        pass
    __main__.CallEntitySpawn(entnihl2)
    
    entnihl2.SetScriptedDiscipline("celerity 5")
    entnihl2.SetScriptedDiscipline("obfuscate 3")
    entnihl2.SetScriptedDiscipline("mind_shield 3")
    return entnihl2

def SetNihGhosts(anameO4):
    allyO4 = __main__.FindEntityByName(anameO4)
    if allyO4:
        allyO4.SetScriptedDiscipline("obfuscate 5")
        allyO4.SetModel("models/weapons/disciplines/Necromancy/lvl5/ghost_female.mdl")
        allyO4.SetGesture("howl")
        allyO4.ChangeSchedule('TAKE_COVER_FROM_ENEMY')
        __main__.ScheduleTask(20.5,"castnihilistics.RemoveNihGhosts('%s')" % anameO4)
	__main__.ScheduleTask(3.25,"__main__.FindEntityByName('%s').ChangeSchedule('SCHED_TROIKA_D_BRAINWIPE_END')" % anameO4)

def RemoveNihGhosts(anameO4):
    allyO4 = __main__.FindEntityByName(anameO4)
    if allyO4:
        allyO4.SetScriptedDiscipline("obfuscate 5")
        allyO4.PlayDialogFile("area/santa_monica/ocean_house/oceanhouse_ghost/help_me.wav")
        __main__.ScheduleTask(1.25,"__main__.FindEntityByName('%s').Kill()" % anameO4)

################
allynih2Index=1
def ActivateNihGhosts(level=1):
    global allynih2Index

    entityType="npc_VGhoulCroucher"
    model="models/weapons/disciplines/Necromancy/lvl5/ghost_female.mdl"

    offset = round(360/level)
    while level > 0:
        anameO4 = "_my_ally_nih2_%d" % allynih2Index
        allyO4 = SpawnNihGhosts(anameO4, (-180 + (offset * level)),entityType,model,-220)
        __main__.ScheduleTask(0.5,"castnihilistics.SetNihGhosts('%s')" % anameO4)
        level=level-1
        allynih2Index=allynih2Index+1

#-------------------------------------------------------------Nihilistics 5 level Nightcry--------
def SpawnCrusader(entityName, angle, entityType, model, distance ):

    point = __main__.FindPlayer().TraceCircle(distance,angle)
    facing=(0,angle,0)

    crus = __main__.CreateEntityNoSpawn(entityType, point, facing )
    try:
        crus.SetName(entityName)
        crus.SetRelationship("player D_LI 5")
        crus.pl_investigate=6
        crus.pl_criminal_flee=6
        crus.pl_criminal_attack=6
        crus.pl_supernatural_flee=6
        crus.pl_supernatural_attack=6
        crus.SetInvestigateMode(4)
        crus.SetInvestigateModeCombat(4)
        crus.physdamagescale=1.0
        crus.TweakParam("hearing 750")
        crus.TweakParam("vision 750")
        crus.AllowKickHintUse(1)
        crus.LookAtEntityEye("!player")
        crus.SetFollowerType("Default")
        crus.SetFollowerBoss("!player")
        crus.SetModel(model)
        crus.MakeInvincible(1)
    except:
        pass
    __main__.CallEntitySpawn(crus)
    
    crus.SetScriptedDiscipline("celerity 5")
    crus.SetScriptedDiscipline("potence 5")
    return crus

def RemoveCrusader(aname):
    crusader = __main__.FindEntityByName(aname)
    if crusader:
        crusader.SetGesture("ACT_FIDGET")
        __main__.ScheduleTask(1.75,"__main__.FindEntityByName('%s').PlayDialogFile('disciplines/nihilistics/lvl5/crus_cry.wav')" % aname)
        __main__.ScheduleTask(3.0,"__main__.FindEntityByName('%s').PlayDialogFile('disciplines/nihilistics/lvl5/crus_loop.wav')" % aname)
        __main__.ScheduleTask(28.75,"__main__.FindEntityByName('%s').PlayDialogFile('disciplines/nihilistics/lvl5/crus_end.wav')" % aname)
	__main__.ScheduleTask(29.5,"__main__.FindEntityByName('%s').SetGesture('ACT_LANDLITE')" % aname)
        __main__.ScheduleTask(30.0,"__main__.FindEntityByName('%s').Kill()" % aname)

################

crusIndex=1
def ActivateCrusaderSummon(level=1):
    global crusIndex

    entityType="npc_VTzimisceHeadClaw"
    model="models/weapons/disciplines/Necromancy/lvl5/crusader_ghost.mdl"

    offset = round(360/level)
    while level > 0:
        aname = "_my_crusader_%d" % crusIndex
        crusader = SpawnCrusader(aname, (-180 + (offset * level)),entityType,model,-60)
        __main__.ScheduleTask(0.1,"castnihilistics.RemoveCrusader('%s')" % aname)
        level=level-1
        crusIndex=crusIndex+1
#-----------------------------------------------end---------------------------
#---------------------------------------------------------------------------
def SpawnNightshades(entityName, angle, entityType, model, distance ):

    point = __main__.FindPlayer().TraceCircle(distance,angle)
    facing=(0,angle,0)

    entol4 = __main__.CreateEntityNoSpawn(entityType, point, facing )
    try:
        entol4.SetName(entityName)
        entol4.SetRelationship("player D_LI 5")
        entol4.pl_investigate=6
        entol4.pl_criminal_flee=6
        entol4.pl_criminal_attack=6
        entol4.pl_supernatural_flee=6
        entol4.pl_supernatural_attack=6
        entol4.SetInvestigateMode(4)
        entol4.SetInvestigateModeCombat(4)
        entol4.physdamagescale=1.0
        entol4.TweakParam("hearing 550")
        entol4.TweakParam("vision 450")
        entol4.AllowKickHintUse(1)
        entol4.LookAtEntityEye("!player")
        entol4.SetFollowerType("Default")
        entol4.SetFollowerBoss("!player")
        entol4.SetModel(model)
        entol4.MakeInvincible(1)
        entol4.PlayDialogFile("disciplines/obtenebration/level1/loop.wav")
    except:
        pass
    __main__.CallEntitySpawn(entol4)
    
    entol4.SetScriptedDiscipline("celerity 5")
    #entol4.SetScriptedDiscipline("obfuscate 1")
    entol4.SetScriptedDiscipline("mind_shield 1")
    return entol4

def RemoveNightshades(anameO4):
    allyO4 = __main__.FindEntityByName(anameO4)
    if allyO4:
        allyO4.SetScriptedDiscipline("obfuscate 5")
        allyO4.PlayDialogFile("disciplines/obtenebration/level1/deactivate.wav")
        __main__.ScheduleTask(1.25,"__main__.FindEntityByName('%s').Kill()" % anameO4)

################
allyO4Index=1
def ActivateNightshades(level=1):
    global allyO4Index

    entityType="npc_VRat"
    model="models/weapons/disciplines/obtenebration/nightshades.mdl"

    offset = round(360/level)
    while level > 0:
        anameO4 = "_my_ally_o4_%d" % allyO4Index
        allyO4 = SpawnNightshades(anameO4, (-180 + (offset * level)),entityType,model,-35)
        __main__.ScheduleTask(9.5,"castnihilistics.RemoveNightshades('%s')" % anameO4)
        level=level-1
        allyO4Index=allyO4Index+1

#---------------------------------------------------------------------------
#-----------------------------------------------------level 3----------------------
def SpawnShadowArms(entityName, angle, entityType, model, distance ):

    point = __main__.FindPlayer().TraceCircle(distance,angle)
    facing=(0,angle,0)

    entol3 = __main__.CreateEntityNoSpawn(entityType, point, facing )
    try:
        entol3.SetName(entityName)
        entol3.SetRelationship("player D_LI 5")
        entol3.pl_investigate=6
        entol3.pl_criminal_flee=6
        entol3.pl_criminal_attack=6
        entol3.pl_supernatural_flee=6
        entol3.pl_supernatural_attack=6
        entol3.SetInvestigateMode(4)
        entol3.SetInvestigateModeCombat(4)
        entol3.physdamagescale=1.0
        entol3.TweakParam("hearing 750")
        entol3.TweakParam("vision 650")
        entol3.AllowKickHintUse(1)
        entol3.LookAtEntityEye("!player")
        entol3.SetFollowerType("Default")
        entol3.SetFollowerBoss("!player")
        entol3.SetModel(model)
        entol3.MakeInvincible(1)
        entol3.PlayDialogFile("disciplines/obtenebration/level3/loop.wav")
    except:
        pass
    __main__.CallEntitySpawn(entol3)
    
    entol3.SetScriptedDiscipline("celerity 5")
    entol3.SetScriptedDiscipline("mind_shield 1")
    return entol3

################
def ActivateShadowArms():
    ShadowArms = __main__.FindEntityByName("ShadowArms")
    ShadowArmsBody = __main__.FindEntityByName("ShadowArmsBody")
    if(ShadowArmsBody):
       return
    else:
       #entityType="npc_VSabbatGunman"
       entityType="npc_VHengeyokai"
       model="models/character/monster/tzimisce/creation3/tzim3_null.mdl"
       ShadowArms="ShadowArms"
       offset = round(360)
       sarms = SpawnShadowArms(ShadowArms, (180 + (offset)),entityType,model,-35)
       __main__.ScheduleTask(0.1,"castnihilistics.ActivateShadowArmsBody()")

def SummonShadowArms():
    ShadowArms = __main__.FindEntityByName("ShadowArms")
    ShadowArmsBody = __main__.FindEntityByName("ShadowArmsBody")
    if ShadowArmsBody:
        ShadowArmsBody.SetParent("ShadowArms")
        __main__.ScheduleTask(17.45,"castnihilistics.RemoveShadowArms()")

def RemoveShadowArms():
       __main__.FindEntityByName("ShadowArms").PlayDialogFile("disciplines/obtenebration/level3/deactivate.wav")
       __main__.FindEntityByName("ShadowArms").SetScriptedDiscipline("obfuscate 5")
       __main__.ScheduleTask(1.55,"castnihilistics.RemoveShadowArms1()")

def RemoveShadowArms1():
       __main__.FindEntityByName("ShadowArms").Kill()
       __main__.FindEntityByName("ShadowArmsBody").Kill()

#---------------
def SpawnShadowArmsBody(entityName, angle, entityType, model, distance ):

    point = __main__.FindPlayer().TraceCircle(distance,angle)
    facing=(0,angle,0)

    entol3a = __main__.CreateEntityNoSpawn(entityType, point, facing )
    try:
        entol3a.SetName(entityName)
        entol3a.SetRelationship("player D_LI 5")
        entol3a.pl_investigate=6
        entol3a.pl_criminal_flee=6
        entol3a.pl_criminal_attack=6
        entol3a.pl_supernatural_flee=6
        entol3a.pl_supernatural_attack=6
        entol3a.SetInvestigateMode(4)
        entol3a.SetInvestigateModeCombat(4)
        entol3a.physdamagescale=1.0
        entol3a.TweakParam("hearing 750")
        entol3a.TweakParam("vision 650")
        entol3a.AllowKickHintUse(1)
        entol3a.LookAtEntityEye("!player")
        entol3a.SetFollowerType("Default")
        entol3a.SetFollowerBoss("!player")
        entol3a.SetModel(model)
        entol3a.MakeInvincible(1)
    except:
        pass
    __main__.CallEntitySpawn(entol3a)
    
    entol3a.SetScriptedDiscipline("celerity 5")
    return entol3a

################
def ActivateShadowArmsBody():
    entityType="npc_VRat"
    model="models/weapons/disciplines/animalism/null.mdl"
    ShadowArmsBody="ShadowArmsBody"
    offset = round(360)
    sarmsbody = SpawnShadowArmsBody(ShadowArmsBody, (180 + (offset)),entityType,model,-35)
    __main__.ScheduleTask(0.1,"castnihilistics.SummonShadowArms()")

#---------------------------------------------------------------------------
#-----------------------------------------------Level 5---------------------------
def SpawnShadowTwin(entityName, angle, entityType, model, distance ):

    point = __main__.FindPlayer().TraceCircle(distance,angle)
    facing=(0,angle,0)

    entOb5 = __main__.CreateEntityNoSpawn(entityType, point, facing )
    try:
        entOb5.SetName(entityName)
        entOb5.SetRelationship("player D_LI 5")
        entOb5.pl_investigate=6
        entOb5.pl_criminal_flee=6
        entOb5.pl_criminal_attack=6
        entOb5.pl_supernatural_flee=6
        entOb5.pl_supernatural_attack=6
        entOb5.SetInvestigateMode(4)
        entOb5.SetInvestigateModeCombat(4)
        entOb5.physdamagescale=1.0
        entOb5.TweakParam("hearing 1024")
        entOb5.TweakParam("vision 1024")
        entOb5.AllowKickHintUse(1)
        entOb5.LookAtEntityEye("!player")
        entOb5.SetFollowerType("Default")
        entOb5.SetFollowerBoss("!player")
        entOb5.SetModel(model)
        entOb5.PlayDialogFile("disciplines/obtenebration/level4/activate.wav")
    except:
        pass
    __main__.CallEntitySpawn(entOb5)
    
    #entOb5.SetScriptedDiscipline("celerity 5")
    entOb5.SetScriptedDiscipline("potence 5")
    entOb5.SetScriptedDiscipline("obfuscate 1")
    #entOb5.SetScriptedDiscipline("Fortitude 1")
    entOb5.SetScriptedDiscipline("shield_of_faith 3")
    return entOb5

################
def ActivateShadowTwin(level=1):

    ShadowWarrior = __main__.FindEntityByName("ShadowWarrior")
    if(ShadowWarrior):
       return
    else:
       entityType="npc_VSabbatGunman"
       model="models/weapons/disciplines/obtenebration/nightshades.mdl"
       ShadowWarrior="ShadowWarrior"
       offset = round(360)
       swarrior = SpawnShadowTwin(ShadowWarrior, (180 + (offset)),entityType,model,-40)
       __main__.ScheduleTask(0.55,"castnihilistics.SetShadowTwin()")

def SetShadowTwin():
    pc=__main__.FindPlayer()
    ShadowWarrior = __main__.FindEntityByName("ShadowWarrior")
    #pevents = __main__.FindEntitiesByClass("events_player")
    #pevents[0].MakePlayerUnkillable()
    ShadowWarrior.SetModel(pc.model)
    ShadowWarrior.SetGesture("land_hard")
    ShadowWarrior.PlayDialogFile("disciplines/dementation/maintain.wav")
    __main__.ScheduleTask(14.9,"castnihilistics.RemoveShadowTwin()")

def RemoveShadowTwin():
    ShadowWarrior = __main__.FindEntityByName("ShadowWarrior")
    ShadowWarrior.SetScriptedDiscipline("obfuscate 5")
    ShadowWarrior.PlayDialogFile("interface/feeding/feed_forced.wav")
    __main__.ScheduleTask(0.2,"castnihilistics.RemoveShadowTwin1()")
    #__main__.ScheduleTask(1.0,"castnihilistics.RemoveShadowTwinPc()")

def RemoveShadowTwin1():
    __main__.FindEntityByName("ShadowWarrior").Kill()

def RemoveShadowTwinPc():
    pevents = __main__.FindEntitiesByClass("events_player")
    pevents[0].MakePlayerKillable()

################