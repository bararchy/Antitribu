############################
#FILENAME : castpresence.py
############################
import __main__
from __main__ import Character

##################
def _TraceCircle(self, radius=50, angleOffset=0):
    """ Find a point around the pc based on radius distance and angle between -180 and 180 """

    from math import pi as _pi
    from math import cos as _cos, sin as _sin

    pos   = self.GetOrigin()
    angle = self.GetAngles()[1] + angleOffset

    # degToRad : r = d/(360/2pi)
    xoffset = radius * _cos((angle/(360/(2*_pi))))
    yoffset = radius * _sin((angle/(360/(2*_pi))))

    return (pos[0]+xoffset, pos[1]+yoffset, pos[2])

Character.TraceCircle=_TraceCircle
##################
#returns the distanceSquared between two 3D points
def distanceSquared(p1, p2):
    xDistance = (p1[0] - p2[0]) * (p1[0] - p2[0])
    yDistance = (p1[1] - p2[1]) * (p1[1] - p2[1])
    zDistance = (p1[2] - p2[2]) * (p1[2] - p2[2])
    return (xDistance + yDistance + zDistance)

################
#-----------------------------------------------level 1---------------------------
def ActivatePresenceOne():
    FindClass = __main__.FindEntitiesByClass
    pc=__main__.FindPlayer()
    __main__.G.PresenceCounter = __main__.G.PresenceCounter + 1

    if(__main__.G.PresenceCounter >= 15):
        npcc = FindClass("npc_V*")
        for npc in npcc:
            npc.SetScriptedDiscipline("presence 0")
	__main__.G.PresenceCounter = 0
	print "exit"
    else:
	__main__.ScheduleTask(1.0,"castpresence.ActivatePresenceOne()")
        p1 = pc.GetCenter()
        npcc = FindClass("npc_VHumanCombatant") + FindClass("npc_VHumanCombatPatrol") + FindClass("npc_VSabbatGunman") + FindClass("npc_VDialogPedestrian") + FindClass("npc_VTzimisceHeadClaw") + FindClass("npc_VTzimisceRunner") + FindClass("npc_VVampire") + FindClass("npc_VHuman") + FindClass("npc_VPedestrian") + FindClass("npc_VCop")
        for npc in npcc:
            p2 = npc.GetCenter()
            dist = distanceSquared(p1, p2)
            if(dist <= 40000):
                npc.SetScriptedDiscipline("presence 1")
                npc.ChangeSchedule('SCHED_TROIKA_D_DAZE')

#-----------------------------------------------level 2---------------------------
def ActivatePresenceTwo():
    FindClass = __main__.FindEntitiesByClass
    pc=__main__.FindPlayer()
    __main__.G.PresenceCounter = __main__.G.PresenceCounter + 1

    if(__main__.G.PresenceCounter >= 15):
        npcc = FindClass("npc_V*")
        for npc in npcc:
            npc.SetScriptedDiscipline("presence 0")
	__main__.G.PresenceCounter = 0
	print "exit"
    else:
	__main__.ScheduleTask(1.0,"castpresence.ActivatePresenceTwo()")
        p1 = pc.GetCenter()
        npcc = FindClass("npc_VHumanCombatant") + FindClass("npc_VHumanCombatPatrol") + FindClass("npc_VSabbatGunman") + FindClass("npc_VDialogPedestrian") + FindClass("npc_VTzimisceHeadClaw") + FindClass("npc_VTzimisceRunner") + FindClass("npc_VVampire") + FindClass("npc_VHuman") + FindClass("npc_VPedestrian") + FindClass("npc_VCop")
        for npc in npcc:
            p2 = npc.GetCenter()
            dist = distanceSquared(p1, p2)
            if(dist <= 90000):
                npc.SetScriptedDiscipline("presence 2")
                npc.ChangeSchedule('SCHED_TROIKA_D_DAZE')

