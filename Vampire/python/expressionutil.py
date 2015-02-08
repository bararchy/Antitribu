import __main__
import idutil
from __main__ import Character
from logutil import log

####################
#  Expression Utility v1.0
#------------------
"""

Adds GetExpressions(), SetExpressionByIndex(), NextExpression() and PrevExpression() to Character Class

Requires: idutil.py - Adds GetID() to Character Class

"""

###################
#  Variables      #
###################
commonexpressions = ("Neutral","Joy","Fear","Very Frightened","Sly Smile","Flirtatious","Anger","Mad","Enraged","Sad","Miserable",    \
                     "Nearly Crying","Melancholy Smile","Confused","Disgust","Apathy","Lowered Both","Raised Both","Raised Right",    \
                     "Raised Left","Lowered Right","Lowered Left","Nearly Crying_No Deform","Meloncholy_NoDeform","Disgust_NoDeform", \
                     "Sad_NoDeform", "Fear_NoDeform","Sly Smile_NoDeform", "Confused_NoDeform","Flirtatious_NoDeform", "Knockback",   \
                     "Anger_No Deform ")


uniqexpressions={"models/character/npc/unique/santa_monica/lily":("Frenzied"), \
    "models/character/npc/unique/downtown/chunk_3":("laugh","Concern No Deform","laugh NoDeform"), \
    "models/character/npc/unique/hollywood/flynn":("Enraged_NoDeform"), \
    "models/character/npc/unique/hollywood/isaac":("mouth open","laugh"), \
    "models/character/npc/unique/santa_monica/kilpatrick":("laugh","Concern No Deform","laugh NoDeform"), \
    "models/character/npc/unique/downtown/lacroix":("Squint","Concern No Deform","Laugh","Mouth Open", \
                "shock", "Laugh No Deform","Insane","In Pain","hurt","Grimace", "Agony Recover","FIX"), \
    "models/character/npc/unique/downtown/larry":("smirk","smile","wince","sneer","Smile closed", \
                "left lip curl","disgusted","smug","disgusted closed","AAA"), \
    "models/character/npc/unique/chinatown/ming_xiao":("Concern No Deform","Sarcasm","delight"), \
    "models/character/npc/unique/downtown/nines":("Enraged_NoDeform","Squint"), \
    "models/character/npc/unique/santa_monica/prophet":("Enraged_NoDeform","Squint"), \
    "models/character/npc/unique/downtown/regent":("Enraged_NoDeform"), \
    "models/character/npc/common/sabbat_henchman":("greedy","greedy_NoDeform","snarl","Mouth Open"), \
    "models/character/npc/common/security_guard":("laugh","Concern No Deform","laugh NoDeform"), \
    "models/character/npc/unique/downtown/skelter":("Irritated"), \
    "models/character/npc/unique/downtown/smiling_jack":("squint","Laugh","Laugh_NoDeform","Snarl", \
                "Snarl_barred_teeth","Sniff","Concern"), \
    "models/character/npc/common/stripper":("eyes_half_closed","pissed_eyes","slutty","left_eyebrow_up", \
                "inner_brow_raiser","right_eyebrow_up","kiss","smile","scared_shitless","eyes closed"), \
    "models/character/npc/unique/santa_monica/therese":("Laugh","mouth open","sneer"), \
    "models/character/npc/unique/downtown/vv":("blow kiss","mouth open","blown kiss","innocent","flirt happy")}


################
# MAIN METHODS #
################

def _GetExpressions(self,key=""):
    """ Returns list of expressions that are valid for the given model"""
    global commonexpressions
    global uniqexpressions
    result=[]
    if not self.classname: return result
    if not self.classname.startswith("npc_V"): return result
    result.extend(commonexpressions)
    if ""==key: key=self.GetID()
    if key in uniqexpressions.keys():
        result.extend(uniqexpressions[key])
    return result

def _SetExpressionByIndex(self,index=0):
    expressions = self.GetExpressions()
    l = len(expressions)
    self.expressionindex=(index % l)
    self.SetData("ExpressionIndex",self.expressionindex)
    
    expression = expressions[self.expressionindex]
    try:
        self.SetExpression(expressions[self.expressionindex % l])
    except:
        self.SetExpression(expressions[self.expressionindex % l])
    data="dummy"
    # awkward bug with SetExpression. After being called, the next if statement
    # causes an exception, so we go ahead and raise/catch it here so that the
    # next command wont fail. 
    try:
        if data=="": return self.expressionindex
    except:
        pass
    return self.expressionindex

def _NextExpression(self):
    """ Allows iteration through expressions """
    self.RestoreExpression()
    self.expressionindex+=1
    return self.SetExpressionByIndex(self.expressionindex)

def _PrevExpression(self):
    """ Allows iteration through expressions """
    self.RestoreExpression()
    self.expressionindex-=1
    return self.SetExpressionByIndex(self.expressionindex)
 
def _RestoreExpression(self,display=0):
    """ Looks up last expression from save game store and restores """
    log("calling restore expression")
    eindex=self.GetData("ExpressionIndex")
    if None == eindex:
        self.SetData("ExpressionIndex",0)
        self.expressionindex=0
    else:
        self.expressionindex=eindex
    if display and (not 0 == self.expressionindex):
        self.SetExpressionByIndex(self.expressionindex)

#####################
# Update Base Class #
#####################

Character.GetExpressions=_GetExpressions
Character.SetExpressionByIndex=_SetExpressionByIndex
Character.NextExpression=_NextExpression
Character.PrevExpression=_PrevExpression
Character.RestoreExpression=_RestoreExpression
