""" 
This class is responsible for storing all the information about the current state of a chess game. it will also be responsible for determining the valid moves in the current state. and it will also keep a move log.

"""


class GameState():
    def __init__(self):
        self.board = [
            []
        ]
