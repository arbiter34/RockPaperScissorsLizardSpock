from Players import Player

class IterativeBot(Player.Player):

    def __init__(self, name):
    	#init currentMove member to 0
        self._currentMove = 0
        super().__init__(name)
    
    def play(self):
    	#generate new move object
        move = self._options[self._currentMove](self._optionNames[self._currentMove])

        #increment currentMove # within 0-4
        self._currentMove = (self._currentMove+1) % 5
        return move