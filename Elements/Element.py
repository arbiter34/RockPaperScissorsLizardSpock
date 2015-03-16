#Base element class

class Element(object):
    
    #constructor - takes name
    def __init__(self, name):
        self._name = name
    
    #get name
    def name(self):
        return self._name
    
    #compareTo - used for play compares - must be overriden    
    def compareTo(self, element):
        raise NotImplementedError("Not yet implemented")