############################
#FILENAME : castkoldunism.py
############################
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
##########################################################################################
##----------------------------------------- Cast koldunism----------------------------------
def castDialog():
    pc = __main__.FindPlayer()
    npc = __main__.FindEntityByName("koldunic_npc1")
    level = 1
    offset = round(360/level)
    #angle = (-180 + (offset * level)) 
    angle = (offset * level)   

    point = __main__.FindPlayer().TraceCircle(-50,(-180 + (offset * level)))
    facing=(0,angle,0)

    npc.SetAngles(facing)
    npc.SetOrigin(point)
    __main__.ScheduleTask(0.1,"castkoldunism.castDialog1()")

def castDialog1():
    __main__.FindEntityByName("koldunic_npc1").StartPlayerDialog(1)


def castDialog1X():
    #__main__.FindEntityByName("koldunic_npc1").StartPlayerDialog(1)
    npc = __main__.FindEntityByName("koldunic_npc1")
    npc.SetScriptedDiscipline("shield_of_faith 3")
    npc.SetModel("models/weapons/disciplines/koldunism/frankenstein/frankenstein.mdl")
    npc.MakeInvincible(0)
    npc.PlayDialogFile("area/santa_monica/ocean_house/oceanhouse_ghost/help_me.wav")
    npc.SetRelationship("player D_LI 5")
    npc.SetFollowerType("Default")
    npc.SetFollowerBoss("!player")

#returns the distanceSquared between two 3D points
def distanceSquared(p1, p2):
    xDistance = (p1[0] - p2[0]) * (p1[0] - p2[0])
    yDistance = (p1[1] - p2[1]) * (p1[1] - p2[1])
    zDistance = (p1[2] - p2[2]) * (p1[2] - p2[2])
    return (xDistance + yDistance + zDistance)


##########################################################################################
##----------------------------------------- LEVEL 1----------------------------------
#------------------------- thing 1-------------------
def Spawn1thing(entityName, angle, entityType, model, distance ):

    point = __main__.FindPlayer().TraceCircle(distance,angle)
    facing=(0,angle,0)

    entl1 = __main__.CreateEntityNoSpawn(entityType, point, facing )
    try:
        entl1.SetName(entityName)
        entl1.physdamagescale=1
        entl1.SetModel(model)
    except:
        pass
    __main__.CallEntitySpawn(entl1)
    return entl1

############### 
ally1Index=1
def Activate1Summon(level=1):
    global ally1Index

    entityType="item_w_baton"
    model="models/null.mdl"

    offset = round(360/level)
    while level > 0:
        aname = "_my_ally_k1_%d" % ally1Index
        ally1 = Spawn1thing(aname, (-180 + (offset * level)),entityType,model,-50)

        level=level-1
        ally1Index=ally1Index+1

#------------------------- thing 2-------------------
def Spawn2thing(entityName, angle, entityType, model, distance ):

    point = __main__.FindPlayer().TraceCircle(distance,angle)
    facing=(0,angle,0)

    entl2 = __main__.CreateEntityNoSpawn(entityType, point, facing )
    try:
        entl2.SetName(entityName)
        entl2.physdamagescale=1
        entl2.SetModel(model)
    except:
        pass
    __main__.CallEntitySpawn(entl2)
    return entl2

################
ally2Index=1
def Activate2Summon(level=1):
    global ally2Index

    entityType="prop_physics"
    model="models/scenery/PHYSICS/sardine/sardine.mdl"

    offset = round(360/level)
    while level > 0:
        aname = "_my_ally_k2_%d" % ally2Index
        ally2 = Spawn2thing(aname, (-180 + (offset * level)),entityType,model,-50)

        level=level-1
        ally2Index=ally2Index+1

#------------------------- thing 3-------------------
def Spawn3thing(entityName, angle, entityType, model, distance ):

    point = __main__.FindPlayer().TraceCircle(distance,angle)
    facing=(0,angle,0)

    entl3 = __main__.CreateEntityNoSpawn(entityType, point, facing )
    try:
        entl3.SetName(entityName)
        entl3.physdamagescale=1
        #entl3.override_mass=10
        #entl3.npc_kickable=1
        #entl3.health=20
        entl3.ExplodeDamage=100
        entl3.ExplodeRadius=100
        entl3.SetModel(model)
    	entl3.SetCausesImpactDamage(100)
    	#entl3.SetHealth(250)
    except:
        pass
    __main__.CallEntitySpawn(entl3)
    return entl3

################
ally3Index=1
def Activate3Summon(level=1):
    global ally3Index

    entityType="prop_physics"
    model="models/scenery/furniture/chairwingback/chairwingback.mdl"

    offset = round(360/level)
    while level > 0:
        aname = "_my_ally_k3_%d" % ally3Index
        ally3 = Spawn3thing(aname, (-180 + (offset * level)),entityType,model,-50)

        level=level-1
        ally3Index=ally3Index+1

##----------------------------------------- LEVEL 2----------------------------------
#------------------------- thing 1-------------------
def Spawn4thing(entityName, angle, entityType, model, distance ):

    point = __main__.FindPlayer().TraceCircle(distance,angle)
    facing=(0,angle,0)

    entl4 = __main__.CreateEntityNoSpawn(entityType, point, facing )
    try:
        entl4.SetName(entityName)
        entl4.physdamagescale=1
        entl4.SetModel(model)
    except:
        pass
    __main__.CallEntitySpawn(entl4)
    return entl4

############### 
ally4Index=1
def Activate4Summon(level=1):
    global ally4Index

    entityType="item_w_katana"
    model="models/null.mdl"

    offset = round(360/level)
    while level > 0:
        aname = "_my_ally_k4_%d" % ally4Index
        ally4 = Spawn4thing(aname, (-180 + (offset * level)),entityType,model,-50)

        level=level-1
        ally4Index=ally4Index+1

#------------------------- thing 2-------------------
def Spawn5thing(entityName, angle, entityType, model, distance ):

    point = __main__.FindPlayer().TraceCircle(distance,angle)
    facing=(0,angle,0)

    entl5 = __main__.CreateEntityNoSpawn(entityType, point, facing )
    try:
        entl5.SetName(entityName)
        entl5.physdamagescale=1
        entl5.SetModel(model)
    except:
        pass
    __main__.CallEntitySpawn(entl5)
    return entl5

############### 
ally5Index=1
def Activate5Summon(level=1):
    global ally5Index

    entityType="item_p_occult_obfuscate"
    model="models/null.mdl"

    offset = round(360/level)
    while level > 0:
        aname = "_my_ally_k5_%d" % ally5Index
        ally5 = Spawn5thing(aname, (-180 + (offset * level)),entityType,model,-50)

        level=level-1
        ally5Index=ally5Index+1

