import __main__
import idutil
import characterext
import consoleutil
import statutil
import configutil
#import vamputil
from logutil import log

############################
#  Possession Utilities 
#---------------------------
#
# 

"""


"""

# Relaoded each time game is started
g_options=configutil.Options("mods.cfg")

###################
#  ONE TIME OPS   #
###################

def initPossessUtil():
    log("possess util : init called")
    if not __main__.G.possessutilonce:
        __main__.G.possessutilonce=1
        log("possess util : Performing One Time ops",1)
        characterext.initCharacterExt()
        __main__.G._npcName=""
        __main__.G._statIndex=-1
        __main__.G._possessed=0

###################
#  Variables      #
###################
#
# Using the console is ok for console commands, but should be limited
# when it comes to python commands. I have found odd behavior, especially
# with parameters that may contain underscores. We minimize python
# data and eliminate parameters by saving off everything that is
# relavent in (module scope) global variables. Yes this is nasty, but
# it helps to keep the system stable and less buggy. 

g_model=""
g_pcOrigin=None
g_pcAngle=None
g_consolecommand=""
g_callback=""
g_experience=0
g_searchHint=""
g_faint=0
g_prev_weapon="item_w_unarmed"

###################
#  VCLAN BUG FIX  #
###################
#
# Needed to support possession
#
# When you change the users clan using vclan, it can crash the game if the
# clans default model isn't in precache. Luckily, 95% of all the clans use
# the same (invalid) model. We can avoid the crash by loading it ahead of
# time. 

def fixVClan():
    vclanfix = __main__.FindEntitiesByName("_vclanfix*")
    if not vclanfix:
      vclanfix1 = __main__.CreateEntityNoSpawn("npc_VVampire",__main__.FindPlayer().GetOrigin(),(0,0,0))
      vclanfix1.SetModel("/models/character/npc/unique/malkgirl/girl.mdl")
      vclanfix1.SetName("_vclanfix1")
      __main__.CallEntitySpawn(vclanfix1)
      vclanfix1.ScriptHide()
      vclanfix2 = __main__.CreateEntityNoSpawn("npc_VVampire",__main__.FindPlayer().GetOrigin(),(0,0,0))
      vclanfix2.SetModel("/models/character/npc/average_vampire_hunter/average_vampire_hunter.mdl")
      vclanfix2.SetName("_vclanfix2")
      __main__.CallEntitySpawn(vclanfix2)
      vclanfix2.ScriptHide()
      vclanfix3 = __main__.CreateEntityNoSpawn("npc_VVampire",__main__.FindPlayer().GetOrigin(),(0,0,0))
      vclanfix3.SetModel("models/character/npc/unique/malkgirl/girl.mdl")
      vclanfix3.SetName("_vclanfix3")
      __main__.CallEntitySpawn(vclanfix3)
      vclanfix3.ScriptHide()
      vclanfix4 = __main__.CreateEntityNoSpawn("npc_VVampire",__main__.FindPlayer().GetOrigin(),(0,0,0))
      vclanfix4.SetModel("models/character/npc/average_vampire_hunter/average_vampire_hunter.mdl")
      vclanfix4.SetName("_vclanfix4")
      __main__.CallEntitySpawn(vclanfix4)
      vclanfix4.ScriptHide()

##################
# DIALOG SUPPORT #
##################

def canPCStay():
    log("Searching for No PC STAY Beacons",4)
    beacons = __main__.FindEntitiesByName("no_pc_stay")
    if 0 != len(beacons):
        log("Beacons Found. Checking Distance",4)
        for node in beacons:
            angles = node.GetAngles()
            dist = round(angles[0] * angles[1]) 
            if __main__.FindPlayer().Near(node.GetOrigin(),dist):
                log("Near Beacon. PC MAY NOT BE TOLD TO STAY",4)
                return 0
        log("Not near any Beacons",4)
    else:
        log("No Beacons Found",4)
    return 1

##################
# HELPER METHODS #
##################

def FixXP(pc):
    log("FixXP called")

    if pc.IsPC():
        log("possessutil : FixXP - nothing to Fix")
        return ""
        
    npcIndex=statutil.GetIndex(pc.GetID())
    if -1 == npcIndex:
        if pc.IsHuman(): npcIndex=statutil.GENERICHUMAN
        else: npcIndex=statutil.GENERICVAMPIRE

    data = ""
    npc_attributes=statutil.GetAttributesByIndex(npcIndex)
    npc_abilities=statutil.GetAbilitiesByIndex(npcIndex)
    npc_disciplines=statutil.GetDisciplinesByIndex(npcIndex)

    i = 0
    while i < len(statutil.AttributeNames):
        diff = (getattr(pc,"base_" + statutil.AttributeNames[i]) - npc_attributes[i])
        if diff > 0: data += "vstats sell %s %d\n" % (statutil.AttributeNames[i], diff)
        i+=1
    i = 0
    l = len(statutil.AbilityNames) - 2
    while i < l:
        diff = (getattr(pc,"base_" + statutil.AbilityNames[i]) - npc_abilities[i])
        if diff > 0: data += "vstats sell %s %d\n" % (statutil.AbilityNames[i], diff)
        i+=1

    # Special Cases : intimidate, computers
    spc1 = (getattr(pc,"base_" + statutil.AbilityNames[l]) - npc_abilities[l])
    if spc1 > 0: data += "vstats sell intimidation %d\n" % spc1
    spc2 = (getattr(pc,"base_" + statutil.AbilityNames[l+1]) - npc_abilities[l+1])
    if spc2 > 0 : data += "vstats sell computer %d\n" % spc2

    # Cant use simple subtraction with disciplines since they may be negative. 
    if pc.IsEmbraced():
        i = 0
        while i < len(statutil.DisciplineNames):
            if not (__main__.G._pcinfo[statutil.DisciplineNames[i]] == -1):
                diff = (getattr(pc,"base_" + statutil.DisciplineNames[i]) - 1)
                if diff > 0: data += "vstats sell %s %d\n" % (statutil.DisciplineNames[i], diff)
            i+=1
    else:
        i = 0
        while i < len(statutil.DisciplineNames):
            if not (getattr(pc,"base_" + statutil.DisciplineNames[i]) == -1):
                diff = (getattr(pc,"base_" + statutil.DisciplineNames[i]) - npc_disciplines[i])
                if diff > 0: data += "vstats sell %s %d\n" % (statutil.DisciplineNames[i], diff)
            i+=1
    return data

