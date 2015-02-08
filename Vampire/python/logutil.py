import configutil

####################
#  Log Util v1.0
#------------------
"""

Allows controllable feedback levels in console. 

"""

g_options=configutil.Options("mods.cfg")

def setLevel(level):
	g_options["mod_logLevel"]=level

def printLevel1(data):
        print "[INFO] " + data
        
def printLevel2(data):
    global g_options
    if g_options["mod_logLevel"] > 1:
        print "[WARN] " + data

def printLevel3(data):
    global g_options
    if g_options["mod_logLevel"] > 2:
        print "[ERROR] " + data

def printLevel4(data):
    global g_options
    if 4 == g_options["mod_logLevel"]:
        print "[DEBUG] " + data

func_map = {1 : printLevel1,
            2 : printLevel2,
            3 : printLevel3,
            4 : printLevel4}

def log(data,level=4):
    """ First parameter is string to print to console. Optional second
        parameter is log level of message. 1 = Info, 2 = Warn, 3 = Error,
        4 = Debug. Default level is 4 """
    global g_options
    
    if 0 == g_options.get("mod_logLevel",0):
        return
    try:
        func_map[level](data)
    except:
        pass
