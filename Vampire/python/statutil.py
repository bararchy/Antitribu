from logutil import log
import fileutil

############################
#  Stat Utilities
#---------------------------

MapNames = ["sm_apartment_1","sm_asylum_1","sm_bailbonds_1","sm_basement_1" \
         ,"sm_beachhouse_1","sm_diner_1","sm_gallery_1","sm_hub_1","sm_hub_2","sm_junkyard_1" \
         ,"sm_medical_1","sm_oceanhouse_1","sm_oceanhouse_2","sm_pawnshop_1","sm_pawnshop_2" \
         ,"sm_pier_1","sm_shreknet_1", "sm_tattoo","sm_vamparena","sm_warehouse_1" \
         ,"la_abandoned_building_1","la_bradbury_2","la_bradbury_3","la_chantry_1" \
         ,"la_confession_1","la_crackhouse_1","la_dane_1","la_empire_1","la_empire_2" \
         ,"la_empire_3","la_expipe_1","la_hospital_1","la_hub_1","la_malkavian_1","la_malkavian_2" \
         ,"la_malkavian_3","la_malkavian_4","la_malkavian_5","la_museum_1","la_parkinggarage_1" \
         ,"la_PlagueBearer_Sewer_1","la_skyline_1","la_ventruetower_1","la_ventrueTower_1b" \
         ,"la_ventruetower_2","la_ventruetower_3","hw_609_1","hw_ash_sewer_1","hw_asphole_1" \
         ,"hw_cemetery_1","hw_chinese_1","hw_hub_1","hw_jewelry_1","hw_luckystar_1" \
         ,"hw_metalhead_1","hw_netcafe_1","hw_redspot_1","hw_sinbin_1","hw_tawni_1" \
         ,"hw_vesuvius_1","hw_warrens_1","hw_warrens_2","hw_warrens_3","hw_warrens_4" \
         ,"hw_warrens_5","ch_cloud_1","ch_dragon_1","ch_fishmarket_1","ch_fulab_1","ch_glaze_1" \
         ,"ch_hub_1","ch_lotus_1","ch_ramen_1","ch_shrekhub","ch_temple_1","ch_temple_2" \
         ,"ch_temple_3","ch_temple_4","ch_tsengs_1","ch_zhaos_1", "sp_giovanni_1" \
         ,"sp_giovanni_2a","sp_giovanni_2b","sp_giovanni_3","sp_giovanni_4", "sp_giovanni_5" \
         ,"sp_masquerade_1","sp_ninesintro","sp_observatory_1","sp_observatory_2", "sp_soc_1" \
         ,"sp_soc_2","sp_soc_3","sp_soc_4","sp_taxiride","sp_theatre", "sp_endsequences_a" \
         ,"sp_endsequences_b","sp_epilogue"]


# IDLookup is case sensative. You can append, but do not insert. Values
# correlate to rows in tables below and in possessutil. 

IDLookup={"_GHuman":0,   \
          "_GVampire":1, \
          "models/character/npc/unique/santa_monica/knox":2, \
          "models/character/npc/unique/santa_monica/jeanette":3, \
          "models/character/npc/unique/santa_monica/therese":4, \
          "models/character/npc/unique/santa_monica/tourette":5, \
          "models/character/npc/unique/downtown/vv":6, \
          "models/character/npc/unique/santa_monica/lily":7, \
          "models/character/npc/unique/santa_monica/e":8, \
          "models/character/npc/unique/santa_monica/vandal":9, \
          "models/character/npc/common/prostitute/prostitute_1":10, \
          "models/character/npc/common/prostitute/prostitute_2":11, \
          "models/character/npc/unique/santa_monica/bertram":12, \
          "models/character/npc/unique/santa_monica/carson":13, \
          "models/character/npc/unique/santa_monica/heather":14, \
          "models/character/npc/unique/chinatown/yukie":15, \
          "models/character/npc/unique/santa_monica/heather_e":16, \
          "models/character/npc/unique/chinatown/yukie_e":17, \
          "models/character/npc/unique/santa_monica/heather_n_e":18, \
          "models/character/npc/unique/chinatown/yukie_n_e":19, \
          "models/character/npc/unique/downtown/damsel":20, \
          "models/character/npc/unique/downtown/skelter":21, \
          "models/character/npc/unique/hollywood/ash":22, \
          #"models/character/npc/common/bum/male":23, \
          "models/character/monster/rockbiter":23, \
          "models/character/npc/unique/santa_monica/danielle":24, \
          "models/character/npc/unique/santa_monica/trip":25, \
          "models/character/npc/unique/downtown/jumbles":26, \
          "models/character/npc/unique/downtown/junky_girl":27, \
          "models/character/npc/unique/downtown/venus":28, \
          "models/character/npc/unique/hollywood/kerri":29, \
          "models/character/npc/unique/hollywood/misti":30, \
          "models/character/npc/unique/hollywood/samantha":31, \
          "models/character/npc/unique/chinatown/shu":32, \
          "models/character/npc/unique/chinatown/barabus":33, \
          "models/character/npc/unique/chinatown/hostess":34, \
          "models/character/npc/unique/giovanni_mansion/mira":35, \
          "models/character/npc/unique/giovanni_mansion/nadia":36, \
          "models/character/npc/common/blood_doll/bd_asp":37, \
          "models/character/npc/common/blood_doll/bd_asylum":38, \
          "models/character/npc/common/blood_doll/bd_confession":39, \
          "models/character/npc/common/blood_doll/bd_dragon":40, \
          "models/character/npc/common/blood_doll":41, \
          "models/character/npc/santa_monica/mcfly":42, \
          "models/character/monster/boo":43}


