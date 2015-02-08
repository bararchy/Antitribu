from __main__ import Character
from logutil import log

####################
#  ID Utility v1.0
#------------------
"""

Adds dialog support methods to base Character Class

"""

################
# MAIN METHODS #
################

def _IsLine1(self):
    try:
        if 1 == self.openingline:
            self.openingline=2
            return 1
        else:
            return 0
    except:
        self.openingline=2
        return 1

def _IsLine2(self):
    try:
        if 2 == self.openingline:
            self.openingline=3
            return 1
        else:
            return 0
    except:
        self.openingline=3
        return 1

def _IsLine3(self):
    try:
        if 3 == self.openingline:
            self.openingline=1
            return 1
        else:
            return 0
    except:
        self.openingline=1
        return 1

def _ResetCounter(self):
    log("Reset Counter")
    self.dialogcounter=0
    
def _CountLine(self):
    if self.dialogcounter == 3: return 1
    self.dialogcounter += 1
    return 1

def _IsMaxCount(self):
    if self.dialogcounter == 3:
        self.ResetCounter()
        return 1
    return 0
    
    
#####################
# Update Base Class #
#####################
Character.IsLine1       = _IsLine1
Character.IsLine2       = _IsLine2
Character.IsLine3       = _IsLine3
Character.ResetCounter  = _ResetCounter
Character.CountLine     = _CountLine
Character.IsMaxCount    = _IsMaxCount