#------------------------- thing 3-------------------
def Spawn6thing(entityName, angle, entityType, model, distance ):

    point = __main__.FindPlayer().TraceCircle(distance,angle)
    facing=(0,angle,0)

    entl6 = __main__.CreateEntityNoSpawn(entityType, point, facing )
    try:
        entl6.solid=6
        entl6.SetName(entityName)
        entl6.physdamagescale=1
        entl6.SetModel(model)
        entl6.SetCausesImpactDamage(200)
    	entl6.SetHealth(300)
    except:
        pass
    __main__.CallEntitySpawn(entl6)
    return entl6

###############
ally6Index=1
def Activate6Summon(level=1):
    global ally6Index

    entityType="prop_physics"
    model="models/scenery/structural/warehouse/break_crate.mdl"

    offset = round(360/level)
    while level > 0:
        aname = "_my_ally_k6_%d" % ally6Index
        ally6 = Spawn6thing(aname, (-180 + (offset * level)),entityType,model,-50)

        level=level-1
        ally6Index=ally6Index+1

##----------------------------------------- LEVEL 3----------------------------------
#------------------------- thing 1-------------------
def Spawn7thing(entityName, angle, entityType, model, distance ):

    point = __main__.FindPlayer().TraceCircle(distance,angle)
    facing=(0,angle,0)

    entl7 = __main__.CreateEntityNoSpawn(entityType, point, facing )
    try:
        entl7.SetName(entityName)
        entl7.physdamagescale=1
        entl7.SetModel(model)
    except:
        pass
    __main__.CallEntitySpawn(entl7)
    return entl7

############### 
ally7Index=1
def Activate7Summon(level=1):
    global ally7Index

    entityType="item_w_uzi"
    model="models/null.mdl"

    offset = round(360/level)
    while level > 0:
        aname = "_my_ally_k7_%d" % ally7Index
        ally7 = Spawn7thing(aname, (-180 + (offset * level)),entityType,model,-50)

        level=level-1
        ally7Index=ally7Index+1

#------------------------- thing 2-------------------
def Spawn8thing(entityName, angle, entityType, model, distance ):

    point = __main__.FindPlayer().TraceCircle(distance,angle)
    facing=(0,angle,0)

    entl8 = __main__.CreateEntityNoSpawn(entityType, point, facing )
    try:
        entl8.SetName(entityName)
        entl8.physdamagescale=1
        entl8.SetModel(model)
    except:
        pass
    __main__.CallEntitySpawn(entl8)
    return entl8

############### 
ally8Index=1
def Activate8Summon(level=1):
    global ally8Index

    entityType="item_g_watch_fancy"
    model="models/null.mdl"

    offset = round(360/level)
    while level > 0:
        aname = "_my_ally_k8_%d" % ally8Index
        ally8 = Spawn8thing(aname, (-180 + (offset * level)),entityType,model,-50)

        level=level-1
        ally8Index=ally8Index+1

##----------------------------------------- LEVEL 4----------------------------------
#------------------------- thing 1-------------------
def Spawn9thing(entityName, angle, entityType, model, distance ):

    point = __main__.FindPlayer().TraceCircle(distance,angle)
    facing=(0,angle,0)

    entl9 = __main__.CreateEntityNoSpawn(entityType, point, facing )
    try:
        entl9.SetName(entityName)
        entl9.physdamagescale=1
        entl9.SetModel(model)
    except:
        pass
    __main__.CallEntitySpawn(entl9)
    return entl9

############### 
ally9Index=1
def Activate9Summon(level=1):
    global ally9Index

    entityType="item_w_grenade_frag"
    model="models/null.mdl"

    offset = round(360/level)
    while level > 0:
        aname = "_my_ally_k9_%d" % ally9Index
        ally9 = Spawn9thing(aname, (-180 + (offset * level)),entityType,model,-50)

        level=level-1
        ally9Index=ally9Index+1

#------------------------- thing 2-------------------
def Spawn10thing(entityName, angle, entityType, model, distance ):

    point = __main__.FindPlayer().TraceCircle(distance,angle)
    facing=(0,angle,0)

    entl10 = __main__.CreateEntityNoSpawn(entityType, point, facing )
    try:
        entl10.SetName(entityName)
        entl10.physdamagescale=1
        entl10.SetModel(model)
    except:
        pass
    __main__.CallEntitySpawn(entl10)
    return entl10

############### 
ally10Index=1
def Activate10Summon(level=1):
    global ally10Index

    entityType="item_g_jumbles_flyer"
    model="models/null.mdl"

    offset = round(360/level)
    while level > 0:
        aname = "_my_ally_k10_%d" % ally10Index
        ally10 = Spawn10thing(aname, (-180 + (offset * level)),entityType,model,-50)

        level=level-1
        ally10Index=ally10Index+1

##----------------------------------------- LEVEL 5 ----------------------------------
##Humanoid

def Spawn11Ally(entityName, angle, entityType, model, distance ):

    point = __main__.FindPlayer().TraceCircle(distance,angle)
    facing=(0,angle,0)

    entl11 = __main__.CreateEntityNoSpawn(entityType, point, facing )

    try:
        entl11.SetName(entityName)
        entl11.SetRelationship("player D_LI 5")
        entl11.pl_investigate=6
        entl11.pl_criminal_flee=6
        entl11.pl_criminal_attack=6
        entl11.pl_supernatural_flee=6
        entl11.pl_supernatural_attack=6
        entl11.SetInvestigateMode(4)
        entl11.SetInvestigateModeCombat(4)
        entl11.physdamagescale=1.0
        entl11.TweakParam("hearing 50")
        entl11.TweakParam("vision 250")
        entl11.AllowKickHintUse(1)
        entl11.LookAtEntityEye("!player")
        entl11.SetFollowerType("Default")
        entl11.SetFollowerBoss("!player")
        entl11.SetModel(model)
    except:
        pass
    __main__.CallEntitySpawn(entl11)
    
    entl11.SetScriptedDiscipline("shield_of_faith 3")
    #entl11.SetScriptedDiscipline("mind_shield 3")
    return entl11

def Set11Ally(aname):
    ally11 = __main__.FindEntityByName(aname)
    if ally11:
        ally11.SetModel("models/weapons/disciplines/koldunism/humanoid/humanoid.mdl")
        ally11.SetGesture("ACT_SLEEP_GETUP")
    	ally11.SetScriptedDiscipline("fortitude 3")
    	ally11.SetScriptedDiscipline("potence 3")
        __main__.ScheduleTask(60.0,"castkoldunism.Remove11Ally('%s')" % aname)