GENERICHUMAN=0
GENERICVAMPIRE=1

AttributeNames=["strength","dexterity","stamina","charisma","manipulation","appearance","perception","intelligence",     \
                "wits"]

# NOTE: intimidate is special case. use "intimidation" with vstats
# NOTE: computers is special case. use "computer" with vstats

AbilityNames=["brawl","dodge","subterfuge","firearms","melee","security","stealth", "finance","investigation",  \
               "academics", "intimidate", "computers"]

DisciplineNames=["animalism","auspex","blood_healing","celerity","corpus_vampirus","dementation","dominate","fortitude", \
                 "obfuscate","potence","presence","protean","thaumaturgy"]

#                  17      18       19        20          21          22         23        24
ClanNames=["clear","human","brujah","gangrel","malkavian","nosferatu","toreador","tremere","ventrue"]

# cln = clan (what shows up in character info) . See values above Special: 15 = thinblood. -1 = embraced (copy PC)
# dc  = dialog clan (How are they treated by dialogs). 1 = human, 2 = brujah, 3 = gangrel, etc... Special : thinbloods vary
# hlt = health. Weak is 60. Boss level is 200. 
# NOTE: With disciplines, -1 means they dont have it and 0 means they have it, but no points allocated
# NOTE: It is important that stats are equal to or greater than the chosen clan default values.
# NOTE: corpus_vampirus = "Blood Buff" ability
#       clan and dc values of -1 means embraced. The PC's values will be used. When clan is -1, disciplines are ignored.
#
#                                            ATTRIBUTES                                  ABILITIES                                           DISCIPLINES
# index                           0   1   2   3   4   5   6   7   8     0   1   2   3   4   5   6   7   8   9  10  11     0   1   2   3   4   5   6   7   8   9  10  11  12
# stat  Name          cln ,dc,hlt  str dex sta chr man app per int wit   bwl dge sub fir mel sec ste fin inv aca itm com   ani aus bdh cel crp dem dom for obf pot pre pro tha
stats=(("Human"      ,17 ,1 ,120 ,( 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 ),( 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ),(-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 )), \
       ("Vampire"    ,18 ,2 ,320,( 2 , 1 , 1 , 1 , 1 , 1 , 2 , 1 , 1 ),( 2 , 2 , 0 , 0 , 1 , 0 , 1 , 0 , 1 , 0 , 2 , 0 ),(-1 , 1 ,-1 , 1 , -1 ,-1 ,-1 ,-1 ,-1 , 1 ,-1 ,-1 ,-1 )), \
       ("Knox"       ,17 ,1 ,170 ,( 3 , 1 , 2 , 1 , 1 , 1 , 2 , 1 , 1 ),( 2 , 2 , 1 , 1 , 2 , 1 , 1 , 0 , 1 , 0 , 2 , 1 ),(-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 )), \
       ("Jeanette"   ,10 ,4 ,380,( 3 , 2 , 2 , 3 , 2 , 4 , 3 , 2 , 3 ),( 1 , 2 , 4 , 3 , 1 , 1 , 2 , 1 , 2 , 0 , 1 , 1 ),(-1 , 2 ,-1 ,-1 , -1 ,-1 , 3 ,-1 , 3 ,-1 ,-1 ,-1 ,-1 )), \
       ("Therese"    ,10 ,4 ,380,( 3 , 2 , 2 , 3 , 2 , 4 , 3 , 3 , 2 ),( 1 , 2 , 3 , 3 , 1 , 1 , 2 , 3 , 2 , 0 , 1 , 2 ),(-1 , 2 ,-1 ,-1 , -1 ,-1 , 3 ,-1 , 3 ,-1 ,-1 ,-1 ,-1 )), \
       ("Tourette"   ,10 ,4 ,380,( 3 , 2 , 2 , 2 , 2 , 4 , 3 , 3 , 3 ),( 1 , 2 , 4 , 3 , 1 , 1 , 2 , 2 , 2 , 0 , 1 , 2 ),(-1 , 2 ,-1 ,-1 , -1 ,-1 , 3 ,-1 , 3 ,-1 ,-1 ,-1 ,-1 )), \
       ("VV"         ,12 ,6 ,350,( 3 , 2 , 2 , 5 , 2 , 5 , 3 , 1 , 1 ),( 1 , 3 , 5 , 4 , 1 , 1 , 1 , 3 , 1 , 1 , 1 , 1 ),(-1 , 2 ,-1 , 3 , -1 ,-1 ,-1 ,-1 ,-1 ,-1 , 4 ,-1 ,-1 )), \
       ("Lily"       ,15 ,2 ,260,( 3 , 3 , 2 , 3 , 1 , 2 , 2 , 1 , 1 ),( 2 , 2 , 2 , 1 , 2 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ),(-1 , 1 ,-1 , 1 ,  1 ,-1 ,-1 ,-1 , 1 , 1 ,-1 ,-1 ,-1 )), \
       ("E"          ,15 ,2 ,240,( 3 , 3 , 3 , 2 , 1 , 2 , 2 , 1 , 1 ),( 3 , 3 , 1 , 2 , 3 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ),(-1 , 1 ,-1 , 1 ,  1 ,-1 ,-1 ,-1 , 1 , 1 ,-1 ,-1 ,-1 )), \
       ("Vandal"     ,17 ,1 ,130 ,( 2 , 1 , 2 , 1 , 1 , 1 , 3 , 2 , 1 ),( 1 , 3 , 0 , 3 , 1 , 2 , 2 , 1 , 1 , 0 , 0 , 2 ),(-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 )), \
       ("Prostitute" ,17 ,1 ,100 ,( 1 , 2 , 1 , 1 , 1 , 2 , 2 , 1 , 2 ),( 0 , 0 , 2 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 0 ),(-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 )), \
       ("Prostitute" ,17 ,1 ,100 ,( 1 , 2 , 1 , 1 , 1 , 2 , 2 , 1 , 2 ),( 0 , 0 , 2 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 0 ),(-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 )), \
       ("Bertram"    ,11 ,5 ,390,( 3 , 2 , 3 , 1 , 2 , 0 , 3 , 3 , 3 ),( 3 , 3 , 0 , 2 , 3 , 4 , 4 , 0 , 4 , 2 , 4 , 4 ),(-1 ,-1 ,-1 ,-1 , 3 ,-1 ,-1 ,-1 , 4 , 2 ,-1 ,-1 ,-1 )), \
       ("Carson"     ,17 ,1 ,175, ( 1 , 1 , 2 , 1 , 1 , 1 , 2 , 1 , 2 ),( 2 , 2 , 0 , 2 , 2 , 2 , 1 , 0 , 1 , 0 , 1 , 2 ),(-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 )), \
       ("Heather"    ,17 ,1 ,120, ( 1 , 1 , 1 , 2 , 1 , 2 , 1 , 3 , 1 ),( 0 , 1 , 2 , 1 , 0 , 2 , 1 , 3 , 1 , 4 , 0 , 4 ),(-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 )), \
       ("Yukie"      ,14 ,1 ,220,( 3 , 3 , 3 , 2 , 1 , 2 , 2 , 3 , 2 ),( 3 , 3 , 1 , 2 , 3 , 4 , 3 , 0 , 1 , 3 , 0 , 3 ),(-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 )), \
       ("Heather"    ,-1 ,-1,200,( 2 , 2 , 2 , 2 , 1 , 2 , 2 , 4 , 2 ),( 2 , 2 , 2 , 3 , 2 , 3 , 2 , 3 , 2 , 4 , 1 , 5 ),(-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 )), \
       ("Yukie"      ,-1 ,-1,200,( 4 , 4 , 4 , 3 , 1 , 2 , 3 , 3 , 3 ),( 3 , 4 , 2 , 2 , 4 , 2 , 4 , 0 , 2 , 3 , 1 , 0 ),(-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 )), \
       ("Heather"    ,-1 ,-1,200,( 3 , 2 , 3 , 1 , 1 , 0 , 3 , 4 , 3 ),( 3 , 2 , 0 , 3 , 3 , 4 , 3 , 3 , 3 , 4 , 4 , 5 ),(-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 )), \
       ("Yukie"      ,-1 ,-1,200,( 4 , 4 , 4 , 1 , 1 , 0 , 3 , 3 , 3 ),( 3 , 4 , 0 , 2 , 4 , 3 , 5 , 0 , 3 , 3 , 4 , 2 ),(-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 )), \
       ("Damsel"     ,9 ,2 ,360,( 3 , 2 , 2 , 2 , 1 , 1 , 3 , 1 , 1 ),( 3 , 3 , 1 , 1 , 2 , 1 , 1 , 1 , 1 , 1 , 3 , 1 ),(-1 ,-1 ,-1 , 4 ,-1 ,-1 ,-1 , -1 ,-1 , 2 , 3 ,-1 ,-1 )), \
       ("Skelter"    ,9 ,2 ,400,( 4 , 2 , 3 , 2 , 1 , 2 , 3 , 1 , 2 ),( 4 , 3 , 2 , 4 , 3 , 1 , 1 , 1 , 1 , 1 , 3 , 1 ),(-1 ,-1 ,-1 , 3 ,-1 ,-1 ,-1 , -1 ,-1 , 4 , 2 ,-1 ,-1 )), \
       ("Ash"        ,12 ,6 ,400,( 3 , 2 , 2 , 3 , 2 , 5 , 3 , 1 , 2 ),( 1 , 3 , 5 , 4 , 2 , 1 , 2 , 1 , 1 , 2 , 1 , 1 ),(-1 , 1 ,-1 , 4 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 , 3 ,-1 ,-1 )), \
       ("Rockbiter"        ,13 ,2 ,400 ,( 3 , 3 , 5 , 0 , 0 , 0 , 1 , 1 , 1 ),( 4 , 3 , 0 , 0 , 0 , 0 , 3 , 0 , 0 , 0 , 0 , 0 ),(-1 ,-1 ,-1 , 2 , -1 ,-1 ,-1 ,-1 ,3 ,4 ,-1 ,-1 ,-1 )), \
       ("Danielle"   ,17 ,1 ,110 ,( 1 , 2 , 1 , 2 , 1 , 2 , 2 , 1 , 2 ),( 0 , 0 , 2 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 1 ),(-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 )), \
       ("Trip"       ,17 ,1 ,135, ( 2 , 2 , 2 , 1 , 1 , 2 , 2 , 1 , 1 ),( 1 , 1 , 1 , 3 , 1 , 3 , 2 , 0 , 1 , 0 , 0 , 0 ),(-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 )), \
       ("Jumbles"    ,17 ,1 ,150, ( 2 , 2 , 2 , 1 , 1 , 1 , 2 , 1 , 1 ),( 2 , 1 , 1 , 2 , 1 , 1 , 1 , 0 , 1 , 0 , 0 , 0 ),(-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 )), \
       ("Azara"      ,17 ,1 ,150, ( 1 , 2 , 2 , 2 , 1 , 2 , 2 , 1 , 1 ),( 0 , 2 , 2 , 2 , 0 , 1 , 1 , 0 , 1 , 0 , 0 , 1 ),(-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 )), \
       ("Venus"      ,17 ,1 ,160, ( 2 , 2 , 2 , 2 , 1 , 2 , 2 , 2 , 3 ),( 1 , 2 , 1 , 3 , 1 , 2 , 1 , 0 , 1 , 0 , 0 , 1 ),(-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 )), \
       ("Kerri"      ,17 ,1 ,100 ,( 1 , 2 , 1 , 1 , 1 , 2 , 2 , 1 , 2 ),( 0 , 0 , 2 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 0 ),(-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 )), \
       ("Misti"      ,17 ,1 ,100 ,( 1 , 2 , 1 , 1 , 1 , 2 , 2 , 1 , 2 ),( 0 , 0 , 2 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 0 ),(-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 )), \
       ("Samantha"   ,17 ,1 ,120 ,( 1 , 2 , 1 , 2 , 1 , 2 , 2 , 1 , 2 ),( 0 , 0 , 2 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 1 ),(-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 )), \
       ("Shu"        ,17 ,1 ,190 ,( 2 , 1 , 2 , 1 , 1 , 1 , 3 , 2 , 1 ),( 1 , 3 , 0 , 3 , 1 , 2 , 2 , 1 , 1 , 0 , 0 , 2 ),(-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 )), \
       ("Barabus"    ,11 ,5 ,350,( 3 , 2 , 2 , 1 , 2 , 0 , 3 , 3 , 3 ),( 3 , 3 , 0 , 2 , 3 , 4 , 4 , 0 , 3 , 1 , 3 , 3 ),(-1 ,-1 ,-1 ,-1 , 2 ,-1 ,-1 ,-1 , 3 , 4 ,-1 ,-1 ,-1 )), \
       ("Kate"       ,17 ,1 ,140 ,( 1 , 2 , 1 , 2 , 1 , 2 , 2 , 1 , 2 ),( 0 , 0 , 2 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 1 ),(-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 )), \
       ("Mira"       ,17 ,1 ,150, ( 1 , 2 , 1 , 2 , 2 , 2 , 2 , 2 , 2 ),( 0 , 1 , 2 , 2 , 0 , 1 , 2 , 2 , 2 , 2 , 1 , 0 ),(-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 )), \
       ("Nadia"      ,17 ,1 ,150, ( 1 , 2 , 1 , 2 , 1 , 2 , 2 , 3 , 1 ),( 0 , 1 , 2 , 1 , 0 , 2 , 1 , 2 , 1 , 4 , 0 , 4 ),(-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 )), \
       ("Blood Doll" ,17 ,1 ,100 ,( 1 , 2 , 1 , 1 , 1 , 2 , 2 , 1 , 2 ),( 0 , 0 , 2 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 0 ),(-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 )), \
       ("Blood Doll" ,17 ,1 ,100 ,( 1 , 2 , 1 , 1 , 1 , 2 , 2 , 1 , 2 ),( 0 , 0 , 2 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 0 ),(-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 )), \
       ("Blood Doll" ,17 ,1 ,100 ,( 1 , 2 , 1 , 1 , 1 , 2 , 2 , 1 , 2 ),( 0 , 0 , 2 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 0 ),(-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 )), \
       ("Blood Doll" ,17 ,1 ,100 ,( 1 , 2 , 1 , 1 , 1 , 2 , 2 , 1 , 2 ),( 0 , 0 , 2 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 0 ),(-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 )), \
       ("Blood Doll" ,17 ,1 ,100 ,( 1 , 2 , 1 , 1 , 1 , 2 , 2 , 1 , 2 ),( 0 , 0 , 2 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 0 ),(-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 )), \
       ("McFly"      ,17 ,1 ,160 ,( 2 , 3 , 1 , 1 , 2 , 1 , 2 , 2 , 1 ),( 1 , 2 , 0 , 2 , 2 , 3 , 0 , 1 , 1 , 1 , 1 , 3 ),(-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 )), \
       ("Boo"        ,18 ,2 ,9999 ,( 1 , 5 , 5 , 5 , 5 , 5 , 5 , 3 , 3 ),( 0 , 5 , 0 , 5 , 0 , 0 , 5 , 0 , 0 , 0 , 0 , 0 ),(-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 , 3 ,-1 ,-1 ,-1 ,-1 )))


