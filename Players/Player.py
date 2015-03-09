from Elements import *

class Player(object):

    _options = {
        0 : Rock.Rock,
        1 : Paper.Paper,
        2 : Scissors.Scissors,
        3 : Lizard.Lizard,
        4 : Spock.Spock
    }
    
    _optionNames = {
        0 : 'Rock',
        1 : 'Paper',
        2 : 'Scissors',
        3 : 'Lizard',
        4 : 'Spock'
    }
    
    def __init__(self, name):
        self._name = name
        
    def name(self):
        return self._name
    
    def play(self):
        raise NotImplementedError("Not Yet Implemented")
    