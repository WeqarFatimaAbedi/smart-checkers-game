import pygame
from .constants import RED, WHITE, SQUARE_SIZE, GREY, BLUE, GREEN, CROWN

#when we make a new piece we need to pass what row its in, what column its in, and what color it is
class Piece:

    PADDING = 15   #for radius FROM DRAW_PIECE()
    OUTLINE = 2   #for the outline  FROM DRAW_PIECE()



    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False  #This will tell us, are we a King piece? that means we can jump backwards.
        self.x = 0
        self.y = 0
        self.calc_position()
        
        #DOWN = POSITIVE
        #UP = NEGATIVE
        #if self.color == BLUE:        #Direction will be negative, we are going up(down pieces)
            #self.direction = -1    #what way are we going, positive or negative.
        #else:
            #self.direction = 1

        
    

    #This will calculate the x and y positions base on the row and column we are in.
    #We need to know what our x and y positions will be according to the square size.
    def calc_position(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE //2    
        #col=dealing with the x which is the horizontal axis, and 
        # squaresize//2: we want the piece to be in the middle of the squarex and y pos
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE //2


    #This function will change the King variable
    def King_piece(self):
        self.king = True    #we will make this piece a king


    #we will draw, we will draw the actual piece itself
    def draw_piece(self, win):

        radius = SQUARE_SIZE // 2 - self.PADDING 

        #draw an outline (LARGER CIRCLE)
        pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.OUTLINE)

        #start by drawing a circle and outline so that we can see it  (SMALLER CIRCLE)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        #x, y pos=center of the circle
        #pick a radius: based on padding bw the edge of the square and the circle. define class vari a the top.

        #for king piece
        if self.king:
            #blit():put some image on to the screen, or put some surface on the screen.pygame method
            win.blit(CROWN, (self.x - CROWN.get_width()//2, self.y - CROWN.get_height()//2))
            #take the x and y radius and the crown image height and wdth so that it fits in the middle


    #for moving the pieces, defined even in board.py
    def move_pieces(self, row, col):
        #when we move a piece, then it will have a new row, the piece will be updated
        self.row = row
        self.col = col
        self.calc_position()   #tells us the x and y position of our piece should be, so we have to recalculate that

    def __repr__(self):
        return str(self.color)




        
        