# STAT TEMPLATES: Companion Mod
# -----------------------------
# Attribute and Ability Values must be equal or greater than the stats below, or possession will break.
#
#        Name        cln ,dc,hlt  str dex sta chr man app per int wit   bwl dge sub fir mel sec ste fin inv aca itm com   ani aus bdh cel crp dem dom for obf pot pre pro tha
#       ("Human"    ,17 ,1 ,60, ( 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 ),( 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ),(-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 )),
#       ("Brujah"   ,18 ,2 ,180,( 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 ),( 1 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ),(-1 ,-1 ,-1 , 2 , 1 ,-1 ,-1 ,-1 ,-1 , 4 , 1 ,-1 ,-1 )),
#       ("Gangrel"  ,19 ,3 ,165,( 2 , 1 , 2 , 1 , 1 , 1 , 1 , 1 , 2 ),( 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ),( 2 ,-1 ,-1 ,-1 , 1 ,-1 ,-1 , 1 ,-1 ,-1 ,-1 , 4 ,-1 )),
#       ("Malkavian",20 ,4 ,150,( 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 2 ),( 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 2 , 0 , 0 , 0 ),(-1 , 1 ,-1 ,-1 , 1 , 4 ,-1 ,-1 , 2 ,-1 ,-1 ,-1 ,-1 )),
#       ("Nosferatu",21 ,5 ,180,( 1 , 1 , 1 , 1 , 1 , 0 , 1 , 1 , 1 ),( 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ),( 2 ,-1 ,-1 ,-1 , 1 ,-1 ,-1 ,-1 , 4 , 1 ,-1 ,-1 ,-1 )),
#       ("Toreador" ,22 ,6 ,150,( 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 ),( 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ),(-1 , 2 ,-1 , 4 , 1 ,-1 ,-1 ,-1 ,-1 ,-1 , 1 ,-1 ,-1 )),
#       ("Tremere"  ,23 ,7 ,120,( 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 ),( 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ),(-1 , 1 ,-1 ,-1 , 1 ,-1 , 2 ,-1 ,-1 ,-1 ,-1 ,-1 , 4 )),
#       ("Ventrue"  ,24 ,8 ,150,( 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 ),( 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ),(-1 ,-1 ,-1 ,-1 , 1 ,-1 , 4 , 1 ,-1 ,-1 , 2 ,-1 ,-1 )),
#       ("ThinBlood",15 ,2 ,120,( 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 ),( 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ),(-1 ,-1 ,-1 ,-1 , 1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 )),

