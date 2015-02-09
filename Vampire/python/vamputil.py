import __main__
from random import Random
from time import time
from string import atoi
from __main__ import Character

huntersDead = [0, 0, 0]

Find = __main__.FindEntityByName
FindList = __main__.FindEntitiesByName
FindClass = __main__.FindEntitiesByClass

##############################################################################
# Companion Mod
#
# The following events/methods were created to support the companion mod, but
# have been broken out globally so that other mods can hook into the extended
# events.

import time
import configutil
import companion
import possessutil
import characterext
import dialogutil
import havenutil
import consoleutil
import fileutil
import eventutil
import statutil
import musicutil
import soundutil
import castanimalism
import castnecromancy
import castnihilistics
import castthanatosislvl3
import castkoldunism
import castpresence
import idutil
import dispositionutil
import expressionutil
import modelutil
  
from logutil import log

##############################################################################
# ZVTools
#

_mod_options=configutil.Options("mods.cfg")
if _mod_options.get("mod_enable_zvtools",0):
    from zvtool.zvtool import *

##############################################################################
# Root Events
##############################################################################

##############################################################################
# Discpline Interception

# Code requires that the following aliases are present in autoexec.cfg:
#
# alias execonsole "exec console.cfg"
# alias m_vdiscipline_last "__main__.ScheduleTask(0.3,'OnActivateDiscipline()');vdiscipline_last"
##############################################################################

def CaptureDisciplines():
    import nt
    
    path ='Vampire/cfg/config.cfg'
    try: st = nt.stat(path)
    except nt.error: return

    lines = []
    data = ''
    fin = None
    try:
        fin = open(path,"r")
        line = fin.readline()
        while line:
            line = line.rstrip()
            slice = line.rfind('"vdiscipline_last"')
            if -1 != slice:
                rbound = slice
                slice = line.find(' ')
                data = '%sbind %s "m_vdiscipline_last"\n' % (data,line[slice:rbound].strip())
            line=fin.readline()
    finally:
        if fin: fin.close()
    if data=="": return
    cfg=open('Vampire/cfg/console.cfg', 'w')
    try: cfg.write(data)
    finally: cfg.close()
    __main__.ccmd.execonsole=""

#--------------------------------NEW DISCIPLINES---------------------------------
#NEW Disciplines for Bloodlines: Antitribu (made by Lenusk@)

CaptureDisciplines()

def OnActivateDiscipline():

    pc=__main__.FindPlayer()
    npc=__main__.FindEntitiesByClass("npc_V*")
    clan = pc.clan
    koldunism = Find("koldunic_helper")
            
#--------------------------------Disciplines starting----------------------
#------------------------------Discipline NEW Domination------------
#Discipline NEW Domination 

    if(1 == pc.active_dominate):
        pc.RemoveItem("item_w_fists")
        __main__.ccmd.player_immobilize=""
        if(pc.IsMale()):
            pc.GiveItem("item_w_mingxiao_spit")
            consoleutil.console("use item_w_mingxiao_spit")
            __main__.ScheduleTask(1.85,"castmalend()")
        else:
            pc.GiveItem("item_w_tzimisce2_head")
            consoleutil.console("use item_w_tzimisce2_head")
            __main__.ScheduleTask(1.85,"castfemend()")

    if(2 == pc.active_dominate):
        pc.RemoveItem("item_w_fists")
        __main__.ccmd.player_immobilize=""
        if(pc.IsMale()):
            pc.GiveItem("item_w_mingxiao_spit")
            consoleutil.console("use item_w_mingxiao_spit")
            __main__.ScheduleTask(1.85,"castmalend()")
        else:
            pc.GiveItem("item_w_tzimisce2_head")
            consoleutil.console("use item_w_tzimisce2_head")
            __main__.ScheduleTask(1.85,"castfemend()")

    if(3 == pc.active_dominate):
        pc.RemoveItem("item_w_fists")
        __main__.ccmd.player_immobilize=""
        if(pc.IsMale()):
            pc.GiveItem("item_w_mingxiao_spit")
            consoleutil.console("use item_w_mingxiao_spit")
            __main__.ScheduleTask(1.85,"castmalend()")
        else:
            pc.GiveItem("item_w_tzimisce2_head")
            consoleutil.console("use item_w_tzimisce2_head")
            __main__.ScheduleTask(1.85,"castfemend()")

    if(4 == pc.active_dominate):
        pc.RemoveItem("item_w_fists")
        __main__.ccmd.player_immobilize=""
        if(pc.IsMale()):
            pc.GiveItem("item_w_mingxiao_spit")
            consoleutil.console("use item_w_mingxiao_spit")
            __main__.ScheduleTask(1.85,"castmalend()")
        else:
            pc.GiveItem("item_w_tzimisce2_head")
            consoleutil.console("use item_w_tzimisce2_head")
            __main__.ScheduleTask(1.85,"castfemend()")

    if(5 == pc.active_dominate):
        pc.RemoveItem("item_w_fists")
        __main__.ccmd.player_immobilize=""
        if(pc.IsMale()):
            pc.GiveItem("item_w_mingxiao_spit")
            consoleutil.console("use item_w_mingxiao_spit")
            __main__.ScheduleTask(1.85,"castmalend()")
        else:
            pc.GiveItem("item_w_tzimisce2_head")
            consoleutil.console("use item_w_tzimisce2_head")
            __main__.ScheduleTask(1.85,"castfemend()")

#------------------------------Discipline presence------------
#Discipline presence

    if(1 == pc.active_presence):
        __main__.ScheduleTask(0.0,"PresenceCastOne()")

    if(2 == pc.active_presence):
        __main__.ScheduleTask(0.0,"PresenceCastTwo()")

    if(3 == pc.active_presence):
        __main__.ScheduleTask(0.0,"PresenceCastThree()")

    if(4 == pc.active_presence):
        __main__.ScheduleTask(0.0,"PresenceCastFour()")

    if(5 == pc.active_presence):
        __main__.ScheduleTask(0.0,"PresenceCastFive()")

#------------------------------Discipline Serpentis------------
#Discipline Serpentis (fortitude) (animalism)

    if(1 == pc.active_animalism):
        __main__.ccmd.player_immobilize=""
        __main__.ScheduleTask(0.0,"CastSerpentisOne()")

    if(2 == pc.active_animalism):
        __main__.ccmd.player_immobilize=""
        __main__.ScheduleTask(0.0,"CastSerpentisTwo()")

    if(3 == pc.active_animalism):
        __main__.ScheduleTask(0.0,"CastSerpentisThree()")

    if(4 == pc.active_animalism):
        __main__.ccmd.player_immobilize=""
        __main__.ScheduleTask(0.0,"CastSerpentisFour()")

    if(5 == pc.active_animalism):
        __main__.ccmd.player_immobilize=""
        __main__.ScheduleTask(0.0,"CastSerpentisFive()")

#------------------------------NEW Discipline Thanatosis------------
#NEW Discipline Thanatosis

    if 1 == pc.active_thaumaturgy:
            pc.RemoveItem("item_w_fists")
            pc.GiveItem("item_w_mingxiao_spit")
            consoleutil.console("hidehud 1")
            __main__.ScheduleTask(0.1,"thanatosislvl1()")

    if 2 == pc.active_thaumaturgy:
            pc.RemoveItem("item_w_fists")
            __main__.ccmd.player_immobilize=""
            pc.GiveItem("item_w_zombie_fists")
            consoleutil.console("use item_w_zombie_fists")
            #__main__.ScheduleTask(0.1,"thanatosislvl2()")
            __main__.ScheduleTask(1.65,"castthanatosisend()")

    if 3 == pc.active_thaumaturgy:
            pc.RemoveItem("item_w_fists")
            pc.GiveItem("item_w_mingxiao_spit")
            consoleutil.console("hidehud 1")
	    __main__.ccmd.player_immobilize=""
            __main__.ScheduleTask(0.65,"thanatosislvl3()")

    if 4 == pc.active_thaumaturgy:
            pc.RemoveItem("item_w_fists")
            __main__.ccmd.player_immobilize=""
            pc.GiveItem("item_w_zombie_fists")
            consoleutil.console("use item_w_zombie_fists")
            #__main__.ScheduleTask(0.1,"thanatosislvl4()")
            __main__.ScheduleTask(1.65,"castthanatosisend()")

    if 5 == pc.active_thaumaturgy:
            pc.RemoveItem("item_w_fists")
            __main__.ccmd.player_immobilize=""
            pc.GiveItem("item_w_zombie_fists")
            consoleutil.console("use item_w_zombie_fists")
            #__main__.ScheduleTask(0.1,"thanatosislvl5()")
            __main__.ScheduleTask(1.65,"castthanatosisend()")

#------------------------------NEW passive animalism------------
#NEW Discipline Animalism 

    if(6 == pc.active_thaumaturgy):
        pc.RemoveItem("item_w_fists")
        __main__.ccmd.player_immobilize=""
        if(pc.IsMale()):
            pc.GiveItem("item_w_mingxiao_spit")
            consoleutil.console("use item_w_mingxiao_spit")
            __main__.ScheduleTask(0.45,"passiveanimlvl1()")
            __main__.ScheduleTask(1.85,"castmalend()")
        else:
            pc.GiveItem("item_w_tzimisce2_head")
            consoleutil.console("use item_w_tzimisce2_head")
            __main__.ScheduleTask(0.45,"passiveanimlvl1()")
            __main__.ScheduleTask(1.85,"castfemend()")

    if(7 == pc.active_thaumaturgy):
        pc.RemoveItem("item_w_fists")
        __main__.ccmd.player_immobilize=""
        if(pc.IsMale()):
            pc.GiveItem("item_w_mingxiao_spit")
            consoleutil.console("use item_w_mingxiao_spit")
            __main__.ScheduleTask(0.45,"passiveanimlvl2()")
            __main__.ScheduleTask(1.85,"castmalend()")
        else:
            pc.GiveItem("item_w_tzimisce2_head")
            consoleutil.console("use item_w_tzimisce2_head")
            __main__.ScheduleTask(0.45,"passiveanimlvl2()")
            __main__.ScheduleTask(1.85,"castfemend()")

    if(8 == pc.active_thaumaturgy):
        pc.RemoveItem("item_w_fists")
        __main__.ccmd.player_immobilize=""
        if(pc.IsMale()):
            pc.GiveItem("item_w_mingxiao_spit")
            consoleutil.console("use item_w_mingxiao_spit")
            __main__.ScheduleTask(0.45,"passiveanimlvl3()")
            __main__.ScheduleTask(1.85,"castmalend()")
        else:
            pc.GiveItem("item_w_tzimisce2_head")
            consoleutil.console("use item_w_tzimisce2_head")
            __main__.ScheduleTask(0.45,"passiveanimlvl3()")
            __main__.ScheduleTask(1.85,"castfemend()")

    if(9 == pc.active_thaumaturgy):
        pc.RemoveItem("item_w_fists")
        __main__.ccmd.player_immobilize=""
        if(pc.IsMale()):
            pc.GiveItem("item_w_mingxiao_spit")
            consoleutil.console("use item_w_mingxiao_spit")
            __main__.ScheduleTask(0.45,"passiveanimlvl4()")
            __main__.ScheduleTask(1.85,"castmalend()")
        else:
            pc.GiveItem("item_w_tzimisce2_head")
            consoleutil.console("use item_w_tzimisce2_head")
            __main__.ScheduleTask(0.45,"passiveanimlvl4()")
            __main__.ScheduleTask(1.85,"castfemend()")

    if(10 == pc.active_thaumaturgy):
        pc.RemoveItem("item_w_fists")
        __main__.ccmd.player_immobilize=""
        if(pc.IsMale()):
            pc.GiveItem("item_w_mingxiao_spit")
            consoleutil.console("use item_w_mingxiao_spit")
            __main__.ScheduleTask(0.45,"passiveanimlvl5()")
            __main__.ScheduleTask(1.85,"castmalend()")
        else:
            pc.GiveItem("item_w_tzimisce2_head")
            consoleutil.console("use item_w_tzimisce2_head")
            __main__.ScheduleTask(0.45,"passiveanimlvl5()")
            __main__.ScheduleTask(1.85,"castfemend()")

#------------------------------NEW Discipline passive Necromancy ------------

    if(11 == pc.active_thaumaturgy):
        pc.RemoveItem("item_w_fists")
        __main__.ccmd.player_immobilize=""
        if(clan == 5):
            pc.GiveItem("item_w_zombie_fists")
            consoleutil.console("use item_w_zombie_fists")
            __main__.ScheduleTask(0.45,"passivenecrolvl1()")
            __main__.ScheduleTask(1.85,"castthanatosisend()")
        elif(not clan == 5 and pc.IsMale()):
            pc.GiveItem("item_w_mingxiao_spit")
            consoleutil.console("use item_w_mingxiao_spit")
            __main__.ScheduleTask(0.45,"passivenecrolvl1()")
            __main__.ScheduleTask(1.85,"castmalend()")
        elif(not clan == 5 and not pc.IsMale()):
            pc.GiveItem("item_w_tzimisce2_head")
            consoleutil.console("use item_w_tzimisce2_head")
            __main__.ScheduleTask(0.45,"passivenecrolvl1()")
            __main__.ScheduleTask(1.85,"castfemend()")

    if(12 == pc.active_thaumaturgy):
        pc.RemoveItem("item_w_fists")
        __main__.ccmd.player_immobilize=""
        if(clan == 5):
            pc.GiveItem("item_w_zombie_fists")
            consoleutil.console("use item_w_zombie_fists")
            __main__.ScheduleTask(0.45,"passivenecroSamedilvl2()")
            __main__.ScheduleTask(1.85,"castthanatosisend()")
        elif(clan == 7 and pc.IsMale()):
            pc.GiveItem("item_w_mingxiao_spit")
            consoleutil.console("use item_w_mingxiao_spit")
            __main__.ScheduleTask(0.45,"passivenecroSamedilvl2()")
            __main__.ScheduleTask(1.85,"castmalend()")
        elif(clan == 7 and not pc.IsMale()):
            pc.GiveItem("item_w_tzimisce2_head")
            consoleutil.console("use item_w_tzimisce2_head")
            __main__.ScheduleTask(0.45,"passivenecroSamedilvl2()")
            __main__.ScheduleTask(1.85,"castfemend()")
        elif(clan == 8 and pc.IsMale()):
            pc.GiveItem("item_w_mingxiao_spit")
            consoleutil.console("use item_w_mingxiao_spit")
            __main__.ScheduleTask(0.45,"passivenecrolvl2()")
            __main__.ScheduleTask(1.85,"castmalend()")
        elif(clan == 8 and not pc.IsMale()):
            pc.GiveItem("item_w_tzimisce2_head")
            consoleutil.console("use item_w_tzimisce2_head")
            __main__.ScheduleTask(0.45,"passivenecrolvl2()")
            __main__.ScheduleTask(1.85,"castfemend()")

    if(13 == pc.active_thaumaturgy):
        pc.RemoveItem("item_w_fists")
        __main__.ccmd.player_immobilize=""
        if(clan == 5):
            pc.GiveItem("item_w_zombie_fists")
            consoleutil.console("use item_w_zombie_fists")
            __main__.ScheduleTask(0.45,"passivenecroSamedilvl3()")
            __main__.ScheduleTask(1.85,"castthanatosisend()")
        elif(clan == 7 and pc.IsMale()):
            pc.GiveItem("item_w_mingxiao_spit")
            consoleutil.console("use item_w_mingxiao_spit")
            __main__.ScheduleTask(0.45,"passivenecroSamedilvl3()")
            __main__.ScheduleTask(1.85,"castmalend()")
        elif(clan == 7 and not pc.IsMale()):
            pc.GiveItem("item_w_tzimisce2_head")
            consoleutil.console("use item_w_tzimisce2_head")
            __main__.ScheduleTask(0.45,"passivenecroSamedilvl3()")
            __main__.ScheduleTask(1.85,"castfemend()")
        elif(clan == 8 and pc.IsMale()):
            pc.GiveItem("item_w_mingxiao_spit")
            consoleutil.console("use item_w_mingxiao_spit")
            __main__.ScheduleTask(0.45,"passivenecrolvl3()")
            __main__.ScheduleTask(1.85,"castmalend()")
        elif(clan == 8 and not pc.IsMale()):
            pc.GiveItem("item_w_tzimisce2_head")
            consoleutil.console("use item_w_tzimisce2_head")
            __main__.ScheduleTask(0.45,"passivenecrolvl3()")
            __main__.ScheduleTask(1.85,"castfemend()")

    if(14 == pc.active_thaumaturgy):
        pc.RemoveItem("item_w_fists")
        __main__.ccmd.player_immobilize=""
        if(clan == 5):
            pc.GiveItem("item_w_zombie_fists")
            consoleutil.console("use item_w_zombie_fists")
            __main__.ScheduleTask(0.45,"passivenecroSamedilvl4()")
            __main__.ScheduleTask(1.85,"castthanatosisend()")
        elif(clan == 7 and pc.IsMale()):
            pc.GiveItem("item_w_mingxiao_spit")
            consoleutil.console("use item_w_mingxiao_spit")
            __main__.ScheduleTask(0.45,"passivenecroNagarajalvl4()")
            __main__.ScheduleTask(1.85,"castmalend()")
        elif(clan == 7 and not pc.IsMale()):
            pc.GiveItem("item_w_tzimisce2_head")
            consoleutil.console("use item_w_tzimisce2_head")
            __main__.ScheduleTask(0.45,"passivenecroNagarajalvl4()")
            __main__.ScheduleTask(1.85,"castfemend()")
        elif(clan == 8 and pc.IsMale()):
            pc.GiveItem("item_w_mingxiao_spit")
            consoleutil.console("use item_w_mingxiao_spit")
            __main__.ScheduleTask(0.45,"passivenecrolvl4()")
            __main__.ScheduleTask(1.85,"castmalend()")
        elif(clan == 8 and not pc.IsMale()):
            pc.GiveItem("item_w_tzimisce2_head")
            consoleutil.console("use item_w_tzimisce2_head")
            __main__.ScheduleTask(0.45,"passivenecrolvl4()")
            __main__.ScheduleTask(1.85,"castfemend()")

    if(15 == pc.active_thaumaturgy):
        pc.RemoveItem("item_w_fists")
        __main__.ccmd.player_immobilize=""
        if(clan == 5):
            pc.GiveItem("item_w_zombie_fists")
            consoleutil.console("use item_w_zombie_fists")
            __main__.ScheduleTask(0.45,"passivenecroSamedilvl5()")
            __main__.ScheduleTask(1.85,"castthanatosisend()")
        elif(clan == 7 and pc.IsMale()):
            pc.GiveItem("item_w_mingxiao_spit")
            consoleutil.console("use item_w_mingxiao_spit")
            __main__.ScheduleTask(0.45,"passivenecroNagarajalvl5()")
            __main__.ScheduleTask(1.85,"castmalend()")
        elif(clan == 7 and not pc.IsMale()):
            pc.GiveItem("item_w_tzimisce2_head")
            consoleutil.console("use item_w_tzimisce2_head")
            __main__.ScheduleTask(0.45,"passivenecroNagarajalvl5()")
            __main__.ScheduleTask(1.85,"castfemend()")
        elif(clan == 8 and pc.IsMale()):
            pc.GiveItem("item_w_mingxiao_spit")
            consoleutil.console("use item_w_mingxiao_spit")
            __main__.ScheduleTask(0.45,"passivenecrolvl5()")
            __main__.ScheduleTask(1.85,"castmalend()")
        elif(clan == 8 and not pc.IsMale()):
            pc.GiveItem("item_w_tzimisce2_head")
            consoleutil.console("use item_w_tzimisce2_head")
            __main__.ScheduleTask(0.45,"passivenecrolvl5()")
            __main__.ScheduleTask(1.85,"castfemend()")

#------------------------------ NEW Discipline Koldunism ----------------------------
#NEW Discipline Koldunism  

    if(16 == pc.active_thaumaturgy):
        #__main__.G.Koldunism_Level=1
	#koldunism.Spawn()
        #__main__.ScheduleTask(0.1,"castkoldunism.castDialog()")
        __main__.ScheduleTask(0.0,"castkoldunism.PlayerKoldunicSelectLevel()")

    if(17 == pc.active_thaumaturgy):
        __main__.G.Koldunism_Level=2
	koldunism.Spawn()
        __main__.ScheduleTask(0.1,"castkoldunism.castDialog()")

    if(18 == pc.active_thaumaturgy):
        __main__.G.Koldunism_Level=3
	koldunism.Spawn()
        __main__.ScheduleTask(0.1,"castkoldunism.castDialog()")

    if(19 == pc.active_thaumaturgy):
        __main__.G.Koldunism_Level=4
	koldunism.Spawn()
        __main__.ScheduleTask(0.1,"castkoldunism.castDialog()")

    if(20 == pc.active_thaumaturgy):
        __main__.G.Koldunism_Level=5
	koldunism.Spawn()
        __main__.ScheduleTask(0.1,"castkoldunism.castDialog()")

#------------------------------NEW Discipline Gargoyle  Flight ------------
    if(21 == pc.active_thaumaturgy):
        __main__.ScheduleTask(0.0,"GargoyleFlight()")

