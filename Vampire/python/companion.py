import __main__
import time
import idutil
import characterext
import consoleutil
import possessutil
import statutil
import havenutil
import vamputil
from logutil import log
from __main__ import Character

############################
#  Companion Support Scripts
#---------------------------
# see companion.txt for documentation and design notes
#
# This module is at max capacity. If you wish to add another method, you will
# have to condense an existing method or move it to another module.
"""


"""

###################
#  ONE TIME OPS   #
###################
# We can't access G until a map is loaded. While we want to
# import all new modules from vamputils.py to make them
# globally available, vamputils is loaded before any maps.
# Therefore, we must delay G initialization until a map is
# loaded. See vamputils.py to see where this is called. 
#
# G.companiononce : used to ensure 1 time ops only happen once (When player begins new game)
# G.complist      : list used to maintain names of companions I have asked to join the party.
# G.rcomplist     : list used to maintain names of companions I have asked to leave the party.
#                   Used by map loading function to search for "original" companions and unhide them.  
# G.henchmen      : list used to maintain names of TRAVELLING companions (henchmen).
# G.possessed     : Indicates if pc is currently possessing a travelling companion
#                   None means false, If it has a value, it contains the key of
#                   the companion

def initCompanion():
    log("companion : init called")
    if not __main__.G.companiononce:
        __main__.G.companiononce=1
        log("companion : Performing One Time ops",1)
        characterext.initCharacterExt()
        __main__.G.complist=[]
        __main__.G.henchmen=[]
        __main__.G.rcomplist=[]
        __main__.G._inventory=[]
        __main__.G._inventoryCount=[]
        __main__.G.possessed=0
        pc=__main__.FindPlayer()
        pc.SetData("OName",pc.GetName())
        pc.SetData("OModel",pc.GetModelName())
        pc.SetData("Model",pc.GetModelName())
        pc.SetData("Henchman",0)
        pc.SetData("InStealth",0)
        pc.SetData("InCombat",0)
        pc.SetData("InFakeDeath",0)
        pc.SetData("Follower",1)
        pc.SetData("CombatType","general")
        pc.SetData("NoFight",0)
        pc.SetData("RespawnTimer",0)
        pc.SetData("health",200)
        pc.SetData("hits",5)

###################
#  Variables      #
###################

# MAXHENCHMEN     : Maximum number of TRAVELLING COMPANIONS you can have.
# MAXCOMPANIONS   : Maximum total number of people you can have in your party. Includes all
#                   partymembers, both travelling and those at your haven.
#
# G.pcinfo        : hashmap of info regarding the pc. Used by the possession script to store
#                   and restore PC to original stats when possession ends. 
# G.inCombat      : Indicates if pc is currently in combat. Used by event handlers to enhance
#                   npc fighting AI.

MAXHENCHMEN=2
MAXCOMPANIONS=7
g_embraced=""

#########################
# DIALOG HELPER METHODS #
#########################
# There are potential issues when spawning or altering npcs
# while the dialog engine is running. So for a majority of
# dialog options, we have support methods that simply set a
# global flag and then we handle what was said in the
# OnDialogEnd handler. In a few "safe" cases, we handle the
# function immeditaly. 

# Test : Is it OK to present assimilation dialog to person were are talking to. 
def Test(pc,npc):
    return (pc.HasItem("item_p_occult_lockpicking") and not (npc.GetID() in __main__.G.complist))

# 3 outcomes:
#   -1 = COULD Feed, but timer is running
#    0 = Cant feed because incompatible (NPC is vampire or PC is human)
#    1 = Can feed
# 
def FeedTest(pc,npc):
    log("companion mod : FeedTest")
    if pc.IsHuman():
        log("PC is Human. FeedTest returning false")
        return 0
    if not npc.IsHuman():
        log("PC is Not Human. FeedTest returning false")
        return 0
    feedtimer = npc.GetData("FeedTimer")
    if not feedtimer:
        log("FeedTimer Inactive. Returning True")
        return 1        
    log("feedtimer [%d]" % feedtimer)
    currenttime = time.time()
    if (currenttime > feedtimer):
        log("FeedTimer Expired. Resetting and Returning True")
        npc.SetData("FeedTimer",0)
        return 1
    log("FeedTimer running. Returning -1")
    return -1

def Feed(npc):
    npc.SetData("FeedTimer",round(time.time()) + 600)
    __main__.FindPlayer().SeductiveFeed( npc )

def ShowFeedTimer(npc):
    timer = __main__.FindEntityByName("feed_timer")
    timer.Show()
    timer.count_time=(npc.GetData("FeedTimer") - time.time())
    timer.ResetTimer()
    timer.PauseTimer()
    task="__main__.FindEntityByName('feed_timer').Hide()"
    __main__.ScheduleTask(5.0,task)

    
#---------------------------------
# ResetCompanions()
#---------------------------------
# Called from dlg/companion/travel.dlg
#
#---------------------------------
d_resetCompanions=0
def ResetCompanions():
    global d_resetCompanions
    d_resetCompanions=1

#---------------------------------
# possessHenchman()
#---------------------------------
# Called from dlg/companion/travel.dlg
#
# Sets flag so that PC possesses henchman they are talking to when dialog ends. We know which 
# henchmen they are talking to because each henchman has their own specific OnDialogEnd event
#---------------------------------
d_possessHenchman=0
def possessHenchman():
    global d_possessHenchman
    vamputil.PcGearHelper()
    d_possessHenchman=1
    return 0

#---------------------------------
# unpossessHenchman()
#---------------------------------
# Called from dlg/companion/travel.dlg
#
# Sets flag so that PC unpossesses the henchman they are currently possessing when dialog ends.
# We know which henchmen they are talking to because each henchman has their own specific
# OnDialogEnd event
#---------------------------------
d_unpossessHenchman=0
def unpossessHenchman():
    global d_unpossessHenchman
    d_unpossessHenchman=1
    return 0

#---------------------------------
# makeHenchman()
#---------------------------------
# Called from dlg/companion/first.dlg
# Called from dlg/companion/haven.dlg
#
# Sets flag so that the companion the PC is talking to becomes a travelling companion when the
# conversation ends. 
#---------------------------------
d_makeHenchman=0
def makeHenchman():
    global d_makeHenchman
    d_makeHenchman=1

d_summonSpell=0
def castSummonSpell(safe=1):
    global d_summonSpell
    if 1 == safe:
        d_summonSpell=1
    else:
        d_summonSpell=2

#---------------------------------
# makeRanged(npc):
#---------------------------------
# Called from dlg/companion/travel.dlg
#
# Updates persistent attributes on npc indicating they should use a ranged combat style. This is
# enforced by the presence of weapons on the NPC instance. In order for the change to take effect,
# we also set a flag to re-spawn the npc when the dialog ends. 
#---------------------------------
def makeRanged(npc):
    global d_makeHenchman
    npc.SetData("CombatType","general")
    npc.SetData("NoFight",0)
    d_makeHenchman=1
    return 0

#---------------------------------
# makeMelee(npc):
#---------------------------------
# Called from dlg/companion/travel.dlg
#
# Updates persistent attributes on npc indicating they should fight hand to hand. This is enforced
# by removing all ranged weapons from the NPC. instance. In order for the change to take effect,
# we also set a flag to re-spawn the npc when the dialog ends.
#---------------------------------
def makeMelee(npc):
    global d_makeHenchman
    npc.SetData("CombatType","melee")    
    npc.SetData("NoFight",0)
    d_makeHenchman=1
    return 0

#---------------------------------
# removeFromParty():
#---------------------------------
# Called from dlg/companion/first.dlg
# Called from dlg/companion/travel.dlg
# Called from dlg/companion/haven.dlg
#
# Sets flag so that dialog companion is removed from the party when the dialog ends. Companion
# id is moved from G.complist to G.rcomplist. Auto map loaders scan the G.rcomplist every time
# you enter a map and look for the npc. If found, they are restored and their ID is removed from
# G.rcomplist
#---------------------------------
d_removeFromParty=0
def removeFromParty():
    global d_removeFromParty
    d_removeFromParty=1

#---------------------------------
# removeFromParty():
#---------------------------------
# Called from dlg/companion/first.dlg
# Called from dlg/companion/travel.dlg
#
# Sets flag so that henchman is removed from travelling companions when the dialog ends.
# Hecnhman id is removed from G.hecnhmen. 
#---------------------------------
d_removeHenchman=0
def removeHenchman():
    global d_removeHenchman
    d_removeHenchman=1

#---------------------------------
# makeFollowPC(npc):
#---------------------------------
# Generally not called directly from dialogs, this is a helper method which not only makes the
# npc follow the pc, but also updates a persistant attribute so if a game is reloaded, they 
# still follow you.
#---------------------------------
def makeFollowPC(npc):
    npc.SetData("Follower",1)
    npc.SetFollowerBoss("!player")

#---------------------------------
# stopFollowPC(npc):
#---------------------------------
def stopFollowPC(npc):
    npc.SetData("Follower",0)
    npc.SetFollowerBoss("")

    # If makehenchman fails, then NPCs will not immediatly rise after combat.
    # And when they do, they will return to the location of their maker factory
    # (if they can find a path to it)

    # I tried using anchoring to keep the npc from wondering, however npcs
    # often fall to the ground resulting in makers being positioned too
    # close to the ground. When an npc maker produces an npc that is not
    # 100% in map boundaries, the behavior is unpredictable. You may not be
    # able to talk to the NPC and/or the maker becomes unresponsive. So we
    # disabled anchoring to prevent the greater of 2 evils.
    #
    # makername1="general_%s_maker" % __main__.G.LDName
    # makername2="melee_%s_maker" % __main__.G.LDName
    # maker1=__main__.FindEntityByName(makername1)
    # maker2=__main__.FindEntityByName(makername2)
    #
    # if maker1 and maker2:
    #    print "Anchoring makers for npc [%s] at current location" % __main__.G.LDName
    #    maker1.SetOrigin(npc.GetOrigin())
    #    maker2.SetOrigin(npc.GetOrigin())
    #else:
    #    print "Unable to find makers for npc [%s]" % __main__.G.LDName

#---------------------------------
# hasMaxHenchmen():
#---------------------------------
# Called from dlg/companion/first.dlg
# Called from dlg/companion/haven.dlg
#
# Helper function that compares current number of henchman to the max number allowed. If
# you have reached the maximum, it returns true. Typically used by "follow me" dialog
# options to allow redirection to an area for henchman haven transfer if you already
# have 2 henchmen following you when you attempt to bring someone on board the team. 
#---------------------------------
def hasMaxHenchmen():
    global MAXHENCHMEN
    return (len(__main__.G.henchmen) == MAXHENCHMEN)

#---------------------------------
# hasMaxCompanions():
#---------------------------------
# Called from dlg/companion/first.dlg
#
# Helper function that compares current number of companions to the max number allowed. If
# you have exceeded the maximum, it returns true. First dialog will abort immediatly if
# it detects you have readched the maximum.
#---------------------------------
def hasMaxCompanions():
    global MAXCOMPANIONS
    return (len(__main__.G.complist) == (MAXCOMPANIONS+1))


#---------------------------------
# resetChoiceData():
#---------------------------------
# Called from dlg/companion/first.dlg
# Called from dlg/companion/haven.dlg
#
# Part of a 5 command set of Helper functions to support choice system for selecting
# a henchman to remove (send to haven) in order to make room for a new npc. Initializes
# arrays.  Must be called before isHenchman, isUnknownHenchman or getUnknownHenchman
#---------------------------------
d_henchmennames=[]
d_unknownHenchmen=[]
def resetChoiceData():
    global d_henchmennames
    global d_unknownHenchmen

    log("companion - resetChoiceData()")
    d_henchmennames=[]
    d_unknownHenchmen=[]

    ## Do we need to explicitly delete? (does re-assignment above create memory leak?)
    ##    hncpy=[]
    ##    for henchman in d_henchmennames:
    ##        hncpy.append(henchman)
    ##    for henchman in hncpy:
    ##        print "Removing stale entry [%s] from d_henchmennames" % henchman
    ##        del d_henchmennames[d_henchmennames.index(henchman)]
    ##    uhcpy=[]
    ##    for henchman in d_unknownHenchmen:
    ##        uhcpy.append(henchman)
    ##    for henchman in uhcpy:
    ##        print "Removing stale entry [%s] from d_unknownHenchmen" % henchman
    ##        del d_unknownHenchmen[d_unknownHenchmen.index(henchman)]

    for key in __main__.G.henchmen:
        name=None
        npcIndex = statutil.GetIndex(key)
        if -1 == npcIndex:
            cdata=None
            try:
                cdata = __main__.G.npcdata[key]
            except:
                log("companion mod : resetChoiceData - henchman key [%s] not found in npcdata" % key)
            if cdata: name=cdata["OName"]
        else:
            stats = statutil.GetAllStatsByIndex(npcIndex)
            name = stats[statutil.NAME]
            
        if name:
            log("companion mod : resetChoiceData - adding henchman [%s] to d_henchmennames" % name)
            d_henchmennames.append(name)

#---------------------------------
# isHenchman():
#---------------------------------
# Called from dlg/companion/first.dlg
# Called from dlg/companion/haven.dlg
#
# Part of a 5 command set of Helper functions to support choice system for selecting
# a henchman to remove (send to haven) in order to make room for a new npc. Checks
# d_henchmennames array and removes if name is found. Returns true if name is found
# and name is not the PC (possession complicates things).
#---------------------------------
def isHenchman(name):
    global d_henchmennames

    if name in d_henchmennames:

        log("companion mod : isHenchman - Found [%s] in Henchman names. Removing from d_henchmennames" % name)

        del d_henchmennames[d_henchmennames.index(name)]

        #If possessing someone, we need to do some extra stuff
        if not __main__.FindPlayer().IsPC():
            log("companion mod : isHenchman - Possession detected. Performing PC checks")

            henchkey=""
            #Reverse lookup name to key...
            for key in __main__.G.henchmen:
                npcIndex = statutil.GetIndex(key)
                if -1 == npcIndex:
                    cdata=None
                    try:
                        cdata = __main__.G.npcdata[key]
                    except:
                        log("companion mod : isHenchman - henchman key [%s] not found in npcdata" % key)

                    if cdata:
                        oname=None
                        oname=cdata["OName"]
                        if oname and oname == name:
                            henchkey=key
                            break
                else:
                    hname=None
                    stats = statutil.GetAllStatsByIndex(npcIndex)
                    hname = stats[statutil.NAME]
                    if hname and hname == name:
                        return 1

            if idutil.isKeyPCTest(henchkey):
                log("companion mod : isHenchman - key [%s] is PC. Ignoring (returning false)" % henchkey)
                return 0

        return 1

    log("companion mod : isHenchman - [%s] NOT FOUND in Henchman names. Returning False" % name)
    return 0
    