#-----------------------------------------------level 3---------------------------
def ActivatePresenceThree():
    FindClass = __main__.FindEntitiesByClass
    pc=__main__.FindPlayer()
    __main__.G.PresenceCounter = __main__.G.PresenceCounter + 1

    if(__main__.G.PresenceCounter >= 15):
        npcc = FindClass("npc_V*")
        for npc in npcc:
            npc.SetScriptedDiscipline("presence 0")
	__main__.G.PresenceCounter = 0
	print "exit"
    else:
	__main__.ScheduleTask(1.0,"castpresence.ActivatePresenceThree()")
        p1 = pc.GetCenter()
        npcc = FindClass("npc_VHumanCombatant") + FindClass("npc_VHumanCombatPatrol") + FindClass("npc_VSabbatGunman") + FindClass("npc_VDialogPedestrian") + FindClass("npc_VTzimisceHeadClaw") + FindClass("npc_VTzimisceRunner") + FindClass("npc_VVampire") + FindClass("npc_VHuman") + FindClass("npc_VPedestrian") + FindClass("npc_VCop")
        for npc in npcc:
            p2 = npc.GetCenter()
            dist = distanceSquared(p1, p2)
            if(dist <= 160000):
                npc.SetScriptedDiscipline("presence 3")
                npc.ChangeSchedule('SCHED_TROIKA_D_DAZE')

#-----------------------------------------------level 4---------------------------
def ActivatePresenceFour():
    FindClass = __main__.FindEntitiesByClass
    pc=__main__.FindPlayer()
    __main__.G.PresenceCounter = __main__.G.PresenceCounter + 1

    if(__main__.G.PresenceCounter >= 15):
        npcc = FindClass("npc_V*")
        for npc in npcc:
            npc.SetScriptedDiscipline("presence 0")
	__main__.G.PresenceCounter = 0
	print "exit"
    else:
	__main__.ScheduleTask(1.0,"castpresence.ActivatePresenceFour()")
        p1 = pc.GetCenter()
        npcc = FindClass("npc_VHumanCombatant") + FindClass("npc_VHumanCombatPatrol") + FindClass("npc_VSabbatGunman") + FindClass("npc_VDialogPedestrian") + FindClass("npc_VTzimisceHeadClaw") + FindClass("npc_VTzimisceRunner") + FindClass("npc_VVampire") + FindClass("npc_VHuman") + FindClass("npc_VPedestrian") + FindClass("npc_VCop")
        npcc = FindClass("npc_V*")
        for npc in npcc:
            p2 = npc.GetCenter()
            dist = distanceSquared(p1, p2)
            if(dist <= 250000):
                npc.SetScriptedDiscipline("presence 4")
                npc.ChangeSchedule('SCHED_TROIKA_D_DAZE')

#-----------------------------------------------level 5---------------------------
def ActivatePresenceFive():
    FindClass = __main__.FindEntitiesByClass
    pc=__main__.FindPlayer()
    __main__.G.PresenceCounter = __main__.G.PresenceCounter + 1

    if(__main__.G.PresenceCounter >= 15):
        npcc = FindClass("npc_V*")
        for npc in npcc:
            npc.SetScriptedDiscipline("presence 0")
	__main__.G.PresenceCounter = 0
	print "exit"
    else:
	__main__.ScheduleTask(1.0,"castpresence.ActivatePresenceFive()")
        p1 = pc.GetCenter()
        npcc = FindClass("npc_VHumanCombatant") + FindClass("npc_VHumanCombatPatrol") + FindClass("npc_VSabbatGunman") + FindClass("npc_VDialogPedestrian") + FindClass("npc_VTzimisceHeadClaw") + FindClass("npc_VTzimisceRunner") + FindClass("npc_VVampire") + FindClass("npc_VHuman") + FindClass("npc_VPedestrian") + FindClass("npc_VCop")
        npcc = FindClass("npc_V*")
        for npc in npcc:
            p2 = npc.GetCenter()
            dist = distanceSquared(p1, p2)
            if(dist <= 360000):
                npc.SetScriptedDiscipline("presence 5")
                npc.ChangeSchedule('SCHED_TROIKA_D_DAZE')

#-----------------------------------------------end---------------------------
def Castszlachta():
    pc = __main__.FindPlayer()
    viper = __main__.FindEntityByName("Serpentis_Viper")
    level = 1
    offset = round(360/level)
    #angle = (-180 + (offset * level)) 
    angle = (offset * level)   

    point = __main__.FindPlayer().TraceCircle(-50,(-180 + (offset * level)))
    facing=(0,angle,0)

    viper.SetAngles(facing)
    viper.SetOrigin(point)
    __main__.ScheduleTask(0.1,"castpresence.Castszlachta2()")

