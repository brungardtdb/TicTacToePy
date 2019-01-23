'''
Program: TicTacToe.py
Author: David Brungardt
This class will handle the logic for our tic-tac-toe game.
'''

class TicTacToe:
    # Initialize variables for TicTacToe class
    xWin = False # boolean if X wins
    oWin = False # boolean if Y wins

    # dictionary that holds values for tic-tac-toe board
    gamedict = {"SQ1": " ",
               "SQ2": " ",
               "SQ3": " ",
               "SQ4": " ",
               "SQ5": " ",
               "SQ6": " ",
               "SQ7": " ",
               "SQ8": " ",
               "SQ9": " "}

    # funtion that prints positions on the playing board
    def print_position():

        print(" " + "1" + " | " + "2" + " | " + "3" + " " )
        print("---|---|---")
        print(" " + "4" + " | " + "5" + " | " + "6" + " " )
        print("---|---|---")
        print(" " + "7" + " | " + "8" + " | " + "9" + " " )

    # function that prints the current gameplay
    def print_gameboard(self):

        # values for tic-tac-toe board
        SQ1 = self.gamedict["SQ1"]
        SQ2 = self.gamedict["SQ2"]
        SQ3 = self.gamedict["SQ3"]
        SQ4 = self.gamedict["SQ4"]
        SQ5 = self.gamedict["SQ5"]
        SQ6 = self.gamedict["SQ6"]
        SQ7 = self.gamedict["SQ7"]
        SQ8 = self.gamedict["SQ8"]
        SQ9 = self.gamedict["SQ9"]

        # prints current position of players on board
        print(" " + SQ1 + " | " + SQ2 + " | " + SQ3 + " " )
        print("---|---|---")
        print(" " + SQ4 + " | " + SQ5 + " | " + SQ6 + " " )
        print("---|---|---")
        print(" " + SQ7 + " | " + SQ8 + " | " + SQ9 + " " )

    # function to set X on the board
    def set_X(self, num):
        if (num > 0 and num < 10):
            if (num == 1):
                self.gamedict["SQ1"] = "X"
            elif (num == 2):
                self.gamedict["SQ2"] = "X"
            elif (num == 3):
                self.gamedict["SQ3"] = "X"
            elif (num == 4):
                self.gamedict["SQ4"] = "X"
            elif (num == 5):
                self.gamedict["SQ5"] = "X"
            elif (num == 6):
                self.gamedict["SQ6"] = "X"
            elif (num == 7):
                self.gamedict["SQ7"] = "X"
            elif (num == 8):
                self.gamedict["SQ8"] = "X"
            else:
                self.gamedict["SQ9"] = "X"
        else:
            print("Invalid number selected")

    # function to set O on the board
    def set_O(self, num):
        if (num > 0 and num < 10):
            if (num == 1):
                self.gamedict["SQ1"] = "O"
            elif (num == 2):
                self.gamedict["SQ2"] = "O"
            elif (num == 3):
                self.gamedict["SQ3"] = "O"
            elif (num == 4):
                self.gamedict["SQ4"] = "O"
            elif (num == 5):
                self.gamedict["SQ5"] = "O"
            elif (num == 6):
                self.gamedict["SQ6"] = "O"
            elif (num == 7):
                self.gamedict["SQ7"] = "O"
            elif (num == 8):
                self.gamedict["SQ8"] = "O"
            else:
                self.gamedict["SQ9"] = "O"
        else:
            print("Invalid number selected")

    # function to see if X has won
    def isX_Won(self):
        if (self.gamedict["SQ1"] == "X" and self.gamedict["SQ2"] == "X" and self.gamedict["SQ3"] == "X"):
            self.xWin = True
        elif (self.gamedict["SQ4"] == "X" and self.gamedict["SQ5"] == "X" and self.gamedict["SQ6"] == "X"):
            self.xWin = True
        elif (self.gamedict["SQ7"] == "X" and self.gamedict["SQ8"] == "X" and self.gamedict["SQ9"] == "X"):
            self.xWin = True
        elif (self.gamedict["SQ1"] == "X" and self.gamedict["SQ4"] == "X" and self.gamedict["SQ7"] == "X"):
            self.xWin = True
        elif (self.gamedict["SQ2"] == "X" and self.gamedict["SQ5"] == "X" and self.gamedict["SQ8"] == "X"):
            self.xWin = True
        elif (self.gamedict["SQ3"] == "X" and self.gamedict["SQ6"] == "X" and self.gamedict["SQ9"] == "X"):
            self.xWin = True
        elif (self.gamedict["SQ1"] == "X" and self.gamedict["SQ5"] == "X" and self.gamedict["SQ9"] == "X"):
            self.xWin = True
        elif (self.gamedict["SQ3"] == "X" and self.gamedict["SQ5"] == "X" and self.gamedict["SQ7"] == "X"):
            self.xWin = True

        # return boolean value
        return self.xWin

    # function to see if X has won
    def isO_Won(self):
        if (self.gamedict["SQ1"] == "O" and self.gamedict["SQ2"] == "O" and self.gamedict["SQ3"] == "O"):
            self.oWin = True
        elif (self.gamedict["SQ4"] == "O" and self.gamedict["SQ5"] == "O" and self.gamedict["SQ6"] == "O"):
            self.oWin = True
        elif (self.gamedict["SQ7"] == "O" and self.gamedict["SQ8"] == "O" and self.gamedict["SQ9"] == "O"):
            self.oWin = True
        elif (self.gamedict["SQ1"] == "O" and self.gamedict["SQ4"] == "O" and self.gamedict["SQ7"] == "O"):
            self.oWin = True
        elif (self.gamedict["SQ2"] == "O" and self.gamedict["SQ5"] == "O" and self.gamedict["SQ8"] == "O"):
            self.oWin = True
        elif (self.gamedict["SQ3"] == "O" and self.gamedict["SQ6"] == "O" and self.gamedict["SQ9"] == "O"):
            self.oWin = True
        elif (self.gamedict["SQ1"] == "O" and self.gamedict["SQ5"] == "O" and self.gamedict["SQ9"] == "O"):
            self.oWin = True
        elif (self.gamedict["SQ3"] == "O" and self.gamedict["SQ5"] == "O" and self.gamedict["SQ7"] == "O"):
            self.oWin = True

        # return boolean value
        return self.oWin
