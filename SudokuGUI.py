import pygame as pygame
import SudokuEngine as SudokuEngine

WIDTH = HEIGHT = 540
DIMENSION = 9
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}


def loadImages():
    digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    for digit in digits:
        IMAGES[digit] = pygame.image.load("./images/regularSet/" + digit +".png")


def main():
    pygame.init()

    screen = pygame.display.set_mode(( WIDTH, HEIGHT ))
    clock = pygame.time.Clock()
    screen.fill(pygame.Color('white'))
    gamestate = SudokuEngine.Gamestate()

    loadImages()

    mainLoop = True
    while mainLoop:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                mainLoop = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                location = pygame.mouse.get_pos()
                col = location[0] // SQ_SIZE
                row = location[1] // SQ_SIZE

                print(row, "-", col)

        drawGameState(screen, gamestate)
        clock.tick(MAX_FPS)
        pygame.display.flip()

def drawGameState(screen, gamestate):
    drawBoard(screen) # Draw Board
    drawPieces(screen, gamestate) # Draw Pieces

def drawBoard(screen):
    colors = [pygame.Color("white"), pygame.Color("gray")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r + c) % 2)]
            pygame.draw.rect(screen, color, pygame.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
    
def drawPieces(screen, gamestate):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            square = gamestate.board[r][c]
            if( square != '?'):
                screen.blit(IMAGES[square], pygame.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))





main()