import __main__
import time
import idutil
import statutil
import characterext
import dispositionutil
import consoleutil
import companion
import configutil
import fileutil
from __main__ import Character
from logutil import log

g_options=configutil.Options("mods.cfg")
g_freefall=0
# g_poseNPCName=""

############################
#  Haven Utilities 
#---------------------------
#
# 

"""


"""

###################
#  ONE TIME OPS   #
###################

def initHavenUtil():
    log("haven util : init called")
    if not __main__.G.havenutilonce:
        log("haven util : Performing One Time ops",1)
        __main__.G.havenutilonce=1
        __main__.G.CompHaven="sm_pawnshop_1"
        __main__.G.poseNPCName=""
        __main__.G.poseKeysMapped=0
        __main__.G.poseKeys={}
        __main__.G.originalKeys={}
        characterext.initCharacterExt()
        companion.initCompanion()

###################
#  Variables      #
###################

# To support these sequences, I need a seperate scripted_sequence
# embeded in the map for each animation. IE:
#
# animation_madness, animation_intrusion,animation_rubdown ...  
#
# 26 animations requires 26 embeded objects

# (sequenceName,heighAdjustment)
sequencescommon = (("mesmerized",0),("zombie",0),("worship",0), \
                   ("cower1",0),("intrusion",0),("jaded",0),("dance1",0), \
                   ("crying",0),("lost",0),("jittery",0),("dance2",0),\
                   ("lockpick",0),("madness",0),("sobbing",0),("dance3",0), \
                   ("rubdown",0),("laugh",0),("cower2",0), ("computer",0), \
                   ("sitbar",0), ("sleep",0), ("panel",0), ("layonback",-17), \
                   ("sitback",-5),("sitforward",0),("cower3",0))

sequencesmale = (("piss",0),)

sequencesfemale = (("pledge",0),)

# To support these scenes, I need a seperate logic_choreographed_scene
# PER PARTY MEMBER embedded into the map. IE:
#
# choreo1_party1, choreo1_party2, choreo1_party3 ...  
# choreo2_party1, choreo2_party2, choreo2_party3 ...  
#
# 4 scenes and 7 companions requires 28 embedded objects.
#
# In addition, each of the 28 scenes needs a support .vcd file
# (hense why there are so few of these)

#scenes = ()
scenescommon = (("lapdance3",-18,0,0,0),)

scenesmale = ()

scenesfemale = (("sitfrisky",0,0,0,0),("lapdance1",0,0,0,0),("lapdance2",0,0,0,0),)

POSENAME=0
POSEHADJUST=1

########################
# POSE INTERFACE v 1.1 #
########################
#
# In version 1.0, we did everything through dialog. This presented
# some hurdles not the least of which was that you could "LOSE" your
# companion while moving them around. Version 1.1, we use key bindings
# to allow manipulation.

# I refer to it as npc, but in reality, you could probably use this
# system to pose just about any object.

def startPoseSystem(npc):
    global g_options

    log("startPoseSystem()")

    if 0 != len(__main__.G.poseNPCName):        
        log("startPoseSystem: Invalid State",3)
        # TODO : Cancel current state if possible and restart without error

    if not npc:
        log("Invalid Pose Entity",3)
        return

    poseHelpOpt = g_options.get("comp_poseHelp",1)

    if 0 != poseHelpOpt:
        if 1 == poseHelpOpt:
            ps_help()
        elif 0 == __main__.G.has_seen_pose:
            __main__.G.has_seen_pose=1
            ps_help()

    #Remember the name of the NPC we are manipulating
    __main__.G.poseNPCName=npc.GetName()
    __main__.FindPlayer().PoseSystemActive=1

    if 0 == len(__main__.G.poseNPCName):
        __main__.G.poseNPCName="_poseNPC"
        npc.SetName(__main__.G.poseNPCName)

    if not MapPoseKeys(): return

    try:
        poseActiveMessage = g_options.get("comp_poseActiveMessage",1)
        if poseActiveMessage:
            __main__.ccmd.activateIBar=""
            __main__.FindEntityByName("pose_active_msg").Enable()
    except:
        pass

    thehouse = __main__.FindEntitiesByName("partymember*")
    for member in thehouse:
        member.WillTalk(0)
    npc.WillTalk(0)
    BeginMove(npc)

def MapPoseKeys():
    log("MapPosekeys()")
    global g_options

    if not fileutil.exists('Vampire/cfg/config.cfg'):
        log("MapPosekeys : Unable to update User Bindings. config.cfg not detected",3)
        return 0

    #Update poseKeys
    __main__.G.poseKeys['"' + g_options.get("pose_recenter",          "KP_5")          + '"'] = '"havenutil.ps_reCenter()"'
    __main__.G.poseKeys['"' + g_options.get("pose_rotateLeft",        "KP_LEFTARROW")  + '"'] = '"havenutil.ps_rotateLeft()"'
    __main__.G.poseKeys['"' + g_options.get("pose_rotateRight",       "KP_RIGHTARROW") + '"'] = '"havenutil.ps_rotateRight()"'
    __main__.G.poseKeys['"' + g_options.get("pose_raise",             "KP_UPARROW")    + '"'] = '"havenutil.ps_raise()"'
    __main__.G.poseKeys['"' + g_options.get("pose_lower",             "KP_DOWNARROW")  + '"'] = '"havenutil.ps_lower()"'
    __main__.G.poseKeys['"' + g_options.get("pose_leanBackward",      "KP_PGUP")       + '"'] = '"havenutil.ps_leanBackward()"'
    __main__.G.poseKeys['"' + g_options.get("pose_leanForward",       "KP_PGDN")       + '"'] = '"havenutil.ps_leanForward()"'
    __main__.G.poseKeys['"' + g_options.get("pose_nextPose",          "KP_PLUS")       + '"'] = '"havenutil.ps_nextPose()"'
    __main__.G.poseKeys['"' + g_options.get("pose_previousPose",      "KP_MINUS")      + '"'] = '"havenutil.ps_previousPose()"'
    __main__.G.poseKeys['"' + g_options.get("pose_nextFace",          "KP_SLASH")      + '"'] = '"havenutil.ps_nextFace()"'
    __main__.G.poseKeys['"' + g_options.get("pose_previousFace",      "*")             + '"'] = '"havenutil.ps_previousFace()"'
    __main__.G.poseKeys['"' + g_options.get("pose_finished1",         "ENTER")         + '"'] = '"havenutil.endPoseSystem()"'
    __main__.G.poseKeys['"' + g_options.get("pose_finished2",         "KP_ENTER")      + '"'] = '"havenutil.endPoseSystem()"'
    __main__.G.poseKeys['"' + g_options.get("pose_help",              "KP_INS")        + '"'] = '"havenutil.ps_help()"'
    __main__.G.poseKeys['"' + g_options.get("pose_moveLeft",          "LEFTARROW")     + '"'] = '"havenutil.ps_moveLeft()"'
    __main__.G.poseKeys['"' + g_options.get("pose_moveRight",         "RIGHTARROW")    + '"'] = '"havenutil.ps_moveRight()"'
    __main__.G.poseKeys['"' + g_options.get("pose_moveIn",            "DOWNARROW")     + '"'] = '"havenutil.ps_moveIn()"'
    __main__.G.poseKeys['"' + g_options.get("pose_moveOut",           "UPARROW")       + '"'] = '"havenutil.ps_moveOut()"'

    data = 'firstperson\n'
    tempKeys = __main__.G.poseKeys.keys()
    for key in tempKeys:
        data = '%sbind %s %s\n' % (data,key,__main__.G.poseKeys[key])

    lines = fileutil.readlines('Vampire/cfg/config.cfg')

    # Scan for existing Key bindings and store in originalKeys
    for line in lines:
        for key in tempKeys:
            slice = line.find(key)
            if -1 != slice: 
                __main__.G.originalKeys[key] = line[slice + len(key):].strip()
                tempKeys.remove(key)
                break

    consoleutil.console(data)
    __main__.G.poseKeysMapped=1
    return 1
    
