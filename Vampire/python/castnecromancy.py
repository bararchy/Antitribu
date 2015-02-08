#FILENAME : castnecromancy.py

import __main__
from __main__ import Character

import castnecromancy

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
def SpawnBloodAlly1(entityName, angle, entityType, model, distance ):

    point = __main__.FindPlayer().TraceCircle(distance,angle)
    facing=(0,angle,0)

    entl1 = __main__.CreateEntityNoSpawn(entityType, point, facing )
    try:
        entl1.SetName(entityName)
        entl1.SetRelationship("player D_LI 5")
        entl1.pl_investigate=6
        entl1.pl_criminal_flee=6
        entl1.pl_criminal_attack=6
        entl1.pl_supernatural_flee=6
        entl1.pl_supernatural_attack=6
        entl1.SetInvestigateMode(4)
        entl1.SetInvestigateModeCombat(4)
        entl1.physdamagescale=1.0
        entl1.TweakParam("hearing 50")
        entl1.TweakParam("vision 250")
        entl1.AllowKickHintUse(1)
        entl1.LookAtEntityEye("!player")
        entl1.SetFollowerType("Default")
        entl1.SetFollowerBoss("!player")
        entl1.SetModel(model)
    except:
        pass
    __main__.CallEntitySpawn(entl1)
    __main__.ScheduleTask(0.2,"castnecromancy.Activate3Summon(1)")
    return entl1

def RemoveBloodAlly1(aname):
    ally1 = __main__.FindEntityByName(aname)
    if ally1:
        __main__.ScheduleTask(3.0,"__main__.FindEntityByName('%s').Kill()" % aname)

################################################################################################
ally1Index=1
def Activate1Summon(level=1):
    global ally1Index

    entityType="npc_VRat"
    model="models/character/monster/animalism_raven/animalism_raven.mdl"

    timeout=4
    offset = round(360/level)
    while level > 0:
        aname = "_my_ally_n1_%d" % ally1Index
        ally1 = SpawnBloodAlly1(aname, (-180 + (offset * level)),entityType,model,-70)
        if -1 != timeout:
            __main__.ScheduleTask(timeout,"castnecromancy.RemoveBloodAlly1('%s')" % aname)
        level=level-1
        ally1Index=ally1Index+1

#-----------------------------------------------Level 1b---------------------------
def SpawnBloodAlly3(entityName, angle, entityType, model, distance ):

    point = __main__.FindPlayer().TraceCircle(distance,angle)
    facing=(0,angle,0)

    entl3 = __main__.CreateEntityNoSpawn(entityType, point, facing )
    try:
        entl3.SetName(entityName)
        entl3.SetRelationship("player D_LI 5")
        entl3.pl_investigate=6
        entl3.pl_criminal_flee=6
        entl3.pl_criminal_attack=6
        entl3.pl_supernatural_flee=6
        entl3.pl_supernatural_attack=6
        entl3.SetInvestigateMode(4)
        entl3.SetInvestigateModeCombat(4)
        entl3.physdamagescale=1.0
        entl3.TweakParam("hearing 50")
        entl3.TweakParam("vision 250")
        entl3.AllowKickHintUse(1)
        entl3.LookAtEntityEye("!player")
        entl3.SetFollowerType("Default")
        entl3.SetFollowerBoss("!player")
        entl3.SetModel(model)
	entl3.PlayDialogFile("disciplines/necromancy/level1/Start1.wav")
    except:
        pass
    __main__.CallEntitySpawn(entl3)
    return entl3

def RemoveBloodAlly3(aname):
    ally3 = __main__.FindEntityByName(aname)
    if ally3:
        ally3.SetScriptedDiscipline("obfuscate 4")
	ally3.PlayDialogFile("disciplines/necromancy/level4/End4.wav")
        __main__.ScheduleTask(3.0,"__main__.FindEntityByName('%s').Kill()" % aname)