def Remove11Ally(aname):
    ally11 = __main__.FindEntityByName(aname)
    if ally11:
        ally11.SetScriptedDiscipline("obfuscate 4")
        __main__.ScheduleTask(2.0,"__main__.FindEntityByName('%s').Kill()" % aname)

################----------------------------------
ally11Index=1
def Activate11Summon(level=1):
    global ally11Index

    entityType="npc_VGhoulCroucher"
    model="models/null.mdl"

    offset = round(360/level)
    while level > 0:
        aname = "_my_ally_k11_%d" % ally11Index
        ally11 = Spawn11Ally(aname, (-180 + (offset * level)),entityType,model,-50)
        __main__.ScheduleTask(0.1,"castkoldunism.Set11Ally('%s')" % aname)
        level=level-1
        ally11Index=ally11Index+1

##---------------------------------------------------------------------------
##frankenstein's monster

def Spawn12Ally(entityName, angle, entityType, model, distance ):

    point = __main__.FindPlayer().TraceCircle(distance,angle)
    facing=(0,angle,0)

    entl12 = __main__.CreateEntityNoSpawn(entityType, point, facing )

    try:
        entl12.SetName(entityName)
        entl12.SetRelationship("player D_LI 5")
        entl12.pl_investigate=6
        entl12.pl_criminal_flee=6
        entl12.pl_criminal_attack=6
        entl12.pl_supernatural_flee=6
        entl12.pl_supernatural_attack=6
        entl12.SetInvestigateMode(4)
        entl12.SetInvestigateModeCombat(4)
        entl12.physdamagescale=1.0
        entl12.TweakParam("hearing 50")
        entl12.TweakParam("vision 250")
        entl12.AllowKickHintUse(1)
        entl12.LookAtEntityEye("!player")
        entl12.SetFollowerType("Default")
        entl12.SetFollowerBoss("!player")
        entl12.SetModel(model)
        entl12.MakeInvincible(1)
    except:
        pass
    __main__.CallEntitySpawn(entl12)
    
    entl12.SetScriptedDiscipline("shield_of_faith 4")
    return entl12

def Set12Ally(aname):
    ally12 = __main__.FindEntityByName(aname)
    if ally12:
        ally12.SetModel("models/weapons/disciplines/koldunism/frankenstein/frankenstein.mdl")
        ally12.SetGesture("ACT_SLEEP_GETUP")
    	ally12.SetScriptedDiscipline("fortitude 5")
    	ally12.SetScriptedDiscipline("potence 5")
	__main__.ScheduleTask(30.0,"castkoldunism.Invincible12Ally('%s')" % aname)
        __main__.ScheduleTask(60.0,"castkoldunism.Remove12Ally('%s')" % aname)
        __main__.ScheduleTask(1.0,"castObteneblvl4HelperAura()")

def Invincible12Ally(aname):
    ally12 = __main__.FindEntityByName(aname)
    if ally12:
        ally12.MakeInvincible(0)

def Remove12Ally(aname):
    ally12 = __main__.FindEntityByName(aname)
    if ally12:
        ally12.SetScriptedDiscipline("obfuscate 4")
        __main__.ScheduleTask(2.0,"__main__.FindEntityByName('%s').Kill()" % aname)

################----------------------------------
ally12Index=1
def Activate12Summon(level=1):
    global ally12Index

    entityType="npc_VGhoulCroucher"
    model="models/null.mdl"

    offset = round(360/level)
    while level > 0:
        aname = "_my_ally_k12_%d" % ally12Index
        ally12 = Spawn12Ally(aname, (-180 + (offset * level)),entityType,model,-50)
        __main__.ScheduleTask(0.1,"castkoldunism.Set12Ally('%s')" % aname)
        level=level-1
        ally12Index=ally12Index+1

################----------------------------------
#----------------------------------------------- Koldunism select level ---------------------------
def KoldunicSelectLevelStart():
    pc=__main__.FindPlayer()
    clan = pc.clan
    koldunichelper = __main__.FindEntityByName("koldunic_npc1")
    if(clan == 4):
        if(koldunichelper):
            consoleutil.console("say Must wait to use that Discipline again")
        else:
            __main__.ScheduleTask(0.0,"castkoldunism.KoldunicSelectLevelStart1()")
    else:
        consoleutil.console("say You don't have Koldunic Sorcery")

def KoldunicSelectLevelStart1():
    __main__.FindEntityByName("koldunic_helper").Spawn()
    __main__.ScheduleTask(0.15,"castkoldunism.castDialog()")
    __main__.FindPlayer().PlayHUDParticle("d-koldunic-wof-cast-hud-emitter")
    __main__.FindPlayer().SpawnTempParticle("KoldunismCast_particle")
    __main__.ccmd.SoundKoldunic=""

################
def KoldunicSelectLevel(level):                                     
    if(level == 1):
        __main__.G.Last_Koldunism_Level = 1
        consoleutil.console("say Koldunism select level 1: Shatter")
    elif(level == 2):
        __main__.G.Last_Koldunism_Level = 2
        consoleutil.console("say Koldunism select level 2: Magma Surge")
    elif(level == 3):
        __main__.G.Last_Koldunism_Level = 3
        consoleutil.console("say Koldunism select level 3: Gates Of Magma")
    elif(level == 4):
        __main__.G.Last_Koldunism_Level = 4
        consoleutil.console("say Koldunism select level 4: Heat Wave")
    elif(level == 5):
        __main__.G.Last_Koldunism_Level = 5
        consoleutil.console("say Koldunism select level 5: Volcanic Blast")
    else:
	consoleutil.console("say Koldunism level not choosen. Use inventory icon 'Koldunism' or Koldunic Sorcery Hotkey ('v' by default).")