#------------------------------NEW Discipline Nihilistics ------------

    if(1 == pc.active_fortitude):
        __main__.ccmd.player_immobilize=""
	__main__.ScheduleTask(0.0,"nihilisticslvl1()")

    if(2 == pc.active_fortitude):
        pc.RemoveItem("item_w_fists")
        __main__.ccmd.player_immobilize=""
        if(pc.IsMale()):
            pc.GiveItem("item_w_mingxiao_spit")
            consoleutil.console("use item_w_mingxiao_spit")
            __main__.ScheduleTask(0.1,"nihilisticslvl2()")
            __main__.ScheduleTask(1.76,"castmalend()")
        else:
            pc.GiveItem("item_w_tzimisce2_head")
            consoleutil.console("use item_w_tzimisce2_head")
            __main__.ScheduleTask(0.1,"nihilisticslvl2()")
            __main__.ScheduleTask(1.76,"castfemend()")

    if(3 == pc.active_fortitude):
        pc.RemoveItem("item_w_fists")
        __main__.ccmd.player_immobilize=""
        if(pc.IsMale()):
            pc.GiveItem("item_w_mingxiao_spit")
            consoleutil.console("use item_w_mingxiao_spit")
            __main__.ScheduleTask(0.45,"nihilisticslvl3()")
            __main__.ScheduleTask(1.85,"castmalend()")
        else:
            pc.GiveItem("item_w_tzimisce2_head")
            consoleutil.console("use item_w_tzimisce2_head")
            __main__.ScheduleTask(0.45,"nihilisticslvl3()")
            __main__.ScheduleTask(1.85,"castfemend()")

    if(4 == pc.active_fortitude):
        pc.RemoveItem("item_w_fists")
        __main__.ccmd.player_immobilize=""
        if(pc.IsMale()):
            pc.GiveItem("item_w_mingxiao_spit")
            consoleutil.console("use item_w_mingxiao_spit")
            __main__.ScheduleTask(1.95,"castmalend()")
        else:
            pc.GiveItem("item_w_tzimisce2_head")
            consoleutil.console("use item_w_tzimisce2_head")
            __main__.ScheduleTask(1.95,"castfemend()")

    if(5 == pc.active_fortitude):
        pc.RemoveItem("item_w_fists")
        __main__.ccmd.player_immobilize=""
        if(pc.IsMale()):
            pc.GiveItem("item_w_mingxiao_spit")
            consoleutil.console("use item_w_mingxiao_spit")
            __main__.ScheduleTask(0.85,"nihilisticslvl5()")
            __main__.ScheduleTask(1.85,"castmalend()")
        else:
            pc.GiveItem("item_w_tzimisce2_head")
            consoleutil.console("use item_w_tzimisce2_head")
            __main__.ScheduleTask(0.85,"nihilisticslvl5()")
            __main__.ScheduleTask(1.85,"castfemend()")

#------------------------------NEW Discipline Obtenebration------------ old fortitude -> new blood_healing
#NEW Discipline Obtenebration animalism
    if(1 == pc.active_blood_healing):
        pc.RemoveItem("item_w_fists")
        __main__.ccmd.player_immobilize=""
        if(pc.IsMale()):
            pc.GiveItem("item_w_mingxiao_spit")
            consoleutil.console("use item_w_mingxiao_spit")
            __main__.ScheduleTask(0.45,"castObteneblvl1Helper()")
            __main__.ScheduleTask(1.85,"castmalend()")
        else:
            pc.GiveItem("item_w_tzimisce2_head")
            consoleutil.console("use item_w_tzimisce2_head")
            __main__.ScheduleTask(0.45,"castObteneblvl1Helper()")
            __main__.ScheduleTask(1.85,"castfemend()")

    if(2 == pc.active_blood_healing):
        pc.RemoveItem("item_w_fists")
        __main__.ccmd.player_immobilize=""
        if(pc.IsMale()):
            pc.GiveItem("item_w_mingxiao_spit")
            consoleutil.console("use item_w_mingxiao_spit")
            __main__.ScheduleTask(1.85,"castmalend()")
        else:
            pc.GiveItem("item_w_tzimisce2_head")
            consoleutil.console("use item_w_tzimisce2_head")
            __main__.ScheduleTask(1.85,"castfemend()")

    if(3 == pc.active_blood_healing):
        pc.RemoveItem("item_w_fists")
        __main__.ccmd.player_immobilize=""
        if(pc.IsMale()):
            pc.GiveItem("item_w_mingxiao_spit")
            consoleutil.console("use item_w_mingxiao_spit")
            __main__.ScheduleTask(0.45,"castObteneblvl3Helper()")
            __main__.ScheduleTask(1.85,"castmalend()")
        else:
            pc.GiveItem("item_w_tzimisce2_head")
            consoleutil.console("use item_w_tzimisce2_head")
            __main__.ScheduleTask(0.45,"castObteneblvl3Helper()")
            __main__.ScheduleTask(1.85,"castfemend()")

    if(4 == pc.active_blood_healing):
        __main__.ScheduleTask(0.1,"castObteneblvl4Helper()")

    if(5 == pc.active_blood_healing):
        __main__.ScheduleTask(0.1,"castObteneblvl5Helper()")

#------------------------------NEW Discipline Vicissitude------------
#Discipline Vicissitude level 1 changeling

    if(1 == pc.active_dementation): 
        if(pc.HasWeaponEquipped("item_w_claws_protean4") or pc.HasWeaponEquipped("item_w_claws_protean5")):
            __main__.ScheduleTask(0.1,"cast1viclvl1aHelper()")
        else:
            __main__.ScheduleTask(0.1,"cast1viclvl1Helper()")  
        #if(pc.HasWeaponEquipped("item_w_claws_protean4")):
        #    __main__.ScheduleTask(0.1,"cast1viclvl1aHelper()")
        #elif(pc.HasWeaponEquipped("item_w_claws_protean5")):
        #    __main__.ScheduleTask(0.1,"cast1viclvl1aHelper()")
        #elif(not pc.HasWeaponEquipped("item_w_claws_protean4") or not pc.HasWeaponEquipped("item_w_claws_protean5")):
        #    __main__.ScheduleTask(0.1,"cast1viclvl1Helper()")

#Discipline Vicissitude level 2 fleshcraft
    if(2 == pc.active_dementation):
        pc.RemoveItem("item_w_fists")
        __main__.ccmd.player_immobilize=""
        if(pc.IsMale()):
            pc.GiveItem("item_w_mingxiao_spit")
            consoleutil.console("use item_w_mingxiao_spit")
            __main__.ScheduleTask(1.85,"castmalend()")
        else:
            pc.GiveItem("item_w_tzimisce2_head")
            consoleutil.console("use item_w_tzimisce2_head")
            __main__.ScheduleTask(1.85,"castfemend()")

#Discipline Vicissitude level 3 bonecraft
    if(3 == pc.active_dementation):
        pc.RemoveItem("item_w_fists")
        __main__.ccmd.player_immobilize=""
        if(pc.IsMale()):
            pc.GiveItem("item_w_mingxiao_spit")
            consoleutil.console("use item_w_mingxiao_spit")
            __main__.ScheduleTask(1.85,"castmalend()")
        else:
            pc.GiveItem("item_w_tzimisce2_head")
            consoleutil.console("use item_w_tzimisce2_head")
            __main__.ScheduleTask(1.85,"castfemend()")

#Discipline Vicissitude level 4 horrid form
    if(4 == pc.active_dementation):
        pcHform = __main__.FindEntityByName("pcHform")
        if(pcHform):
          return
        else:
          __main__.ScheduleTask(0.1,"viclvl4Helper()")
          __main__.ScheduleTask(0.1,"viclvl4Helper1a()")

#Discipline Vicissitude level 5 creating shlazta
    if(5 == pc.active_dementation):
        pc.RemoveItem("item_w_fists")
        __main__.ccmd.player_immobilize=""
        if(pc.IsMale()):
            pc.GiveItem("item_w_mingxiao_spit")
            consoleutil.console("use item_w_mingxiao_spit")
            __main__.ScheduleTask(0.45,"castviclvl5()")
            __main__.ScheduleTask(1.85,"castmalend()")
        else:
            pc.GiveItem("item_w_tzimisce2_head")
            consoleutil.console("use item_w_tzimisce2_head")
            __main__.ScheduleTask(0.45,"castviclvl5()")
            __main__.ScheduleTask(1.85,"castfemend()")

#--------------------------------Disciplines starting END---------------------------------------------
#Disciplines cast end: male, female
def castmalend():
       pc=__main__.FindPlayer()
       pc.RemoveItem("item_w_mingxiao_spit")
       pc.GiveItem("item_w_fists")
       __main__.ccmd.player_mobilize=""
       __main__.ccmd.holster=""

def castfemend():
       pc=__main__.FindPlayer()
       pc.RemoveItem("item_w_tzimisce2_head")
       pc.GiveItem("item_w_fists")
       __main__.ccmd.player_mobilize=""
       __main__.ccmd.holster=""

#--------------------------------Gargoyle  Flight ---------------------------------------------
#Disciplines Gargoyle Flight helper
def GargoyleFlight():
       pc=__main__.FindPlayer()
       GargoyleWings = __main__.FindEntityByName("GargoyleWings")
       __main__.G.Gargoyle_Flight=1                                         
       if(GargoyleWings):
          return
       else:
          __main__.ScheduleTask(25.0,"GargoyleFlight1()")
          consoleutil.console("sv_gravity 100")
          GargoyleWings=__main__.CreateEntityNoSpawn("prop_dynamic_ornament",pc.GetOrigin(),pc.GetAngles())
          GargoyleWings.SetName("GargoyleWings")
          GargoyleWings.SetModel("models/character/monster/rockbiter/wings/rockbiter_wings.mdl")
          __main__.CallEntitySpawn(GargoyleWings)
          GargoyleWings = __main__.FindEntityByName("GargoyleWings")
          if GargoyleWings: GargoyleWings.SetAttached("!player")

def GargoyleFlight1():
       __main__.G.Gargoyle_Flight=0
       GargoyleWings = __main__.FindEntityByName("GargoyleWings") 
       consoleutil.console("sv_gravity 800")
       if GargoyleWings: GargoyleWings.Kill()


#--------------------------------Gargoyle  Flight END---------------------------------------------
#--------------------------------Discipline Serpentis helper ------------------------------
def CastSerpentisOne():
    __main__.ScheduleTask(1.45,"CastSerpentisOne1()")

def CastSerpentisOne1():
    __main__.ccmd.player_mobilize=""

#--------------------------------
def CastSerpentisTwo():
    __main__.ccmd.thirdperson=""
    __main__.ScheduleTask(2.45,"CastSerpentisTwo1()")

def CastSerpentisTwo1():
    __main__.ccmd.player_mobilize=""
    viper = __main__.FindEntityByName("Serpentis_Viper")
    if(viper):
       __main__.FindPlayer().Bloodgain(2)
       consoleutil.console("say Must wait to use that Discipline again")
       #return
    else:
       __main__.FindEntityByName("Serpentis_Spawn_Viper").Spawn()

#--------------------------------
def CastSerpentisThree():
    if(__main__.G.Player_Cobra_Form == 1):
       return
    else:
       __main__.ScheduleTask(0.05,"CastSerpentisThree1a()")

def CastSerpentisThree1a():
    __main__.G.Player_Cobra_Form = 1
    consoleutil.console("use item_w_chang_energy_ball")
    pc=__main__.FindPlayer()
    if(pc.IsMale()):
       __main__.ScheduleTask(0.45,"CastSerpentisThree1()")
       __main__.ScheduleTask(44.75,"CastSerpentisThreeEnd()")
    else:
       __main__.ScheduleTask(0.45,"CastSerpentisThree1()")
       __main__.ScheduleTask(44.5,"CastSerpentisThreeFem()")
       __main__.ScheduleTask(44.75,"CastSerpentisThreeEnd()")

def CastSerpentisThree1():
    __main__.FindPlayer().SetModel("models/weapons/disciplines/serpentis/serpentis_cobra.mdl")
    __main__.ScheduleTask(0.15,"CastSerpentisThree2()")

def CastSerpentisThree2():
    __main__.ccmd.thirdperson=""

def CastSerpentisThreeFem():
    consoleutil.console("vgender_int 0")

def CastSerpentisThreeEnd():
    __main__.ScheduleTask(0.25,"CastSerpentisThreeEnd1()")

def CastSerpentisThreeEnd1():
    __main__.G.Player_Cobra_Form = 0

#--------------------------------
def CastSerpentisFour():
    __main__.ScheduleTask(1.85,"CastSerpentisFour1()")

def CastSerpentisFour1():
    __main__.ccmd.player_mobilize=""

#--------------------------------
def CastSerpentisFive():
    __main__.ScheduleTask(1.75,"CastSerpentisFive1()")

def CastSerpentisFive1():
    __main__.ccmd.player_mobilize=""
    SandStorm = __main__.FindEntityByName("SandStorm")
    if(SandStorm):
       __main__.FindPlayer().Bloodgain(5)
       consoleutil.console("say Must wait to use that Discipline again")
    else:
       castpresence.SummonSandStorm()

#--------------------------------Discipline Presence helper ------------------------------
def PresenceCastOne():
    if(__main__.G.PresenceCounter > 0):
       __main__.FindPlayer().Bloodgain(1)
       consoleutil.console("say Must wait to use that Discipline again")
    else:
       castpresence.ActivatePresenceOne()

def PresenceCastTwo():
    if(__main__.G.PresenceCounter > 0):
       __main__.FindPlayer().Bloodgain(1)
       consoleutil.console("say Must wait to use that Discipline again")
    else:
       castpresence.ActivatePresenceTwo()

def PresenceCastThree():
    if(__main__.G.PresenceCounter > 0):
       __main__.FindPlayer().Bloodgain(1)
       consoleutil.console("say Must wait to use that Discipline again")
    else:
       castpresence.ActivatePresenceThree() 
def PresenceCastFour():
    if(__main__.G.PresenceCounter > 0):
       __main__.FindPlayer().Bloodgain(1)
       consoleutil.console("say Must wait to use that Discipline again")
    else:
       castpresence.ActivatePresenceFour()

def PresenceCastFive():
    if(__main__.G.PresenceCounter > 0):
       __main__.FindPlayer().Bloodgain(1)
       consoleutil.console("say Must wait to use that Discipline again")
    else:
       castpresence.ActivatePresenceFive()

#--------------------------------Discipline chimerstry End------------------------------
#--------------------------------Discipline Obtenebration helper ------------------------------

def castObteneblvl1Helper():
	castnihilistics.ActivateNightshades(1)

def castObteneblvl3Helper():
	castnihilistics.ActivateShadowArms()

#--------------------------------
#Discipline Obtenebration level 4 Black Metamorphosis
def castObteneblvl4Helper():
    if(__main__.G.BlackMetamorphosisCounter > 0):
       return
    else:
       __main__.ScheduleTask(0.1,"castObteneblvl4Helper1()")
       __main__.ScheduleTask(0.15,"castObteneblvl4tentacles()")
       __main__.cvar.sv_gravity=3000

#Obtenebration level 4 Timer 
def castObteneblvl4Helper1():
    castObteneblvl4HelperAura()
    __main__.G.BlackMetamorphosisCounter = __main__.G.BlackMetamorphosisCounter + 1
     
    if(__main__.G.BlackMetamorphosisCounter >= 15):
        __main__.ScheduleTask(0.1,"castObteneblvl4Helper2()")
	print "exit"
	__main__.cvar.sv_gravity=800
        __main__.G.BlackMetamorphosisCounter = 0
    else:
        __main__.ScheduleTask(1.05,"castObteneblvl4Helper1()") 


def castObteneblvl4Helper2():
    __main__.FindPlayer().ClearActiveDisciplines()
    __main__.FindEntityByName("pcTentacles").Kill()

def castObteneblvl4HelperAura():
    pc=__main__.FindPlayer()
    aura = __main__.FindEntityByName("BlackMetamorphosis")
    o = pc.GetOrigin()
    no= (o[0],o[1],o[2]+35)
    aura.SetOrigin(no)
    __main__.ScheduleTask(0.1,"castObteneblvl4HelperAura1()")

def castObteneblvl4HelperAura1():
    __main__.FindEntityByName("BlackMetamorphosis").Explode()

def castObteneblvl4tentacles():
    pc=__main__.FindPlayer()
    pcTentacles=__main__.CreateEntityNoSpawn("prop_dynamic_ornament",pc.GetOrigin(),pc.GetAngles())
    pcTentacles.SetName("pcTentacles")
    pcTentacles.SetModel("models/weapons/disciplines/obtenebration/metamorphosis.mdl")
    __main__.CallEntitySpawn(pcTentacles)
    pcTentacles = __main__.FindEntityByName("pcTentacles")
    if pcTentacles: pcTentacles.SetAttached("!player")

#--------------------------------
#Discipline Obtenebration level 5 Shadow form
def castObteneblvl5Helper():
       pevents = __main__.FindEntitiesByClass("events_player")
       pevents[0].MakePlayerUnkillable()
       __main__.ccmd.thirdperson=""
       __main__.cvar.sv_gravity=100
       __main__.cvar.sv_sneakscale=6.5
       __main__.G.Player_Shadow_Form = 1
       __main__.ScheduleTask(0.1,"castObteneblvl5Helper1()")

def castObteneblvl5Helper1():
        pc=__main__.FindPlayer()       
        if pc.IsMale():
            pc.SetModel("models/weapons/disciplines/obtenebration/nightshades.mdl")
            __main__.ScheduleTask(15.0,"castObteneblvl5Helper2a()")
        else:
            pc.SetModel("models/weapons/disciplines/obtenebration/nightshades.mdl")
            __main__.ScheduleTask(14.5,"castObteneblvl5Helper2b()")

def castObteneblvl5Helper2a():
       pevents = __main__.FindEntitiesByClass("events_player")
       pevents[0].MakePlayerKillable()
       __main__.cvar.sv_sneakscale=2.3
       __main__.cvar.sv_gravity=800
       __main__.G.Player_Shadow_Form = 0

def castObteneblvl5Helper2b():
       pevents = __main__.FindEntitiesByClass("events_player")
       pevents[0].MakePlayerKillable()
       consoleutil.console("vgender_int 0")
       __main__.cvar.sv_sneakscale=2.3
       __main__.cvar.sv_gravity=800
       __main__.G.Player_Shadow_Form = 0


#--------------------------------Discipline Vicissitude helper ------------------------------
#Discipline Vicissitude level 5 creating shlazta
def castviclvl5():
        pc=__main__.FindPlayer()
        __main__.ccmd.player_immobilize=""
        if(pc.HasItem("item_w_claws_protean4") and pc.HasItem("item_w_claws_protean5")):
            __main__.ScheduleTask(2.5,"castviclvl5Helper()")
        else:
            __main__.ScheduleTask(2.5,"cast1viclvl5Helper()")

def castviclvl5Helper():
    pc=__main__.FindPlayer()
    viper = __main__.FindEntityByName("Serpentis_Viper")
    if(viper):
       __main__.FindPlayer().Bloodgain(5)
       consoleutil.console("say Must wait to use that Discipline again")
       #return
    else:
       __main__.FindEntityByName("Serpentis_Spawn_Viper").Spawn()
       pc.RemoveItem("item_w_claws_protean4")
       pc.RemoveItem("item_w_claws_protean5")
       #pc.ClearActiveDisciplines()
       __main__.ccmd.player_mobilize=""
       #__main__.ccmd.holster=""

def castviclvl5HelperX():
       pc=__main__.FindPlayer()
       #castthanatosislvl3.ActivateSzlachtaSummon(1)
       __main__.FindEntityByName("Serpentis_Spawn_Viper").Spawn()
       pc.RemoveItem("item_w_claws_protean4")
       pc.RemoveItem("item_w_claws_protean5")
       pc.ClearActiveDisciplines()
       __main__.ccmd.player_mobilize=""
       __main__.ccmd.holster=""

def cast1viclvl5Helper():
       consoleutil.console("say I need flesh and skeleton for the ritual")
       __main__.FindPlayer().Bloodgain(4)
       __main__.ccmd.player_mobilize=""
       __main__.ccmd.holster=""

#------------------------------------------------------------------
#Discipline Vicissitude level 1 Seduction Helper
def cast1viclvl1Helper():
       consoleutil.console("use item_w_mingxiao_spit")
       __main__.ccmd.thirdperson=""
       __main__.cvar.hidehud=1
       __main__.ScheduleTask(0.1,"cast2viclvl1Helper()")

def cast2viclvl1Helper():
        __main__.FindPlayer().GiveItem("item_w_gargoyle_fist")
        __main__.ScheduleTask(0.1,"cast3viclvl1Helper()")

def cast3viclvl1Helper():
        pc=__main__.FindPlayer()        
        if pc.IsMale():
            pc.SetModel("models/character/pc/male/toreador/armor0/toreador_male_armor_0.mdl")
            __main__.ScheduleTask(15.0,"cast4viclvl1Helper()")
        else:
            pc.SetModel("models/character/pc/female/toreador/armor0/toreador_female_armor_0.mdl")
            __main__.ScheduleTask(15.0,"cast4viclvl1Helper()")

def cast4viclvl1Helper():
       __main__.FindPlayer().RemoveItem("item_w_gargoyle_fist")
       __main__.FindPlayer().GiveItem("item_w_hengeyokai_fist")
       __main__.ScheduleTask(0.15,"cast5viclvl1Helper()")

def cast5viclvl1Helper():
       __main__.FindPlayer().RemoveItem("item_w_hengeyokai_fist")
       __main__.cvar.hidehud=0

#------------------------------------------------------------------
#Discipline Vicissitude level 1 Intimidation Helper
def cast1viclvl1aHelper():
       consoleutil.console("use item_w_mingxiao_spit")
       __main__.ccmd.thirdperson=""
       __main__.cvar.hidehud=1
       __main__.ScheduleTask(0.1,"cast1viclvl1aHelper1()")

def cast1viclvl1aHelper1():
       __main__.FindPlayer().GiveItem("item_w_manbat_claw")
       __main__.ScheduleTask(0.1,"cast1viclvl1aHelper2()")

def cast1viclvl1aHelper2():
       pc=__main__.FindPlayer()        
       if pc.IsMale():
           pc.SetModel("models/character/pc/male/nosferatu/armor0/nosferatu.mdl")
           __main__.ScheduleTask(15.0,"cast1viclvl1aHelper3()")
       else:
           pc.SetModel("models/character/pc/female/nosferatu/armor0/nosferatu_female_armor_0.mdl")
           __main__.ScheduleTask(15.0,"cast1viclvl1aHelper3()")

def cast1viclvl1aHelper3():
       __main__.FindPlayer().RemoveItem("item_w_manbat_claw")
       __main__.FindPlayer().GiveItem("item_w_mingxiao_melee")
       __main__.ScheduleTask(0.15,"cast1viclvl1aHelper4()")

def cast1viclvl1aHelper4():
       __main__.FindPlayer().RemoveItem("item_w_mingxiao_melee")
       __main__.cvar.hidehud=0
       consoleutil.console("inven_wield 52")

#------------------------------------------------------------------
#Discipline Vicissitude level 4 horrid form Helper
def viclvl4Helper():
       __main__.ccmd.thirdperson=""
       __main__.ccmd.RemoveFeed=""
       __main__.cvar.hidehud=1
       __main__.G.Player_Shadow_Form = 1
       __main__.ScheduleTask(0.1,"viclvl4Helper1()")

