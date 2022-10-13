"""
This is the main driver file. it will be responsible for handling user input and displaying the current GameState Object.

"""
import pygame as p
import ChessEngine

WIDTH = HEIGHT = 512  # 400 is another good option
DIMENSION = 8  # dimensions of a chess board are 8x8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15  # for animations later on
IMAGES = {}

'''
Initialize a global directory of images. this will be called exactly once in the main
'''


def loadImages():
    pieces = ['wp', 'wR', 'wN', 'wB', 'wK',
              'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load(
            "Chess/images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))
    # Note: we can access an image by saying for example 'IMAGES['wp']'


'''
the main driver for our code. this will handle user input and updating the graphics 
'''


def main():
    p.init()
    p.display.set_caption('Chessi')
    Icon = p.image.load('Chess/images/icon.png')
    p.display.set_icon(Icon)
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    validMoves = gs.getValidMoves
    moveMade = False  # this is our flag variable for when a move is made
    loadImages()  # only do this once, before the while loop
    running = True
    sqSelected = ()  # no square is selected, keeps track of the last click of the user (tuple: (row, col))
    # keeps track of the player clicks (two tuples: [(6,4),(4,4)])
    playerClicks = []
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            # Mouse Handler
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()  # (x,y) location of the mouse
                col = location[0] // SQ_SIZE
                row = location[1] // SQ_SIZE
                if sqSelected == (row, col):  # the user clicked the same square twice
                    sqSelected = ()  # deselect
                    playerClicks = []  # clear player clicks
                else:
                    sqSelected = (row, col)
                    # append for both 1st and 2nd clicks
                    playerClicks.append(sqSelected)
                if len(playerClicks) == 2:  # after 2nd click
                    move = ChessEngine.Move(
                        playerClicks[0], playerClicks[1], gs.board)
                    print(move.getChessNotation())
                    if move in validMoves:
                        gs.makeMove(move)
                        moveMade = True
                    sqSelected = ()
                    playerClicks = []  # resetting user clicks
            # Key Handler
            elif e.type == p.KEYDOWN:
                if e.key == p.K_z:  # undo move when z is pressed
                    gs.undoMove()
                    moveMade = True
        if moveMade:
            validMoves = gs.getValidMoves()
            moveMade = False

        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()


'''
responsible for all the graphics within a current game state.
'''


def drawGameState(screen, gs):
    drawBoard(screen)  # draw squares on the board
    # add in piece highlighting or move suggestions (later)
    drawPieces(screen, gs.board)  # draw pieces on top of those squares


'''
responsible for drawing the squares on the board. 
'''


def drawBoard(screen):
    colors = [p.Color("#F2E9EE"), p.Color("#783F10")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c) % 2)]
            p.draw.rect(screen, color, p.Rect(
                c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))


'''
responsible for drawing the pieces on the using the current GameState.board
'''


def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":  # not empty square
                screen.blit(IMAGES[piece], p.Rect(
                    c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))


if __name__ == "__main__":
    main()
