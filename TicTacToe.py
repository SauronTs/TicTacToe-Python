import random

class TicTacToe():
    
    scores = {'X': 1, 'O': 3}
    emptyChar = '#'
    playerChar = 'X'
    aiChar = 'O'

    def __init__(self):
        self.field = [['#', '#', '#'], 
                     ['#', '#', '#'],
                     ['#', '#', '#']]
        self.gameIsRunning = True

    def setPosition(self, x, y, isPlayer):
        character = self.aiChar
        if isPlayer:
            character = self.playerChar
    
        self.field[x][y] = character

    def deletePosition(self, x, y):
        self.field[x][y] = self.emptyChar

    def printField(self):
        for test in self.field:
            for test2 in test:
                print(test2 + " ", end='')
            print()
        print("\nInput: ", end='')
    
        if not self.gameIsRunning:
            print("\n")
            if self.hasWon() == 1:
                print("Player has won")
            elif self.hasWon() == 3:
                print("AI has won")
            else:
                print("No one won")

    def getInput(self, inputChar):
        if len(inputChar) == 1 and inputChar.isdigit():
            if(inputChar >= '1' and inputChar <= '9'):
                x = int((int(inputChar) - 1) / 3)
                y = int((int(inputChar) - 1) - int(((int(inputChar) - 1) / 3)) * 3)
                return x,y
        print("Error: Number can only be between 1-9")
        return -1, -1

    def isPositionBlocked(self, x, y):
        return not self.field[x][y] == self.emptyChar

    def fieldIsFull(self):
        for i in self.field:
            for a in i:
                if a == self.emptyChar:
                    return False
        return True

    def nextPlayerMove(self, x, y):
        if self.isPositionBlocked(x, y):
            print("Illegal player move")
            return False
        self.setPosition(x, y, True)

        if self.hasWon() != -2:
            self.gameIsRunning = False
            return False

        return True

    def nextAIMove(self):
        bestScore = 1
        bestX = -1
        bestY = -1

        for i in range(0, 3):
            for a in range(0, 3):
                if not self.isPositionBlocked(i, a):
                    self.setPosition(i, a, False)
                    score = self.minimax(0, False)
                    self.deletePosition(i, a)

                    if(score > bestScore):
                        bestScore = score
                        bestX = i
                        bestY = a

        self.setPosition(bestX, bestY, False)

    def minimax(self, depth, isMax):
        bestScore = 3
    
        if self.hasWon() != -2:
            return self.hasWon()

        if isMax:
            bestScore = 1

        for i in range(0, 3):
            for a in range(0,3):
                if not self.isPositionBlocked(i, a):
                    self.setPosition(i, a, not isMax)
                    score = self.minimax(depth + 1, not isMax)
                    self.deletePosition(i, a)

                    if isMax:
                        bestScore = max(bestScore, score)
                    else:
                        bestScore = min(bestScore, score)

        return bestScore



    def hasWon(self):
        for i in range(0, 3):
            if self.field[i][0] != self.emptyChar and self.field[i][0] == self.field[i][1] and self.field[i][1] == self.field[i][2]:
                return self.scores[self.field[i][0]]
            if self.field[0][i] != self.emptyChar and self.field[0][i] == self.field[1][i] and self.field[1][i] == self.field[2][i]:
                return self.scores[self.field[0][i]]

        if self.field[1][1] != self.emptyChar and ((self.field[0][0] == self.field[1][1] and self.field[1][1] == self.field[2][2]) or (self.field[0][2] == self.field[1][1] and self.field[1][1] == self.field[2][0])):
            return self.scores[self.field[1][1]]

        if self.fieldIsFull():
            return 2

        return -2

    def performMoves(self, currentInput):
        x, y = self.getInput(currentInput)

        if x == -1:
            return

        if self.nextPlayerMove(x, y):
            self.nextAIMove()

        if self.hasWon() != -2:
            self.gameIsRunning = False