def UnmapPoseKeys():
    
    tempKeys = __main__.G.poseKeys.keys()
    otempKeys = __main__.G.originalKeys.keys()
    data = ''

    for key in otempKeys:
        data = '%sbind %s %s\n' % (data,key,__main__.G.originalKeys[key])
        if key in tempKeys: tempKeys.remove(key)

    for key in tempKeys:
        data = '%sunbind %s\n' % (data,key)

    __main__.G.poseKeys.clear()
    __main__.G.originalKeys.clear()
    consoleutil.console(data)
    __main__.G.poseKeysMapped=0

def endPoseSystem():
    global g_options
    
    log("endPoseSystem()")
    if 0 == checkPoseActive(): return    
    npc = __main__.FindEntityByName(__main__.G.poseNPCName)
    if npc:
        if (npc.GetName() == "_poseNPC"):
            npc.SetName("")
        __main__.G.poseNPCName=""
        EndMove(npc)
        npc.WillTalk(1)
        
    thehouse = __main__.FindEntitiesByName("partymember*")
    for member in thehouse:
        member.WillTalk(1)
    UnmapPoseKeys()
    __main__.ccmd.fixcamera=""
    try:
        __main__.FindEntityByName("pose_active_msg").Disable()
    except:
        pass    
    
##############################
# POSE SYSTEM HELPER METHODS #
##############################

def ps_nextPose():
    global g_options
    log("ps_nextPose()")
    if 0 == checkPoseActive(): return    
    npc = __main__.FindEntityByName(__main__.G.poseNPCName)
    # Patch 1.3 : All willing companions refuse
    if npc.GetData("Type")==4 and not g_options.get("comp_poseWilling",0):
        consoleutil.console("say '%s refuses.'" % npc.GetData("OName"))
        return
    if npc:
        EndMove(npc)
        npc.NextPose()
        BeginMove(npc)

def ps_previousPose():
    global g_options
    log("ps_previousPose()")
    if 0 == checkPoseActive(): return    
    npc = __main__.FindEntityByName(__main__.G.poseNPCName)
    # Patch 1.3 : All willing companions refuse
    if npc.GetData("Type")==4 and not g_options.get("comp_poseWilling",0):
        consoleutil.console("say '%s refuses.'" % npc.GetData("OName"))
        return
    if npc:
        EndMove(npc)
        npc.PrevPose()
        BeginMove(npc)

def ps_nextFace():
    log("ps_nextFace()")
    if 0 == checkPoseActive(): return    
    npc = __main__.FindEntityByName(__main__.G.poseNPCName)
    # Patch 1.3 : All willing companions refuse
    if npc.GetData("Type")==4 and not g_options.get("comp_poseWilling",0):
        consoleutil.console("say '%s refuses.'" % npc.GetData("OName"))
        return
    if npc:
        npc.NextExpression()

def ps_previousFace():
    log("ps_previousFace()")
    if 0 == checkPoseActive(): return    
    npc = __main__.FindEntityByName(__main__.G.poseNPCName)
    # Patch 1.3 : All willing companions refuse
    if npc.GetData("Type")==4 and not g_options.get("comp_poseWilling",0):
        consoleutil.console("say '%s refuses.'" % npc.GetData("OName"))
        return
    if npc:
        npc.PrevExpression()    

def ps_raise():
    log("ps_raise()")
    if 0 == checkPoseActive(): return    
    npc = __main__.FindEntityByName(__main__.G.poseNPCName)
    if npc:
        EndMove(npc)
        npc.Raise()
        BeginMove(npc)

def ps_lower():
    log("ps_lower()")
    if 0 == checkPoseActive(): return    
    npc = __main__.FindEntityByName(__main__.G.poseNPCName)
    if npc:
        EndMove(npc)
        npc.Lower()
        BeginMove(npc)

def ps_leanForward():
    log("ps_leanForward()")
    if 0 == checkPoseActive(): return    
    npc = __main__.FindEntityByName(__main__.G.poseNPCName)
    # Patch 1.3 : All willing companions refuse
    if npc.GetData("Type")==4 and not g_options.get("comp_poseWilling",0):
        consoleutil.console("say '%s refuses.'" % npc.GetData("OName"))
        return
    if npc:
        EndMove(npc)
        npc.LeanForward()
        BeginMove(npc)

def ps_leanBackward():
    log("ps_leanBackward()")
    if 0 == checkPoseActive(): return
    npc = __main__.FindEntityByName(__main__.G.poseNPCName)
    # Patch 1.3 : All willing companions refuse
    if npc.GetData("Type")==4 and not g_options.get("comp_poseWilling",0):
        consoleutil.console("say '%s refuses.'" % npc.GetData("OName"))
        return
    if npc:
        EndMove(npc)
        npc.LeanBackward()
        BeginMove(npc)

def ps_moveLeft():
    log("ps_moveLeft()")
    if 0 == checkPoseActive(): return    
    npc = __main__.FindEntityByName(__main__.G.poseNPCName)
    if npc:
        pc=__main__.FindPlayer()
        pc.npc_angle=pc.npc_angle + 5
        EndMove(npc)
        BeginMove(npc)

def ps_moveRight():
    log("ps_moveRight()")
    if 0 == checkPoseActive(): return    
    npc = __main__.FindEntityByName(__main__.G.poseNPCName)
    if npc:
        pc=__main__.FindPlayer()
        pc.npc_angle=pc.npc_angle - 5
        EndMove(npc)
        BeginMove(npc)

