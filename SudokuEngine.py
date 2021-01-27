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


    def checkQuadrant(self, squareSelected):
        squareValue = self.board[squareSelected[0]][squareSelected[1]]
        if squareValue == "?": return

        for r in range(0, 3):
            for c in range(0, 3):
                testRow = (squareSelected[0] // 3)*3 + r
                testCol = (squareSelected[1] // 3)*3 + c
                if (squareSelected[0] == testRow and squareSelected[1] == testCol): 
                    continue                
                testSquareValue = self.board[testRow][testCol]
                if( squareValue == testSquareValue ):
                    if not self.conflictingSquares.__contains__((squareSelected[0], squareSelected[1])):
                        self.conflictingSquares.append((squareSelected[0], squareSelected[1]))
                    if not self.conflictingSquares.__contains__((testRow, testCol)):
                        self.conflictingSquares.append((testRow, testCol))
                    return True
        return False

    def checkLines(self, squareSelected):
        squareValue = self.board[squareSelected[0]][squareSelected[1]]
        testRow = squareSelected[0]
        for testCol in range(0, 9):
            testSquareValue = self.board[testRow][testCol]
            if (squareSelected[0] == testRow and squareSelected[1] == testCol): 
                continue
            if( squareValue == testSquareValue ):
                if not self.conflictingSquares.__contains__((squareSelected[0], squareSelected[1])):
                    self.conflictingSquares.append((squareSelected[0], squareSelected[1]))
                if not self.conflictingSquares.__contains__((testRow, testCol)):
                    self.conflictingSquares.append((testRow, testCol))
                return True
        testCol = squareSelected[1]
        for testRow in range(0, 9):
            testSquareValue = self.board[testRow][testCol]
            if (squareSelected[0] == testRow and squareSelected[1] == testCol): 
                continue
            if( squareValue == testSquareValue ):
                if not self.conflictingSquares.__contains__((squareSelected[0], squareSelected[1])):
                    self.conflictingSquares.append((squareSelected[0], squareSelected[1]))
                if not self.conflictingSquares.__contains__((testRow, testCol)):
                    self.conflictingSquares.append((testRow, testCol))
                    return True
        return False

    def removeDuplicates(self):
        for square in self.conflictingSquares:
            if not self.checkQuadrant(square) and not self.checkLines(square) :
                self.conflictingSquares.remove(square)


    def setDuplicates(self, squareSelected):
        self.checkQuadrant(squareSelected)
        self.checkLines(squareSelected)
        #if not checkQuadrant and not checkLines :
        #    self.removeDuplicates(squareSelected)
            


                