def GetPCInfoLevel():
    total=0
    i = 0
    while i < len(statutil.AttributeNames):
        total+=__main__.G._pcinfo[statutil.AttributeNames[i]]
        i+=1
    i = 0
    while i < len(statutil.AbilityNames):
        total+=__main__.G._pcinfo[statutil.AbilityNames[i]]
        i+=1
    i = 0
    while i < len(statutil.DisciplineNames):
        v = __main__.G._pcinfo[statutil.DisciplineNames[i]]
        i+=1
        if v != -1:
            total+=v

    # 120 possible, Level = 1 to 20
    level = (total / 6)
    log("PCINFO Computed Level [%d]" % level,4)
    return level
    
def FindPCBody(searchHint=""):
    global g_searchhint

    if __main__.FindPlayer().IsPC():
        return __main__.FindPlayer()

    #search 1: searchHint optimization
    if len(searchHint) > 0:
        npcs = __main__.FindEntitiesByName(searchHint)
        if npcs:
            for old in npcs:
                if old.IsPC(): return old

    try:
        if len(g_searchhint) > 0:
            npcs = __main__.FindEntitiesByName(g_searchhint)
            if npcs:
                for old in npcs:
                    if old.IsPC(): return old
    except:
        log("g_searchhint undefined")
        
    #search 2: previous G.npcName value
    if len(__main__.G._npcName) > 0:
        npcs = __main__.FindEntitiesByName(__main__.G._npcName)
        if npcs:
            for old in npcs:
                if old.IsPC(): return old

    #search 3: all npcs on current map:
    npcs = __main__.FindEntitiesByClass("npc_V*")
    if npcs:
        for old in npcs:
            if old.IsPC(): return old
    return None

def DeleteAll(classname):
    ents=__main__.FindEntitiesByClass(classname)
    if ents:
        for ent in ents:
            ent.Kill()
    
def RemoveBasicInventory():
    log("remove Basic")
    DeleteAll("weapon_physcannon")
    # DeleteAll("item_g_keyring")
    DeleteAll("item_g_wallet")
    DeleteAll("item_w_unarmed")
    DeleteAll("item_w_fists")
    DeleteAll("item_a_lt_cloth")
    
def AddBasicInventory():
    pc=__main__.FindPlayer()
    clan = pc.clan
    if not pc.HasItem("item_g_lockpick")  : pc.GiveItem("item_g_lockpick")
    if not pc.HasItem("item_w_unarmed")   : pc.GiveItem("item_w_unarmed")
    if not pc.HasItem("item_g_wallet")    : pc.GiveItem("item_g_wallet")
    if not pc.HasItem("weapon_physcannon"): pc.GiveItem("weapon_physcannon")
    if not pc.HasItem("item_a_lt_cloth")  : pc.GiveItem("item_a_lt_cloth")
    if not pc.HasItem("item_w_fists")     : 
        if(clan == 13):
            pc.ClearActiveDisciplines()
        else:
            pc.GiveItem("item_w_fists")
    
################
# MAIN METHODS #
################

def GetPossessed():
    return __main__.G._possessed
    
def possessByName(name,searchHint=""):
    global g_searchhint

    log("possessByName called")
    g_searchhint=searchHint

    npc=__main__.FindEntitiesByName(name)[0]
    if not npc:
        log("possessutil : possess - Error. Unable to find npc [%s]" %  name,3)
        return

    possess(npc,searchHint)
    
