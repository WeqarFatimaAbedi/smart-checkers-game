
#Put all the constant values inside of this file

import pygame

#DEFINE THE HEIGHT AND WIDTH
WIDTH, HEIGHT = 700, 700   #800 pixels

#DEFINE ROWS AND COLS IN CHECKERS BOARD
ROWS, COLS = 8, 8

#HOW BIG IS ONE SQAURE OF THE CHECKER BOARD
SQUARE_SIZE = WIDTH//COLS

#DEFINE VARIABLE FOR COLOURS
#RGB COLOR
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0,255,255)
GREY = (128,128,128)
GREEN = (0, 153, 0)


#load the king image
#pygame.transform will resize the image
#44,25 is the resolution of the image, this reletively keeps the aspect ratio of the image 
# and it makes it small enough to put it in the direct center so that we will put on or pieces
CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'), (44, 25))