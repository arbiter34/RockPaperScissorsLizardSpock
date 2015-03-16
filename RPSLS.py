from Elements import *
from Players import *

#Array of constructors
players = {
    0 : StupidBot.StupidBot,
    1 : RandomBot.RandomBot,
    2 : IterativeBot.IterativeBot,
    3 : LastPlayBot.LastPlayBot,
    4 : Human.Human,
    5 : MyBot.MyBot
}

#Array of constructor names for menu generation and argument passing
playerStrings = {
    0 : 'StupidBot',
    1 : 'RandomBot',
    2 : 'IterativeBot',
    3 : 'LastPlayBot',
    4 : 'Human',
    5 : 'MyBot'
}

print("Rock Paper Scissor Lizard Spock by Travis Alpers\n\n")

#init 
playerType = {}
player = {}


#Get player type loop
for j in range(0, 2):
    #default to -1 
    playerType[j] = -1

    #loop until valid input
    while(True):
        #print entry for each player type
        for y in range(0, len(players)):
            print(str(y+1) + " - " + playerStrings[y] + "\n")  
        #quit option
        print("7 - Quit")    

        #try catch for invalid input catching
        try: 
            #get player type as int - none int will throw exception - caught below
            playerType[j] = int(input("\n\nChoose Player " + str(j+1) + ": "))

            #check for exit
            if (playerType[j] == 7):
                print("\nExiting...\n")
                exit()

            #valid value - break loop
            if (playerType[j] <= 6 and playerType[j] >= 1):
                break;

        except ValueError:
            #invalid input - do nothing and loop
            y = y
        print("\nInvalid Option, Please try again!\n")

    #Dynamically call constructor for selected type
    player[j] = players[playerType[j]-1](playerStrings[playerType[j]-1])

#Main play loop - 5 games    
for i in range(0, 5):
    print("\n")
    playerMoves = {}

    #generate moves
    for k in range(0, 2):
        playerMoves[k] = player[k].play()
    
    #print moves and pass moves to opponent object
    for k in range(0, 2):
        print("Player " + str(k+1) + " chose " + playerMoves[k].name() + "!\n\n")
        player[k].opponentMove(playerMoves[not k])
    
    #Get result of round and print
    result = playerMoves[0].compareTo(playerMoves[1])
    print("\n" + result[0] + "\n")
    
    #Generate winner message
    winner = "Player 2" if (result[1] == "Lose") else "Player 1"
    if result[1] == "Win":
        winner = "Player 1 Wins!\n\n"
    elif result[1] == "Lose":
        winner = "Player 2 Wins!\n\n"
    elif result[1] == "Tie":
        winner = "Tie!\n\n"
    
    #print winner
    print(winner)