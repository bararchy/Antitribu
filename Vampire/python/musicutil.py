import __main__
import statutil
import consoleutil
import configutil
import fileutil
import time
from logutil import log

####################
#  Music Manager v1.01
#------------------
"""

A prototype Music Manager for VTMB (as the original game provided
no control over the background music).

"""


# ROW 1
# "sm_apartment_1",          "Stems\Vampire Extra Music Stem5.mp3", 151, 20
# "sm_asylum_1",             "Licenced/05. chiasm - isolated.mp3",317,35
# "sm_bailbonds_1",          None, None, None
# "sm_basement_1",           "Stems/Vampire Extra Music Stem1.mp3", 111, 40
# "sm_beachhouse_1",         "Dangerous_Places.mp3", 261 , 50

# ROW 2
# "sm_diner_1",              None, None, None
# "sm_gallery_1",            "Creepy_Ambience1.mp3", 137 , 40
# "sm_hub_1",                "Santa_Monica/Santa_Monica_Theme2.mp3",304,40
# "sm_hub_2",                "Santa_Monica/Santa_Monica_Theme2.mp3",304,40
# "sm_junkyard_1",           "Stems/Vampire Extra Music Stem2.wav", 61, 30

# ROW 3
# "sm_medical_1",             None, None, None
# "sm_oceanhouse_1",          "Disturbed_and_Twisted.mp3", 270 , 40
# "sm_oceanhouse_2",          "Disturbed_and_Twisted.mp3", 270 , 40
# "sm_pawnshop_1",            None, None, None
# "sm_pawnshop_2",            None, None, None

# ROW 4
# "sm_pier_1",                None, None, None
# "sm_shreknet_1",            "Stems/Vampire Extra Music Stem5.mp3", 151, 20
# "sm_tattoo",                None, None, None
# "sm_vamparena",             None, None, None
# "sm_warehouse_1",           "Santa_Monica/Santa_Monica_Theme2.mp3", 304, 40

# ROW 5
# "la_abandoned_building_1",  "Stems/Vampire Extra Music Stem1.mp3", 111, 35
# "la_bradbury_2",            "Dangerous_Places.mp3", 261, 40
# "la_bradbury_3",            "Disturbed_and_Twisted.mp3", 270, 40
# "la_chantry_1",             "Stems/Vampire Extra MusicStem10.wav", 63, 40
# "la_confession_1",          "Licenced/Ministry - Bloodlines.mp3", 436, 25

# ROW 6
# "la_crackhouse_1",          "Dangerous_Places.mp3", 261, 40
# "la_dane_1",                "Dangerous_Places.mp3", 261, 60
# "la_empire_1",              None, None, None
# "la_empire_2",              "Dangerous_Places.mp3", 261, 50
# "la_empire_3",              None, None, None

# ROW 7
# "la_expipe_1",              "Licenced/Genitorturers - Lecher Bitch.mp3",253,25
# "la_hospital_1",            "Creepy_Ambience1.mp3",137,40
# "la_hub_1",                 "Downtown/Downtown_Theme.mp3",259,40
# "la_malkavian_1",           "Disturbed_and_Twisted.mp3", 270 , 40
# "la_malkavian_2",           "Disturbed_and_Twisted.mp3", 270 , 40

# ROW 8
# "la_malkavian_3",           "Disturbed_and_Twisted.mp3", 270 , 40
# "la_malkavian_4",           "Disturbed_and_Twisted.mp3", 270 , 40
# "la_malkavian_5",           "Disturbed_and_Twisted.mp3", 270 , 40
# "la_museum_1",              "Disturbed_and_Twisted.mp3", 270 , 40
# "la_parkinggarage_1",       "Dangerous_Places.mp3", 261, 25

# ROW 9
# "la_PlagueBearer_Sewer_1",  "Creepy_Ambience1.mp3",137,40
# "la_skyline_1",             "Stems/Vampire Extra MusicStem11.wav",78,40
# "la_ventruetower_1",        "Stems/Vampire Extra MusicStem11.wav",78,40
# "la_ventrueTower_1b",       "Stems/Vampire Extra MusicStem11.wav",78,40
# "la_ventruetower_2",        "Mission_Impossible.mp3",264,40

# ROW 10
# "la_ventruetower_3",        "Mission_Impossible.mp3",264,40
# "hw_609_1",                 "Dangerous_Places.mp3",261,50
# "hw_ash_sewer_1",           "Creepy_Ambience1.mp3",137,40
# "hw_asphole_1",             "Licenced/Asp Hole.mp3",562,30
# "hw_cemetery_1",            "Creepy_Ambience3.mp3",218,50