def viclvl4Helper1():
        pc=__main__.FindPlayer()        
        if pc.IsMale():
            pc.SetModel("models/weapons/disciplines/Viscicitude/horrid form/male_form.mdl")
            __main__.ScheduleTask(0.1,"viclvl4Helper2()")
        else:
            pc.SetModel("models/weapons/disciplines/Viscicitude/horrid form/female_form.mdl")
            __main__.ScheduleTask(0.1,"viclvl4Helper2()")

def viclvl4Helper1a():
       pc=__main__.FindPlayer()
       pcHform = __main__.FindEntityByName("pcHform")                                         
       if(pcHform):
          return
       else:
          pcHform=__main__.CreateEntityNoSpawn("prop_dynamic_ornament",pc.GetOrigin(),pc.GetAngles())
          pcHform.SetName("pcHform")
          #pcHform.SetModel("models/character/monster/andrei/andrei.mdl")
          pcHform.SetModel("models/weapons/disciplines/Viscicitude/szlachta2.mdl")
          __main__.CallEntitySpawn(pcHform)
          pcHform = __main__.FindEntityByName("pcHform")
          if pcHform: pcHform.SetAttached("!player")

def viclvl4Helper2():
       consoleutil.console("player_sequence ACT_HOWL")
       __main__.ScheduleTask(35.0,"viclvl4Helper3()")

def viclvl4Helper3():
       pc=__main__.FindPlayer()
       pcHform = __main__.FindEntityByName("pcHform")
       pcHform.Kill()
       __main__.cvar.hidehud=0
       __main__.ccmd.RestoreFeed=""
       __main__.G.Player_Shadow_Form = 0

#--------------------------------Discipline Vicissitude helper END-------------------
#--------------------------------------------PASSIVE animalism---------------------------------
#PASSIVE animalism LEVEL 1
def passiveanimlvl1():
    	  pc=__main__.FindPlayer()
          consoleutil.console("player_sequence seductive_attacker_shortvictim_front_release_standing")
          __main__.ScheduleTask(0.85,"passiveanimlvl1a()")

def passiveanimlvl1a():
	  castanimalism.SummonRavens()

#PASSIVE animalism LEVEL 2
def passiveanimlvl2():
    	  pc=__main__.FindPlayer()
          consoleutil.console("player_sequence burning_outof")
	  castanimalism.SummonRats()

#PASSIVE animalism LEVEL 3
def passiveanimlvl3():
    	  pc=__main__.FindPlayer()
          consoleutil.console("player_sequence waveover01")
	  castanimalism.SummonDogMain()

#PASSIVE animalism LEVEL 4
def passiveanimlvl4():
          consoleutil.console("player_sequence howl")
          __main__.ScheduleTask(0.95,"passiveanimlvl4a()")

def passiveanimlvl4a():
	  castanimalism.SummonWolf()

#PASSIVE animalism LEVEL 5
def passiveanimlvl5():
          consoleutil.console("player_sequence howl")
	  __main__.ScheduleTask(0.95,"passiveanimlvl5a()")

def passiveanimlvl5a():
	  castanimalism.Activate3Summon(1)

def passiveanimlvl1end():
       pc=__main__.FindPlayer()
       pc.RemoveItem("item_w_mingxiao_spit")
       pc.GiveItem("item_w_fists")
       __main__.ccmd.player_mobilize=""
       __main__.ccmd.holster=""

#---------------------------------------------PASSIVE Necromancy---------------------------------
#PASSIVE Necromancy LEVEL 1
def passivenecrolvl1():
    	  pc=__main__.FindPlayer()
          consoleutil.console("player_sequence d_thaum_idle")
          __main__.ScheduleTask(0.85,"passivenecrolvl1a()")

def passivenecrolvl1a():
          consoleutil.console("player_sequence d_thaum_idle")
	  castnecromancy.Activate1Summon(1)

#PASSIVE Necromancy LEVEL 2
def passivenecrolvl2():
    	  pc=__main__.FindPlayer()
          consoleutil.console("player_sequence d_thaum_idle")
          __main__.ScheduleTask(0.85,"passivenecrolvl2a()")

def passivenecrolvl2a():
          consoleutil.console("player_sequence d_thaum_idle")
	  castnecromancy.Activate4Summon(3)

#-------------------------------samedi and nagaraja 2 level--------------------------------
#PASSIVE Necromancy LEVEL 2
def passivenecroSamedilvl2():
    	  pc=__main__.FindPlayer()
          consoleutil.console("player_sequence d_thaum_idle")
          __main__.ScheduleTask(0.85,"passivenecroSamedilvl2a()")

def passivenecroSamedilvl2a():
          consoleutil.console("player_sequence d_thaum_idle")
	  castnecromancy.Activate4Summon(2)

#-------------------------------giovanni 3 level--------------------------
#PASSIVE Necromancy LEVEL 3
def passivenecrolvl3():
    	  pc=__main__.FindPlayer()
          consoleutil.console("player_sequence d_thaum_idle")
          __main__.ScheduleTask(0.85,"passivenecrolvl3a()")

def passivenecrolvl3a():
          consoleutil.console("player_sequence d_thaum_idle")
	  castnecromancy.Activate5Summon(3)

#-------------------------------samedi and nagaraja 3 level--------------------------------
#PASSIVE Necromancy LEVEL 3
def passivenecroSamedilvl3():
    	  pc=__main__.FindPlayer()
          consoleutil.console("player_sequence d_thaum_idle")
          __main__.ScheduleTask(0.85,"passivenecroSamedilvl3a()")

def passivenecroSamedilvl3a():
          consoleutil.console("player_sequence d_thaum_idle")
	  castnecromancy.Activate5Summon(2)

#-------------------------------giovanni 4 level---------------------------
#PASSIVE Necromancy LEVEL 4
def passivenecrolvl4():
    	  pc=__main__.FindPlayer()
          consoleutil.console("player_sequence d_thaum_idle")
          __main__.ScheduleTask(0.85,"passivenecrolvl4a()")

def passivenecrolvl4a():
          consoleutil.console("player_sequence d_thaum_idle")
	  castnecromancy.Activate5Summon(3)
	  castnecromancy.Activate6Summon(1)

#-------------------------------samedi 4 level-----------------------------
#PASSIVE Necromancy LEVEL 4
def passivenecroSamedilvl4():
    	  pc=__main__.FindPlayer()
          consoleutil.console("player_sequence d_thaum_idle")
          __main__.ScheduleTask(0.85,"passivenecroSamedilvl4a()")

def passivenecroSamedilvl4a():
          consoleutil.console("player_sequence d_thaum_idle")
	  castnecromancy.Activate5Summon(3)

#-------------------------------Nagaraja 4 level--------------------------------
#PASSIVE Necromancy LEVEL 4
def passivenecroNagarajalvl4():
    	  pc=__main__.FindPlayer()
          consoleutil.console("player_sequence d_thaum_idle")
          __main__.ScheduleTask(0.85,"passivenecroNagarajalvl4a()")

def passivenecroNagarajalvl4a():
          consoleutil.console("player_sequence d_thaum_idle")
	  #castnecromancy.Activate5Summon(2)
	  castnecromancy.SummonNagarajaGhost()

#-------------------------------giovanni 5 level----------------------------
#PASSIVE Necromancy LEVEL 5
def passivenecrolvl5():
    	  pc=__main__.FindPlayer()
          consoleutil.console("player_sequence d_thaum_idle")
          __main__.ScheduleTask(0.85,"passivenecrolvl5a()")

def passivenecrolvl5a():
          consoleutil.console("player_sequence d_thaum_idle")
	  castnecromancy.Activate5Summon(3)
	  castnecromancy.Activate7Summon(1)

#-------------------------------samedi 5 level-----------------------------
#PASSIVE Necromancy LEVEL 5
def passivenecroSamedilvl5():
    	  pc=__main__.FindPlayer()
          consoleutil.console("player_sequence d_thaum_idle")
          __main__.ScheduleTask(0.85,"passivenecroSamedilvl5a()")

def passivenecroSamedilvl5a():
          consoleutil.console("player_sequence d_thaum_idle")
	  #castnecromancy.Activate5Summon(3)
	  castnecromancy.SummonSkeletonMain()

#-------------------------------Nagaraja 5 level----------------------------
#PASSIVE Necromancy LEVEL 5
def passivenecroNagarajalvl5():
    	  pc=__main__.FindPlayer()
          consoleutil.console("player_sequence d_thaum_idle")
          __main__.ScheduleTask(0.85,"passivenecroNagarajalvl5a()")

def passivenecroNagarajalvl5a():
          consoleutil.console("player_sequence d_thaum_idle")
	  #castnecromancy.Activate5Summon(2)
	  castnecromancy.SummonSpecterMain()

#-------------------------------------------------------------THANATOSIS----------------------------------
#Discipline Thanatosis level 1 Helper
def thanatosislvl1():
       consoleutil.console("use item_w_mingxiao_spit")
       __main__.ScheduleTask(0.1,"thanatosislvl1a()")

def thanatosislvl1a():
       world=__main__.FindEntitiesByName("world")[0]
       world.SetNosferatuTolerant(1)
       __main__.ScheduleTask(0.1,"thanatosislvl1b()")

def thanatosislvl1b():
        pc=__main__.FindPlayer()        
        if(pc.IsMale()):
            pc.SetModel("models/character/pc/male/samedi/samedi_male_thanatosis.mdl")
            __main__.ScheduleTask(15.0,"thanatosislvl1c()")
        else:
            if(pc.GetID() == "models/character/npc/unique/chinatown/yukie_n_e"):
                pc.SetModel("models/character/npc/unique/chinatown/yukie/yukie.mdl")
                __main__.ScheduleTask(15.0,"thanatosislvl1c()")
                __main__.ScheduleTask(15.5,"thanatosisYukie()")
            else:
                if(pc.GetID() == "models/character/npc/unique/santa_monica/heather_n_e"):
                    pc.SetModel("models/character/pc/female/samedi/samedi_female_thanatosis.mdl")
                    __main__.ScheduleTask(15.0,"thanatosislvl1c()")
                    __main__.ScheduleTask(15.5,"thanatosisHeather()")
                else:
                    pc.SetModel("models/character/pc/female/samedi/samedi_female_thanatosis.mdl")
                    __main__.ScheduleTask(15.0,"thanatosislvl1c()")

def thanatosislvl1c():
       world=__main__.FindEntitiesByName("world")[0]
       world.SetNosferatuTolerant(0)
       __main__.ScheduleTask(0.1,"thanatosislvl1d()")

def thanatosislvl1d():
       consoleutil.console("hidehud 0")
       __main__.ScheduleTask(0.1,"thanatosislvl1e()")

def thanatosislvl1e():
       pc=__main__.FindPlayer()
       pc.RemoveItem("item_w_mingxiao_spit")
       pc.GiveItem("item_w_fists")
       consoleutil.console("use item_w_fists")
       __main__.ScheduleTask(0.1,"thanatosislvl1f()")

def thanatosislvl1f():
       consoleutil.console("player_sequence land_hard")
       __main__.ccmd.holster=""

def thanatosisYukie():
       __main__.FindPlayer().SetModel("models/character/npc/unique/chinatown/yukie_n_e/yukie_n_e.mdl")

def thanatosisHeather():
       __main__.FindPlayer().SetModel("models/character/npc/unique/santa_monica/heather_n_e/heather_n_e.mdl")

#-------------------------
#Discipline Thanatosis level 2 Helper
def thanatosislvl2():
       consoleutil.console("player_sequence d_thaum_idle")
       __main__.ScheduleTask(1.25,"thanatosislvl2a()")

def thanatosislvl2a():
       __main__.ccmd.holster=""

#-------------------------
#Discipline Thanatosis level 3 Helper
def thanatosislvl3():
        __main__.G.Player_Ashes_Form = 1
        consoleutil.console("use item_w_mingxiao_spit")
	castthanatosislvl3.ActivatetThanatosis(1)
        __main__.ScheduleTask(0.1,"thanatosislvl3a()")

def thanatosislvl3a():
        pc=__main__.FindPlayer()        
        if pc.IsMale():
            pc.SetModel("models/null.mdl")
            __main__.ScheduleTask(11.85,"thanatosislvl3b()")
        else:
            if(pc.GetID() == "models/character/npc/unique/chinatown/yukie_n_e"):
                pc.SetModel("models/null.mdl")
                __main__.ScheduleTask(11.85,"thanatosislvl3bf()")
                __main__.ScheduleTask(11.9,"thanatosisYukie()")
            else:
                if(pc.GetID() == "models/character/npc/unique/santa_monica/heather_n_e"):
                    pc.SetModel("models/null.mdl")
                    __main__.ScheduleTask(11.85,"thanatosislvl3bf()")
                    __main__.ScheduleTask(11.9,"thanatosisHeather()")
                else:
                    pc.SetModel("models/null.mdl")
                    __main__.ScheduleTask(11.85,"thanatosislvl3bf()")

def thanatosislvl3bf():
       consoleutil.console("vgender_int 0")
       __main__.ScheduleTask(0.1,"thanatosislvl3b()")

def thanatosislvl3b():
       consoleutil.console("hidehud 0")
       __main__.ScheduleTask(0.1,"thanatosislvl3c()")

def thanatosislvl3c():
       pc=__main__.FindPlayer()
       pc.RemoveItem("item_w_mingxiao_spit")
       pc.GiveItem("item_w_fists")
       __main__.ccmd.player_mobilize=""
       __main__.ccmd.holster=""
       __main__.G.Player_Ashes_Form = 0        

#-------------------------
#Discipline Thanatosis level 4 Helper
def thanatosislvl4():
       consoleutil.console("player_sequence d_thaum_idle")
       __main__.ScheduleTask(1.25,"thanatosislvl4a()")

def thanatosislvl4a():
       __main__.ccmd.holster=""

#-------------------------
#Discipline Thanatosis level 5 Helper
def thanatosislvl5():
       consoleutil.console("player_sequence d_thaum_idle")
       __main__.ScheduleTask(1.25,"thanatosislvl5a()")

def thanatosislvl5a():
       __main__.ccmd.holster=""

#-------------------------
def castthanatosisend():
       pc=__main__.FindPlayer()
       pc.RemoveItem("item_w_zombie_fists")
       pc.GiveItem("item_w_fists")
       __main__.ccmd.player_mobilize=""
       __main__.ccmd.holster=""

#-------------------------------------------- OLD KOLDUNISM ---------------------------------
#cast KOLDUNISM particles helper
def CastKoldunismHelper():
       pc=__main__.FindPlayer()
       pc.PlayHUDParticle("d_koldunism_hud-emitter")
       koldunist =__main__.CreateEntityNoSpawn("npc_VHuman",pc.GetOrigin(),pc.GetAngles())
       koldunist.SetName("koldunist")
       koldunist.SetModel("models/character/monster/undead/undead_male_sceleton.mdl")
       __main__.CallEntitySpawn(koldunist)
       koldunist = __main__.FindEntityByName("koldunist")
       if koldunist:
           koldunist.SetParent("!player")
           koldunist.SetOrigin(pc.GetOrigin())
           koldunist.SetAngles(pc.GetAngles())
           koldunist.SetModel("models/character/monster/undead/undead_male_sceleton.mdl")
    	   koldunist.SetScriptedDiscipline("divine_vision 1")
           __main__.ScheduleTask(1.0,"CastKoldunismHelper1()")

def CastKoldunismHelper1():
       koldunist = __main__.FindEntityByName("koldunist")
       koldunist.ClearParent()
       koldunist.Kill()
#-------------------------------------------- 
#cast KOLDUNISM LEVEL 1 A
def CastKoldunismlvl1_1():
    	pc=__main__.FindPlayer()
        pc.RemoveItem("item_w_fists")
        __main__.ccmd.player_immobilize=""
	CastKoldunismHelper()
        if(pc.IsMale()):
            pc.GiveItem("item_w_mingxiao_spit")
            consoleutil.console("use item_w_mingxiao_spit")
            __main__.ScheduleTask(0.45,"koldunismlvl1_1()")
            __main__.ScheduleTask(1.85,"castmalend()")
        else:
            pc.GiveItem("item_w_tzimisce2_head")
            consoleutil.console("use item_w_tzimisce2_head")
            __main__.ScheduleTask(0.45,"koldunismlvl1_1()")
            __main__.ScheduleTask(1.85,"castfemend()")

def koldunismlvl1_1():
    	  pc=__main__.FindPlayer()
          consoleutil.console("player_sequence d_thaum_idle")
          __main__.ScheduleTask(0.85,"koldunismlvl1_1a()")

def koldunismlvl1_1a():
	  castkoldunism.Activate1Summon(1)

#--------------------------------------------
#cast KOLDUNISM LEVEL 1 B
def CastKoldunismlvl1_2():
    	pc=__main__.FindPlayer()
        pc.RemoveItem("item_w_fists")
        __main__.ccmd.player_immobilize=""
	CastKoldunismHelper()
        if(pc.IsMale()):
            pc.GiveItem("item_w_mingxiao_spit")
            consoleutil.console("use item_w_mingxiao_spit")
            __main__.ScheduleTask(0.45,"koldunismlvl1_2()")
            __main__.ScheduleTask(1.85,"castmalend()")
        else:
            pc.GiveItem("item_w_tzimisce2_head")
            consoleutil.console("use item_w_tzimisce2_head")
            __main__.ScheduleTask(0.45,"koldunismlvl1_2()")
            __main__.ScheduleTask(1.85,"castfemend()")

def koldunismlvl1_2():
    	  pc=__main__.FindPlayer()
          consoleutil.console("player_sequence d_thaum_idle")
          __main__.ScheduleTask(0.85,"koldunismlvl1_2a()")

def koldunismlvl1_2a():
	  castkoldunism.Activate2Summon(1)


#--------------------------------------------
#cast KOLDUNISM LEVEL 1 C
def CastKoldunismlvl1_3():
    	pc=__main__.FindPlayer()
        pc.RemoveItem("item_w_fists")
        __main__.ccmd.player_immobilize=""
	CastKoldunismHelper()
        if(pc.IsMale()):
            pc.GiveItem("item_w_mingxiao_spit")
            consoleutil.console("use item_w_mingxiao_spit")
            __main__.ScheduleTask(0.45,"koldunismlvl1_3()")
            __main__.ScheduleTask(1.85,"castmalend()")
        else:
            pc.GiveItem("item_w_tzimisce2_head")
            consoleutil.console("use item_w_tzimisce2_head")
            __main__.ScheduleTask(0.45,"koldunismlvl1_3()")
            __main__.ScheduleTask(1.85,"castfemend()")

def koldunismlvl1_3():
    	  pc=__main__.FindPlayer()
          consoleutil.console("player_sequence d_thaum_idle")
          __main__.ScheduleTask(0.85,"koldunismlvl1_3a()")

def koldunismlvl1_3a():
	  castkoldunism.Activate3Summon(1)

#-------------------------------------------- LEVEL 2 ------------------------
#cast KOLDUNISM LEVEL 2 A
def CastKoldunismlvl2_1():
    	pc=__main__.FindPlayer()
        pc.RemoveItem("item_w_fists")
        __main__.ccmd.player_immobilize=""
	CastKoldunismHelper()
        if(pc.IsMale()):
            pc.GiveItem("item_w_mingxiao_spit")
            consoleutil.console("use item_w_mingxiao_spit")
            __main__.ScheduleTask(0.45,"koldunismlvl2_1()")
            __main__.ScheduleTask(1.85,"castmalend()")
        else:
            pc.GiveItem("item_w_tzimisce2_head")
            consoleutil.console("use item_w_tzimisce2_head")
            __main__.ScheduleTask(0.45,"koldunismlvl2_1()")
            __main__.ScheduleTask(1.85,"castfemend()")

def koldunismlvl2_1():
    	  pc=__main__.FindPlayer()
          consoleutil.console("player_sequence d_thaum_idle")
          __main__.ScheduleTask(0.85,"koldunismlvl2_1a()")

def koldunismlvl2_1a():
	  castkoldunism.Activate4Summon(1)
#-------------------------------------------- 
#cast KOLDUNISM LEVEL 2 B
def CastKoldunismlvl2_2():
    	pc=__main__.FindPlayer()
        pc.RemoveItem("item_w_fists")
        __main__.ccmd.player_immobilize=""
	CastKoldunismHelper()
        if(pc.IsMale()):
            pc.GiveItem("item_w_mingxiao_spit")
            consoleutil.console("use item_w_mingxiao_spit")
            __main__.ScheduleTask(0.45,"koldunismlvl2_2()")
            __main__.ScheduleTask(1.85,"castmalend()")
        else:
            pc.GiveItem("item_w_tzimisce2_head")
            consoleutil.console("use item_w_tzimisce2_head")
            __main__.ScheduleTask(0.45,"koldunismlvl2_2()")
            __main__.ScheduleTask(1.85,"castfemend()")

def koldunismlvl2_2():
    	  pc=__main__.FindPlayer()
          consoleutil.console("player_sequence d_thaum_idle")
          __main__.ScheduleTask(0.85,"koldunismlvl2_2a()")

def koldunismlvl2_2a():
	  castkoldunism.Activate5Summon(1)

#-------------------------------------------- 
#cast KOLDUNISM LEVEL 2 C
def CastKoldunismlvl2_3():
    	pc=__main__.FindPlayer()
        pc.RemoveItem("item_w_fists")
        __main__.ccmd.player_immobilize=""
	CastKoldunismHelper()
        if(pc.IsMale()):
            pc.GiveItem("item_w_mingxiao_spit")
            consoleutil.console("use item_w_mingxiao_spit")
            __main__.ScheduleTask(0.45,"koldunismlvl2_3()")
            __main__.ScheduleTask(1.85,"castmalend()")
        else:
            pc.GiveItem("item_w_tzimisce2_head")
            consoleutil.console("use item_w_tzimisce2_head")
            __main__.ScheduleTask(0.45,"koldunismlvl2_3()")
            __main__.ScheduleTask(1.85,"castfemend()")

def koldunismlvl2_3():
    	  pc=__main__.FindPlayer()
          consoleutil.console("player_sequence d_thaum_idle")
          __main__.ScheduleTask(0.85,"koldunismlvl2_3a()")

def koldunismlvl2_3a():
	  castkoldunism.Activate6Summon(1)

