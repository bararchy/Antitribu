############################
#FILENAME : castthanatosislvl3.py
############################
import __main__
from __main__ import Character

 
"""
Example of adding summon blood allies power

"""
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

#-------------------------------------------------------------------THANATOSIS level 3-----
#Spawn 'ash to ash'
def SpawnThanatosis(entityName, angle, entityType, model, distance ):

    point = __main__.FindPlayer().TraceCircle(distance,angle)
    facing=(0,angle,0)

    entt3 = __main__.CreateEntityNoSpawn(entityType, point, facing )
    try:
        entt3.SetName(entityName)
        entt3.SetModel(model)
    except:
        pass
    __main__.CallEntitySpawn(entt3)
    
    return entt3

def RemoveThanatosis(aname):
    allyt3 = __main__.FindEntityByName(aname)
    if allyt3:
        __main__.ScheduleTask(0.1,"__main__.FindEntityByName('%s').Kill()" % aname)

################
allyt3Index=1
def ActivatetThanatosis(level=1):
    global allyt3Index

    entityType="prop_dynamic"
    model="models/scenery/misc/skeleton/dead_skeleton_samedi.mdl"

    offset = round(360/level)
    while level > 0:
        aname = "_my_ally_t3_%d" % allyt3Index
        allyt3 = SpawnThanatosis(aname, __main__.FindPlayer().GetAngles()[1],entityType,model,1)
        __main__.ScheduleTask(12.0,"castthanatosislvl3.RemoveThanatosis('%s')" % aname)
        level=level-1
        allyt3Index=allyt3Index+1

#-------------------------------------------------------------Vicissitude level 5--------
#Spawn Szlachta
def SpawnSzlachta(entityName, angle, entityType, model, distance ):

    point = __main__.FindPlayer().TraceCircle(distance,angle)
    facing=(0,angle,0)

    szlachta = __main__.CreateEntityNoSpawn(entityType, point, facing )
    try:
        szlachta.SetName(entityName)
        szlachta.SetRelationship("player D_LI 5")
        szlachta.pl_investigate=6
        szlachta.pl_criminal_flee=6
        szlachta.pl_criminal_attack=6
        szlachta.pl_supernatural_flee=6
        szlachta.pl_supernatural_attack=6
        szlachta.SetInvestigateMode(5)
        szlachta.SetInvestigateModeCombat(5)
        szlachta.physdamagescale=1.0
        szlachta.TweakParam("hearing 1024")
        szlachta.TweakParam("vision 1024")
        szlachta.AllowKickHintUse(1)
        szlachta.LookAtEntityEye("!player")
        szlachta.SetFollowerType("Default")
        szlachta.SetFollowerBoss("!player")
        szlachta.SetModel(model)
        szlachta.PlayDialogFile("disciplines/Viscicitude/level3/Loop3.wav")
    except:
        pass
    __main__.CallEntitySpawn(szlachta)
    
    szlachta.SetScriptedDiscipline("celerity 5")
    szlachta.SetScriptedDiscipline("potence 1")
    #szlachta.SetScriptedDiscipline("mind_shield 4")
    szlachta.SetScriptedDiscipline("auspex 3")
    szlachta.SpawnTempParticle("SerpentisViperSpawn_particle")
    return szlachta

def RemoveSzlachta(aname):
    allySzl = __main__.FindEntityByName(aname)
    if allySzl:
        allySzl.SetScriptedDiscipline("obfuscate 4")
        __main__.ScheduleTask(3.0,"__main__.FindEntityByName('%s').Kill()" % aname)

################

allyV5Index=1
def ActivateSzlachtaSummon(level=1):
    global allyV5Index

    entityType="npc_VTzimisceRunner"
    #entityType="npc_VTzimisceHeadClaw"
    model="models/character/monster/tzimisce/creation3/tzim3.mdl"
    #model="models/weapons/disciplines/Viscicitude/szlachta.mdl"
    timeout=900

    offset = round(360/level)
    while level > 0:
        aname = "_my_ally_v5_%d" % allyV5Index
        allySzl = SpawnSzlachta(aname, (-180 + (offset * level)),entityType,model,-70)
        if -1 != timeout:
            __main__.ScheduleTask(timeout,"castthanatosislvl3.RemoveSzlachta('%s')" % aname)
        level=level-1
        allyV5Index=allyV5Index+1