# STAT TEMPLATES: (Version 1.2)
# -----------------------------
# Attribute and Ability Values must be equal or greater than the stats below, or possession will break.
#       ("Human"    ,97  ,1 ,60 ,( 2 , 1 , 1 , 1 , 1 , 1 , 2 , 1 , 2 ),( 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ),(-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 )),
#       ("Brujah"   ,66 ,2 ,180,( 3 , 2 , 1 , 1 , 1 , 1 , 2 , 1 , 2 ),( 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ),(-1 ,-1 ,-1 , 2 , 1 ,-1 ,-1 ,-1 ,-1 , 4 , 1 ,-1 ,-1 )),
#       ("Gangrel"  ,67 ,3 ,165,( 2 , 1 , 1 , 1 , 1 , 1 , 2 , 1 , 2 ),( 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ),( 2 ,-1 ,-1 ,-1 , 1 ,-1 ,-1 , 1 ,-1 ,-1 ,-1 , 4 ,-1 )),
#       ("Malkavian",68 ,4 ,150,( 2 , 1 , 2 , 1 , 1 , 1 , 2 , 1 , 2 ),( 0 , 1 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ),(-1 , 1 ,-1 ,-1 , 1 , 4 ,-1 ,-1 , 2 ,-1 ,-1 ,-1 ,-1 )),
#       ("Nosferatu",69 ,5 ,180,( 2 , 1 , 1 , 1 , 1 , 1 , 2 , 1 , 2 ),( 0 , 0 , 0 , 0 , 4 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ),( 2 ,-1 ,-1 ,-1 , 1 ,-1 ,-1 ,-1 , 4 , 1 ,-1 ,-1 ,-1 )),
#       ("Toreador" ,70 ,6 ,150,( 2 , 1 , 1 , 1 , 1 , 1 , 2 , 1 , 2 ),( 0 , 4 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ),(-1 , 2 ,-1 , 4 , 1 ,-1 ,-1 ,-1 ,-1 ,-1 , 1 ,-1 ,-1 )),
#       ("Tremere"  ,71 ,7 ,120,( 2 , 1 , 5 , 1 , 1 , 1 , 2 , 1 , 2 ),( 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ),(-1 , 1 ,-1 ,-1 , 1 ,-1 , 2 ,-1 ,-1 ,-1 ,-1 ,-1 , 4 )),
#       ("Ventrue"  ,72 ,8 ,150,( 2 , 1 , 5 , 1 , 1 , 1 , 2 , 1 , 2 ),( 0 , 0 , 0 , 0 , 4 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ),(-1 ,-1 ,-1 ,-1 , 1 ,-1 , 4 , 1 ,-1 ,-1 , 2 ,-1 ,-1 )),
#       ("ThinBlood",13 ,2 ,120,( 3 , 2 , 2 , 2 , 2 , 2 , 3 , 2 , 3 ),( 2 , 2 , 0 , 0 , 1 , 0 , 1 , 0 , 1 , 0 , 2 , 0 ),(-1 ,-1 ,-1 ,-1 , 1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 )),

