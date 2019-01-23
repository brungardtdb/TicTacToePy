'''
Program: TicTacToeConsoleUI.py
Author: David Brungardt
This class will handle the gameplay for our tic-tac-toe game.
'''

# declare and initialize variables
xWin = False
oWin = False
stopPlaying = False

# loop to simulate gameplay
while(stopPlaying == False):

    # initialize new game of tic-tac-toe
    thisgame = TicTacToe()

    # introduce players to game
    print("Welcome to Tic-Tac-Toe!")



    # loop to simulate each round
    while(xWin == False and oWin == False):
        print("stuff")
        break # DELETE WHEN FINISHED!!!

    #ask user if they would like to continue
    toContinue = input("Would you like to continue? \nPlease type \"Y\"  or \"N\"\n")

    if (toContinue == "Y"):
        stopPlaying = False
    elif (toContinue == "N"):
        stopPlaying = True
    else:
        print("Input was invalid")
        stopPlaying = True