################################################################################################
ally3Index=1
def Activate3Summon(level=1):
    global ally3Index

    entityType="npc_VZombie"
    model="models/character/monster/undead/female/undead_female.mdl"

    timeout=4
    offset = round(360/level)
    while level > 0:
        aname = "_my_ally_n1b_%d" % ally3Index
        ally3 = SpawnBloodAlly3(aname, (-180 + (offset * level)),entityType,model,-70)
        if -1 != timeout:
            __main__.ScheduleTask(timeout,"castnecromancy.RemoveBloodAlly3('%s')" % aname)
        level=level-1
        ally3Index=ally3Index+1

#-----------------------------------------------Level 2---------------------------
def SpawnBloodAlly4(entityName, angle, entityType, model, distance ):

    point = __main__.FindPlayer().TraceCircle(distance,angle)
    facing=(0,angle,0)

    entl4 = __main__.CreateEntityNoSpawn(entityType, point, facing )
    try:
        entl4.SetName(entityName)
        entl4.SetRelationship("player D_LI 5")
        entl4.pl_investigate=6
        entl4.pl_criminal_flee=6
        entl4.pl_criminal_attack=6
        entl4.pl_supernatural_flee=6
        entl4.pl_supernatural_attack=6
        entl4.SetInvestigateMode(4)
        entl4.SetInvestigateModeCombat(4)
        entl4.physdamagescale=1.0
        entl4.TweakParam("hearing 50")
        entl4.TweakParam("vision 250")
        entl4.AllowKickHintUse(1)
        entl4.LookAtEntityEye("!player")
        entl4.SetFollowerType("Default")
        entl4.SetFollowerBoss("!player")
        entl4.SetModel(model)
	entl4.PlayDialogFile("disciplines/necromancy/level2/Activate2.wav")
    except:
        pass
    __main__.CallEntitySpawn(entl4)
    return entl4

def RemoveBloodAlly4(aname4):
    ally4 = __main__.FindEntityByName(aname4)
    if ally4:
        ally4.SetModel("models/weapons/disciplines/Necromancy/lvl2/zombie_2.mdl")
        ally4.SetGesture("crawlout")
        ally4.SetScriptedDiscipline("mind_shield 2")
        __main__.ScheduleTask(60.5,"castnecromancy.RemoveBloodAlly4helper('%s')" % aname4)

def RemoveBloodAlly4helper(aname4):
    ally4 = __main__.FindEntityByName(aname4)
    if ally4:
        ally4.SetScriptedDiscipline("obfuscate 4")
	ally4.PlayDialogFile("disciplines/necromancy/level4/End4.wav")
        __main__.ScheduleTask(1.0,"__main__.FindEntityByName('%s').Kill()" % aname4)

################################################################################################
ally4Index=1
def Activate4Summon(level=1):
    global ally4Index

    entityType="npc_VGhoulCroucher"
    model="models/weapons/disciplines/Necromancy/lvl2/zombie_2.mdl"

    timeout=0.1
    offset = round(360/level)
    while level > 0:
        aname4 = "_my_ally_n2_%d" % ally4Index
        ally4 = SpawnBloodAlly4(aname4, (-180 + (offset * level)),entityType,model,-85)
        if -1 != timeout:
            __main__.ScheduleTask(timeout,"castnecromancy.RemoveBloodAlly4('%s')" % aname4)
        level=level-1
        ally4Index=ally4Index+1

#-----------------------------------------------Level 3---------------------------
def SpawnBloodAlly5(entityName, angle, entityType, model, distance ):

    point = __main__.FindPlayer().TraceCircle(distance,angle)
    facing=(0,angle,0)

    entl5 = __main__.CreateEntityNoSpawn(entityType, point, facing )
    try:
        entl5.SetName(entityName)
        entl5.SetRelationship("player D_LI 5")
        entl5.pl_investigate=6
        entl5.pl_criminal_flee=6
        entl5.pl_criminal_attack=6
        entl5.pl_supernatural_flee=6
        entl5.pl_supernatural_attack=6
        entl5.SetInvestigateMode(4)
        entl5.SetInvestigateModeCombat(4)
        entl5.physdamagescale=1.0
        entl5.TweakParam("hearing 50")
        entl5.TweakParam("vision 250")
        entl5.AllowKickHintUse(1)
        entl5.LookAtEntityEye("!player")
        entl5.SetFollowerType("Default")
        entl5.SetFollowerBoss("!player")
        entl5.SetModel(model)
	entl5.PlayDialogFile("disciplines/necromancy/level3/Activate3.wav")
    except:
        pass
    __main__.CallEntitySpawn(entl5)
    return entl5