NAME=0
CLAN=1
DIALOGCLAN=2
HEALTH=3
ATTRIBUTES=4
ABILITIES=5
DISCIPLINES=6

ArmorNames = ("item_a_lt_cloth","item_a_hvy_cloth","item_a_lt_leather","item_a_hvy_leather","item_a_body_armor")

g_cwd = fileutil.getcwd()
def IsSteam():
    global g_cwd
    return (-1 != g_cwd.find("steam"))

def GetAllStatsByID(id):
    """ returns tuple containing NPC stats or NONE if npc is not found in lookup table """
    global stats
    global IDLookup

    retval=None
    try:
        retval=stats[IDLookup[id]]
    except:
        pass
    return retval

def GetAttributesByID(id):
    """ returns tuple containing NPC attributes or NONE if npc is not found in lookup table """
    global stats
    global IDLookup
    global ATTRIBUTES
    retval=None
    try:
        retval=stats[IDLookup[id]][ATTRIBUTES]
    except:
        pass
    return retval

def GetAbilitiesByID(id):
    """ returns tuple containing NPC attributes or NONE if npc is not found in lookup table """
    global stats
    global IDLookup
    global ABILITIES
    retval=None
    try:
        retval=stats[IDLookup[id]][ABILITIES]
    except:
        pass
    return retval