def Castszlachta2():
    viper = __main__.FindEntityByName("Serpentis_Viper")
    viper.PlayDialogFile("disciplines/serpentis/level2/viper_spawn.wav")
    viper.SetModel("models/weapons/disciplines/Viscicitude/szlachta.mdl")
    viper.SetScriptedDiscipline("auspex 5")
    viper.SetScriptedDiscipline("celerity 5")
    viper.SpawnTempParticle("SerpentisViperSpawn_particle")

#-----------------------------------------------Serpentis Spawn Viper ---------------------------
def CastViperSpawn():
    pc=__main__.FindPlayer()
    clan = pc.clan
    if(clan == 3):
	__main__.ScheduleTask(0.0,"castpresence.CastViperSpawn1()")
    elif(clan == 6):
	__main__.ScheduleTask(0.0,"castpresence.Castszlachta()")

def CastViperSpawn1():
    pc = __main__.FindPlayer()
    viper = __main__.FindEntityByName("Serpentis_Viper")
    level = 1
    offset = round(360/level)
    #angle = (-180 + (offset * level)) 
    angle = (offset * level)   

    point = __main__.FindPlayer().TraceCircle(-50,(-180 + (offset * level)))
    facing=(0,angle,0)

    viper.SetAngles(facing)
    viper.SetOrigin(point)
    __main__.ScheduleTask(0.1,"castpresence.CastViperSpawn2()")

def CastViperSpawn2():
    viper = __main__.FindEntityByName("Serpentis_Viper")
    viper.PlayDialogFile("disciplines/serpentis/level2/viper_spawn.wav")
    viper.SetModel("models/weapons/disciplines/serpentis/serpentis_viper.mdl")
    viper.SpawnTempParticle("SerpentisViperSpawn_particle")
    #viper.SetScriptedDiscipline("mind_shield 4")
    __main__.ScheduleTask(0.1,"castpresence.ViperAttack()")

################
def ViperAttack():
    pc=__main__.FindPlayer()
    viper = __main__.FindEntityByName("Serpentis_Viper")
    FindClass = __main__.FindEntitiesByClass
    __main__.G.ViperCounter = __main__.G.ViperCounter + 1

    if(__main__.G.ViperCounter >= 20):
	#viper.Kill()
	viper.ChangeSchedule('SCHED_TROIKA_D_SUICIDE')
	viper.PlayDialogFile("disciplines/serpentis/level2/viper_death.wav")
	__main__.G.ViperCounter = 0
	print "viper die"
    else:
	__main__.ScheduleTask(1.5,"castpresence.ViperAttack()")
        p1 = viper.GetCenter()
        npcc = FindClass("npc_VHumanCombatant") + FindClass("npc_VHumanCombatPatrol") + FindClass("npc_VDialogPedestrian") + FindClass("npc_VTzimisceHeadClaw") + FindClass("npc_VTzimisceRunner") + FindClass("npc_VVampire") + FindClass("npc_VHuman") + FindClass("npc_VPedestrian") + FindClass("npc_VCop") + FindClass("npc_VSabbatGunman") +FindClass("npc_VAsianVampire") + FindClass("npc_VChangBrosBlade") + FindClass("npc_VChangBrosClaw") + FindClass("npc_VLasombra") + FindClass("npc_VSabbatLeader") + FindClass("npc_VSheriffMan") + FindClass("npc_VTzimisce") 
        npcs = FindClass("npc_VGhoulCroucher") + FindClass("npc_VHengeyokai") + FindClass("npc_VZombie") + FindClass("npc_VGargoyle")
        damage = pc.base_strength*6+30
        for npc in npcc:
            p2 = npc.GetCenter()
            dist = distanceSquared(p1, p2)
            if(dist <= 3025):
                viper.PlayDialogFile("disciplines/serpentis/level2/viper_attack.wav")
                viper.SetGesture("ACT_SMALL_FLINCH")
                viper.SpawnTempParticle("SerpentisCobraAltattack_particle")
                viper.ChangeSchedule('TAKE_COVER_FROM_ENEMY')
                npc.ChangeSchedule('SCHED_TROIKA_D_DAZE')
                npc.TakeDamage(damage)
                #print "viper bite npc"

        for npc in npcs:
            p2 = npc.GetCenter()
            dist = distanceSquared(p1, p2)
            if(dist <= 3025):
                viper.PlayDialogFile("disciplines/serpentis/level2/viper_attack.wav")
                viper.SetGesture("ACT_SMALL_FLINCH")
                viper.SpawnTempParticle("SerpentisCobraAltattack_particle")
                viper.ChangeSchedule('TAKE_COVER_FROM_ENEMY')
                npc.ChangeSchedule('SCHED_TROIKA_ONFIRE')
                #print "viper bite npc"
