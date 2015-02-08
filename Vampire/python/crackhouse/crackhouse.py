print "loading crackhome level script"

import __main__
import consoleutil

from __main__ import G

__main__.Level = __name__

Find = __main__.FindEntityByName
FindList = __main__.FindEntitiesByName
FindClass = __main__.FindEntitiesByClass

# added by wesp
def girlDeath():
    pc = __main__.FindPlayer()
    if(pc.humanity >= 3):
        pc.HumanityAdd( -1 )

def bishopVickDeath():
    pc = __main__.FindPlayer()
    if pc.GetQuestState("AllPlague") > 0:
        pc.SetQuest( "AllPlague", 3 )

    if pc.GetQuestState("Regent") > 0:
        pc.SetQuest("Regent", 5)

    G.Jumbles_Removed = 1
    __main__.ChangeMap(3, "ch_exit_landmark", "trig_ch_exit")
    G.Vick_Dead = 1

#MAP: la_crackhouse_2
#------------------------------------SAMEDI2------------------------------
#SAMEDI: samedi_2 cast zombies.         
def Samedi2CastSpellzombies():
    if(G.samedi_2_anger == 1):
        Find("samedi2_cast_zombies").BeginSequence()
	__main__.ScheduleTask(0.1,"Samedi2CastZombies1()")

def Samedi2CastZombies1():
        pc=__main__.FindPlayer()
        samedi2 = Find("samedi_2")
        zombie = Find("zombie_spawner_samedi")
        zombie1 = Find("zombie_spawner1_samedi")
        samedi2.PlayDialogFile("disciplines/necromancy/level3/Activate3.wav")
        zombie.Spawn()
        zombie1.Spawn()
	__main__.ScheduleTask(5.0,"Samedi2CastThanatosis1()")

#SAMEDI: samedi_2 cast thanatosis 2 level.... 
def Samedi2CastThanatosis1():
        Find("samedi2_cast_thanatosis1").BeginSequence()
        Find("samedi_2").PlayDialogFile("disciplines/thanatosis/thanatosis1.wav")
        consoleutil.console("player_sequence knockback_smalldazed")
	__main__.ScheduleTask(0.1,"Samedi2CastThanatosis1helper1()")

def Samedi2CastThanatosis1helper1():
        consoleutil.console("sv_maxspeed 50")
	__main__.ScheduleTask(6.0,"Samedi2CastThanatosis1helper2()")

def Samedi2CastThanatosis1helper2():
        consoleutil.console("sv_maxspeed 2048")
	__main__.ScheduleTask(6.0,"Samedi2CastThanatosis2()")

#SAMEDI: samedi_2 cast thanatosis 3 level 'dust to dust'....
def Samedi2CastThanatosis2():
        Find("samedi_2").MakeInvincible(1)
	__main__.ScheduleTask(0.1,"Samedi2CastThanatosis2a()")

def Samedi2CastThanatosis2a():
        Find("samedi2_cast_thanatosis2").BeginSequence()

def Samedi2CastThanatosis2helper1():
        Find("samedi2_coat").ScriptHide()
        samedi2 = Find("samedi_2")
        Find("samedi_2").PlayDialogFile("disciplines/thanatosis/thanatosis2.wav")
        samedi2.SetModel("models/character/monster/undead/undead_male_sceleton.mdl")
        samedi2Clone=__main__.CreateEntityNoSpawn("npc_VHuman",samedi2.GetOrigin(),samedi2.GetAngles())
        samedi2Clone.SetName("samedi2Clone")
        __main__.CallEntitySpawn(samedi2Clone)
        samedi2Clone = __main__.FindEntityByName("samedi2Clone")
        if samedi2Clone:
            samedi2Clone.SetParent("samedi_2")
            samedi2Clone.SetOrigin(samedi2.GetOrigin())
            samedi2Clone.SetAngles(samedi2.GetAngles())
            samedi2Clone.SetModel("models/scenery/misc/skeleton/dead_skeleton_samedi.mdl")
	    __main__.ScheduleTask(5.0,"Samedi2CastThanatosis2helper2()")

def Samedi2CastThanatosis2helper2():
        Find("samedi2_coat").ScriptUnhide()
        samedi2 = Find("samedi_2")
        samedi2Clone = Find("samedi2Clone")
        samedi2.SetModel("models/character/npc/common/samedi/samedi.mdl")
        samedi2Clone.ClearParent()
        samedi2Clone.Kill()
	__main__.ScheduleTask(0.1,"Samedi2CastThanatosis2helper3()")

def Samedi2CastThanatosis2helper3():
        Find("samedi2_cast3_thanatosis2").BeginSequence()
        __main__.ScheduleTask(1.5,"Samedi2CastThanatosis2helper4()")

def Samedi2CastThanatosis2helper4():
        Find("samedi_2").MakeInvincible(0)
        __main__.ScheduleTask(7.1,"Samedi2CastVooDoo1()")

#SAMEDI: Samedi2 cast voodoo. damage player....      
def Samedi2CastVooDoo1():
    if(G.samedi_2_dead == 1):
        pc=__main__.FindPlayer()
        pc.Bloodloss(0)
    else:
        __main__.ScheduleTask(0.1,"Samedi2CastVooDoo2()")

def Samedi2CastVooDoo2():
    	Find("samedi2_Spell_voodoo").BeginSequence()
    	Find("samedi_2").PlayDialogFile("disciplines/thanatosis/thanatosis3.wav")
        consoleutil.console("vdmg 30")
	__main__.ScheduleTask(0.1,"Samedi2CastVooDoo3()")

