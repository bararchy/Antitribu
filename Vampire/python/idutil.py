from __main__ import Character
from logutil import log

####################
#  ID Utility v1.0
#------------------
"""

Adds GetID() to Character Class

NOTE: modelutil and skinutil assume the key returned by GetID is model directory based. If this design
is changed, it will break those modules.

"""

################
# MAIN METHODS #
################

# Notes: we use model path up to slice-1 (instead of slice) because pc models have armor0, armor1, armor2, etc...
# To get pc ids to resolve to 1 id (regardless of armor), we remove 1 character from the end of the model
# parent directory.
def isKeyPCTest(test):
    return "/pc/" == test[16:20]

def isKeyEmbracedTest(test):
    return "_e" == test[-6:-4]

def _IsPC(self):
    return isKeyPCTest(self.model)

def _IsEmbraced(self):
    return isKeyEmbracedTest(self.model)

# Note : If GetID changes, then statutil must be updated as well. Changes to
# this implementation will also break any and all save games. Some functions
# such as embrace assume that GetID returns the full model path. 
def _GetID(self):
    """ Returns model specific id. Generally the model path without the model file name """
    key=""
    slice = self.model.rindex("/")
    if slice > 0:
        if self.IsPC(): 
            key=self.model[0:(slice-1)]
        else:
            key=self.model[0:slice]
    else:
        log("[Error] GetID - NPC [%s] - model is invalid or does not exist" % self.GetName(),3)
    if "model" == key:
        log("Model IS null model. Checking name")
        if self.name.startswith("#_"):
            log("Key found in name")
            key=self.name[2:len(self.name)]
    return key.lower()

def _GetUniqueID(self):
    """ Returns a statistically unique id (good probability of being unique).
        Generally the modelIndex + instance name + model name """

    #TODO: mapname + model index would be ideal, but we need a way of
    #      getting the map name.
    
    return "%d_%s_%s" % (self.modelindex,self.GetName(),self.GetID())

#####################
# Update Base Class #
#####################

Character.GetID=_GetID
Character.GetUniqueID=_GetUniqueID
Character.IsPC=_IsPC
Character.IsEmbraced=_IsEmbraced