def RemoveBloodAlly5(aname5):
    ally5 = __main__.FindEntityByName(aname5)
    if ally5:
        ally5.SetScriptedDiscipline("mind_shield 3")
        ally5.SetModel("models/weapons/disciplines/Necromancy/lvl2/zombie_2.mdl")
        ally5.SetGesture("crawlout")
        __main__.ScheduleTask(90.5,"castnecromancy.RemoveBloodAlly5helper('%s')" % aname5)
        __main__.ScheduleTask(3.5,"castnecromancy.RemoveBloodAlly5helper1('%s')" % aname5)

def RemoveBloodAlly5helper1(aname5):
    ally5 = __main__.FindEntityByName(aname5)
    if ally5:
        #ally5.ChangeSchedule('SCHED_VGHOUL_CROUCHER_UNAWARE_EXIT')
        ally5.ChangeSchedule('SCHED_TROIKA_D_POSSESSION')

def RemoveBloodAlly5helper(aname5):
    ally5 = __main__.FindEntityByName(aname5)
    if ally5:
        ally5.SetScriptedDiscipline("obfuscate 4")
	ally5.PlayDialogFile("disciplines/necromancy/level4/End4.wav")
        __main__.ScheduleTask(1.0,"__main__.FindEntityByName('%s').Kill()" % aname5)

################################################################################################
ally5Index=1
def Activate5Summon(level=1):
    global ally5Index

    entityType="npc_VGhoulCroucher"
    model="models/weapons/disciplines/Necromancy/lvl2/zombie_2.mdl"

    timeout=0.01
    offset = round(360/level)
    while level > 0:
        aname5 = "_my_ally_n3_%d" % ally5Index
        ally5 = SpawnBloodAlly5(aname5, (-180 + (offset * level)),entityType,model,75)
        if -1 != timeout:
            __main__.ScheduleTask(timeout,"castnecromancy.RemoveBloodAlly5('%s')" % aname5)
        level=level-1
        ally5Index=ally5Index+1

#-----------------------------------------------Level 4---------------------------
def SpawnBloodAlly6(entityName, angle, entityType, model, distance ):

    point = __main__.FindPlayer().TraceCircle(distance,angle)
    facing=(0,angle,0)

    entl6 = __main__.CreateEntityNoSpawn(entityType, point, facing )
    try:
        entl6.SetName(entityName)
        entl6.SetRelationship("player D_LI 5")
        entl6.pl_investigate=6
        entl6.pl_criminal_flee=6
        entl6.pl_criminal_attack=6
        entl6.pl_supernatural_flee=6
        entl6.pl_supernatural_attack=6
        entl6.SetInvestigateMode(4)
        entl6.SetInvestigateModeCombat(4)
        entl6.physdamagescale=1.0
        entl6.TweakParam("hearing 50")
        entl6.TweakParam("vision 250")
        entl6.AllowKickHintUse(1)
        entl6.LookAtEntityEye("!player")
        entl6.SetFollowerType("Default")
        entl6.SetFollowerBoss("!player")
        entl6.SetModel(model)
	entl6.PlayDialogFile("disciplines/necromancy/level4/Activate4.wav")
    except:
        pass
    __main__.CallEntitySpawn(entl6)  
    entl6.SetScriptedDiscipline("shield_of_faith 2")
    return entl6

def RemoveBloodAlly6(aname6):
    ally6 = __main__.FindEntityByName(aname6)
    if ally6:
        ally6.SetModel("models/weapons/disciplines/Necromancy/lvl3/zombie_3.mdl")
        ally6.SetGesture("ACT_SLEEP_GETUP")
	__main__.ScheduleTask(45,"castnecromancy.RemoveBloodAlly6a('%s')" % aname6)

def RemoveBloodAlly6a(aname6):
    ally6 = __main__.FindEntityByName(aname6)
    if ally6:
        ally6.PlayDialogFile("disciplines/necromancy/level4/End4.wav")
        ally6.SetScriptedDiscipline("shield_of_faith 3")
        __main__.ScheduleTask(1.5,"__main__.FindEntityByName('%s').Kill()" % aname6)


