print "loading griffith park level script"

import __main__

from __main__ import G

__main__.Level = __name__

Find = __main__.FindEntityByName

def playerEscape():
    pc = __main__.FindPlayer()
    pc.SetQuest( "Alliance", 4 )

def hackAreaChange():
    __main__.ChangeMap(3, "taxi_landmark", "taxi_trigger")

def jackEndDialog():
    G.Story_State = 90
    __main__.ScheduleTask(4.0, "__main__.ChangeMap(3, \"observahaven\", \"changelevel_observahaven\")")

#SP_OBSERVATORY_1 : This function alters the way the player can enter/leave the map based on clan
def removeSewerOrTaxi() :
    # Updated for CompMod
    # if ( __main__.IsClan(__main__.FindPlayer(), "Nosferatu") ):
    if 5 == __main__.G._pcinfo["clan"]:
        relay = Find("relay_kill_cab")
        relay.Trigger()
    else:
        relay = Find("relay_kill_sewer")
        relay.Trigger()

#SP_OBSERVATORY_2 : This function activates the particles, so it can be done in dialog
def startFire() :
    fire = Find("when_werewolves_attack_relay")
    fire.Trigger()

#SP_OBSERVATORY_2 : This function starts the cable car moving so Nines can curse at it leaving
def startCar() :
    cablecar = Find("tram_hide_relay")
    cablecar.Trigger()

#SP_OBSERVATORY_2 : This allows Nines to float one line for localization purposes
def float691():
    Nines = Find("Nines")
    Nines.PlayDialogFile("Character/dlg/MAIN CHARACTERS/nines/line691_col_e.mp3")

#Timer Clan Weakness
def WerewolfDamageX():
        WEREWORF_MAX_COUNT = 10 
        __main__.G.WerewolfDamageCounter = __main__.G.WerewolfDamageCounter + 1
     
        if(__main__.G.WerewolfDamageCounter >= WEREWORF_MAX_COUNT):
	    Find("werewolf_dead").Trigger()	        
            #__main__.G.WerewolfDamageCounter = 0
	    print "Werewolf die!"

def WerewolfDamage():   
    pc=__main__.FindPlayer()
    DmgBrawl=pc.base_brawl+pc.base_melee  
    DmgMelee=pc.base_strength+pc.base_melee 
    DmgRanged=pc.base_perception+pc.base_firearms                                      
    if(pc.HasWeaponEquipped("item_w_sheriff_sword")):
       DmgReaver=DmgMelee*7
       Find("werewolf_hit_counter").Subtract(DmgReaver)
       Find("werewolf").TakeDamage(DmgReaver)
    elif(pc.HasWeaponEquipped("item_w_flamethrower")):
       DmgFlamethrower=DmgRanged+20
       Find("werewolf_hit_counter").Subtract(DmgFlamethrower)
       Find("werewolf").TakeDamage(DmgFlamethrower)	
    else:
       DmgFire=DmgRanged*6
       if(pc.HasWeaponEquipped("item_w_remington_m_700") or pc.HasWeaponEquipped("item_w_crossbow_flaming")): 
          Find("werewolf_hit_counter").Subtract(DmgFire)
          Find("werewolf").TakeDamage(DmgFire)
       else:
          DmgClaws=DmgBrawl*7
          if(pc.HasWeaponEquipped("item_w_chang_claw") or pc.HasWeaponEquipped("item_w_chang_energy_ball") or pc.HasWeaponEquipped("item_w_claws") or pc.HasWeaponEquipped("item_w_claws_ghoul") or pc.HasWeaponEquipped("item_w_claws_protean4") or pc.HasWeaponEquipped("item_w_claws_protean5") or pc.HasWeaponEquipped("item_w_fists")):
             Find("werewolf_hit_counter").Subtract(DmgClaws)
             Find("werewolf").TakeDamage(DmgClaws)
          else:
             DmgClubs=DmgMelee*5
             if(pc.HasWeaponEquipped("item_w_baseball_bat") or pc.HasWeaponEquipped("item_w_baton") or pc.HasWeaponEquipped("item_w_severed_arm") or pc.HasWeaponEquipped("item_w_sledgehammer") or pc.HasWeaponEquipped("item_w_tire_iron") or pc.HasWeaponEquipped("item_w_torch")):
                Find("werewolf_hit_counter").Subtract(DmgClubs)
                Find("werewolf").TakeDamage(DmgClubs)
             else:
                DmgBlades=DmgMelee*6
                if(pc.HasWeaponEquipped("item_w_avamp_blade") or pc.HasWeaponEquipped("item_w_bush_hook") or pc.HasWeaponEquipped("item_w_chang_blade") or pc.HasWeaponEquipped("item_w_fireaxe") or pc.HasWeaponEquipped("item_w_katana") or pc.HasWeaponEquipped("item_w_knife") or pc.HasWeaponEquipped("item_w_occultblade")):
                   Find("werewolf_hit_counter").Subtract(DmgBlades)
                   Find("werewolf").TakeDamage(DmgBlades) 
                else:
                   Find("werewolf_hit_counter").Subtract(DmgRanged)
                   Find("werewolf").TakeDamage(DmgRanged)        

def WerewolfDead():
    wer = Find("werewolf")
    wera=wer.GetAngles()
    #wero=wer.GetOrigin()
    o = wer.GetOrigin()
    wero= (o[0],o[1],o[2]+10)
    werbody=__main__.CreateEntityNoSpawn("prop_ragdoll",wero,wera)
    werbody.SetName("werbody")
    werbody.SetModel( "models/character/monster/werewolf/werewolf.mdl")
    __main__.CallEntitySpawn(werbody)
    werbody = __main__.FindEntityByName("werbody")
    if werbody:
       werbody.SetOrigin(wero)
       werbody.SetAngles(wera)
       werbody.SetModel( "models/character/monster/werewolf/werewolf.mdl")

print "griffith park levelscript loaded"