# ROW 11
# "hw_chinese_1",             "Creepy_Ambience3.mp3",218,60
# "hw_hub_1",                 "Hollywood/Hollywood_Theme.mp3",335,40
# "hw_jewelry_1",             "Stems/Mid_Short cutscene56.mp3",68,30
# "hw_luckystar_1",           "Stems/Mid_Short cutscene stem10.mp3",72,50
# "hw_metalhead_1",           None, None, None

# ROW 12
# "hw_netcafe_1",             "Hollywood/Hollywood_Theme.mp3",335,50
# "hw_redspot_1",             None, None, None
# "hw_sinbin_1",              None, None, None
# "hw_tawni_1",               None, None, None
# "hw_vesuvius_1",            "Hollywood/AspHole/Asp_Hole.mp3",112,30

# ROW 13
# "hw_warrens_1",             "Crypts.mp3",127,40
# "hw_warrens_2",             "Crypts.mp3",127,40
# "hw_warrens_3",             "Crypts.mp3",127,40
# "hw_warrens_4",             "Crypts.mp3",127,40
# "hw_warrens_5",             "Crypts.mp3",127,40

# ROW 14
# "ch_cloud_1",               None, None, None
# "ch_dragon_1",              None, None, None
# "ch_fishmarket_1",          None, None, None
# "ch_fulab_1",               None, None, None
# "ch_glaze_1",               "Licenced/Glaze.mp3",682,25

# ROW 15
# "ch_hub_1",                 "Chinatown/Chinatown_Theme.mp3",369,40
# "ch_lotus_1",               "Dark_Asia.mp3",232,80
# "ch_ramen_1",               None, None, None
# "ch_shrekhub",              None, None, None
# "ch_temple_1",              "Dark_Asia.mp3",232,80

# ROW 16
# "ch_temple_2",              "Dark_Asia.mp3",232,80
# "ch_temple_3",              "Dark_Asia.mp3",232,80
# "ch_temple_4",              "Dark_Asia.mp3",232,40
# "ch_tsengs_1",              None, None, None
# "ch_zhaos_1",               "Dark_Asia.mp3",232,25

# ROW 17
# "sp_giovanni_1",            "Moldy_Old_World.mp3",158,60
# "sp_giovanni_2a",           "stems/Vampire Extra Music Stem1.mp3",111,25
# "sp_giovanni_2b",           "Moldy_Old_World.mp3",158,60
# "sp_giovanni_3",            "creepy_ambience1.mp3",137,20
# "sp_giovanni_4",            "Crypts.mp3",127,40

# ROW 18
# "sp_giovanni_5",            "Crypts.mp3",127,40
# "sp_masquerade_1",          None, None, None
# "sp_ninesintro",            None, None, None
# "sp_observatory_1",         "Dangerous_Places.mp3",261,40
# "sp_observatory_2",         "Dangerous_Places.mp3",261,40

# ROW 19
# "sp_soc_1",                 "Mission_Impossible.mp3",264,40
# "sp_soc_2",                 "Stems/Vampire Extra MusicStem10.wav",63,30
# "sp_soc_3",                 "Moldy_Old_World.mp3",158,40
# "sp_soc_4",                 "Moldy_Old_World.mp3",158,40
# "sp_taxiride",              "Stems/Mid_Short cutscene72.mp3",40,75

# ROW 20
# "sp_theatre",               None, None, None
# "sp_endsequences_a",        None, None, None
# "sp_endsequences_b",        None, None, None
# "sp_epilogue"               None, None, None

