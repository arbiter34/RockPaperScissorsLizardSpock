from Players import Player
import random

class LastPlayBot(Player.Player):
    
    def play(self):
        try:
            self._move
        except AttributeError:
            moveExists = False
        else:
            moveExists = True
        if not moveExists:
            randomNumber = random.randint(0, 4)
            self._move = self._options[randomNumber](self._optionNames[randomNumber])
        return self._move