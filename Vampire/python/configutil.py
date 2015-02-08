import fileutil
from vUserDict import vUserDict

####################
#  Config Utility v1.0
#------------------
"""
Process cfg file. Set properties on Options object. (Options
acts like dictionary or hash map). Initialize with filename or
call load after creation. If load is called more than
once, additional properties are appended to current object, but
if properties have same name, they will overwrite. 

Requesting a non-existing property will never throw exceptions. It
will return None or an optional default value. 

Example:

  [logutil.py]
    import configutil
    g_options = configutil.Options("mods.cfg")

  or to search for/import from multiple config files:

  [logutil.py]
    import configutil
    g_options = configutil.Options()
    g_options.load("mods.cfg")
    g_options.load("logging.cfg")
  
    ...
    
    def exampleFunc():
      global g_options
      
      print "\\n".join(["%s=%s" % (k, v) for k, v in g_options.items()])
      if g_options["someBool"]:
        pass
      elif "default" == g_options.get("somestr","default")
        pass
      elif 3 == g_options.get("somenum",3)
        pass

"""

class Options(vUserDict):
    "Loads Options from config file"

    def __init__(self, filename=None):
        vUserDict.__init__(self)
        if filename is not None: self.load(filename)

    def load(self,filename):
        """ Process mod cfg file. Set properties on this module """
        self.filename = "Vampire/cfg/" + filename
        if fileutil.exists(self.filename):
            print "Loading config file [%s]" % self.filename
        else:
            print "File [%s] NOT FOUND" % self.filename
            return

        lines=fileutil.readlines(self.filename)
        for line in lines:
            rbound = len(line)
            slice = line.find("=")
            if -1 == slice:
                continue
            comment = line.find("#")
            if -1 != comment:
                if comment < slice:
                    continue
                else:
                    rbound=comment
            key=line[0:slice].strip()
            value=line[slice+1:rbound].strip()
            trynum=1
            if value.startswith('"') and value.endswith('"'):
                value=value[1:len(value)-1]
                trynum=0
            if value.startswith("'") and value.endswith("'"):
                value=value[1:len(value)-1]
                trynum=0
            if trynum:
                try:
                    self.__addNumValue(key,int(value))
                except:
                    self.__addStrValue(key,value)
            else:
                self.__addStrValue(key,value)                
                    
    def __addNumValue(self,key,value):
        self[key]=value
    
    def __addStrValue(self,key,value):
        self[key]=value

    # Additional get method allows you to specify
    # default value

    def get(self, key, default=None):
        value=default
        try:
            value = vUserDict.__getitem__(self, key)
        except:
            vUserDict.__setitem__(self, key, default)
        return value

    def set(self, key, item):         
        vUserDict.__setitem__(self, key, item)

    # Override array access to return None on failure (instead
    # of throwing an exception)

    def __getitem__(self, key):
        return self.get(key)

    # Inherited from parent class:
    # def clear():
    # def copy():                             
    # def keys():     
    # def items():  
    # def values():