def ps_moveIn():
    log("ps_moveIn()")
    if 0 == checkPoseActive(): return    
    npc = __main__.FindEntityByName(__main__.G.poseNPCName)
    if npc:
        pc=__main__.FindPlayer()
        pc.npc_distance=pc.npc_distance - 5
        EndMove(npc)
        BeginMove(npc)
    

def ps_moveOut():
    log("ps_moveOut()")
    if 0 == checkPoseActive(): return    
    npc = __main__.FindEntityByName(__main__.G.poseNPCName)
    if npc:
        pc=__main__.FindPlayer()
        pc.npc_distance=pc.npc_distance + 5
        EndMove(npc)
        BeginMove(npc)

def ps_reCenter():
    log("ps_reCenter()")
    if 0 == checkPoseActive(): return    
    npc = __main__.FindEntityByName(__main__.G.poseNPCName)
    if npc:
        pc=__main__.FindPlayer()
        pc.npc_distance=100
        pc.npc_angle=0
        # facing=(abs(((pc.GetAngles()[1]+180)/360)-0.5)*360)-180
        facing=pc.GetAngles()[1]-180
        pose_origin = npc.GetData("PoseOrigin")
        npc.SetData("PoseZ",pose_origin[2])
        EndMove(npc)
        npc.SetAngles((0,facing,0))
        BeginMove(npc)

def ps_rotateLeft():
    log("ps_rotateLeft()")
    if 0 == checkPoseActive(): return    
    npc = __main__.FindEntityByName(__main__.G.poseNPCName)
    if npc:
        EndMove(npc)
        angles = npc.GetAngles()
        npc.SetAngles((angles[0],angles[1]-10,angles[2]))
        BeginMove(npc)

def ps_rotateRight():
    log("ps_rotateRight()")
    if 0 == checkPoseActive(): return    
    npc = __main__.FindEntityByName(__main__.G.poseNPCName)
    if npc:
        EndMove(npc)
        angles = npc.GetAngles()
        npc.SetAngles((angles[0],angles[1]+10,angles[2]))
        BeginMove(npc)

def ps_help():
    log("ps_help()")
    sign = __main__.FindEntityByName("pose_popup")
    if sign:
        sign.OpenWindow()
    else:
        consoleutil.console("say 'Use Numpad and Arrow Keys to manipulate companion. Press ENTER when finished.'")
        

#########################
# DIALOG HELPER METHODS #
#########################
# There are potential issues when spawning or altering npcs
# while the dialog engine is running. So for a majority of
# dialog options, we have support methods that simply set a
# global flag and then we handle what was said in the
# OnDialogEnd handler. 

d_nextPose=0
def NextPose():
    log("NextPose")
    global d_nextPose
    d_nextPose=1

d_prevPose=0
def PrevPose():
    log("PrevPose")
    global d_prevPose
    d_prevPose=1

d_pausePose=0
def PausePose():
    log("PausePose")
    global d_pausePose
    d_pausePose=1

d_stopPose=0
def StopPose():
    log("StopPose")
    global d_stopPose
    d_stopPose=1

d_resumePose=0
def ResumePose():
    log("ResumePose")
    global d_resumePose
    d_resumePose=1

d_startPose=0
def StartPose():
    log("StartPose")
    global d_startPose
    d_startPose=1

d_resetParty=0
def ResetParty():
    log("ResetParty")
    global d_resetParty
    d_resetParty=1

def isInHaven():
    log("IsInHaven")
    inhaven = __main__.FindEntityByName("haven_companion_maker")
    if inhaven : return 1
    return 0

# isMoving tracked by NPC instance

##############################
# partymember Event Handlers #
##############################
# npc_maker objects (which I) embeded onto every map are setup to call these event handlers


def partymember_OnSpawnNPC():
    log("partymember_OnSpawnNPC")

def partymember_OnDialogBegin():
    log("partymember_OnDialogBegin")

def partymember_OnDeath():
    log("partymember_OnDeath")
    existslist=[]
    for member in __main__.G.complist:
        existslist.append(member)

    for henchman in __main__.G.henchmen:
        if henchman in existslist:
            del existslist[existslist.index(henchman)]

    thehouse = __main__.FindEntitiesByName("partymember*")
    for member in thehouse:
        id = member.GetID()
        if id in existslist:
            del existslist[existslist.index(id)]

    if len(existslist) == 0:
        log("All npcs accounted for. Unable to find deceased PartyMember",2)
        return

    for npcKey in existslist:
        if npcKey in __main__.G.complist:
            log("NPC [%s] unaccounted for. Killed NPC discovered" % npcKey)
            # TODO : should encapsualte alteration of data structure to companion
            #        method
            del __main__.G.complist[__main__.G.complist.index(npcKey)]
        else:
            log("NPC [%s] not in compList" % npcKey)          

        

# d_talking : Original name of the npc that the pc is talking to. 
d_talking=""

def OnDialogStart(npc):
    global d_talking

    log("OnDialogStart")
    npc.StandUpStrait()

    d_talking=npc.GetName()

    # Special Case : If the pose is a choreographed scene and you 
    # change the name of the PC, the scene will break. 2 solutions
    #
    # 1 (hard) - Stop the choreographed scene before starting the
    #            the conversation. This involves not only stopping
    #            the scene, but respawning the NPC and getting the
    #            newly spawned NPC to begin talking to the PC. 
    #
    # 2 (easy) - if the current scene is a choreopaphed scene, dont
    #            change the name and rediect to a generic response. 
    #            the redirection is done by having this function 
    #            return true. 

    if npc.IsPoseChoreo(): return 1

    # data=npc.GetPoseData()
    # numsequences=data[0]
    # numscenes=data[1]
    # numdispositions=data[2]
    # poses=data[3]
    # l = len(poses)
    # ss_sum = numsequences + numscenes
    # try:
    #  poseindex=npc.GetData("PoseIndex")
    #  if poseindex > (numsequences) and poseindex < (ss_sum+1):
    #except:
    #  pass

    npc.SetName("talking_pm")
    return 0

def partymember_OnDialogEnd():
    global d_talking
    # global d_nextPose
    # global d_prevPose
    global d_stopPose
    global d_startPose
    # global d_resumePose
    # global d_pausePose
    # global d_startMove
    # global d_stopMove
    global d_resetParty
    global d_npcheight

    
    log("partymember_OnDialogEnd")
    npc=__main__.FindEntityByName("talking_pm")
    if npc:
        npc.SetName(d_talking)
    else:
        npc=__main__.FindEntityByName(d_talking)
        
    if d_stopPose:
        d_stopPose=0
        npc.StopPose()
    elif d_startPose:
        d_startPose=0
        startPoseSystem(npc)
    elif companion.d_replaceHenchman:
        npc.SetName("new_companion")
        companion.new_companion_OnDialogEnd()
    elif companion.d_makeHenchman:
        npc.SetName("new_companion")
        companion.new_companion_OnDialogEnd()        
    elif companion.d_removeFromParty:
        log("haventutil - partymember_OnDialogEnd : d_removeFromParty called")
        npc=__main__.FindEntityByName(d_talking)
        npc.SetName("new_companion")
        companion.new_companion_OnDialogEnd()        
    elif d_resetParty:
        d_resetParty=0
        ResetHaven()
    else:
        if npc.IsPoseRunning():
            log("Resuming Pose")
            npc.ResumePose()

