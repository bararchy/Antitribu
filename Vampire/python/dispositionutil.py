import __main__
import idutil
from __main__ import Character

####################
#  Disposition Utility v1.0
#------------------
"""

Adds GetDispositions(), SetDispositionByIndex(), NextDisposition() and PrevDisposition() to Character Class

Requires: idutil.py - Adds GetID() to Character Class

"""

###################
#  Variables      #
###################

# disposition tuple = name, level, hieght adjust
commondispositions = (("Neutral",0,0),("Anger",0,1),("Anger",0,2),("Anger",0,3), ("Joy",0,1),("Joy",0,2),("Joy",0,3),("Sad",0,1), \
                      ("Sad",0,2),("Sad",0,3),("Fear",0,1),("Fear",0,2),("Disgust",0,1),("Apathy",0,1),("Flirtatious",0,1), \
                      ("Confused",0,1),("lay",-18,1),("lay",-18,2),("lay",-18,3), ("lay",-18,4),("Damaged",0,1),("Dead",-18,1),("Sitting",-5,1), \
                      ("Bartender",0,1),("Bartender",0,2),("BehindBack",0,1))

uniqdispositions={"models/character/npc/unique/santa_monica/lily":(("Lily",0,1),("Lily",0,2),("ChairDamaged",0,1),("ChairDamaged",0,2)), \
    "models/character/npc/unique/downtown/lacroix":(("PrinceSitting",0,1)), \
    "models/character/npc/unique/santa_monica/therese":(("Therese",0,1),("Therese",0,2),("Therese",0,3))}

NAME=0
HADJUST=1
LEVEL=2

################
# MAIN METHODS #
################

def _GetDispositions(self,key=""):
    """ Returns list of expressions that are valid for the given model"""
    global commondispositions
    global uniqdispositions
    result=[]
    if not self.classname: return result
    if not self.classname.startswith("npc_V"): return result
    result.extend(commondispositions)
    if ""==key: key=self.GetID()
    if key in uniqdispositions.keys():
        result.extend(uniqdispositions[key])
    return result

def _SetDispositionByIndex(self,index=0):
    global NAME
    global LEVEL
    global HADJUST

    dispositions=self.GetDispositions()
    l = len(dispositions)

    try:
        self.dindex=self.dindex
    except:
        self.dindex=index % l

    tuple = dispositions[self.dindex]
    hadjust=tuple[HADJUST]
    if not (hadjust == 0):
        o = self.GetOrigin()
        no= (o[0],o[1],o[2]-hadjust)
        self.SetOrigin(no)

    self.dindex=index % l
    tuple = dispositions[self.dindex]

    dname=tuple[NAME]
    dlevel=tuple[LEVEL]
    hadjust=tuple[HADJUST]
    if not (hadjust == 0):
        o = self.GetOrigin()
        no= (o[0],o[1],o[2]+hadjust)
        self.SetOrigin(no)
    self.SetDisposition(dname,dlevel)
    return self.dindex

def _NextDisposition(self):
    """ Allows iteration through expressions """
    index = 0
    try:
        index=self.dindex
        index+=1
    except:
        index=1
    return self.SetPoseByIndex(index)

def _PrevDisposition(self):
    """ Allows iteration through expressions """
    index = 0
    try:
        index=self.dindex
        index-=1
    except:
        index=-1
    return self.SetPoseByIndex(index)
 
#####################
# Update Base Class #
#####################

Character.GetDispositions=_GetDispositions
Character.SetDispositionByIndex=_SetDispositionByIndex
Character.NextDisposition=_NextDisposition
Character.PrevDisposition=_PrevDisposition
