#FILENAME : castanimalism.py

import __main__
from __main__ import Character

############################

import consoleutil

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
def SummonRavens():
       ravens = __main__.FindEntityByName("ravens")
       pc=__main__.FindPlayer()
       if(ravens):
          __main__.FindPlayer().Bloodgain(1)
          consoleutil.console("say Must wait to use that Discipline again")
          return
       else:
          __main__.ScheduleTask(0.1,"castanimalism.Activate2Summon(1)")
          ravens=__main__.CreateEntityNoSpawn("npc_VHuman",pc.GetOrigin(),pc.GetAngles())
          ravens.SetName("ravens")
          ravens.SetModel("models/null.mdl")
          __main__.CallEntitySpawn(ravens)
          ravens = __main__.FindEntityByName("ravens")
          if ravens:
              ravens.SetParent("!player")
              ravens.SetOrigin(pc.GetOrigin())
              ravens.SetAngles(pc.GetAngles())
              ravens.SetModel("models/weapons/disciplines/animalism/null.mdl")
              __main__.ScheduleTask(0.1,"castanimalism.SummonRavens1()")

def SummonRavens1():
       __main__.FindEntityByName('ravens').ChangeSchedule('SCHED_TROIKA_D_RAVENS')
       __main__.ScheduleTask(12.0,"castanimalism.SummonRavens2()")

def SummonRavens2():
       __main__.FindEntityByName('ravens').Kill()

#-----------------------------------------------Level 1 helper---------------------------

def SpawnBloodAlly2(entityName, angle, entityType, model, distance ):

    point = __main__.FindPlayer().TraceCircle(distance,angle)
    facing=(0,angle,0)

    entl2 = __main__.CreateEntityNoSpawn(entityType, point, facing )
    try:
        entl2.SetName(entityName)
        entl2.SetRelationship("player D_LI 5")
        entl2.pl_investigate=6
        entl2.pl_criminal_flee=6
        entl2.pl_criminal_attack=6
        entl2.pl_supernatural_flee=6
        entl2.pl_supernatural_attack=6
        entl2.SetInvestigateMode(4)
        entl2.SetInvestigateModeCombat(4)
        entl2.physdamagescale=1.0
        entl2.TweakParam("hearing 50")
        entl2.TweakParam("vision 250")
        entl2.AllowKickHintUse(1)
        entl2.LookAtEntityEye("!player")
        entl2.SetFollowerType("Default")
        entl2.SetFollowerBoss("!player")
        entl2.SetModel(model)     
        entl2.MakeInvincible(1)
        entl2.PlayDialogFile("disciplines/animalism/nightwisp ravens/anm_lvl1_loop.wav")
    except:
        pass
    __main__.CallEntitySpawn(entl2)
    return entl2

def RemoveBloodAlly2(aname):
    ally2 = __main__.FindEntityByName(aname)
    if ally2:
        #ally2.SetScriptedDiscipline("obfuscate 4")
        __main__.ScheduleTask(1.0,"__main__.FindEntityByName('%s').Kill()" % aname)

################################################################################################

ally2Index=1
def Activate2Summon(level=1):
    global ally2Index

    entityType="npc_VRat"
    model="models/null.mdl"

    timeout=11
    offset = round(360/level)
    while level > 0:
        aname = "_my_ally_a2_%d" % ally2Index
        ally2 = SpawnBloodAlly2(aname, (-180 + (offset * level)),entityType,model,-5)
        if -1 != timeout:
            __main__.ScheduleTask(timeout,"castanimalism.RemoveBloodAlly2('%s')" % aname)
        level=level-1
        ally2Index=ally2Index+1

#-----------------------------------------------Level 2---------------------------
def SummonRats():
       rats = __main__.FindEntityByName("rats")
       pc=__main__.FindPlayer()
       if(rats):
          __main__.FindPlayer().Bloodgain(1)
          consoleutil.console("say Must wait to use that Discipline again")
          return
       else:
          __main__.ScheduleTask(0.1,"castanimalism.Activate1Summon(4)")
          rats=__main__.CreateEntityNoSpawn("npc_VHuman",pc.GetOrigin(),pc.GetAngles())
          rats.SetName("rats")
          rats.SetModel("models/null.mdl")
          __main__.CallEntitySpawn(rats)
          rats = __main__.FindEntityByName("rats")
          if rats:
              rats.SetParent("!player")
              rats.SetOrigin(pc.GetOrigin())
              rats.SetAngles(pc.GetAngles())
              rats.SetModel("models/weapons/disciplines/animalism/null.mdl")
              __main__.ScheduleTask(25.0,"castanimalism.SummonRats1()")

def SummonRats1():
       __main__.FindEntityByName('rats').Kill()

#-----------------------------------------------Level 2 helper---------------------------

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
        entl1.PlayDialogFile("disciplines/animalism/level1/anm_lvl1_activate.wav")
    except:
        pass
    __main__.CallEntitySpawn(entl1)
    
    entl1.SetScriptedDiscipline("mind_shield 4")
    return entl1

def RemoveBloodAlly1(aname):
    ally1 = __main__.FindEntityByName(aname)
    if ally1:
        #ally1.SetScriptedDiscipline("obfuscate 4")
        __main__.ScheduleTask(3.0,"__main__.FindEntityByName('%s').Kill()" % aname)

################################################################################################

