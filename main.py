import pygame as pg
import numpy as np
from snake import *
from vars import *
import sys
from food import Food
import os

np.set_printoptions(threshold=sys.maxsize)
clear = lambda : os.system('cls')

def main():
    pg.init()
    global SCREEN, GAMEBOARD 
    SCREEN = pg.display.set_mode(SCREEN_SIZE)
    GAMEBOARD = np.zeros((GAMEBOARD_X, GAMEBOARD_Y) , dtype=int)
    running = True
    SCREEN.fill(BLACK)
    snake = Snake(SNAKENUMBER, [(1, 1),(0,1)], (0,255,0), Directions.DOWN, GAMEBOARD)
    food = Food(BLOCK_SIZE, SCREEN_SIZE, GAMEBOARD)
    clock = pg.time.Clock()

    while running:
        time = clock.tick(FPS) / 1000
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        snake.check_food(food)
        GAMEBOARD = snake.move(GAMEBOARD, time)
        GAMEBOARD = snake.draw(GAMEBOARD)
        GAMEBOARD = food.draw(GAMEBOARD)
        
        if PLAYER_INPUT:
            keys = pg.key.get_pressed()
            if keys[pg.K_UP]:
                snake.change_direction(Directions.UP)
            elif keys[pg.K_DOWN]:
                snake.change_direction(Directions.DOWN)
            elif keys[pg.K_RIGHT]:
                snake.change_direction(Directions.RIGHT)
            elif keys[pg.K_LEFT]:
                snake.change_direction(Directions.LEFT)
        
        
        
        
        running = snake.check_collision()
        draw_grid()
        pg.display.update()
        
        

def draw_grid():
    clear()
    print(GAMEBOARD)
    for i in range(0, GAMEBOARD_X):
        for j in range(0, GAMEBOARD_Y):
            if GAMEBOARD[i][j] == SNAKENUMBER:
                rect = pg.Rect(translate_to_cords(i), translate_to_cords(j), BLOCK_SIZE, BLOCK_SIZE)
                pg.draw.rect(SCREEN, (0,255,0), rect, 0)
                pg.draw.rect(SCREEN, GRAY, rect, 1)
            elif GAMEBOARD[i][j] == FOOD:
                rect = pg.Rect(translate_to_cords(i), translate_to_cords(j), BLOCK_SIZE, BLOCK_SIZE)
                pg.draw.rect(SCREEN, (255,0,0), rect, 0)
                pg.draw.rect(SCREEN, GRAY, rect, 1)
            else:
                rect = pg.Rect(translate_to_cords(i), translate_to_cords(j), BLOCK_SIZE, BLOCK_SIZE)
                pg.draw.rect(SCREEN, BLACK, rect, 0)
                pg.draw.rect(SCREEN, GRAY, rect, 1)




if __name__ == "__main__":
    main()