"""
This is the main driver file. it will be responsible for handling user input and displaying the current GameState Object.

"""
import pygame as p
import engine

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
            "images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))
    # Note: we can access an image by saying for example 'IMAGES['wp']'


'''
the main driver for our code. this will handle user input and updating the graphics 
'''


def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = engine.GameState()
    loadImages()  # only do this once, before the while loop
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False

        clock.tick(MAX_FPS)
        p.display.flip


if __name__ == "__main__":
    main()
