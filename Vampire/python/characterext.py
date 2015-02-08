import __main__
from __main__ import Character
import idutil
import dispositionutil
import expressionutil
import modelutil
import statutil
from logutil import log

####################
#  Character Extensions v1.0
#------------------
"""

Adds usefull methods to the Character Class. All npcs including the PC inherit the methods:

     IsHuman(),
     IsPC(),
     IsStealth(),
     GetItems(),
     GetLevel(),
     GetModels(),
     GetSkins(),
     GetExpressions(),
     GetDispositions(),
     GetID(),
     GetWeapon(),
     GetData(),
     SetData(),
     CloneData(),
     GetUniqueID(),
     NextSkin(),
     PrevSkin(),
     SetSkinByIndex(),
     SetSkin(),
     NextExpression()
     PrevExpression()
     SetExpressionByIndex(),
     NextDisposition()
     PrevDisposition()
     SetDispositionByIndex(),
     TraceLine(),
     Near(),

"""

###################
#  Variables      #
###################

# G.charextonce   : used to ensure 1 time ops only happen once (typically when player begins new game)
# allkeys         : LARGE tuple of all keys
# allitems        : LARGE tuple of all (non-key) game items
#
# Why the seperation? vclan does not cause you to lose your items, but it does cause you to lose your keys.

allkeys=('item_k_ash_cell_key','item_k_carson_apartment_key','item_k_chinese_theatre_key','item_k_clinic_cs_key' \
         ,'item_k_clinic_maintenance_key','item_k_clinic_stairs_key','item_k_edane_key','item_k_empire_jezebel_key' \
         ,'item_k_empire_mafia_key','item_k_fu_cell_key','item_k_fu_office_key','item_k_gallery_noir_key' \
         ,'item_k_gimble_key','item_k_hannahs_safe_key','item_k_hitman_ji_key','item_k_hitman_lu_key' \
         ,'item_k_kiki_key','item_k_leopold_int_key','item_k_lilly_key','item_k_lucky_star_murder_key' \
         ,'item_k_malcolm_office_key','item_k_malkavian_refrigerator_key','item_k_murietta_key','item_k_museum_basement_key' \
         ,'item_k_museum_office_key','item_k_museum_storage_key','item_k_museum_storeroom_key','item_k_netcafe_office_key' \
         ,'item_k_oceanhouse_basement_key','item_k_oceanhouse_sewer_key','item_k_oceanhouse_upstairs_key','item_k_oh_front_key' \
         ,'item_k_sarcophagus_key','item_k_shrekhub_four_key','item_k_shrekhub_one_key','item_k_shrekhub_three_key' \
         ,'item_k_skyline_haven_key','item_k_tatoo_parlor_key','item_k_tawni_apartment_key','item_k_tutorial_chopshop_stairs_key')

allweaps=('item_w_avamp_blade','item_w_baseball_bat','item_w_baton','item_w_bush_hook','item_w_chang_blade' \
         ,'item_w_chang_claw','item_w_chang_energy_ball','item_w_chang_ghost','item_w_claws' \
         ,'item_w_claws_ghoul','item_w_claws_protean4','item_w_claws_protean5','item_w_colt_anaconda' \
         ,'item_w_crossbow','item_w_crossbow_flaming','item_w_deserteagle','item_w_fireaxe' \
         ,'item_w_fists','item_w_flamethrower','item_w_gargoyle_fist','item_w_glock_17c' \
         ,'item_w_grenade_frag','item_w_hengeyokai_fist','item_w_ithaca_m_37','item_w_katana' \
         ,'item_w_knife','item_w_mac_10','item_w_manbat_claw','item_w_mingxiao_melee' \
         ,'item_w_mingxiao_spit','item_w_mingxiao_tentacle','item_w_occultblade','item_w_rem_m_700_bach' \
         ,'item_w_remington_m_700','item_w_sabbatleader_attack','item_w_severed_arm','item_w_sheriff_sword' \
         ,'item_w_sledgehammer','item_w_steyr_aug','item_w_supershotgun','item_w_thirtyeight' \
         ,'item_w_throwing_star','item_w_tire_iron','item_w_torch','item_w_tzimisce2_claw' \
         ,'item_w_tzimisce2_head','item_w_tzimisce3_claw','item_w_tzimisce_melee','item_w_unarmed' \
         ,'item_w_uzi','item_w_werewolf_attacks','item_w_wolf_head','item_w_zombie_fists' \
         ,'weapon_physcannon','weapon_physgun','weapon_pistol')

