from Players import Player
import random

class MyBot(Player.Player):
    
    def play(self):
    	#generate random # 0-4
        randomNumber = random.randint(0, 4)

        #return new play object
        return self._options[randomNumber](self._optionNames[randomNumber])