g_areaSongs=(("Stems/Vampire Extra Music Stem5.mp3", 151, 20),("Licenced/05. chiasm - isolated.mp3",317,35),(None,None,None),("Stems/Vampire Extra Music Stem1.mp3", 111, 40), ("Dangerous_Places.mp3", 261 , 50) \
            ,(None,None,None),("Creepy_Ambience1.mp3", 137 , 40),("Santa_Monica/Santa_Monica_Theme2.mp3",304,40),("Santa_Monica/Santa_Monica_Theme2.mp3",304,40),("Stems/Vampire Extra Music Stem2.wav", 61, 30) \
            ,(None,None,None),("Disturbed_and_Twisted.mp3", 270 , 40),("Disturbed_and_Twisted.mp3", 270 , 40),(None,None,None),(None,None,None) \
            ,(None,None,None),("Stems/Vampire Extra Music Stem5.mp3", 151, 20),(None,None,None),(None,None,None),("Santa_Monica/Santa_Monica_Theme2.mp3", 304, 40) \
            ,("Stems/Vampire Extra Music Stem1.mp3", 111, 35),("Dangerous_Places.mp3", 261, 40),("Disturbed_and_Twisted.mp3",270,40),("Stems/Vampire Extra MusicStem10.wav", 63, 40), ("Licenced/Ministry - Bloodlines.mp3", 436, 25) \
            ,("Dangerous_Places.mp3", 261, 40),("Dangerous_Places.mp3", 261, 60),(None,None,None),("Dangerous_Places.mp3", 261, 50),(None,None,None) \
            ,("Licenced/Genitorturers - Lecher Bitch.mp3",253,25),("Creepy_Ambience1.mp3",137,40),("Downtown/Downtown_Theme.mp3",259,40),("Disturbed_and_Twisted.mp3", 270 , 40),("Disturbed_and_Twisted.mp3", 270 , 40) \
            ,("Disturbed_and_Twisted.mp3", 270 , 40),("Disturbed_and_Twisted.mp3", 270 , 40),("Disturbed_and_Twisted.mp3", 270 , 40),("Disturbed_and_Twisted.mp3", 270 , 40),("Dangerous_Places.mp3", 261, 25) \
            ,("Creepy_Ambience1.mp3",137,40),("Stems/Vampire Extra MusicStem11.wav",78,40),("Stems/Vampire Extra MusicStem11.wav",78,40),("Stems/Vampire Extra MusicStem11.wav",78,40),("Mission_Impossible.mp3",264,40) \
            ,("Mission_Impossible.mp3",264,40),("Dangerous_Places.mp3",261,50),("Creepy_Ambience1.mp3",137,40),("Licenced/Asp Hole.mp3",562,30),("Creepy_Ambience3.mp3",218,50) \
            ,("Creepy_Ambience3.mp3",218,60),("Hollywood/Hollywood_Theme.mp3",335,40),("Stems/Mid_Short cutscene56.mp3",68,30),("Stems/Mid_Short cutscene stem10.mp3",72,50), (None,None,None) \
            ,("Hollywood/Hollywood_Theme.mp3",335,50),(None,None,None),(None,None,None),(None,None,None),("Hollywood/AspHole/Asp_Hole.mp3",112,30) \
            ,("Crypts.mp3",127,40),("Crypts.mp3",127,40),("Crypts.mp3",127,40),("Crypts.mp3",127,40),("Crypts.mp3",127,40) \
            ,(None,None,None),(None,None,None),(None,None,None),(None,None,None),("Licenced/Glaze.mp3",682,25) \
            ,("Chinatown/Chinatown_Theme.mp3",369,40),("Dark_Asia.mp3",232,80),(None,None,None),(None,None,None),("Dark_Asia.mp3",232,80) \
            ,("Dark_Asia.mp3",232,80),("Dark_Asia.mp3",232,80),("Dark_Asia.mp3",232,40),(None,None,None),("Dark_Asia.mp3",232,25) \
            ,("Moldy_Old_World.mp3",158,60),("stems/Vampire Extra Music Stem1.mp3",111,25),("Moldy_Old_World.mp3",158,60),("creepy_ambience1.mp3",137,20),("Crypts.mp3",127,40) \
            ,("Crypts.mp3",127,40),(None,None,None),(None,None,None),("Dangerous_Places.mp3",261,40),("Dangerous_Places.mp3",261,40) \
            ,("Mission_Impossible.mp3",264,40),("Stems/Vampire Extra MusicStem10.wav",63,30),("Moldy_Old_World.mp3",158,40),("Moldy_Old_World.mp3",158,40),("Stems/Mid_Short cutscene72.mp3",40,75) \
            ,(None,None,None),(None,None,None),(None,None,None),(None,None,None))