################################################################################################
ally6Index=1
def Activate6Summon(level=1):
    global ally6Index

    entityType="npc_VGhoulCroucher"
    model="models/weapons/disciplines/Necromancy/lvl2/zombie_2.mdl"

    timeout=0.1
    offset = round(360/level)
    while level > 0:
        aname6 = "_my_ally_n4_%d" % ally6Index
        ally6 = SpawnBloodAlly6(aname6, (-180 + (offset * level)),entityType,model,-75)
        if -1 != timeout:
            __main__.ScheduleTask(timeout,"castnecromancy.RemoveBloodAlly6('%s')" % aname6)
        level=level-1
        ally6Index=ally6Index+1

#-----------------------------------------------Level 5---------------------------
def SpawnBloodAlly7(entityName, angle, entityType, model, distance ):

    point = __main__.FindPlayer().TraceCircle(distance,angle)
    facing=(0,angle,0)

    entl7 = __main__.CreateEntityNoSpawn(entityType, point, facing )
    try:
        entl7.SetName(entityName)
        entl7.SetRelationship("player D_LI 5")
        entl7.pl_investigate=6
        entl7.pl_criminal_flee=6
        entl7.pl_criminal_attack=6
        entl7.pl_supernatural_flee=6
        entl7.pl_supernatural_attack=6
        entl7.SetInvestigateMode(4)
        entl7.SetInvestigateModeCombat(4)
        entl7.physdamagescale=1.0
        entl7.TweakParam("hearing 50")
        entl7.TweakParam("vision 250")
        entl7.AllowKickHintUse(1)
        entl7.LookAtEntityEye("!player")
        entl7.SetFollowerType("Default")
        entl7.SetFollowerBoss("!player")
        entl7.SetModel(model)
        entl7.PlayDialogFile("disciplines/necromancy/level5/Activate5.wav")
        entl7.MakeInvincible(1)
    except:
        pass
    __main__.CallEntitySpawn(entl7)  
    entl7.SetScriptedDiscipline("shield_of_faith 2")
    return entl7

def RemoveBloodAlly7(aname7):
    ally7 = __main__.FindEntityByName(aname7)
    if ally7:
        ally7.SetModel("models/weapons/disciplines/Necromancy/lvl3/zombie_3.mdl")
        ally7.SetGesture("praying_end")
	__main__.ScheduleTask(5,"castnecromancy.RemoveBloodAlly7a('%s')" % aname7)

def RemoveBloodAlly7a(aname7):
    ally7 = __main__.FindEntityByName(aname7)
    if ally7:
        ally7.PlayDialogFile("disciplines/necromancy/level5/Activate5.wav")
        #ally7.MakeInvincible(1)
        ally7.SetScriptedDiscipline("shield_of_faith 5")
        #ally7.SetScriptedDiscipline("presence 1")
        #ally7.SetScriptedDiscipline("mind_shield 1")
        ally7.SetModel("models/weapons/disciplines/Necromancy/lvl5/ghost_female.mdl")
	__main__.ScheduleTask(30,"castnecromancy.RemoveBloodAlly7b('%s')" % aname7)
	__main__.ScheduleTask(0.25,"castnecromancy.RemoveBloodAlly7c('%s')" % aname7)

def RemoveBloodAlly7b(aname7):
    ally7 = __main__.FindEntityByName(aname7)
    if ally7:
        ally7.PlayDialogFile("disciplines/necromancy/level4/End4.wav")
        ally7.SetScriptedDiscipline("shield_of_faith 4")
        __main__.ScheduleTask(1.5,"__main__.FindEntityByName('%s').Kill()" % aname7)

def RemoveBloodAlly7c(aname7):
    ally7 = __main__.FindEntityByName(aname7)
    if ally7:
        #ally7.SetGesture("theft_outof")
        ally7.ChangeSchedule('SCHED_TROIKA_D_BERSERK')