#-------------------------------------------- LEVEL 3 ------------------------
#cast KOLDUNISM LEVEL 3 A
def CastKoldunismlvl3_1():
    	pc=__main__.FindPlayer()
        pc.RemoveItem("item_w_fists")
        __main__.ccmd.player_immobilize=""
	CastKoldunismHelper()
        if(pc.IsMale()):
            pc.GiveItem("item_w_mingxiao_spit")
            consoleutil.console("use item_w_mingxiao_spit")
            __main__.ScheduleTask(0.45,"koldunismlvl3_1()")
            __main__.ScheduleTask(1.85,"castmalend()")
        else:
            pc.GiveItem("item_w_tzimisce2_head")
            consoleutil.console("use item_w_tzimisce2_head")
            __main__.ScheduleTask(0.45,"koldunismlvl3_1()")
            __main__.ScheduleTask(1.85,"castfemend()")

def koldunismlvl3_1():
    	  pc=__main__.FindPlayer()
          consoleutil.console("player_sequence d_thaum_idle")
          __main__.ScheduleTask(0.85,"koldunismlvl3_1a()")

def koldunismlvl3_1a():
	  castkoldunism.Activate7Summon(1)

#--------------------------------------
#cast KOLDUNISM LEVEL 3 B
def CastKoldunismlvl3_2():
    	pc=__main__.FindPlayer()
        pc.RemoveItem("item_w_fists")
        __main__.ccmd.player_immobilize=""
	CastKoldunismHelper()
        if(pc.IsMale()):
            pc.GiveItem("item_w_mingxiao_spit")
            consoleutil.console("use item_w_mingxiao_spit")
            __main__.ScheduleTask(0.45,"koldunismlvl3_2()")
            __main__.ScheduleTask(1.85,"castmalend()")
        else:
            pc.GiveItem("item_w_tzimisce2_head")
            consoleutil.console("use item_w_tzimisce2_head")
            __main__.ScheduleTask(0.45,"koldunismlvl3_2()")
            __main__.ScheduleTask(1.85,"castfemend()")

def koldunismlvl3_2():
    	  pc=__main__.FindPlayer()
          consoleutil.console("player_sequence d_thaum_idle")
          __main__.ScheduleTask(0.85,"koldunismlvl3_2a()")

def koldunismlvl3_2a():
	  castkoldunism.Activate8Summon(1)

#-------------------------------------------- LEVEL 4 -------------------
#cast KOLDUNISM LEVEL 4 A
def CastKoldunismlvl4_1():
    	pc=__main__.FindPlayer()
        pc.RemoveItem("item_w_fists")
        __main__.ccmd.player_immobilize=""
	CastKoldunismHelper()
        if(pc.IsMale()):
            pc.GiveItem("item_w_mingxiao_spit")
            consoleutil.console("use item_w_mingxiao_spit")
            __main__.ScheduleTask(0.45,"koldunismlvl4_1()")
            __main__.ScheduleTask(1.85,"castmalend()")
        else:
            pc.GiveItem("item_w_tzimisce2_head")
            consoleutil.console("use item_w_tzimisce2_head")
            __main__.ScheduleTask(0.45,"koldunismlvl4_1()")
            __main__.ScheduleTask(1.85,"castfemend()")

def koldunismlvl4_1():
    	  pc=__main__.FindPlayer()
          consoleutil.console("player_sequence d_thaum_idle")
          __main__.ScheduleTask(0.85,"koldunismlvl4_1a()")

def koldunismlvl4_1a():
	  castkoldunism.Activate9Summon(1)

#--------------------------------------
#cast KOLDUNISM LEVEL 4 B
def CastKoldunismlvl4_2():
    	pc=__main__.FindPlayer()
        pc.RemoveItem("item_w_fists")
        __main__.ccmd.player_immobilize=""
	CastKoldunismHelper()
        if(pc.IsMale()):
            pc.GiveItem("item_w_mingxiao_spit")
            consoleutil.console("use item_w_mingxiao_spit")
            __main__.ScheduleTask(0.45,"koldunismlvl4_2()")
            __main__.ScheduleTask(1.85,"castmalend()")
        else:
            pc.GiveItem("item_w_tzimisce2_head")
            consoleutil.console("use item_w_tzimisce2_head")
            __main__.ScheduleTask(0.45,"koldunismlvl4_2()")
            __main__.ScheduleTask(1.85,"castfemend()")

def koldunismlvl4_2():
    	  pc=__main__.FindPlayer()
          consoleutil.console("player_sequence d_thaum_idle")
          __main__.ScheduleTask(0.85,"koldunismlvl4_2a()")

def koldunismlvl4_2a():
	  castkoldunism.Activate10Summon(1)


#-------------------------------------------- LEVEL 5 ------------------------
#cast KOLDUNISM LEVEL 5 A
def CastKoldunismlvl5_1():
    	pc=__main__.FindPlayer()
        pc.RemoveItem("item_w_fists")
        __main__.ccmd.player_immobilize=""
	CastKoldunismHelper()
        if(pc.IsMale()):
            pc.GiveItem("item_w_mingxiao_spit")
            consoleutil.console("use item_w_mingxiao_spit")
            __main__.ScheduleTask(0.45,"koldunismlvl5_1()")
            __main__.ScheduleTask(1.85,"castmalend()")
        else:
            pc.GiveItem("item_w_tzimisce2_head")
            consoleutil.console("use item_w_tzimisce2_head")
            __main__.ScheduleTask(0.45,"koldunismlvl5_1()")
            __main__.ScheduleTask(1.85,"castfemend()")

def koldunismlvl5_1():
    	  pc=__main__.FindPlayer()
          consoleutil.console("player_sequence d_thaum_idle")
          __main__.ScheduleTask(0.85,"koldunismlvl5_1a()")

def koldunismlvl5_1a():
	  castkoldunism.Activate11Summon(1)

#--------------------------------------
#cast KOLDUNISM LEVEL 5 B
def CastKoldunismlvl5_2():
    	pc=__main__.FindPlayer()
        pc.RemoveItem("item_w_fists")
        __main__.ccmd.player_immobilize=""
	CastKoldunismHelper()
        if(pc.IsMale()):
            pc.GiveItem("item_w_mingxiao_spit")
            consoleutil.console("use item_w_mingxiao_spit")
            __main__.ScheduleTask(0.45,"koldunismlvl5_2()")
            __main__.ScheduleTask(1.85,"castmalend()")
        else:
            pc.GiveItem("item_w_tzimisce2_head")
            consoleutil.console("use item_w_tzimisce2_head")
            __main__.ScheduleTask(0.45,"koldunismlvl5_2()")
            __main__.ScheduleTask(1.85,"castfemend()")

def koldunismlvl5_2():
    	  pc=__main__.FindPlayer()
          consoleutil.console("player_sequence d_thaum_idle")
          __main__.ScheduleTask(0.85,"koldunismlvl5_2a()")

def koldunismlvl5_2a():
	  castkoldunism.Activate12Summon(1)

#----------------------------------------------------------------------NIHILISTICS-----------------------
#Discipline Nihilistics LEVEL 1
def nihilisticslvl1():
    __main__.ccmd.thirdperson=""
    __main__.ScheduleTask(0.5,"nihilisticslvl1f()")
    if(__main__.G.Eyes_of_the_Wraith == 1):
        return
    else:
	__main__.FindEntityByName("pevents").MakePlayerUnkillable()
    	consoleutil.console("fov 120")
	__main__.ccmd.RemoveFeed=""
	__main__.cvar.hidehud=1
        __main__.ScheduleTask(0.1,"nihilisticslvl1a()")

def nihilisticslvl1a():
    __main__.G.Eyes_of_the_Wraith = 1 
    #consoleutil.console("hidehud 1")
    __main__.ScheduleTask(0.1,"nihilisticslvl1b()")

def nihilisticslvl1b():
    consoleutil.console("npc_ignore_player 1")
    __main__.ScheduleTask(10.0,"nihilisticslvl1c()")

def nihilisticslvl1c():
    consoleutil.console("npc_ignore_player 0")
    __main__.cvar.hidehud=0
    __main__.G.Eyes_of_the_Wraith = 0 
    __main__.ScheduleTask(0.05,"nihilisticslvl1d()")

def nihilisticslvl1d():
    consoleutil.console("fov 75")
    __main__.ScheduleTask(0.05,"nihilisticslvl1e()")

def nihilisticslvl1e():
    #consoleutil.console("hidehud 0")
    __main__.ccmd.RestoreFeed=""
    __main__.FindEntityByName("pevents").MakePlayerKillable()

def nihilisticslvl1f():
    __main__.ccmd.player_mobilize=""

#-------------------------------------------- LEVEL 2 ------------------------
#Discipline Nihilistics LEVEL 2 Consume Dead
def nihilisticslvl2():
    from random import Random
    from time import time
    R = Random( time() )
    chance1 = R.randint(1, 4)
    if(chance1 == 1):
        __main__.ScheduleTask(0.1,"nihilisticslvl2a()")
    elif(chance1 == 2):
        __main__.ScheduleTask(0.1,"nihilisticslvl2b()")
    elif(chance1 == 3):
        __main__.ScheduleTask(0.1,"nihilisticslvl2c()")
    elif(chance1 == 4):
        __main__.ScheduleTask(0.1,"nihilisticslvl2a()")

def nihilisticslvl2a():
    consoleutil.console("infobar_message 53")
    __main__.FindPlayer().Bloodgain(1)

def nihilisticslvl2b():
    castnihilistics.ActivateNihGhosts(2)

def nihilisticslvl2c():
    castnihilistics.ActivateNihGhosts(3)

#------------------------------------------- LEVEL 3 ------------------------
#Discipline Nihilistics LEVEL 3 Aura Of Decay
def nihilisticslvl3():
    __main__.ScheduleTask(0.1,"nihilisticslvl3a()")
    __main__.cvar.sv_gravity=3000

#Nihilistics level 3 Timer 
def nihilisticslvl3a():
    nihilisticslvl3aura()
    __main__.G.NihilCounter = __main__.G.NihilCounter + 1
     
    if(__main__.G.NihilCounter >= 10):
        __main__.ScheduleTask(0.1,"nihilisticslvl3b()")
	print "exit"
	__main__.cvar.sv_gravity=800
        __main__.G.NihilCounter = 0
    else:
        __main__.ScheduleTask(1.05,"nihilisticslvl3a()") 


def nihilisticslvl3b():
    __main__.FindPlayer().ClearActiveDisciplines()

def nihilisticslvl3aura():
    pc=__main__.FindPlayer()
    aura = __main__.FindEntityByName("AuraOfDecay")
    o = pc.GetOrigin()
    no= (o[0],o[1],o[2]+35)
    aura.SetOrigin(no)
    __main__.ScheduleTask(0.1,"nihilisticslvl3aura1()")

def nihilisticslvl3aura1():
    __main__.FindEntityByName("AuraOfDecay").Explode()

#-------------------------------------------- LEVEL 5 ------------------------
#Discipline Nihilistics LEVEL 5 night cry
def nihilisticslvl5():
    castnihilistics.ActivateCrusaderSummon(1)

#----------------------------------------------------------All Disciplines END----------------------         
def OnPollEvent():
    companion.timer_OnTimer()
    possessutil.timer_OnTimer()
    OnBLEvent()
    ClanWeakness()

#------------------------
def SoulReaverAltAttack():
    pevents = __main__.FindEntitiesByClass("events_player")
    pevents[0].CreateControllerNPC()
    __main__.FindPlayer().SetSupernaturalLevel(5)
    __main__.ScheduleTask(0.05,"SoulReaverAltAttack1()")
    #__main__.FindPlayer().FrenzyCheck(-10)

def SoulReaverAltAttack1():
    playerclone =  __main__.FindEntityByName("!playercontroller")
    playerclone.SetGesture("sheriffsword_attack_heavy")
    __main__.ScheduleTask(1.0,"SoulReaverAltAttack2()")
    #__main__.ScheduleTask(0.95,"castObteneblvl4HelperAura()")
    __main__.ScheduleTask(0.85,"nihilisticslvl3aura()")  
    #__main__.ScheduleTask(0.0,"castkoldunism.KoldunicPlayerBloodloss(1)")

def SoulReaverAltAttack2():
    pevents = __main__.FindEntitiesByClass("events_player")
    pevents[0].RemoveControllerNPC()
    consoleutil.console("vdmg 2")
  
#----------------------------------------------------------- PC COMBAT stuff ----------------------
#PC kick leg if press 'Q' and strike by shield
def PcKick():
       pc=__main__.FindPlayer()                                      
       if(pc.HasWeaponEquipped("item_w_grenade_frag") or pc.HasWeaponEquipped("item_w_crossbow_flaming") or pc.HasWeaponEquipped("item_w_flamethrower") or pc.HasWeaponEquipped("item_w_remington_m_700") or pc.HasWeaponEquipped("item_w_rem_m_700_bach")):
          return
       else:
          if(pc.clan == 13):
             __main__.ScheduleTask(0.01,"PcGargoyleClaws2()")
          else:
             #__main__.ScheduleTask(0.01,"PcKick1()")
             if(pc.HasWeaponEquipped("item_w_chang_energy_ball")):
                __main__.ScheduleTask(0.01,"SerpentisAltAttack()")
             else:
                #__main__.ScheduleTask(0.01,"PcKick1()")
                if(pc.HasWeaponEquipped("item_w_sheriff_sword")):
                   __main__.ScheduleTask(0.0,"SoulReaverAltAttack()")
                else:
                   __main__.ScheduleTask(0.01,"PcKick1()")

#PC kick main block
def PcKick1():
       pc=__main__.FindPlayer()
       PcKickhelper = __main__.FindEntityByName("PcKickhelper")                                         
       if(PcKickhelper):
          return
       elif(not PcKickhelper):
          if(pc.base_brawl <= 2):
             consoleutil.console("player_sequence kick_short")
             __main__.ScheduleTask(1.05,"PcKick2()")
          elif(pc.base_brawl == 3):
             consoleutil.console("player_sequence kick_long")
             __main__.ScheduleTask(1.05,"PcKick2()")
          elif(pc.base_brawl == 4):
             consoleutil.console("player_sequence kick_long")
             __main__.ScheduleTask(1.05,"PcKick2()")
          elif(pc.base_brawl == 5):
             consoleutil.console("player_sequence kick_long")
             __main__.ScheduleTask(0.75,"PcKickShield()")
             __main__.ScheduleTask(1.05,"PcKick2()")
          PcKickhelper=__main__.CreateEntityNoSpawn("prop_dynamic_ornament",pc.GetOrigin(),pc.GetAngles())
          PcKickhelper.SetName("PcKickhelper")
          PcKickhelper.SetModel("models/null.mdl")
          __main__.CallEntitySpawn(PcKickhelper)
          PcKickhelper = __main__.FindEntityByName("PcKickhelper")
          if PcKickhelper: PcKickhelper.SetAttached("!player")

def PcKick2():
          PcKickhelper = __main__.FindEntityByName("PcKickhelper")
	  PcKickhelper.Kill()

#PC strike by shield
def PcKickShield():
       pcShield = __main__.FindEntityByName("pcShield")                                     
       if(not pcShield):
	  return
       else:
          consoleutil.console("player_sequence sledgehammer_combo_C3")

#-----------------------------------------
def SerpentisAttack():
       if(__main__.G.SerCobAttackCounter > 0):
	  return
       else:
          __main__.FindPlayer().SpawnTempParticle("SerpentisCobraAttack_particle")
          __main__.ccmd.SerpentisAttack=""
          castpresence.SerpentisCobraAlt2Attack()

def SerpentisAltAttack():
       if(__main__.G.SerCobAltAttackCounter > 0):
	  return
       else:
          __main__.FindPlayer().SpawnTempParticle("SerpentisCobraAltattack_particle")
          __main__.ccmd.SerpentisAltAttack=""
          castpresence.SerpentisCobraAltAttack()

#----------------------------------------- Main attack block ---------------------
#CHECK PC Weapon Equipped
def OnPlayerAttackStart():
       pc=__main__.FindPlayer()                                       
       if(pc.HasWeaponEquipped("item_w_grenade_frag")):
          consoleutil.console("player_sequence fists_ready")
       elif(pc.HasWeaponEquipped("item_g_cash_box")):
          __main__.ScheduleTask(0.0,"ExplosiveBotYukie()")
       elif(pc.HasWeaponEquipped("item_g_car_stereo")):
          __main__.ScheduleTask(0.0,"CollectExplBotYukie()")
       elif(pc.HasWeaponEquipped("item_w_claws")):
          __main__.ScheduleTask(0.0,"PcGargoyleClaws()")
       elif(pc.HasWeaponEquipped("item_g_drugs_morphine_bottle")):
          __main__.ScheduleTask(0.0,"PcHumanHeal()")
       elif(pc.HasWeaponEquipped("item_g_drugs_pill_bottle")):
          __main__.ScheduleTask(0.0,"PcHumanAmphetamine()")
       elif(pc.HasWeaponEquipped("item_g_pisha_book")):
          __main__.ScheduleTask(0.0,"PcRiseNecromancy()")
       elif(pc.HasWeaponEquipped("item_g_wireless_camera_4")):
          __main__.ScheduleTask(0.0,"NagarajaEatFlesh()")
       elif(pc.HasWeaponEquipped("item_g_jumbles_flyer")):
          __main__.ScheduleTask(0.0,"PcUseHeartOfDarkness()")
       elif(pc.HasWeaponEquipped("item_w_chang_energy_ball")):
          __main__.ScheduleTask(0.0,"SerpentisAttack()")
       elif(pc.HasWeaponEquipped("item_g_wireless_camera_2")):
          __main__.ScheduleTask(0.0,"castkoldunism.KoldunicSelectLevelStart()")

def OnPlayerAttackEnd():
       pc=__main__.FindPlayer()  
                                       
#-----------------------------------------
#PC possess gargoyle use claws
def PcGargoyleClaws():
       pc=__main__.FindPlayer()
       PcKickhelper = __main__.FindEntityByName("PcKickhelper")                                        
       if(PcKickhelper):
          return
       elif(not PcKickhelper):
          #consoleutil.console("player_sequence ACT_MELEE_ATTACK")
	  PcGargoyleRandomAttack()
          __main__.ScheduleTask(0.65,"PcKick2()")
          PcKickhelper=__main__.CreateEntityNoSpawn("prop_dynamic_ornament",pc.GetOrigin(),pc.GetAngles())
          PcKickhelper.SetName("PcKickhelper")
          PcKickhelper.SetModel("models/null.mdl")
          __main__.CallEntitySpawn(PcKickhelper)
          PcKickhelper = __main__.FindEntityByName("PcKickhelper")
          if PcKickhelper: PcKickhelper.SetAttached("!player")

def PcGargoyleRandomAttack():
    from random import Random
    from time import time
    R = Random( time() )
    GargAttack = R.randint(1, 4)
    if(GargAttack == 1):
        consoleutil.console("player_sequence 75")
    elif(GargAttack == 2):
        consoleutil.console("player_sequence 76")
    elif(GargAttack == 3):
        consoleutil.console("player_sequence 78")
    elif(GargAttack == 4):
        consoleutil.console("player_sequence 79")


#PC possess gargoyle press 'Q' gargoyle strike from ground
def PcGargoyleClaws2():
       pc=__main__.FindPlayer()
       PcKickhelper = __main__.FindEntityByName("PcKickhelper")                                        
       if(PcKickhelper):
          return
       elif(not PcKickhelper):
          consoleutil.console("player_sequence ACT_ANDREI_DIVE_OUT")
          __main__.ScheduleTask(0.65,"PcKick2()")
          PcKickhelper=__main__.CreateEntityNoSpawn("prop_dynamic_ornament",pc.GetOrigin(),pc.GetAngles())
          PcKickhelper.SetName("PcKickhelper")
          PcKickhelper.SetModel("models/null.mdl")
          __main__.CallEntitySpawn(PcKickhelper)
          PcKickhelper = __main__.FindEntityByName("PcKickhelper")
          if PcKickhelper: PcKickhelper.SetAttached("!player")

#--------------------------------------------
def PcUseHeartOfDarkness():
    pc=__main__.FindPlayer()
    clan = pc.clan 
    if(clan == 2):
        if(pc.base_blood_healing >= 3):
    	    __main__.ScheduleTask(0.0,"PcUseHeartOfDarkness1()")
    elif(clan == 6):     
        if(pc.base_dementation >= 4 and pc.base_intelligence >= 4):
    	    __main__.ScheduleTask(0.0,"PcUseHeartOfDarkness1()")

def PcUseHeartOfDarkness1():
    __main__.ccmd.thirdperson="" 
    __main__.FindPlayer().RemoveItem("item_g_jumbles_flyer")
    consoleutil.console("player_sequence seductive_attacker_shortvictim_front_release_standing")
    __main__.ScheduleTask(0.45,"PcUseHeartOfDarkness2()")

def PcUseHeartOfDarkness2():
    castnihilistics.ActivateShadowTwin(1)
    consoleutil.console("inven_wield 52")
 
#-------------------------------------------- Nagaraja weakness --------------------------------
#Clan Weakness: player nagaraja eat flesh
def NagarajaEatFlesh():
       pc=__main__.FindPlayer()
       clan = pc.clan                                       
       if(clan == 7):
          __main__.ScheduleTask(0.15,"NagarajaEatFlesh1()")
       elif(clan == 6):
          if(pc.base_dementation >= 3):
             __main__.ScheduleTask(0.0,"TzimisceHeadRunner()")
          else:
             consoleutil.console("say Need Vicissitude level 3")

def NagarajaEatFlesh1():
       PcCamera()
       NagarajaEatFleshHelper()
       __main__.ScheduleTask(0.1,"NagarajaEatFlesh2()")

def NagarajaEatFlesh2():
       __main__.ccmd.NagarajaEat=""
       __main__.ScheduleTask(1.85,"NagarajaEatFlesh3()")

def NagarajaEatFlesh3():
       __main__.ccmd.NagarajaEat=""
       __main__.ScheduleTask(2.15,"NagarajaEatFlesh4()")

def NagarajaEatFlesh4():
       __main__.FindPlayer().RemoveItem("item_g_wireless_camera_4")
       __main__.FindEntityByName("PcNagaFlesh").Kill()
       __main__.G.NagarajaFeed = 1
       __main__.ccmd.player_mobilize=""