def possess(npc,searchHint=""):
    global g_model
    global g_pcOrigin
    global g_pcAngle
    global g_consolecommand
    global g_searchhint
    global g_prev_weapon
    global g_options
    
    log("possess called v0.2")
    g_searchhint=searchHint

    if not npc:
        log("possessutil : possess - Error. None is invalid npc",3)
        return

    if npc.IsPC():
        unpossess(searchHint)
        return

    npcClan=17
    __main__.G._statIndex=statutil.GetIndex(npc.GetID())
    if -1 == __main__.G._statIndex:
        log("possessutil : possess - Companion ID not found in statutil lookup table. Using GENERIC values.",2)
        if npc.IsHuman(): __main__.G._statIndex=statutil.GENERICHUMAN
        else: __main__.G._statIndex=statutil.GENERICVAMPIRE
    npcClan=statutil.GetAllStatsByIndex(__main__.G._statIndex)[statutil.CLAN]
    if -1 == npcClan or npc.IsEmbraced():
        npcClan = __main__.G._pcinfo["clan"] + 16
        log("possessutil : possess : Target npc embraced. Using clan %d" % npcClan)

    pc=__main__.FindPlayer()

    fixXP = ""
    clanchange=""
    fixKeys=""

    if pc.IsPC():
        # __main__.G._hitstillunpossess = npc.GetData("hits")
        # __main__.G._maxhits = round(npc.GetData("health") * pc.GetLevel() / 200 )
        # if __main__.G._hitstillunpossess < 1:
        #    __main__.G._hitstillunpossess = __main__.G._maxhits

        # storePCInfo() defined in vamputil.py. Populates G._pcinfo array
        __main__.storePCInfo()
        __main__.G._possessed=1
    else:
        # HANDLE CHAINED POSSESSION
        
        # If we can't find PC Body, we fail.
        oldnpc=FindPCBody(searchHint)
        if not oldnpc:
            log("possessutil : possess - Unable to find pc body. Please return to map with PC. Aborting ",3)
            return

        pc.SetData("bloodpool",pc.base_bloodpool)

        # pc.SetData("hits",__main__.G._hitstillunpossess)
        # __main__.G._hitstillunpossess = npc.GetData("hits")
        # __main__.G._maxhits = round(npc.GetData("health") * GetPCInfoLevel() / 200 )
        # if __main__.G._hitstillunpossess < 1:
        #     __main__.G._hitstillunpossess = __main__.G._maxhits


        # Fix oldnpc model
        oldnpc.SetModel(pc.GetModelName())

        pcIndex=statutil.GetIndex(pc.GetID())
        pcClan=1
        if -1 == pcIndex:
            if pc.IsHuman(): pcIndex=statutil.GENERICHUMAN
            else: pcIndex=statutil.GENERICVAMPIRE
        pcClan=statutil.GetAllStatsByIndex(pcIndex)[statutil.CLAN]
        if -1 == pcClan or pc.IsEmbraced():
            pcClan = __main__.G._pcinfo["clan"] + 16
            log("possessutil : possess : PC possessing Embraced NPC. Using clan %d" % pcClan)

        # if npc's current clan is also the target clan, the attributes wont reset.
        # In this case, we have to throw in an extra clan change to ensure different
        # attributes

        if pcClan == npcClan: clanchange+="vclan 1\n"

        # Need to compare stats to original and "sell" extra stats back to
        # re-emburse XP points
        fixXP += FixXP(pc)


    # if showhits is always on, activate counter
    # if 2 == g_options.get("comp_showHits",1):
    #    counter=__main__.FindEntityByName("poss_hit_counter")
    #    if counter:
    #        counter.Show()
    #        counter.count_time=__main__.G._hitstillunpossess
    #        counter.ResetTimer()
    #        counter.PauseTimer()

    __main__.G._pcinfo["doorkeys"]=pc.GetKeys()
    log("possess() : keys = [%s]" % __main__.G._pcinfo["doorkeys"])
    clanchange+="vclan %d" % npcClan
    __main__.G._npcName=npc.GetName()
    g_model=npc.GetModelName()
    g_pcOrigin=pc.GetOrigin()
    g_pcAngle=(0,pc.GetAngles()[1],0)

    __main__.G._currentlevel=pc.GetLevel()

    # NOTE: SetModel() will not always work on pc if they are in firstperson (ex: when clan is 1)
    g_consolecommand = "teleport_player \"%s\"\n%s\nthirdperson\nvamplight_enabled 1\n" % (__main__.G._npcName, clanchange)
    if g_options.get("comp_keepWeapon",1):
        g_consolecommand += "use %s\n" % g_prev_weapon

    # armor
    armor=0
    try: 
        armor=__main__.G._pcinfo["armor"]
    except:
        __main__.G._pcinfo["armor"]=0
    
    if 0 != armor :    
        g_consolecommand += "use %s\n" % statutil.ArmorNames[armor]

    # g_consolecommand+= "vstats get armor_rating 5\nvstats get automatic_soak_successes 10\nvstats get max_health 800\n"
    # g_consolecommand+= "vstats get health 800\nvstats get generation 800\nvstats get soak_pool 50\npossessutil.possessHelper()"

    if pc.IsPC():
        g_consolecommand+= "buddha\n"

    g_consolecommand+= "possessutil.possessHelper()"

    npc.ScriptHide()
    if len(fixXP) > 0:
        log("Executing fixXP")
        fixXP+="possessutil.grabExperience()"
        consoleutil.console(fixXP)
    else:
        # fixVClan()
        # consoleutil.console(g_consolecommand)    
        grabExperience()

def grabExperience():
    global g_consolecommand
    global g_experience

    log("grabExperience called")
    g_experience=0
    g_experience=__main__.FindPlayer().base_experience
    fixVClan()
    consoleutil.console(g_consolecommand)    
    