g_combatSongs=((None,None,None),(None,None,None),(None,None,None),("dangerous_places_combat.mp3",183,50),("dangerous_places_combat.mp3",183,50) \
              ,(None,None,None),("Creepy_Ambience_Combat.mp3",135,40),("Default_Combat.mp3",139,70),("Default_Combat.mp3",139,70),(None,None,None) \
              ,(None,None,None),("disturbed_twisted_combat.mp3", 134, 40),("disturbed_twisted_combat.mp3", 134, 40),(None,None,None),(None,None,None) \
              ,(None,None,None),(None,None,None),(None,None,None),(None,None,None),("dangerous_places_combat.mp3",183,50) \
              ,(None,None,None),("Dangerous_Places_Combat.mp3",183,40),("Disturbed_Twisted_Combat.mp3",134,40),(None,None,None),(None,None,None) \
              ,("Dangerous_Places_Combat.mp3",183,40),("Dangerous_Places_Combat.mp3",183,60),(None,None,None),("Dangerous_Places_Combat.mp3",183,50),(None,None,None) \
              ,(None,None,None),("Creepy_Ambience_Combat.mp3",135,40),("Default_Combat.mp3",139,70),("disturbed_twisted_combat.mp3", 134, 40),("disturbed_twisted_combat.mp3", 134, 40) \
              ,("disturbed_twisted_combat.mp3", 134, 40),("disturbed_twisted_combat.mp3", 134, 40),("disturbed_twisted_combat.mp3", 134, 40),("disturbed_twisted_combat.mp3", 134, 40),("dangerous_places_combat.mp3",183,25) \
              ,("Creepy_Ambience_Combat.mp3",135,40),(None,None,None),("Creepy_Ambience_Combat.mp3",135,40),("Creepy_Ambience_Combat.mp3",135,40),("Mission_Impossible_Combat.mp3",169,40) \
              ,("Mission_Impossible_Combat.mp3",169,40),("Dangerous_Places_Combat.mp3",183,50),("Creepy_Ambience_Combat.mp3",135,40),(None,None,None),("Creepy_Ambience_Combat.mp3",135,50) \
              ,("Creepy_Ambience_Combat.mp3",135,60),("Default_Combat.mp3",139,70),(None,None,None),(None,None,None),("Stems/Mid_Short cutscene87.mp3",37,30) \
              ,("Default_Combat.mp3",139,50),(None,None,None),(None,None,None),(None,None,None),(None,None,None) \
              ,("Crypts_Combat.mp3",140,40),("Crypts_Combat.mp3",140,40),("Crypts_Combat.mp3",140,40),("Crypts_Combat.mp3",140,40),("Crypts_Combat.mp3",140,40) \
              ,(None,None,None),(None,None,None),(None,None,None),(None,None,None),("Licenced/Glaze.mp3",682,35) \
              ,("Dark_Asia_Combat.mp3",150,70),("Dark_Asia_Combat.mp3",150,80),(None,None,None),("Dark_Asia_Combat.mp3",150,50),("Dark_Asia_Combat.mp3",150,70) \
              ,("Dark_Asia_Combat.mp3",150,70),("Dark_Asia_Combat.mp3",150,70),("Dark_Asia_Combat.mp3",150,40),(None,None,None),("Dark_Asia_Combat.mp3",150,70) \
              ,("Crypts_Combat.mp3",140,80),("Crypts_Combat.mp3",140,80),("Crypts_Combat.mp3",140,80),("Creepy_Ambience_Combat.mp3",135,50),("Crypts_Combat.mp3",140,40) \
              ,("Crypts_Combat.mp3",140,40),(None,None,None),(None,None,None),("dangerous_places_combat.mp3",183,40),("dangerous_places_combat.mp3",183,40) \
              ,("Mission_Impossible_Combat.mp3",169,40),("dangerous_places_combat.mp3",183,40),("dangerous_places_combat.mp3",183,40),("dangerous_places_combat.mp3",183,40),(None,None,None) \
              ,(None,None,None),(None,None,None),(None,None,None),(None,None,None))

g_options=configutil.Options("mods.cfg")
g_bgMusicCache = []
g_cbMusicCache = []
g_bgMusicIndex = 0
g_cbMusicIndex = 0
g_inEvent=0
g_inEvent2=0
g_inEvent3=0
g_currentSong=""
g_currentStartTime=0
g_currentType=0

def OnBeginCombatMusic():
    global g_bgMusicCache
    global g_cbMusicCache
    global g_cbMusicIndex

    if g_options.get("mod_music_manager_enabled",0):
        if len(g_cbMusicCache) == 0: updateCbMusicCache()
        if len(g_cbMusicCache) != 0 or len(g_bgMusicCache) != 0:
            delay = g_options.get("mod_music_play_delay",3000)/1000.0
            __main__.ScheduleTask(delay,"musicutil.OnBeginCombatMusicHelper()")

def OnBeginNormalMusic():
    global g_bgMusicCache
    global g_bgMusicIndex
    global g_inEvent2

    if g_options.get("mod_music_manager_enabled",0):
        if len(g_bgMusicCache) == 0: updateBgMusicCache()
        if len(g_cbMusicCache) != 0 or len(g_bgMusicCache) != 0:
            delay = g_options.get("mod_music_play_delay",3000)/1000.0
            __main__.ScheduleTask(delay,"musicutil.OnBeginNormalMusicHelper()")