def NagarajaEatFleshHelper():
       pc=__main__.FindPlayer()
       PcNagaFlesh = __main__.FindEntityByName("PcNagaFlesh")
       __main__.ccmd.thirdperson=""                                         
       if(PcNagaFlesh):
          return
       else:
          PcNagaFlesh=__main__.CreateEntityNoSpawn("prop_dynamic_ornament",pc.GetOrigin(),pc.GetAngles())
          PcNagaFlesh.SetName("PcNagaFlesh")
          PcNagaFlesh.SetModel("models/cinematic/visual_stuff/pc/nagaraja_flesh/nagaraja_flesh.mdl")
          __main__.CallEntitySpawn(PcNagaFlesh)
          PcNagaFlesh = __main__.FindEntityByName("PcNagaFlesh")
          if PcNagaFlesh: PcNagaFlesh.SetAttached("!player")

#--------------------------------------------
def TzimisceHeadRunner():
    __main__.ccmd.player_immobilize=""
    __main__.ccmd.thirdperson=""  
    consoleutil.console("player_sequence land_hard")
    __main__.ScheduleTask(0.75,"TzimisceHeadRunner1()")

def TzimisceHeadRunner1():
    castthanatosislvl3.ActivateSzlachtaSummon(1)
    __main__.FindPlayer().RemoveItem("item_g_wireless_camera_4")
    __main__.ccmd.player_mobilize=""
  
#-------------------------------------------- Yukie use explosive bot-------------------------------------------------
#Special ability: explosive bot for Yukie
def ExplosiveBotYukie():
       pc=__main__.FindPlayer()
       clan = pc.clan                                       
       if(clan == 14):
          __main__.ScheduleTask(0.0,"ExplosiveBotYukie1()")

def ExplosiveBotYukie1():
       BotShell = __main__.FindEntityByName("BotShell")                                       
       if(BotShell):
          return
       else:
          __main__.ccmd.thirdperson=""
          __main__.ccmd.player_immobilize=""
          consoleutil.console("player_sequence place_bomb")
          __main__.ScheduleTask(1.45,"ExplosiveBotYukie2()")

def ExplosiveBotYukie2():
       castthanatosislvl3.SummonBotMain()
       __main__.FindPlayer().RemoveItem("item_g_cash_box")
       __main__.ScheduleTask(0.1,"ExplosiveBotYukie3()")

def ExplosiveBotYukie3():
       __main__.ccmd.player_mobilize=""
       __main__.FindPlayer().Holster()

#----------------------------------------
#Special ability: collecting explosive bot for Yukie
def CollectExplBotYukie():
       pc=__main__.FindPlayer()
       clan = pc.clan                                       
       if(clan == 14):
          __main__.ccmd.thirdperson=""
          __main__.ccmd.player_immobilize=""
          consoleutil.console("player_sequence place_bomb")
          __main__.ScheduleTask(0.1,"CollectExplBotYukie1()")

def CollectExplBotYukie1():
       pc=__main__.FindPlayer()                                       
       if(pc.AmmoCount("item_g_car_stereo") > 0 ):
          __main__.ScheduleTask(1.25,"CollectExplBotYukie2()")
          __main__.FindPlayer().RemoveItem("item_g_car_stereo")
	  if(pc.HasItem("item_g_cash_box")):
             __main__.FindPlayer().GiveAmmo("item_g_cash_box",1)
          else:
	     pc.GiveItem("item_g_cash_box")

def CollectExplBotYukie2():
       __main__.ccmd.player_mobilize=""

#----------------------------------------
#PC human heal: if use morphine, new method human player +10 to soak 30 sec.
def PcHumanHeal():
       pc=__main__.FindPlayer()
       clan = pc.clan                                       
       if(clan == 14 or clan == 17):
          __main__.ccmd.thirdperson=""
          consoleutil.console("player_sequence fists_ready")
          __main__.ScheduleTask(0.25,"PcHumanHealHelper()")
          pc.RemoveItem("item_g_drugs_morphine_bottle")

def PcHumanHealHelper():
       consoleutil.console("say Morphine Effect Gained")
       __main__.ccmd.SoundGood=""
       __main__.ScheduleTask(0.5,"PcHumanHealHelper1()")

def PcHumanHealHelper1():
       consoleutil.console("vhistory morphineeffect")
       __main__.ScheduleTask(30.0,"PcHumanHealHelper2()")

def PcHumanHealHelper2():
       consoleutil.console("vhistory none")
       __main__.ScheduleTask(1.5,"PcHumanHealHelper3()")

def PcHumanHealHelper3():
       consoleutil.console("say Morphine Effect Lost")
       __main__.ccmd.SoundBad=""

#----------------------------------------
#PC amphetamine: if use amphetamine, +50% speed 30 sec.
def PcHumanAmphetamine():
       pc=__main__.FindPlayer()
       clan = pc.clan                                       
       if(clan == 14 or clan == 17):
          __main__.ccmd.thirdperson=""
          consoleutil.console("player_sequence fists_ready")
          __main__.ScheduleTask(0.25,"PcHumanAmphetamineHelper()")
          pc.RemoveItem("item_g_drugs_pill_bottle")

def PcHumanAmphetamineHelper():
       consoleutil.console("say Desoxyn Effect Gained")
       __main__.ccmd.SoundGood=""
       __main__.ScheduleTask(0.5,"PcHumanAmphetamineHelper1()")

def PcHumanAmphetamineHelper1():
       #consoleutil.console("sv_runscale 1.5")
       __main__.cvar.sv_runscale=1.5
       __main__.ScheduleTask(30.0,"PcHumanAmphetamineHelper2()")

def PcHumanAmphetamineHelper2():
       #consoleutil.console("sv_runscale 1.0")
       __main__.cvar.sv_runscale=1.0
       __main__.ScheduleTask(0.5,"PcHumanAmphetamineHelper3()")

def PcHumanAmphetamineHelper3():
       consoleutil.console("say Desoxyn Effect Lost")
       __main__.ccmd.SoundBad=""

#---------------------------------------------------------------------------------------------
#----------------------------------------------------------PC camera-----------------------------------
#Camera fly 360' around PC (used when nagaraja eat flesh)
def PcCamera():
    	  pc=__main__.FindPlayer()
          consoleutil.console("cam_yaw 0")
          __main__.ScheduleTask(0.1,"PcCamera0()")

def PcCamera0():
    	  pc=__main__.FindPlayer()
          consoleutil.console("cam_yaw 22")
          __main__.ScheduleTask(0.1,"PcCamera1()")

def PcCamera1():
    	  pc=__main__.FindPlayer()
          consoleutil.console("cam_yaw 45")
          __main__.ScheduleTask(0.1,"PcCamera1a()")

def PcCamera1a():
    	  pc=__main__.FindPlayer()
          consoleutil.console("cam_yaw 67")
          __main__.ScheduleTask(0.1,"PcCamera2()")

def PcCamera2():
    	  pc=__main__.FindPlayer()
          consoleutil.console("cam_yaw 90")
          __main__.ScheduleTask(0.1,"PcCamera2a()")

def PcCamera2a():
    	  pc=__main__.FindPlayer()
          consoleutil.console("cam_yaw 112")
          __main__.ScheduleTask(0.1,"PcCamera3()")

def PcCamera3():
    	  pc=__main__.FindPlayer()
          consoleutil.console("cam_yaw 135")
          __main__.ScheduleTask(0.1,"PcCamera3a()")

def PcCamera3a():
    	  pc=__main__.FindPlayer()
          consoleutil.console("cam_yaw 157")
          __main__.ScheduleTask(0.1,"PcCamera4()")

def PcCamera4():
    	  pc=__main__.FindPlayer()
          consoleutil.console("cam_yaw 180")
          __main__.ScheduleTask(0.1,"PcCamera4a()")

def PcCamera4a():
    	  pc=__main__.FindPlayer()
          consoleutil.console("cam_yaw 202")
          __main__.ScheduleTask(0.1,"PcCamera5()")

def PcCamera5():
    	  pc=__main__.FindPlayer()
          consoleutil.console("cam_yaw 225")
          __main__.ScheduleTask(0.1,"PcCamera5a()")

def PcCamera5a():
    	  pc=__main__.FindPlayer()
          consoleutil.console("cam_yaw 247")
          __main__.ScheduleTask(0.1,"PcCamera6()")

def PcCamera6():
    	  pc=__main__.FindPlayer()
          consoleutil.console("cam_yaw 270")
          __main__.ScheduleTask(0.1,"PcCamera6a()")

def PcCamera6a():
    	  pc=__main__.FindPlayer()
          consoleutil.console("cam_yaw 292")
          __main__.ScheduleTask(0.1,"PcCamera7()")

def PcCamera7():
    	  pc=__main__.FindPlayer()
          consoleutil.console("cam_yaw 315")
          __main__.ScheduleTask(0.1,"PcCamera7a()")

def PcCamera7a():
    	  pc=__main__.FindPlayer()
          consoleutil.console("cam_yaw 337")
          __main__.ScheduleTask(0.1,"PcCamera8()")

def PcCamera8():
    	  pc=__main__.FindPlayer()
          consoleutil.console("cam_yaw 0")

#----------------------------------------------------------PC GEAR-----------------------------------
#Pc gear: this block response of newPC gear: shield, hockey mask, shoulder pad 
def PcSuit():
       PlayerMask = __main__.FindEntityByName("PcMask")
       PlayerSpad = __main__.FindEntityByName("pcSpad")
       pcShield()
       #PcMask()
       #PcSpad()
       GargoyleUnpossessCheck()
       if(__main__.G.Player_Cobra_Form == 1 or __main__.G.Player_Shadow_Form == 1 or __main__.G.Player_Ashes_Form == 1):
	  if(PlayerSpad and PlayerMask):
	     PlayerMask.Kill()
             PlayerSpad.Kill()                                   
	  elif(PlayerSpad):
             PlayerSpad.Kill()
	  elif(PlayerMask):
             PlayerMask.Kill()
	  #return
       else:
	  PcMask()
	  PcSpad()
       
#Pc gear helper: fix bug with PC gear if load map
def PcGearHelper():
       pc=__main__.FindPlayer()
       PcMask = __main__.FindEntityByName("PcMask")
       pcSpad = __main__.FindEntityByName("pcSpad")
       PcUnarmedCheck()
       SetComputerRandomPassword()
                              
       if(pcSpad and PcMask):
	  PcMask.Kill()
          pcSpad.Kill()                                   
       elif(pcSpad):
          pcSpad.Kill()
       elif(PcMask):
          PcMask.Kill()

#Pc Gear: shield
def pcShield():
       pc=__main__.FindPlayer()
       pcShield = __main__.FindEntityByName("pcShield")
                                       
       if(pc.HasItem("item_p_occult_hacking") and pcShield):
       	  if(pc.HasWeaponEquipped("item_w_avamp_blade") or pc.HasWeaponEquipped("item_w_baseball_bat") or pc.HasWeaponEquipped("item_w_baton") or pc.HasWeaponEquipped("item_w_chang_blade") or pc.HasWeaponEquipped("item_w_katana") or pc.HasWeaponEquipped("item_w_knife") or pc.HasWeaponEquipped("item_w_occultblade") or pc.HasWeaponEquipped("item_w_severed_arm") or pc.HasWeaponEquipped("item_w_sheriff_sword") or pc.HasWeaponEquipped("item_w_tire_iron") or pc.HasWeaponEquipped("item_w_torch")):
	       return
          elif(not pc.HasWeaponEquipped("item_w_avamp_blade") or not pc.HasWeaponEquipped("item_w_baseball_bat") or not pc.HasWeaponEquipped("item_w_baton") or not pc.HasWeaponEquipped("item_w_chang_blade") or not pc.HasWeaponEquipped("item_w_katana") or not pc.HasWeaponEquipped("item_w_knife") or not pc.HasWeaponEquipped("item_w_occultblade") or not pc.HasWeaponEquipped("item_w_severed_arm") or not pc.HasWeaponEquipped("item_w_sheriff_sword") or not pc.HasWeaponEquipped("item_w_tire_iron") or not pc.HasWeaponEquipped("item_w_torch")):
               pc.RemoveItem("item_w_tzimisce3_claw")
               pcShield.Kill()
               __main__.ScheduleTask(0.1,"pcShieldhelper()")
       elif(pc.HasItem("item_p_occult_hacking") and not pcShield):
       	  if(pc.HasWeaponEquipped("item_w_avamp_blade") or pc.HasWeaponEquipped("item_w_baseball_bat") or pc.HasWeaponEquipped("item_w_baton") or pc.HasWeaponEquipped("item_w_chang_blade") or pc.HasWeaponEquipped("item_w_katana") or pc.HasWeaponEquipped("item_w_knife") or pc.HasWeaponEquipped("item_w_occultblade") or pc.HasWeaponEquipped("item_w_severed_arm") or pc.HasWeaponEquipped("item_w_sheriff_sword") or pc.HasWeaponEquipped("item_w_tire_iron") or pc.HasWeaponEquipped("item_w_torch")):
               pc.GiveItem("item_w_tzimisce3_claw")              
	       pcShield=__main__.CreateEntityNoSpawn("prop_dynamic_ornament",pc.GetOrigin(),pc.GetAngles())
               pcShield.SetName("pcShield")
               pcShield.SetModel("models/cinematic/visual_stuff/pc/shield/w_m_pc_shield.mdl")
               __main__.CallEntitySpawn(pcShield)
               pcShield = __main__.FindEntityByName("pcShield")
               if pcShield: pcShield.SetAttached("!player")
       elif(not pc.HasItem("item_p_occult_hacking") and pcShield):
	  pc.RemoveItem("item_w_tzimisce3_claw")
	  pcShield.Kill()
          __main__.ScheduleTask(0.1,"pcShieldhelper()")

def pcShieldhelper():
       __main__.FindPlayer().GiveItem("item_w_tzimisce2_claw")
       __main__.ScheduleTask(0.1,"pcShieldhelper1()")

def pcShieldhelper1():
       __main__.FindPlayer().RemoveItem("item_w_tzimisce2_claw")

#Pc Gear: hockey mask
def PcMask():
       pc=__main__.FindPlayer()
       PcMask = __main__.FindEntityByName("PcMask")
       clan = pc.clan
                              
       if(pc.HasItem("item_p_occult_strength") and PcMask):
          return 0
       elif(pc.HasItem("item_p_occult_strength")):
          PcMask=__main__.CreateEntityNoSpawn("prop_dynamic_ornament",pc.GetOrigin(),pc.GetAngles())
          PcMask.SetName("PcMask")
          if(pc.IsMale()):
            	if clan == 2: PcMask.SetModel("models/cinematic/visual_stuff/pc/hockey_mask/male/ventrue/hockey_mask.mdl")
          	elif clan == 3: PcMask.SetModel("models/cinematic/visual_stuff/pc/hockey_mask/male/toreador/hockey_mask.mdl")
          	elif clan == 4: PcMask.SetModel("models/cinematic/visual_stuff/pc/hockey_mask/male/malkavian/hockey_mask.mdl")
          	elif clan == 5: PcMask.SetModel("models/cinematic/visual_stuff/pc/hockey_mask/male/nosferatu/hockey_mask.mdl")
          	elif clan == 6: PcMask.SetModel("models/cinematic/visual_stuff/pc/hockey_mask/male/malkavian/hockey_mask.mdl")
          	elif clan == 7: PcMask.SetModel("models/cinematic/visual_stuff/pc/hockey_mask/male/tremere/hockey_mask.mdl")
          	elif clan == 8: PcMask.SetModel("models/cinematic/visual_stuff/pc/hockey_mask/male/tremere/hockey_mask.mdl")
       	  #else:
          elif(not pc.IsMale()):
            	if clan == 2: PcMask.SetModel("models/cinematic/visual_stuff/pc/hockey_mask/female/toreador/hockey_mask.mdl")
          	elif clan == 3: PcMask.SetModel("models/cinematic/visual_stuff/pc/hockey_mask/female/gangrel/hockey_mask.mdl")
          	elif clan == 4: PcMask.SetModel("models/cinematic/visual_stuff/pc/hockey_mask/female/ventrue/hockey_mask.mdl")
          	elif clan == 5: PcMask.SetModel("models/cinematic/visual_stuff/pc/hockey_mask/female/nosferatu/hockey_mask.mdl")
          	elif clan == 6: PcMask.SetModel("models/cinematic/visual_stuff/pc/hockey_mask/female/malkavian/hockey_mask.mdl")
          	#elif clan == 7: PcMask.SetModel("models/cinematic/visual_stuff/pc/hockey_mask/female/tremere/hockey_mask.mdl")
		elif clan == 7: PcMask.SetModel("models/cinematic/visual_stuff/pc/hockey_mask/female/nagaraja/hockey_mask.mdl")
          	elif clan == 8: PcMask.SetModel("models/cinematic/visual_stuff/pc/hockey_mask/female/tremere/hockey_mask.mdl")
          __main__.CallEntitySpawn(PcMask)
          PcMask = __main__.FindEntityByName("PcMask")
          if PcMask: PcMask.SetAttached("!player")
       elif(not pc.HasItem("item_p_occult_strength") and PcMask):
	  PcMask.Kill()

#Pc Gear: shoulder pad
def PcSpad():
       pc=__main__.FindPlayer()
       pcSpad = __main__.FindEntityByName("pcSpad")
       clan = pc.clan
                                         
       if(pc.HasItem("item_p_occult_obfuscate") and pcSpad):
          return
       elif(pc.HasItem("item_p_occult_obfuscate")):
          pcSpad=__main__.CreateEntityNoSpawn("prop_dynamic_ornament",pc.GetOrigin(),pc.GetAngles())
          pcSpad.SetName("pcSpad")
          if(pc.IsMale()):
            	if clan == 2: pcSpad.SetModel("models/cinematic/visual_stuff/pc/shoulder_pad/male/ventrue/shoulder_pad.mdl")
          	elif clan == 3: pcSpad.SetModel("models/cinematic/visual_stuff/pc/shoulder_pad/male/toreador/shoulder_pad.mdl")
          	elif clan == 4: pcSpad.SetModel("models/cinematic/visual_stuff/pc/shoulder_pad/male/malkavian/shoulder_pad.mdl")
          	elif clan == 5: pcSpad.SetModel("models/cinematic/visual_stuff/pc/shoulder_pad/male/nosferatu/shoulder_pad.mdl")
          	elif clan == 6: pcSpad.SetModel("models/cinematic/visual_stuff/pc/shoulder_pad/male/malkavian/shoulder_pad.mdl")
          	elif clan == 7: pcSpad.SetModel("models/cinematic/visual_stuff/pc/shoulder_pad/male/tremere/shoulder_pad.mdl")
          	elif clan == 8: pcSpad.SetModel("models/cinematic/visual_stuff/pc/shoulder_pad/male/tremere/shoulder_pad.mdl")
       	  #else:
          elif(not pc.IsMale()):
            	pcSpad.SetModel("models/cinematic/visual_stuff/pc/shoulder_pad/female/shoulder_pad.mdl")
          __main__.CallEntitySpawn(pcSpad)
          pcSpad = __main__.FindEntityByName("pcSpad")
          if pcSpad: pcSpad.SetAttached("!player")
       elif(not pc.HasItem("item_p_occult_obfuscate") and pcSpad):
	  pcSpad.Kill()

#---------------------------
#Some test stuff: need remove
def PcSuit1():
       pc=__main__.FindPlayer()
       pcClone = __main__.FindEntityByName("pcClone")                                         
       if(pc.HasItem("item_g_stake") and pcClone):
          return
       elif(pc.HasItem("item_g_stake")):
          pcClone=__main__.CreateEntityNoSpawn("prop_dynamic_ornament",pc.GetOrigin(),pc.GetAngles())
          pcClone.SetName("pcClone")
          pcClone.SetModel("models/weapons/disciplines/obtenebration/metamorphosis.mdl")
          __main__.CallEntitySpawn(pcClone)
          pcClone = __main__.FindEntityByName("pcClone")
          if pcClone: pcClone.SetAttached("!player")
       elif(not pc.HasItem("item_g_stake") and pcClone):
	  pcClone.Kill()

def PcSuit2():
       pc=__main__.FindPlayer()
       pcClone2 = __main__.FindEntityByName("pcClone2")                                        
       if(pc.HasItem("item_g_stake") and pcClone2):
          return
       elif(pc.HasItem("item_g_stake")):
          pcClone2=__main__.CreateEntityNoSpawn("prop_dynamic_ornament",pc.GetOrigin(),pc.GetAngles())
          pcClone2.SetName("pcClone2")
          pcClone2.SetModel("models/cinematic/visual_stuff/laser designator_ak47/w_m_laser_pist1.mdl")
          #pcClone2.SetModel(pc.model)
          __main__.CallEntitySpawn(pcClone2)
          pcClone2 = __main__.FindEntityByName("pcClone2")
          if pcClone2: pcClone2.SetAttached("!player")
       elif(not pc.HasItem("item_g_stake") and pcClone2):
	  pcClone2.Kill()

#--------------------------------------------------------- Masquerade ------------------------
#New Masquerade Check: If pc possess nosferatu gargoyle or embraced samedi
def NewMasqueradeCheck():
       PcMasquerade()
       #if(comp1):
       #Comp1Masquerade()
       #elif(comp2):
       #Comp2Masquerade()

def PcMasquerade():
       pc=__main__.FindPlayer()
       clan = pc.clan                                       
       if(clan == 13 or clan == 11 or clan == 21):
          pc.SetSupernaturalLevel(3)
          #print ( "*************** Masquerade violation check***************" )

#---------------------------------------------------------------------------------
#New Masquerade hepler: If pc travel with nosferatu, gargoyle or embraced samedi, testing
def Comp1MasqueradeX():
       pc=__main__.FindPlayer()
       clan = pc.clan 
       comp1 = Find("companion1")                                       
       if(comp1.GetData("OName")=="Bertram"):
          #comp1.SetScriptedDiscipline("mind_shield 2")
          #__main__.ScheduleTask(0.75,"__main__.FindEntityByName('companion1').ClearActiveDisciplines()")
          #__main__.ScheduleTask(0.5,"__main__.FindEntityByName('companion1').SetScriptedDiscipline('mind_shield 0')")
          pc.SetSupernaturalLevel(5)
       elif(comp1.GetData("OName")=="Rockbiter"):
          pc.SetSupernaturalLevel(5)
       elif(comp1.GetData("OName")=="Barabus"):
          pc.SetSupernaturalLevel(5)
       elif(comp1.GetData("Embraced")==3 and comp1.GetData("OName")=="Heather" and clan == 5):
          pc.SetSupernaturalLevel(5)

