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
        self.speed = SNAKESPEED
        self.timer = 1.0 / self.speed
        self.respawn(body, direction)

    def respawn(self, body, direction):
        self.length = 1
        self.direction = direction
        self.body = body

    def draw(self, game, window):
        for segment in self.body:
            self.game_board[segment[0]][segment[1]] = self.indicator

    def move(self, GAMEBOARD, time):
        if self.timer > 0:
            self.timer -= time
            return GAMEBOARD
        else:
            curr_head = self.body[-1]
            if self.direction == Directions.UP:
                new_head = (curr_head[0], curr_head[1] - 1)
            elif self.direction == Directions.DOWN:
                new_head = (curr_head[0], curr_head[1] + 1)
            elif self.direction == Directions.LEFT:
                new_head = (curr_head[0] - 1, curr_head[1])
            elif self.direction == Directions.RIGHT:
                new_head = (curr_head[0] + 1, curr_head[1])

            self.body.append(new_head)
            GAMEBOARD[new_head[0]][new_head[1]] = self.indicator
            GAMEBOARD[self.body[0][0]][self.body[0][1]] = EMPTY
            self.body.pop(0)
            self.timer += 1 / self.speed
            return GAMEBOARD
    
    def change_direction(self, direction):
        if self.direction == Directions.UP and direction == Directions.DOWN:
            return
        elif self.direction == Directions.DOWN and direction == Directions.UP:
            return
        elif self.direction == Directions.LEFT and direction == Directions.RIGHT:
            return
        elif self.direction == Directions.RIGHT and direction == Directions.LEFT:
            return
        else:
            self.direction = direction

def translate_to_grid(n):
    return n // BLOCK_SIZE

def translate_to_cords(n):
    return n * BLOCK_SIZE