allitems=('item_a_body_armor','item_a_hvy_cloth','item_a_hvy_leather','item_a_lt_cloth' \
         ,'item_a_lt_leather','item_d_animalism','item_d_dementation','item_d_dominate' \
         ,'item_d_holy_light','item_d_thaumaturgy','item_g_animaltrainingbook','item_g_astrolite' \
         ,'item_g_bach_journal','item_g_badlucktalisman','item_g_bailbond_receipt','item_g_bertrams_cd' \
         ,'item_g_bloodpack','item_g_bluebloodpack','item_g_brotherhood_flyer','item_g_car_stereo' \
         ,'item_g_cash_box','item_g_chewinggum','item_g_computerbookhighgrade','item_g_computerbooklowgrade' \
         ,'item_g_driver_license_gimble','item_g_drugs_drug_box','item_g_drugs_morphine_bottle','item_g_drugs_perscription_bottle' \
         ,'item_g_drugs_pill_bottle','item_g_edane_print_report','item_g_edane_report','item_g_eldervitaepack' \
         ,'item_g_eyes','item_g_gargoyle_book','item_g_garys_cd','item_g_garys_film' \
         ,'item_g_garys_photo','item_g_garys_tape','item_g_ghost_pendant','item_g_giovanni_invitation_maria' \
         ,'item_g_giovanni_invitation_victor','item_g_guy_magazine','item_g_hannahs_appt_book','item_g_hatters_screenplay' \
         ,'item_g_horrortape_1','item_g_horrortape_2','item_g_idol_cat','item_g_idol_crane' \
         ,'item_g_idol_dragon','item_g_idol_elephant','item_g_jumbles_flyer','item_g_junkyard_businesscard' \
         ,'item_g_keyring','item_g_larry_briefcase','item_g_lilly_diary','item_g_lilly_photo' \
         ,'item_g_lilly_purse','item_g_lillyonbeachphoto','item_g_linedpaper','item_g_locket' \
         ,'item_g_lockpick','item_g_mercurio_journal','item_g_milligans_businesscard','item_g_oh_diary' \
         ,'item_g_pisha_book','item_g_pisha_fetish','item_g_pulltoy','item_g_ring03','item_g_ring_gold' \
         ,'item_g_ring_serial_killer_1','item_g_ring_serial_killer_2','item_g_ring_silver','item_g_sewerbook_1' \
         ,'item_g_stake','item_g_vampyr_apocrypha','item_g_vv_photo','item_g_wallet' \
         ,'item_g_warr_clipboard','item_g_warr_ledger_1','item_g_warr_ledger_2','item_g_warrens4_passkey' \
         ,'item_g_watch_fancy','item_g_watch_normal','item_g_werewolf_bloodpack','item_g_wireless_camera_1' \
         ,'item_g_wireless_camera_2','item_g_wireless_camera_3','item_g_wireless_camera_4','item_i_written' \
         ,'item_m_money_clip','item_m_money_envelope','item_m_wallet','item_p_gargoyle_talisman' \
         ,'item_p_occult_blood_buff','item_p_occult_dexterity','item_p_occult_dodge','item_p_occult_experience' \
         ,'item_p_occult_frenzy','item_p_occult_hacking','item_p_occult_heal_rate','item_p_occult_lockpicking' \
         ,'item_p_occult_obfuscate','item_p_occult_passive_durations','item_p_occult_presence','item_p_occult_regen' \
         ,'item_p_occult_strength','item_p_occult_thaum_damage','item_p_research_hg_computers','item_p_research_hg_dodge' \
         ,'item_p_research_hg_firearms','item_p_research_hg_melee','item_p_research_lg_computers','item_p_research_lg_dodge' \
         ,'item_p_research_lg_firearms','item_p_research_lg_stealth','item_p_research_mg_brawl','item_p_research_mg_finance' \
         ,'item_p_research_mg_melee','item_p_research_mg_security','item_s_physicshand')