#----------------------------------------------- Koldunism choose level ---------------------------
################
def PlayerKoldunicSelectLevel():
    pc = __main__.FindPlayer()
    bp = pc.base_bloodpool                                       
    if(__main__.G.Last_Koldunism_Level == 1):
        if(pc.base_bloodpool >= 1):
            __main__.ScheduleTask(0.0,"castkoldunism.KoldunicStrikeAttack()")
        else:
            consoleutil.console("say Need blood")
    elif(__main__.G.Last_Koldunism_Level == 2):
        if(pc.base_bloodpool >= 2):
            __main__.ScheduleTask(0.0,"castkoldunism.CastMagmaSurge()")
        else:
            consoleutil.console("say Need 2 blood points")
    elif(__main__.G.Last_Koldunism_Level == 3):
        if(pc.base_bloodpool >= 3):
            __main__.ScheduleTask(0.0,"castkoldunism.CastGatesOfMagma()")
        else:
            consoleutil.console("say Need 3 blood points")
    elif(__main__.G.Last_Koldunism_Level == 4):
        if(pc.base_bloodpool >= 4):
            __main__.ScheduleTask(0.0,"castkoldunism.CastHeatWave()")
        else:
            consoleutil.console("say Need 4 blood points")
    elif(__main__.G.Last_Koldunism_Level == 5):
        if(pc.base_bloodpool >= 5):
            __main__.ScheduleTask(0.0,"castkoldunism.CastVolcanicBlast()")
        else:
            consoleutil.console("say Need 5 blood points")
    else:
	consoleutil.console("say Koldunism level not choosen. Use inventory icon 'Koldunism' or Koldunic Sorcery Hotkey ('v' by default).")

#--------------------------------------------------------------------------
def KoldunicSkipAllLevels():
    __main__.G.Last_Koldunism_Level = 0

#----------------------------------------------- Koldunism fix xp ---------------------------
################

def KoldunicPlayerFixXp(level):
    pc = __main__.FindPlayer()
    xp = pc.base_experience
    spxp = (xp - level)
    consoleutil.console("giftxp %s" % spxp)

#----------------------------------------------- Koldunism bloodloss ---------------------------
################

def KoldunicPlayerBloodloss(level):
    pc = __main__.FindPlayer()
    bp = pc.base_bloodpool
    spcx = (bp - level)
    consoleutil.console("blood %s" % spcx)

#----------------------------------------------- Koldunism Level 1---------------------------
################				Shatter 		castkoldunism.KoldunicStrikeAttack()
def KoldunicStrikeAttack():
    if(__main__.G.MagmaShatterCounter == 1):
	consoleutil.console("say Must wait to use that Discipline again")
    else:
	__main__.G.MagmaShatterCounter = 1
	__main__.ScheduleTask(1.5,"castkoldunism.KoldunicStrikeAttack4()")
	__main__.grapple=None                                      
	__main__.ccmd.npc_freeze=""
	__main__.ScheduleTask(0.1,'castkoldunism.OnPlayerAttackHelper()')

def OnPlayerAttackHelper(found=0):
    global attackGrapple

    if (found==1):
        OnPlayerAttackBegin(attackGrapple)
    elif(found==2):
        OnPlayerAttackBegin1(attackGrapple)
    else:
        FindClass = __main__.FindEntitiesByClass
        npcs = FindClass("npc_VHumanCombatant") + FindClass("npc_VHumanCombatPatrol") + FindClass("npc_VDialogPedestrian") + FindClass("npc_VTzimisceHeadClaw") + FindClass("npc_VTzimisceRunner") + FindClass("npc_VVampire") + FindClass("npc_VHuman") + FindClass("npc_VPedestrian") + FindClass("npc_VCop") + FindClass("npc_VSabbatGunman") +FindClass("npc_VAsianVampire") + FindClass("npc_VChangBrosBlade") + FindClass("npc_VChangBrosClaw") + FindClass("npc_VLasombra") + FindClass("npc_VSabbatLeader") + FindClass("npc_VSheriffMan") + FindClass("npc_VTzimisce") 
        npcc = FindClass("npc_VGhoulCroucher") + FindClass("npc_VHengeyokai") + FindClass("npc_VZombie") + FindClass("npc_VVampireBoss") + FindClass("npc_VMingXiao") + FindClass("npc_VGargoyle") + FindClass("npc_VManBat")
        for npc in npcs:
            try:
                if (npc.playbackrate==0.00):
                    attackGrapple=npc
                    __main__.ccmd.npc_freeze="" 
                    __main__.ScheduleTask(0.1,'castkoldunism.OnPlayerAttackHelper(1)')                                              
                    break;
            except:
                pass
        for npc in npcc:
            try:
                if (npc.playbackrate==0.00):
                    attackGrapple=npc
                    __main__.ccmd.npc_freeze="" 
                    __main__.ScheduleTask(0.1,'castkoldunism.OnPlayerAttackHelper(2)')                                              
                    break;
            except:
                pass

def OnPlayerAttackBegin(target):
    pc = __main__.FindPlayer()
    target.TakeDamage(pc.base_manipulation*10+50)
    target.ChangeSchedule('SCHED_TROIKA_ONFIRE')
    target.SpawnTempParticle("KoldunismBodyFire_particle")
    target.PlayDialogFile("disciplines/koldunism/shatter_npc.wav")
    __main__.ScheduleTask(0.0,"castkoldunism.KoldunicStrikeAttack1()")

def OnPlayerAttackBegin1(target):
    target.ChangeSchedule('SCHED_TROIKA_ONFIRE')
    target.SpawnTempParticle("KoldunismBodyFire_particle")
    target.PlayDialogFile("disciplines/koldunism/VolcanicBlast_end.wav")
    __main__.ScheduleTask(0.0,"castkoldunism.KoldunicStrikeAttack1()")

def KoldunicStrikeAttack1():
    __main__.FindPlayer().PlayHUDParticle("d-koldunic-wof-cast-hud-emitter")
    __main__.FindPlayer().SetSupernaturalLevel(1)
    __main__.ScheduleTask(0.0,"castkoldunism.KoldunicPlayerBloodloss(1)")
    __main__.FindPlayer().SpawnTempParticle("KoldunismCast_particle")
    pevents = __main__.FindEntitiesByClass("events_player")
    __main__.ccmd.SoundKoldunic=""
    pevents[0].CreateControllerNPC()
    __main__.ScheduleTask(0.05,"castkoldunism.KoldunicStrikeAttack2()")

def KoldunicStrikeAttack2():
    playerclone =  __main__.FindEntityByName("!playercontroller")
    #playerclone.SetGesture("holy_light_cast")
    playerclone.SetGesture("payphone_hangup")
    __main__.ScheduleTask(0.60,"castkoldunism.KoldunicStrikeAttack3()")

def KoldunicStrikeAttack3():
    pevents = __main__.FindEntitiesByClass("events_player")
    pevents[0].RemoveControllerNPC()
    consoleutil.console("say Koldunic Sorcery: Shatter")

def KoldunicStrikeAttack4():
    __main__.G.MagmaShatterCounter = 0

#-----------------------------------------------Koldunism Level 2---------------------------
################				Magma Surge 