def OnBeginCombatMusicHelper():
    global g_cbMusicCache
    global g_cbMusicIndex
    global g_currentStartTime
    global g_currentType

    if len(g_cbMusicCache) != 0:
        g_currentStartTime = time.time()
        g_currentType=1
        if "sm_asylum_1" == __main__.G.currentMap:
            ss=__main__.FindEntitiesByClass("ambient_soundscheme")
            for s in ss:
                s.Kill()
            s=__main__.FindEntityByName("music")
            if s: s.Kill()
        index = 0
        check = 1
        mytuple = g_cbMusicCache[g_cbMusicIndex]
            
        if __main__.G.currentMap in statutil.MapNames:
            index = statutil.MapNames.index(__main__.G.currentMap)
            check = (g_areaSongs[index][0] != None)
        if check or g_options.get("mod_music_always_on",0):
            vol = g_options.get("mod_music_vol",100)/100.0
            if check and 3 == len(mytuple):
                ovol = mytuple[2]/100.0
                vol = vol * ovol
            play(mytuple[0],vol)
            if None != mytuple[1]:
                __main__.ScheduleTask(mytuple[1],"musicutil.NextSong(\"%s\",%d)" % (mytuple[0],mytuple[1]))
                g_cbMusicIndex = g_cbMusicIndex+1
                if g_cbMusicIndex == len(g_cbMusicCache): g_cbMusicIndex = 0

def OnBeginNormalMusicHelper():
    global g_bgMusicCache
    global g_bgMusicIndex
    global g_currentStartTime
    global g_currentType
    global g_inEvent2

    if 0 != g_inEvent2: return
    g_inEvent2=1

    try:
        if len(g_bgMusicCache) != 0:
            g_currentStartTime = time.time()
            g_currentType=0
            if "sm_asylum_1" == __main__.G.currentMap:
                ss=__main__.FindEntitiesByClass("ambient_soundscheme")
                for s in ss:
                    s.Kill()
                s=__main__.FindEntityByName("music")
                if s: s.Kill()
            index = 0
            check = 0
            mytuple = g_bgMusicCache[g_bgMusicIndex]

            if __main__.G.currentMap in statutil.MapNames:
                index = statutil.MapNames.index(__main__.G.currentMap)
                check = (g_areaSongs[index][0] != None)
            if check or g_options.get("mod_music_always_on",0):
                vol = g_options.get("mod_music_vol",100)/100.0
                if check and 3 == len(mytuple):
                    ovol = mytuple[2]/100.0
                    vol = vol * ovol
                play(mytuple[0],vol)
                if None != mytuple[1]:
                    __main__.ScheduleTask(mytuple[1],"musicutil.NextSong(\"%s\",%d)" % (mytuple[0],mytuple[1]))
                    g_bgMusicIndex = g_bgMusicIndex+1
                    if g_bgMusicIndex == len(g_bgMusicCache): g_bgMusicIndex = 0
    finally:
        g_inEvent2=0
    
                
def OnBeginDialog():
    if g_options.get("mod_music_manager_enabled",0):
        #TODO : Lower volume if possible?
        pass

def OnEnterMap(mapName):
    global g_cbMusicCache
    global g_cbMusicIndex
    global g_bgMusicCache
    global g_bgMusicIndex

    if g_options.get("mod_music_manager_enabled",0):
        if g_options.get("mod_music_use_custom",0):
            # testing for both 0 and 1 is used to pick up the scenario where use_custom is true but there
            # isn't anything in the directory. In that case, the default songs are used. There is only
            # 1 default per map, so when that scenario happens, the cache will have exactly 1 file. 
            lbg = len(g_bgMusicCache)
            lcb = len(g_cbMusicCache)
            if lbg == 0 or lbg == 1: updateBgMusicCache()
            if lcb == 0 or lcb == 1: updateCbMusicCache()
        else:
            updateBgMusicCache()
            updateCbMusicCache()
        if len(g_bgMusicCache) != 0:
            delay = g_options.get("mod_music_play_delay",3000)/1000.0
            __main__.ScheduleTask(delay,"musicutil.OnBeginNormalMusicHelper()")

