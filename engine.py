""" 
This class is responsible for storing all the information about the current state of a chess game. it will also be responsible for determining the valid moves in the current state. and it will also keep a move log.

"""


class GameState():
    def __init__(self):
        # board is an 8x8 2d list, each element of the list has 2 characters.
        # the first character represents the color of the piece, 'b' or 'w'
        # the second character represents the type of the piece, 'K','Q','R','B','N' or 'p'
        # "--" represents an empty space with no piece
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"]
        ]
        self.whiteToMove = True
        self.moveLog = []
