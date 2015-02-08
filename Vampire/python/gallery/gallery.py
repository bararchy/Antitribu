print "loading gallery level script"
#function's comments indicate what map they are called on
import __main__

from __main__ import G

__main__.Level = __name__

Find = __main__.FindEntityByName
FindList = __main__.FindEntitiesByName
FindClass = __main__.FindEntitiesByClass

from __main__ import Character

RandomLine = __main__.RandomLine
#slashedPaintings = [0, 0, 0, 0]

# added by wesp
def civilianDeath():
    pc = __main__.FindPlayer()
    if(pc.humanity >= 3):
        pc.HumanityAdd( -1 )

#GALLERY: called when the blood guardian is killed
def bloodGuardianDeath():
    __main__.FindPlayer().SetQuest("Slashterpiece", 2)
    G.Jeanette_Quest = 2

#GALLERY: called when the PC steals the charity money from Gallery Noir, changed by wesp
def charityMoneyStolen():
    pc = __main__.FindPlayer()
    pc.MoneyAdd(250)
    box_spark = Find("box_sparklies")
    box_spark.ScriptHide()
    if (pc.humanity >= 6 and G.Charity_Know == 0):
        pc.HumanityAdd(-1)

#GALLERY: gives the player the money, added by wesp
def playerGotBox():
    pc = __main__.FindPlayer()
    if (G.Got_Cash == 0):
        G.Got_Cash = 1
        pc.MoneyAdd(250)
        box_spark = Find("box_sparklies")
        if (box_spark): box_spark.ScriptHide()
        if (pc.humanity >= 6 and G.Charity_Know == 0):
            pc.HumanityAdd(-1)

#GALLERY: disables security in the Gallery if Chunk allows the player to enter, changed by wesp
def disableGallerySecurity():
    if(G.Jeanette_Quest == 1 and (G.Chunk_Befriend >= 2 or G.Chunk_Dominated >= 1 or G.Chunk_Demented == 1)):
        __main__.FindPlayer().SetQuest("Slashterpiece", 6)
        switch = Find("camera_switch")
        switch.Deactivate()

#pretty self explanatory really
def enterGallery():
    G.SlashedPaintings = [0, 0, 0, 0]

#the paintings were slashed out of order, and now they will heal themselves
def healPaintings():
    i = 0
    while(i < 4):
        G.SlashedPaintings[i] = 0
        i = i + 1
    healer = Find("painting_healer")
    healer.Trigger()
    __main__.FindPlayer().Bloodloss(1)

#GALLERY: determines if the paintings have been placed in the gallery
def paintingsInGallery():
    if(G.Jeanette_Quest == 1 or G.Jeanette_Refuse > 0):
        i = 0
        while(i < 4):
            painting = Find("painting_%i" % i)
            painting.ScriptUnhide()
            i = i + 1
        signs = __main__.FindEntitiesByName("signs")
        for s in signs:
            s.ScriptUnhide()
        #monies = Find("cash_box")
        #monies = Find("charity_monies")
        #monies.ScriptUnhide()
	Find("charity_monies_box").ScriptUnhide()
        box_spark = Find("box_sparklies")
        box_spark.ScriptUnhide()
    if(G.Jeanette_Refuse > 0 or G.Jeanette_Quest == 2):
        relay = Find("gallery_done_relay")
        relay.Trigger()
# removed       monies = Find("charity_monies")
# by wesp       monies.Kill()

#Gallery: called when a painting gets slashed.  Determines if it stays slashed, or if healing occurs
def paintingSlashed(p):
    outOfOrder = 0
    if(p == 0):
        G.SlashedPaintings[0] = 1
    else:
        i = 0
        while(i < p):
            if(G.SlashedPaintings[i] == 0):
                outOfOrder = 1
                break;
            i = i + 1
        if(outOfOrder == 1):
            healPaintings()
        else:
            G.SlashedPaintings[p] = 1
            if(p == 3):
                summonBloodCreature()

#GALLERY: updates the PC when they have slashed the paintings
def paintingsSlashed():
    G.Jeanette_Quest = 2
    __main__.FindPlayer().SetQuest("Slashterpiece", 2)

#GALLERY: Summons the blood creature when all four paintings are slashed.
def summonBloodCreature():
    summoner = Find("summon_relay")
    summoner.Trigger()

#--------------------------------------------Antitribu mod-----------------------------------
#MUMMY GUARD:  check die mummy urns 
def GalMummyUrnsCheck():
    #Find("BloodGuardian").PlayDialogFile("area/santa_monica/ocean_house/spell_necromantic_evil_undead.wav")
    #Find("BloodGuardian").SetGesture("knockback_biglow")
    G.GalMummyUrns_Death = G.GalMummyUrns_Death + 1
    
    if(G.GalMummyUrns_Death == 3):
       Find("BloodGuardian").PlayDialogFile("area/santa_monica/ocean_house/spell_necromantic_evil_undead.wav")
       #Find("BloodGuardian").SetGesture("knockback_biglow")
       __main__.ScheduleTask(0.35,"GalMummyTransform1()")
       Find("MummyTransform_relay").Trigger()

