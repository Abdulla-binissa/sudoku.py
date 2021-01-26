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
        self.givenSpots = {(0,0)}

    def generateNewSudoku(self):
        for row in range( 0, len(self.board) ):
            for col in range( 0, len(self.board) ):
                string = str(col)
                self.board[row][col] = string

    def isEmptySpot(self, squareSelected):
        if(self.board[squareSelected[0]][squareSelected[1]] == '?'):
            return True
        else: 
            return False

    def isPlayableSpot(self, squareSelected):
        if( self.givenSpots.__contains__(squareSelected) ):
            return False
        else: 
            return True

    def setSpot(self, number, squareSelected):
        self.board[squareSelected[0]][squareSelected[1]] = number
