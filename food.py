import random
from vars import *

class Food:
    block_size = None
    color = (255,0,0)
    x = FOOD_START[0];
    y = FOOD_START[1];
    bounds = None

    def __init__(self, block_size, bounds, game_board):
        self.block_size = block_size
        self.bounds = bounds
        self.game_board = game_board

    def draw(self, GAMEBOARD):
        GAMEBOARD[self.x][self.y] = FOOD
        return GAMEBOARD

    def respawn(self):
        self.x = random.randint(0, GAMEBOARD_X - 1)
        self.y = random.randint(0, GAMEBOARD_Y - 1)