#---------
def ViperDie():
    pc=__main__.FindPlayer()
    clan = pc.clan
    if(clan == 3):
	__main__.FindEntityByName("Serpentis_Viper").ChangeSchedule('SCHED_TROIKA_D_SUICIDE')

#-----------------------------------------------Serpentis Cobra Attack ---------------------------
def SerpentisCobraAlt2Attack():
    __main__.G.SerCobAttackCounter = __main__.G.SerCobAttackCounter + 1

    if(__main__.G.SerCobAttackCounter >= 2):
	__main__.G.SerCobAttackCounter = 0
    else:
	__main__.ScheduleTask(1.0,"castpresence.SerpentisCobraAlt2Attack()")

#-----------------------------------------------Serpentis Cobra Alternative Attack ---------------------------
################
def SerpentisCobraAltAttack():
    FindClass = __main__.FindEntitiesByClass
    pc=__main__.FindPlayer()
    __main__.G.SerCobAltAttackCounter = __main__.G.SerCobAltAttackCounter + 1

    if(__main__.G.SerCobAltAttackCounter >= 3):
	__main__.G.SerCobAltAttackCounter = 0
        p1 = pc.GetCenter()
        npcc = FindClass("npc_VHumanCombatant") + FindClass("npc_VHumanCombatPatrol") + FindClass("npc_VDialogPedestrian") + FindClass("npc_VTzimisceHeadClaw") + FindClass("npc_VTzimisceRunner") + FindClass("npc_VVampire") + FindClass("npc_VHuman") + FindClass("npc_VPedestrian") + FindClass("npc_VCop") + FindClass("npc_VSabbatGunman") +FindClass("npc_VAsianVampire") + FindClass("npc_VChangBrosBlade") + FindClass("npc_VChangBrosClaw") + FindClass("npc_VLasombra") + FindClass("npc_VSabbatLeader") + FindClass("npc_VSheriffMan") + FindClass("npc_VTzimisce") 
        npcs = FindClass("npc_VGhoulCroucher") + FindClass("npc_VHengeyokai") + FindClass("npc_VZombie") + FindClass("npc_VGargoyle")
        for npc in npcc:
            p2 = npc.GetCenter()
            dist = distanceSquared(p1, p2)
            if(dist <= 4900):
                npc.TakeDamage(5)
                npc.ChangeSchedule('SCHED_TROIKA_D_HALLUCINATION')
        for npc in npcs:
            p2 = npc.GetCenter()
            dist = distanceSquared(p1, p2)
            if(dist <= 4900):
                npc.ChangeSchedule('SCHED_TROIKA_D_MESMERIZE')
    else:
	__main__.ScheduleTask(1.0,"castpresence.SerpentisCobraAltAttack()")
        p1 = pc.GetCenter()
        npcc = FindClass("npc_VHumanCombatant") + FindClass("npc_VHumanCombatPatrol") + FindClass("npc_VDialogPedestrian") + FindClass("npc_VTzimisceHeadClaw") + FindClass("npc_VTzimisceRunner") + FindClass("npc_VVampire") + FindClass("npc_VHuman") + FindClass("npc_VPedestrian") + FindClass("npc_VCop") + FindClass("npc_VSabbatGunman") +FindClass("npc_VAsianVampire") + FindClass("npc_VChangBrosBlade") + FindClass("npc_VChangBrosClaw") + FindClass("npc_VLasombra") + FindClass("npc_VSabbatLeader") + FindClass("npc_VSheriffMan") + FindClass("npc_VTzimisce") 
        npcs = FindClass("npc_VGhoulCroucher") + FindClass("npc_VHengeyokai") + FindClass("npc_VZombie") + FindClass("npc_VGargoyle")
        damage = pc.base_strength*6+30
        for npc in npcc:
            p2 = npc.GetCenter()
            dist = distanceSquared(p1, p2)
            if(dist <= 3600):
                npc.TakeDamage(damage)
                npc.ChangeSchedule('SCHED_TROIKA_D_BLOODSHOT_KNOCKBACK')
        for npc in npcs:
            p2 = npc.GetCenter()
            dist = distanceSquared(p1, p2)
            if(dist <= 3600):
                npc.ChangeSchedule('SCHED_TROIKA_D_DAZE')

