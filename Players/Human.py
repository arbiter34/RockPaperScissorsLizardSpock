from Players import Player

class Human(Player.Player):
    
    def play(self):
        choice = 10
        while (True):
            print("(1) : Rock\n")
            print("(2) : Paper\n")
            print("(3) : Scissors\n")
            print("(4) : Lizard\n")
            print("(5) : Spock\n")
            try:
                choice = int(input("Enter your move: "))
                if (choice <= 5 and choice >= 1):
                    break;
            except ValueError:
                choice = choice
            print("\nInvalid Option, please try again!\n")    
            
        choice = choice - 1
        return self._options[choice](self._optionNames[choice])