#---------------------------------
# isUnknownHenchman():
#---------------------------------
# Called from dlg/companion/first.dlg
# Called from dlg/companion/haven.dlg
#
# Part of a 5 command set of Helper functions to support choice system for selecting
# a henchman to remove (send to haven) in order to make room for a new npc. Pops 
# d_henchmennames array and places 1 item in the d_unknownHenchmen. If there is
# a name to pop, and the name is not the PC (possession complicates things), returns
# true. Otherwise returns false. 
#---------------------------------
def isUnknownHenchman():
    global d_henchmennames
    global d_unknownHenchmen

    l = len(d_henchmennames)
    if l < 1: return 0

    log("companion mod : isUnknownHenchman - Appending name [%s] to UnknownHenchman list" % d_henchmennames[l-1])

    d_unknownHenchmen.append(d_henchmennames[l-1])
    henchname=d_henchmennames[l-1]
    del d_henchmennames[l-1]

    henchkey=""

    #Reverse lookup name to key...
    for key in __main__.G.henchmen:
        npcIndex = statutil.GetIndex(key)
        if -1 == npcIndex:
            cdata=None
            try:
                cdata = __main__.G.npcdata[key]
            except:
                log("companion mod : isUnknownHenchman - henchman key [%s] not found in npcdata" % key)

            if cdata:
                oname=None
                oname=cdata["OName"]
                if oname and oname == henchname:
                    henchkey=key
                    break
        else:
            hname=None
            stats = statutil.GetAllStatsByIndex(npcIndex)
            hname = stats[statutil.NAME]
            if hname and hname == henchname:
                return 1

    if idutil.isKeyPCTest(henchkey):
        log("companion mod : isUnknownHenchman - key [%s] is PC. Returning False" % henchkey)
        return 0

    return 1

#---------------------------------
# getUnknownHenchman(number):
#---------------------------------
# Called from dlg/companion/first.dlg
# Called from dlg/companion/haven.dlg
#
# Part of a 5 command set of Helper functions to support choice system for selecting
# a henchman to remove (send to haven) in order to make room for a new npc. Given an
# index (starting at value 1), returns name string of unknown henchman. Unknown henchmen
# are generally generic characters like prostitues or bums. 
#---------------------------------
def getUnknownHenchman(number):
    global d_unknownHenchmen
    return d_unknownHenchmen[(number-1)]

#---------------------------------
# replaceHenchman(name):
#---------------------------------
# Called from dlg/companion/first.dlg
# Called from dlg/companion/haven.dlg
#
# Part of a 5 command set of Helper functions to support choice system for selecting
# a henchman to remove (send to haven) in order to make room for a new npc. Similar
# to makeHenchman, however replaceHenchman first removes the henchman bearing the
# persistent attribute "OName" that matches the name parameter and then makes the
# npc the pc is talking to a new travel companion. 
#---------------------------------
d_replaceHenchman=0
d_replaceHenchmanName=""
def replaceHenchman(name):
    global d_replaceHenchman
    global d_replaceHenchmanName
    d_replaceHenchmanName=name
    d_replaceHenchman=1
    

#---------------------------------
# storeGlobals(npc):
#---------------------------------
# Called from many .dlg files. 
#
# G.LDName        : used by some Dialog files to mark the name of the last NPC the PC talked to.
#                   Needed for Scheduling tasks.
#
# When hooking the companion system up to an existing npc (eg: Knox), we dont have control
# over the npc's events. So therefore, we call store globals as the first executed line
# of the target NPC's dialog file. This is actually done towards the bottom of the file
# as the first (STARTING CONDITION). IT IS IMPORTANT THAT YOU RETURN 0
# (or the whole game will break)
#---------------------------------
def storeGlobals(npc):
    __main__.G.LDName=npc.GetName()
    return 0

#---------------------------------
# fakeDominate(npc,level):
#---------------------------------
#
# Supports stable Tremere dominate hack by simulating sound + special FX
# that normally accompany dominate. Specifically, supports the various
# situations where the fake dominate may be used in this game. 
def fakeDominate(npc,level):
    npc.PlayDialogFile("disciplines/dominate/dominate_mesmerize.wav")
    __main__.FindPlayer().Bloodloss(level)
    __main__.ScheduleTask(0.3,"companion.startDominate('%s')" % npc.GetName())
    __main__.ScheduleTask(0.3,"companion.startDominate('%s')" % __main__.G.LDName)
    __main__.ScheduleTask(0.3,"companion.startDominate('new_companion')")
    __main__.ScheduleTask(1.3,"companion.endDominate('%s')" % npc.GetName())
    __main__.ScheduleTask(1.3,"companion.endDominate('%s')" % __main__.G.LDName)
    __main__.ScheduleTask(1.3,"companion.endDominate('new_companion')")

def startDominate(npcName):
    npc = __main__.FindEntityByName(npcName)
    if npc:
        log("Starting Dominate Effect To %s" % npcName,4)
        npc.SetScriptedDiscipline('auspex 1')         

def endDominate(npcName):
    npc = __main__.FindEntityByName(npcName)
    if npc:
        log("Ending Dominate Effect on %s" % npcName,4)
        npc.SetScriptedDiscipline('auspex 0')         

#---------------------------------
# findServantOK(npc):
#---------------------------------
#
# Called from travel.dlg. Used to prevent bug where you could revive
# a fallen companion quickly by talking to the other companion and
# asking them to reset companions. "Bring the other servant here" was
# MEANT to allow you to retrieve a servant quickly who you had told to
# stand still.

def findServantOK():
    if not hasMaxHenchmen():
        return 0
    c1 = __main__.FindEntityByName("companion1")
    if c1 and c1.GetData("InFakeDeath"):
        return 0
    c2 = __main__.FindEntityByName("companion2")
    if c2 and c2.GetData("InFakeDeath"):
        return 0
    return 1

# Notes: You can not alter the contents of a container while it
#        is hidden. 
def openInventory():
    print "OPEN INVENTORY!"
    i=None
    npc=None
    try:
        i = __main__.FindEntityByName("global_inventory")
        npc = __main__.FindEntityByName(__main__.G.LDName)
    except:
        pass
    if i:
        if npc:
            print "Inventory Support objects Found"
            i.SetModel(npc.GetModelName())
            i.SetOrigin(npc.GetOrigin())
            i.SetAngles(npc.GetAngles())
            npc.ScriptHide()
            i.ScriptUnhide()
            index=0
            while index < len(__main__.G._inventory):
                item = __main__.G._inventory[index]
                count = __main__.G._inventoryCount[index]
                if count > 0:
                    while count > 0:
                        i.SpawnItemInContainer(item)
                        count=count-1
                else:
                    i.SpawnItemInContainer(item)
                index=index+1
            __main__.ScheduleTask(0.1,"consoleutil.console('+use')")
            __main__.ScheduleTask(0.2,"consoleutil.console('-use')")
            # Inventory close event picked up in events section.
        else:
            print "NPC not found for inventory model. Aborting"
    else:
        print "Inventory Container not found Aborting Inventory"


####################
# Helper Functions #
####################

def clearCompanions():
    
    comps = __main__.FindEntitiesByName("companion*")
    for comp in comps:
        comp.ScriptUnhide()
        comp.Kill()
    stale=__main__.FindEntitiesByName("new_companion")
    for comp in stale:
        removeHenchmanHelper(comp,1)
    stale=__main__.FindEntitiesByName("*_scrap")
    for comp in stale:
        comp.ScriptUnhide()
        comp.Kill()
    stale=__main__.FindEntitiesByName("scrap_*")
    for comp in stale:
        comp.ScriptUnhide()
        comp.Kill()

    rlistcpy=[]
    for rname in __main__.G.rcomplist:
        rlistcpy.append(rname)
    for rname in rlistcpy:
        log("companion : clearCompanions : searching for [%s]" % rname)        
        c = __main__.FindEntityByName(rname)
        if c:
            log("companion : clearCompanions : found [%s] Restoring..." % rname)
            slice = rname.rindex("_")
            c.SetName(rname[0:slice])
            del __main__.G.rcomplist[__main__.G.rcomplist.index(rname)]
            c.ScriptUnhide()
        else:
            log("companion : clearCompanions : [%s] Not found..." % rname)        

def populateCompanions():

    numHench = len(__main__.G.henchmen)
    if (not numHench == 0):
        pc=__main__.FindPlayer()
        offset = round(180 / (numHench+1))
        i=0
        __main__.G._spawnFailure=0

        # Buf fix Patch 1.2: PC changes maps during combat. OnBeginNormal Music
        # fires. InCombat state is still 1, so OnEndCombat also fires, respawning
        # any companions standing on the map that hadn't been cleaned up yet. This
        # in turn re-adds them to the G.henchmen array and causes a doopleganger to
        # appear when this method is finally invoked. I would reset InCombat to
        # 0 in OnEnterMap, however OnBeginNormalMusic actually fires first.
        #
        # So plan B: To prevent dooplegangers, we verify that the PC's current
        # id is not in G.henchmen. if found, we remove. It is a reactive instead
        # of a proactive fix, but it is better than nothing and may inadvertently
        # fix other bugs we haven't discovered.

        if (pc.GetID() in __main__.G.henchmen):
            log("Doopleganger Detected. Removing entry from henchmen",3)
            del __main__.G.henchmen[__main__.G.henchmen.index(pc.GetID())]
        
        for henchman in __main__.G.henchmen:
            log("Spawning Henchman [%s]" % henchman,4)
            c = spawnHenchman(henchman)
            if c:
                # Bug fix Patch 1.2: if nosferatu, they spawn in small
                # sewer tunnels more often, so we place the NPCs in a
                # location that wont knock them off map. 
                if 5 == __main__.G._pcinfo["clan"]:
                  i+=1
                  angle=90 + (i*offset)
                  c.SetOrigin(pc.TraceCircle(42,angle))
                c.ScriptUnhide()
                c.SetData("InFakeDeath",0)
                if pc.IsPC():
                    c.SetData("hits",round(c.GetData("health") * pc.GetLevel() / 120 ))
                else:
                    c.SetData("hits",round(c.GetData("health") * possessutil.GetPCInfoLevel() / 120 ))
            else:
                __main__.G._spawnFailure=1

def ResetCompanionHelper():
    clearCompanions()
    populateCompanions()

################
# MAIN METHODS #
################

def verifyCompanion(npc,type=0):
    """ Setup npc with initial companion module attributes if we have never seen them before """
    if not npc:
        log("companion mod : verifyCompanion - npc invalid. ")        
        return

    if npc.IsPC():
        return

    key = npc.GetID()
    if 0 != type: npc.SetData("Type",type)
    if not npc.IsCompanion(key):
        log("key [%s] not found in complist. Adding... " % key)        

        #Companion Perstistent Attributes

        npc.SetData("OName",npc.GetName())
        npc.SetData("OModel",npc.GetModelName())
        npc.SetData("Model",npc.GetModelName())
        npc.SetData("Henchman",0)
        npc.SetData("InStealth",0)
        npc.SetData("InCombat",0)
        npc.SetData("InFakeDeath",0)
        npc.SetData("Follower",0)
        npc.SetData("CombatType","general")
        npc.SetData("NoFight",0)

        # Haven persistent attributes
        npc.SetData("RespawnTimer",0)

        # Try to lookup stats in statutil.
        npcIndex = statutil.GetIndex(key)
        if -1 == npcIndex:
            if npc.IsHuman(): npcIndex=statutil.GENERICHUMAN
            else: npcIndex=statutil.GENERICVAMPIRE
        stats = statutil.GetAllStatsByIndex(npcIndex)
        health = stats[statutil.HEALTH]
                        
        # hits = health * PlayerLevel / 120
        # PlayerLevel is number of red dots / 3 (25 max possible)
        # Weak players have 60 HP
        # Powerfull players have 200 HP (essentially 2 hits per level)
        # Will likely update so that HP = BASE + 10*END + 5*DEX

        npc.SetData("health",health)

        # computation also used below and in possessutl.py
        pc = __main__.FindPlayer()
        if pc.IsPC():
            npc.SetData("hits",round(health * pc.GetLevel() / 120))
        else:
            npc.SetData("hits",round(health * possessutil.GetPCInfoLevel() / 120))            
        __main__.G.complist.append(key)


#---------------------------------
# addToParty(npc)
#---------------------------------
# General assumption is that addToParty is called from an NPCs dialog file which someone has altered:
#    ScheduleTask(0.2,'companion.addToParty(FindEntityByName("<some_name>"))')
# For generic npcs (such as prostitutes), you may have to store off the name in the starting conditions
# and then use the saved value:
#    ScheduleTask(0.2,'companion.addToParty(FindEntityByName("'+G.LDName+'"))')
#    ...
#    {9999}{(STARTING_CONDITION)}{(STARTING_CONDITION)}{}{companion.storeGlobals(npc)}{}{}{}{}{}{}{}{}
#---------------------------------

# type 0 : default (domination). Does not change if previously companion.
# type 1 : domination (change if previously something else)
# type 2 : dementation
# type 3 : presence
# type 4 : willing
# type 5 : embrace

