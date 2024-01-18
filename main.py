import pygame as pg
import numpy as np
from snake import *
from vars import *
import sys
from food import Food
import os

np.set_printoptions(threshold=sys.maxsize)
clear = lambda : os.system('cls')

pg.init()

SCREEN = pg.display.set_mode(SCREEN_SIZE)
GAMEBOARD = np.zeros((GAMEBOARD_X, GAMEBOARD_Y) , dtype=int)
RUNNING = True
SCREEN.fill(BLACK)
GAMEOVER = False 
snake = Snake(SNAKENUMBER, [(1, 1),(0,1)], GREEN, Directions.DOWN, GAMEBOARD)
food = Food(BLOCK_SIZE, SCREEN_SIZE, GAMEBOARD)
clock = pg.time.Clock()

AIMOVE = None
REWARD = 0

def run():

    global RUNNING, GAMEBOARD, GAMEOVER, snake, food, clock, AIMOVE, REWARD
    while RUNNING:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                RUNNING = False 
                pg.quit()

        if PLAYER_INPUT:
            keys = pg.key.get_pressed()
            if keys[pg.K_UP]:
                move = Directions.UP
            elif keys[pg.K_DOWN]:
                move = Directions.DOWN
            elif keys[pg.K_RIGHT]:
                move = Directions.RIGHT
            elif keys[pg.K_LEFT]:
                move = Directions.LEFT
            else:
                move = snake.direction
        elif AI_INPUT:
            move = AIMOVE
        else:
            move = snake.direction
        
        GAMEBOARD, REWARD, GAMEOVER = step(GAMEBOARD, move)

        if GAMEOVER:
            print("GAME OVER")
            print("REWARD: ", REWARD)
            RUNNING = False
            break 
    
        
def step(GAMEBOARD, Move):
    FOODREWARD = 0
    GAMEOVER = snake.check_collision()
    if GAMEOVER:
        return GAMEBOARD, REWARD - 1000, GAMEOVER
    else:
        time = clock.tick(FPS) / 1000
        snake.change_direction(Move)
        FOODREWARD = snake.check_food(food)
        GAMEBOARD= food.draw(GAMEBOARD)
        GAMEBOARD = snake.move(GAMEBOARD, time)
        draw_grid()
        pg.display.update()
        if FOODREWARD:
            return GAMEBOARD, REWARD + 200, GAMEOVER
        else:
            return GAMEBOARD, REWARD - 1, GAMEOVER

def draw_grid():
    #clear()
    #print(GAMEBOARD)
    for i in range(0, GAMEBOARD_X):
        for j in range(0, GAMEBOARD_Y):
            if GAMEBOARD[i][j] == SNAKENUMBER:
                rect = pg.Rect(translate_to_cords(i), translate_to_cords(j), BLOCK_SIZE, BLOCK_SIZE)
                pg.draw.rect(SCREEN, GREEN, rect, 0)
                pg.draw.rect(SCREEN, GRAY, rect, 1)
            elif GAMEBOARD[i][j] == FOOD:
                rect = pg.Rect(translate_to_cords(i), translate_to_cords(j), BLOCK_SIZE, BLOCK_SIZE)
                pg.draw.rect(SCREEN, RED, rect, 0)
                pg.draw.rect(SCREEN, GRAY, rect, 1)
            else:
                rect = pg.Rect(translate_to_cords(i), translate_to_cords(j), BLOCK_SIZE, BLOCK_SIZE)
                pg.draw.rect(SCREEN, BLACK, rect, 0)
                pg.draw.rect(SCREEN, GRAY, rect, 1)

if __name__ == "__main__":
    run()