def SpawnMagmaSurgeAlly(entityName, angle, entityType, model, distance ):

    point = __main__.FindPlayer().TraceCircle(distance,angle)
    facing=(0,angle,0)

    entwof2 = __main__.CreateEntityNoSpawn(entityType, point, facing )
    try:
        entwof2.SetName(entityName)
        entwof2.SetRelationship("player D_LI 6")
        entwof2.pl_investigate=6
        entwof2.pl_criminal_flee=6
        entwof2.pl_criminal_attack=6
        entwof2.pl_supernatural_flee=6
        entwof2.pl_supernatural_attack=6
        entwof2.SetInvestigateMode(4)
        entwof2.SetInvestigateModeCombat(4)
        entwof2.physdamagescale=1
        entwof2.TweakParam("hearing 0.1")
        entwof2.TweakParam("vision 10")
        entwof2.AllowKickHintUse(1)
        entwof2.LookAtEntityEye("!player")
        entwof2.SetFollowerType("Default")
        entwof2.SetFollowerBoss("!player")
        entwof2.SetModel(model)
        entwof2.PlayDialogFile("disciplines/koldunism/MagmaSurge_activate.wav")
        entwof2.MakeInvincible(1)
    except:
        pass
    __main__.CallEntitySpawn(entwof2)
    #entwof2.SetScriptedDiscipline("mind_shield 2")
    return entwof2

################			
def SummonMagmaSurgeHelper():
    entityType="npc_VCamera"
    model="models/weapons/disciplines/animalism/null.mdl"
    offset = round(360)
    allykwf2 = SpawnMagmaSurgeAlly("MagmaSurge", (180 + (offset)),entityType,model,-1)
    __main__.ScheduleTask(0.05,"castkoldunism.SummonMagmaSurgeHelper1()")

def SummonMagmaSurgeHelper1():
    __main__.FindEntityByName("MagmaSurge").SpawnTempParticle("KoldunismMagmaSurge_particle")

def SummonMagmaSurgeHelper2():
    __main__.FindEntityByName("MagmaSurge").Kill()

################				
def SummonMagmaSurge():
    pc=__main__.FindPlayer()
    MagmaSurge = __main__.FindEntityByName("MagmaSurge")
    FindClass = __main__.FindEntitiesByClass
    __main__.G.MagmaSurgeCounter = __main__.G.MagmaSurgeCounter + 1

    if(__main__.G.MagmaSurgeCounter >= 10):
	MagmaSurge.PlayDialogFile("disciplines/koldunism/MagmaSurge_deactivate.wav")
	__main__.ScheduleTask(0.85,"castkoldunism.SummonMagmaSurgeHelper2()")
	__main__.G.MagmaSurgeCounter = 0
    else:
	__main__.ScheduleTask(1.0,"castkoldunism.SummonMagmaSurge()")
        damage = pc.base_manipulation*10+5*__main__.G.MagmaSurgeCounter
        p1 = MagmaSurge.GetCenter() 
        npcc = FindClass("npc_VHumanCombatant") + FindClass("npc_VHumanCombatPatrol") + FindClass("npc_VDialogPedestrian") + FindClass("npc_VTzimisceHeadClaw") + FindClass("npc_VTzimisceRunner") + FindClass("npc_VVampire") + FindClass("npc_VHuman") + FindClass("npc_VPedestrian") + FindClass("npc_VCop") + FindClass("npc_VSabbatGunman") +FindClass("npc_VAsianVampire") + FindClass("npc_VChangBrosBlade") + FindClass("npc_VChangBrosClaw") + FindClass("npc_VLasombra") + FindClass("npc_VSabbatLeader") + FindClass("npc_VSheriffMan") + FindClass("npc_VTzimisce") + FindClass("npc_VManBat") 
        npcs = FindClass("npc_VGhoulCroucher") + FindClass("npc_VHengeyokai") + FindClass("npc_VZombie")
        for npc in npcc:
            p2 = npc.GetCenter()
            dist = distanceSquared(p1, p2)
            if(dist <= 22500):
                npc.TakeDamage(damage)
                npc.ChangeSchedule('SCHED_TROIKA_ONFIRE')
                npc.SpawnTempParticle("KoldunismBodyFire_particle")
                npc.PlayDialogFile("environmental/fire/fire_hit.wav")
        for npc in npcs:
            p2 = npc.GetCenter()
            dist = distanceSquared(p1, p2)
            if(dist <= 22500):
                npc.ChangeSchedule('SCHED_TROIKA_ONFIRE')
                npc.SpawnTempParticle("KoldunismBodyFire_particle")
                npc.PlayDialogFile("environmental/fire/fire_hit.wav")

################			castkoldunism.CastMagmaSurge()
def CastMagmaSurge():
    MagmaSurge = __main__.FindEntityByName("MagmaSurge")
    #if(__main__.G.GatesOfMagmaCounter > 0):
    if(MagmaSurge):
       consoleutil.console("say Must wait to use that Discipline again")
       #return
    else:
       __main__.ScheduleTask(0.05,"castkoldunism.CastMagmaSurge1()")
					
def CastMagmaSurge1():
    __main__.FindPlayer().PlayHUDParticle("d-koldunic-wof-cast-hud-emitter")
    __main__.FindPlayer().SpawnTempParticle("KoldunismCast_particle")
    __main__.FindPlayer().SetSupernaturalLevel(2)
    __main__.ScheduleTask(0.0,"castkoldunism.KoldunicPlayerBloodloss(2)")
    pevents = __main__.FindEntitiesByClass("events_player")
    pevents[0].CreateControllerNPC()
    #__main__.ccmd.thirdperson="" 
    __main__.ScheduleTask(0.05,"castkoldunism.CastMagmaSurge2()")

def CastMagmaSurge2():
    playerclone =  __main__.FindEntityByName("!playercontroller")
    playerclone.SetGesture("holy_light_cast")
    __main__.ScheduleTask(1.15,"castkoldunism.CastMagmaSurge3()")
    __main__.ScheduleTask(0.95,"castkoldunism.SummonMagmaSurge()")
    __main__.ScheduleTask(0.5,"castkoldunism.SummonMagmaSurgeHelper()")

def CastMagmaSurge3():
    pevents = __main__.FindEntitiesByClass("events_player")
    pevents[0].RemoveControllerNPC()
    consoleutil.console("say Koldunic Sorcery: Magma Surge")
    __main__.FindEntityByName("MagmaSurge").PlayDialogFile("disciplines/koldunism/MagmaSurge_loop.wav")