##########################
# CHARACTER POSE METHODS #
##########################

POSESTOPPED=1
POSERUNNING=2
POSEPAUSED=3

def _GetSequences(self):
    """ Returns list of animation sequences that are valid for the given model within the haven"""

    log("_GetSequences()")
    global sequencescommon
    global sequencesmale
    global sequencesfemale
    
    result=[]
    if not self.classname: return result
    if not self.classname.startswith("npc_V"): return result
    result.extend(sequencescommon)
    if self.IsMale():
        result.extend(sequencesmale)
    else:
        result.extend(sequencesfemale)
    return result

def _GetScenes(self):
    """ Returns list of choreographed scenes that are valid for the given model within the haven"""

    log("_GetScenes()")
    global scenescommon
    global scenesmale
    global scenesfemale
    
    result=[]
    if not self.classname: return result
    if not self.classname.startswith("npc_V"): return result
    result.extend(scenescommon)
    if self.IsMale():
        result.extend(scenesmale)
    else:
        result.extend(scenesfemale)
    return result

def _GetPoseData(self):
    """ Returns list of poses that are valid for the given model"""

    log("_GetPoseData")
    sequences=self.GetSequences()
    scenes=self.GetScenes()
    dispositions=self.GetDispositions()
    poses=[]
    poses.insert(0,dispositions[0])
    del dispositions[0]
    poses.extend(sequences)
    poses.extend(scenes)
    poses.extend(dispositions)
    l = len(poses)
    ss_sum = len(sequences) + len(scenes)
    result=[]
    result.extend((len(sequences),len(scenes),len(dispositions)))
    result.insert(3,poses)
    return result

def _SetPoseByIndex(self,index=0,announce=1):

    log("_SetPoseByIndex()")

    oname=self.GetName()
    l = self.PausePose()
    self=__main__.FindEntityByName(oname)
    
    # Update Index

    self.poseindex=index % l
    self.SetData("PoseIndex",self.poseindex)

    # Start the new animation
    posename=self.ResumePose()
    
    if announce:
        data="say \"Pose [%s]\"\n" % posename
        consoleutil.console(data)

def _NextPose(self):
    """ Allows iteration through poses """

    log("_NextPose()")

    self.RestorePose()
    index = self.poseindex
    index+=1
    self.StandUpStrait()
    return self.SetPoseByIndex(index)

def _PrevPose(self):
    """ Allows iteration through poses """

    log("_PrevPose()")

    self.RestorePose()
    index = self.poseindex
    index-=1
    self.StandUpStrait()
    return self.SetPoseByIndex(index)

def _RestorePose(self,display=0):
    """ Looks up last pose from save game and restores """

    log("calling restore pose")
    pindex=self.GetData("PoseIndex")
    if None == pindex:
        self.SetData("PoseIndex",0)
        self.poseindex=0
    else:
        self.poseindex=pindex

    pstate=self.GetData("PoseState")
    if None == pstate:
        self.SetData("PoseState",POSESTOPPED)
        self.posestate=POSESTOPPED
    else:
        self.posestate=pstate

    if display:
        self.SetPoseByIndex(self.poseindex,0)

# _PausePose
#
# Pause stops the animaiton
#
# note : Pause Pose may respawn the npc. Always
#        re-initialize your instance handle after invoking.
#        ie: reinit=__main__.FindEntityByName("Old_NPC_Name")

def _PausePose(self):
    global POSENAME

    log("_PausePose()")
    self.posestate=POSEPAUSED
    self.SetData("PoseState",POSEPAUSED)
    data=self.GetPoseData()
    numsequences=data[0]
    numscenes=data[1]
    numdispositions=data[2]
    poses=data[3]
    l = len(poses)
    ss_sum = numsequences + numscenes
    try: self.poseindex=self.poseindex
    except: self.poseindex=0
    oname=self.GetName()
    tuple = poses[self.poseindex]
    
    # Try to stop current animation
    if 0 == self.poseindex:
        self.SetDispositionByIndex(0)
    elif self.poseindex < (numsequences+1):
        safeorigin = __main__.FindEntityByName("haven_companion_maker").GetOrigin()
        # It is a sequence
        # Find sequence
        self.SetName("partymember")
        seq = __main__.FindEntityByName("animation_%s" % poses[self.poseindex][POSENAME])
        # Call CancelSequence()
        seq.SetOrigin(self.GetOrigin())
        seq.CancelSequence()
        self.SetName(oname)
        seq.SetOrigin(safeorigin)
    elif self.poseindex < (ss_sum+1):
        # It is a choreographed_scene
        # Special : In order to get an NPC to return to "normal" after having been
        # part of a scene, you must Kill and respawn them. 
        # Find scene
        scene = __main__.FindEntityByName("%s_%s" % (poses[self.poseindex][POSENAME],self.GetName()))        
        # Call Cancel()
        scene.SetOrigin(self.GetOrigin())
        scene.Cancel()
        o = self.GetData("PoseOrigin")
        zadjusted=self.GetData("PoseZ")
        if not o[2] == zadjusted:
            self.SetOrigin(o)
            log("fixing origin [%d,%d,%d]" % (o[0],o[1],o[2]))
        Respawn(oname)
        return l
    else:
        self.SetDispositionByIndex(0)

    # Fix height:
    o = self.GetData("PoseOrigin")
    zadjusted=self.GetData("PoseZ")
    if not o[2] == zadjusted:
        self.SetOrigin(o)
        log("fixing origin [%d,%d,%d]" % (o[0],o[1],o[2]))
    return l