def addToParty(npc, type=0):
    log("companion mod: addToParty")
    pc = __main__.FindPlayer()
    
    if not npc:
        log("companion mod: addToParty - Invalid npc variable.",2)        
        return

    # Embrace Support
    if 5 == type:
        log("companion mod: addToParty. Embrace Type detected")

        if not npc.IsHuman():
            log("You can not embrace this NPC. They are not human",2)
            return

        if not pc.IsPC():
            log("companion mod: addToParty - You can not embrace while possessing",2)        
            return

        key = npc.GetID()
        if 5 == __main__.G._pcinfo["clan"]:
            key_e = key + "_n_e"
        else:
            key_e = key + "_e"
            
        log("key [%s]" % key)
        log("key_e [%s]" % key_e)

        if npc.IsCompanion(key_e):
            log("companion mod: Can't complete embrace. An embraced version of this NPC already exists.")
            return
        
        if npc.IsCompanion(key):
            log("NPC is already a companion")
            #verify
            if npc.GetName().startswith("companion"):
                #They are already a henchmen. Set Type and Embrace and begin dialog.
                log("NPC is a henchment. Beginning Conversation")
                npc.SetData("Type",5)
                npc.SetData("Embraced",3)
                __main__.ScheduleTask(0.1, "__main__.FindEntityByName('%s').StartPlayerDialog(0)" % npc.GetName())
            elif npc.GetName().startswith("partymember"):
                #They are already a partymember. We must make them a henchmen to procede
                c2 = __main__.FindEntityByName("companion2")
                henchman = None
                origin = pc.TraceLine(42)
                if c2:
                    # Swap the two
                    origin = c2.GetOrigin()
                    removeHenchmanHelper(c2,1)
                    henchman = makeHenchmanHelper(npc)
                else:
                    # Make partymember a companion
                    henchman = makeHenchmanHelper(npc)
                if havenutil.isInHaven():
                    henchman.SetOrigin(origin)
                    havenutil.PopulateHaven()
                henchman.SetData("Type",5)
                henchman.SetData("Embraced",3)
                __main__.ScheduleTask(0.1, "__main__.FindEntityByName('%s').StartPlayerDialog(0)" % henchman.GetName())
            else:
                log("Error. NPC [%s] does not start with companion or partymember" % npc.GetName(),2)
            return
        else:
            log("addToParty: NPC is not yet a companion. Spawning new companion")

    log("companion mod: addToParty - Finding Maker") 
    maker = __main__.FindEntityByName("new_companion_maker")
    if not maker:
        log("companion mod: addToParty - Unable to find new_companion_maker (likely map not updated)",3)
        return
    log("companion mod: addToParty - Creating Character") 
    maker.Spawn()
    c=__main__.FindEntityByName("new_companion")
    if c:
        log("companion mod: addToParty - New Companion Created")
    else:
        log("companion mod: addToParty - new_companion_maker.Spawn() failed (likely func called from dialog)",3)
        return

    origin= npc.GetOrigin()

    # verifyCompanion adds them to G.complist[]
    verifyCompanion(npc,type)
    # Reset embrace state tracking variable if embracing
    if 5 == type: npc.SetData("Embraced",0)
    
    c.SetModel(npc.GetData("Model"))
    c.SetAngles(npc.GetAngles())
    
    if npc.GetName() == "new_companion":
        log("companion mod: addToParty - companion is named new_companion",3) 
        npc.Kill()
    else:
        log("companion mod: addToParty - Changing old name to _orig") 
        npc.SetName(npc.GetName() + "_orig")
        npc.ScriptHide()

    c.SetOrigin(origin)
    __main__.ScheduleTask(0.1, '__main__.FindEntityByName("new_companion").StartPlayerDialog(0)')

#---------------------------------
# removeFromPartyHelper(npc)
#---------------------------------

def removeFromPartyHelper(npc):
    """ Completly removes NPC from party. (Hopefully) restores original NPC (whereever you collected them).  """
    if not npc:
        log("companion mod : removeFromPartyHelper - npc invalid. ",3)        
        return
    key = npc.GetID()
    if not npc.IsCompanion(key):
        log("Companion Mod: removeFromPartyHelper - npc is not a companion",3)        
        return
    # Search the current area befor appending to list:
    rname=npc.GetData("OName") + "_orig"

    if havenutil.isInHaven():
        removeHenchmanHelper(npc,0,0)
    else:
        removeHenchmanHelper(npc)    
    del __main__.G.complist[__main__.G.complist.index(key)]
    c = __main__.FindEntityByName(rname)
    if c:
        slice = rname.rindex("_")
        c.SetName(rname[0:slice])
        npc.Kill()
        c.ScriptUnhide()
    else:
        __main__.G.rcomplist.append(rname)


#---------------------------------
# spawnHenchman(key)
#---------------------------------
# return new henchmen. Assumption is that key points to cateloged npc that
# is already marked as henchmen. returns None on error. Must call
# ScriptUnhide() on returned henchman
#
# G.npcdata defined in characterext.py
#---------------------------------

def spawnHenchman(key, follower=1):
    """ Spawns and returns Henchmen NPC. Must call ScriptUnhide() on returned npc """
    if not (key in __main__.G.henchmen):
        log("companion mod : spawnHenchman - Invalid key",2)        
        return None

    try:
      cdata = __main__.G.npcdata[key]
    except:
        log("companion mod : spawnHenchman - hecnhmen key not found in npcdata persistent data store.")        
        return None

    c=None
    c1=__main__.FindEntityByName("companion1")
    if not c1:
        makername="%s_companion1_maker" % cdata["CombatType"]
        log("maker name = [%s]" % makername)
        maker = __main__.FindEntityByName(makername)
        maker.Spawn()
        c = __main__.FindEntityByName("companion1")
    else:
        c2=__main__.FindEntityByName("companion2")
        if not c2:
            makername="%s_companion2_maker" % cdata["CombatType"]
            log("maker name = [%s]" % makername)
            maker = __main__.FindEntityByName(makername)
            maker.Spawn()
            c = __main__.FindEntityByName("companion2")
    if c:
        pc=__main__.FindPlayer()
        c.SetModel(cdata["Model"])
        a = pc.GetAngles()
        c.SetAngles((0,a[1],0))
        c.RestoreExpression(1)
        c.LookAtEntityEye("!player")

        if pc.IsStealth():
            c.SetScriptedDiscipline("obfuscate 4")
            c.SetData("InStealth",1)
        if follower: makeFollowPC(c)
        c.ScriptHide()
        c.SetOrigin(pc.GetOrigin())        
    else:
        log("companion mod : spawnHenchman - Error creating henchman. (possibly exceeded factory maximum?). Retry in 15 sec ",3)
    return c
    
#---------------------------------
# makeHenchman(npc, follower=1)
#---------------------------------    
# Note that makeHenchman could be called on just about anyone from anywhere.
# - dialogs, non-party npcs, party npcs, haven npcs, even existing henchmen.
#---------------------------------    

def makeHenchmanHelper(npc, follower=1):
    """ Makes the NPC a member of your travelling group """
    verifyCompanion(npc)

    npc.SetData("Henchman",1)
    key = npc.GetID()
    if not (key in __main__.G.henchmen): __main__.G.henchmen.append(key)

    # Renaming the companion is dangerous and presents race conditions, So we
    # Try to minimize the window:

    c=None
    maker1=None
    maker2=None
    if npc.GetData("CombatType") == "general":
        maker1=__main__.FindEntityByName("general_companion1_maker")
        maker2=__main__.FindEntityByName("general_companion2_maker")
    else:
        maker1=__main__.FindEntityByName("melee_companion1_maker")
        maker2=__main__.FindEntityByName("melee_companion2_maker")
    if npc.GetName().startswith("companion"):
        npc.SetName(npc.GetName() + "_scrap")
    if not __main__.FindEntityByName("companion1"):
        maker1.Spawn()
        c = __main__.FindEntityByName("companion1")
    else:
        maker2.Spawn()
        c = __main__.FindEntityByName("companion2")

    if c:
        pc=__main__.FindPlayer()
        nmodel = npc.GetData("Model")
        log("makeHenchmanHelper : key=[%s] model=[%s]" % (key,nmodel))
        c.SetModel(nmodel)
        c.SetAngles(pc.GetAngles())
        c.RestoreExpression(1)

        if pc.IsStealth():
            c.SetScriptedDiscipline("obfuscate 4")
            c.SetData("InStealth",1)
        if follower==2:
            if c.GetData("Follower"): makeFollowPC(c)
        if follower==1: makeFollowPC(c)
        c.ScriptHide()
        c.SetOrigin(npc.GetOrigin())
        c.SetAngles(npc.GetAngles())

        name=npc.GetName()
        if name == "new_companion" or name.startswith("companion") or name.startswith("partymember"):
            log("removing npc [%s]" % name)
            npc.SetName(name + "_scrap")
            npc.Kill()
        else:
            log("Marking Original NPC [%s]" % name)
            npc.SetName(npc.GetData("OName") + "_orig")
            npc.ScriptHide()
        c.ScriptUnhide()
        c.LookAtEntityEye("!player")

        # embrace support
        if 5 == c.GetData("Type"):
            if 2 == c.GetData("Embraced"):
                c.SetData("Embraced",3)
                __main__.ScheduleTask(0.1, "__main__.FindEntityByName('%s').StartPlayerDialog(0)" % c.GetName())
        return c
    else:        
        log("companion mod : makeHenchmanHelper - Error creating henchman. (possibly exceeded maximum?)",3)
        name=npc.GetName()
        if name.startswith("companion"):
            slice = name.rindex("_")
            npc.SetName(name[0:slice])
        return npc

#---------------------------------
# removeHenchmanHelper(npc, fast=0, repopulate=0)
#---------------------------------
# When fast is 1, removal is immediate with no fadeout.
# When repopulate is 1, removal is also immediate. If in haven,
#   we also call haevenutil.PopulateHaven() after removal. 
#---------------------------------

def removeHenchmanHelper(npc,fast=0,repopulate=0):
    """ removes NPC from your travelling group. """
    if not npc:
        log("Companion Mod: removeHenchmanHelper - npc is invalid ",3)
        return
    key = npc.GetID()
    if not npc.IsCompanion(key):
        log("Companion Mod: removeHenchmanHelper - npc is not a companion",2)
        return

    npc.SetData("Henchman",0)
    npc.WillTalk(0)

    # What about if we are at haven? Need special case where person walks or
    # teleports to assigned haven location. 

    stopFollowPC(npc)
    scrapname = npc.GetName() + "_scrap"
    npc.SetName(scrapname)
    if key in __main__.G.henchmen:
        log("Removing henchman from managed henchman [%s]" % key)
        del __main__.G.henchmen[__main__.G.henchmen.index(key)]

    if fast or repopulate:
        log("Killing NPC")
        npc.Kill()
    else:
        __main__.ccmd.fadeout=""
        __main__.ScheduleTask(2.0, '__main__.FindEntityByName("%s").Kill()' % scrapname)
        __main__.ScheduleTask(2.1, '__main__.ccmd.fadein=""')

    if havenutil.isInHaven() and repopulate:
        log("Calling PopulateHaven")
        havenutil.PopulateHaven()

def replaceHenchmanHelper(npc, currentHenchmanName):

    #Reverse lookup name to key...
    henchkey = ""
    for key in __main__.G.henchmen:
        npcIndex = statutil.GetIndex(key)
        if -1 == npcIndex:
            cdata=None
            try:
                cdata = __main__.G.npcdata[key]
            except:
                log("companion mod : isUnknownHenchman - henchman key [%s] not found in npcdata" % key)

            if cdata:
                oname=None
                oname=cdata["OName"]
                if oname and oname == currentHenchmanName:
                    henchkey=key
                    break
        else:
            hname=None
            stats = statutil.GetAllStatsByIndex(npcIndex)
            hname = stats[statutil.NAME]
            if hname and hname == currentHenchmanName:
                henchkey=key
                break
    
    # Find old Henchman
    oldHenchman=None
    c1=__main__.FindEntityByName("companion1")
    c2=__main__.FindEntityByName("companion2")
    if c1:
        if henchkey == c1.GetID(): oldHenchman = c1
    if c2:
        if henchkey == c2.GetID(): oldHenchman = c2
    if not oldHenchman:
        log("companion - replaceHenchmanHelper : Unable to find Henchman matching name [%s] with key [%s]" % (currentHenchmanName,henchkey))
        return
    
    # Remove old Henchman 
    # Important not to repopulate here because partymemeber hasn't
    # been added to henchman list yet.
    removeHenchmanHelper(oldHenchman,1)

    # Add npc as Henchman
    henchman = makeHenchmanHelper(npc)

    # Do some special stuff if we are embracing inside the haven
    if havenutil.isInHaven():
        if 5 == henchman.GetData("Type") and 3 == henchman.GetData("Embraced"):
            log("moving embrace candidate in front of PC")
            henchman.SetOrigin(__main__.FindPlayer().TraceLine(42))
        else:
            henchman.SetOrigin(__main__.FindPlayer().TraceLine(-50))
        havenutil.PopulateHaven()

def embrace(npc):
    if not npc:
        return
    pc=__main__.FindPlayer()
    if not pc.IsPC():
        return

    # Set type to embraced (This should already be the case)
    npc.SetData("Type",5)

    __main__.ScheduleTask(0.0,"__main__.FindPlayer().SeductiveFeed(__main__.FindEntityByName('%s'))" % npc.GetName())
    __main__.ScheduleTask(7.0,'consoleutil.console("+feed")')
    __main__.ScheduleTask(7.1,'consoleutil.console("-feed")')
    __main__.ScheduleTask(9.6,"companion.embraceHelper('%s','%s',1)" % (npc.GetName(),npc.GetID()))