def possessHelper():
    global g_model
    global g_pcOrigin
    global g_pcAngle
    global g_callback
    global g_experience

    log("possessionHelper called")

    pc=__main__.FindPlayer()
    npc=__main__.FindEntityByName(__main__.G._npcName)

    npc.SetOrigin(g_pcOrigin)
    npc.SetAngles(g_pcAngle)
    npc.SetModel(__main__.G._pcinfo["model"])
    npc.ScriptUnhide()
    pc.SetModel(g_model)
    allInfo=statutil.GetAllStatsByIndex(__main__.G._statIndex)
    __main__.G._statIndex=-1
    __main__.cvar.name=allInfo[statutil.NAME]

    __main__.ScheduleTask(0.15,"SetitesWeaknessHelper()")

    # computation from companion.py
    #
    # __main__.G._statIndex=statutil.GetIndex(pc.GetID())
    # if -1 == __main__.G._statIndex:
    #     if pc.IsHuman(): __main__.G._statIndex=statutil.GENERICHUMAN
    #     else: __main__.G._statIndex=statutil.GENERICVAMPIRE
    # allInfo=statutil.GetAllStatsByIndex(__main__.G._statIndex)

    data = ""

    # vclan reset all the attributes, so we must now do a compare and update. Roll through stat
    # arrays and fix attributes

    # While we COULD use Character.BumpStat() from the Helper, the problem is they cause feedback to
    # appear on the screen. By using the console vstats command we avoid lots of game feedback.

    npc_attributes=allInfo[statutil.ATTRIBUTES]
    npc_abilities=allInfo[statutil.ABILITIES]
    npc_disciplines=allInfo[statutil.DISCIPLINES]
    i = 0
    while i < len(statutil.AttributeNames):
        diff = (npc_attributes[i] - getattr(pc,"base_" + statutil.AttributeNames[i]))
        if diff > 0: data += "vstats get %s %d\n" % (statutil.AttributeNames[i], diff)
        i+=1
    i = 0
    l = len(statutil.AbilityNames) - 2
    while i < l:
        diff = (npc_abilities[i] - getattr(pc,"base_" + statutil.AbilityNames[i]))
        if diff > 0: data += "vstats get %s %d\n" % (statutil.AbilityNames[i], diff)
        i+=1

    # Special Cases : intimidate, computers
    spc1 = (npc_abilities[l] - getattr(pc,"base_" + statutil.AbilityNames[l]))
    if spc1 > 0: data += "vstats get intimidation %d\n" % spc1
    spc2 = (npc_abilities[l+1] - getattr(pc,"base_" + statutil.AbilityNames[l+1]))
    if spc2 > 0 : data += "vstats get computer %d\n" % spc2

    if pc.IsEmbraced():
        i = 0
        while i < len(statutil.DisciplineNames):
            if not (__main__.G._pcinfo[statutil.DisciplineNames[i]] == -1):
                data += "vstats get %s %d\n" % (statutil.DisciplineNames[i], (1 - getattr(pc,"base_" + statutil.DisciplineNames[i])))
            i+=1
    else:
        # Cant use simple subtraction with disciplines since they may be negative. 
        i = 0
        while i < len(statutil.DisciplineNames):
            if not (npc_disciplines[i] == -1):
                data += "vstats get %s %d\n" % (statutil.DisciplineNames[i], (npc_disciplines[i] - getattr(pc,"base_" + statutil.DisciplineNames[i])))
            i+=1

    # experience
    if g_experience > 0:
        data+="giftxp %d\n" % g_experience
        g_experience=0

    # bloodpool
    bp = pc.GetData("bloodpool")
    if bp and 0 != bp:
        spc3 = (bp - pc.base_bloodpool)
        if spc3 > 0 and spc3 < 16:
            log("adding [%d] points of blood" % spc3)
            pc.Bloodgain(spc3)
        elif not (spc3 == 0):
            log("setting blood [%d]" % bp)
            data+="blood %d\n" % bp
        
    RemoveBasicInventory()
    __main__.ScheduleTask(0.1,"possessutil.AddBasicInventory()")
        
    # items

    # give PC npc items
    if 0 != g_options.get("comp_copyInventory",0):
        items=npc.GetItems()
        for item in items:
            if not pc.HasItem(item):
                pc.GiveItem(item)
            if npc.AmmoCount(item) > 0:
                pc.GiveAmmo(item, npc.AmmoCount(item))

    # Restore Keys
    doorkeys=__main__.G._pcinfo["doorkeys"]
    log("possessHelper : Restoring keys [%s]" % doorkeys)
    for doorkey in doorkeys:
        if not pc.HasItem(doorkey):
            pc.GiveItem(doorkey)

    # Invincibility
    # eventplayers = __main__.FindEntitiesByClass("events_player")
    # if eventplayers:
    #    eventplayers[0].MakePlayerUnkillable()

    # We use a registration pattern. Calling module registers a callback
    # method with us before calling possess. We in turn call the callback when
    # we are finished. Flexible design allows different modules to do different
    # things with possessed NPC.

    if len(data) > 0:
        if len(g_callback) > 0:
            data += "\n%s" % g_callback
        consoleutil.console(data)
    else:
        __main__.ScheduleTask(0.0,g_callback)
    g_callback=""

def registerCallback(callback):
    global g_callback
    log("registerCallback called")
    g_callback = callback

# Called from vampire/dlg/companion/travel.dlg
def StoreWeap(pc):
    global g_prev_weapon
    g_prev_weapon = pc.GetWeapon()
    return 0

# Returns npc or None. NPC if unpossess worked and None if it didn't (likely
# because PC Body not found in local area). Important for PossessUtil PC took
# damage events. 

