print "loading museum level script"

import __main__

from __main__ import G

__main__.Level = __name__

Find = __main__.FindEntityByName

## set Occult Items quest state, changed by wesp
def doorCode():
    pc = __main__.FindPlayer()
    state = pc.GetQuestState("Museum")
    if state < 3:
            pc.SetQuest("Museum", 4)

## spawn key player needs to unlock storage if he triggered beams
def SpawnStorageKey():
    guard = Find("guard_maker_5")
    center = guard.GetCenter()
    point = (center[0], center[1], center[2])
    key = __main__.CreateEntityNoSpawn( "item_k_museum_storage_key", point, (0,0,0) )
    key.SetName("storage_key")
    __main__.CallEntitySpawn(key)
    sparklies = __main__.CreateEntityNoSpawn("inspection_node", point, (0, 0, 0))
    sparklies.SetParent("storage_key")
    __main__.CallEntitySpawn(sparklies)

def OnKeyGuardDeath():
    ## don't spawn key if guard has already dropped it.
    if not G.Museum_DroppedKey:
        SpawnStorageKey()

## fade alarm sound out when player opens door to sarcophagus workroom
def AlarmFadeOut():
    if (G.Museum_Alarm == 1):
        a = Find("fade_out_alarm")
        a.Trigger()

## synchronize patrol routes of upstairs guards so they're always
## on opposite sides of the gallery
def WaitForPartner(i):
    g3 = Find("npc_guard_3")
    g4 = Find("npc_guard_4")

    if (not g3):
        G.Museum_Guard3 = 1
    elif (not g4):
        G.Museum_Guard4 = 1

    if (i == 3):
        G.Museum_Guard3 = 1
    elif (i == 4):
        G.Museum_Guard4 = 1

    # alert triggered.  g3 takes ready position, g4 continues patrol.
    if (i == -1):
        if g4: g4.SetupPatrolType("9999 0 FOLLOW_PATROL_PATH_WALK")
        if g4: g4.FollowPatrolPath("C3 C4 C5 C1 C2")

    elif (G.Museum_Guard3 and G.Museum_Guard4):
        if g3: g3.SetupPatrolType("0 0 FOLLOW_PATROL_PATH_WALK")
        if g4: g4.SetupPatrolType("0 0 FOLLOW_PATROL_PATH_WALK")
        if g3: g3.FollowPatrolPath("C1 C2 C3 C4 C5")
        if g4: g4.FollowPatrolPath("C3 C4 C5 C1 C2")

        G.Museum_Guard3 = 0
        G.Museum_Guard4 = 0

## set Occult Items quest state, changed by wesp
def SetOccultQuestState():
    pc = __main__.FindPlayer()
    state = pc.GetQuestState("Occult")
    if state == 3:
            pc.SetQuest("Occult", 4)
    elif state == 1:
            pc.SetQuest("Occult", 2)

## infrared beams towards the end of the museum, changed by RobinHood70
class MuseumBeams :
    def __init__(self):
        self.reinit()

    def reinit(self):
        self.track = []
        self.beamTrig = []
        self.beam = []
        self.beamOn = [0, 0, 0, 0, 0, 0, 0, 0]
        self.numBeams = 8
        self.beamsEnabled = 1
        self.beamsFlicker = G.MuseumBeamsFlicker
        self.beamsStarted = 0

        self.FindTracks()
        self.FindBeamTrigs()
        self.FindBeams()

        self.SetBeamWidth(1)

        for i in range(self.numBeams):
            __main__.ScheduleTask(0.10, "mb.ToggleBeam(%i)" % i)
            __main__.ScheduleTask(0.20, "mb.ToggleBeam(%i)" % i)

        #drawer = Find("basement_desk_drawer")
        #if G.Patch_Plus < 2:
        #    drawer.SpawnItemInContainer("item_g_wireless_camera_3")

    ## get beams started
    def StartBeams(self):
        if self.beamsStarted == 0:
            for i in range( len(self.track) ):
                self.track[i].Open()
                self.beamOn[i] = 1

            self.beamsStarted = 1

    ## make beam[i] go other direction when it hits the end of its track
    ## toggle beam[i] on/off when open/close if power shot out
    def ToggleBeam(self, i):
        if i >= self.numBeams:
            print("Invalid Beam %d" % i)
            return
        elif self.beamOn[i] == 1:
            self.beamOn[i] = 0
            try:
                self.track[i].Close()
            except:
                print("Track %i could not be closed.  This is a normal error when re-loading." % i)
        else:
            self.beamOn[i] = 1
            try:
                self.track[i].Open()
            except:
                print("Track %i could not be opened.  This is a normal error when re-loading." % i)

        if self.beamsFlicker == 1 and self.beamsEnabled == 1:
            try:
                self.beam[i].Toggle()
            except:
                print("Could not toggle beam %i.  This is a normal error when re-loading." % i)
            try:
                self.beamTrig[i].Toggle()
            except:
                print("Could not toggle beamTrig %i.  This is a normal error when re-loading." % i)
