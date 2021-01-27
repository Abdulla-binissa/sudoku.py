import pygame as pygame
import SudokuEngine as SudokuEngine

WIDTH = HEIGHT = 540
DIMENSION = 9
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
DIGITS = ['1', '2', '3', '4', '5', '6', '7', '8', '9']


def main():
    pygame.init()

    pygame.font.init()
    font = pygame.font.Font('freesansbold.ttf', 54)
    
    screen = pygame.display.set_mode(( WIDTH, HEIGHT ))
    clock = pygame.time.Clock()
    gamestate = SudokuEngine.Gamestate()

    pygame.display.set_caption('Sudoku')
    screen.fill(pygame.Color('white'))

    gamestate.generateNewSudoku()

    squareSelected = ()

    mainLoop = True
    while mainLoop:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                mainLoop = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                location = pygame.mouse.get_pos()
                col = location[0] // SQ_SIZE
                row = location[1] // SQ_SIZE
                squareSelected = (row, col)
                
            elif ( event.type == pygame.KEYDOWN and gamestate.isPlayableSpot(squareSelected) ):
                key = event.unicode
                
                if DIGITS.__contains__(key):
                    gamestate.setSpot(key, squareSelected)
                    gamestate.setDuplicates(squareSelected)
                    gamestate.removeDuplicates()
                
                else: 
                    print(gamestate.conflictingSquares)

        drawGameState(screen, gamestate, font)
        clock.tick(MAX_FPS)
        pygame.display.flip()

def drawGameState(screen, gamestate, font):
    drawBoard(screen) 
    drawConflictingHighlights(screen, gamestate)
    drawNumbers(screen, gamestate, font)

def drawBoard(screen):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            thickness = 1
            squareOutline = pygame.Rect(
                c*SQ_SIZE, 
                r*SQ_SIZE, 
                SQ_SIZE, 
                SQ_SIZE)
            squareInner = pygame.Rect(
                c*SQ_SIZE + thickness - thickness*(c%3), 
                r*SQ_SIZE + thickness - thickness*(r%3), 
                SQ_SIZE - 2*thickness, 
                SQ_SIZE - 2*thickness)
            pygame.draw.rect(screen, pygame.Color("black"), squareOutline)
            pygame.draw.rect(screen, pygame.Color("white"), squareInner)

def drawNumbers(screen, gamestate, font):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            square = gamestate.board[r][c]
            if( square != '?' ):
                if( gamestate.givenSquares.__contains__((r,c)) ):
                    textsurface = font.render(square, True, (0, 0, 0))
                else: 
                    textsurface = font.render(square, True, (80, 80, 80))
                screen.blit(textsurface, pygame.Rect(c*SQ_SIZE + (SQ_SIZE // 4), r*SQ_SIZE + (SQ_SIZE // 8), SQ_SIZE, SQ_SIZE))

def drawConflictingHighlights(screen, gamestate):
    thickness = 1
    s = pygame.Surface((SQ_SIZE - (2*thickness), SQ_SIZE - (2*thickness)))
    s.set_alpha(60) # 0 - transparent ; 255 - opaque
    s.fill(pygame.Color('red'))
    for square in gamestate.conflictingSquares:
        
        r = square[0]
        c = square[1]
        screen.blit(s, pygame.Rect(
            c*SQ_SIZE + thickness - thickness*(c%3), 
            r*SQ_SIZE + thickness - thickness*(r%3), 
            (SQ_SIZE - (2*thickness)), 
            (SQ_SIZE - (2*thickness))))

main()

#for i in range(0, 9):
#        print( (i // 3)*3 )