def updateBgMusicCache():
    global g_bgMusicCache
    global g_bgMusicIndex
    global g_inEvent

    if 0 != g_inEvent: return
    g_bgMusicCache=[]

    if 0 == g_options.get("mod_music_vol",100): return
    
    g_inEvent=1
    try:
        rootdir=fileutil.getcwd()
        if ""==rootdir: return
        path = rootdir + "\\Vampire\\sound\\custom"
        if g_options.get("mod_music_use_custom",0) and fileutil.exists(path):
            songdirlist=fileutil.listfiles(path)
            if len(songdirlist) != 0:
                playList=""
                sequence=[]
                for dirfile in songdirlist:
                    if dirfile.lower().endswith(".mp3"):
                        log("Adding [%s] to Normal Music Cache" % dirfile)
                        sequence.append(dirfile)
                    elif dirfile.lower().endswith(".wav"):
                        log("Adding [%s] to Normal Music Cache" % dirfile)
                        sequence.append(dirfile)
                    elif dirfile.lower().endswith(".m3u"):
                        log("Found Playlist [%s]" % dirfile)
                        playList=dirfile
                if "" != playList:
                    filename = "Vampire/sound/custom/" + playList
                    if fileutil.exists(filename):
                        ordered=[]
                        log("Loading Playlist [%s]" % playList)
                        lines=fileutil.readlines(filename)
                        for line in lines:
                            fixed=line.strip()
                            if fixed.lower().endswith(".mp3") or fixed.lower().endswith(".wav"):
                                fixed2 = fixed.replace("\\","/")
                                lbound = fixed2.rfind("/")
                                extract_name=""
                                if -1 == lbound:
                                    extract_name=fixed2
                                else:
                                    extract_name=fixed2[lbound+1:]
                                if extract_name in sequence:
                                    ordered.append(extract_name)
                        if len(ordered) > 0:
                            sequence=ordered
                    else:
                        log("File [%s] NOT FOUND" % playList)
                if len(sequence) != 0:
                    i = 0
                    while i < len(sequence):
                        time=200
                        path = rootdir + "\\Vampire\\sound\\custom\\"
                        if sequence[i].lower().endswith(".mp3"):
                            if isValidMP3(path,sequence[i]):
                                path = path + sequence[i]
                                time = fileutil.getsize(path)/15625
                                g_bgMusicCache.append(("/custom/%s" % sequence[i], time))
                        elif sequence[i].lower().endswith(".wav"):
                            path = path + sequence[i]
                            time = fileutil.getsize(path)/175250
                            g_bgMusicCache.append(("/custom/%s" % sequence[i], time))
                        i=i+1
                            
        if 0 == len(g_bgMusicCache):
            # either mod_music_use_custom was false, or there wasn't anything to be found.
            if __main__.G.currentMap in statutil.MapNames:
                tuple = g_areaSongs[statutil.MapNames.index(__main__.G.currentMap)]
                if None != tuple[0]:
                    g_bgMusicCache.append(("/music/%s" % tuple[0], tuple[1], tuple[2]))
                    
        if g_bgMusicIndex >= len(g_bgMusicCache):
            g_bgMusicIndex=0
    finally:
        g_inEvent=0
            
def updateCbMusicCache():
    global g_cbMusicCache
    global g_cbMusicIndex
    global g_inEvent

    if 0 != g_inEvent: return
    g_cbMusicCache=[]
    if 0 == g_options.get("mod_music_vol",100): return

    g_inEvent=1
    try:
        rootdir=fileutil.getcwd()    
        if ""==rootdir: return
        path = rootdir + "\\Vampire\\sound\\custom\\combat"
        if g_options.get("mod_music_use_custom",0) and fileutil.exists(path):
            songdirlist=fileutil.listfiles(path)
            if len(songdirlist) != 0:
                playList=""
                sequence=[]
                for dirfile in songdirlist:
                    if dirfile.lower().endswith(".mp3"):
                        log("Adding [%s] to Combat Music Cache" % dirfile)
                        sequence.append(dirfile)
                    elif dirfile.lower().endswith(".wav"):
                        log("Adding [%s] to Combat Music Cache" % dirfile)
                        sequence.append(dirfile)
                    elif dirfile.lower().endswith(".m3u"):
                        log("Found Playlist [%s]" % dirfile)
                        playList=dirfile
                if "" != playList:
                    filename = "Vampire/sound/custom/combat/" + playList
                    if fileutil.exists(filename):
                        ordered=[]
                        log("Loading Playlist [%s]" % playList)
                        lines=fileutil.readlines(filename)
                        for line in lines:
                            fixed=line.strip()
                            if fixed.lower().endswith(".mp3") or fixed.lower().endswith(".wav"):
                                fixed2 = fixed.replace("\\","/")
                                lbound = fixed2.rfind("/")
                                extract_name=""
                                if -1 == lbound:
                                    extract_name=fixed2
                                else:
                                    extract_name=fixed2[lbound+1:]
                                if extract_name in sequence:
                                    ordered.append(extract_name)
                        if len(ordered) > 0:
                            sequence=ordered
                    else:
                        log("File [%s] NOT FOUND" % playList)
                if len(sequence) != 0:
                    i = 0
                    while i < len(sequence):
                        time=200
                        path = rootdir + "\\Vampire\\sound\\custom\\combat\\"
                        if sequence[i].lower().endswith(".mp3"):
                            if isValidMP3(path,sequence[i]):
                                path = path + sequence[i]
                                time = fileutil.getsize(path)/15625
                                g_cbMusicCache.append(("/custom/combat/%s" % sequence[i], time))
                        elif sequence[i].lower().endswith(".wav"):
                            path = path + sequence[i]                        
                            time = fileutil.getsize(path)/175250
                            g_cbMusicCache.append(("/custom/combat/%s" % sequence[i], time))
                        i=i+1
        if 0 == len(g_cbMusicCache):
            # either mod_music_use_custom was false, or there wasn't anything to be found.
            if __main__.G.currentMap in statutil.MapNames:
                tuple = g_combatSongs[statutil.MapNames.index(__main__.G.currentMap)]
                if None != tuple[0]:
                    g_cbMusicCache.append(("/music/%s" % tuple[0], tuple[1], tuple[2]))

        if g_cbMusicIndex >= len(g_cbMusicCache):
            g_cbMusicIndex=0

    finally:
        g_inEvent=0