################################################################################################
ally7Index=1
def Activate7Summon(level=1):
    global ally7Index

    entityType="npc_VGhoulCroucher"
    model="models/weapons/disciplines/Necromancy/lvl2/zombie_2.mdl"

    timeout=0.1
    offset = round(360/level)
    while level > 0:
        aname7 = "_my_ally_n5_%d" % ally7Index
        ally7 = SpawnBloodAlly7(aname7, (-180 + (offset * level)),entityType,model,-75)
        if -1 != timeout:
            __main__.ScheduleTask(timeout,"castnecromancy.RemoveBloodAlly7('%s')" % aname7)
        level=level-1
        ally7Index=ally7Index+1

#-----------------------------------------------Level 5 samedi---------------------------

def SpawnSkeletonAlly(entityName, angle, entityType, model, distance ):

    point = __main__.FindPlayer().TraceCircle(distance,angle)
    facing=(0,angle,0)

    entl8 = __main__.CreateEntityNoSpawn(entityType, point, facing )
    try:
        entl8.SetName(entityName)
        entl8.SetRelationship("player D_LI 5")
        entl8.pl_investigate=6
        entl8.pl_criminal_flee=6
        entl8.pl_criminal_attack=6
        entl8.pl_supernatural_flee=6
        entl8.pl_supernatural_attack=6
        entl8.SetInvestigateMode(4)
        entl8.SetInvestigateModeCombat(4)
        entl8.physdamagescale=1
        entl8.TweakParam("hearing 50")
        entl8.TweakParam("vision 250")
        entl8.AllowKickHintUse(1)
        entl8.LookAtEntityEye("!player")
        entl8.SetFollowerType("Default")
        entl8.SetFollowerBoss("!player")
        entl8.SetModel(model)
        entl8.PlayDialogFile("disciplines/necromancy/level4/Activate4.wav")
    except:
        pass
    __main__.CallEntitySpawn(entl8)
    entl8.SetScriptedDiscipline("shield_of_faith 3")
    entl8.SetScriptedDiscipline("potence 3")
    #entl8.SetScriptedDiscipline("holy_light 5")
    return entl8

################
def SummonSkeletonMain():
    skeleton = __main__.FindEntityByName("skeleton")
    allyskeleton = __main__.FindEntityByName("allyskeleton")
    if(allyskeleton):
       __main__.FindPlayer().Bloodgain(3)
       return
    else:
       entityType="npc_VGhoulCroucher"
       model="models/null.mdl"
       skeleton="skeleton"
       offset = round(360)
       ally8 = SpawnSkeletonAlly(skeleton, (180 + (offset)),entityType,model,-50)
       __main__.ScheduleTask(0.1,"castnecromancy.SummonSkeletonMain1()")
       __main__.ScheduleTask(0.1,"castnecromancy.Activate5Summon(3)")

################
def SummonSkeletonMain1():
    skeleton = __main__.FindEntityByName("skeleton")
    allyskeleton = __main__.FindEntityByName("allyskeleton")
    if skeleton:
       __main__.ScheduleTask(0.1,"castnecromancy.SummonSkeleton()")
       skeleton.SetModel("models/character/monster/undead/undead_male_sceleton.mdl")
       skeleton.SetGesture("praying_end")

################
def SummonSkeleton():
       skeleton = __main__.FindEntityByName("skeleton")
       allyskeleton = __main__.FindEntityByName("allyskeleton")

       allyskeleton=__main__.CreateEntityNoSpawn("prop_dynamic_ornament",skeleton.GetOrigin(),skeleton.GetAngles())
       allyskeleton.SetName("allyskeleton")
       allyskeleton.SetModel("models/character/npc/common/skeleton/skeleton_male.mdl")
       __main__.CallEntitySpawn(allyskeleton)
       allyskeleton = __main__.FindEntityByName("allyskeleton")
       if allyskeleton: 
	   allyskeleton.SetAttached("skeleton")
           __main__.ScheduleTask(60.0,"castnecromancy.SummonSkeleton2()")

def SummonSkeleton1():
       __main__.FindEntityByName("skeleton").PlayDialogFile("disciplines/necromancy/level4/Flyout4.wav")
       __main__.ScheduleTask(2.0,"castnecromancy.SummonSkeleton2()")