#-----------------------------------------------Koldunism Level 3---------------------------
################				Gates Of Magma

def SpawnGatesOfMagmaAlly(entityName, angle, entityType, model, distance ):

    point = __main__.FindPlayer().TraceCircle(distance,angle)
    facing=(0,angle,0)

    entwof3 = __main__.CreateEntityNoSpawn(entityType, point, facing )
    try:
        entwof3.SetName(entityName)
        entwof3.SetRelationship("player D_LI 6")
        entwof3.pl_investigate=6
        entwof3.pl_criminal_flee=6
        entwof3.pl_criminal_attack=6
        entwof3.pl_supernatural_flee=6
        entwof3.pl_supernatural_attack=6
        entwof3.SetInvestigateMode(4)
        entwof3.SetInvestigateModeCombat(4)
        entwof3.physdamagescale=1
        entwof3.TweakParam("hearing 0.1")
        entwof3.TweakParam("vision 10")
        entwof3.AllowKickHintUse(1)
        entwof3.LookAtEntityEye("!player")
        entwof3.SetFollowerType("Default")
        entwof3.SetFollowerBoss("!player")
        entwof3.SetModel(model)
        entwof3.PlayDialogFile("disciplines/koldunism/GatesOfMagma_activate.wav")
        entwof3.MakeInvincible(1)
        entwof3.SpawnTempParticle("KoldunismHeatWave_particle")
    except:
        pass
    __main__.CallEntitySpawn(entwof3)
    #entwof3.SetScriptedDiscipline("mind_shield 3")
    return entwof3

################			
def SummonGatesOfMagmaHelper():
    entityType="npc_VCamera"
    model="models/weapons/disciplines/animalism/null.mdl"
    offset = round(360)
    allykwf3 = SpawnGatesOfMagmaAlly("GatesOfMagma", (180 + (offset)),entityType,model,-1)
    __main__.ScheduleTask(0.05,"castkoldunism.SummonGatesOfMagmaHelper1()")

def SummonGatesOfMagmaHelper1():
    __main__.FindEntityByName("GatesOfMagma").SetParent("!player")

def SummonGatesOfMagmaHelper2():
    __main__.FindEntityByName("GatesOfMagma").Kill()

################				
def SummonGatesOfMagma():
    pc=__main__.FindPlayer()
    FindClass = __main__.FindEntitiesByClass
    __main__.G.GatesOfMagmaCounter = __main__.G.GatesOfMagmaCounter + 1

    if(__main__.G.GatesOfMagmaCounter >= 15):
	__main__.FindEntityByName("GatesOfMagma").PlayDialogFile("disciplines/koldunism/GatesOfMagma_deactivate.wav")
	__main__.ScheduleTask(0.85,"castkoldunism.SummonGatesOfMagmaHelper2()")
	__main__.G.GatesOfMagmaCounter = 0
    else:
	__main__.ScheduleTask(1.0,"castkoldunism.SummonGatesOfMagma()")
        damage = pc.base_manipulation*10+10
        p1 = pc.GetCenter() 
        npcc = FindClass("npc_VHumanCombatant") + FindClass("npc_VHumanCombatPatrol") + FindClass("npc_VDialogPedestrian") + FindClass("npc_VTzimisceHeadClaw") + FindClass("npc_VTzimisceRunner") + FindClass("npc_VVampire") + FindClass("npc_VHuman") + FindClass("npc_VPedestrian") + FindClass("npc_VCop") + FindClass("npc_VSabbatGunman") +FindClass("npc_VAsianVampire") + FindClass("npc_VChangBrosBlade") + FindClass("npc_VChangBrosClaw") + FindClass("npc_VLasombra") + FindClass("npc_VSabbatLeader") + FindClass("npc_VSheriffMan") + FindClass("npc_VTzimisce") + FindClass("npc_VManBat") 
        npcs = FindClass("npc_VGhoulCroucher") + FindClass("npc_VHengeyokai") + FindClass("npc_VZombie")
        for npc in npcc:
            p2 = npc.GetCenter()
            dist = distanceSquared(p1, p2)
            if(dist <= 8100):
                npc.TakeDamage(damage)
                npc.ChangeSchedule('SCHED_TROIKA_ONFIRE')
                npc.SpawnTempParticle("KoldunismBodyFire_particle")
                npc.PlayDialogFile("environmental/fire/fire_hit.wav")
        for npc in npcs:
            p2 = npc.GetCenter()
            dist = distanceSquared(p1, p2)
            if(dist <= 8100):
                npc.ChangeSchedule('SCHED_TROIKA_ONFIRE')
                npc.SpawnTempParticle("KoldunismBodyFire_particle")
                npc.PlayDialogFile("environmental/fire/fire_hit.wav")

################			castkoldunism.CastGatesOfMagma()
def CastGatesOfMagma():
    GatesOfMagma = __main__.FindEntityByName("GatesOfMagma")
    #if(__main__.G.GatesOfMagmaCounter > 0):
    if(GatesOfMagma):
       consoleutil.console("say Must wait to use that Discipline again")
       #return
    else:
       __main__.ScheduleTask(0.05,"castkoldunism.CastGatesOfMagma1()")
					
def CastGatesOfMagma1():
    __main__.FindPlayer().PlayHUDParticle("d-koldunic-wof-cast-hud-emitter")
    __main__.FindPlayer().SpawnTempParticle("KoldunismCast_particle")
    __main__.FindPlayer().SetSupernaturalLevel(3)
    __main__.ScheduleTask(0.0,"castkoldunism.KoldunicPlayerBloodloss(3)")
    pevents = __main__.FindEntitiesByClass("events_player")
    pevents[0].CreateControllerNPC()
    #__main__.ccmd.thirdperson="" 
    __main__.ScheduleTask(0.05,"castkoldunism.CastGatesOfMagma2()")

def CastGatesOfMagma2():
    playerclone =  __main__.FindEntityByName("!playercontroller")
    playerclone.SetGesture("howl")
    __main__.ScheduleTask(1.85,"castkoldunism.CastGatesOfMagma3()")
    __main__.ScheduleTask(0.95,"castkoldunism.SummonGatesOfMagma()")
    __main__.ScheduleTask(0.5,"castkoldunism.SummonGatesOfMagmaHelper()")

def CastGatesOfMagma3():
    __main__.FindPlayer().PlayHUDParticle("d-koldunic-wof-cast-hud2-emitter")
    pevents = __main__.FindEntitiesByClass("events_player")
    pevents[0].RemoveControllerNPC()
    consoleutil.console("say Koldunic Sorcery: Gates of Magma")
    __main__.FindEntityByName("GatesOfMagma").PlayDialogFile("disciplines/koldunism/GatesOfMagma_loop.wav")