def NextSong(originalsong,length):
    global g_currentSong
    global g_currentStartTime
    global g_currentType

    log ("musicutil : NextSong()")
    log("Testing originalsong [%s] == g_currentSong [%s]" % (originalsong, g_currentSong))
    if  originalsong == g_currentSong:
        log("Original Song = Current Song")
        now = (time.time()+5) - length
        log("Testing now [%d] > g_currentStartTime [%d]" % (now, g_currentStartTime))
        if now > g_currentStartTime:
            log("Time Test Passed")
            if g_currentType:
                log("Activating Combat Music")
                OnBeginCombatMusicHelper()
            else:
                log("Activating Normal Music")
                OnBeginNormalMusicHelper()

# returns name of file if it is OK
# returns NONE if file is NOT OK.
def isValidMP3(path,filename):
    fullpath = path + filename
    if -1 == fullpath.find("\\Vampire\\"): 
         log("musicutil : processMP3 - Invalid Directory",3)
         return 0
    if not fileutil.exists(fullpath):
         log("musicutil : processMP3 - [%s] does not exist in Directory [%s]" % (filename,path), 3)
         return 0
    fsize = fileutil.getsize(fullpath)    
    if fsize < 11:
         log("musicutil : processMP3 - Not a valid MP3",3)
         return 0
    if fsize > g_options.get("mod_music_mp3_size_cap",16777216):
         log("musicutil : processMP3 - MP3 is larger than size Cap. Ignoring.",2)
         return 0
    if g_options.get("mod_music_autofix_MP3",0) and g_options.get("mod_autofix_acknowledge",0):
        # MP3s will be verified at play time.
        return 1
    else:
        # Ignore if it has MP3 Headers
        fsrc = None
        try:
            fsrc = open(fullpath, 'rb')
            ID3 = fsrc.read(3)
            if ID3 != "ID3":
                fsrc.close()
                fsrc = None
                return 1
        finally:
            if fsrc: fsrc.close()

    log("musicutil : processMP3 - MP3 [%s] has ID3v2 tags. Ignoring" % filename, 2)
    return 0