def embraceHelper(npcName, npcID, thread=0):
    global g_embraced
    npc=__main__.FindEntityByName(npcName)
    if not npc:
        log("embraceHelper: npc [%s] not found" % npcName,3)
        return
    elif 1 == thread:
        npc.Faint()
        __main__.ScheduleTask(4.0,"companion.embraceHelper('%s','%s',2)" % (npcName, npcID))
    elif 2 == thread:
        npc.SetScriptedDiscipline("obfuscate 4")
        __main__.ScheduleTask(2.0,"companion.embraceHelper('%s','%s',3)" % (npcName, npcID))
    elif 3 == thread:
        embraceUpdate(npc, npcName, npcID)
        __main__.ScheduleTask(1.0,"companion.embraceHelper('%s','%s',4)" % (npcName, npcID))        
    elif 4 == thread:
        npc.SetScriptedDiscipline("obfuscate 0")
        __main__.ScheduleTask(5.0,"companion.embraceHelper('%s','%s',5)" % (npcName, npcID))        
    elif 5 == thread:
        npc.SetGesture("ACT_SLEEP_GETUP")
        __main__.ScheduleTask(1.5,"companion.embraceHelper('%s','%s',6)" % (npcName, npcID))        
    elif 6 == thread:
        npc.ChangeSchedule("")
        __main__.ScheduleTask(1.0,"companion.embraceHelper('%s','%s')" % (npcName, npcID))
    else:
        # Set embrace flag and begin conversation
        npc.SetData("Embraced",1)
        __main__.G.EmbracedCount=__main__.G.EmbracedCount+1
        if __main__.G.EmbracedCount > 1 and __main__.G.Story_State < 90:
            consoleutil.console('map sp_masquerade_1')
        else:
            if 1 == npc.GetData("Follower"):
                npc.SetFollowerBoss("!player")
            g_embraced=npc.GetName()
            log("Scheduling Dialog Task")
            __main__.ScheduleTask(0.1, '__main__.FindEntityByName("%s").StartPlayerDialog(0)' % g_embraced)

def embraceUpdate(npc, npcName, npcID):
    modelname=""
    key=""
    slice = npc.model.rindex("/")
    if slice > 0:
        key=npc.model[0:slice]
        modelname=npc.model[slice:-4]
    else:
        log("embraceUpdate: npc model invalid [%s]" % npc.model,2)
    slice = key.rindex("/")
    if slice > 0:
        id=key[slice:]
        if 5 == __main__.G._pcinfo["clan"]:
            id = id + "_n_e"
            modelname = modelname + "_n_e"
        else:
            id = id + "_e"
            modelname = modelname + "_e"
        model = key[0:slice] + id + modelname + ".mdl"
        omodel = key[0:slice] + id + id + ".mdl"
        log("embraceUpdate: model [%s] omodel [%s]" % (model,omodel))
        npc.SetModel(model)
        key = npc.GetID()

        log("embraceUpdate: npcName=[%s] npcID=[%s]" % (npcName,npcID))
        # if companion, clone old data, update henchmen and companion lists
        if npcID in __main__.G.complist:
            npc.CloneDataFromID(npcID)
            if npcID in __main__.G.henchmen:
                log("Updating henchman key [%s] -> [%s]" % (npcID,key))
                del __main__.G.henchmen[__main__.G.henchmen.index(npcID)]
                if not (key in __main__.G.henchmen):
                    __main__.G.henchmen.append(key)
            log("Updating Companion Key [%s] -> [%s]" % (npcID,key))
            del __main__.G.complist[__main__.G.complist.index(npcID)]
            if not (key in __main__.G.complist):
                __main__.G.complist.append(key)

            npc.SetData("Model",model)
            npc.SetData("OModel",omodel)

            # Fix health and hits
            # hits = health * PlayerLevel / 120

            npcIndex = statutil.GetIndex(key)
            if -1 == npcIndex: npcIndex=statutil.GENERICVAMPIRE
            stats = statutil.GetAllStatsByIndex(npcIndex)
            health = stats[statutil.HEALTH]

            npc.SetData("health",health)

            # computation also used above and in possessutl.py
            pc = __main__.FindPlayer()
            if pc.IsPC():
                  npc.SetData("hits",round(health * pc.GetLevel() / 120))
            else:
                npc.SetData("hits",round(health * possessutil.GetPCInfoLevel() / 120))

            # remove previous ID and info from save data
            try:
                if __main__.G.npcdata.has_key(npcID):
                    del __main__.G.npcdata[npcID]
            except:
                log("embraceUpdate: Unable to remove key from complist." % key,3)
        else:
            log("embraceUpdate: npcID [%s] not in complist" % npcName)
    else:
        log("embraceUpdate: npc key invalid [%s]" % key,2)

def IsPostEmbrace(npc):
    global g_embraced
    if 0 != len(g_embraced) and npc.GetName() == g_embraced:
        g_embraced=""
        return 1
    return 0


################################
# New_Companion Event Handlers #
################################
# npc_maker objects (which I) embeded onto every map are setup to call these event handlers

def new_companion_OnSpawnNPC():
    log("new_companion_OnSpawnNPC")

def new_companion_OnDialogBegin():
    log("new_companion_OnDialogBegin")

def new_companion_OnDialogEnd():
    log("new_companion_OnDialogEnd")
    global d_makeHenchman
    global d_removeHenchman    
    global d_removeFromParty
    global d_replaceHenchman
    global d_replaceHenchmanName
    global inEvent
    inEvent=1

    try:
        c = __main__.FindEntityByName("new_companion")
        if c:
            log("Found NPC")
            #Embrace Support
            if 5 == c.GetData("Type") and 0 == c.GetData("Embraced"):
                # Set Embraced State to 1 so that makeHenchman starts
                # the embace conversation with the PC after spawn
                c.SetData("Embraced",2)
            if d_removeHenchman:
                d_removeHenchman=0            
                if havenutil.isInHaven():
                    removeHenchmanHelper(c,1,1)
                else:
                    removeHenchmanHelper(c)
            elif d_makeHenchman:
                d_makeHenchman=0
                makeHenchmanHelper(c)
            elif d_removeFromParty:
                d_removeFromParty=0
                removeFromPartyHelper(c)
            elif d_replaceHenchman:
                d_replaceHenchman=0
                replaceHenchmanHelper(c,d_replaceHenchmanName)
                d_replaceHenchmanName=""
    finally:
        inEvent=0

##############################
# Companion 1 Event Handlers #
##############################
# npc_maker objects (which I) embeded onto every map are setup to call these event handlers
inEvent=0

def companion1_OnSpawnNPC():
    log("companion1_OnSpawnNPC")

def companion1_OnDialogBegin():
    """ Called from companion dialog files to support companion system"""
    log("companion1_OnDialogBegin")

    global inEvent
    inEvent=2

    c=__main__.FindEntityByName("companion1")
    if not c:
        c=__main__.FindEntityByName("companion_talking")
        
    c.SetScriptedDiscipline("obfuscate 0")
    c.SetData("InStealth",0)

def companion1_OnDialogEnd():
    """ Called from companion dialog files to support companion system"""
    log("companion1_OnDialogEnd")

    global inEvent
    global d_removeHenchman
    global d_removeFromParty
    global d_makeHenchman
    global d_possessHenchman
    global d_unpossessHenchman
    global d_resetCompanions
    global d_summonSpell
    
    try:
        c=__main__.FindEntityByName("companion_talking")
        if c:
            c.SetName("companion1")
            if 4 == c.GetData("Embraced") and 5 == c.GetData("Type"):
                # PC embraced
                embrace(c)
            elif 3 == c.GetData("Embraced") and 5 == c.GetData("Type"):
                # PC decided not to embrace
                c.SetData("Type",4)
                c.SetData("Embraced",0)
            elif d_removeHenchman:
                d_removeHenchman=0
                if havenutil.isInHaven():
                    removeHenchmanHelper(c,1,1)
                else:
                    removeHenchmanHelper(c)
            elif d_makeHenchman:
                d_makeHenchman=0
                makeHenchmanHelper(c)
            elif d_possessHenchman:
                d_possessHenchman=0
                possessutil.registerCallback("companion.OnPossessEnd('companion1')") 
                possessutil.possess(c,"companion*")
            elif d_unpossessHenchman:
                d_unpossessHenchman=0
                possessutil.registerCallback("companion.OnUnPossessEnd('companion1')") 
                possessutil.unpossess("companion*")
            elif d_removeFromParty:
                d_removeFromParty=0
                removeFromPartyHelper(c)
            elif d_resetCompanions:
                d_resetCompanions=0
                ResetCompanionHelper()
            elif 1 == d_summonSpell:
                d_summonSpell=0
                summonBoo(c)
            elif 2 == d_summonSpell:
                d_summonSpell=0
                summonBoo(c,0,0)
        else:
            log("companion1 not found after dialog. (Likely called remove henchman)")

    finally:
        inEvent=0