def GalMummyTransform1():
    #Find("BloodGuardian").SetModel("models/character/monster/undead/undead_female_sceleton.mdl")
    G.GalMummyTransform = 1
    Find("BloodGuardian").SetScriptedDiscipline("potence 3")
    Find("BloodGuardian_cast_timer").Disable()
    #Find("BloodGuardian").SetGesture("ACT_ZOMBIE_FEED_LUNGE")
    Find("BloodGuardian").SetGesture("Reaching")

def bloodGuardianDamaged():
    if(not G.GalMummyTransform == 1):
       __main__.ccmd.DamagePlayer=""

def bloodGuardianCast():
    pc=__main__.FindPlayer()
    if(not G.GalMummyTransform == 1):
       Find("BloodGuardian").PlayDialogFile("disciplines/thanatosis/thanatosis1.wav")
       Find("BloodGuardian").SetGesture("Reaching")
       Find("BloodGuardian").SpawnTempParticle("SamediSpell3")
       Find("BloodGuardian").SpawnTempParticle("SamediSpell4")
       pc.SpawnTempParticle("SamediSpell3")
       pc.SpawnTempParticle("SamediSpell4")
       pc.Bloodloss(1)
       __main__.ccmd.PcDominatedAnim=""
       #__main__.cvar.fadein=10 
       __main__.ccmd.fadein=""
       __main__.ccmd.thirdperson=""

#--------------------------------------------
#BLOODHUNT: called to see if the obfuscators should use potence
def obfuscatorsCheck():
    if(G.Bloodhunt_Obfuscate == 0):
        obfuscate_users = FindList("obfuscate_*")
        for obfuscate_user in obfuscate_users:
            obfuscate_user.SetScriptedDiscipline("potence 3")

#BLOODHUNT: called to see if Trip or Mercurio will still deal during the bloodhunt
def openShops():
    IsDead = __main__.IsDead
    if(not IsDead("Trip")):
        door = Find("trips_door")
        door.Unlock()
    if(not IsDead("Mercurio") and G.Mercurio_Attack == 0):
        door = Find("apartment_door_right")
        door.Unlock()
        door = Find("apartment_door_left")
        door.Unlock()
    #puts angry Ghouls on the map
    if(not IsDead("Knox") and G.Knox_Pissed > 0):
        knox = Find("Knox")
        if knox: knox.ScriptUnhide()
    if(not IsDead("Mercurio") and G.Mercurio_Attack == 1 and G.Prince_Mercurio == 0):
        mercurio = Find("Mercurio")
        if mercurio: mercurio.ScriptUnhide()

#BLOODHUNT: called by caine to transition to the taxi map
def toCaineTaxi():
    __main__.ChangeMap(2.5, "Caine_landmark", "CaineTeleport1")

#------------------------------------Gangrel1 transform------------------------------
#Blood hunt gangrel1 wolf form transform
def Gangrel1WolfTransform():
    if(G.Gangrel1_wolfform == 1):
         return
    else:
         __main__.ScheduleTask(0.1,"Gangrel1WolfTransform1a()")
	 G.Gangrel1_wolfform = 1

def Gangrel1WolfTransform1a():
    Find("gangrel1_transform").BeginSequence()

def Gangrel1WolfTransform1():
    Find("gangrel_1").SetModel("models/weapons/disciplines/animalism/grey_wolf.mdl")
    Find("gangrel_1").PlayDialogFile("disciplines/animalism/level5/anm_lvl5_activate.wav")
    #Find("gangrel_1").SetScriptedDiscipline("mind_shield 5")
    __main__.ScheduleTask(0.25,"Gangrel1WolfTransform1b()")

def Gangrel1WolfTransform1b():
    Find("gangrel_1").MakeInvincible(0)
    Find("ip_10a").Disable()
    Find("ip_10b").Disable()
    Find("ip_10c").Disable()

#------------------------------------Gangrel2 transform------------------------------
#Blood hunt gangrel1 wolf form transform
def Gangrel2WolfTransform():
    if(G.Gangrel2_wolfform == 1):
         return
    else:
         __main__.ScheduleTask(0.1,"Gangrel2WolfTransform1a()")
	 G.Gangrel2_wolfform = 1

def Gangrel2WolfTransform1a():
    Find("gangrel2_transform").BeginSequence()

def Gangrel2WolfTransform1():
    Find("gangrel_2").SetModel("models/weapons/disciplines/animalism/grey_wolf.mdl")
    Find("gangrel_2").PlayDialogFile("disciplines/animalism/level5/anm_lvl5_activate.wav")
    #Find("gangrel_2").SetScriptedDiscipline("mind_shield 5")
    __main__.ScheduleTask(0.25,"Gangrel2WolfTransform1b()")

def Gangrel2WolfTransform1b():
    Find("gangrel_2").MakeInvincible(0)

#--------------------------------------------

print "levelscript loaded"