def SummonSkeleton2():
       __main__.FindEntityByName("allyskeleton").Kill()
       __main__.FindEntityByName("skeleton").Kill()

#-----------------------------------------------Level 4 Nagaraja---------------------------

def SpawnGhostAlly(entityName, angle, entityType, model, distance ):

    point = __main__.FindPlayer().TraceCircle(distance,angle)
    facing=(0,angle,0)

    entl9 = __main__.CreateEntityNoSpawn(entityType, point, facing )
    try:
        entl9.SetName(entityName)
        entl9.SetRelationship("player D_LI 5")
        entl9.pl_investigate=6
        entl9.pl_criminal_flee=6
        entl9.pl_criminal_attack=6
        entl9.pl_supernatural_flee=6
        entl9.pl_supernatural_attack=6
        entl9.SetInvestigateMode(4)
        entl9.SetInvestigateModeCombat(4)
        entl9.physdamagescale=1
        entl9.TweakParam("hearing 50")
        entl9.TweakParam("vision 250")
        entl9.AllowKickHintUse(1)
        entl9.LookAtEntityEye("!player")
        entl9.SetFollowerType("Default")
        entl9.SetFollowerBoss("!player")
        entl9.SetModel(model)
        #entl9.PlayDialogFile("disciplines/necromancy/level4/Activate4.wav")
        #entl9.WillTalk(1)
        #entl9.StartPlayerDialog("dlg/antitribu/Necromancer2.dlg")
        #entl9.PlayDialogFile("area/santa_monica/ocean_house/oceanhouse_ghost/help_me.wav")
    except:
        pass
    __main__.CallEntitySpawn(entl9)
    #entl9.SetScriptedDiscipline("shield_of_faith 2")
    #entl9.SetScriptedDiscipline("Animalism 1")
    return entl9

################
def SummonNagarajaGhost():
    ghost = __main__.FindEntityByName("ghost")
    if(ghost):
       __main__.FindPlayer().Bloodgain(3)
       return
    else:
       entityType="npc_VGhoulCroucher"
       model="models/null.mdl"
       ghost="ghost"
       offset = round(360)
       ally9 = SpawnGhostAlly(ghost, (180 + (offset)),entityType,model,-40)
       __main__.ScheduleTask(0.1,"castnecromancy.SummonNagarajaGhost1()")
       __main__.ScheduleTask(0.1,"castnecromancy.Activate5Summon(2)")

################
def SummonNagarajaGhost1():
    ghost = __main__.FindEntityByName("ghost")
    if ghost:
       __main__.ScheduleTask(60.1,"castnecromancy.SummonNagarajaGhost2()")
       ghost.SetModel("models/weapons/disciplines/Necromancy/ghost/ghost.mdl")
       ghost.MakeInvincible(1)
       ghost.SetGesture("ghost_tablelook_0")
       ghost.SetScriptedDiscipline("shield_of_faith 2")

def SummonNagarajaGhost2():
       __main__.FindEntityByName("ghost").PlayDialogFile("area/santa_monica/ocean_house/oceanhouse_ghost/help_me.wav")
       __main__.ScheduleTask(2.1,"castnecromancy.SummonNagarajaGhost3()")

def SummonNagarajaGhost3():
       __main__.FindEntityByName("ghost").Kill()

#-----------------------------------------------Level 5 Nagaraja---------------------------

def SpawnSpecterAlly(entityName, angle, entityType, model, distance ):

    point = __main__.FindPlayer().TraceCircle(distance,angle)
    facing=(0,angle,0)

    entl10 = __main__.CreateEntityNoSpawn(entityType, point, facing )
    try:
        entl10.SetName(entityName)
        entl10.SetRelationship("player D_LI 5")
        entl10.pl_investigate=6
        entl10.pl_criminal_flee=6
        entl10.pl_criminal_attack=6
        entl10.pl_supernatural_flee=6
        entl10.pl_supernatural_attack=6
        entl10.SetInvestigateMode(4)
        entl10.SetInvestigateModeCombat(4)
        entl10.physdamagescale=1
        entl10.TweakParam("hearing 50")
        entl10.TweakParam("vision 250")
        entl10.AllowKickHintUse(1)
        entl10.LookAtEntityEye("!player")
        entl10.SetFollowerType("Default")
        entl10.SetFollowerBoss("!player")
        entl10.SetModel(model)
    except:
        pass
    __main__.CallEntitySpawn(entl10)
    entl10.SetScriptedDiscipline("shield_of_faith 5")
    return entl10