g_petCounter=0
def petBoo(boo, animation=0, start=1.0):
    global g_petCounter

    if not boo:
        log("petBooHelper() : Invalid npc")
        return

    if 0 == animation:
        animation = g_petCounter
        if 0 == animation:
            animation = 1
            g_petCounter = 1
        g_petCounter = g_petCounter + 1
            

    booClone=__main__.FindEntityByName("booClone")
    booAudio=__main__.FindEntityByName("booAudio")
    if not booClone: 
        booClone=__main__.CreateEntityNoSpawn("prop_dynamic",(0,0,0),(0,0,0))
        booClone.SetName("booClone")
        booClone.SetModel("models/null.mdl")
        __main__.CallEntitySpawn(booClone)
    if not booAudio: 
        booAudio=__main__.CreateEntityNoSpawn("npc_VHuman",(0,0,0),(0,0,0))
        booAudio.SetName("booAudio")
        booAudio.SetModel("models/null.mdl")
        __main__.CallEntitySpawn(booAudio)

    booClone.SetParent(boo.GetName())
    booAudio.SetParent(boo.GetName())
    booClone.SetOrigin(boo.GetOrigin())
    booAudio.SetOrigin(boo.GetOrigin())
    booClone.SetAngles(boo.GetAngles())
    booClone.SetModel("models/character/monster/boo/boo.mdl")
    booClone.SetAnimation("rat_idle")
    boo.ScriptHide()

    a = boo.GetAngles()
    if 1 == animation:
        # Animation 1 : Roll in Circle

        # roll over
        distance = 0.0
        angle = -90
        offset = 0
        __main__.ScheduleTask(start,"__main__.FindEntityByName('booClone').SetAngles((%d,%d,%d))" % (a[0],a[1]-offset,a[2]+offset))
        while distance != 5.0:
            start = start + 0.05
            offset = offset + 18
            o = boo.TraceCircle(distance,angle)
            o = (o[0],o[1],o[2]+2)
            __main__.ScheduleTask(start,"__main__.FindEntityByName('booClone').SetOrigin((%d,%d,%d))" % (o[0],o[1],o[2]))
            __main__.ScheduleTask(start,"__main__.FindEntityByName('booClone').SetAngles((%d,%d,%d))" % (a[0],a[1]-offset,a[2]+offset))
            distance = distance + 0.5
            angle = angle - 10

        # twitch
        __main__.ScheduleTask(start,"__main__.FindEntityByName('booAudio').PlayDialogFile('character/monster/boo/boo3.mp3')")
        __main__.ScheduleTask(start,"__main__.FindEntityByName('booClone').SetAnimation('rat_walk')")
        __main__.ScheduleTask(start + 0.3,"__main__.FindEntityByName('booClone').SetAnimation('rat_idle')")
        __main__.ScheduleTask(start + 0.8,"__main__.FindEntityByName('booClone').SetAnimation('rat_walk')")
        __main__.ScheduleTask(start + 1.3,"__main__.FindEntityByName('booClone').SetAnimation('rat_idle')")
        __main__.ScheduleTask(start + 1.8,"__main__.FindEntityByName('booClone').SetAnimation('rat_walk')")
        __main__.ScheduleTask(start + 2.5,"__main__.FindEntityByName('booClone').SetAnimation('rat_idle')")

        # finish roll
        start = start + 2.5
        distance = 4.5
        angle = 180
        offset = 180
        __main__.ScheduleTask(start,"__main__.FindEntityByName('booClone').SetAngles((%d,%d,%d))" % (a[0],a[1]+offset,a[2]-offset))
        while distance != -0.5:
            start = start + 0.05
            offset = offset - 18
            o = boo.TraceCircle(distance,angle)
            o = (o[0],o[1],o[2]+2)
            __main__.ScheduleTask(start,"__main__.FindEntityByName('booClone').SetOrigin((%d,%d,%d))" % (o[0],o[1],o[2]))
            __main__.ScheduleTask(start,"__main__.FindEntityByName('booClone').SetAngles((%d,%d,%d))" % (a[0],a[1]+offset,a[2]-offset))
            distance = distance - 0.5
            angle = angle - 10
    elif 2 == animation:
        # Animation 2 : Roll to left

        # roll over
        distance = 0
        offset = 0
        __main__.ScheduleTask(start,"__main__.FindEntityByName('booClone').SetAngles((%d,%d,%d))" % (a[0],a[1],a[2]+offset))
        while distance != 10.0:
            start = start + 0.05
            offset = offset + 36
            o = boo.TraceCircle(distance,-90)
            o = (o[0],o[1],o[2]+2)
            __main__.ScheduleTask(start,"__main__.FindEntityByName('booClone').SetOrigin((%d,%d,%d))" % (o[0],o[1],o[2]))
            __main__.ScheduleTask(start,"__main__.FindEntityByName('booClone').SetAngles((%d,%d,%d))" % (a[0],a[1],a[2]+offset))
            distance = distance + 1

        # sit up
        angle = 0
        while angle != 180.0:
            start = start + 0.1
            angle = angle + 30
            __main__.ScheduleTask(start,"__main__.FindEntityByName('booClone').SetAngles((%d,%d,%d))" % (a[0]-angle,a[1],a[2]+offset))


        # twitch
        __main__.ScheduleTask(start,"__main__.FindEntityByName('booAudio').PlayDialogFile('character/monster/boo/boo3.mp3')")
        __main__.ScheduleTask(start,"__main__.FindEntityByName('booClone').SetAnimation('rat_walk')")
        __main__.ScheduleTask(start + 0.3,"__main__.FindEntityByName('booClone').SetAnimation('rat_idle')")
        __main__.ScheduleTask(start + 0.8,"__main__.FindEntityByName('booClone').SetAnimation('rat_walk')")
        __main__.ScheduleTask(start + 1.3,"__main__.FindEntityByName('booClone').SetAnimation('rat_idle')")

        start = start + 1.3

        # sit down
        angle = 180.0
        while angle != 0.0:
            start = start + 0.1
            angle = angle - 30.0
            __main__.ScheduleTask(start,"__main__.FindEntityByName('booClone').SetAngles((%d,%d,%d))" % (a[0]-angle,a[1],a[2]+offset))

        # roll back
        distance = 9.0
        offset = 360
        __main__.ScheduleTask(start,"__main__.FindEntityByName('booClone').SetAngles((%d,%d,%d))" % (a[0],a[1],a[2]+offset))
        while distance != -1.0:
            start = start + 0.05
            offset = offset - 36
            o = boo.TraceCircle(distance,-90)
            o = (o[0],o[1],o[2]+2)
            __main__.ScheduleTask(start,"__main__.FindEntityByName('booClone').SetOrigin((%d,%d,%d))" % (o[0],o[1],o[2]))
            __main__.ScheduleTask(start,"__main__.FindEntityByName('booClone').SetAngles((%d,%d,%d))" % (a[0],a[1],a[2]+offset))
            distance = distance - 1.0

    elif 3 == animation:
        # Animation 2 : Roll to Right

        # roll right
        distance = 0
        offset = 0
        __main__.ScheduleTask(start,"__main__.FindEntityByName('booClone').SetAngles((%d,%d,%d))" % (a[0],a[1],a[2]-offset))
        while distance != 10.0:
            start = start + 0.05
            offset = offset + 36
            o = boo.TraceCircle(distance,90)
            o = (o[0],o[1],o[2]+2)
            __main__.ScheduleTask(start,"__main__.FindEntityByName('booClone').SetOrigin((%d,%d,%d))" % (o[0],o[1],o[2]))
            __main__.ScheduleTask(start,"__main__.FindEntityByName('booClone').SetAngles((%d,%d,%d))" % (a[0],a[1],a[2]-offset))
            distance = distance + 1

        # sit up
        angle = 0
        while angle != 180.0:
            start = start + 0.1
            angle = angle + 30
            __main__.ScheduleTask(start,"__main__.FindEntityByName('booClone').SetAngles((%d,%d,%d))" % (a[0]-angle,a[1],a[2]+offset))


        # twitch
        __main__.ScheduleTask(start,"__main__.FindEntityByName('booAudio').PlayDialogFile('character/monster/boo/boo3.mp3')")
        __main__.ScheduleTask(start,"__main__.FindEntityByName('booClone').SetAnimation('rat_walk')")
        __main__.ScheduleTask(start + 0.3,"__main__.FindEntityByName('booClone').SetAnimation('rat_idle')")
        __main__.ScheduleTask(start + 0.8,"__main__.FindEntityByName('booClone').SetAnimation('rat_walk')")
        __main__.ScheduleTask(start + 1.3,"__main__.FindEntityByName('booClone').SetAnimation('rat_idle')")

        start = start + 1.3

        # sit down
        angle = 180.0
        while angle != 0.0:
            start = start + 0.1
            angle = angle - 30.0
            __main__.ScheduleTask(start,"__main__.FindEntityByName('booClone').SetAngles((%d,%d,%d))" % (a[0]-angle,a[1],a[2]+offset))

        # roll back
        distance = 9.0
        offset = 360
        __main__.ScheduleTask(start,"__main__.FindEntityByName('booClone').SetAngles((%d,%d,%d))" % (a[0],a[1],a[2]-offset))
        while distance != -1.0:
            start = start + 0.05
            offset = offset - 36
            o = boo.TraceCircle(distance,90)
            o = (o[0],o[1],o[2]+2)
            __main__.ScheduleTask(start,"__main__.FindEntityByName('booClone').SetOrigin((%d,%d,%d))" % (o[0],o[1],o[2]))
            __main__.ScheduleTask(start,"__main__.FindEntityByName('booClone').SetAngles((%d,%d,%d))" % (a[0],a[1],a[2]-offset))
            distance = distance - 1.0

    else:
        # Activates special end credits
        __main__.G.Boo_HamsterDance=1
        
        g_petCounter=1
        start=0.0
        consoleutil.console("stopsound")
        hamDance=__main__.FindEntityByName("hamDance")
        if not hamDance: 
            hamDance=__main__.CreateEntityNoSpawn("npc_VHuman",(0,0,0),(0,0,0))
            hamDance.SetName("hamDance")
            hamDance.SetModel("models/null.mdl")
            __main__.CallEntitySpawn(hamDance)
        hamDance.SetParent("!player")
        hamDance.SetOrigin(__main__.FindPlayer().GetOrigin())
        hamDance.PlayDialogFile('character/monster/boo/hamsterdance.mp3')

        # song lasts 7 seconds.
        # 1.7 seconds for left roll
        # 2.1 seconds for right roll
        # 0.6 secods to get back to the middle
        # 1.3 seconds to go around.

        # roll left : .5
        distance = 0
        offset = 0
        __main__.ScheduleTask(start,"__main__.FindEntityByName('booClone').SetAngles((%d,%d,%d))" % (a[0],a[1],a[2]+offset))
        while distance != 10.0:
            start = start + 0.05
            offset = offset + 36
            o = boo.TraceCircle(distance,-90)
            o = (o[0],o[1],o[2]+2)
            __main__.ScheduleTask(start,"__main__.FindEntityByName('booClone').SetOrigin((%d,%d,%d))" % (o[0],o[1],o[2]))
            __main__.ScheduleTask(start,"__main__.FindEntityByName('booClone').SetAngles((%d,%d,%d))" % (a[0],a[1],a[2]+offset))
            distance = distance + 1

        # sit up .6
        angle = 0
        while angle != 180.0:
            start = start + 0.1
            angle = angle + 30
            __main__.ScheduleTask(start,"__main__.FindEntityByName('booClone').SetAngles((%d,%d,%d))" % (a[0]-angle,a[1],a[2]+offset))

        # sit down .6
        angle = 180.0
        while angle != 0.0:
            start = start + 0.1
            angle = angle - 30.0
            __main__.ScheduleTask(start,"__main__.FindEntityByName('booClone').SetAngles((%d,%d,%d))" % (a[0]-angle,a[1],a[2]+offset))

        # roll center .45
        distance = 8.0
        offset = 324
        __main__.ScheduleTask(start,"__main__.FindEntityByName('booClone').SetAngles((%d,%d,%d))" % (a[0],a[1],a[2]+offset))
        while distance != -1.0:
            start = start + 0.05
            offset = offset - 36
            o = boo.TraceCircle(distance,-90)
            o = (o[0],o[1],o[2]+2)
            __main__.ScheduleTask(start,"__main__.FindEntityByName('booClone').SetOrigin((%d,%d,%d))" % (o[0],o[1],o[2]))
            __main__.ScheduleTask(start,"__main__.FindEntityByName('booClone').SetAngles((%d,%d,%d))" % (a[0],a[1],a[2]+offset))
            distance = distance - 1.0

        # roll right .45
        distance = 1
        offset = 36
        __main__.ScheduleTask(start,"__main__.FindEntityByName('booClone').SetAngles((%d,%d,%d))" % (a[0],a[1],a[2]-offset))
        while distance != 10.0:
            start = start + 0.05
            offset = offset + 36
            o = boo.TraceCircle(distance,90)
            o = (o[0],o[1],o[2]+2)
            __main__.ScheduleTask(start,"__main__.FindEntityByName('booClone').SetOrigin((%d,%d,%d))" % (o[0],o[1],o[2]))
            __main__.ScheduleTask(start,"__main__.FindEntityByName('booClone').SetAngles((%d,%d,%d))" % (a[0],a[1],a[2]-offset))
            distance = distance + 1

        # sit up .5
        angle = 30
        while angle != 180.0:
            start = start + 0.1
            angle = angle + 30
            __main__.ScheduleTask(start,"__main__.FindEntityByName('booClone').SetAngles((%d,%d,%d))" % (a[0]-angle,a[1],a[2]+offset))

        # sit down .5
        angle = 150.0
        while angle != 0.0:
            start = start + 0.1
            angle = angle - 30.0
            __main__.ScheduleTask(start,"__main__.FindEntityByName('booClone').SetAngles((%d,%d,%d))" % (a[0]-angle,a[1],a[2]+offset))

        # roll center .5
        distance = 9.0
        offset = 360
        __main__.ScheduleTask(start,"__main__.FindEntityByName('booClone').SetAngles((%d,%d,%d))" % (a[0],a[1],a[2]-offset))
        while distance != -1.0:
            start = start + 0.05
            offset = offset - 36
            o = boo.TraceCircle(distance,90)
            o = (o[0],o[1],o[2]+2)
            __main__.ScheduleTask(start,"__main__.FindEntityByName('booClone').SetOrigin((%d,%d,%d))" % (o[0],o[1],o[2]))
            __main__.ScheduleTask(start,"__main__.FindEntityByName('booClone').SetAngles((%d,%d,%d))" % (a[0],a[1],a[2]-offset))
            distance = distance - 1.0

        # roll over
        distance = 0.0
        angle = -90
        offset = 0
        __main__.ScheduleTask(start,"__main__.FindEntityByName('booClone').SetAngles((%d,%d,%d))" % (a[0],a[1]-offset,a[2]+offset))
        while distance != 5.0:
            start = start + 0.05
            offset = offset + 18
            o = boo.TraceCircle(distance,angle)
            o = (o[0],o[1],o[2]+2)
            __main__.ScheduleTask(start,"__main__.FindEntityByName('booClone').SetOrigin((%d,%d,%d))" % (o[0],o[1],o[2]))
            __main__.ScheduleTask(start,"__main__.FindEntityByName('booClone').SetAngles((%d,%d,%d))" % (a[0],a[1]-offset,a[2]+offset))
            distance = distance + 0.5
            angle = angle - 10

        # twitch
        __main__.ScheduleTask(start,"__main__.FindEntityByName('booClone').SetAnimation('rat_walk')")
        __main__.ScheduleTask(start + 0.3,"__main__.FindEntityByName('booClone').SetAnimation('rat_idle')")
        __main__.ScheduleTask(start + 0.8,"__main__.FindEntityByName('booClone').SetAnimation('rat_walk')")
        __main__.ScheduleTask(start + 1.5,"__main__.FindEntityByName('booClone').SetAnimation('rat_idle')")

        # finish roll
        start = start + 1.8
        distance = 4.5
        angle = 180
        offset = 180
        __main__.ScheduleTask(start,"__main__.FindEntityByName('booClone').SetAngles((%d,%d,%d))" % (a[0],a[1]+offset,a[2]-offset))
        while distance != -0.5:
            start = start + 0.05
            offset = offset - 18
            o = boo.TraceCircle(distance,angle)
            o = (o[0],o[1],o[2]+2)
            __main__.ScheduleTask(start,"__main__.FindEntityByName('booClone').SetOrigin((%d,%d,%d))" % (o[0],o[1],o[2]))
            __main__.ScheduleTask(start,"__main__.FindEntityByName('booClone').SetAngles((%d,%d,%d))" % (a[0],a[1]+offset,a[2]-offset))
            distance = distance - 0.5
            angle = angle - 10

    # cleanup
    __main__.ScheduleTask(start,"__main__.FindEntityByName('booClone').SetModel('models/null.mdl')")
    __main__.ScheduleTask(start,"__main__.FindEntityByName('booClone').ClearParent()")
    __main__.ScheduleTask(start,"__main__.FindEntityByName('booAudio').ClearParent()")
    __main__.ScheduleTask(start,"__main__.FindEntityByName('%s').ScriptUnhide()" % boo.GetName())
    
# Generally triggered by "Faint()" command, but could also be triggered
# by enemy attacks that paralyze

def companion1_OnIncapacitatedStart():
    log("companion1_OnIncapacitatedStart")
    global inEvent
    inEvent=3

    try:
        c=__main__.FindEntityByName("companion1")
        c.TweakParam("hearing -1")
        c.TweakParam("vision -1")
        c.SetFollowerBoss("") # causes enemies to stop hitting
        c.SetData("InFakeDeath",1)

        # OnIncapacitatedEnd() doesn't work, so we fake it by scheduling
        # the event manually. Faint lasts for 120 seconds. We give them
        # 10 extra seconds to stand up and get their bearings. 

        __main__.ScheduleTask(128.0,"companion.companion1_OnIncapacitatedEnd()")

    finally:
        inEvent=0

def companion1_OnIncapacitatedEnd():
    log("companion1_OnIncapacitatedEnd")

    global inEvent
    inEvent=4

    try:
        c=__main__.FindEntityByName("companion1")
        if not c:
            c=__main__.FindEntityByName("companion_talking")
        c.SetData("InFakeDeath",0)
        if c.GetData("Follower"):
            makeFollowPC(c)
    finally:
        inEvent=0

def companion1_OnDamaged():
    global inEvent
    inEvent=5

    try:
        c=__main__.FindEntityByName("companion1")
        hits= c.GetData("hits")
        if hits==0:
            c.Faint()
            pc = __main__.FindPlayer()
            if pc.IsPC():
                c.SetData("hits",round(c.GetData("health") * pc.GetLevel() / 120))
            else:
                c.SetData("hits",round(c.GetData("health") * possessutil.GetPCInfoLevel() / 120))
        else:
            log("companion1_OnDamaged [%d] hits left" % c.GetData("hits"))
            hits-=1
            c.SetData("hits",hits)
    finally:
        inEvent=0

def companion1_OnDeath():
    log("companion1_OnDeath")
    # Two methods : get ID from npc object or grab ID from henchmen array 
    c=__main__.FindEntityByName("companion1")
    if c:
        npcKey = c.GetID()
        log("found companion1. Removing key [%s] from existance" % npcKey)
        i = __main__.G.complist.index(npcKey)
        log("Removing key [%s], index [%d] from G.complist" % (npcKey,i))
        del __main__.G.complist[i]
        i = __main__.G.henchmen.index(npcKey)
        log("Removing key [%s], index [%d] from G.henchmen" % (npcKey,i))
        del __main__.G.henchmen[__main__.G.henchmen.index(npcKey)]
    else:
        npcKey = __main__.G.henchmen[0]
        log("Cant find companion1. Assuming henchmen array index 0 [%s] " % npcKey)
        del __main__.G.complist[__main__.G.complist.index(npcKey)]
        del __main__.G.henchmen[0]

def companion1_OnHalfHealth():
    log("companion1_OnHalfHealth")

