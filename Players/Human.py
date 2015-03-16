from Players import Player

class Human(Player.Player):
    
    def play(self):
        choice = 10
        #Loop until valid input
        while (True):
            #Print menu
            for y in range(0, 5):
                print ("(" + str(y+1) + ") : " + self._optionNames[y] + "\n")
            
            #Try catch to validate input
            try:
                choice = int(input("Enter your move: "))
                if (choice <= 5 and choice >= 1):
                    #valid input - break
                    break;
            except ValueError:
                #invalid input - loop
                choice = choice
            print("\nInvalid Option, please try again!\n")    
        
        #adjust index   
        choice = choice - 1

        #return player object
        return self._options[choice](self._optionNames[choice])