def unpossess(searchHint="",faint=0,teleport=2):
    __main__.G.SetitesWeakness = 0
    global g_consolecommand
    global g_searchhint
    global g_pcOrigin
    global g_pcAngle
    global g_model
    global g_faint
    global g_prev_weapon
    global g_options
    
    log("Unpossess called")
    g_faint=faint

    # Find the companion currently holding the PC model
    g_searchhint=searchHint
    npc=FindPCBody(searchHint)

    if not npc:
        log("possessutil : unpossess - Unable to find pc body. Please return to map with PC. Aborting ",3)
        return None

    # Deactivate disciplines
    npc.SetScriptedDiscipline("auspex 0")
    npc.SetScriptedDiscipline("celerity 0")
    npc.SetScriptedDiscipline("fortitude 0")
    npc.SetScriptedDiscipline("potence 0")
    npc.SetScriptedDiscipline("presence 0")
    npc.SetBloodShieldDiscipline(0)

    pc=__main__.FindPlayer()
    pc.ClearActiveDisciplines()

    # Deactivate the hit counter if active. 
    # if g_options.get("comp_showHits",1) != 0:
    #    counter=__main__.FindEntityByName("poss_hit_counter")
    #    if counter:
    #        log("Hiding Counter")
    #        counter.Hide()

    # Remember possessed pc's hits remaining
    # pc.SetData("hits",__main__.G._hitstillunpossess)
    
    # re-emburse XP points
    fixXP = FixXP(pc)

    __main__.G._npcName=npc.GetName()
    g_model=pc.GetModelName()

    # pc at this point is the companion. Save off their
    # blood level for later restoration.
    # TODO: may need to check for 1==pc.base_corpus_vampirus
    pc.SetData("bloodpool",pc.base_bloodpool)

    # TELEPORT == 1 = teleport away from current location to pc body
    # TELEPORT == 0 = teleport pc body to current location.  
    if 0 != teleport:
        #If pc is following, do not teleport away
        if npc.GetData("Follower"):
            teleport = 0
        elif 1 == teleport:
            teleport = 1
        else:
            # auto detect (look for boss fight beacon)
            teleport = 1

            # See if there is a no_death_teleport beacon nearby. For distance,
            # we multiple the first 2 angles together.

            log("Searching for No Teleport Beacons",4)
            beacons = __main__.FindEntitiesByName("no_death_teleport")
            if 0 != len(beacons):
                log("Beacons Found. Checking Distance",4)
                for node in beacons:
                    angles = node.GetAngles()
                    dist = round(angles[0] * angles[1]) 
                    if pc.Near(node.GetOrigin(),dist):
                        log("Near Beacon. Teleport Canceled",4)
                        teleport=0
                        break
            else:
                log("No Beacons Found",4)
                            
    if teleport:
        g_pcOrigin=pc.GetOrigin()
        g_pcAngle=(0,pc.GetAngles()[1],0)
    else:
        g_pcOrigin=npc.GetOrigin()
        g_pcAngle=(0,npc.GetAngles()[1],0)
    
    __main__.G._pcinfo["doorkeys"]=pc.GetKeys()
    
    log("unpossess() : keys = [%s]" % __main__.G._pcinfo["doorkeys"])
    
    RemoveBasicInventory()
    g_consolecommand=""
    if teleport:
        g_consolecommand="teleport_player \"%s\"\n" % __main__.G._npcName
    g_consolecommand+="vclan %d\nthirdperson\nvamplight_enabled 0\n" % __main__.G._pcinfo["clan"]
    if g_options.get("comp_keepWeapon",1):
        g_consolecommand += "use %s\n" % g_prev_weapon

    # We throw in a get health so that the PC's health bar wakes up. Without
    # it, the bar will not update until the pc takes a hit. 

    g_consolecommand += "buddha\nvstats get health 1\npossessutil.unpossessHelper()"
    npc.ScriptHide()
    if len(fixXP) > 0:
        log("Executing fixXP")
        fixXP+="possessutil.grabExperience()"
        consoleutil.console(fixXP)
    else:
        grabExperience()
    return npc