def companion1_OnFoundEnemy():
    log("companion1_OnFoundEnemy")
    if 0 == __main__.G.inCombat:
        # This typically occures when the PC force feeds a human. The game
        # treats the human as hostile even though combat hasn't begun. We
        # cancel the companion's desire to attack by respawning them, thus
        # resetting what they consider to be an enemy
        c1=__main__.FindEntityByName("companion1")
        if c1:
            c1.SetOrigin(__main__.FindPlayer().TraceLine(-50))
            makeHenchmanHelper(c1,2)
        
def companion1_OnLostEnemyLOS():
    log("companion1_OnLostEnemyLOS")

def companion1_OnLostEnemy():
    log("companion1_OnLostEnemy")

##############################
# Companion 2 Event Handlers #
##############################

def companion2_OnSpawnNPC():
    log("companion2_OnSpawnNPC")

def companion2_OnDialogBegin():
    """ Called from companion dialog files to support companion system"""
    log("companion2_OnDialogBegin")

    global inEvent
    global d_possessHenchman
    inEvent=6

    c=__main__.FindEntityByName("companion2")
    if not c:
        c=__main__.FindEntityByName("companion_talking")

    c.SetScriptedDiscipline("obfuscate 0")
    c.SetData("InStealth",0)
    
def companion2_OnDialogEnd():
    """ Called from companion dialog files to support companion system"""
    log("companion2_OnDialogEnd")
    global inEvent
    global d_removeHenchman
    global d_makeHenchman
    global d_removeFromParty
    global d_possessHenchman
    global d_unpossessHenchman
    global d_resetCompanions
    global d_summonSpell

    try:
        c=__main__.FindEntityByName("companion_talking")
        if c:
            c.SetName("companion2")
            if 4 == c.GetData("Embraced") and 5 == c.GetData("Type"):
                # PC embraced
                c.SetData("Embraced",1)
                embrace(c)
            elif 3 == c.GetData("Embraced") and 5 == c.GetData("Type"):
                # PC decided not to embrace
                c.SetData("Type",4)
                c.SetData("Embraced",0)
            elif d_removeHenchman:
                d_removeHenchman=0
                if havenutil.isInHaven():
                    removeHenchmanHelper(c,1,1)
                else:
                    removeHenchmanHelper(c)
            elif d_makeHenchman:
                d_makeHenchman=0
                makeHenchmanHelper(c)
            elif d_possessHenchman:
                d_possessHenchman=0
                possessutil.registerCallback("companion.OnPossessEnd('companion2')") 
                possessutil.possess(c,"companion*")
            elif d_unpossessHenchman:
                d_unpossessHenchman=0
                possessutil.registerCallback("companion.OnUnPossessEnd('companion2')") 
                possessutil.unpossess("companion*")            
            elif d_removeFromParty:
                d_removeFromParty=0
                removeFromPartyHelper(c)
            elif d_resetCompanions:
                d_resetCompanions=0
                ResetCompanionHelper()
            elif 1 == d_summonSpell:
                d_summonSpell=0
                summonBoo(c)
            elif 2 == d_summonSpell:
                d_summonSpell=0
                summonBoo(c,0,0)
        else:
            log("Warning: companion2 not found after dialog. (Likely called remove henchman)")

    finally:
        inEvent=0

# Generally triggered by "Faint()" command, but could also be triggered
# by enemy attacks that paralyze

def companion2_OnIncapacitatedStart():
    global inEvent

    log("companion2_OnIncapacitatedStart")
    inEvent=7

    try:
        c=__main__.FindEntityByName("companion2")
        c.TweakParam("hearing -1")
        c.TweakParam("vision -1")
        c.SetFollowerBoss("") # causes enemies to stop attacking
        c.SetData("InFakeDeath",1)

        # OnIncapacitatedEnd() doesn't work, so we fake it by scheduling
        # the event manually. Faint lasts for 120 seconds. We give them
        # 10 extra seconds to stand up and get their bearings. 

        __main__.ScheduleTask(128.0,"companion.companion2_OnIncapacitatedEnd()")

    finally:
        inEvent=0

def companion2_OnIncapacitatedEnd():
    global inEvent

    log("companion2_OnIncapacitatedEnd")
    inEvent=8

    try:
        c=__main__.FindEntityByName("companion2")
        if not c:
            c=__main__.FindEntityByName("companion_talking")
        c.SetData("InFakeDeath",0)
        if c.GetData("Follower"):
            makeFollowPC(c)
    finally:
        inEvent=0

# TODO : try catch to cache companion ptr?
def companion2_OnDamaged():
    global inEvent
    inEvent=9

    try:
        c=__main__.FindEntityByName("companion2")
        hits= c.GetData("hits")
        if hits==0:
            c.Faint()
            pc = __main__.FindPlayer()
            if pc.IsPC():
                c.SetData("hits",round(c.GetData("health") * pc.GetLevel() / 120))
            else:
                c.SetData("hits",round(c.GetData("health") * possessutil.GetPCInfoLevel() / 120))
        else:
            log("companion2_OnDamaged [%d] hits left" % c.GetData("hits"))
            hits-=1
            c.SetData("hits",hits)
    finally:
        inEvent=0

def companion2_OnDeath():
    log("companion2_OnDeath")

    # Two methods : get ID from npc object or grab ID from henchmen array 
    c=__main__.FindEntityByName("companion2")
    if c:
        npcKey = c.GetID()
        log("found companion2. Removing key [%s] from existance" % npcKey)
        i = __main__.G.complist.index(npcKey)
        log("Removing key [%s], index [%d] from G.complist" % (npcKey,i))
        del __main__.G.complist[i]
        i = __main__.G.henchmen.index(npcKey)
        log("Removing key [%s], index [%d] from G.henchmen" % (npcKey,i))
        del __main__.G.henchmen[__main__.G.henchmen.index(npcKey)]
    else:
        npcKey = __main__.G.henchmen[1]
        log("Cant find companion1. Assuming henchmen array index 1 [%s] " % npcKey)
        del __main__.G.complist[__main__.G.complist.index(npcKey)]
        del __main__.G.henchmen[1]

def companion2_OnHalfHealth():
    log("companion2_OnHalfHealth")

def companion2_OnFoundEnemy():
    log("companion2_OnFoundEnemy")
    if 0 == __main__.G.inCombat:
        # This typically occures when the PC force feeds a human. The game
        # treats the human as hostile even though combat hasn't begun. We
        # cancel the companion's desire to attack by respawning them, thus
        # resetting what they consider to be an enemy
        c2=__main__.FindEntityByName("companion2")
        if c2:
            c2.SetOrigin(__main__.FindPlayer().TraceLine(-100))
            makeHenchmanHelper(c2,2)

def companion2_OnLostEnemyLOS():
    log("companion2_OnLostEnemyLOS")

def companion2_OnLostEnemy():
    log("companion2_OnLostEnemy")

#####################
# Update Base Class #
#####################
    
def _IsCompanion(self,key=None):
    if not key: key=self.GetID()
    if key in __main__.G.complist:
        return 1
    return 0

Character.IsCompanion=_IsCompanion

######################
# logic_auto Handler #
######################
#
# Only gets called when transitioning into map from another map.
# Does NOT get called on savegame reload.
    
def auto_OnMapLoad(map=""):
    log("companion.auto_OnMapLoad('%s') called" % map)

    verifyMap = __main__.FindEntityByName("general_companion1_maker")
    if not verifyMap:
        log("companion : OnMapLoad : Support modules not found. OnMapLoad Cancelled")
        return
    
    verifyTimer = __main__.FindEntityByName("feed_timer")
    if not verifyTimer:
        timer=__main__.CreateEntityNoSpawn("hud_timer",(0,0,0),(0,0,0))
        timer.SetName("feed_timer")
        __main__.CallEntitySpawn(timer)

    if  "sp_observatory_1" == map:
        if 0 == __main__.G.sp_observatory_once:
            __main__.G.sp_observatory_once=1
            ResetCompanionHelper()        
    elif "sp_observatory_2" != map:
        ResetCompanionHelper()

#################
# Custom Events #
#################

# --------------
# OnPossessEnd |
# --------------
#
# Must be called after Possess to make corrections to
# the (Companion managed) G.henchmen array.
#
# See possessutil.py
# Execution Trace Notes:
#   dialog
#     -> companion.possessHenchman()
#   companion.possessHenchman()
#     -> d_possessHenchman = 1
#   companion.companionX_OnDialogEnd() : if d_possessHenchman
#     -> possessutil.registerCallback("companion.OnPossessEnd"))
#     -> possessutil.possess(npc)
#   possessutil.possess(npc)
#     -> possessHelper()
#   possessutil.possessHelper()
#     -> ScheduleTask(callback)
#   companion.OnPossessEnd

def OnPossessEnd(npcName):
    log("companion.OnPossessEnd('%s')" % npcName)

    pc=__main__.FindPlayer()
    npc=__main__.FindEntityByName(npcName)

    # Copy companion info from PC Body
    npc.CloneData(pc)
    if npc.IsPC():
        log("Found NPC (model=[%s]). Calling clone" % npc.model)
        log("PC (model=[%s]). Calling clone" % pc.model)
        npc.SetData("Model",npc.model)
    
    # Update the henchmen array:
    i = len(__main__.G.henchmen)
    while i > 0:
       del __main__.G.henchmen[i-1]
       i-=1
    companions = __main__.FindEntitiesByName("companion*")
    for c in companions: __main__.G.henchmen.append(c.GetID())
    
    # Set global to support dialog options. 
    if pc.IsPC():
        __main__.G.possessed=0
    else:
        __main__.G.possessed=1
            
# --------------
# OnUnPossessEnd |
# --------------
#
# Must be called after Unpossess to make corrections to
# the (Companion managed) G.henchmen array. 
#
# See possessutil.py
# Execution Trace Notes:
#   dialog
#     -> companion.unpossessHenchman()
#   companion.unpossessHenchman()
#     -> d_possessHenchman = 1
#   companion.companionX_OnDialogEnd() : if d_possessHenchman
#     -> possessutil.registerCallback("companion.OnUnPossessEnd"))
#     -> possessutil.unpossess(npc)
#   possessutil.unpossess(npc)
#     -> unpossessHelper()
#   possessutil.unpossessHelper()
#     -> ScheduleTask(callback)
#   companion.OnUnPossessEnd

def OnUnPossessEnd(npcName):
    log("companion.OnUnPossessEnd('%s')" % npcName)

    pc=__main__.FindPlayer()
    npc=__main__.FindEntityByName(npcName)

    log("pc.model=[%s] npc.model=[%s]" % (pc.model,npc.model))

    #if npc:
    #print "Found NPC (model=[%s]). Calling clone" % npc.model
    #print "PC (model=[%s]). Calling clone" % pc.model
    # Copy companion info onto New Body
    #npc.CloneData(pc)
    #Update model
    #npc.SetData("Model",npc.model)
    # Update the henchmen array:
    i = len(__main__.G.henchmen)
    while i > 0:
       del __main__.G.henchmen[i-1]
       i-=1
    companions = __main__.FindEntitiesByName("companion*")
    for c in companions: __main__.G.henchmen.append(c.GetID())

    __main__.G.possessed=0

# --------------
# OnCombatStart |
# --------------
# See vamputils.py
# Execution Trace Notes:
#   events_world: OnCombatMusicStart
#     -> vamputils.OnBeginCombatMusic()
#   vamputils.OnBeginCombatMusic()
#     -> vamputils.OnBeginCombat
#   vamputils.OnBeginCombat
#     -> companion.OnCombatStart()
#   companion.OnCombatStart

def CombatStartHelper(c):

    log("Combat Start: processing companion [%s]" % c.GetName())

    if c.GetData("NoFight"):
        c.SetScriptedDiscipline("obfuscate 4")
        c.SetData("InStealth",1)
        task="__main__.FindEntityByName('%s').ScriptHide()" % c.GetName()
        __main__.ScheduleTask(1.5,task)
        if c.GetID() == "models/character/monster/boo":
            __main__.FindPlayer().GiveItem("item_p_occult_obfuscate")
    elif c.IsFollowerOf(__main__.FindPlayer()):
        c.SetScriptedDiscipline("obfuscate 0")
        c.SetData("InStealth",0)
        # AI
        if not c.IsHuman():
            log("Vampire Companion Detected")
            if c.IsPC():
                log("PC companion detected")
                # Use G._pcinfo
                if not (-1 == __main__.G._pcinfo["auspex"]):
                    log("Activating Discipline auspex %d" % __main__.G._pcinfo["auspex"])
                    c.SetScriptedDiscipline("auspex %d" % __main__.G._pcinfo["auspex"])
                if not (-1 == __main__.G._pcinfo["celerity"]):
                    log("Activating Discipline celerity %d" % __main__.G._pcinfo["celerity"])
                    c.SetScriptedDiscipline("celerity %d" % __main__.G._pcinfo["celerity"])
                    c.SetMovementMultiplier(2.0)
                if not (-1 == __main__.G._pcinfo["fortitude"]):
                    log("Activating Discipline fortitude %d" % __main__.G._pcinfo["fortitude"])
                    c.SetScriptedDiscipline("fortitude %d" % __main__.G._pcinfo["fortitude"])
                if not (-1 == __main__.G._pcinfo["potence"]):
                    log("Activating Discipline potence %d" % __main__.G._pcinfo["potence"])
                    c.SetScriptedDiscipline("potence %d" % __main__.G._pcinfo["potence"])
                if not (-1 == __main__.G._pcinfo["presence"]):
                    log("Activating Discipline presence %d" % __main__.G._pcinfo["presence"])
                    c.SetScriptedDiscipline("presence %d" % __main__.G._pcinfo["presence"])
                if (2 < __main__.G._pcinfo["thaumaturgy"]):
                    log("Activating Discipline thaumaturgy 3")
                    c.SetBloodShieldDiscipline(1)
            elif c.IsEmbraced():
                log("Embraced companion detected")
                # Use G._pcinfo
                if not (-1 == __main__.G._pcinfo["auspex"]):
                    log("Activating Discipline auspex 1")
                    c.SetScriptedDiscipline("auspex 1")
                if not (-1 == __main__.G._pcinfo["celerity"]):
                    log("Activating Discipline celerity 1")
                    c.SetScriptedDiscipline("celerity 1")
                if not (-1 == __main__.G._pcinfo["fortitude"]):
                    log("Activating Discipline fortitude 1")
                    c.SetScriptedDiscipline("fortitude 1")
                if not (-1 == __main__.G._pcinfo["potence"]):
                    log("Activating Discipline potence 1")
                    c.SetScriptedDiscipline("potence 1")
                if not (-1 == __main__.G._pcinfo["presence"]):
                    log("Activating Discipline presence 1")
                    c.SetScriptedDiscipline("presence 1")
            else:
                disciplines = statutil.GetDisciplinesByID(c.GetID())
                if disciplines:
                    if not (-1 == disciplines[1]) : #(Auspex)
                        log("Activating Discipline auspex %d" % disciplines[1])
                        c.SetScriptedDiscipline("auspex %d" % disciplines[1])
                    if not (-1 == disciplines[3]) : #(Celerity)
                        log("Activating Discipline celerity %d" % disciplines[3])
                        c.SetScriptedDiscipline("celerity %d" % disciplines[3])
                        c.SetMovementMultiplier(2.0)
                    if not (-1 == disciplines[7]) : #(Fortitude)
                        log("Activating Discipline fortitude %s" % disciplines[7])
                        c.SetScriptedDiscipline("fortitude %d" % disciplines[7])
                    if not (-1 == disciplines[9]) : #(Potence)
                        log("Activating Discipline potence %d" % disciplines[9])
                        c.SetScriptedDiscipline("potence %d" % disciplines[9])
                    if not (-1 == disciplines[10]) : #(Presence)
                        log("Activating Discipline presence %d" % disciplines[10])
                        c.SetScriptedDiscipline("presence %d" % disciplines[10])
                    if (2 < disciplines[12]) : #(Thaumaturgy)
                        log("Activating Discipline thaumaturgy 3")
                        c.SetBloodShieldDiscipline(1)
        else:
            log("Companion is Human. Skipping AI")
 
        c.TweakParam("hearing 50")
        c.TweakParam("vision 250")        

