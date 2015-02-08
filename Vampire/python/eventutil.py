import __main__
import consoleutil
import configutil
import fileutil
from logutil import log

####################
#  Custom Event Extension v1.0
#------------------
"""

Example event handlers:

"""

g_options=configutil.Options("mods.cfg")

###################
#  Variables      #
###################

attackGrapple=None
useGrapple=None

##############################################################################
# Event hook Support
##############################################################################
#
# By default, event hooks are disabled. To enable, you must edit the
# mod.cfg and add:
#
# mod_enable_event_hooks = 1

# FixBindings()
#
# In order to capture events, we have to update the users bindings. This
# happens when the game loads. If a user changes their keyboard/mouse
# layout, they will have to restart the game for event hooks to begin
# working again.
#
# Remaps the following events:
#
# Original  New           Function Hook
# ---------------------------------------
# +attack -> +m_attack -> OnAttackBegin()
# -attack -> -m_attack -> OnAttackEnd()
# +use    -> +m_use    -> OnUseBegin()
# -use    -> -m_use    -> OnUseEnd()

def FixBindings():
    if not fileutil.exists('Vampire/cfg/config.cfg'):
        log("Unable to update User Bindings. config.cfg not detected",3)
        return
    lines = fileutil.readlines('Vampire/cfg/config.cfg')
    data = ''

    for line in lines:
        slice = line.rfind('"+attack"')
        if -1 != slice:
            rbound = slice
            slice = line.find(' ')
            data = '%sbind %s "+m_attack"\n' % (data,line[slice:rbound].strip())
        else:
            slice = line.rfind('"+use"')
            if -1 != slice:
                rbound = slice
                slice = line.find(' ')
                data = '%sbind %s "+m_use"\n' % (data,line[slice:rbound].strip())
        
    consoleutil.console(data)

if g_options.get("mod_enable_event_hooks",0):
    FixBindings()

#----------------------------------------------------------
# Event Hooks
#----------------------------------------------------------

def OnPlayerAttackBegin(target):
    if target:
        print "OnPlayerAttackBegin : TARGET [%s] " % target.GetName()
        target.TakeDamage(40)
        target.ChangeSchedule('SCHED_TROIKA_ONFIRE')
    else:
        print "OnPlayerAttackBegin : NO TARGET"        

def OnPlayerAttackEnd():
    print "OnPlayerAttackEnd"

def OnPlayerUseBegin(target):
    if target:
        print "OnPlayerUseBegin : TARGET [%s] " % target.GetName()
    else:
        print "OnPlayerUseBegin : NO TARGET"        

def OnPlayerUseEnd():
    print "OnPlayerUseEnd"

#----------------------------------------------------------
# Support methods
#----------------------------------------------------------

def OnAttackBegin():
    # alt # if __main__.FindPlayer().HasItem("item_w_fists"):
    if __main__.FindPlayer().HasWeaponEquipped("item_w_fists"):
        __main__.ccmd.npc_freeze=""
        __main__.ScheduleTask(0.1,'eventutil.OnPlayerAttackHelper()')

def OnPlayerAttackHelper(done=0):
    global attackGrapple

    if done:
        OnPlayerAttackBegin(attackGrapple)
    else:
        attackGrapple=None
        npcs = __main__.FindEntitiesByClass("npc_V*")
        for npc in npcs:
            try:
                if (npc.playbackrate==0.00):
                    attackGrapple=npc
                    break;
            except:
                pass
        __main__.ccmd.npc_freeze=""
        __main__.ScheduleTask(0.1,'eventutil.OnPlayerAttackHelper(1)')

def OnAttackEnd():
    # alt # if __main__.FindPlayer().HasItem("item_w_unarmed"):
    if __main__.FindPlayer().HasWeaponEquipped("item_w_unarmed"):
        OnPlayerAttackEnd()

def OnUseBegin():
    # alt # if __main__.FindPlayer().HasItem("item_w_fists"):
    if __main__.FindPlayer().HasWeaponEquipped("item_w_fists"):
        __main__.ccmd.npc_freeze=""
        __main__.ScheduleTask(0.1,'eventutil.OnPlayerUseHelper()')

def OnPlayerUseHelper(done=0):
    global useGrapple

    if done:
        OnPlayerUseBegin(useGrapple)
    else:
        useGrapple=None
        npcs = __main__.FindEntitiesByClass("npc_V*")
        for npc in npcs:
            try:
                if (npc.playbackrate==0.00):
                    useGrapple=npc
                    break;
            except:
                pass
        __main__.ccmd.npc_freeze=""
        __main__.ScheduleTask(0.1,'eventutil.OnPlayerUseHelper(1)')

def OnUseEnd():
    # alt # if __main__.FindPlayer().HasItem("item_w_fists"):
    if __main__.FindPlayer().HasWeaponEquipped("item_w_fists"):
        OnPlayerUseEnd()