def Samedi2CastVooDoo3():
        Find("voodoo_pc_start").BeginSequence()
        __main__.ScheduleTask(0.25,"Samedi2CastVooDoo4()")

def Samedi2CastVooDoo4():
        Find("voodoo_pc_start2").BeginSequence()
        __main__.ScheduleTask(2.25,"Samedi2CastVooDoo5()")

def Samedi2CastVooDoo5():
        Find("voodoo_pc_loop").BeginSequence()
        __main__.ScheduleTask(2.35,"Samedi2CastVooDoo6()")

def Samedi2CastVooDoo6():
        Find("voodoo_end").BeginSequence()
        Find("voodoo_heart").ScriptHide()

#------------------------------------SAMEDI2 END------------------------------
#----------------------------------------------------------------------------------
#la_crackhouse_2: zombies change model, for fast fight
def Zombie1ChangeModel():
    if(__main__.IsDead("sq1_zombie1")):
    	return
    else:
    	Find("sq1_zombie1").SetModel("models/character/monster/undead/undead_male_sceleton.mdl")
    	__main__.ScheduleTask(3.0,"Zombie1ChangeModel1()")

def Zombie1ChangeModel1():
    if(__main__.IsDead("sq1_zombie1")):
    	return
    else:
    	Find("sq1_zombie1").SetModel("models/character/monster/undead/zombie_male_null.mdl")

def Zombie2ChangeModel():
    if(__main__.IsDead("hall_zombie2")):
    	return
    else:
    	Find("hall_zombie2").SetModel("models/character/monster/undead/undead_male_sceleton.mdl")
    	__main__.ScheduleTask(3.0,"Zombie2ChangeModel1()")

def Zombie2ChangeModel1():
    if(__main__.IsDead("hall_zombie2")):
    	return
    else:
    	Find("hall_zombie2").SetModel("models/character/monster/undead/zombie_male_null.mdl")

def Zombie3ChangeModel():
    if(__main__.IsDead("hall_zombie1")):
    	return
    else:
    	Find("hall_zombie1").SetModel("models/character/monster/undead/undead_male_sceleton.mdl")
    	__main__.ScheduleTask(3.0,"Zombie3ChangeModel1()")

def Zombie3ChangeModel1():
    if(__main__.IsDead("hall_zombie1")):
    	return
    else:
    	Find("hall_zombie1").SetModel("models/character/monster/undead/zombie_male_null.mdl")

def Zombie4ChangeModel():
    if(__main__.IsDead("sq3_zombie5")):
    	return
    else:
    	Find("sq3_zombie5").SetModel("models/character/monster/undead/undead_male_sceleton.mdl")
    	__main__.ScheduleTask(3.0,"Zombie4ChangeModel1()")

def Zombie4ChangeModel1():
    if(__main__.IsDead("sq3_zombie5")):
    	return
    else:
    	Find("sq3_zombie5").SetModel("models/character/monster/undead/zombie_male_null.mdl")

def Zombie5ChangeModel():
    if(__main__.IsDead("sq1_zombie7")):
    	return
    else:
    	Find("sq1_zombie7").SetModel("models/character/monster/undead/undead_male_sceleton.mdl")
    	__main__.ScheduleTask(3.0,"Zombie5ChangeModel1()")

def Zombie5ChangeModel1():
    if(__main__.IsDead("sq1_zombie7")):
    	return
    else:
    	Find("sq1_zombie7").SetModel("models/character/monster/undead/zombie_male_null.mdl")

def Zombie6ChangeModel():
    if(__main__.IsDead("sq2_zombie1")):
    	return
    else:
    	Find("sq2_zombie1").SetModel("models/character/monster/undead/undead_male_sceleton.mdl")
    	__main__.ScheduleTask(3.0,"Zombie6ChangeModel1()")

def Zombie6ChangeModel1():
    if(__main__.IsDead("sq2_zombie1")):
    	return
    else:
    	Find("sq2_zombie1").SetModel("models/character/monster/undead/zombie_male_null.mdl")

def Zombie7ChangeModel():
    if(__main__.IsDead("sq3_zombie3")):
    	return
    else:
    	Find("sq3_zombie3").SetModel("models/character/monster/undead/undead_male_sceleton.mdl")
    	__main__.ScheduleTask(3.0,"Zombie7ChangeModel1()")

def Zombie7ChangeModel1():
    if(__main__.IsDead("sq3_zombie3")):
    	return
    else:
    	Find("sq3_zombie3").SetModel("models/character/monster/undead/zombie_male_null.mdl")

def Zombie8ChangeModel():
    if(__main__.IsDead("sq2_zombie3")):
    	return
    else:
    	Find("sq2_zombie3").SetModel("models/character/monster/undead/undead_male_sceleton.mdl")
    	__main__.ScheduleTask(3.0,"Zombie8ChangeModel1()")

def Zombie8ChangeModel1():
    if(__main__.IsDead("sq2_zombie3")):
    	return
    else:
    	Find("sq2_zombie3").SetModel("models/character/monster/undead/zombie_male_null.mdl")

def Zombie9ChangeModel():
    if(__main__.IsDead("sq2_zombie5")):
    	return
    else:
    	Find("sq2_zombie5").SetModel("models/character/monster/undead/undead_male_sceleton.mdl")
    	__main__.ScheduleTask(3.0,"Zombie9ChangeModel1()")

def Zombie9ChangeModel1():
    if(__main__.IsDead("sq2_zombie5")):
    	return
    else:
    	Find("sq2_zombie5").SetModel("models/character/monster/undead/zombie_male_null.mdl")

#----------------------------------------------------------------------------------

print "crackhouse levelscript loaded"