def GetDisciplinesByID(id):
    """ returns tuple containing NPC attributes or NONE if npc is not found in lookup table """
    global stats
    global IDLookup
    global DISCIPLINES
    retval=None
    try:
        retval=stats[IDLookup[id]][DISCIPLINES]
    except:
        pass
    return retval

def GetIndex(id):
    global IDLookup
    index=-1
    try:
        index=IDLookup[id]
    except:
        pass
    return index

def GetAllStatsByIndex(index):
    global stats
    retval=None
    if index > -1:
        try:
            retval=stats[index]
        except:
            pass
    return retval

def GetAttributesByIndex(index):
    """ returns tuple containing NPC attributes or NONE if npc is not found in lookup table """
    global stats
    global ATTRIBUTES
    retval=None
    if index > -1:
        try:
            retval=stats[index][ATTRIBUTES]
        except:
            pass
    return retval

def GetAbilitiesByIndex(index):
    """ returns tuple containing NPC attributes or NONE if npc is not found in lookup table """
    global stats
    global ABILITIES
    retval=None
    if index > -1:
        try:
            retval=stats[index][ABILITIES]
        except:
            pass
    return retval

def GetDisciplinesByIndex(index):
    """ returns tuple containing NPC attributes or NONE if npc is not found in lookup table """
    global stats
    global DISCIPLINES
    retval=None
    if index > -1:
        try:
            retval=stats[index][DISCIPLINES]
        except:
            pass
    return retval
 