#def _PausePose(self,stopanimation=1):
#    global POSEPAUSED
#    global POSENAME
#
#    log("_PausePose()")
#
#    self.posestate=POSEPAUSED
#
#    data=self.GetPoseData()
#    numsequences=data[0]
#    numscenes=data[1]
#    numdispositions=data[2]
#    poses=data[3]
#    l = len(poses)
#    ss_sum = numsequences + numscenes
#    
#    try:
#        self.poseindex=self.poseindex
#    except:
#        self.poseindex=0
#
#    oname=self.GetName()
#
#    tuple = poses[self.poseindex]
#    
#    # Try to stop current animation
#
#    if 0 == self.poseindex:
#        self.SetDispositionByIndex(0)
#        # Fix height:
#        o = self.GetData("PoseOrigin")
#        zadjusted=self.GetData("PoseZ")
#        if not o[2] == zadjusted:
#            self.SetOrigin(o)
#            log("fixing origin [%d,%d,%d]" % (o[0],o[1],o[2]))
#    elif self.poseindex < (numsequences+1):
#        safeorigin = __main__.FindEntityByName("haven_companion_maker").GetOrigin()
#        # It is a sequence
#        # Find sequence
#        self.SetName("partymember")
#        seq = __main__.FindEntityByName("animation_%s" % poses[self.poseindex][POSENAME])
#        # Call CancelSequence()
#        seq.SetOrigin(self.GetOrigin())
#        seq.CancelSequence()
#        self.SetName(oname)
#        seq.SetOrigin(safeorigin)
#        # Fix height:
#        o = self.GetData("PoseOrigin")
#        zadjusted=self.GetData("PoseZ")
#        if not o[2] == zadjusted:
#            self.SetOrigin(o)
#            log("fixing origin [%d,%d,%d]" % (o[0],o[1],o[2]))
#    elif self.poseindex < (ss_sum+1):
#        # It is a choreographed_scene
#        # Special : In order to get an NPC to return to "normal" after having been
#        # part of a scene, you must Kill and respawn them. 
#        # Find scene
#        scene = __main__.FindEntityByName("%s_%s" % (poses[self.poseindex][POSENAME],self.GetName()))        
#        # Call Cancel()
#        scene.SetOrigin(self.GetOrigin())
#        scene.Cancel()
#        o = self.GetData("PoseOrigin")
#        zadjusted=self.GetData("PoseZ")
#        if not o[2] == zadjusted:
#            self.SetOrigin(o)
#            log("fixing origin [%d,%d,%d]" % (o[0],o[1],o[2]))
#        Respawn(oname)
#    else:
#        self.SetDispositionByIndex(0)
#        # Fix height:
#        o = self.GetData("PoseOrigin")
#        zadjusted=self.GetData("PoseZ")
#        if not o[2] == zadjusted:
#            self.SetOrigin(o)
#            log("fixing origin [%d,%d,%d]" % (o[0],o[1],o[2]))
#    return l

# _ResumePose:
# While PausePose and ResumePose share a lot of the functionality of SetPoseByIndex,
# the code is replicated because some animations require location\height adjustments
# We needed to ensure that only the SetPoseByIndex method made angle\height adjustments. 
# note : Pause Pose may respawn npc. Always re-initialize your instance handle after
#        invoking. ie: reinit=__main__.FindEntityByName("Old_NPC_Name")
def _ResumePose(self):
    global POSENAME
    global POSEHADJUST

    self.posestate=POSERUNNING
    self.SetData("PoseState",POSERUNNING)
    
    log("_ResumePose()")

    data=self.GetPoseData()
    numsequences=data[0]
    numscenes=data[1]
    numdispositions=data[2]
    poses=data[3]
    l = len(poses)
    ss_sum = numsequences + numscenes
    
    try:
        self.poseindex=self.poseindex
    except:
        self.poseindex=0

    oname=self.GetName()
    tuple = poses[self.poseindex]
    posename="Error"
    
    if 0 == self.poseindex:
        # Special Case : No Pose
        self.SetDispositionByIndex(0)
        dname=tuple[dispositionutil.NAME]
        dlevel=tuple[dispositionutil.LEVEL]
        posename="%s version %d" % (dname,dlevel)
    elif self.poseindex < (numsequences+1):
        safeorigin = __main__.FindEntityByName("haven_companion_maker").GetOrigin()
        # It is a sequence
        # Find sequence
        self.SetName("partymember")
        sname=tuple[POSENAME]
        seq = __main__.FindEntityByName("animation_%s" % sname)
        seq.SetOrigin(self.GetOrigin())
        # Call BeginSequence()
        seq.BeginSequence()
        self.SetName(oname)
        seq.SetOrigin(safeorigin)
        posename="%s" % sname        
    elif self.poseindex < (ss_sum+1):
        # It is a choreographed_scene
        # Find scene
        sname=tuple[POSENAME]
        scene = __main__.FindEntityByName("%s_%s" % (sname,self.GetName()))
        scene.SetOrigin(self.GetOrigin())
        # Call Start()
        scene.Start()
        posename="%s" % sname
    else:
        # It is a disposition
        dnum = self.poseindex - ss_sum
        self.SetDispositionByIndex(dnum)
        dname=tuple[dispositionutil.NAME]
        dlevel=tuple[dispositionutil.LEVEL]
        posename="%s version %d" % (dname,dlevel)

    hadjust=tuple[POSEHADJUST]
    o = self.GetData("PoseOrigin")
    zadjusted=o[2]+hadjust
    self.SetData("PoseZ",zadjusted)
    if not o[2] == zadjusted:
        self.SetOrigin((o[0],o[1],zadjusted))
        log("Pose Height non-zero. Adjusting: [%d,%d,%d]" % (o[0],o[1],zadjusted))

    return posename


def _StopPose(self):

    log("_StopPose()")

    self.PausePose()
    self.posestate=POSESTOPPED
    self.SetData("PoseState",POSESTOPPED)
    self.poseindex=0
    self.SetData("PoseIndex",self.poseindex)

# Checks for the condition that a user began the pose without finishing it.
# Issue is that we need to resolve when the PC is in the haven. So even if
# there is a problem detected, if we are not in the haven, we can't fix it
# Assumption is that this is only called when npc.poseSystemActive SHOULD be
# true. This is called by all the pose system functions and the person may or
# may not be in the haven. If it returns true, there is an error and the
# caller function is aborted. 

def checkPoseActive():
    if __main__.G.currentMap != __main__.G.CompHaven or 0 == len(__main__.G.poseNPCName):
        log("Pose System not active. Ignoring Request",2)
        return 0
    try:
        if __main__.FindPlayer().PoseSystemActive: return 1
    except:
        pass
    log("Pose System not syncrhonized (Did player save while posing?). Attempting to fix",2)
    if __main__.G.poseKeysMapped: UnmapPoseKeys()
    thehouse = __main__.FindEntitiesByName("partymember*")
    for member in thehouse: member.WillTalk(1)
    npc = __main__.FindEntityByName(__main__.G.poseNPCName)
    if npc:
        npc.Kill()
        __main__.G.poseNPCName=""
        try:
            __main__.FindEntityByName("pose_active_msg").Disable()
        except:
            pass
        PopulateHaven()

#def _CheckPose(self):
#    log("_Check Pose executing")
#    if self.IsPosePaused():
#        log("Resuming Pose")
#        self.ResumePose()

