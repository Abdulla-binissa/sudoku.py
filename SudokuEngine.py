import random

class Gamestate():

    def __init__(self):

        self.board = [
            ['1', '?', '?', '?', '?', '?', '?', '?', '?'],
            ['?', '?', '?', '?', '?', '?', '?', '?', '?'],
            ['?', '?', '?', '?', '?', '?', '?', '?', '?'],
            ['?', '?', '?', '?', '?', '?', '?', '?', '?'],
            ['?', '?', '?', '?', '?', '?', '?', '?', '?'],
            ['?', '?', '?', '?', '?', '?', '?', '?', '?'],
            ['?', '?', '?', '?', '?', '?', '?', '?', '?'],
            ['?', '?', '?', '?', '?', '?', '?', '?', '?'],
            ['?', '?', '?', '?', '?', '?', '?', '?', '?']
        ]
        self.givenSquares = {}

    def generateNewSudoku(self):
        #for row in range( 0, len(self.board) ):
        #    for col in range( 0, len(self.board) ):
        #        string = str(random.randint(1, 9))
        #        self.board[row][col] = string
        self.board = [
            ['8', '9', '?', '7', '?', '4', '?', '?', '?'],
            ['2', '3', '?', '?', '?', '?', '?', '?', '9'],
            ['?', '?', '7', '?', '?', '?', '5', '3', '?'],
            ['9', '4', '?', '?', '5', '1', '?', '?', '6'],
            ['?', '7', '8', '?', '2', '6', '?', '4', '?'],
            ['?', '?', '?', '4', '?', '3', '?', '?', '1'],
            ['7', '?', '4', '?', '?', '8', '?', '1', '?'],
            ['?', '?', '?', '3', '?', '?', '?', '?', '?'],
            ['?', '?', '6', '?', '?', '?', '2', '?', '?']
        ]
        self.givenSquares = {
            (0,0),(0,1),(0,3),(0,5),
            (1,0),(1,1),(1,8),
            (2,2),(2,6),(2,7),
            (3,0),(3,1),(3,4),(3,5),(3,8),
            (4,1),(4,2),(4,4),(4,5),(4,7),
            (5,3),(5,5),(5,8),
            (6,0),(6,2),(6,5),(6,7),
            (7,3),
            (8,2),(8,6)
        }
        self.conflictingSquares = []

    def isEmptySpot(self, squareSelected):
        if(self.board[squareSelected[0]][squareSelected[1]] == '?'):
            return True
        else: 
            return False

    def isPlayableSpot(self, squareSelected):
        if( self.givenSquares.__contains__(squareSelected) ):
            return False
        else: 
            return True

    def setSpot(self, number, squareSelected):
        self.board[squareSelected[0]][squareSelected[1]] = number

    #def checkSquares(self, currentSquare, checkSquare):

    def checkQuadrant(self, squareSelected):
        squareValue = self.board[squareSelected[0]][squareSelected[1]]
        if squareValue == "?": 
            return

        for r in range(0, 2):
            for c in range(0, 2):
                row = squareSelected[0] // 3
                col = squareSelected[1] // 3
                sameSquare = True if (squareSelected[0] == row+r and squareSelected[1] == col+c) else False
                testSquareValue = self.board[row+r][col+c]
                if( squareValue == testSquareValue and not sameSquare):
                    print(
                        "(", squareSelected[0], ", ", squareSelected[1], ")", squareValue, 
                        "(", row+r, ", ", col+c, ")", testSquareValue )
                    self.conflictingSquares.append((squareSelected[0], squareSelected[1]))
                    self.conflictingSquares.append((row+r, col+c))

    def checkLines(self, squareSelected):
        for row in range(0, 8):
           for col in range(0, 8):
               self.checkQuadrant(squareSelected)
                
                
                