def OnCombatStart():
    log("OnCombatStart")
    global inEvent
    inEvent=10

    try:
        __main__.G.inCombat=1
        c1=__main__.FindEntityByName("companion1")
        if c1: CombatStartHelper(c1)
        c2=__main__.FindEntityByName("companion2")
        if c2: CombatStartHelper(c2)
        
    finally:
        inEvent=0

def CombatEndHelper(c):
    log("CombatEnd : processing companion [%s]" % c.GetName())
    if c.GetData("NoFight"):
        if c.GetID() == "models/character/monster/boo":
            boos=__main__.FindEntitiesByClass("item_p_occult_obfuscate")
            for boo in boos:
                boo.Kill()
        c.ScriptUnhide()
    c = makeHenchmanHelper(c,2)
    c.SetData("InFakeDeath",0)

# --------------
# OnCombatEnd |
# --------------
# See vamputils.py
# Execution Trace Notes:
#   events_world: OnNormalMusicStart
#     -> vamputils.OnBeginNormalMusic()
#   vamputils.OnBeginNormalMusic()
#     -> vamputils.OnEndCombat
#   vamputils.OnEndCombat
#     -> companion.OnCombatEnd()
#   companion.OnCombatEnd
#
# NOTES: The only way to end combat "grudges" is to
# kill the current companion instance and respawn. This
# also addresses things like reviving fallen companions,
# and ending any vampire disciplines.

# See vamputils.py
def OnCombatEnd():
    global inEvent

    log("OnCombatEnd")
    inEvent=11

    try:
        __main__.G.inCombat=0
        c1=__main__.FindEntityByName("companion1")
        if c1: CombatEndHelper(c1)
        c2=__main__.FindEntityByName("companion2")
        if c2: CombatEndHelper(c2)
                
    finally:
        inEvent=0


#######################
# logic_timer Handler #
#######################
# 
# Timer fires every 15 seconds allows us to poll game state. Primary duty is keeping
# the NPC near the PC by auto teleporting if NPC gets out of circular range.
#
# Secondary duty is making the npc go stealth if the PC is trying to play stealth.
# Solution is not perfect. If companion touches enemy, enemy  becomes aware of
# companion and attacks companion. Companion will defend themself.
#
# timer is not thread safe. Most of the events fire from the main thread and are
# therefore mutually exclusive. (OnHearPlayer is maybe the one exception).
# The timer on the other hand fires whenever... and can (and has) presented race
# conditions. Some of these I ran into and fixed through design (makeHenchman, notice
# that I append "_scap" to the name instead of renaming). However, I am sure there
# are cases I haven't identitified. I have also tried to minimize the possibility
# of overlooked conflicts with the "inEvent" flag. But it is not bullet proof.
# That said, I haven't seen any problems since I introduced the inEvent flag. 

def timer_OnTimer():
    """ Polled method makes sure companions keep up with pc and go to stealth if PC tries to hide """
    global inEvent

    log("timer_OnTimer")

    if 0 == inEvent:
        if __main__.G._spawnFailure:
            clearCompanions()
            populateCompanions()

        pc = __main__.FindPlayer()

        # Search for no teleport beacon. If found, hide companions and do nothing. 
        beacons = __main__.FindEntitiesByName("no_npc_teleport")
        nearNoTeleport=0
        if 0 != len(beacons):
            for node in beacons:
                angles = node.GetAngles()
                dist = round(angles[0] * angles[1]) 
                if pc.Near(node.GetOrigin(),dist):
                    log("Player near no NPC Teleport Beacon.",4)
                    nearNoTeleport=1
                    break

        companions=__main__.FindEntitiesByName("companion*")
        if 1 == nearNoTeleport:
            if 0 == __main__.G._hidecomps:
                for c in companions:
                    c.ScriptHide()
                __main__.G._hidecomps=1
            return
        elif 1 == __main__.G._hidecomps:
            for c in companions:
                c.ScriptUnhide()
            __main__.G._hidecomps=0
            # the return here affords you another 15 sec after you
            # get off the elevator before they re-appear. 
            return

        pcStealth=pc.IsStealth()
        i=0
        for c in companions:
            npcCurrLoc=c.GetOrigin()

            npcStealth=c.GetData("InStealth")
            npcFakeDeath=c.GetData("InFakeDeath")
            npcNoFight=c.GetData("NoFight")
            npcLastLoc=c.GetData("LastLocation")
            c.SetData("LastLocation",npcCurrLoc)

            if pcStealth and not npcFakeDeath:
                if not npcStealth:
                    if __main__.G.inCombat and c.IsFollowerOf(pc):
                        c = makeHenchmanHelper(c,2)
                    c.SetScriptedDiscipline("obfuscate 4")
                    c.SetData("InStealth",1)
            else:
                if npcStealth:
                    if not npcNoFight or not __main__.G.inCombat:
                        c.SetScriptedDiscipline("obfuscate 0")
                        c.SetData("InStealth",0)
        
            if  c.IsFollowerOf(pc) and not pcStealth and not npcFakeDeath and not __main__.G.inCombat:
                # BUG Fix : Testing revealed getting stuck a lot because npc was
                # blocking door (and couldn't talk to npc). Added 15 no movemenet
                # timeout whereby npc will get behind player again. To unblock
                # doorways. 
                if npcLastLoc == npcCurrLoc or (not c.Near(pc.GetOrigin(),200)):
                     i+=1
                     c.SetOrigin(pc.TraceLine(-50 * i))
    else:
        log("timer skipped (in event)")
  

def OnInventoryClose():
    i=None
    npc=None
    try:
        i = __main__.FindEntityByName("global_inventory")
        npc = __main__.FindEntityByName(__main__.G.LDName)
    except:
        pass
    if i and npc:
        __main__.G._inventory = i.GetItems()
        __main__.G._inventoryCount=[]
        index=0
        while index < len(__main__.G._inventory):
            __main__.G._inventoryCount.append(i.AmmoCount(__main__.G._inventory[index]))
            index=index+1
        i.DeleteItems()
        i.ScriptHide()
        npc.ScriptUnhide()
    else:
        log("Inventory Support objects not found Aborting Inventory",3)

###########
# Special #
###########

def canCastSummonSpell():
    if ("item_p_occult_hacking" in __main__.G._inventory): return 1
    return 0

def summonBoo(c,thread=0,safe=1):
    from vamputil import showParticle

    global inEvent
    inEvent=12

    log("summonBoo")
    try:
        if 0 == thread:
            hasitems=1
            missing = ""
            if not ("item_p_occult_hacking" in __main__.G._inventory):
                hasitems=1
                missing="the Summon Spell."
            if not ("item_g_eldervitaepack" in __main__.G._inventory):
                hasitems=1
                missing="Elder Blood Vitae."
            if not ("item_g_stake" in __main__.G._inventory):
                hasitems=1
                missing="a wooden stake."
            if not ("item_g_ring_gold" in __main__.G._inventory):
                hasitems=1
                missing="a plain gold ring."
            #if not ("item_g_lilly_purse" in __main__.G._inventory):
                #hasitems=0
                #missing="a woman's purse."
            if hasitems:
                stopFollowPC(c)
                c.WillTalk(0)
                pevents=None
                peventslist=__main__.FindEntitiesByClass("events_player")
                if len(peventslist) > 0:
                    pevents=peventslist[0]
                    pevents.ImmobilizePlayer()
                wevents=None
                weventslist=__main__.FindEntitiesByClass("events_world")
                if len(weventslist) > 0:
                    wevents=weventslist[0]
                    wevents.HideCutsceneInterferingEntities()
                del __main__.G._inventory[__main__.G._inventory.index("item_p_occult_hacking")]                
                del __main__.G._inventory[__main__.G._inventory.index("item_g_eldervitaepack")]                
                del __main__.G._inventory[__main__.G._inventory.index("item_g_stake")]                
                del __main__.G._inventory[__main__.G._inventory.index("item_g_ring_gold")]                
                del __main__.G._inventory[__main__.G._inventory.index("item_g_lilly_purse")]                
                __main__.ScheduleTask(0.1,"consoleutil.console(\"say AUTOSAVING (If Game crashes, reload autosave)\\ncompanion.summonBoo(__main__.FindEntityByName('%s'),1,%d)\")" % (c.GetName(),safe))
                return
            else:
                __main__.ScheduleTask(0.1,"consoleutil.console(\"say You attempt to cast the spell but it fizzles out.\\nsay The backpack is missing %s\")" % missing)
                return    
        elif 1 == thread:
            __main__.cvar.cam_yaw=0
            __main__.ccmd.thirdperson=""
            __main__.cvar.cam_idealdist=115
            __main__.ScheduleTask(3.0,"companion.summonBoo(__main__.FindEntityByName('%s'),2,%d)" % (c.GetName(),safe))
            return
        elif 2 == thread:
            __main__.ccmd.autosave=""
            __main__.cvar.draw_hud=0
            __main__.ScheduleTask(1.0,"companion.summonBoo(__main__.FindEntityByName('%s'),3,%d)" % (c.GetName(),safe))
            return
        elif 3 == thread:
            __main__.ccmd.stopsound=""
            if not safe:
                showParticle("temple_teleport_emitter.txt",32,c.GetOrigin(),(0,0,0),1)
            __main__.ScheduleTask(0.5,"companion.summonBooHelper('%s',13)" % c.GetName())
    finally:
        inEvent=0

