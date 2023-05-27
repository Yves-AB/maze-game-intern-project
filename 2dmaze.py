# This code is not intended to be used for the project, it is just a small 2d template for the game
# Make sure to have pygame installed before running the code

# Written by Yves-AB
# Most recent date modified: 5/27/2023


import pygame
import os
from pygame import gfxdraw

##the code will consist of 2 classes , one for the player ( u control ) and one for the walls
class Player(object):
    
    def __init__(self):
        self.rect = pygame.Rect(32, 32, 16, 16)

    #function of collision of player with wall
    def collide(self,x,y):
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if x > 0:
                    self.rect.right = wall.rect.left
                if x < 0:
                    self.rect.left = wall.rect.right
                if y > 0:
                    self.rect.bottom = wall.rect.top
                if y < 0:
                    self.rect.top = wall.rect.bottom

    #moves player on either x axis or y axis , helper method for move()
    def moveAxis(self,x,y):
        self.rect.x +=x
        self.rect.y +=y
        self.collide(self,x,y)

    def move(self,x,y):
        if x != 0:
            self.moveAxis(self,x,0)
        if y != 0:
            self.moveAxis(self,0,y)


class Wall(object):
    def __init__(self,position):
        walls.append(self)
        self.rect = pygame.rect(position[0],position[1],16,16)


# now we initialize the environment
os.environ["SDL_VIDEO_CENTERED"] = "1" #centers the game window on the screen
pygame.init()  # initiliazes pygame library for use

pygame.display.set_caption("Reach the red square!")
screen = pygame.display.set_mode((360, 270))
 
clock = pygame.time.Clock()
walls = []
player = Player() # initialize player

#initialize the map
map = """
11111111111111111111
1                  1
1         111111   1
1   1111       1   1
1   1        1111  1
1 111  1111        1
1   1     1 1      1
1   1     1   111 11
1   111 111   1 1  1
1     1   1   1 1  1
111   1   11111 1  1
1 1      11        1
1 1   1111   111   1
1     1    2   1   1
11111111111111111111
""".splitlines()[1:]
 
# Parse the level string above. 1 = wall, 2 = destination(end point)
x = y = 1
for row in map:
    for col in row:
        if col == "1":
            Wall((x, y))
        if col == "2":
            end_rect = pygame.Rect(x, y, 10, 10)
        x += 18
    y += 18
    x = 1
 