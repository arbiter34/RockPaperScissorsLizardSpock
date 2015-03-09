from Elements import *
from Players import *

players = {
    0 : StupidBot.StupidBot,
    1 : RandomBot.RandomBot,
    2 : IterativeBot.IterativeBot,
    3 : LastPlayBot.LastPlayBot,
    4 : Human.Human,
    5 : MyBot.MyBot
}

playerStrings = {
    0 : 'StupidBot',
    1 : 'RandomBot',
    2 : 'IterativeBot',
    3 : 'LastPlayBot',
    4 : 'Human',
    5 : 'MyBot'
}

print("Rock Paper Scissor Lizard Spock by Travis Alpers\n\n")
for i in range(0, 5):
    playerType = {}
    player = {}
    for j in range(0, 2):
        playerType[j] = -1
        while(True):
            for y in range(0, len(players)):
                print(str(y+1) + " - " + playerStrings[y] + "\n")  
            print("7 - Quit")    
            try: 
                playerType[j] = int(input("\n\nChoose Player " + str(j+1) + ": "))
                if (playerType[j] == 7):
                    print("\nExiting...\n")
                    exit()
                if (playerType[j] <= 6 and playerType[j] >= 1):
                    break;
            except ValueError:
                y = y
            print("\nInvalid Option, Please try again!\n")
        player[j] = players[playerType[j]-1](playerStrings[playerType[j]-1])
        print(player[j])
    
    player1move = player[0].play()
    player2move = player[1].play()
    
    result = player1move.compareTo(player2move)
    print("\n" + result[0] + "\n")
    
    winner = "Player 2" if (result[1] == "Lose") else "Player 1"
    if result[1] == "Win":
        winner = "Player 1 Wins!\n\n"
    elif result[1] == "Lose":
        winner = "Player 2 Wins!\n\n"
    elif result[1] == "Tie":
        winner = "Tie!\n\n"
    
    print(winner)