################
def SummonSpecterMain():
    specter = __main__.FindEntityByName("specter")
    specterclone = __main__.FindEntityByName("specterclone")
    if(specterclone):
       __main__.FindPlayer().Bloodgain(3)
       return
    else:
       entityType="npc_VGhoulCroucher"
       model="models/null.mdl"
       specter="specter"
       offset = round(360)
       ally10 = SpawnSpecterAlly(specter, (180 + (offset)),entityType,model,-40)
       __main__.ScheduleTask(0.1,"castnecromancy.SummonSpecterMain1()")
       __main__.ScheduleTask(0.1,"castnecromancy.Activate5Summon(2)")

################
def SummonSpecterMain1():
    specter = __main__.FindEntityByName("specter")

    if specter:
       __main__.ScheduleTask(0.1,"castnecromancy.SummonSpecter()")
       __main__.ScheduleTask(0.1,"castnecromancy.SummonSpectera()")
       __main__.ScheduleTask(0.1,"castnecromancy.SummonSpecterb()")
       specter.SetModel("models/character/monster/undead/undead_male_sceleton.mdl")
       specter.SetGesture("ACT_SLEEP_GETUP")
       specter.MakeInvincible(1)

################################ specter Clones 
def SummonSpecter():
       specter = __main__.FindEntityByName("specter")
       specterclone = __main__.FindEntityByName("specterclone")

       specterclone=__main__.CreateEntityNoSpawn("prop_dynamic_ornament",specter.GetOrigin(),specter.GetAngles())
       specterclone.SetName("specterclone")
       specterclone.SetModel("models/weapons/disciplines/Necromancy/skeleton_ghost/ghost_stuff.mdl")
       __main__.CallEntitySpawn(specterclone)
       specterclone = __main__.FindEntityByName("specterclone")
       if specterclone: 
	   specterclone.SetAttached("specter")
           __main__.ScheduleTask(40.1,"castnecromancy.SummonSpecterEnd()")

def SummonSpectera():
       specter = __main__.FindEntityByName("specter")
       specterclone1 = __main__.FindEntityByName("specterclone1")

       specterclone1=__main__.CreateEntityNoSpawn("prop_dynamic_ornament",specter.GetOrigin(),specter.GetAngles())
       specterclone1.SetName("specterclone1")
       specterclone1.SetModel("models/weapons/disciplines/Necromancy/skeleton_ghost/skeleton_male_ghost.mdl")
       __main__.CallEntitySpawn(specterclone1)
       specterclone1 = __main__.FindEntityByName("specterclone1")
       if specterclone1: specterclone1.SetAttached("specter")

def SummonSpecterb():
       specter = __main__.FindEntityByName("specter")
       specterclone2 = __main__.FindEntityByName("specterclone2")

       specterclone2=__main__.CreateEntityNoSpawn("prop_dynamic_ornament",specter.GetOrigin(),specter.GetAngles())
       specterclone2.SetName("specterclone2")
       specterclone2.SetModel("models/weapons/disciplines/Necromancy/skeleton_ghost/ghost_cuirasse.mdl")
       __main__.CallEntitySpawn(specterclone2)
       specterclone2 = __main__.FindEntityByName("specterclone2")
       if specterclone2: specterclone2.SetAttached("specter")

#-----------------------------------------------
def SummonSpecterEnd():
       __main__.FindEntityByName("specter").PlayDialogFile("environmental/spooky/ghost 1.wav")
       __main__.ScheduleTask(4.0,"castnecromancy.SummonSpecterEnd1()")

def SummonSpecterEnd1():
       __main__.FindEntityByName("specterclone").Kill()
       __main__.FindEntityByName("specterclone1").Kill()
       __main__.FindEntityByName("specterclone2").Kill()
       __main__.FindEntityByName("specter").Kill()