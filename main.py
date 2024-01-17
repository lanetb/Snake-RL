import pygame as pg
import numpy as np
from snake import *
from vars import *
import sys
from enum import Enum

np.set_printoptions(threshold=sys.maxsize)

def main():
    pg.init()
    global SCREEN, GAMEBOARD 
    SCREEN = pg.display.set_mode(SCREEN_SIZE)
    GAMEBOARD = np.zeros((GAMEBOARD_X, GAMEBOARD_Y) , dtype=int)
    running = True
    SCREEN.fill(BLACK)
    snake = Snake(SNAKENUMBER, [(translate_to_grid(SCREEN_X//2), translate_to_grid(SCREEN_Y//2))], (0,255,0), Directions.UP, GAMEBOARD)

    print(GAMEBOARD)

    while running: 
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        snake.draw(pg, SCREEN)
        draw_grid()
        pg.display.update()

def draw_grid():
    for i in range(0, GAMEBOARD_X):
        for j in range(0, GAMEBOARD_Y):
            if GAMEBOARD[i][j] == SNAKENUMBER:
                rect = pg.Rect(translate_to_cords(i), translate_to_cords(j), BLOCK_SIZE, BLOCK_SIZE)
                pg.draw.rect(SCREEN, (0,255,0), rect, 0)
                pg.draw.rect(SCREEN, GRAY, rect, 1)
            else:
                rect = pg.Rect(translate_to_cords(i), translate_to_cords(j), BLOCK_SIZE, BLOCK_SIZE)
                pg.draw.rect(SCREEN, BLACK, rect, 0)
                pg.draw.rect(SCREEN, GRAY, rect, 1)




if __name__ == "__main__":
    main()