g_mmcacheid=0
def play(filename, vol):
    global g_currentSong
    global g_mmcacheid
    global g_inEvent3

    if None == filename:
        log("musicutil: play(filename[None]) Aborting")
        return
    
    log("musicutil : play(filename[%s],vol[%f])" % (filename,vol))

    if 0 == g_inEvent3:
        g_inEvent3 = 1
    else:
        log("musicutil : play - 2nd Thread Ignored")
        return

    rootdir=fileutil.getcwd()    
    if ""==rootdir:
        g_inEvent3=0
        return

    fix1 = filename.replace("/","\\")
    fullpath = rootdir + "\\Vampire\\sound" + fix1

    if not fileutil.exists(fullpath):
         log("musicutil : play - [%s] does not exist. (Default music?) Sending to console anyway." % filename, 2)
         g_currentSong  = filename
         consoleutil.console("stopsound\nplayvol \"%s\" %f" % (filename,vol))
         g_inEvent3=0
         return

    if filename.lower().endswith(".wav"):
        g_currentSong  = filename
        consoleutil.console("stopsound\nplayvol \"%s\" %f" % (filename,vol))
    elif filename.lower().endswith(".mp3"):
        
        # By commenting this out, it also checks original MP3s (incase
        # users listen to them with Windows Media Player and invalidate them).
        #
        # if not g_options.get("mod_music_use_custom",0):
        #    g_currentSong = filename
        #    consoleutil.console("stopsound\nplayvol \"%s\" %f" % (filename,vol))
        #    g_inEvent3=0
        #    return
        
        fsize = fileutil.getsize(fullpath)    
        if fsize < 11:
             log("musicutil : play - Not a valid MP3",3)
             g_inEvent3=0
             return
        if fsize > g_options.get("mod_music_mp3_size_cap",16777216):
             log("musicutil : play - MP3 is larger than size Cap. Ignoring.",2)
             g_inEvent3=0
             return
        if not (g_options.get("mod_music_autofix_MP3",0) and g_options.get("mod_autofix_acknowledge",0)):
            log("musicutil : play - Autofix disabled. Skipping ID3v2 checks")
            # if autofix is off, Bad MP3s should have been filtered. If someone calls this method
            # directly with a bad MP3, that is their own fault.
            g_currentSong  = filename
            consoleutil.console("stopsound\nplayvol \"%s\" %f" % (filename,vol))
            g_inEvent3=0
            return
        fsrc = None
        fdst = None
        try:
            fsrc = open(fullpath, 'rb')
            ID3 = fsrc.read(3)
            if ID3 != "ID3":
                fsrc.close()
                fsrc = None
                g_currentSong  = filename
                consoleutil.console("stopsound\nplayvol \"%s\" %f" % (filename,vol))
                g_inEvent3=0
                return
            g_mmcacheid = g_mmcacheid + 1
            fixedfile = "mmcache%d.mp3" % g_mmcacheid
            if g_mmcacheid >= 2: g_mmcacheid = 0
            fixedpath = rootdir + "\\Vampire\\sound\\" + fixedfile
            fsrc.seek(6)
            id3v2HeaderSizeStr = fsrc.read(4);
            id3v2HeaderSize = bin2dec(bytes2bin(id3v2HeaderSizeStr, 7)) + 10
            log("musicutil : play - Header size: [%d]" % id3v2HeaderSize)
            # sanity check : Header can't be larger than the filesize.
            if fsize < id3v2HeaderSize:
                log("musicutil : play - MP3 [%s] has illegal ID3v2 headers. Ignoring." % filename, 2)
                fsrc.close()
                fsrc = None
                g_inEvent3=0
                return
            fsrc.seek(id3v2HeaderSize)
            log("musicutil : play - [%s] has id3v2 headers. Creating temp file [%s]." % (filename,fixedfile), 2)
            fdst = open(fixedpath, 'wb')
            # length = fsize - id3v2HeaderSize
            # fdst.write(fsrc.read(length))
            length=16*1024
            while 1:
                buf = fsrc.read(length)
                if not buf:
                    break
                fdst.write(buf)
            fsrc.close()
            fdst.close()
            fsrc = None
            fdst = None
            log("musicutil : play - Temporary file [%s] created." % fixedfile)
            g_currentSong  = filename
            consoleutil.console("stopsound\nplayvol \"%s\" %f" % (fixedfile,vol))
        finally:
            if fsrc: fsrc.close()
            if fdst: fdst.close()
    g_inEvent3=0     
    
# Note : Hi order bit is ignored in MP3 data, so sz should be 7.  And if
# converting from dec to bytes, you must derive value without the help of
# the high order bit. (every 8th bit must be 0)
#
# format of MP3 size field (4 bytes, 16 bits) : [0xxxxxxx][0xxxxxxx][0xxxxxxx][0xxxxxxx]
#
# the "x" may be a 0 or 1, but the "0" must be 0. Right-Most x is the low order bit (value 1)
# so the max size of Header = [01111111011111110111111101111111] or 2,139,062,143.
def bytes2bin(bytes, sz = 8):
   if sz < 1 or sz > 8:
      raise ValueError("Invalid sz value: " + str(sz));

   retVal = [];
   for b in bytes:
      bits = [];
      b = ord(b);
      while b > 0:
         bits.append(b & 1);
         b >>= 1;

      if len(bits) < sz:
         bits.extend([0] * (sz - len(bits)));
      elif len(bits) > sz:
         bits = bits[:sz];

      # Big endian byte order.
      bits.reverse();
      retVal.extend(bits);

   if len(retVal) == 0:
      retVal = [0];
   return retVal;

def bin2dec(x):
   bits = [];
   bits.extend(x);
   bits.reverse();

   multi = 1;
   value = long(0);
   for b in bits:
      value += b * multi;
      multi *= 2;
   return value;
