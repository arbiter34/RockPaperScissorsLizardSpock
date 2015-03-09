from Players import Player

class IterativeBot(Player.Player):

    def __init__(self, name):
        self._currentMove = 0
        super().__init__(name)
    
    def play(self):
        move = self._options[self._currentMove](self._optionNames[self._currentMove])
        self._currentMove = (self._currentMove+1) % 5
        return move