#-----------------------------------------------Koldunism Level 4---------------------------
################				Heat Wave 

def SpawnHeatWaveAlly(entityName, angle, entityType, model, distance ):

    point = __main__.FindPlayer().TraceCircle(distance,angle)
    facing=(0,angle,0)

    entwof4 = __main__.CreateEntityNoSpawn(entityType, point, facing )
    try:
        entwof4.SetName(entityName)
        entwof4.SetRelationship("player D_LI 6")
        entwof4.pl_investigate=6
        entwof4.pl_criminal_flee=6
        entwof4.pl_criminal_attack=6
        entwof4.pl_supernatural_flee=6
        entwof4.pl_supernatural_attack=6
        entwof4.SetInvestigateMode(4)
        entwof4.SetInvestigateModeCombat(4)
        entwof4.physdamagescale=1
        entwof4.TweakParam("hearing 1.0")
        entwof4.TweakParam("vision 1024")
        entwof4.AllowKickHintUse(1)
        entwof4.LookAtEntityEye("!player")
        entwof4.SetFollowerType("Default")
        entwof4.SetFollowerBoss("!player")
        entwof4.SetModel(model)
        #entwof4.PlayDialogFile("disciplines/koldunism/HeatWave_activate.wav")
        entwof4.MakeInvincible(1)
        entwof4.SpawnTempParticle("KoldunismHeatWave_particle")
    except:
        pass
    __main__.CallEntitySpawn(entwof4)
    #entwof4.SetScriptedDiscipline("mind_shield 3")
    entwof4.SetScriptedDiscipline("shield_of_faith 4")
    entwof4.SetScriptedDiscipline("celerity 5")
    return entwof4

################			
def SummonHeatWave():
    entityType="npc_VGargoyle"
    model="models/weapons/disciplines/animalism/null.mdl"
    offset = round(360)
    allykwf4 = SpawnHeatWaveAlly("HeatWave", (180 + (offset)),entityType,model,-61.5)
    __main__.ScheduleTask(0.25,"castkoldunism.SummonHeatWave1()")

################					castkoldunism.SummonHeatWave()
def SummonHeatWave1():
    pc=__main__.FindPlayer()
    HeatWave = __main__.FindEntityByName("HeatWave")
    FindClass = __main__.FindEntitiesByClass
    __main__.G.HeatWaveCounter = __main__.G.HeatWaveCounter + 1

    if(__main__.G.HeatWaveCounter >= 30):
	__main__.ScheduleTask(0.5,"castkoldunism.SummonHeatWave2()")
	HeatWave.PlayDialogFile("disciplines/koldunism/HeatWave_deactivate.wav")
	__main__.G.HeatWaveCounter = 0
    else:
	__main__.ScheduleTask(1.0,"castkoldunism.SummonHeatWave1()")
        damage = __main__.G.HeatWaveCounter*6/10 + 7
        p1 = HeatWave.GetCenter() 
        p3 = pc.GetCenter()
        dist1 = distanceSquared(p1, p3)
        npcc = FindClass("npc_VHumanCombatant") + FindClass("npc_VHumanCombatPatrol") + FindClass("npc_VDialogPedestrian") + FindClass("npc_VTzimisceHeadClaw") + FindClass("npc_VTzimisceRunner") + FindClass("npc_VVampire") + FindClass("npc_VHuman") + FindClass("npc_VPedestrian") + FindClass("npc_VCop") + FindClass("npc_VSabbatGunman") +FindClass("npc_VAsianVampire") + FindClass("npc_VChangBrosBlade") + FindClass("npc_VChangBrosClaw") + FindClass("npc_VLasombra") + FindClass("npc_VSabbatLeader") + FindClass("npc_VSheriffMan") + FindClass("npc_VTzimisce") + FindClass("npc_VManBat") 
        npcs = FindClass("npc_VGhoulCroucher") + FindClass("npc_VHengeyokai") + FindClass("npc_VZombie")
        for npc in npcc:
            p2 = npc.GetCenter()
            dist = distanceSquared(p1, p2)
            if(dist <= 3600):
                npc.TakeDamage(damage)
                npc.ChangeSchedule('SCHED_TROIKA_ONFIRE')
                npc.SpawnTempParticle("KoldunismBodyHeatWave_particle")
                npc.PlayDialogFile("environmental/fire/fire_hit.wav")
                #npc.SetScriptedDiscipline("mind_shield 3")
        for npc in npcs:
            p2 = npc.GetCenter()
            dist = distanceSquared(p1, p2)
            if(dist <= 3600):
                npc.ChangeSchedule('SCHED_TROIKA_ONFIRE')
        if(dist1 <= 3600):
            consoleutil.console("vdmg 1")
            __main__.ccmd.SoundFire=""

def SummonHeatWave2():
    __main__.FindEntityByName("HeatWave").Kill()

################			castkoldunism.CastHeatWave()
def CastHeatWave():
    HeatWave = __main__.FindEntityByName("HeatWave")
    if(HeatWave):
       consoleutil.console("say Must wait to use that Discipline again")
       #return
    else:
       __main__.ScheduleTask(0.05,"castkoldunism.CastHeatWave1()")
					
def CastHeatWave1():
    __main__.FindPlayer().PlayHUDParticle("d-koldunic-wof-cast-hud-emitter")
    __main__.FindPlayer().SpawnTempParticle("KoldunismCast_particle")
    __main__.FindPlayer().SetSupernaturalLevel(4)
    __main__.ScheduleTask(0.0,"castkoldunism.KoldunicPlayerBloodloss(4)")
    pevents = __main__.FindEntitiesByClass("events_player")
    pevents[0].CreateControllerNPC()
    __main__.ccmd.SoundKoldunic=""
    #__main__.ccmd.thirdperson="" 
    __main__.ScheduleTask(0.05,"castkoldunism.CastHeatWave2()")

def CastHeatWave2():
    playerclone =  __main__.FindEntityByName("!playercontroller")
    playerclone.SetGesture("land_hard")
    __main__.ScheduleTask(1.35,"castkoldunism.CastHeatWave3()")
    __main__.ScheduleTask(0.95,"castkoldunism.SummonHeatWave()")

def CastHeatWave3():
    pevents = __main__.FindEntitiesByClass("events_player")
    pevents[0].RemoveControllerNPC()
    consoleutil.console("say Koldunic Sorcery: Heat Wave")
    __main__.FindEntityByName("HeatWave").PlayDialogFile("disciplines/koldunism/VolcanicBlast_loop.wav")