def unpossessHelper():
    global g_callback
    global g_experience
    global g_pcOrigin
    global g_pcAngle
    global g_model
    global g_faint
    
    log("UnpossessHelper called")

    __main__.ScheduleTask(0.15,"PcGearHelper()")

    pc=__main__.FindPlayer()
    npc=__main__.FindEntityByName(__main__.G._npcName)
    npc.SetOrigin(g_pcOrigin)
    npc.SetAngles(g_pcAngle)
    npc.SetModel(g_model)
    npc.ScriptUnhide()
    if g_faint: npc.Faint()
    g_faint=0
    pc.SetModel(__main__.G._pcinfo["model"])
    __main__.cvar.name=__main__.G._pcinfo["name"]
    
    # Abilities, Attributes and Disciplines
    data = ""
    i = 0
    while i < len(statutil.AttributeNames):
        diff = (__main__.G._pcinfo[statutil.AttributeNames[i]] - getattr(pc,"base_" + statutil.AttributeNames[i]))
        if diff > 0: data += "vstats get %s %d\n" % (statutil.AttributeNames[i], diff)
        i+=1
    i = 0
    l = len(statutil.AbilityNames) - 2
    while i < l:
        diff = (__main__.G._pcinfo[statutil.AbilityNames[i]] - getattr(pc,"base_" + statutil.AbilityNames[i]))
        if diff > 0: data += "vstats get %s %d\n" % (statutil.AbilityNames[i], diff)
        i+=1

    spc1 = (__main__.G._pcinfo[statutil.AbilityNames[l]] - getattr(pc,"base_" + statutil.AbilityNames[l]))
    if spc1 > 0: data += "vstats get intimidation %d\n" % spc1
    spc2 = (__main__.G._pcinfo[statutil.AbilityNames[l+1]] - getattr(pc,"base_" + statutil.AbilityNames[l+1]))
    if spc2 > 0 : data += "vstats get computer %d\n" % spc2

    i = 0
    while i < len(statutil.DisciplineNames):
        if not (__main__.G._pcinfo[statutil.DisciplineNames[i]] == -1):
            data += "vstats get %s %d\n" % (statutil.DisciplineNames[i], (__main__.G._pcinfo[statutil.DisciplineNames[i]] - getattr(pc,"base_" + statutil.DisciplineNames[i])))
        i+=1
    # experience
    # if __main__.G._pcinfo["experience"] > 0: g_experience+= __main__.G._pcinfo["experience"]
    if g_experience > 0:
        data+="giftxp %d\n" % g_experience
        g_experience=0
    
    # masquerade
    if not (0 == __main__.G._pcinfo["masquerade"]):
         # vclan will reset to 0.
         # increase using vstats and no feedback.
         data+="vstats get masquerade %d\n" % __main__.G._pcinfo["masquerade"]

    # humanity
    if not (7 == __main__.G._pcinfo["humanity"]):
        # vclan will reset to 7.
        # increase using vstats with no feedback.
        # decrease using HumanityAdd (negative value) with feedback.
        # humanity add works in multiple of 2 with Toreador
        if __main__.G._pcinfo["humanity"] > 7:
            data+="vstats get humanity %d\n" % __main__.G._pcinfo["humanity"]            
        elif __main__.IsClan(pc,"Toreador"):
            if 0 == __main__.G._pcinfo["humanity"] % 2:
                data+="vstats get humanity 1\n"            
                __main__.G._pcinfo["humanity"]-=1
            pc.HumanityAdd((7 - __main__.G._pcinfo["humanity"])/-2)
        else:
            pc.HumanityAdd(__main__.G._pcinfo["humanity"] - 7)

    # history
    vhist=-1
    try: 
        vhist=__main__.G._pcinfo["vhistory"]
    except:
        __main__.G._pcinfo["vhistory"]=-1
    
    if -1 != vhist : data += "vhistory %d\n" % vhist

    # armor (must follow history)
    armor=0
    try: 
        armor=__main__.G._pcinfo["armor"]
    except:
        __main__.G._pcinfo["armor"]=0
    
    if 0 != armor : 
        data += "use %s\n" % statutil.ArmorNames[armor]

    # bloodpool
    bp = __main__.G._pcinfo["bloodpool"]
    spc3 = (bp - getattr(pc,"base_bloodpool"))
    if spc3 > 0 and spc3 < 16:
        log("adding [%d] points of blood" % spc3)
        pc.Bloodgain(spc3)
    elif not (spc3 == 0):
        log("setting blood to [%d]" % bp)
        data+="blood %d\n" % bp

    # items
    __main__.G._possessed=0

    # Stop Invincibility:
    # eventplayers = __main__.FindEntitiesByClass("events_player")
    # if eventplayers:
    #    eventplayers[0].MakePlayerKillable()
    
    if len(data) > 0:
        if len(g_callback) > 0:
            data += "\n%s" % g_callback
        consoleutil.console(data)
    else:
        __main__.ScheduleTask(0.0,g_callback)
    g_callback=""

    #keys
    #
    # Patch 1.1 Fix. Keys must be updated last as a change
    # in vclan may cause the key ring to reset.
    __main__.ScheduleTask(2.5,"possessutil.updateKeys()")

def updateKeys():
    pc=__main__.FindPlayer()
    doorkeys=__main__.G._pcinfo["doorkeys"]
    log("possessHelper : Restoring keys [%s]" % doorkeys)
    for doorkey in doorkeys:
        if not pc.HasItem(doorkey):
            pc.GiveItem(doorkey)

    keyrings=__main__.FindEntitiesByClass("item_g_keyring")
    if len(keyrings) > 1: keyrings[1].Kill()
    

    
###########################################################################
# POSSESSION AND DIALOGS : The Following Tables maintain the info used to #
# control who you can and can not talk to while possessed.                #
###########################################################################

# DIALOG_LOOKUP : Each index in this table corresponds to a dialog index.
# (See docs\dialogreftable). If the value is zero, the dialog is unprotected
# and we return 0. If the value is 1, the dialog requires that the pc is not
# possessing anyone and we alwaysreturn 1
# If the value is > 1, it corresponds to an entry in the DENYALLOW_TABLE.

               # 0   1   2   3   4   5   6   7   8   9
DIALOG_LOOKUP =( 1  ,0  ,0  ,0  ,0  ,1  ,0  ,1  ,1  ,0  , \
                 0  ,0  ,0  ,1  ,1  ,0  ,1  ,1  ,0  ,2  , \
                 0  ,3  ,0  ,1  ,0  ,0  ,0  ,0  ,0  ,4  , \
                 0  ,1  ,0  ,0  ,5  ,0  ,0  ,1  ,0  ,0  , \
                 0  ,1  ,0  ,0  ,6  ,1  ,0  ,7  ,1  ,0  , \
                 0  ,0  ,0  ,0  ,0  ,0  ,0  ,8  ,0  ,0  , \
                 9  ,0  ,0  ,1  ,0  ,0  ,0  ,0  ,1  ,0  , \
                 0  ,0  ,10 ,0  ,0  ,0  ,0  ,0  ,0  ,0  , \
                 1  ,1  ,1  ,0  ,0  ,0  ,0  ,0  ,0  ,0  , \
                 0  ,0  ,0  ,0  ,1  ,1  ,1  ,11 ,0  ,0  , \
                 1  ,0  ,1  ,1  ,1  ,1  ,0  ,1  ,0  ,1  , \
                 1  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  , \
                 0  ,0  ,0)
                 
                  