#def _CheckPose(self):
#    log("_Check Pose executing")
#    if self.IsPoseRunning():
#        log("Resuming Pose")
#        self.ResumePose()

#def _IsPoseStopped(self):
#    global POSESTOPPED
#
#    log("_IsPoseStopped()")
#
#    ret = 1
#    try:
#        if not (self.posestate == POSESTOPPED):
#           ret = 0
#    except:
#        self.posestate = POSESTOPPED
#    return ret

#def _IsPosePaused(self):
#    global POSEPAUSED
#    global POSESTOPPED
#
#    log("IsPosePaused()")
#
#    ret = 0
#    try:
#        if self.posestate == POSEPAUSED:
#           ret = 1
#    except:
#        self.posestate = POSESTOPPED
#    return ret

def _IsPoseRunning(self):

    log("_IsPoseRunning()")

    # Restore Pose ensures self.poseindex is defined
    self.RestorePose()

    # Pose index of 0 trumps the state flags
    if 0 == self.poseindex:
        log("poseindex is 0. Resetting posestate to POSESTOPPED")
        self.posestate = POSESTOPPED
        return 0
    
    if self.posestate == POSERUNNING:
        return 1
    return 0

def _IsPoseChoreo(self):

    log("_IsPoseChoreo()")

    if not self.IsPoseRunning(): return 0

    sequences=self.GetSequences()
    scenes=self.GetScenes()
    if self.poseindex > len(sequences) and self.poseindex < (len(sequences) + len(scenes) + 1):
        return 1

    return 0    

#####################
# Update Base Class #
#####################

Character.GetPoseData=_GetPoseData
Character.GetScenes=_GetScenes
Character.GetSequences=_GetSequences
Character.SetPoseByIndex=_SetPoseByIndex
Character.NextPose=_NextPose
Character.PrevPose=_PrevPose
Character.RestorePose=_RestorePose
Character.StopPose=_StopPose
Character.PausePose=_PausePose
#Character.CheckPose=_CheckPose
Character.ResumePose=_ResumePose
#Character.IsPoseStopped=_IsPoseStopped
#Character.IsPosePaused=_IsPosePaused
Character.IsPoseRunning=_IsPoseRunning
Character.IsPoseChoreo=_IsPoseChoreo

####################
# Movement Methods #
####################

# Notes:
#     SetParent is a pretty cool function for moving objects around. However, it has 1
#     problem. Once you set a parent for an object, GetOrigin and GetCenter begin returning
#     invalid values for that object. When you clear the parent, the object returns to its
#     "origin" which is not being reported correctly and the object normally "disappears".
#
#     To circumvent this issue, we maintain our own origin value and update it
#     when EndMove is called. "PoseOrigin" is used for this. It is created with each
#     henchment when they are spawned and when you move the henchman around it is
#     in fact this value that is updated.
#
#     NOTES: Poses maintain their own offsets which are applied to the PoseOrigin when you
#     cycle through the poses. This is because some posses are the result of one actors
#     movements in a much larger choreographed scene. The origin of this scene may have to
#     be shiften to a different room or even floor of your haven to make the NPC appear
#     in front of you.

#     We store off the facing and origin of both parties and then perform transformation
#     math when the movement is over to fix the new location. Luckly, facing information
#     is not lost, therefore we do not need to correct the NPCs facing. 

def BeginMove(npc):
    from math import sqrt as _sqrt
    from math import atan2 as _atan2
    from math import pi as _pi
    npc.beingmoved=1
    pc=__main__.FindPlayer()

    log("_BeginMove() npc.name = %s" % npc.GetName())

    # Step 1 : Transform PoseOrigin's old coordinates. Shift so that PC would have been at origin:
    pose_origin = npc.GetData("PoseOrigin")
    tx = (pose_origin[0] - pc.GetOrigin()[0])
    ty = (pose_origin[1] - pc.GetOrigin()[1])

    # Step 2 : Calculate angle of NPC relative to new origin
    # NOTE : The atan2 function is the only slope to radians function that
    #        understands the various quadrants. ta will be in the range
    #        180 to -180

    # RadToDeg : (360/2pi)r = d

    relative_angle = (360/(2*_pi))*(_atan2(ty,tx))

    pc_angles=pc.GetAngles()

    log("havenutil:_BeginMove - PC Origin  (%d,%d,%d)" % (pc.GetOrigin()[0],pc.GetOrigin()[1],pc.GetOrigin()[2]))
    log("havenutil:_BeginMove - PC Angles  (%d,%d,%d)" % (pc_angles[0],pc_angles[1],pc_angles[2]))
    log("havenutil:_BeginMove - NPC Origin (%d,%d,%d)" % (npc.GetOrigin()[0],npc.GetOrigin()[1],npc.GetOrigin()[2]))
    log("havenutil:_BeginMove - NPC Angles (%d,%d,%d)" % (npc.GetAngles()[0],npc.GetAngles()[1],npc.GetAngles()[2]))
    log("havenutil:_BeginMove - Pose Origin (%d,%d,%d)" % (pose_origin[0],pose_origin[1],pose_origin[2]))

    # Step 3 : Calculate the angular DIFFERENCE between the relative angle and the PC facing
    #          This is trivial since we made the PC the origin. 
    angle_diff = relative_angle - pc_angles[1] 
    log("havenutil:_BeginMove - PC Facing (%d) Relative Angle (%d) Difference (%d)" % (pc_angles[1],relative_angle,angle_diff))

    # Step 4 : Calculate the DISTANCE between the PoseOrigin and the PC (assume same plane)
    npc_dist = _sqrt((tx*tx) + (ty*ty))
    log("havenutil:_BeginMove - Distance (%d)" % npc_dist)

    pc.npc_distance = npc_dist
    pc.npc_angle = angle_diff

    # Step 5 : Sanity check : Move NPC to location
    zadjusted=npc.GetData("PoseZ")
    (x,y,z)=pc.TraceCircle(npc_dist,angle_diff)
    # na = npc_angles
    origin=(x,y,zadjusted)
    npc.SetOrigin(origin)
    npc.SetParent("!player")
    return 1

def EndMove(npc):

    log("EndMove() npc.name = %s" % npc.GetName())

    npc.beingmoved=0
    pose_origin = npc.GetData("PoseOrigin")
    pc=__main__.FindPlayer()
    angle_diff = pc.npc_angle
    npc_dist = pc.npc_distance
    
    # When you cycle through the posses, they maintain the offsets needed to make the NPC appear
    # infront of the PC. Sometimes these offsets include changes to the Z axis. We maintain
    # elevation changes with a seperate data item "PoseZ". It is not an offset, but rather the
    # adjusted value that Z should be.

    zadjusted=npc.GetData("PoseZ")
    zdiff= zadjusted - pose_origin[2]

    (x,y,z)=pc.TraceCircle(npc_dist,angle_diff)
    # na = npc_angles
    origin=(x,y,z+zdiff)
    log("havenutil : EndMove - Adjusting location (%d,%d,%d)" % (origin[0],origin[1],origin[2]))
    npc.SetData("PoseOrigin",(x,y,z))
    npc.SetData("PoseZ",z+zdiff)
    npc.ClearParent()
    npc.SetOrigin(origin)
    # self.SetAngles(facing)

