'''
Program: TicTacToeConsoleUI.py
Author: David Brungardt
This class will handle the gameplay for our tic-tac-toe game.
'''

#import TicTacToe class
import TicTacToe

# declare and initialize variables
xWin = False
oWin = False
stopPlaying = False
oneRoundDown = False
player1_or_2 = 1

# loop to simulate gameplay
while(stopPlaying == False):

    # initialize new game of tic-tac-toe
    thisgame = TicTacToe.TicTacToe()

    # introduce players to game
    print("\nWelcome to Tic-Tac-Toe!\n")

    # for the sake of simplicity, order of X and O will be set
    # inform players of order so they can choose which player to be
    print("Player 1 will be \"X\"\nPlayer 2 will be \"O\"")

    # introduce user to game board
    print("\nThe boxes on the board are numbered top-to-bottom, and left to right.\nLike so: \n")
    thisgame.print_position()
    print("\n")

    # loop to simulate each round
    while(xWin == False and oWin == False):
        oneRoundDown = True

        if(player1_or_2 % 2 == 1):
            #prompt player for position
            playerposition = int(input("\nPlayer 1, please pick your position: \n(Please enter an integer between 1 and 9)\n"))

            # check to see if number is between 1 and 9
            if (playerposition > 0 and playerposition < 10):
                thisgame.set_X(playerposition) #set player position
                thisgame.print_gameboard() #print game board
                player1_or_2 += 1 # increment player

        elif(player1_or_2 % 2 == 0):
            #prompt player for position
            playerposition = int(input("\nPlayer 2, please pick your position: \n(Please enter an integer between 1 and 9)\n"))

            # check to see if number is between 1 and 9
            if (playerposition > 0 and playerposition < 10):
                thisgame.set_O(playerposition) #set player position
                thisgame.print_gameboard() #print game board
                player1_or_2 += 1 # increment player

        # check to see if either player has won
        xWin = thisgame.isX_Won()
        oWin = thisgame.isO_Won()

        # if player 1 wins, announce them as the winner
        if(xWin):
            print("\nPlayer 1 wins!!!")
            thisgame.clearBoard()
        # if player 2 wins, announce them as the winner
        elif(oWin):
            print("\nPlayer 2 wins!!!")
            thisgame.clearBoard()
        elif(player1_or_2 > 9):
            print("\nIt's a draw!!!")
            thisgame.clearBoard()
            break

    #ask user if they would like to continue
    toContinue = input("Would you like to continue? \nPlease type \"Y\"  or \"N\"\n")

    if(oneRoundDown == True):
        if (toContinue == "Y" or toContinue == "y"):
            stopPlaying = False
            oneRoundDown = False
            xWin = False
            oWin = False
            player1_or_2 = 1

        elif (toContinue == "N" or toContinue == "n"):
            stopPlaying = True

        else:
            print("Input was invalid")
            stopPlaying = True
