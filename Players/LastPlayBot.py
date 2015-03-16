from Players import Player
import random

class LastPlayBot(Player.Player):
    
    def play(self):
        #check if last move has been set
        try:
            self._move
        except AttributeError:
            moveExists = False
        else:
            moveExists = True

        #move doesn't exist, generate random move
        if not moveExists:
            randomNumber = random.randint(0, 4)
            #set move to random element object
            self._move = self._options[randomNumber](self._optionNames[randomNumber])

        #return move object
        return self._move