def _LeanForward(self):
    angles=self.GetAngles()
    newangles=(angles[0]+15,angles[1],angles[2])
    log("New Angle [%d]" % newangles[0])
    self.SetAngles(newangles)

def _LeanBackward(self):
    angles=self.GetAngles()
    newangles=(angles[0]-15,angles[1],angles[2])
    log("New Angle [%d]" % newangles[0])
    self.SetAngles(newangles)

def _Raise(self):
    zadjusted = self.GetData("PoseZ") + 3
    self.SetData("PoseZ",zadjusted)
    o = self.GetData("PoseOrigin")
    self.SetOrigin((o[0],o[1],zadjusted))

def _Lower(self):
    zadjusted = self.GetData("PoseZ") - 1
    self.SetData("PoseZ",zadjusted)
    o = self.GetData("PoseOrigin")
    self.SetOrigin((o[0],o[1],zadjusted))

def _StandUpStrait(self):
    angles=self.GetAngles()
    newangles=(0,angles[1],angles[2])
    self.SetAngles(newangles)

def _IsBeingMoved(self):
    ret = 0
    try:
        ret = self.beingmoved
    except:
        self.beingmoved=0
    return ret

#####################
# Update Base Class #
#####################

Character.IsBeingMoved=_IsBeingMoved
Character.LeanForward=_LeanForward
Character.LeanBackward=_LeanBackward
Character.Raise=_Raise
Character.Lower=_Lower
Character.StandUpStrait=_StandUpStrait
    
########
# main #
########

def Feed(npc):
    npc.SetData("RespawnTimer",round(time.time()) + 600)
    __main__.FindPlayer().SeductiveFeed( npc )
    
def Respawn(name):
    log("Respawn(%s)" % name)
    
    npc=__main__.FindEntityByName(name)
    oname=npc.GetName()
    origin=npc.GetOrigin()
    npc.SetName(oname+"_scrap")    
    maker = __main__.FindEntityByName("haven_companion_maker")
    maker.Spawn()
    c = __main__.FindEntityByName("new_partymember")
    if c:
        c.SetName(oname)
        c.SetAngles(npc.GetAngles())
        c.SetModel(npc.GetModelName())
        c.LookAtEntityEye("!player")
        c.AllowAlertLookaround(0)
        # there is probably an easier dynamic way to copy attributes
        try:
            c.poseindex = npc.poseindex
        except:
            pass
        try:
            c.posestate = npc.posestate
        except:
            pass
        try:
            c.distancefromPC = npc.distancefromPC
        except:
            pass
        try:
            c.zdiff = npc.zdiff
        except:
            pass
        try:
            c.anglediff = npc.anglediff
        except:
            pass
        try:
            c.beingmoved = npc.beingmoved
        except:
            pass
        npc.Kill()
        c.SetOrigin(origin)
        c.RestoreExpression(1)
    else:
        log("companion mod : havenutil : Respawn - Error creating companion. (possibly exceeded maximum?)",3)
        name=npc.GetName()
        slice = name.rindex("_")
        npc.SetName(name[0:slice])        

def PopulateHaven():
    log("havenutil.PopulateHaven() called")
    createlist = []
    existslist=[]
    for member in __main__.G.complist:
        createlist.append(member)
        
    for henchman in __main__.G.henchmen:
        if henchman in createlist:
            del createlist[createlist.index(henchman)]

    # A little somthing extra when possessing someone
    pc=__main__.FindPlayer()
    if not pc.IsPC():
        key = pc.GetID()
        if key in createlist:
            del createlist[createlist.index(key)]

    thehouse = __main__.FindEntitiesByName("partymember*")
    currenttime = time.time()
    for member in thehouse:
        id = member.GetID()
        if id in createlist:
            del createlist[createlist.index(id)]
            existslist.append(member.GetName())
            respawntimer = member.GetData("RespawnTimer")
            if not (respawntimer == 0) and (currenttime > respawntimer):
                oname = member.GetName()
                Respawn(oname)
                member = __main__.FindEntityByName(oname)
                member.RestorePose(1)
            else:
                member.RestoreExpression(1)
                # If it is a disposition, then restore since dispositions aren't remembered by save games
                if (member.GetData("PoseIndex") > (len(member.GetSequences()) + len(member.GetScenes()))):
                    member.RestorePose(1)
        else:
            log("Removing stale companion [%s]" % id)
            member.Kill()

    if len(createlist) == 0: return

    maker = __main__.FindEntityByName("haven_companion_maker")
    for key in createlist:
        try:
            # G.npcdata from IDUtil.py Mostly populated by companion.py
            cdata = __main__.G.npcdata[key]
        except:
            log("havenutil : PopulateHaven - companion key not found in npcdata persistent data store.")
            break
        maker.Spawn()
        c = __main__.FindEntityByName("new_partymember")
        if c:
            # Find an open slot, teleport there and rename self to reflect
            i=1
            slot=""
            while i < 8:
                slot="partymember%d" % i
                if not (slot in existslist):
                    break
                i+=1
            log("using slot [%s]" % slot)
            c.SetName(slot)
            teleport=__main__.FindEntityByName("spawn_%s" % slot)
            c.SetOrigin(teleport.GetOrigin())
            c.SetAngles(teleport.GetAngles())
            c.SetModel(cdata["Model"])
            c.LookAtEntityEye("!player")
            c.AllowAlertLookaround(0)
            c.SetExpressionByIndex(0)                     # reset expression to neutral
            c.SetData("PoseOrigin",teleport.GetOrigin())  # Place in spawn slot
            c.SetData("PoseZ",teleport.GetOrigin()[2])    # Height Adjusted Z value (changes based on pose)
            c.SetPoseByIndex(0,0)                         # Reset pose to 0
            existslist.append(slot)
        else:
            log("havenutil : PopulateHaven - Error creating partymember. (possibly exceeded maximum?)",3)

def ClearHaven():
    log("havenutil.ClearHaven() called")
    # CompMod 1.3 Patch : Stop scenes or they will continue on next Map enter.
    scenes=__main__.FindEntitiesByClass("logic_choreographed_scene")
    for scene in scenes:
        if scene.target1 and scene.target1.startswith("partymember"):
            scene.Cancel()
    sequences=__main__.FindEntitiesByClass("scripted_sequence")
    for seq in sequences:
        if seq.targetname and seq.targetname.startswith("animation_"):
            seq.CancelSequence()
    comps=__main__.FindEntitiesByName("partymember*")
    for comp in comps:
        comp.StopPose()
        comp.Kill()    