# DENYALLOW_TABLE : Each row contains a list of IDs from the statutil
# IDLookup table. The meaning of the list is determined by the
# first entree. If the first entree is -1, the list represents a DENY LIST.
# We only require unpossess if the PC is possessing one of the people identified by
# the list. 
#
# If the first entree is -2, the list represents an ALLOW LIST.
# We require unpossess unless the PC is possessing one of the people identified by
# the list. 
#
# Index -> Notes
#  0 ->                      DENY  NO ONE
#  1 ->                      ALLOW NO ONE
#  2 -> Dialog = bertrum(19) ALLOW Therese, Tourette, Jeanette, Knox
#  3 -> Dialog = cal(21)     DENY  Therese, Tourette, Jeanette, Knox
#  4 -> Dialog= E(29)        ALLOW Lily
#  5 -> Dialog= knox(34)     ALLOW Bertrum (Deprecated)
#  6 -> Dialog= therese(44)  ALLOW Vandal
#  7 -> Dialog= vandal(47)   ALLOW Therese, Tourette, Jeanette
#  8 -> Dialog= ash (57)     DENY  VV
#  9 => Dialog= dhatter(60)  DENY  VV
# 10 -> Dialog= vv           ALLOW Therese, Tourette, Jeanette
# 11 -> Dialog= Skelter      ALLOW Damsel

DENYALLOW_TABLE =( (-1,),        \
                   (-2,),        \
                   (-2,2,3,4,5), \
                   (-1,2,3,4,5), \
                   (-2,7),       \
                   (-2,12),      \
                   (-2,9),       \
                   (-2,3,4,5),   \
                   (-1,6),       \
                   (-1,6),       \
                   (-2,3,4,5),   \
                   (-2,20))

# NOFIRST_TABLE : Some npcs have an opening dialog that fires a scene or
# something special that always happens when the first dialog ends. For
# example, when Jeanette walks away after talking to her in Asylum for the
# first time. If we unpossess (which restarts the dialog), we break things.
# This lookup table indicates if a dialog should NEVER unpossess for the first
# interaction, no matter what the settings. This overrides any other checks or
# settings. 
#
# Jennette = 31

               # 0   1   2   3   4   5   6   7   8   9
NO_FIRST_TABLE =( 0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  , \
                  0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  , \
                  0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  , \
                  0  ,1  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  , \
                  0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  , \
                  0  ,0  ,0  ,0  ,0  ,0  ,1  ,0  ,1  ,1  , \
                  0  ,0  ,0  ,0  ,0  ,0  ,1  ,0  ,0  ,0  , \
                  0  ,0  ,0  ,1  ,1  ,0  ,0  ,0  ,0  ,0  , \
                  0  ,0  ,0  ,0  ,0  ,0  ,1  ,0  ,1  ,0  , \
                  0  ,0  ,1  ,0  ,0  ,0  ,0  ,0  ,0  ,0  , \
                  0  ,1  ,1  ,1  ,0  ,0  ,1  ,0  ,1  ,1  , \
                  0  ,0  ,0  ,0  ,1  ,0  ,0  ,0  ,0  ,0  , \
                  0  ,0  ,0)

##################
# EVENT HANDLERS #
##################

def timer_OnTimer():
    CheckForUnpossess()

def CheckForUnpossess():
    if __main__.G._possessed:
        pc = __main__.FindPlayer()
        if 1 == pc.health:
            StoreWeap(pc)
            c1=__main__.FindEntityByName("companion1")
            if c1 and c1.IsPC():
                registerCallback("companion.OnUnPossessEnd('companion1')")
                unpossess('companion1',1,g_options.get("comp_combatTeleport",2))
            else:
                c2=__main__.FindEntityByName("companion2")
                if c2 and c2.IsPC():
                    registerCallback("companion.OnUnPossessEnd('companion2')")
                    unpossess('companion2',1,g_options.get("comp_combatTeleport",2))
                else:
                    log("possessutil.player_OnPlayerTookDamage(). Unable to find PC BODY! Aborting Unpossess!",3)

def auto_OnMapLoad(map=""):
    global g_options
    log("possessutil.auto_OnMapLoad('%s') called" % map)

    # verifyCounter = __main__.FindEntityByName("poss_hit_counter")
    # if not verifyCounter:
    #    counter=__main__.CreateEntityNoSpawn("hud_timer",(0,0,0),(0,0,0))
    #    counter.SetName("poss_hit_counter")
    #    __main__.CallEntitySpawn(counter)

    # if showhits is always on, activate counter
    # if GetPossessed() and 2 == g_options.get("comp_showHits",1):
    #    cntr=__main__.FindEntityByName("poss_hit_counter")
    #    if cntr:
    #        cntr.Show()
    #        cntr.count_time=__main__.G._hitstillunpossess
    #        cntr.ResetTimer()
    #        cntr.PauseTimer()

def OnCombatStart():
    global g_options
    log("possessutil : OnCombatStart")

    # if GetPossessed() and (g_options.get("comp_showHits",1) != 0):
    #    log("possessutil : showHits True. Showing counter")
    #    counter=__main__.FindEntityByName("poss_hit_counter")
    #    if counter:
    #        counter.Show()
    #        counter.count_time=__main__.G._hitstillunpossess
    #        counter.ResetTimer()
    #        counter.PauseTimer()

def OnCombatEnd():
    global g_options
    log("possessutil : OnCombatEnd")

    # if GetPossessed() and 1 == g_options.get("comp_showHits",1):
    #    counter=__main__.FindEntityByName("poss_hit_counter")
    #    if counter:
    #        counter.Hide()
    
