from Players import Player
import random

class RandomBot(Player.Player):
    
    def play(self):
    	#Get random int 0-4
        randomNumber = random.randint(0, 4)

        #return new move object
        return self._options[randomNumber](self._optionNames[randomNumber])