from Players import Player
import random

class MyBot(Player.Player):
    
    def play(self):
        randomNumber = random.randint(0, 4)
        return self._options[randomNumber](self._optionNames[randomNumber])