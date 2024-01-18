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

    def draw(self, game, window):
        self.game_board[self.x][self.y] = FOOD
        return self.game_board

    def respawn(self):
        blocks_in_x = (self.bounds[0])/self.block_size;
        blocks_in_y = (self.bounds[1])/self.block_size;
        self.x = random.randint(0, blocks_in_x - 1) * self.block_size
        self.y = random.randint(0, blocks_in_y - 1) * self.block_size

