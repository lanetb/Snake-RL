from enum import Enum
from vars import *
import numpy as np

class Directions(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

class Snake:
    length = None
    direction = None
    body = None
    indicator = None
    block_size = None
    color = (0,255,0)
    bounds = None
    game_board = np.zeros((GAMEBOARD_X, GAMEBOARD_Y) , dtype=int)


    def __init__(self, indicator, body, color, direction, game_board):
        self.indicator = indicator
        self.bounds = SCREEN_SIZE
        self.body = body
        self.block_size = BLOCK_SIZE
        color = color
        game_board = game_board
        game_board[body[0][0]][body[0][1]] = indicator
        self.respawn(body, direction)

    def respawn(self, body, direction):
        self.length = 1
        self.direction = direction
        self.body = body

    def draw(self, game, window):
        for segment in self.body:
            self.game_board[segment[0]][segment[1]] = self.indicator

def translate_to_grid(n):
    return n // BLOCK_SIZE

def translate_to_cords(n):
    return n * BLOCK_SIZE