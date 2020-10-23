import pygame
import random
import sys
from pygame.locals import *


#---------------------------------------------------------------------------------
# constants
# defination about display
WIDTH    = 800
HEIGHT   = 600
CELL     = 20
COL      = int(WIDTH / CELL)
ROW      = int(HEIGHT / CELL)
FPS      = 10

# define color
BG_COLOR   = (255,255,255)
HEAD_COLOR = (0, 128, 128)
FOOD_COLOR = (255, 255, 0)
BODY_COLOR = (200,200,200)

# define direction 
UP    = 1
DOWN  = 2
RIGHT = 3
LEFT  = 4
#----------------------------------------------------------------------------------


#----------------------------------------------------------------------------------
# class
class Point:
    row = 0
    col = 0
    def __init__(self,row,col):
        self.row = row
        self.col = col
    def copy(self):
        return Point(self.row, self.col)
#----------------------------------------------------------------------------------


#----------------------------------------------------------------------------------
# basic function
# display start infomation
def display_start_info(screen):
    pygame.draw.rect(screen, BG_COLOR, (0, 0, WIDTH, HEIGHT))
    font = pygame.font.Font('C://Windows//Fonts//msyh.ttc', 40)
    start_info = font.render('Press any key to start the game', True, HEAD_COLOR)
    screen.blit(start_info, (100, 250))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                game_end()
            elif event.type == KEYDOWN:
                if event.type == K_ESCAPE:
                    game_end()
                else:
                    return

# display when game over
def display_end_info(screen):
    font = pygame.font.Font('C://Windows//Fonts//msyh.ttc', 40)
    end_info = font.render('GAME OVER!', True, HEAD_COLOR)
    conti_info = font.render('Press any key to continue', True, HEAD_COLOR)
    screen.blit(end_info, (260, 230))
    screen.blit(conti_info, (160,300))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                game_end()
            elif event.type == KEYDOWN:
                if event.type == K_ESCAPE or event.key == K_q:
                    game_end()
                else:
                    return

# end game and quit
def game_end():
    pygame.quit()
    sys.exit()

# run game
def running_game(screen, sys_clock):
    food   = get_random_food()
    head   = Point(ROW/2, COL/2)
    bodies = [Point(head.row, head.col+1), Point(head.row, head.col+2)]
    direction = LEFT
    speed = FPS
    score = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                game_end()
            elif event.type == KEYDOWN:
                if (event.key == K_LEFT) and direction != RIGHT:
                    direction = LEFT
                elif (event.key == K_RIGHT) and direction != LEFT:
                    direction = RIGHT
                elif (event.key == K_UP) and direction != DOWN:
                    direction = UP
                elif (event.key == K_DOWN) and direction != UP:
                    direction = DOWN
                elif event.key == K_ESCAPE:
                    game_end()
        
        if snake_dead(head, bodies):
            break
        
        # move the bodies
        bodies.insert(0, head.copy())
        if food_eaten(head, food):
            food = get_random_food()
            speed += 1
            score += 1
        else:
            bodies.pop()

        # move the head
        if direction == LEFT:
            head.col -= 1
        if direction == DOWN:
            head.row += 1
        if direction == UP:
            head.row -= 1
        if direction == RIGHT:
            head.col += 1

        # draw screen
        pygame.draw.rect(screen, BG_COLOR, (0, 0, WIDTH, HEIGHT))
        # draw snake
        pygame.draw.rect(screen, HEAD_COLOR, (head.col*CELL, head.row*CELL, CELL, CELL))
        for body in bodies:
            pygame.draw.rect(screen, BODY_COLOR, (body.col*CELL, body.row*CELL, CELL, CELL))
        # draw food
        pygame.draw.rect(screen, FOOD_COLOR, (food.col*CELL, food.row*CELL, CELL, CELL))
        # display score
        display_score(screen, score)

        # update screen
        pygame.display.update()
        sys_clock.tick(speed)
#----------------------------------------------------------------------------------


#----------------------------------------------------------------------------------
# detailed functoin
# creative food
def get_random_food():
    food_pos = Point(random.randint(0,ROW-1),random.randint(0, COL-1))
    return food_pos

# judge snake dead or not
def snake_dead(head, bodies):
    if (head.row < 0 or head.col < 0 or head.row > ROW or head.col > COL):
        return True
    for body in bodies:
        if (head.row == body.row and head.col == body.col):
            return True

# judge food get eaten or not
def food_eaten(head, food):
    if (head.row == food.row and head.col == food.col):
        return True

# display score
def display_score(screen, score):
    font = pygame.font.Font('C://Windows//Fonts//msyh.ttc', 20)
    end_info = font.render('score: %s' % score, True, HEAD_COLOR)
    screen.blit(end_info, (700, 10))
#----------------------------------------------------------------------------------


#----------------------------------------------------------------------------------
def main():
    # init
    pygame.init()
    sys_clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Slither")
    display_start_info(screen)

    # judgement and reaction
    while True:
        running_game(screen, sys_clock)
        display_end_info(screen)
#----------------------------------------------------------------------------------

# run all
main()