#-----------------------------------------------Koldunism Level 5---------------------------
################				Volcanic Blast

def SpawnVolcanicBlastAlly(entityName, angle, entityType, model, distance ):

    point = __main__.FindPlayer().TraceCircle(distance,angle)
    facing=(0,angle,0)

    entwof5 = __main__.CreateEntityNoSpawn(entityType, point, facing )
    try:
        entwof5.SetName(entityName)
        entwof5.SetRelationship("player D_LI 6")
        entwof5.pl_investigate=6
        entwof5.pl_criminal_flee=6
        entwof5.pl_criminal_attack=6
        entwof5.pl_supernatural_flee=6
        entwof5.pl_supernatural_attack=6
        entwof5.SetInvestigateMode(4)
        entwof5.SetInvestigateModeCombat(4)
        entwof5.physdamagescale=1
        entwof5.TweakParam("hearing 1.0")
        entwof5.TweakParam("vision 1024")
        entwof5.AllowKickHintUse(1)
        entwof5.LookAtEntityEye("!player")
        entwof5.SetFollowerType("Default")
        entwof5.SetFollowerBoss("!player")
        entwof5.SetModel(model)
        entwof5.PlayDialogFile("disciplines/koldunism/VolcanicBlast_loop.wav")
        entwof5.MakeInvincible(1)
        entwof5.SpawnTempParticle("KoldunismBlast_particle")
    except:
        pass
    __main__.CallEntitySpawn(entwof5)
    #entwof5.SetScriptedDiscipline("mind_shield 2")
    entwof5.SetScriptedDiscipline("shield_of_faith 4")
    return entwof5

################			
def SummonVolcanicBlast():
    entityType="npc_VGargoyle"
    model="models/weapons/disciplines/koldunism/wof_helper.mdl"
    #VolcanicBlast="VolcanicBlast"
    offset = round(360)
    allykwf5 = SpawnVolcanicBlastAlly("VolcanicBlast", (180 + (offset)),entityType,model,-120)
    __main__.ScheduleTask(0.25,"castkoldunism.SummonVolcanicBlast1()")

################					castkoldunism.SummonVolcanicBlast()
def SummonVolcanicBlast1():
    pc=__main__.FindPlayer()
    VolcanicBlast = __main__.FindEntityByName("VolcanicBlast")
    FindClass = __main__.FindEntitiesByClass
    __main__.G.VolcanicBlastCounter = __main__.G.VolcanicBlastCounter + 1

    if(__main__.G.VolcanicBlastCounter >= 30):
	__main__.ScheduleTask(0.5,"castkoldunism.SummonVolcanicBlast2()")
	VolcanicBlast.PlayDialogFile("disciplines/koldunism/VolcanicBlast_end.wav")
	__main__.G.VolcanicBlastCounter = 0
    else:
	__main__.ScheduleTask(1.0,"castkoldunism.SummonVolcanicBlast1()")
        damage = pc.base_manipulation*10+25
        p1 = VolcanicBlast.GetCenter() 
        p3 = pc.GetCenter()
        dist1 = distanceSquared(p1, p3)
        npcc = FindClass("npc_VHumanCombatant") + FindClass("npc_VHumanCombatPatrol") + FindClass("npc_VDialogPedestrian") + FindClass("npc_VTzimisceHeadClaw") + FindClass("npc_VTzimisceRunner") + FindClass("npc_VVampire") + FindClass("npc_VHuman") + FindClass("npc_VPedestrian") + FindClass("npc_VCop") + FindClass("npc_VSabbatGunman") +FindClass("npc_VAsianVampire") + FindClass("npc_VChangBrosBlade") + FindClass("npc_VChangBrosClaw") + FindClass("npc_VLasombra") + FindClass("npc_VSabbatLeader") + FindClass("npc_VSheriffMan") + FindClass("npc_VTzimisce") + FindClass("npc_VManBat") 
        npcs = FindClass("npc_VGhoulCroucher") + FindClass("npc_VHengeyokai") + FindClass("npc_VZombie")
        for npc in npcc:
            p2 = npc.GetCenter()
            dist = distanceSquared(p1, p2)
            if(dist <= 22500):
                npc.TakeDamage(damage)
                npc.ChangeSchedule('SCHED_TROIKA_ONFIRE')
                npc.SpawnTempParticle("KoldunismBodyFire_particle")
                npc.PlayDialogFile("environmental/fire/fire_hit.wav")
        for npc in npcs:
            p2 = npc.GetCenter()
            dist = distanceSquared(p1, p2)
            if(dist <= 22500):
                npc.ChangeSchedule('SCHED_TROIKA_ONFIRE')
        if(dist1 <= 22500):
            consoleutil.console("vdmg 2")
            __main__.ccmd.SoundFire=""

def SummonVolcanicBlast2():
    __main__.FindEntityByName("VolcanicBlast").Kill()

################			castkoldunism.CastVolcanicBlast()
def CastVolcanicBlast():
    VolcanicBlast = __main__.FindEntityByName("VolcanicBlast")
    if(VolcanicBlast):
       consoleutil.console("say Must wait to use that Discipline again")
       #return
    else:
       __main__.ScheduleTask(0.05,"castkoldunism.CastVolcanicBlast1()")
					
def CastVolcanicBlast1():
    __main__.FindPlayer().PlayHUDParticle("d-koldunic-wof-cast-hud-emitter")
    __main__.FindPlayer().SpawnTempParticle("KoldunismCast_particle")
    __main__.FindPlayer().SetSupernaturalLevel(5)
    __main__.ScheduleTask(0.0,"castkoldunism.KoldunicPlayerBloodloss(5)")
    pevents = __main__.FindEntitiesByClass("events_player")
    pevents[0].CreateControllerNPC()
    __main__.ccmd.SoundKoldunic=""
    __main__.ccmd.thirdperson="" 
    __main__.ScheduleTask(0.05,"castkoldunism.CastVolcanicBlast2()")

def CastVolcanicBlast2():
    playerclone =  __main__.FindEntityByName("!playercontroller")
    playerclone.SetGesture("stake_target")
    __main__.ScheduleTask(1.35,"castkoldunism.CastVolcanicBlast3()")
    __main__.ScheduleTask(0.95,"castkoldunism.SummonVolcanicBlast()")

def CastVolcanicBlast3():
    pevents = __main__.FindEntitiesByClass("events_player")
    pevents[0].RemoveControllerNPC()
    consoleutil.console("say Koldunic Sorcery: Volcanic Blast")
################