# There are 159 clans included with version 1.2. This array translates the value
# to one of the BASE clan values. (See clannames above). Generic vampires
# translate to Brujah
# clanNormalize=(0,1,2,3,4,5,6,7,8,1, 1,1,1,2,2,2,2,3,2,1 ,3,2,7,6,6,5,5,8,5,2 \
#              ,2,2,2,2,2,2,2,2,2,2, 2,0,3,5,5,5,5,5,5,1 ,1,1,1,1,1,1,1,1,1,5 \
#              ,5,5,5,0,0,0,2,3,4,5, 6,7,8,2,2,2,2,2,2,2 ,1,1,1,1,2,1,1,1,1,1 \
#              ,1,1,1,2,2,2,2,1,1,1, 1,1,1,1,2,1,2,2,2,0 ,0,0,1,3,3,3,1,1,7,7 \
#              ,7,1,1,1,1,1,1,1,8,1, 1,5,6,1,1,1,1,1,1,1 ,1,1,1,1,1,1,1,2,1,1 \
#              ,1,1,1,1,1,1,2,2,1,1)

clanNormalize=()

# After updating system/vdata/clandocs000.txt with additional clans to support
# possession and multiplayer, there are 323 clans with the retail version
# and 411 clans with the Steam version of the game. See the VCLAN appendix
# of the Mod Developers Guide for an explanation for these numbers.