def ResetHaven():
    log("havenutil.ResetHaven() called")
    ClearHaven()
    PopulateHaven()

######################
# logic_auto Handler #
######################
#
# Only gets called when transitioning into map from another map.
# Does NOT get called on savegame reload.

def OnMapLoad(map=""):
    global g_freefall

    g_freefall=__main__.FindPlayer().GetOrigin()[2]
    log("havenutil.OnMapLoad('%s') called" % map)
    if 0 != len(__main__.G.poseNPCName):
        log("Pose State Active. (User left haven or loaded game while posing). Correcting...",2)
        npc = __main__.FindEntityByName(__main__.G.poseNPCName)
        if npc:
            npc.Kill()
            __main__.G.poseNPCName=""
            thehouse = __main__.FindEntitiesByName("partymember*")
            for member in thehouse:
                member.WillTalk(1)

    if map==__main__.G.CompHaven or map=="reload":
        PopulateHaven()
    else:
        ClearHaven()
    __main__.ScheduleTask(2.0,"havenutil.CheckFreeFall()")


def CheckFreeFall():
    global g_freefall

    pc=__main__.FindPlayer()
    log("Checking for free fall (Off map)")
    if (g_freefall - pc.GetOrigin()[2]) > 900:
        playerStarts = __main__.FindEntitiesByClass("info_player_start")
        if len(playerStarts) != 0:
            log("Freefall detected. Saving PC")
            saveFreeFall = playerStarts[0]
            pc.SetOrigin(saveFreeFall.GetOrigin())
    else:
        log("Freefall Not detected. Everything seems OK.")
    
# Visit the neighbors. Take up a collection for our new "protection" services
# Im sure you can think of a way to make money with that body of yours
# [Nosferatu] Put your skills to use. Hack into a bank or something and get me some money

        
# FROM OnDialogStart
# fix height
# Ideally, when beginning dialog, we want to fix their height/position.
# When moving an npc, we set their parent to the pc. Problem is, that
# when you do this, the child no longer reports a valid origin. As a result
# we must cacluate a location in front of the pc.

# o = npc.GetData("PoseOrigin")
# if not npc.IsBeingMoved():
#     log("havenutil : OnDialogStart - Adjusting height (%d,%d,%d)" % (o[0],o[1],o[2]))
#    npc.SetOrigin(o)

#    # pc=__main__.FindPlayer()
#    # self.distancefromPC set by self.BeginMove()
#    # origin=pc.TraceLine(npc.distancefromPC)
#    # pa=pc.GetAngles()[1]
#    # na=npc.GetAngles()
#    # reverse=(abs(((pa+180)/360)-0.5)*360)-180
#    # facing=(na[0],reverse,na[2])
#    # npc.SetAngles(facing)
#    # npc.SetOrigin(origin)        
# else:


# FROM ONDialogEnd
# o = npc.GetData("PoseOrigin")
# zadjusted=npc.GetData("PoseZ")
# Notes: When moving an npc, we set their parent to
# the pc. Problem is, that when you do this, the
# child no longer reports a valid origin. As a result
# we must traceline

#if npc.IsBeingMoved():
#    zdiff= zadjusted - o[2]
#    pc=__main__.FindPlayer()
#    p=pc.GetOrigin()
#    (x,y,z)=pc.TraceLine(npc.distancefromPC)
#    pa=pc.GetAngles()[1]
#    na=npc.GetAngles()
#    reverse=(abs(((pa+180)/360)-0.5)*360)-180
#    facing=(na[0],reverse,na[2])
#    origin=(x,y,z+zdiff)
#    npc.SetAngles(facing)
#    log("havenutil : OnDialogEnd - Adjusting height (%d,%d,%d)" % (origin[0],origin[1],origin[2]))
#    npc.SetOrigin(origin)
#else:
#    log("havenutil : OnDialogEnd - Adjusting height (%d,%d,%d)" % (o[0],o[1],zadjusted))
#    npc.SetOrigin((o[0],o[1],zadjusted))        
# if d_nextPose:
#    d_nextPose=0
#    npc.NextPose()
#elif d_prevPose:
#    d_prevPose=0
#    npc.PrevPose()
#elif d_resumePose:
#    d_resumePose=0
#    npc.ResumePose()
#elif d_pausePose:
#    d_pausePose=0
#    npc.PausePose()
# elif d_startMove:
#    d_startMove=0
#    #Once parent is set, you can't change the animation, so we must
#    #restore first:
#    npc.CheckPose()
#    npc.BeginMove()
#elif d_stopMove:
#    d_stopMove=0
#    npc.EndMove()
#    npc.CheckPose()


# scrapped
# self.anglediff=(pa[1]+180) - (na[1]+180)


# def _BeginMove(self):
#     from math import sqrt as _sqrt
#     self.beingmoved=1
#     pc=__main__.FindPlayer()
#     p=pc.GetOrigin()
#     n=self.GetOrigin()
#     log("havenutil:_BeginMove - NPC Origin (%d,%d,%d)" % (n[0],n[1],n[2]))

#     #calculate distance from pc:
#     xd=p[0]-n[0]
#     yd=p[1]-n[1]
#     self.distancefromPC=_sqrt((xd*xd) + (yd*yd))

#     # 
#     #
#     # PoseOrigin is the origin of the POSE (not necessarily the npc that we see)
#     # PoseZ keeps track of any elevation changes the USER has made to the Pose
    

#     o = self.GetData("PoseOrigin")
#     zadjusted=self.GetData("PoseZ")
#     zdiff= zadjusted - o[2]

#     (x,y,z)=pc.TraceLine(self.distancefromPC)
#     origin=(x,y,z+zdiff)
#     pa=pc.GetAngles()[1]
#     na=self.GetAngles()
#     reverse=(abs(((pa+180)/360)-0.5)*360)-180
#     facing=(na[0],reverse,na[2])
#     log("havenutil:_BeginMove - distance (%d) animation height diff=(%d)" % (self.distancefromPC,zdiff))
#     log("havenutil:_BeginMove - moving npc to (%d,%d,%d) angle" % (origin[0],origin[1],origin[2]))
#     log("havenutil:_BeginMove - adjusting facing to (%d,%d,%d)" % (facing[0],facing[1],facing[2]))
#     self.SetOrigin(origin)
#     self.SetAngles(facing)
#     self.SetParent("!player")
#     return 1

#     # scrapped
#     # self.anglediff=(pa[1]+180) - (na[1]+180)