###################
#  ONE TIME OPS   #
###################

def initCharacterExt():
    log("characterext : init called")
    if not __main__.G.charextonce:
        __main__.G.charextonce=1
        log("characterext : Performing One Time ops",1)
        modelutil.initModelUtil()
        __main__.G.charextonce=1
        __main__.G.npcdata={}

################
# MAIN METHODS #
################

def _TraceLine(self, dist=50):
    """ Locates point directly infront of or behind character on same plain. Use negative value for distance if desire behind """

    from math import pi as _pi
    from math import cos as _cos, sin as _sin

    pos   = self.GetOrigin()
    angle = self.GetAngles()[1]

    # degToRad : r = d/(360/2pi)
    xoffset = dist * _cos((angle/(360/(2*_pi))))
    yoffset = dist * _sin((angle/(360/(2*_pi))))

    return (pos[0]+xoffset, pos[1]+yoffset, pos[2])


def _Near(self,loc,r=200):
    """ Param 1 = location (x,y,z) Param 2 = radius [default 200]. Imagine sphere around location with radius. If npc is within sphere, returns true"""  

    # Calculate distance between 2 points in 3D:
    # Distance = SquareRoot((x2-x1)^2 + (y2-y1)^2 + (z2-z1)^2)
    # - avoid square root function. very innefficient
    # if (Distance)^2 > (x2-x1)^2 + (y2-y1)^2 + (z2-z1)^2

    loc2=self.GetOrigin()
    xd=loc2[0]-loc[0]
    yd=loc2[1]-loc[1]
    zd=loc2[2]-loc[2]
    return (r*r) > (xd*xd) + (yd*yd) + (zd*zd)

def _TraceCircle(self, radius=50, angleOffset=0):
    """ Like TraceLine, however allows the point to be circularly
        offset by degrees. For example, an angle offset of 90 would be
        the point to the players immediate left. """

    from math import pi as _pi
    from math import cos as _cos, sin as _sin

    pos   = self.GetOrigin()
    angle = self.GetAngles()[1] + angleOffset

    # degToRad : r = d/(360/2pi)
    xoffset = radius * _cos((angle/(360/(2*_pi))))
    yoffset = radius * _sin((angle/(360/(2*_pi))))

    return (pos[0]+xoffset, pos[1]+yoffset, pos[2])


def _GetItems(self):
    result = []
    for item in allitems:
      if self.HasItem(item): result.append(item)
    for weap in allweaps:
      if self.HasItem(weap): result.append(weap)
    return result

def _GetWeapon(self):
    for weap in allweaps:
      if self.HasWeaponEquipped(weap): return weap

def _GetKeys(self):
    result = []
    for key in allkeys:
      if self.HasItem(key): result.append(key)
    return result

def _IsHuman(self):
    return statutil.IsHuman(self)

def _IsStealth(self):
    squating = ((self.GetCenter()[2] - self.GetOrigin()[2]) == 18)
    return (self.active_obfuscate or squating)

def _GetLevel(self):
    """ Returns value between 1 and 20 indicating experience level of character """
    total=0
    total+=self.base_strength
    total+=self.base_dexterity
    total+=self.base_stamina
    total+=self.base_charisma
    total+=self.base_manipulation
    total+=self.base_appearance
    total+=self.base_perception
    total+=self.base_intelligence
    total+=self.base_wits
    total+=self.base_brawl
    total+=self.base_dodge
    total+=self.base_intimidate
    total+=self.base_subterfuge
    total+=self.base_firearms
    total+=self.base_melee
    total+=self.base_security
    total+=self.base_stealth
    total+=self.base_computers
    total+=self.base_finance
    total+=self.base_investigation
    total+=self.base_academics

    if self.base_animalism       != -1: total+=self.base_animalism
    if self.base_auspex          != -1: total+=self.base_auspex
    if self.base_blood_healing   != -1: total+=self.base_blood_healing
    if self.base_celerity        != -1: total+=self.base_celerity
    if self.base_corpus_vampirus != -1: total+=self.base_corpus_vampirus
    if self.base_dementation     != -1: total+=self.base_dementation
    if self.base_dominate        != -1: total+=self.base_dominate
    if self.base_fortitude       != -1: total+=self.base_fortitude
    if self.base_obfuscate       != -1: total+=self.base_obfuscate
    if self.base_potence         != -1: total+=self.base_potence
    if self.base_presence        != -1: total+=self.base_presence
    if self.base_protean         != -1: total+=self.base_protean
    if self.base_thaumaturgy     != -1: total+=self.base_thaumaturgy
    #if self.base_shield_of_faith     != -1: total+=self.base_shield_of_faith
    #if self.base_divine_vision       != -1: total+=self.base_divine_vision
    #if self.base_holy_light          != -1: total+=self.base_holy_light

    # 120 possible, Level = 1 to 20
    # Updated : Patch 1.2 - There are only 375 XP available throughout game
    # which is not enough to max out all stats. In fact the most possible is
    # 72/120. So we double the amount returned by GetLevel (by dividing by 3
    # instead of 6)

    #return (total / 6)
    return (total / 3)

