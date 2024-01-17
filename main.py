import pygame as pg
import numpy as np
from vars import *

def main():
    pg.init()
    global SCREEN, GAMEBOARD 
    SCREEN = pg.display.set_mode(SCREEN_SIZE)
    GAMEBOARD = np.zeros((SCREEN_X // BLOCK_SIZE, SCREEN_Y // BLOCK_SIZE) , dtype=int)
    running = True
    SCREEN.fill(BLACK)
    while running:
        draw_grid()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        pg.display.update()

def draw_grid():
    for x in range(0, SCREEN_X, BLOCK_SIZE):
        for y in range(0, SCREEN_Y, BLOCK_SIZE):
            rect = pg.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pg.draw.rect(SCREEN, GRAY, rect, 1)

if __name__ == "__main__":
    main()