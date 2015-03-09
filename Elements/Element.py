

class Element(object):
    
    def __init__(self, name):
        self._name = name
    
    def name(self):
        return self._name
        
    def compareTo(self, element):
        raise NotImplementedError("Not yet implemented")