def Comp1Masquerade():
       pc=__main__.FindPlayer()
       clan = pc.clan 
       comp1 = Find("companion1")                                       
       if(comp1.GetData('OName')=='Bertram' or comp1.GetData('OName')=='Rockbiter' or comp1.GetData('OName')=='Barabus' or comp1.GetData('OModel')=='models/character/npc/unique/santa_monica/heather_n_e'):
          pc.SetSupernaturalLevel(5)

def Comp2Masquerade():
       pc=__main__.FindPlayer()
       clan = pc.clan 
       comp2 = Find("companion2")                                       
       if(comp2.GetData('OName')=='Bertram' or comp2.GetData('OName')=='Rockbiter' or comp2.GetData('OName')=='Barabus' or comp2.GetData('OModel')=='models/character/npc/unique/santa_monica/heather_n_e'):
          pc.SetSupernaturalLevel(5)

#Gargoyle unpossess helper: Fix bug's with unpossessing gargoyle
def GargoyleUnpossessCheck():
       pc=__main__.FindPlayer()
       clan = pc.clan                                       
       if(clan == 13):
          return
       else:
          if(__main__.G.Gargoyle_Flight==0):
             return
          else:
             __main__.ScheduleTask(0.15,"GargoyleFlight1()")

#---------------------------------------------------------------------------------
#Jenny blood healing
def BloodHealJenny():
       __main__.FindEntityByName("Jenny").MakeInvincible(1)
       __main__.FindEntityByName("Jenny_blood_heal").TurnOn()
       __main__.ScheduleTask(60.0,"BloodHealJenny1()")

def BloodHealJenny1():
       __main__.FindEntityByName("Jenny").MakeInvincible(0)

#---------------------------------------------------------------------------------
#Test
def PcDominated():
       pc=__main__.FindPlayer()
       __main__.ccmd.player_immobilize=""                                       
       if(pc.base_dominate >= 4):
          __main__.ccmd.PcDominatedAnim=""
          __main__.ScheduleTask(0.25,"PcDominatedEnd()")
       else:
          __main__.ccmd.PcDominatedAnim=""
          __main__.ScheduleTask(1.85,"PcDominatedEnd()")

def PcDominatedEnd():
       __main__.ccmd.player_mobilize=""

#---------------------------------------------------------------------------------
#TEST Fix some bugs when map load or PC use some weapon or PC die
def PcUnarmedCheck():
    pevents = __main__.FindEntitiesByClass("events_player")
    pevents[0].MakePlayerKillable()
    consoleutil.console("inven_holster 1")
    __main__.cvar.sv_runscale=1.0
    __main__.cvar.sv_gravity=800
    __main__.cvar.hidehud=0
    __main__.G.Gargoyle_Flight=0
    __main__.G.Eyes_of_the_Wraith = 0
    __main__.G.NihilCounter = 0
    __main__.G.Player_Cobra_Form = 0
    __main__.G.PresenceCounter = 0
    __main__.G.SetitesWeakness = 0
    __main__.G.Player_Shadow_Form = 0
    __main__.G.Player_Ashes_Form = 0
    __main__.G.MagmaShatterCounter = 0
    __main__.ccmd.RestoreFeed=""
    #__main__.ccmd.VhistoryNone=""
    __main__.FindPlayer().ClearActiveDisciplines()
    SetitesWeaknessHelper()

#RANDOM PASSWORDS: set random paswords for side pc's
def SetComputerRandomPassword():
    from random import Random
    from time import time
    R = Random( time() )
    password = R.randint(1, 3)
    if(password == 1):
 	print ( "****************** Password 1 ********************" )
 	__main__.G.Computer_Password = 1
    elif(password == 2):
 	print ( "****************** Password 2 ********************" )
 	__main__.G.Computer_Password = 2
    elif(password == 3):
 	print ( "****************** Password 3 ********************" )
 	__main__.G.Computer_Password = 3

#---------------------------------------------------------------------------------
#Next Dheu code of comanion mode
#---------------------------------------------------------------------------------
# OnEnterMap : Required logic_auto entities placed on every map.
# {
# "classname" "logic_auto"
# "spawnflags" "0"
# "OnMapLoad" ",,,0,-1,OnEnterMap('sm_hub_1'),"
# "origin" "-2420.54 -2558.76 -111.97"
# }
# Notes : Does not get called on save game reload.
#         See OnBeginNormalMusic below to place
#         code you want executed on both map
#         transitions AND save game reloads. 

CompModIgnoreMaps=("la_malkavian_1","sp_tutorial_1","sp_ninesintro","sp_theatre" \
                  ,"sp_taxiride","sp_masquerade_1","sp_epilogue")

def OnEnterMap(mapName):
    global InCombat
    
    __main__.G.currentMap=mapName
    log("Entering map [%s]" % mapName,1)
    log("Game State [%d]" % __main__.G.Story_State,1)

    # Buf fix Patch 1.2: PC changes maps during combat. OnBeginNormal Music
    # fires. InCombat state was still 1, so OnEndCombat also fired, respawning
    # any companions standing on the map that hadn't been cleaned up yet. This
    # in turn re-added them to the G.henchmen array and caused a doopleganger to
    # appear when populateCompanions was finally invoked. Resetting InCombat
    # to 0 prevents the bug.
    InCombat=0

    # Skip Tutorial Bug Fix
    if "sm_pawnshop_1" == mapName:
        if not __main__.FindPlayer().HasItem("item_g_lockpick"):
            __main__.FindPlayer().GiveItem("item_g_lockpick")
    
    # Fix Edited Map bug
    try:
        world=__main__.FindEntitiesByName("world")[0]
        world.AIEnable(1)
    except:
        pass

    # Cycles Maps Support
    if __main__.G.cyclemaps:
        index = statutil.MapNames.index(mapName) + 1
        if index < len(statutil.MapNames):
            nextTask="consoleutil.console(\"map %s\")" % statutil.MapNames[index]
            __main__.ScheduleTask(7.0,nextTask)
        else:
            __main__.G.cyclemaps=0

    # Initialize modules (1 time per campaign)
    if not __main__.G.vamputilinit:
        InitializeModules()

    # Music Manager Integration
    musicutil.OnEnterMap(mapName)

    # Sound Manager (Battle Cries)
    soundutil.OnEnterMap(mapName)

    #if mapName == "ch_lotus_1":
    #    cams = FindClass("npc_VCamera") 
    #    for cam in cams:
    #        cam.Kill()

    #if mapName == "ch_zhaos_1":
    #    cams = FindClass("npc_VCamera") 
    #    for cam in cams:
    #        cam.Kill()

    #if mapName == "sm_gallery_1":
    #    __main__.ScheduleTask(5.0,"SamediCastSpellzombies()")
    #    __main__.ScheduleTask(100.0,"SamediCastCompress()")

    # Damsel Fight Setup
    if 1==__main__.G.Damsel_Fight and mapName == "la_hub_1":
        damsel = __main__.FindEntityByName("Damsel")
        if damsel:
            __main__.G.Damsel_Fight=2
            damsel.ScriptUnhide()

    if 2==__main__.G.Damsel_Fight and mapName == "la_expipe_1":
        damsel = __main__.FindEntityByName("Damsel")
        if damsel:
            log("Hiding original Damsel. Renaming to Damsel_orig")
            damsel.SetName("Damsel_orig")
            damsel.ScriptHide()
            __main__.G.Damsel_Fight=3

    if not (mapName in CompModIgnoreMaps):
        companion.auto_OnMapLoad(mapName)
        possessutil.auto_OnMapLoad(mapName)

    # Pose System Fixes
    __main__.ccmd.fixcamera=""
    if __main__.G.poseKeysMapped: havenutil.UnmapPoseKeys()

    if havenutil.isInHaven():
        log("Calling havenutil.OnMapLoad",1)
        havenutil.OnMapLoad(mapName)

    # Create Phylax Spell Easter Egg
    if mapName == "la_malkavian_2":
        if 0 == __main__.G._spawned_spell:
            spell=__main__.CreateEntityNoSpawn("item_p_occult_hacking", (509.03125, 688.03125, -3007.96875),(0,0,0))
            if spell:
                __main__.CallEntitySpawn(spell)
            if spell:
                __main__.G._spawned_spell=1
    

# The following methods require an events_world object
# added/updated on every map that key into the
# OnCombatMusicStart/OnNormalMusicStart events
# {
# "classname" "events_world"
# "targetname" "world"
# "StartHidden" "0"
# "OnCombatMusicStart" ",,,0,-1,OnBeginCombatMusic(),"
# "OnNormalMusicStart" ",,,0,-1,OnEndCombatMusic(),"
# "origin" "-2683.47 -2152.89 -111"
# }

InCombat=0
def OnBeginCombatMusic():
    global InCombat

    log("OnBeginCombatMusic")
    InCombat=1

    # Music Manager Integration
    musicutil.OnBeginCombatMusic()
    # Sound Manager Integration (Battle Cries)
    soundutil.OnBeginCombatMusic()
    

    OnBeginCombat()

def OnBeginNormalMusic():
    global InCombat

    log("OnBeginNormalMusic")

    # Music Manager Integration
    musicutil.OnBeginNormalMusic()
    # Sound Manager Integration (Battle Cries)
    soundutil.OnBeginNormalMusic()

    if InCombat:
        InCombat=0
        OnEndCombat()
    else:
        log("Map Load Detected")
        if not __main__.FindPlayer().IsPC():
            consoleutil.console("vamplight_enabled 1");
        # if havenutil.isInHaven():
        #    log("Calling havenutil.OnMapLoad",1)
        #    havenutil.OnMapLoad(__main__.G.currentMap)
        


# The following methods require an events_player object
# added/updated on every map that key into the
# OnPlayerTookDamage/OnPlayerKilled/OnWolfMorphBegin
# OnWolfMorphEnd events
# {
# "classname" "events_player"
# "StartHidden" "0"
# "enabled" "1"
# "targetname" "pevents"
# "OnWolfMorphBegin" ",,,0,-1,possessutil.player_OnWolfMorphBegin(),"
# "OnWolfMorphEnd" ",,,0,-1,possessutil.player_OnWolfMorphEnd(),"
# "OnPlayerTookDamage" ",,,0,-1,possessutil.player_OnPlayerTookDamage(),"
# "OnPlayerKilled" ",,,0,-1,possessutil.player_OnPlayerKilled(),"
# "origin" "-2683.47 -2152.89 -111"
# }

def OnBeginWolfMorph():
    log("OnBeginWolfMorph")

def OnEndWolfMorph():
    log("OnEndWolfMorph")

def OnPlayerDamaged():
    log("OnPlayerDamaged")
    possessutil.player_OnPlayerTookDamage()

def OnPlayerDeath():
    PcUnarmedCheck()
    log("OnPlayerDeath")
    possessutil.player_OnPlayerKilled()

# OnBeginDialog requires adding a call to this function to every dialog in the game.
# Return value of 1 cancels dialog. (If this functional always returned 1,
# you wouldn't be able to speak to anyone in the game).

def OnBeginDialog(pc,npc,dialogindex):

    # Music Manager Integration
    musicutil.OnBeginDialog()

    log("Starting Dialog with [%s] dialog index [%d]" % (npc.GetName(),dialogindex))
    ret = companion.storeGlobals(npc)
    ret = (ret or possessutil.handleDialogIndex(pc,npc,dialogindex))
    if 1 != ret: companion.handleBeginDialog(dialogindex)
    return ret

def OnEpilogueMusic(thread=0):
    swamp   = __main__.FindEntityByName("Swamp")
    credits_music = __main__.FindEntityByName("credits_music")
    hamsterdance = __main__.FindEntityByName("HamsterDance")
    if 0 == thread:
        if hamsterdance and __main__.G.Boo_HamsterDance:
            log("Starting Special Ending Music")
            hamsterdance.FadeIn(1)
            __main__.ScheduleTask(8.5,"HamsterDance()")
            __main__.ScheduleTask(104.0,"OnEpilogueMusic(1)")
        elif swamp:
            log("Starting Normal Ending Music")
            swamp.FadeIn(1)
            __main__.ScheduleTask(240.0,"OnEpilogueMusic(1)")
    elif 1 == thread:
        if hamsterdance and __main__.G.Boo_HamsterDance:
            hamsterdance.FadeOut(4)
            if swamp:
                log("Starting Normal Ending Music")
                swamp.FadeIn(4)
                __main__.ScheduleTask(240.0,"OnEpilogueMusic(2)")
            elif credits_music:
                log("Beginning Credits Music")
                credits_music.FadeIn(4)
        elif swamp:
            log("Ending Normal Ending Music")
            swamp.FadeOut(1)
            if credits_music:
                log("Beginning Credits Music")
                credits_music.FadeIn(1)
    elif swamp:
        log("Ending Normal Ending Music")
        swamp.FadeOut(1)
        if credits_music:
            log("Beginning Credits Music")
            credits_music.FadeIn(1)
        
def HamsterDance(thread=0):
    booClone=__main__.FindEntityByName("booClone")
    if not booClone:
        cam = __main__.FindEntityByName("dance_cam")
        tar = __main__.FindEntityByName("dance_target")
        o = characterext._TraceCircle(tar,100,-65)
        o2 = (o[0],o[1],o[2]-30)
        a=tar.GetAngles()
        a=(a[0],a[1]+30,a[2])
        booClone=__main__.CreateEntityNoSpawn("prop_dynamic",o2,a)
        booClone.SetName("booClone")
        booClone.SetModel("models/null.mdl")
        log("Creating Boo")
        __main__.CallEntitySpawn(booClone)
        booClone=__main__.FindEntityByName("booClone")
        if not booClone:
            log("Boo Clone Creation Failed")
            return
        if cam and tar:
            cam.PlayAsCameraPosition()
            tar.PlayAsCameraTarget()        
    if 0 == thread:
        booClone.SetModel(__main__.FindPlayer().model)
        booClone.SetAnimation("dance01")
        __main__.ScheduleTask(9.5,"HamsterDance(1)")
    if 1 == thread:
        booClone.SetModel("models/character/npc/unique/downtown/lacroix/lacroix.mdl")
        booClone.SetAnimation("dance02")
        __main__.ScheduleTask(3.5,"HamsterDance(2)")
    if 2 == thread:
        booClone.SetModel("models/character/npc/unique/downtown/sheriff/sheriff.mdl")
        booClone.SetAnimation("dance03")
        __main__.ScheduleTask(3.5,"HamsterDance(3)")
    if 3 == thread:
        booClone.SetModel("models/character/npc/unique/santa_monica/beckett/beckett.mdl")
        booClone.SetAnimation("dance01")
        __main__.ScheduleTask(4.0,"HamsterDance(4)")
    if 4 == thread:
        booClone.SetModel("models/character/npc/unique/downtown/damsel/damsel.mdl")
        booClone.SetAnimation("dance02")
        __main__.ScheduleTask(4.0,"HamsterDance(5)")
    if 5 == thread:
        booClone.SetModel("models/character/npc/unique/hollywood/gary/nosferatu_gary.mdl")
        booClone.SetAnimation("dance03")
        __main__.ScheduleTask(4.0,"HamsterDance(6)")
    if 6 == thread:
        booClone.SetModel("models/character/npc/unique/santa_monica/heather/heather.mdl")
        booClone.SetAnimation("dance01")
        __main__.ScheduleTask(4.0,"HamsterDance(7)")
    if 7 == thread:
        booClone.SetModel("models/character/npc/unique/santa_monica/jeanette/jeanette.mdl")
        booClone.SetAnimation("dance02")
        __main__.ScheduleTask(4.0,"HamsterDance(8)")
    if 8 == thread:
        booClone.SetModel("models/character/npc/unique/downtown/nines/nines.mdl")
        booClone.SetAnimation("dance03")
        __main__.ScheduleTask(4.0,"HamsterDance(9)")
    if 9 == thread:
        booClone.SetModel("models/character/npc/unique/downtown/regent/regent.mdl")
        booClone.SetAnimation("dance01")
        __main__.ScheduleTask(4.0,"HamsterDance(10)")
    if 10 == thread:
        booClone.SetModel("models/character/npc/unique/santa_monica/therese/therese.mdl")
        booClone.SetAnimation("dance02")
        __main__.ScheduleTask(4.0,"HamsterDance(11)")
    if 11 == thread:
        booClone.SetModel("models/character/npc/unique/downtown/venus/venus.mdl")
        booClone.SetAnimation("dance03")
        __main__.ScheduleTask(4.0,"HamsterDance(12)")
    if 12 == thread:
        booClone.SetModel("models/character/npc/unique/downtown/vv/vv.mdl")
        booClone.SetAnimation("dance01")
        __main__.ScheduleTask(4.0,"HamsterDance(13)")        
    if 13 == thread:
        booClone.SetModel("models/character/monster/gargoyle/gargoyle.mdl")
        booClone.SetAnimation("dance02")
        __main__.ScheduleTask(4.0,"HamsterDance(14)")
    if 14 == thread:
        booClone.SetModel("models/character/npc/unique/santa_monica/stan_gimble/stan_gimble.mdl")
        booClone.SetAnimation("dance03")
        __main__.ScheduleTask(4.0,"HamsterDance(15)")
    if 15 == thread:
        booClone.SetModel("models/character/npc/unique/santa_monica/bertram/bertram.mdl")
        booClone.SetAnimation("dance01")
        __main__.ScheduleTask(4.0,"HamsterDance(16)")
    if 16 == thread:
        booClone.SetModel("models/character/monster/mingxiao/mingxiao.mdl")
        booClone.SetAnimation("dance02")
        __main__.ScheduleTask(4.0,"HamsterDance(17)")
    if 17 == thread:
        booClone.SetModel("models/character/npc/unique/downtown/pisha/pisha.mdl")
        booClone.SetAnimation("dance03")
        __main__.ScheduleTask(4.0,"HamsterDance(18)")
    if 18 == thread:
        booClone.SetModel("models/character/npc/unique/hollywood/andrei/andrei.mdl")
        booClone.SetAnimation("dance01")
        __main__.ScheduleTask(4.0,"HamsterDance(19)")
    if 19 == thread:
        booClone.SetModel("models/character/npc/unique/santa_monica/doris/doris.mdl")
        booClone.SetAnimation("dance02")
        __main__.ScheduleTask(4.0,"HamsterDance(20)")
    if 20 == thread:
        booClone.SetModel("models/character/npc/unique/downtown/bishop_vick/bishop_vick.mdl")
        booClone.SetAnimation("dance03")
        __main__.ScheduleTask(4.0,"HamsterDance(21)")
    if 21 == thread:
        booClone.SetModel("models/character/npc/unique/downtown/chunk_3/chunk_3.mdl")
        booClone.SetAnimation("dance01")
        __main__.ScheduleTask(4.0,"HamsterDance(22)")
    if 22 == thread:
        booClone.SetModel("models/character/monster/boo/boo.mdl")
        __main__.ScheduleTask(4.0,"HamsterDance(24)")
    if 23 == thread:
        booClone.SetModel("models/character/npc/unique/downtown/skelter/skelter.mdl")
        booClone.SetAnimation("dance02")
        __main__.ScheduleTask(4.0,"HamsterDance(23)")
    if 24 == thread:
        consoleutil.console("fadeout")
    return



##############################################################################
# Derived Events
##############################################################################

# InitializeModules:
#   __main__.G is not valid when vamputils loads. By keying
#   into the OnEnterMap event, we delay module initialization
#   until __main__.G is valid. Note: this will only get
#   called once, when a player begins a new game. 

def InitializeModules():
    __main__.G.vamputilinit=1
    # compmodVersion variable introduced with version 1.2
    # will allow autopatching code to be installed to help
    # mitigate issues with loading old save games. 
    __main__.G.compmodVersion=1.21
    __main__.G._pcinfo={}
    storePCInfoOnce()
    companion.initCompanion()
    possessutil.initPossessUtil()
    havenutil.initHavenUtil()
    
def OnBeginCombat():
    log("OnBeginCombat")
    companion.OnCombatStart()
    possessutil.OnCombatStart()

def OnEndCombat():
    log("OnEndCombat")
    companion.OnCombatEnd()
    possessutil.OnCombatEnd()

def IsClan(char, ClanName):
    return char.IsClan(ClanName)


##############################################################################
# DEVELOPMENT UTILITIES
##############################################################################

#
# Cheat() - Like the name
#

def Cheat():
    __main__.FindPlayer().GiveItem("item_p_occult_lockpicking")

def Boo():
    __main__.FindPlayer().GiveItem("item_p_occult_hacking")
    __main__.FindPlayer().GiveItem("item_g_eldervitaepack")
    __main__.FindPlayer().GiveItem("item_g_stake")
    __main__.FindPlayer().GiveItem("item_g_ring_gold")
    __main__.FindPlayer().GiveItem("item_g_lilly_purse")

#
# showParticle : Creates Particle effect at location.
#
# ex use: showParticle("trem_fireshield_emitter.txt",FindPlayer.GetOrigin(),(0,0,0),20)
#
# Notes: Particle takes 1 sec to appear.