#-----------------------------------------------Serpentis Level 5 breathe the sandstorm---------------------------

def SpawnSandStormAlly(entityName, angle, entityType, model, distance ):

    point = __main__.FindPlayer().TraceCircle(distance,angle)
    facing=(0,angle,0)

    ents4 = __main__.CreateEntityNoSpawn(entityType, point, facing )
    try:
        ents4.SetName(entityName)
        ents4.SetRelationship("player D_LI 6")
        ents4.pl_investigate=6
        ents4.pl_criminal_flee=6
        ents4.pl_criminal_attack=6
        ents4.pl_supernatural_flee=6
        ents4.pl_supernatural_attack=6
        ents4.SetInvestigateMode(4)
        ents4.SetInvestigateModeCombat(4)
        ents4.physdamagescale=1
        ents4.TweakParam("hearing 1.0")
        ents4.TweakParam("vision 1024")
        ents4.AllowKickHintUse(1)
        ents4.LookAtEntityEye("!player")
        ents4.SetFollowerType("Default")
        ents4.SetFollowerBoss("!player")
        ents4.SetModel(model)
        ents4.PlayDialogFile("disciplines/serpentis/level5/maintain.wav")
        ents4.MakeInvincible(1)
        ents4.SpawnTempParticle("SerpentisSandstorm_particle")
    except:
        pass
    __main__.CallEntitySpawn(ents4)
    #ents4.SetScriptedDiscipline("mind_shield 5")
    ents4.SetScriptedDiscipline("shield_of_faith 4")
    return ents4

################			
def SummonSandStorm():
    SandStorm = __main__.FindEntityByName("SandStorm")
    if(SandStorm):
       #consoleutil.console("say Must wait to use that Discipline again")
       return
    else:
       entityType="npc_VVampireBoss"
       model="models/weapons/disciplines/animalism/null.mdl"
       SandStorm="SandStorm"
       offset = round(360)
       ally = SpawnSandStormAlly(SandStorm, (180 + (offset)),entityType,model,-60)
       __main__.ScheduleTask(0.1,"castpresence.SummonSandStorm1()")

################					castpresence.SummonSandStorm()
def SummonSandStorm1():
    SandStorm = __main__.FindEntityByName("SandStorm")
    FindClass = __main__.FindEntitiesByClass
    __main__.G.SandStormCounter = __main__.G.SandStormCounter + 1

    if(__main__.G.SandStormCounter >= 30):
	__main__.ScheduleTask(0.5,"castpresence.SummonSandStorm2()")
	SandStorm.PlayDialogFile("disciplines/serpentis/level5/deactivate.wav")
	__main__.G.SandStormCounter = 0
    else:
	__main__.ScheduleTask(1.0,"castpresence.SummonSandStorm1()")
        p1 = SandStorm.GetCenter() 
        npcc = FindClass("npc_VHumanCombatant") + FindClass("npc_VHumanCombatPatrol") + FindClass("npc_VDialogPedestrian") + FindClass("npc_VTzimisceHeadClaw") + FindClass("npc_VTzimisceRunner") + FindClass("npc_VVampire") + FindClass("npc_VHuman") + FindClass("npc_VPedestrian") + FindClass("npc_VCop") + FindClass("npc_VSabbatGunman") +FindClass("npc_VAsianVampire") + FindClass("npc_VChangBrosBlade") + FindClass("npc_VChangBrosClaw") + FindClass("npc_VLasombra") + FindClass("npc_VSabbatLeader") + FindClass("npc_VSheriffMan") + FindClass("npc_VTzimisce") 
        npcs = FindClass("npc_VGhoulCroucher") + FindClass("npc_VHengeyokai") + FindClass("npc_VZombie") + FindClass("npc_VGargoyle")
        for npc in npcc:
            p2 = npc.GetCenter()
            dist = distanceSquared(p1, p2)
            if(dist <= 40000):
                npc.TakeDamage(25)
                npc.ChangeSchedule('SCHED_TROIKA_ONFIRE')
        for npc in npcs:
            p2 = npc.GetCenter()
            dist = distanceSquared(p1, p2)
            if(dist <= 40000):
                npc.ChangeSchedule('SCHED_TROIKA_ONFIRE')

def SummonSandStorm2():
    __main__.FindEntityByName("SandStorm").Kill()

################