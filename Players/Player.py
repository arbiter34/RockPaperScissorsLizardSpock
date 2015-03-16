from Elements import *

class Player(object):

    #array of element options
    _options = {
        0 : Rock.Rock,
        1 : Paper.Paper,
        2 : Scissors.Scissors,
        3 : Lizard.Lizard,
        4 : Spock.Spock
    }
    
    #array of element names
    _optionNames = {
        0 : 'Rock',
        1 : 'Paper',
        2 : 'Scissors',
        3 : 'Lizard',
        4 : 'Spock'
    }
    
    #constructor - set name to argument
    def __init__(self, name):
        self._name = name
    
    #get name    
    def name(self):
        return self._name
    
    #get play - must be overriden
    def play(self):
        raise NotImplementedError("Not Yet Implemented")
    
    #set opponent move
    def opponentMove(self, move):
        self._move = move