def showParticle(particleName,timeout=30,loc=None,facing=None,state=0):

    # Take advantage of a bug in VTMB whereby a dynamically created
    # env_particle object will load particles/__INVALID__.txt if it
    # exists. There are limits to this functions use:
    # - If the game tries to load a map that contains one of these temp
    #   particles, the game will crash. So we MUST kill the particle.
    # - The game caches the particle info. So it can only be used once per
    #   game execution (The user must quit and restart the game for a
    #   secondary call to successfully create a different particle.)
    # - Ideal for mods that wish to allow the user to cast a single
    #   spell once anywhere in the game, but not more than once.

    if 0 == state:
        log("showParticle : Phase 1 : Creating temp particle file")
        p = __main__.FindEntityByName("temp_particle_scrap")
        if p:
            log("showParticle Error: temp_particle_scrap already exists")
            return
        if timeout < 0:
            log("showParticle Error: Invalid timeout")
            return
        cwd = fileutil.getcwd()
        srcName = cwd + "\\Vampire\\particles\\" + particleName
        if not fileutil.exists(srcName):
            log("Particle Name [%s] not found. (Did you extract it from the vpk file?)" % srcName)
            return
        trgName = cwd + "\\Vampire\\particles\\__INVALID__.txt"
        fileutil.copyfile(srcName,trgName)
        if not loc:
            loc = __main__.FindPlayer().TraceLine(50)
        if not facing:
            facing = (0,0,0)
        log("showParticle : Phase 1 : Complete")
        # delay for a second to allow disk write to complete
        __main__.ScheduleTask(1.0,"showParticle('',%d,(%d,%d,%d),(%d,%d,%d),1)" % (timeout,loc[0],loc[1],loc[2],facing[0],facing[1],facing[2]))
    elif 1 == state:
        log("showParticle : Phase 2 : Creating env_particle")
        if not fileutil.exists("Vampire\\particles\\__INVALID__.txt"):
            log("Error creating temp particle file. (Possible timing issue?)")
            return
        if not loc:
            loc = __main__.FindPlayer().TraceLine(50)
        if not facing:
            facing = (0,0,0)
        log("showParticle : Creating particle at (%d,%d,%d)" % (loc[0],loc[1],loc[2]))
        p = __main__.CreateEntityNoSpawn("env_particle", loc, facing)
        p.SetName("temp_particle_scrap")
        __main__.ScheduleTask(timeout,"showParticle('',0,None,None,2)")
    elif 2 == state:
        p = __main__.FindEntityByName("temp_particle_scrap")
        if p:
            log("showParticle : Removing particle")            
            p.Kill()
    
#
# LimitSet is a convenience function for dialogs. See Mod Developers
# Guide for use
#
def LimitSet(iteration,setid):
    npc = None
    modelindex = -1
    timestalked = -1
    oldTT = -1
    oldMI = -1
    oldID = -1
    oldIter = 512    
    try:
        npc = __main__.npc
        modelindex = npc.modelindex
        timestalked = npc.times_talked
    except:
        npc = __main__.FindPlayer()
    try:
        oldTT   = npc.limitset_timestalked
        oldMI   = npc.limitset_modelindex
        oldID   = npc.limitset_id
        oldIter = npc.limitset_iteration
    except:
        pass
    if (timestalked != oldTT) or (modelindex != oldMI) or (setid != oldID) or not (iteration > oldIter):
        npc.limitset_timestalked=timestalked
        npc.limitset_modelindex=modelindex
        npc.limitset_iteration=iteration
        npc.limitset_id=setid
        return 1
    return 0
        
#
# Start New Game, from Tutorial lwvwl, bring up console window and type
# cycleMaps() <- Auto visits every map in the game, generating the
#                map nodes so that you dont get AI disabled errors.
def cycleMaps(begin=0):
    __main__.G.cyclemaps=1
    start="noclip\nnotarget\ngod\nmap %s" % statutil.MapNames[begin]
    consoleutil.console(start)

_debugToggle=1
def debugMode():
    global _debugToggle
    """ Convenience function for exploring maps, especially otherwise hostile areas.
    param 1 : toggle. [0/1]. (def=1)"""
    if (_debugToggle):
        _debugToggle=0
        __main__.cvar.draw_hud=0
        __main__.cvar.cl_showfps=1
        __main__.cvar.cl_showpos="1"
    else:
        __main__.cvar.draw_hud=1
        __main__.cvar.cl_showfps=0
        __main__.cvar.cl_showpos="0"
    __main__.ccmd.notarget=""
    __main__.ccmd.noclip=""
    __main__.ccmd.picker=""
    __main__.ccmd.ai_show_interesting=""

def showInstances(prefix="npc_V"):
    """ Similar to the console command report_entities, however this function will tell you entity names

    param 1 : prefix. String filter. Only classes starting with filter are returned. (def="npc_V")"""

    entities = __main__.FindEntitiesByClass(prefix+"*")
    print "Class                                  Name"
    print "---------------------------------------------------------"
    for ent in entities:
      name="";
      try: name=ent.GetName()
      except: pass
      if name != "":
        print "%s %s" % (ent.classname.ljust(35),ent.GetName())

#
# This is also called when the game begins to ensure the _pcinfo array is initialized for the Embrace
# capability (We need to know what the original clan and disciplines were).

# Takes a snapshot of the PC and stores it in globally accessible array "__main__.G._pcinfo".
# Tis version gets called once per game, so we can set some values that should
# never change over the coarse of the game. 
def storePCInfoOnce():
    pc = __main__.FindPlayer()
    if pc.IsPC():
        i = 0
        while i < len(statutil.AttributeNames):
            __main__.G._pcinfo[statutil.AttributeNames[i]]=getattr(pc,"base_" + statutil.AttributeNames[i])
            i+=1
        i = 0
        while i < len(statutil.AbilityNames):
            __main__.G._pcinfo[statutil.AbilityNames[i]]=getattr(pc,"base_" + statutil.AbilityNames[i])
            i+=1
        i = 0
        while i < len(statutil.DisciplineNames):
            __main__.G._pcinfo[statutil.DisciplineNames[i]]=getattr(pc,"base_" + statutil.DisciplineNames[i])
            i+=1
        __main__.G._pcinfo["armor"]=pc.armor_rating
        __main__.G._pcinfo["masquerade"]=pc.base_masquerade
        __main__.G._pcinfo["model"]=pc.model
        __main__.G._pcinfo["experience"]=pc.base_experience
        __main__.G._pcinfo["bloodpool"]=pc.base_bloodpool
        __main__.G._pcinfo["humanity"]=pc.base_humanity

        # One time storage:
        __main__.G._pcinfo["vhistory"]=pc.vhistory
        __main__.G._pcinfo["name"]=__main__.cvar.name    
        __main__.G._pcinfo["clan"]=pc.clan

# Takes a snapshot of the PC and stores it in globally accessible array "__main__.G._pcinfo".
# Possession calls this function when the PC possesses someone to ensure the info is up to date
# so that XP re-embursment can be properly calculated when the PC unpossesses.
def storePCInfo():
    pc = __main__.FindPlayer()
    if pc.IsPC():
        i = 0
        while i < len(statutil.AttributeNames):
            __main__.G._pcinfo[statutil.AttributeNames[i]]=getattr(pc,"base_" + statutil.AttributeNames[i])
            i+=1
        i = 0
        while i < len(statutil.AbilityNames):
            __main__.G._pcinfo[statutil.AbilityNames[i]]=getattr(pc,"base_" + statutil.AbilityNames[i])
            i+=1
        i = 0
        while i < len(statutil.DisciplineNames):
            __main__.G._pcinfo[statutil.DisciplineNames[i]]=getattr(pc,"base_" + statutil.DisciplineNames[i])
            i+=1
        __main__.G._pcinfo["armor"]=pc.armor_rating
        __main__.G._pcinfo["masquerade"]=pc.base_masquerade
        __main__.G._pcinfo["model"]=pc.model
        __main__.G._pcinfo["experience"]=pc.base_experience
        __main__.G._pcinfo["bloodpool"]=pc.base_bloodpool
        __main__.G._pcinfo["humanity"]=pc.base_humanity

##############################################################################
# TODO
##############################################################################

# OnExitMap would require events placed on every trigger teleport object in the
# game.. which is why it isn't implemented

def OnExitMap(mapName):
    log("Leaving map [%s]" % mapName,1)

# OnEndDialog would require adding OnDialogEnd Events to every npc_V* class
# entity in the game.. which is why it isn't implemented

def OnEndDialog(npcName):
    log("Ending Dialog with [%s]" % npcName,1)

##############################################################################
# General Utility Functions
##############################################################################
#Sun Light damage at ocean house 
def OceanHouseSunLightDamage():
    pc=__main__.FindPlayer()
    clan = pc.clan

    if(clan == 3):
        consoleutil.console("vdmg 6")
        __main__.ccmd.SoundFire=""
    else:
        __main__.ccmd.SoundFire=""
        consoleutil.console("vdmg 3")

#------------------------------------------------------
#Pisha Book: rise player Necromancy
def PcRiseNecromancy():
    pc=__main__.FindPlayer()
    clan = pc.clan
    if (clan == 5 or clan == 7 or clan == 8):
        if(pc.CalcFeat("research") >= 9):
	    pc.BumpStat("protean", 1)
	    pc.RemoveItem("item_g_pisha_book")

def dominatePlayer():
    __main__.FindPlayer().PlayHUDParticle("D_Dominate_HUD_Cast_emitter2")

def Whisper(soundfile):
    from __main__ import pc
    pc.Whisper(soundfile)

#Blood Timer (For Antitribu mod) does not damage health
def OnBLEvent():
    pc = __main__.FindPlayer()

    BLOOD_MAX_COUNT = 30 			# 3 minute old value. 
    __main__.G.BloodCounter = __main__.G.BloodCounter + 1
     
    if(__main__.G.BloodCounter >= BLOOD_MAX_COUNT):
	print "Player loses 1 Blood point"
        if(pc.bloodpool == 15): consoleutil.console("blood 14")
        elif(pc.base_bloodpool == 14): consoleutil.console("blood 13")
        elif(pc.base_bloodpool == 13): consoleutil.console("blood 12")
	elif(pc.base_bloodpool == 12): consoleutil.console("blood 11")
	elif(pc.base_bloodpool == 11): consoleutil.console("blood 10")
	elif(pc.base_bloodpool == 10): consoleutil.console("blood 9")
	elif(pc.base_bloodpool == 9): consoleutil.console("blood 8")
	elif(pc.base_bloodpool == 8): consoleutil.console("blood 7")
	elif(pc.base_bloodpool == 7): consoleutil.console("blood 6")
	elif(pc.base_bloodpool == 6): consoleutil.console("blood 5")
	elif(pc.base_bloodpool == 5): consoleutil.console("blood 4")
	elif(pc.base_bloodpool == 4): consoleutil.console("blood 3")
	elif(pc.base_bloodpool == 3): consoleutil.console("blood 2")
	elif(pc.base_bloodpool == 2): consoleutil.console("blood 1")
	elif(pc.base_bloodpool == 1): consoleutil.console("blood 0")
	elif(pc.base_bloodpool == 0): consoleutil.console("frenzyplayer 1")  
        __main__.G.BloodCounter = 0 

#Timer Clan Weakness, test
def ClanWeakness():
    pc=__main__.FindPlayer()
    clan = pc.clan

    if (clan == 4 or clan == 6): 
	TzimisceWeakness()
    elif (clan == 7):
	NagarajaWeakness()

#Tzimisce Clan Weakness
def TzimisceWeakness():

    if(__main__.G.TzimisceRested == 1):
        TZIMISCE_MAX_COUNT = 160		# time if Tzimisce  pc already sleep in heaven : Default 5 min
        __main__.G.TzimisceCounter = __main__.G.TzimisceCounter + 1
     	
        if(__main__.G.TzimisceCounter >= TZIMISCE_MAX_COUNT):       
            __main__.G.TzimisceCounter = 0
            __main__.G.TzimisceRested = 0
            __main__.G.TzimisceTired = 0
	    print "Tzimisce Rested"
    else:     
        if(__main__.G.TzimisceTired == 1):
            TZIMISCE_MAX_COUNT = 4	# time if Tzimisce  pc not sleep in heaven (pc damage 10%) : Default 1 sec
            __main__.G.TzimisceCounter = __main__.G.TzimisceCounter + 1
     	
            if(__main__.G.TzimisceCounter >= TZIMISCE_MAX_COUNT):       
                __main__.G.TzimisceCounter = 0
	        __main__.ccmd.TzimisceWeakness=""
	        __main__.ccmd.DamagePlayer=""
	        print "Tzimisce weakness"
        else:
            TZIMISCE_MAX_COUNT = 12	# time if Tzimisce  pc want to sleep : Default 3 min
            __main__.G.TzimisceCounter = __main__.G.TzimisceCounter + 1
     	
            if(__main__.G.TzimisceCounter >= TZIMISCE_MAX_COUNT):       
                __main__.G.TzimisceCounter = 0
                __main__.G.TzimisceRested = 0
                __main__.G.TzimisceTired = 1
	        print "Tzimisce Tired"

#Nagaraja Clan Weakness
def NagarajaWeakness():

    if(__main__.G.NagarajaFeed == 1):
        NAGARAJA_MAX_COUNT = 25		# time if nagaraja pc already feed : Default 5 min
        __main__.G.NagarajaCounter = __main__.G.NagarajaCounter + 1
     	
        if(__main__.G.NagarajaCounter >= NAGARAJA_MAX_COUNT):       
            __main__.G.NagarajaCounter = 0
            __main__.G.NagarajaFeed = 0
            __main__.G.NagarajaHunger = 0
	    print "Nagaraja Feed"
    else:     
        if(__main__.G.NagarajaHunger == 1):
            NAGARAJA_MAX_COUNT = 4	# time if nagaraja pc hunger (pc damage 10%) : Default 1 sec
            __main__.G.NagarajaCounter = __main__.G.NagarajaCounter + 1
     	
            if(__main__.G.NagarajaCounter >= NAGARAJA_MAX_COUNT):       
                __main__.G.NagarajaCounter = 0
	        __main__.ccmd.NagarajaWeakness=""
	        __main__.ccmd.DamagePlayer=""
	        print "Nagaraja weakness"
        else:
            NAGARAJA_MAX_COUNT = 12	# time if nagaraja pc want to eat flesh : Default 3 min
            __main__.G.NagarajaCounter = __main__.G.NagarajaCounter + 1
     	
            if(__main__.G.NagarajaCounter >= NAGARAJA_MAX_COUNT):       
                __main__.G.NagarajaCounter = 0
                __main__.G.NagarajaFeed = 0
                __main__.G.NagarajaHunger = 1
	        print "Nagaraja Hunger"

#------------------------------------------------------
#New Hub map Lasombra Weakness:
def LasombraWeaknessCheck():
    pc=__main__.FindPlayer()
    clan = pc.clan
    lasombra_hunter = Find("lasombra_hunter")

    if (clan == 2):     
        if(lasombra_hunter):
	    return
        else: 
	    Find("hunter_lasombra_maker").Spawn()
	    print "Lasombra weakness - hunter spawn"

#------------------------------------------------------
#Bright map Setites Clan Weakness:
def SetitesWeaknessCheck():
    pc=__main__.FindPlayer()
    clan = pc.clan

    if (clan == 3):     
        if(__main__.G.SetitesWeakness == 1):
	    return
        else:
	    #consoleutil.console("vhistory setitesweaknesseffect") 
	    __main__.ccmd.SetitesScreen=""
	    __main__.G.SetitesWeakness = 1
	    print "Setites weakness - stats decreased"
	    __main__.cvar.cl_obfuscate_daylight=4
	    __main__.cvar.cl_overlay_obfuscate_scale=1.0
	    __main__.cvar.debug_stealth_light=10

def SetitesWeaknessDisable():
    Find("BrightMapSetitesWeakness").Disable()
    #__main__.ccmd.VhistoryNone=""
    __main__.G.SetitesWeakness = 0
    consoleutil.console("say Setites weakness - stats restored") 
    print "Setites weakness disabled"
    SetitesWeaknessHelper()

def SetitesWeaknessHelper():
    __main__.cvar.cl_obfuscate_daylight=0
    __main__.cvar.cl_overlay_obfuscate_scale=0.6
    __main__.cvar.debug_stealth_light=-1

#------------------------------------------------------
# OLD method, now not used  
#Masquerade map Clan Weakness: Lasombra, Ravnos
def MasqueradeMapClanWeakness():
    pc=__main__.FindPlayer()
    clan = pc.clan

    if (clan == 3):
        RAVNOS_MAX_COUNT = pc.base_humanity 	# Default 2 minute
        __main__.G.RavnosCounter = __main__.G.RavnosCounter + 1
     
        if(__main__.G.RavnosCounter >= RAVNOS_MAX_COUNT):
	    RavnosWeakness()        
            __main__.G.RavnosCounter = 0
	    print "Ravnos weakness"
    elif (clan == 2):
        LASOMBRA_MAX_COUNT = pc.base_humanity 	# Default 2 minute
        __main__.G.LasombraCounter = __main__.G.LasombraCounter + 1
     
        if(__main__.G.LasombraCounter >= LASOMBRA_MAX_COUNT):
 	    pc.SetSupernaturalLevel(5)
	    print "lasombra weakness"        
            __main__.G.LasombraCounter = 0

def RavnosWeakness():
    pc=__main__.FindPlayer()
    if(pc.base_humanity >= 9):
	pc.SetCriminalLevel(0)
    else:     
        if(pc.base_humanity >= 7):
	    pc.SetCriminalLevel(1)
        else:
            if(pc.base_humanity >= 5):
            	pc.SetCriminalLevel(2)
            else:
            	if(pc.base_humanity >= 3):
            	    pc.SetCriminalLevel(3)
                else:
            	    pc.SetCriminalLevel(5)

#------------------------------------------------------      

def GiveItem(char, ItemName):
    char.GiveItem(ItemName)

def HasItem(char, ItemName):
    return char.HasItem(ItemName)

def RemoveItem(char, ItemName):
    char.RemoveItem(ItemName)

def FrenzyTrigger(char):
    char.FrenzyTrigger(1)

# IsClan : Updated for companion mod possession ability

##def IsClan(char, ClanName):
##    if (char.clan == 0 and ClanName == "None"):
##        return 1
##    elif (char.clan == 2 and ClanName == "Brujah"):
##        return 1
##    elif (char.clan == 3 and ClanName == "Gangrel"):
##        return 1
##    elif (char.clan == 4 and ClanName == "Malkavian"):
##        return 1
##    elif (char.clan == 5 and ClanName == "Nosferatu"):
##        return 1
##    elif (char.clan == 6 and ClanName == "Toreador"):
##        return 1
##    elif (char.clan == 7 and ClanName == "Tremere"):
##        return 1
##    elif (char.clan == 8 and ClanName == "Ventrue"):
##        return 1
##    return 0

def IsMale(char):
    return char.IsMale()

def IsDead(charname):
    return __main__.G.morgue.has_key(charname)

def MarkAsDead(charname):
    __main__.G.morgue[charname] = 1

def CheckFrenzy(char, value):
    char.FrenzyCheck(value)
    return None

def NumTimesTalkedTo(num):
    if ( npc.times_talked == num ):
        return 1
    else:
        return 0

def RandomLine( NumList ):
    R = Random( time() )
    Index = R.randint(0, len(NumList)-1)
    return NumList[Index]

#called on the hubs (and possibly other maps?) to place hunters if the player violates the masquerade
def checkMasquerade():
    level = __main__.FindPlayer().GetMasqueradeLevel()
    print "level %i" % level
    if(level >= 2 and level < 5):
        #changed by dan_upright 07/12/04
        G = __main__.G
        if (G.In_Hollywood != 1 or G.Courier_QuickBuck != 1):
            i = 2
            while(i <= level):
                if(huntersDead[i - 2] == 0):
                    spawner = Find("hunter_maker_%i" % (i - 1))
                    spawner.Spawn()
                i = i + 1
        #changes end

#spawns in the appropriate cop car given the input
def spawnCopCar(i):
    ent = Find("cop_car_%i" % (i))
    if ent: ent.ScriptUnhide()
    ent = Find("cop_front_%i" % (i))
    if ent: ent.Spawn()
    ent = Find("cop_rear_%i" % (i))
    if ent: ent.Spawn()
    ent = Find("red%i" % (i))
    if ent: ent.TurnOn()
    ent = Find("blue%i" % (i))
    if ent: ent.TurnOn()
    ent = Find("cover_front_%i" % (i))
    if ent: ent.ScriptUnhide()
    ent = Find("cover_rear_%i" % (i))
    if ent: ent.ScriptUnhide()

#removes cop cars that may have been spawned onto the map previously
#argument specifies the total number of cop cars on the given hub
def removeCopCar(total):
    i = 1
    while(i <= total):
       ent = Find("cop_car_%i" % (i))
       if ent: ent.ScriptHide()
       ent = Find("red%i" % (i))
       if ent: ent.TurnOff()
       ent = Find("blue%i" % (i))
       if ent: ent.TurnOff()
       ent = Find("cover_front_%i" % (i))
       if ent: ent.ScriptHide()
       ent = Find("cover_rear_%i" % (i))
       if ent: ent.ScriptHide()
       i = i + 1
    cops = FindList("stake_out_cop")
    for cop in cops:
        cop.Kill()
    cops = FindList("cop")
    for cop in cops:
        cop.Kill()
    cops = FindList("patrol_cop_1")
    for cop in cops:
        cop.Kill()
    cops = FindList("patrol_cop_2")
    for cop in cops:
        cop.Kill()

#returns the distanceSquared between two 3D points
def distanceSquared(p1, p2):
    xDistance = (p1[0] - p2[0]) * (p1[0] - p2[0])
    yDistance = (p1[1] - p2[1]) * (p1[1] - p2[1])
    zDistance = (p1[2] - p2[2]) * (p1[2] - p2[2])
    return (xDistance + yDistance + zDistance)

#starts the BloodDoll on a random line
def doll1dlg():
    doll = Find("Doll1")
    if(__main__.IsClan(__main__.FindPlayer(), "Nosferatu")):
        return 121
    elif(__main__.G.Doll_Seduce == 1):
        return 91
    else:
        return RandomLine([1, 31, 61])

#HAVEN: used to give silver ring, added by Wesp5
def spawnRing():
    pc = __main__.FindPlayer()
    if(pc.AmmoCount("item_g_ring_silver") == 0):
        pc.GiveItem("item_g_ring_silver")
    else:
        pc.GiveAmmo("item_g_ring_silver",1)

#HAVEN: Used to place heather in the various player havens
def heatherHaven():
    G = __main__.G
    IsDead = __main__.IsDead
    heather = Find("Heather")
    if(G.Heather_Haven and not IsDead("Heather") and heather):
        heather.ScriptUnhide()
    if((G.Heather_Gone or (G.Story_State >= 75 and G.Heather_Indoors == 0)) and heather):
        heather.Kill()
    if(G.Story_State >= 30 and G.Heather_Haven and not IsDead("Heather") and G.Heather_Gone == 0 and G.Story_State < 75 and not G.Heather_Lure):
        G.Mcfly_Present = 1
        mcfly = Find("McFly")
        if mcfly: mcfly.ScriptUnhide()
    if(G.Mcfly_Leave or G.Mcfly_Feed or G.Mcfly_Dominated or G.Mcfly_Dementated or IsDead("McFly")):
        mcfly = Find("McFly")
        if mcfly: mcfly.Kill()
    if(G.Heather_Clothes and heather):
        if(G.Heather_Outfit == 0):
            heather.SetModel("models/character/npc/unique/Santa_Monica/Heather/Heather_goth.mdl")
        elif(G.Heather_Outfit == 1):
            heather.SetModel("models/character/npc/unique/Santa_Monica/Heather/Heather_3.mdl")
        else:
            heather.SetModel("models/character/npc/unique/Santa_Monica/Heather/Heather.mdl")
        G.Heather_Outfit = G.Heather_Outfit + 1
        if(G.Heather_Outfit > 2):
            G.Heather_Outfit = 0
        G.Heather_Clothes = 0
    if(IsDead("Heather") and heather):
        heather.Kill()
        mcfly = Find("mcfly")
        if mcfly: mcfly.Kill()

