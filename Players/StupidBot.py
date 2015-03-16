from Players import Player

class StupidBot(Player.Player):
    
    def play(self):
    	#return same move object everytime - he's not very smart
        return self._options[4](self._optionNames[4]) 