#-------------------------------------------------------------Explosive bot for Yukie--------
def SpawnExpBot(entityName, angle, entityType, model, distance ):

    point = __main__.FindPlayer().TraceCircle(distance,angle)
    facing=(0,angle,0)

    Bot1 = __main__.CreateEntityNoSpawn(entityType, point, facing )
    try:
        Bot1.SetName(entityName)
        Bot1.SetRelationship("player D_LI 6")
        Bot1.pl_investigate=6
        Bot1.pl_criminal_flee=6
        Bot1.pl_criminal_attack=6
        Bot1.pl_supernatural_flee=6
        Bot1.pl_supernatural_attack=6
        Bot1.SetInvestigateMode(4)
        Bot1.SetInvestigateModeCombat(4)
        Bot1.physdamagescale=1.0
        Bot1.TweakParam("hearing 1024")
        Bot1.TweakParam("vision 1024")
        Bot1.AllowKickHintUse(1)
        #Bot1.LookAtEntityEye("!player")
        Bot1.SetFollowerType("Default")
        Bot1.SetFollowerBoss("!player")
        #Bot1.SetFollowerBoss("none")
        Bot1.SetModel(model)
        Bot1.MakeInvincible(1)
    except:
        pass
    __main__.CallEntitySpawn(Bot1)
    
    #Bot1.SetScriptedDiscipline("celerity 5")
    #Bot1.SetScriptedDiscipline("potence 5")
    return Bot1

################				castthanatosislvl3.SummonBotMain()
def SummonBotMain():
    Bot = __main__.FindEntityByName("Bot")
    BotShell = __main__.FindEntityByName("BotShell")
    if(BotShell):
       return
    else:
       #entityType="npc_VTzimisceRunner"
       entityType="npc_VRat"
       model="models/weapons/disciplines/animalism/null.mdl"
       Bot="Bot"
       offset = round(360)
       BotMain = SpawnExpBot(Bot, (180 + (offset)),entityType,model,-50)
       __main__.ScheduleTask(0.1,"castthanatosislvl3.UseBot()")

################
def UseBot():
    Bot = __main__.FindEntityByName("Bot")
    BotShell = __main__.FindEntityByName("BotShell")

    BotShell=__main__.CreateEntityNoSpawn("prop_dynamic_ornament",Bot.GetOrigin(),Bot.GetAngles())
    BotShell.SetName("BotShell")
    BotShell.SetModel("models/cinematic/visual_stuff/bot_explosive/bot_explosive.mdl")
    __main__.CallEntitySpawn(BotShell)
    BotShell = __main__.FindEntityByName("BotShell")
    if BotShell: 
       BotShell.SetAttached("Bot")
       __main__.ScheduleTask(6.0,"castthanatosislvl3.UseBot1()")

def UseBot1():
    Bot = __main__.FindEntityByName("Bot")
    Bot.SetModel("models/null.mdl")
    __main__.ScheduleTask(0.1,"castthanatosislvl3.UseBot2()")

def UseBot2():
    Bot = __main__.FindEntityByName("Bot")
    expl = __main__.FindEntityByName("yukie_point_explosion")
    o = Bot.GetOrigin()
    no= (o[0],o[1],o[2]+10)
    expl.SetOrigin(no)
    __main__.ScheduleTask(0.1,"castthanatosislvl3.UseBot3()")
    __main__.ScheduleTask(0.2,"castthanatosislvl3.RemoveBot()")

def UseBot3():
    expl = __main__.FindEntityByName("yukie_point_explosion")
    expl.Explode()

def RemoveBot():
    __main__.FindEntityByName("BotShell").Kill()
    __main__.FindEntityByName("Bot").Kill()