if IsSteam():

    clanNormalize=(0,1,2,3,4,5,6,7,8,1, 1,1,1,1,1,2,0,1,2,3, 4,5,6,7,8,1,1,1,1,1 \
                ,1,2,0,1,2,3,4,5,6,7, 8,0,1,2,3,4,5,6,7,8, 1,1,1,1,1,1,2,0,1,2 \
                ,3,4,5,6,7,8,1,1,1,1, 1,1,2,0,1,2,3,4,5,6, 7,8,0,1,2,3,4,5,6,7 \
                ,8,1,1,1,1,1,1,2,0,1, 2,3,4,5,6,7,8,1,1,1, 1,1,1,2,0,1,2,3,4,5 \
                ,6,7,8,0,1,2,3,4,5,6, 7,8,1,1,1,1,1,1,2,0, 1,2,3,4,5,6,7,8,1,1 \
                ,1,1,1,1,2,0,1,2,3,4, 5,6,7,8,2,2,2,2,3,2, 1,3,2,7,6,6,5,5,8,5 \
                ,2,2,2,2,2,2,2,2,2,2, 2,2,0,3,5,5,5,5,5,5, 1,1,1,1,1,1,1,5,5,5 \
                ,5,0,0,0,0,1,1,1,1,2, 1,1,1,1,1,1,1,1,2,2, 2,2,1,2,2,2,0,0,0,1 \
                ,3,3,3,1,1,1,8,5,6,1, 1,1,1,2,1,1,1,1,1,2, 2,2,2,3,2,1,3,2,7,6 \
                ,6,5,5,8,5,2,2,2,2,2, 2,2,2,2,2,2,2,0,3,5, 5,5,5,5,5,1,1,1,1,1 \
                ,1,1,1,1,1,5,5,5,5,0, 0,0,2,3,4,5,6,7,8,2, 2,2,2,2,2,2,1,1,1,1 \
                ,2,1,1,1,1,1,1,1,1,2, 2,2,2,1,1,1,1,1,1,1, 2,1,2,2,2,0,0,0,1,3 \
                ,3,3,1,1,7,7,7,1,1,1, 1,1,1,1,8,1,1,5,6,1, 1,1,1,1,1,1,1,1,1,1 \
                ,1,1,1,2,1,1,1,1,1,1, 1,1,2,2,1,1,1,1,1,1, 1,1)

else:

    clanNormalize=(0,1,2,3,4,5,6,7,8,1, 1,1,1,1,1,2,0,1,2,3, 4,5,6,7,8,1,1,1,1,1 \
                  ,1,2,0,1,2,3,4,5,6,7, 8,0,1,2,3,4,5,6,7,8, 1,1,1,1,1,1,2,0,1,2 \
                  ,3,4,5,6,7,8,1,1,1,1, 1,1,2,0,1,2,3,4,5,6, 7,8,2,2,2,2,3,2,1,3 \
                  ,2,7,6,6,5,5,8,5,2,2, 2,2,2,2,2,2,2,2,2,2, 0,3,5,5,5,5,5,5,1,1 \
                  ,1,1,1,1,1,5,5,5,5,0, 0,0,0,1,1,1,1,2,1,1, 1,1,1,1,1,1,2,2,2,2 \
                  ,1,2,2,2,0,0,0,1,3,3, 3,1,1,1,8,5,6,1,1,1, 1,2,1,1,1,1,1,2,2,2 \
                  ,2,3,2,1,3,2,7,6,6,5, 5,8,5,2,2,2,2,2,2,2, 2,2,2,2,2,0,3,5,5,5 \
                  ,5,5,5,1,1,1,1,1,1,1, 1,1,1,5,5,5,5,0,0,0, 2,3,4,5,6,7,8,2,2,2 \
                  ,2,2,2,2,1,1,1,1,2,1, 1,1,1,1,1,1,1,2,2,2, 2,1,1,1,1,1,1,1,2,1 \
                  ,2,2,2,0,0,0,1,3,3,3, 1,1,7,7,7,1,1,1,1,1, 1,1,8,1,1,5,6,1,1,1 \
                  ,1,1,1,1,1,1,1,1,1,1, 1,2,1,1,1,1,1,1,1,1, 2,2,1,1)
    
def IsHuman(npc):
    global DIALOGCLAN
    global ClanNames

    if npc.IsPC() or npc.IsEmbraced(): return 0
    stats = GetAllStatsByID(npc.GetID())
    if stats:
        nClan=stats[DIALOGCLAN]
    else:
        nClan=clanNormalize[npc.clan]
    return (1==nClan)

def IsClan(npc,clanname):
    """ First tries to lookup pc's clan in local stats table based on current model. If the pc ID is not found, we normalize the clan based on the current instance's clan """
    import __main__
    global DIALOGCLAN
    global ClanNames
    global clanNormalize

    nClan=0
    lookup=0
    try:
        lookup=ClanNames.index(clanname.lower())
    except:
        return 0

    stats = GetAllStatsByID(npc.GetID())
    if stats:
        nClan=stats[DIALOGCLAN]
        if -1 == nClan:
            nClan=__main__.G._pcinfo["clan"]
    else:
        nClan=clanNormalize[npc.clan]
    log("statUtil : IsClan returning (lookup<%s>==nClan<%d>" % (lookup,nClan))
    return (lookup==nClan)

def GetClan(npc):
    import __main__
    global DIALOGCLAN
    global ClanNames

    nClan=0
    stats = GetAllStatsByID(npc.GetID())
    if stats:
        nClan=stats[DIALOGCLAN]
        if -1 == nClan:
            nClan=__main__.G._pcinfo["clan"]
    else:
        nClan=clanNormalize[npc.clan]
    return ClanNames[nClan]