ally1Index=1
def Activate1Summon(level=1):
    global ally1Index

    entityType="npc_VRat"
    model="models/weapons/disciplines/animalism/black_rat.mdl"
    #model="models/character/monster/mingxiao/mingxiao_baby/mingxiao_baby.mdl"

    timeout=60

    offset = round(360/level)
    while level > 0:
        aname = "_my_ally_a1_%d" % ally1Index
        ally1 = SpawnBloodAlly1(aname, (-180 + (offset * level)),entityType,model,-70)
        if -1 != timeout:
            __main__.ScheduleTask(timeout,"castanimalism.RemoveBloodAlly1('%s')" % aname)
        level=level-1
        ally1Index=ally1Index+1

#-----------------------------------------------Level 3---------------------------

def SpawnDogAlly(entityName, angle, entityType, model, distance ):

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
        entl4.physdamagescale=1
        entl4.TweakParam("hearing 50")
        entl4.TweakParam("vision 250")
        entl4.AllowKickHintUse(1)
        entl4.LookAtEntityEye("!player")
        entl4.SetFollowerType("Default")
        entl4.SetFollowerBoss("!player")
        entl4.SetModel(model)
        entl4.PlayDialogFile("disciplines/animalism/level3/anm_lvl3_activate.wav")
    except:
        pass
    __main__.CallEntitySpawn(entl4)
    entl4.SetScriptedDiscipline("mind_shield 4")
    return entl4

################
def SummonDogMain():
    dog = __main__.FindEntityByName("dog")
    allydog = __main__.FindEntityByName("allydog")
    if(allydog):
       __main__.FindPlayer().Bloodgain(2)
       consoleutil.console("say Must wait to use that Discipline again")
       return
    else:
       entityType="npc_VGhoulCroucher"
       model="models/null.mdl"
       dog="dog"
       offset = round(360)
       ally = SpawnDogAlly(dog, (180 + (offset)),entityType,model,-50)
       __main__.ScheduleTask(0.1,"castanimalism.SummonDogMain1()")

################
def SummonDogMain1():
    dog = __main__.FindEntityByName("dog")
    allydog = __main__.FindEntityByName("allydog")
    if dog:
       __main__.ScheduleTask(0.1,"castanimalism.SummonDogs()")
       dog.SetModel("models/character/monster/wolf_form/wolf_form_null.mdl")
       dog.SetGesture("sit_outof")

################
def SummonDogs():
       dog = __main__.FindEntityByName("dog")
       allydog = __main__.FindEntityByName("allydog")

       allydog=__main__.CreateEntityNoSpawn("prop_dynamic_ornament",dog.GetOrigin(),dog.GetAngles())
       allydog.SetName("allydog")
       allydog.SetModel("models/character/monster/dog/guard/dog_guard.mdl")
       __main__.CallEntitySpawn(allydog)
       allydog = __main__.FindEntityByName("allydog")
       if allydog: 
	   allydog.SetAttached("dog")
           __main__.ScheduleTask(20.1,"castanimalism.SummonDogs1()")

def SummonDogs1():
       __main__.FindEntityByName("allydog").Kill()
       __main__.FindEntityByName("dog").Kill()

#-----------------------------------------------Level 4---------------------------
def SummonWolf():
       Wolf = __main__.FindEntityByName("Wolf")
       pc=__main__.FindPlayer()
       if(Wolf):
          __main__.FindPlayer().Bloodgain(3)
          consoleutil.console("say Must wait to use that Discipline again")       
          return
       else:
          __main__.ScheduleTask(0.1,"castanimalism.Activate3Summon(1)")
          Wolf=__main__.CreateEntityNoSpawn("npc_VHuman",pc.GetOrigin(),pc.GetAngles())
          Wolf.SetName("Wolf")
          Wolf.SetModel("models/null.mdl")
          __main__.CallEntitySpawn(Wolf)
          Wolf = __main__.FindEntityByName("Wolf")
          if Wolf:
              Wolf.SetParent("!player")
              Wolf.SetOrigin(pc.GetOrigin())
              Wolf.SetAngles(pc.GetAngles())
              Wolf.SetModel("models/weapons/disciplines/animalism/null.mdl")
              __main__.ScheduleTask(30.0,"castanimalism.SummonWolf1()")

def SummonWolf1():
       __main__.FindEntityByName('Wolf').Kill()

#-----------------------------------------------Level 5---------------------------

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
        entl3.PlayDialogFile("disciplines/animalism/level5/anm_lvl5_activate.wav")
    except:
        pass
    __main__.CallEntitySpawn(entl3)
    
    entl3.SetScriptedDiscipline("mind_shield 5")
    return entl3

def RemoveBloodAlly3(aname):
    ally3 = __main__.FindEntityByName(aname)
    if ally3:
        ally3.SetModel("models/weapons/disciplines/animalism/grey_wolf.mdl")
        ally3.SetGesture("sit_outof")                       
        __main__.ScheduleTask(60.0,"__main__.FindEntityByName('%s').Kill()" % aname)

###############################################################################################

ally3Index=1
def Activate3Summon(level=1):
    global ally3Index

    entityType="npc_VGhoulCroucher"
    model="models/weapons/disciplines/animalism/grey_wolf.mdl"

    timeout=0.1

    offset = round(360/level)
    while level > 0:
        aname = "_my_ally_a3_%d" % ally3Index
        ally3 = SpawnBloodAlly3(aname, (-180 + (offset * level)),entityType,model,-70)
        if -1 != timeout:
            __main__.ScheduleTask(timeout,"castanimalism.RemoveBloodAlly3('%s')" % aname)
        level=level-1
        ally3Index=ally3Index+1

#-----------------------------------------------end---------------------------