g_restoreNPCList=[]
def summonBooHelper(npcName,thread=0):
    global g_restoreNPCList
    c=__main__.FindEntityByName(npcName)
    s1=None
    s2=None
    if thread < 13: s1=__main__.FindEntityByName("scrap_temp_sound1")
    if thread < 10: s2=__main__.FindEntityByName("scrap_temp_sound2")
    log("thread = [%d]" % thread)
    if 13 == thread:
        s1 = __main__.CreateEntityNoSpawn("npc_VHuman", c.GetOrigin(), (0,0,0))
        s1.SetName("scrap_temp_sound1")
        s1.SetModel("models/null.mdl")
        __main__.CallEntitySpawn(s1)
        # There is something supernatural happening. Let people near PC
        # know it and inflict masquerade violation if seen
        __main__.FindPlayer().SetSupernaturalLevel(6)
        s1.PlayDialogFile("environmental/machines/elevator_crashes.wav")
        #Spawn Doorway
        angles  = c.GetAngles()
        revAngles = (angles[0],angles[1]-180,angles[2])
        b1 = __main__.CreateEntityNoSpawn("prop_dynamic", c.TraceLine(340), revAngles)
        b1.SetName("scrap_temp_background")
        b2 = __main__.CreateEntityNoSpawn("prop_dynamic", c.TraceLine(-168), angles)
        b2.SetName("scrap_temp_doorway")
        b1.SetModel("models/scenery/Structural/Ritual_Chamber/Ritual_Chamber.mdl")
        b2.SetModel("models/scenery/Structural/Theatarch/Theatarch.mdl")
        __main__.CallEntitySpawn(b1)
        __main__.CallEntitySpawn(b2)
        __main__.ScheduleTask(1.0,"companion.summonBooHelper('%s',12)" % npcName)
    elif 12 == thread:
        __main__.ccmd.thirdperson=""
        __main__.cvar.cam_idealdist=145
        __main__.ScheduleTask(1.0,"companion.summonBooHelper('%s',11)" % npcName)
    elif 11 == thread:
        __main__.ccmd.thirdperson=""
        __main__.cvar.cam_idealdist=180
        s1.PlayDialogFile("disciplines/potence/maintain.wav")
        __main__.ScheduleTask(2.0,"companion.summonBooHelper('%s',10)" % npcName)
    elif 10 == thread:
        s2 = __main__.CreateEntityNoSpawn("npc_VHuman", c.GetOrigin(), (0,0,0))
        s2.SetName("scrap_temp_sound2")
        s2.SetModel("models/null.mdl")
        __main__.CallEntitySpawn(s2)
        __main__.ScheduleTask(1.0,"companion.summonBooHelper('%s',9)" % npcName)
    elif 9 == thread:
        npcs = __main__.FindEntitiesByClass("npc_V*")
        for npc in npcs:
            try:
                # We dont want to add NPCs that are already
                # hidden to the list as we may break
                # something. 224 means npc is hidden
                if 224 != npc.effects and "" != npc.GetName() and not (npc.GetName().startswith("scrap")):
                    g_restoreNPCList.append(npc)
                    npc.ScriptHide()
            except:
                pass
        o=c.TraceLine(-270)
        fixedOrigin= (o[0],o[1],o[2]-150)
        b3 = __main__.CreateEntityNoSpawn("prop_dynamic", fixedOrigin, c.GetAngles())
        b3.SetName("scrap_temp_light")
        b3.SetModel("models/scenery/Structural/Ritual_Chamber/Beam.mdl")
        __main__.CallEntitySpawn(b3)
        s2.PlayDialogFile("epic/explosion8.wav")
        consoleutil.console("shake")
        __main__.ScheduleTask(5.0,"companion.summonBooHelper('%s',8)" % npcName)
    elif 8 == thread:
        npcID = c.GetID()
        # Remove NPC from party, but keep the body around.
        # so we can re-use it for boo.
        if npcID in __main__.G.complist:
            if npcID in __main__.G.henchmen:
                log("Deleting henchman key [%s]" % npcID)
                del __main__.G.henchmen[__main__.G.henchmen.index(npcID)]
            del __main__.G.complist[__main__.G.complist.index(npcID)]
            # remove previous ID and info from save data
            try:
                if __main__.G.npcdata.has_key(npcID):
                    del __main__.G.npcdata[npcID]
            except:
                log("summonBoo: Unable to remove old key from complist." % npcID,3)
        else:
            log("summonBoo: npcID [%s] not in complist" % npcID)
        s1.PlayDialogFile("disciplines/potence/maintain.wav")
        s2.PlayDialogFile("character/monster/gargoyle/idle_agitated_3.wav")
        __main__.ScheduleTask(3.0,"companion.summonBooHelper('%s',7)" % npcName)
    elif 7 == thread:
        s2.PlayDialogFile("area/special/observatory/skylight_landing_1.wav")
        consoleutil.console("shake")
        __main__.ScheduleTask(2.0,"companion.summonBooHelper('%s',6)" % npcName)
    elif 6 == thread:
        s2.PlayDialogFile("area/special/observatory/skylight_landing_2.wav")
        consoleutil.console("shake")
        __main__.ScheduleTask(4.0,"companion.summonBooHelper('%s',5)" % npcName)
    elif 5 == thread:
        s2.PlayDialogFile("character/monster/boo/minsc_bat.wav")
        __main__.ScheduleTask(1.0,"companion.summonBooHelper('%s',4)" % npcName)
    elif 4 == thread:
        s1.PlayDialogFile("disciplines/potence/maintain.wav")
        __main__.ScheduleTask(4.0,"companion.summonBooHelper('%s',3)" % npcName)
    elif 3 == thread:
        o = c.TraceLine(-125)
        r = __main__.FindPlayer().GetAngles()
        fixedFacing = (r[0],r[1]-270,r[2])
        fixedOrigin = (o[0],o[1],o[2]+30)
        m = __main__.CreateEntityNoSpawn("prop_dynamic", fixedOrigin, fixedFacing)
        m.SetName("scrap_temp_monster")
        m.SetModel("models/scenery/Misc/Diarama/Thead.mdl")
        __main__.CallEntitySpawn(m)   
        m.SetOrigin(fixedOrigin)
        s2.PlayDialogFile("character/monster/werewolf/roar_long_1.wav")
        __main__.ScheduleTask(1.0,"companion.summonBooHelper('%s',2)" % npcName)
    elif 2 == thread:
        m=__main__.FindEntityByName("scrap_temp_monster")
        o = c.TraceLine(-110)
        fixedOrigin = (o[0],o[1],o[2]+45)
        m.SetOrigin(fixedOrigin)
        __main__.ScheduleTask(0.5,"companion.summonBooHelper('%s',-1)" % npcName)
    elif -1 == thread:
        m=__main__.FindEntityByName("scrap_temp_monster")
        o = c.TraceLine(-90)
        fixedOrigin = (o[0],o[1],o[2]+60)
        m.SetOrigin(fixedOrigin)
        __main__.ScheduleTask(0.5,"companion.summonBooHelper('%s',-2)" % npcName)
    elif -2 == thread:
        m=__main__.FindEntityByName("scrap_temp_monster")
        o = c.TraceLine(-95)
        fixedOrigin = (o[0],o[1],o[2]+65)
        m.SetOrigin(fixedOrigin)
        __main__.ScheduleTask(0.5,"companion.summonBooHelper('%s',-3)" % npcName)
    elif -3 == thread:
        m=__main__.FindEntityByName("scrap_temp_monster")
        o = c.TraceLine(-100)
        fixedOrigin = (o[0],o[1],o[2]+70)
        m.SetOrigin(fixedOrigin)
        __main__.ScheduleTask(0.5,"companion.summonBooHelper('%s',-4)" % npcName)
    elif -4 == thread:
        m=__main__.FindEntityByName("scrap_temp_monster")
        o = c.TraceLine(-110)
        fixedOrigin = (o[0],o[1],o[2]+80)
        m.SetOrigin(fixedOrigin)
        __main__.ScheduleTask(0.5,"companion.summonBooHelper('%s',-5)" % npcName)
    elif -5 == thread:
        m=__main__.FindEntityByName("scrap_temp_monster")
        o = c.TraceLine(-120)
        fixedOrigin = (o[0],o[1],o[2]+80)
        m.SetOrigin(fixedOrigin)
        __main__.ScheduleTask(0.5,"companion.summonBooHelper('%s',-6)" % npcName)
    elif -6 == thread:
        consoleutil.console("firstperson")
        m=__main__.FindEntityByName("scrap_temp_monster")
        o = c.TraceLine(-125)
        fixedOrigin = (o[0],o[1],o[2]+90)
        m.SetOrigin(fixedOrigin)
        __main__.ScheduleTask(0.5,"companion.summonBooHelper('%s',-7)" % npcName)
    elif -7 == thread:
        m=__main__.FindEntityByName("scrap_temp_monster")
        o = c.TraceLine(-150)
        fixedOrigin = (o[0],o[1],o[2]+100)
        m.SetOrigin(fixedOrigin)
        __main__.ScheduleTask(0.5,"companion.summonBooHelper('%s',-8)" % npcName)
    elif -8 == thread:
        m=__main__.FindEntityByName("scrap_temp_monster")
        m.Kill()
        c.SetModel("models/character/monster/boo/boo.mdl")
        s2.PlayDialogFile("disciplines/potence/deactivate.wav")
        __main__.ScheduleTask(1.0,"companion.summonBooHelper('%s',-9)" % npcName)
    elif -9 == thread:
        __main__.FindPlayer().PlayHUDParticle("chang_blast_emitter")
        __main__.ScheduleTask(1.0,"companion.summonBooHelper('%s',-10)" % npcName)
    elif -10 == thread:
        __main__.FindPlayer().PlayHUDParticle("cold_explosion_emitter")
        __main__.ScheduleTask(0.5,"companion.summonBooHelper('%s',0)" % npcName)
    elif 0 == thread:
        b1=__main__.FindEntityByName("scrap_temp_background")
        b2=__main__.FindEntityByName("scrap_temp_doorway")
        b3=__main__.FindEntityByName("scrap_temp_light")
        b1.Kill()
        b2.Kill()
        b3.Kill()
        for npc in g_restoreNPCList:
            npc.ScriptUnhide()
        g_restoreNPCList=[]
        pevents=None
        peventslist=__main__.FindEntitiesByClass("events_player")
        if len(peventslist) > 0:
            pevents=peventslist[0]
            pevents.MobilizePlayer()
        wevents=None
        weventslist=__main__.FindEntitiesByClass("events_world")
        if len(weventslist) > 0:
            wevents=weventslist[0]
            wevents.UnhideCutsceneInterferingEntities()
        __main__.cvar.cam_idealdist=85
        __main__.cvar.draw_hud=1
        s1.Kill()        
        s2.Kill()        
        c.WillTalk(1)
        c.SetName("Boo")
        __main__.ScheduleTask(2.0, "companion.addToParty(__main__.FindEntityByName('%s'),4)" % c.GetName())

# event fired from Damsel entity in la_hub when she reaches
# half health. Remember that PC may have companions. Not shown here
# is that Damsel goes invincible so that you can't accidently kill
# her.

def HandleDamselFall(state=1):

    # Dont use factories. Too unstable. 2 Versions of Damsel. 1 that
    # you fight and then one that you talk to post fight. No auto-dialog
    # too dificult.
    #
    # Set flag G.Damsel_Comp so that secondary conversations with her will
    # be "Listening" or "Anything else...". This will also aid with the
    # lucky star onMapLoader. 
    
    damsel = __main__.FindEntityByName("Damsel")
    pevents = __main__.FindEntityByName("pevents")
    if 1==state:
        #immbolize the pc:
        pevents.ImmobilizePlayer()
        c1=__main__.FindEntityByName("companion1")
        c2=__main__.FindEntityByName("companion2")
        if c1:
            log("Hiding comapnion 1")
            c1.ScriptHide()
            c1.SetName("companion1_damsel")
        if c2:
            log("Hiding comapnion 2")
            c2.ScriptHide()
            c2.SetName("companion2_damsel")

        # damsel falls part 1
        if damsel:
            damsel.ClearActiveDisciplines()
            damsel.Faint()
        __main__.ccmd.fadeout=""
        __main__.ScheduleTask(3.0,"companion.HandleDamselFall(2)")
    elif 2==state:

        # damsel falls part 2
        ccommand=""
        if damsel:
            damsel.SetName("Damsel_scrap")
            damsel.Kill()
        damsel2 = __main__.FindEntityByName("Damsel2")
        if damsel2:
            damsel2.ScriptUnhide()
            damsel2.SetName("Damsel")
            __main__.G.Damsel_FightEnd=1
        else:
            ccommand += "say 'Compmod Error: Unable to find Damsel. Return to The Last Round'\n"
            __main__.G.rcomplist.append("Damsel_orig")
        ccommand += 'teleport_player "damsel_convo"\ntogglecamera\nfirstperson\n'
        consoleutil.console(ccommand)
        pevents.ClearDialogCombatTimers()
        __main__.ccmd.fadein=""
        __main__.ScheduleTask(2.5,"companion.HandleDamselFall(3)")

    elif 3==state:
        pevents.MobilizePlayer()
        pc = __main__.FindPlayer()
        a = pc.GetAngles()
        pc.SetAngles((0,a[1],0))
        __main__.ScheduleTask(10.0,"companion.HandleDamselFall(4)")
    elif 4==state:
        c1=__main__.FindEntityByName("companion1_damsel")
        c2=__main__.FindEntityByName("companion2_damsel")
        if c1:
            log("Unhiding comapnion 1")
            c1.ScriptUnhide()
            c1.SetName("companion1")
        if c2:
            log("Unhiding comapnion 2")
            c2.ScriptUnhide()
            c2.SetName("companion2")

# Called by damsel.dlg, line 1062. May take place in la_hub_1 or la_expipe_1
def DamselCleanup():
    __main__.G.Damsel_WasComp=1
    if "la_hub_1" == __main__.G.currentMap:
        scrap = __main__.FindEntityByName("Damsel_orig")
        if scrap:
            scrap.SetName("Damsel_scrap")
            scrap.Kill()

# Introduced to fix Long Winded Boss Bug where some bosses would
# attack after a long conversation during which your companions
# would teleport into a wall or outside the room and become useless.
#
# If beginning dialog with a "Boss", we hide any companions
# currently following us. We respawn them when the dialog ends.
#
# 5     = Johnny
# 27    = dennis
# 56    = andrei
# 62    = Gargoyle
# 73    = Bishop Vick
# 88    = jezebel_locke
# 108   = mingxiao2 (end game)
# ?101? = Bach (I dont think there are any problems with him)

g_bossList=(5,27,56,62,73,88,108)
def handleBeginDialog(dialogindex):
    global g_bossList

    if dialogindex in g_bossList:
        c1=__main__.FindEntityByName("companion1")
        c2=__main__.FindEntityByName("companion2")
        if c1 and 1 == c1.GetData("Follower"):
            log("Hiding companion 1")
            c1.ScriptHide()
            c1.SetName("companion1_boss")
        if c2 and 1 == c2.GetData("Follower"):
            log("Hiding companion 2")
            c2.ScriptHide()
            c2.SetName("companion2_boss")

def handleBossEndDialog(dialogindex):
    numHench = len(__main__.G.henchmen)
    if (not numHench == 0):
        pc=__main__.FindPlayer()
        c1=__main__.FindEntityByName("companion1_boss")
        c2=__main__.FindEntityByName("companion2_boss")
        offset = round(180 / (numHench+1))
        i=0
        if c1:
            c1.SetName("companion1") 
            if not c1.GetData("NoFight"):
                log("UnHiding companion 1")
                i=i+1
                angle=-90 + (i*offset)
                c1.SetOrigin(pc.TraceCircle(42,angle))
                c1.SetData("InFakeDeath",0)
                if pc.IsPC():
                    c1.SetData("hits",round(c1.GetData("health") * pc.GetLevel() / 120 ))
                else:
                    c1.SetData("hits",round(c1.GetData("health") * possessutil.GetPCInfoLevel() / 120 ))
                # c1.ScriptUnhide()
                # if we need to activate the maker, we will need a seperate thread since
                # this method is called from within Dialog.
                __main__.ScheduleTask(0.5,"companion.makeHenchmanHelper(__main__.FindEntityByName('companion1'),2)")
        if c2:
            c2.SetName("companion2") 
            if not c2.GetData("NoFight"):
                i=i+1
                angle=-90 + (i*offset)
                c2.SetOrigin(pc.TraceCircle(42,angle))
                log("UnHiding companion 2")
                c2.SetData("InFakeDeath",0)
                if pc.IsPC():
                    c2.SetData("hits",round(c2.GetData("health") * pc.GetLevel() / 120 ))
                else:
                    c2.SetData("hits",round(c2.GetData("health") * possessutil.GetPCInfoLevel() / 120 ))
                # c2.ScriptUnhide()
                # if we need to activate the maker, we will need a seperate thread since
                # this method is called from within Dialog.
                __main__.ScheduleTask(0.5,"companion.makeHenchmanHelper(__main__.FindEntityByName('companion2'),2)")
