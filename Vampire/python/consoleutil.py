import __main__
from logutil import log

####################
#  Console Util v1.0
#------------------
"""

Provides methods for console execution

   console(executionString)

NOTE:

   execution capability requires creation of alias
   in autoexwec.cfg:

   alias execonsole "exec console.cfg"

WARNING:

   calling consoleutil.console() from event handlers may cause
   threading issues.

"""

def console(data=""):
    """ Allows execution of console commands that require parameters.
        NOTE: asynchonous execution. May want to include a call BACK to
        your function. eg console("<command> \n myFunc(state2)")

    param 1 : data. String containing command to execute. (def="")"""

    if data=="": return
    log("SENT TO CONSOLE:\n%s" % data)
    cfg=open('Vampire/cfg/console.cfg', 'w')
    try: cfg.write(data)
    finally: cfg.close()
    __main__.ccmd.execonsole=""