##            __main__.ScheduleTask(0.20, "__main__.FindEntityByName(\"beam_trig_%d\").Toggle()" %(i+1))

    def FindTracks(self):
        self.track = []

        for i in range(self.numBeams):
            t = Find("track_%i" % (i+1))
            self.track.append(t)

    def FindBeamTrigs(self):
        self.beamTrig = []

        for i in range(self.numBeams):
            b = Find("beam_trig_%i" % (i+1))
            self.beamTrig.append(b)

    def FindBeams(self):
        self.beam = []

        for i in range(self.numBeams):
            b = Find("beam_%i" % (i+1))
            self.beam.append(b)

    def SetBeamWidth(self, width):
        for b in self.beam:
            b.Width(width)

    ## hack terminal enables beams
    def EnableBeamTrigs(self):
        for i in range( len(self.beamTrig) ):
            self.beamTrig[i].Enable()
            self.beam[i].TurnOn()
            self.track[i].StartMoving()
        self.beamsEnabled = 1

    ## hack terminal disables beams
    def DisableBeamTrigs(self):
        for i in range( len(self.beamTrig) ):
            self.beamTrig[i].Disable()
            self.beam[i].TurnOff()
            self.track[i].StopMoving()
        self.beamsEnabled = 0

mb = MuseumBeams()

def BeckettDialogEnd():
    if G.Museum_Kill == 0:
        __main__.FindPlayer().AwardExperience('Museum04')
        # if G.Beckett_Goodbye == 1:
        # Changed By CompMod
        # if __main__.IsClan(__main__.FindPlayer(), "Nosferatu"):
    if 5 == __main__.G._pcinfo["clan"]:    
        __main__.ChangeMap(2.5, "sewer_map_landmark", "trig_museum_exit_sewer")
    else:
        __main__.ChangeMap(2.5, "taxi_landmark", "trig_museum_exit")

###-------------------------------------------------------------------
### security cameras can not find PC lasombra
def Lasombrasecuritycamera1check():
    pc=__main__.FindPlayer()
    clan = pc.clan

    if(clan == 2):
	Find("sec_cam_1").Disable()
    else:     
	Find("alert_event").Trigger()
	Find("guard_maker_1").Enable()

def Lasombrasecuritycamera2check():
    pc=__main__.FindPlayer()
    clan = pc.clan

    if(clan == 2):
	Find("sec_cam_2").Disable()
    else:     
	Find("alert_event").Trigger()
	Find("guard_maker_3").Enable()

def Lasombrasecuritycamera3check():
    pc=__main__.FindPlayer()
    clan = pc.clan

    if(clan == 2):
	Find("sec_cam_3").Disable()
    else:     
	Find("alert_event").Trigger()
	Find("guard_maker_2").Enable()

def Lasombrasecuritycamera4check():
    pc=__main__.FindPlayer()
    clan = pc.clan

    if(clan == 2):
	Find("sec_cam_4").Disable()
    else:     
	Find("alert_event").Trigger()
	Find("guard_maker_2").Enable()

def Lasombrasecuritycamera5check():
    pc=__main__.FindPlayer()
    clan = pc.clan

    if(clan == 2):
	Find("sec_cam_5").Disable()
    else:     
	Find("alert_event").Trigger()
	Find("guard_maker_2").Enable()

def Lasombrasecuritycamera6check():
    pc=__main__.FindPlayer()
    clan = pc.clan

    if(clan == 2):
	Find("last_sec_cam_6").Disable()
    else:     
	Find("alert_event").Trigger()
	Find("npc_maker_basement_2").Spawn()

print "levelscript loaded"