#HAVEN: called to see if Heather needs to leave the haven
def heatherLeaves():
    G = __main__.G
    if(G.Heather_Gone and 0==G.Heather_NoFade):
        relay = Find("heather_leaves_relay")
        relay.Trigger()

#HAVEN: called to see if mcfly leaves
def mcflyDialog():
    G = __main__.G
    if(G.Mcfly_Leave or G.Mcfly_Dominated or G.Mcfly_Dementated):
        relay = Find("mcfly_leaves_relay")
        relay.Trigger()

#HAVEN: Used for mailbox events for email quests at the haven, changed by wesp
def putStuffInMailBox():
    mailbox = Find("mailbox_haven")
    if mailbox:
        G = __main__.G
        if(G.Shubs_Email == 1 and G.Shubs_Email_Read < 1):
            mailbox.SpawnItemInContainer("item_k_shrekhub_one_key")
            G.Shubs_Email_Read = 1
        elif(G.Shubs_Email == 2 and G.Shubs_Email_Read < 2):
            mailbox.SpawnItemInContainer("item_g_wireless_camera_1")
            G.Shubs_Email_Read = 2
        elif(G.Shubs_Email == 3 and G.Shubs_Email_Read < 3):
            mailbox.SpawnItemInContainer("item_k_shrekhub_three_key")
            G.Shubs_Email_Read = 3
        elif(G.Shubs_Email == 4 and G.Shubs_Email_Read < 4):
            mailbox.SpawnItemInContainer("item_k_shrekhub_four_key")
            G.Shubs_Email_Read = 4

#HAVEN: used to determine if the player has collected any posters, changed by wesp
def posterCheck():
    G = __main__.G
    if(G.Gary_Voerman):
        poster = Find("poster_jeanette")
        poster.ScriptUnhide()
    if(G.Velvet_Poster):
        poster = Find("poster_vv")
        poster.ScriptUnhide()
    if(G.Gary_Photochop):
        poster = Find("poster_ming")
        poster.ScriptUnhide()
    if(G.Gary_Damsel):
        poster = Find("poster_damsel")
        poster.ScriptUnhide()
    if(G.Gary_Tawni):
        poster = Find("poster_tawni")
        poster.ScriptUnhide()
        if(G.Gary_Complete == 0):
            __main__.FindPlayer().SetQuest("Gary", 6)
            G.Gary_Complete = 1

#HAVEN: Updates the player's mailbox and flags if he has sent the blood in the mail, changed by wesp
def mailboxExitCheck():
    G = __main__.G
    container = Find("mailbox_haven")
    if container:
        if(G.Heather_Lure and G.Mcfly_Present and not (G.Mcfly_Leave or G.Mcfly_Feed or G.Mcfly_Dominated or G.Mcfly_Dementated)):
            G.Mcfly_Leave = 1
            pc = __main__.FindPlayer()
            pc.ChangeMasqueradeLevel(1)
            mcfly = Find("Mcfly")
            if mcfly: mcfly.Kill()
        if (container.HasItem("item_g_werewolf_bloodpack")):
            container.AddEntityToContainer("werewolf_reward")
            container.RemoveItem("item_g_werewolf_bloodpack")
            G.Werewolf_Quest = 4
            pc = __main__.FindPlayer()
            pc.SetQuest("Werewolf Blood", 3)
            pc.ChangeMasqueradeLevel(-1)
        if(container.HasItem("item_g_garys_film") and G.Story_State >= 45):
            container.RemoveItem("item_g_garys_film")
            G.Gary_Voerman = 1
        if(container.HasItem("item_g_garys_tape") and G.Velvet_Poster == 1 and G.Gary_Photochop == 0):
            container.RemoveItem("item_g_garys_tape")
            G.Gary_Photochop = 1
        if(container.HasItem("item_g_garys_photo") and G.Gary_Voerman == 1 and G.Velvet_Poster == 0):
            container.RemoveItem("item_g_garys_photo")
            G.Velvet_Poster = 1
        if(container.HasItem("item_g_garys_cd") and G.Gary_Photochop == 1 and G.Gary_Damsel == 0):
            container.RemoveItem("item_g_garys_cd")
            G.Gary_Damsel = 1
        if(container.HasItem("item_w_claws_protean5") and G.Gary_Damsel == 1 and G.Gary_Tawni == 0):
            container.RemoveItem("item_w_claws_protean5")
            G.Gary_Tawni = 1

#HAVEN: updates the player's quest when he gets the email about werewolf blood
def werewolfBloodQuestAssigned():
    G = __main__.G
    if(G.Werewolf_Quest == 0):
        G.Werewolf_Quest = 1
        __main__.FindPlayer().SetQuest("Werewolf Blood", 1)

#HAVEN: updates the player's quest when he takes the reward for the werewolf blood
def werewolfBloodQuestDone():
    __main__.FindPlayer().SetQuest("Werewolf Blood", 4)

#HAVEN:Setting Quest State Two for Mitnick Quest
def mitSetQuestTwo():
    __main__.FindPlayer().SetQuest("Mitnick", 2)

#HAVEN:Setting Quest State Three for Mitnick Quest
def mitSetQuestThree():
    __main__.FindPlayer().SetQuest("Mitnick", 3)

#HAVEN:Setting Quest State Four for Mitnick Quest
def mitSetQuestFour():
    __main__.FindPlayer().SetQuest("Mitnick", 4)

#HAVEN:Setting Quest State Five for Mitnick Quest
def mitSetQuestFive():
    __main__.FindPlayer().SetQuest("Mitnick", 5)

#HAVEN:Setting Quest State Six for Mitnick Quest
def mitSetQuestSix():
    __main__.FindPlayer().SetQuest("Mitnick", 6)

#HAVEN:Setting Quest State Seven for Mitnick Quest
def mitSetQuestSeven():
    __main__.FindPlayer().SetQuest("Mitnick", 7)

#HAVEN:Setting Quest State Eight for Mitnick Quest
def mitSetQuestEight():
    __main__.FindPlayer().SetQuest("Mitnick", 8)

#HAVEN:Setting Quest State Nine for Mitnick Quest, changed by wesp
def mitSetQuestNine():
    __main__.FindPlayer().SetQuest("Mitnick", 9)
    G.Shubs_Act = 4

#HAVEN:Setting Quest State One for Gary Quest, added by wesp
def garySetQuestOne():
    __main__.FindPlayer().SetQuest("Gary", 1)

#HAVEN:Setting Quest State Two for Gary Quest, added by wesp
def garySetQuestTwo():
    __main__.FindPlayer().SetQuest("Gary", 2)

#HAVEN:Setting Quest State One for Gary Quest, added by wesp
def garySetQuestThree():
    __main__.FindPlayer().SetQuest("Gary", 3)

#HAVEN:Setting Quest State Two for Gary Quest, added by wesp
def garySetQuestFour():
    __main__.FindPlayer().SetQuest("Gary", 4)

#HAVEN:Setting Quest State Two for Gary Quest, added by wesp
def garySetQuestFive():
    __main__.FindPlayer().SetQuest("Gary", 5)

#HAVEN:Setting Quest State One for Bertram Quest, added by wesp
def bertramSetQuest():
    __main__.FindPlayer().SetQuest("BertramCD", 4)

#HAVEN:Setting Quest State One for Tommy Quest
def tomSetQuest():
    __main__.FindPlayer().SetQuest("Tommy", 1)

#changes made by dan_upright 29/11/04
#HAVEN:Setting Quest State Four for Tommy Quest
def tomSetQuestFour():
    __main__.FindPlayer().SetQuest("Tommy", 4)
    container = Find("mailbox_haven")
    if container:
        cash = __main__.CreateEntityNoSpawn("item_m_money_envelope", (0, 0, 0), (0,0,0) )
        cash.SetName("critic_reward")
        cash.SetMoney(100)
        __main__.CallEntitySpawn(cash)
        container.AddEntityToContainer("critic_reward")
#changes end

#HAVEN: called to cause the malk newscaster conversation
def malkTalkToTV():
    G = __main__.G
    pc = __main__.FindPlayer()
    if(IsClan(pc,"Malkavian") and G.Story_State >= 65 and G.News_Spoke == 0):
        newscaster = Find("newscaster")
        malkcaster = Find("newscaster_malkavian")
        malkcaster.ScriptUnhide()
        newscaster.ScriptHide()
        newscaster.SetName("newscaster_break")
        malkcaster.SetName("newscaster")
        trigger = Find("malk_tv_trigger")
        trigger.ScriptUnhide()

#HAVEN: called after the malkavian talks to the TV
def malkTvDone():
    newscaster = Find("newscaster_break")
    malkcaster = Find("newscaster")
    malkcaster.Kill()
    newscaster.ScriptUnhide()
    newscaster.SetName("newscaster")

## Sets a Global for the hub you are in should be on each hubs logic_auto
def setArea( s ):
    G = __main__.G
    G.In_Santa_Monica = 0
    G.In_Downtown = 0
    G.In_Hollywood = 0
    G.In_Chinatown = 0
    G.Whore_Follower = 0
    if ( s == "santa_monica" ):
        print ( "*** In Santa Monica ***" )
        G.In_Santa_Monica = 1
    elif ( s == "downtown" ):
        print ( "*** In Downtown ***" )
        G.In_Downtown = 1
    elif ( s == "hollywood" ):
        print ( "*** In Hollywood ***" )
        G.In_Hollywood = 1
    elif ( s == "chinatown" ):
        print ( "*** In Chinatown ***" )
        G.In_Chinatown = 1

#EMBRACE: determines which models the sire and stakers should use.
def chooseSire():
    pc = __main__.FindPlayer()
    gender = pc.IsMale()
    clan = pc.clan
    sire = Find("Sire")
    staker1 = Find("Vampire1")
    staker2 = Find("Vampire2")
    brujah_female = "models/character/pc/female/lasombra/lasombra_female_armor_3.mdl"
    gangrel_female = "models/character/pc/female/ravnos/ravnos_female_armor_3.mdl"
    malkavian_female = "models/character/pc/female/old_clan_tzimisce/old_clan_female_armor3.mdl"
    nosferatu_female = "models/character/pc/female/nosferatu/armor0/nosferatu_Female_Armor_0.mdl"
    toreador_female = "models/character/pc/female/tzimisce/tzimisce_female_armor_2.mdl"
    tremere_female = "models/character/pc/female/nagaraja/nagaraja_female_armor_3.mdl"
    ventrue_female = "models/character/pc/female/giovanni/giovanni_female_armor3.mdl"

    brujah_male = "models/character/pc/male/lasombra/lasombra_male_armor_1.mdl"
    gangrel_male = "models/character/pc/male/ravnos/ravnos_male_armor_0.mdl"
    malkavian_male = "models/character/npc/common/sire/sire.mdl"
    nosferatu_male = "models/character/pc/male/nosferatu/armor0/Nosferatu.mdl"
    toreador_male = "models/character/pc/male/tzimisce/tzimisce_male_armor_1.mdl"
    tremere_male = "models/character/npc/common/sire/sire.mdl"
    ventrue_male = "models/character/pc/male/giovanni/giovanni_male_armor_1.mdl"
    #MALE
    if(gender):
        #BRUJAH
        if(clan == 2):
            sire.SetModel(brujah_female)
            #staker1.SetModel(malkavian_male)
            #staker2.SetModel(toreador_male)
        #GANGREL
        elif(clan == 3):
            sire.SetModel(gangrel_female)
            #staker1.SetModel(nosferatu_male)
            #staker2.SetModel(tremere_male)
        #MALKAVIAN
        elif(clan == 4):
            sire.SetModel(malkavian_female)
            #staker1.SetModel(toreador_male)
            #staker2.SetModel(ventrue_male)
        #NOSFERATU
        elif(clan == 5):
            sire.SetModel(toreador_female)
            #staker1.SetModel(tremere_male)
            #staker2.SetModel(brujah_male)
        #TOREADOR
        elif(clan == 6):
            sire.SetModel(toreador_female)
            #staker1.SetModel(ventrue_male)
            #staker2.SetModel(gangrel_male)
        #TREMERE
        elif(clan == 7):
            sire.SetModel(tremere_female)
            #staker1.SetModel(brujah_male)
            #staker2.SetModel(malkavian_male)
        #VENTRUE
        elif(clan == 8):
            sire.SetModel(ventrue_female)
            #staker1.SetModel(gangrel_male)
            #staker2.SetModel(nosferatu_male)
    else:
        #BRUJAH
        if(clan == 2):
            sire.SetModel(brujah_male)
            #staker1.SetModel(malkavian_male)
            #staker2.SetModel(toreador_male)
        #GANGREL
        elif(clan == 3):
            sire.SetModel(gangrel_male)
            #staker1.SetModel(nosferatu_male)
            #staker2.SetModel(tremere_male)
        #MALKAVIAN
        elif(clan == 4):
            sire.SetModel(malkavian_male)
            #staker1.SetModel(toreador_male)
            #staker2.SetModel(ventrue_male)
        #NOSFERATU
        elif(clan == 5):
            sire.SetModel(toreador_male)
            #staker1.SetModel(tremere_male)
            #staker2.SetModel(brujah_male)
        #TOREADOR
        elif(clan == 6):
            sire.SetModel(toreador_male)
            #staker1.SetModel(ventrue_male)
            #staker2.SetModel(gangrel_male)
        #TREMERE
        elif(clan == 7):
            sire.SetModel(tremere_male)
            #staker1.SetModel(brujah_male)
            #staker2.SetModel(malkavian_male)
        #VENTRUE
        elif(clan == 8):
            sire.SetModel(ventrue_male)
            #staker1.SetModel(gangrel_male)
            #staker2.SetModel(nosferatu_male)
    #FINISH THIS FUNCTION

#PROSTITUTES: Called when initiating dialogue with a prostitute to change her name to "prostitute"
#              MUST BE CALLED AS THE DIALOG SCRIPT and pass in the original name of the prositute (prostitute_x)
def changeProstituteName(name):
    print "change name from %s" % name
    G = __main__.G
    G.Prostitute_Name = name
    hooker = Find(name)
    hooker.SetName("prostitute")
    return 0

## PROSTITUTES: disband and feed (dialogue)
def disbandFeed():
    G = __main__.G
    print ( "*************** Disband and Feed ***************" )
    __main__.npc.SetFollowerBoss( "" )
    __main__.pc.SeductiveFeed( __main__.npc )
    G.In_Alley = 0
    resetHos()

## PROSTITUTES: Prostitute make whore your ho (from dlg)
def makeFollower():
    print ( "*************** Make Follower ***************" )
    __main__.npc.SetFollowerBoss( "!player" )

## PROSTITUTES: Causes prostitutes to flee(on events_world for each hub)
## fixed by RobinHood70
def fleeingHos():
    print ( "*************** Prostitute Flees Check ***************" )
    pc = __main__.FindPlayer()
    prostitutes = FindList("prostitut*")
    for prostitute in prostitutes:
        if(prostitute.classname != "filter_activator_name"):
            if prostitute.IsFollowerOf(pc):
                print ( "*************** Prostitute Flees ***************" )
                G = __main__.G
                G.Whore_Follower = 0
                if ( G.Romero_Whore == 2 ):
                    G.Romero_Whore = 1
                prostitute.SetFollowerBoss("")
                prostitute.SetRelationship("player D_FR 5")

## PROSTITUTES: Reset Hos, needs to be put on all trigger_change_levels on each hub
## fixed by RobinHood70
def resetHos():
    G = __main__.G
    prostitutes = FindList("prostitut*")
    for prostitute in prostitutes:
        if(prostitute.classname != "filter_activator_name"): prostitute.SetFollowerBoss("")
    G.Whore_Follower = 0
    if (G.Romero_Whore == 2):
        G.Romero_Whore = 1

#PROSTITUTES: Revert's hooker's name at end of dialogue
def revertHookerName():
    G = __main__.G
    print "change name to %s" % G.Prostitute_Name
    hooker = Find("prostitute")
    hooker.SetName(G.Prostitute_Name)

## PROSTITUTES: Prostitute Inits Dialogue (on alley triggers)
## fixed by RobinHood70
def prostituteInit():
    G = __main__.G
    print ( "*************** Check if Prostitue is Follower ***************" )
    if (G.Romero_Whore == 2):
        return
    if (G.Whore_Follower == 1):
        pc = __main__.FindPlayer()
        G.In_Alley = 1
        prostitutes = FindList("prostitut*")
        for prostitute in prostitutes:
            if(prostitute.classname != "filter_activator_name"):
                if (prostitute.IsFollowerOf( pc )):
                    prostitute.StartPlayerDialog(0)

## Refills ammo for the guns the PC has
def masterRefill(param):
    paramlist = param.split()
    quantity = atoi(paramlist[1])
    container = Find( paramlist[0] )
    player = __main__.FindPlayer()
    gotammo = 0
    chance = 0
    if container:
        print ( "****************** Found Container ********************" )
        container.DeleteItems()
        if ( player.HasItem("item_w_colt_anaconda") ):
            quantityv = quantity
            gotammo = 1
            while (quantityv > 0):
                print ( "****************** Anaconda Ammo ********************" )
                container.SpawnItemInContainer("item_w_colt_anaconda")
                quantityv = quantityv - 1
        if ( player.HasItem("item_w_crossbow") ):
            quantityv = quantity
            gotammo = 1
            while (quantityv > 0):
                print ( "****************** Bolts ********************" )
                container.SpawnItemInContainer("item_w_crossbow")
                quantityv = quantityv - 1
        if ( player.HasItem("item_w_crossbow_flaming") ):
            quantityv = quantity
            gotammo = 1
            while (quantityv > 0):
                print ( "****************** Fire Bolts ********************" )
                container.SpawnItemInContainer("item_w_crossbow_flaming")
                quantityv = quantityv - 1
        if ( player.HasItem("item_w_deserteagle") ):
            quantityv = quantity
            gotammo = 1
            while (quantityv > 0):
                print ( "****************** Deagle Clip ********************" )
                container.SpawnItemInContainer("item_w_deserteagle")
                quantityv = quantityv - 1
        ##  if ( player.HasItem("item_w_flamethrower") ):
        ##      quantityv = quantity
        ##      gotammo = 1
        ##      while (quantityv > 0):
        ##          print ( "****************** Flamethrower Fuel ********************" )
        ##          container.SpawnItemInContainer("item_w_flamethrower")
        ##          quantityv = quantityv - 1
        if ( player.HasItem("item_w_glock_17c") ):
            quantityv = quantity
            gotammo = 1
            while (quantityv > 0):
                print ( "****************** Glock Clip ********************" )
                container.SpawnItemInContainer("item_w_glock_17c")
                quantityv = quantityv - 1
        if ( player.HasItem("item_w_ithaca_m_37") ):
            quantityv = quantity
            gotammo = 1
            while (quantityv > 0):
                print ( "****************** Shotgun Shells ********************" )
                container.SpawnItemInContainer("item_w_ithaca_m_37")
                quantityv = quantityv - 1
        if ( player.HasItem("item_w_mac_10") ):
            quantityv = quantity
            gotammo = 1
            while (quantityv > 0):
                print ( "****************** Mac-10 Clip ********************" )
                container.SpawnItemInContainer("item_w_mac_10")
                quantityv = quantityv - 1
        if ( player.HasItem("item_w_rem_m_700_bach") ):
            quantityv = quantity
            gotammo = 1
            while (quantityv > 0):
                print ( "****************** Bach Ammo ********************" )
                container.SpawnItemInContainer("item_w_rem_m_700_bach")
                quantityv = quantityv - 1
        if ( player.HasItem("item_w_remington_m_700") ):
            quantityv = quantity
            gotammo = 1
            while (quantityv > 0):
                print ( "****************** Remington Ammo ********************" )
                container.SpawnItemInContainer("item_w_remington_m_700")
                quantityv = quantityv - 1
        if ( player.HasItem("item_w_steyr_aug") ):
            quantityv = quantity
            gotammo = 1
            while (quantityv > 0):
                print ( "****************** Steyr-Aug Clip ********************" )
                container.SpawnItemInContainer("item_w_steyr_aug")
                quantityv = quantityv - 1
        if ( player.HasItem("item_w_supershotgun") ):
            quantityv = quantity
            gotammo = 1
            while (quantityv > 0):
                print ( "****************** Shotgun Clip ********************" )
                container.SpawnItemInContainer("item_w_supershotgun")
                quantityv = quantityv - 1
        if ( player.HasItem("item_w_thirtyeight") ):
            quantityv = quantity
            gotammo = 1
            while (quantityv > 0):
                print ( "****************** .38 Rounds ********************" )
                container.SpawnItemInContainer("item_w_thirtyeight")
                quantityv = quantityv - 1
        if ( player.HasItem("item_w_uzi") ):
            quantityv = quantity
            gotammo = 1
            while (quantityv > 0):
                print ( "****************** Uzi Clip ********************" )
                container.SpawnItemInContainer("item_w_uzi")
                quantityv = quantityv - 1
        if ( gotammo == 1 ):
            print ( "****************** Filled Container ********************" )
            return
        else:
            print ( "****************** PC has no Guns ********************")
            R = Random( time() )
            chance = R.randint (1, 3)
            if ( chance == 1 or chance == 2 ):
                print ( "****************** Cheap Watch ********************" )
                container.SpawnItemInContainer("item_g_watch_normal")
            if ( chance == 3 ):
                print ( "****************** Nice Watch ********************" )
                container.SpawnItemInContainer("item_g_watch_fancy")
    else:
        print ( "****************** No Container ********************" )

##############################################################################
# Classes
##############################################################################