def _SetData(self,key,value):
    id = self.GetID()
    log("_SetData")
    try:
        __main__.G.npcdata[id][key]=value
    except:
        log("_SetData : Exception thrown assigning value to G.npcdata[self.GetID()]")
        __main__.G.npcdata[id]={}
        __main__.G.npcdata[id][key]=value

def _GetData(self,key):
    id = self.GetID()
    result=None
    try: 
        cdata=__main__.G.npcdata[id]
    except:
        __main__.G.npcdata[id]={}
        cdata=__main__.G.npcdata[id]
    try: 
        result=cdata[key]
    except:
        pass    
    return result


def _CloneData(toEnt,fromEnt):
    idfrom = fromEnt.GetID()
    toEnt.CloneDataFromID(idfrom)

def _CloneDataFromID(toEnt,idfrom):
    idto = toEnt.GetID()

    try:
        if __main__.G.npcdata[idto]:
            keys = __main__.G.npcdata[idfrom].keys()
            for key in keys:
                __main__.G.npcdata[idto][key]=__main__.G.npcdata[idfrom][key]
    except:
        __main__.G.npcdata[idto]={}
        keys = __main__.G.npcdata[idfrom].keys()
        for key in keys:
            __main__.G.npcdata[idto][key]=__main__.G.npcdata[idfrom][key]

def _IsClan(self,clanname):
    log("characterext : _IsClan Executing....")
    return statutil.IsClan(self,clanname)
    
#####################
# Update Base Class #
#####################

Character.TraceLine=_TraceLine
Character.TraceCircle=_TraceCircle
Character.GetItems=_GetItems
Character.GetWeapon=_GetWeapon
Character.GetKeys=_GetKeys
Character.IsHuman=_IsHuman
Character.IsStealth=_IsStealth
Character.GetLevel=_GetLevel
Character.Near=_Near
Character.GetData=_GetData
Character.SetData=_SetData
Character.CloneData=_CloneData
Character.CloneDataFromID=_CloneDataFromID
Character.IsClan=_IsClan

############
# Scrapped #
############

# grapple can not be done synchronously as ccmd command waits for
# main thread to yield before executing. 
#
# NOTE: there may be a way to synchrounously grapple by scanning
# origins of all npc_V* classes and see if they are in front
# of PC based on their GetOrigin() values. (y=mx+b). Tricky part
# is doing this in 3d as you maybe looking at someone on top of a
# balcony. 
#
#def _Grapple(self,helper=0):
#    """ Discovers npc under PCs target hair. Sets global __main__.grapple to npc. None if no NPC is found """
#    if helper:
#        npcs = __main__.FindEntitiesByClass("npc_V*")
#        for npc in npcs:
#            try:
#                if (npc.playbackrate==0.00):
#                    # Do not point to an instance with a __main__.G variable, or it will crash the game
#                    __main__.grapple=npc
#                    break;
#            except:
#                pass
#        __main__.ccmd.npc_freeze=""        
#    else:
#        __main__.grapple=None
#        if not self.classname == "player":
#            print "Grapple only works for Player Entity Classes"
#            return
#        __main__.ccmd.npc_freeze=""
#        __main__.ScheduleTask(0.1,'__main__.FindPlayer().Grapple(1)')
#
#Character.Grapple=_Grapple

