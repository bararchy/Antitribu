import __main__
import fileutil
import idutil
import characterext
from __main__ import Character
from logutil import log

####################
#  Model Utility v1.0
#------------------
"""

Adds GetModels(), GetSkins(), SetSkin(), SetSkinByIndex(), NextSkin(), PrevSkin() to Character Class

See modelutil.txt for documentation

Requires: idutil.py - Adds GetID() to Character Class

"""
###################
#  Variables      #
###################

# G.modelutilonce   : used to ensure 1 time ops only happen once (typically when player begins new game)
# G.default_models : hash table that tracks default model info for NPCs that have multiple models like Heather

###################
#  ONE TIME OPS   #
###################

def initModelUtil():
    log("modelutil : init called")
    if not __main__.G.modelutilonce:
        __main__.G.modelutilonce=1
        log("modelutil : Performing One Time ops")
        __main__.G.default_models={"models/character/npc/unique/santa_monica/heather":"heather_3.mdl"}

################
# MAIN METHODS #
################

# _GetModels
def _GetModels(self,key="",rootdir=""):
    """ Returns list of models that are valid for the given PC."""

    if ""==key: key=self.GetID()
    if ""==key: return [""]

    defaultModel=""
    if key in __main__.G.default_models.keys():
        defaultModel=__main__.G.default_models[key]
    else:
        defaultModel=self.model[self.model.rindex("/")+1:len(self.model)]
        __main__.G.default_models[key]=defaultModel
    resultList=[defaultModel]

    if ""==rootdir: rootdir=fileutil.getcwd()
    if ""==rootdir: return resultList

    mdldirlist=fileutil.listfiles(rootdir + "\\Vampire\\" + key.replace("/","\\"))

    if len(mdldirlist) != 0:
        for mdlfile in mdldirlist:
            if mdlfile.endswith(".mdl") and mdlfile.lower() != defaultModel.lower():
                resultList.append(mdlfile)

    # Special case (Keep these to a minimum)

    if key == "models/character/npc/unique/santa_monica/heather":
        if not "heather.mdl" in resultList: resultList.append("heather.mdl")
        if not "heather_goth.mdl" in resultList: resultList.append("heather_goth.mdl")
        if "heatherneardeath.mdl" in resultList: resultList.remove("heatherneardeath.mdl")
    if key == "models/character/npc/unique/santa_monica/lily":
        if "lilydamaged.mdl" in resultList: resultList.remove("lilydamaged.mdl")
        if "lily.mdl" in resultList: resultList.remove("lily.mdl")

    return resultList

def _HasMoreSkins(self):
    """ Returns true if character has more than 1 skin option """
    result = self.GetModels()
    if len(result) > 1 : return 1
    return 0

# _GetSkins
def _GetSkins(self):
    """ Returns a list of valid skins for use with the SetSkin() function """

    result = self.GetModels()
    return result


# _SetSkin
def _SetSkin(self,skin):
    """ Changes the model to the specified Skin.  """

    try: self.flip=self.flip*-1
    except: self.flip=-1
    stoggle=3+self.flip

    key=self.GetID()
    if ""==key: return 0
    rootdir=fileutil.getcwd()
    if ""==rootdir: return 0

    # fail fast if invalid name
    mdllist=self.GetModels(key,rootdir)
    if not skin in mdllist:
        log("Error: pc [%s] does not support skin [%s]" % (self.GetName(),skin),3)
        return 0
 
    self.FadeToSkin(stoggle)
    self.SetModel(key + "/" + skin)
    self.SetData("Model",key + "/" + skin)
    return 0

def _SetSkinByIndex(self,index=0):
    """ Allows iteration through skins """
    self.sindex=index
    skins = self.GetSkins()
    l = len(skins)
    self.SetSkin(skins[self.sindex % l])
    return self.sindex

def _NextSkin(self):
    """ Allows iteration through skins """
    try:
        self.sindex+=1
    except:
        self.sindex=1
    skins = self.GetSkins()
    l = len(skins)
    self.SetSkin(skins[self.sindex % l])
    return self.sindex

def _PrevSkin(self):
    """ Allows iteration through skins """
    try:
        self.sindex-=1
    except:
        self.sindex=-1
    skins = self.GetSkins()
    l = len(skins)
    self.SetSkin(skins[self.sindex % l])
    return self.sindex

#####################
# Update Base Class #
#####################

Character.GetModels=_GetModels
Character.GetSkins=_GetSkins
Character.SetSkin=_SetSkin
Character.SetSkinByIndex=_SetSkinByIndex
Character.NextSkin=_NextSkin
Character.PrevSkin=_PrevSkin
Character.HasMoreSkins=_HasMoreSkins