def handleDialogIndex(pc,npc,dialogIndex):
    global g_options
    
    # When an npc dialog calls this function, it checks the player model
    # to see if it is the player. If not, it refers to the DIALOG_LOOKUP
    # and DENYALLOW_TABLE to figure out if we must force unpossess.

    if pc.IsPC():
        log("handleDialogIndex : pc is not possessing. Returning 0")
        return 0

    # NO_FIRST_LIST trumps all
    if npc.times_talked == 1:
        log("handleDialogIndex : npc.times_talked == 1")  
        if NO_FIRST_TABLE[dialogIndex]:
            log("handleDialogIndex : dialog Index Found in NO_FIRST_TABLE. Returning 0")
            return 0

    if 4 != pc.GetData("Type"):
        if 2 == g_options.get("comp_forceUnpossess",2):
            # Auto Mode:
            dl = DIALOG_LOOKUP[dialogIndex]
            log("handleDialogIndex : DIALOG_LOOKUP[%d] = %d" % (dialogIndex, dl))
            if dl > 1:
                pcIndex=statutil.GetIndex(pc.GetID())
                if -1 == pcIndex:
                    if pc.IsHuman():
                        pcIndex=statutil.GENERICHUMAN
                    else:
                        pcIndex=statutil.GENERICVAMPIRE

                log("handleDialogIndex : pcIndex = %d" % pcIndex)

                #if list[0] = -1, list find success return = (-1 + 2)
                #if list[0] = -2, list find success return = (-1 + 2)
                
                found = pcIndex in DENYALLOW_TABLE[dl]
                log("handleDialogIndex : pcIndex in DENYALLOW_TABLE[%d] = %d" % (dl,found))
        
                dl = (found == DENYALLOW_TABLE[dl][0]+2)
                log("handleDialogIndex : dl = %d" % dl)

            if 0 == dl:
                log("handleDialogIndex : dl is 0 (false). Returnin 0")
                return 0

        if 0 == g_options["comp_forceUnpossess"]:
            return 0

        # 1 == g_options["comp_forceUnpossess"] or auto said unpossess
    else:
        log("handleDialogIndex : pc is possessing willing companion.")
 
    log("Beginning Unpossess Process")

    # Unpossess    
    task="__main__.FindEntityByName('%s').StartPlayerDialog(0)" % npc.GetName()
    
    c1=__main__.FindEntityByName("companion1")
    if c1 and c1.IsPC():
        registerCallback("companion.OnUnPossessEnd('companion1')")
        unpossess('companion1',0,0)
    else:
        c2=__main__.FindEntityByName("companion2")
        if c2 and c2.IsPC():
            registerCallback("companion.OnUnPossessEnd('companion2')")
            unpossess('companion2',0,0)
        else:
            log("possessutil.handleGlobalDialog(). Unable to find PC BODY! G.Henchman array will be corrupt!",3)
            unpossess('',0,0)
    __main__.ScheduleTask(1.0,task)
    return 1


def player_OnPlayerTookDamage():
    # global g_prev_weapon
    # global g_options

    log("possessutil : player_OnPlayerTookDamage()")
    # OnPlayerTookDamage fires immediatly, reflects health AFTER
    # damage. Problem is, if health after damage is 1 or
    # less, event doesn't fire (when budda is active). So the
    # idea is check the hit BEFORE the final hit. To do this,
    # we introduce a delay that is long enough to allow 2
    # quick hits. This works pretty well in melee as most moves
    # are combos.
    #
    # As a final backup, OnTimer also checks health when possession is
    # active. So worst case is that you may have to wait as long as
    # 15 seconds to unpossess. 
    
    __main__.ScheduleTask(3.0,"possessutil.CheckForUnpossess()")

    # if GetPossessed():
    #    pc = __main__.FindPlayer()
    #    log("possessutil : possession Active. Health [%d]" % pc.health)
    #    if 1 == pc.health:
    #        g_prev_weapon = pc.GetWeapon()
    #        c1=__main__.FindEntityByName("companion1")
    #        if c1 and c1.IsPC():
    #            registerCallback("companion.OnUnPossessEnd('companion1')")
    #            unpossess('companion1',1,g_options.get("comp_combatTeleport",2))
    #        else:
    #            c2=__main__.FindEntityByName("companion2")
    #            if c2 and c2.IsPC():
    #                registerCallback("companion.OnUnPossessEnd('companion2')")
    #                unpossess('companion2',1,g_options.get("comp_combatTeleport",2))
    #            else:
    #                log("possessutil.player_OnPlayerTookDamage(). Unable to find PC BODY! G.Henchman array will be corrupt!",3)
    #                unpossess('',1,g_options.get("comp_combatTeleport",2))





    #     __main__.G._hitstillunpossess = __main__.G._hitstillunpossess - 1;
    #     log("Hits Left [%d]" % __main__.G._hitstillunpossess)
    #     counter=None
    #     if g_options.get("comp_showHits",1) != 0:
    #        counter=__main__.FindEntityByName("poss_hit_counter")
    #        if counter:
    #            counter.Show()
    #            counter.count_time=__main__.G._hitstillunpossess
    #            counter.ResetTimer()
    #            counter.PauseTimer()   
    #     if __main__.G._hitstillunpossess < 1:
    #        pc = __main__.FindPlayer()
    #        g_prev_weapon = pc.GetWeapon()
    #        c1=__main__.FindEntityByName("companion1")
    #        if c1 and c1.IsPC():
    #            registerCallback("companion.OnUnPossessEnd('companion1')")
    #            unpossess('companion1',1,g_options.get("comp_combatTeleport",2))
    #        else:
    #            c2=__main__.FindEntityByName("companion2")
    #            if c2 and c2.IsPC():
    #                registerCallback("companion.OnUnPossessEnd('companion2')")
    #                unpossess('companion2',1,g_options.get("comp_combatTeleport",2))
    #            else:
    #                log("possessutil.player_OnPlayerTookDamage(). Unable to find PC BODY! G.Henchman array will be corrupt!",3)
    #                unpossess('',1,g_options.get("comp_combatTeleport",2))

def player_OnPlayerKilled():
    consoleutil.console("vamplight_enabled 0")
