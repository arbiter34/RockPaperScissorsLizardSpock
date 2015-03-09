from Players import Player

class StupidBot(Player.Player):
    
    def play(self):
        return self._options[4](self._optionNames[4]) 