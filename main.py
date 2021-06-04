import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE, BLUE
from checkers.board import Board
from checkers.game import Game
from minimax.algorithm import minimax

import pygame
from pygame.locals import *
import os

# Game Initialization
pygame.init()
 
# Center the Game Application
os.environ['SDL_VIDEO_CENTERED'] = '1'
 
# Game Resolution
screen_width=700
screen_height=700
screen=pygame.display.set_mode((screen_width, screen_height))
 
# Text Renderer
def text_format(message, textFont, textSize, textColor):
    newFont=pygame.font.Font(textFont, textSize)
    newText=newFont.render(message, 0, textColor)
 
    return newText
 
 
# Colors
white=(255, 255, 255)
black=(0, 0, 0)
gray=(50, 50, 50)
red=(255, 0, 0)
green=(85,107,47)
blue=(0,0,128)
yellow=(255, 255, 0)
pink =(255,0,127)
dblue= (0,255,255)
 
# Game Fonts
font = "freesansbold.ttf"
 
 
# Game Framerate
clock = pygame.time.Clock()
FPS=30

# Main Menu
def main_menu():
 
    menu=True
    selected="start"
    selected1="options"
    selected1="option"
    selected1="option1"
 
    while menu:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()

            if event.type==pygame.KEYDOWN:

                if event.key==pygame.K_UP:
                    selected="start"

                elif event.key==pygame.K_DOWN:
                    selected="quit"

                elif event.key==pygame.K_LEFT:
                    selected1="options"
                elif event.key==pygame.K_LEFT:
                    selected1="option"
                elif event.key==pygame.K_LEFT:
                    selected1="option1"

                if event.key==pygame.K_RETURN:
                    if selected=="start":
                        main()
                    if selected=="quit":
                        pygame.quit()
                        quit()
                    if selected1=="options":
                        pass
                    if selected1=="option":
                        pass
                    if selected1=="option1":
                        pass
 
        # Main Menu UI
        screen.fill(blue)
        title=text_format("AI Based Action Selection Checkers Game", font, 30, yellow)
        if selected=="start":
            text_start=text_format("START", font, 30, red)
        else:
            text_start = text_format("START", font, 30, white)

        if selected=="quit":
            text_quit=text_format("QUIT", font, 30, red)
        else:
            text_quit = text_format("QUIT", font, 30, white)

        if selected1=="options":
            text_opt=text_format("::INSTRUCTIONS::", font, 40, pink)
        else:
            text_opt = text_format("::INSTRUCTIONS::",font,40,pink)

        if selected1=="option":
            text_opts=text_format("BLUE  IS THE HUMAN PLAYER", font, 20, dblue)
        else:
            text_opts = text_format("BLUE PIECE IS THE HUMAN PLAYER",font,20,dblue)
        
        if selected1=="option1":
            text_opt1=text_format("WHITE PIECE IS THE COMPUTER PLAYER", font, 20,dblue)
        else:
            text_opt1 = text_format("WHITE IS THE COMPUTER PLAYER",font,20,dblue)
 
        title_rect=title.get_rect()
        start_rect=text_start.get_rect()
        quit_rect=text_quit.get_rect()
        opt_rect=text_opt.get_rect()
        opts_rect=text_opts.get_rect()
        opt1_rect=text_opts.get_rect()
 
        # Main Menu Text
        screen.blit(title, (screen_width/2 - (title_rect[2]/2), 80))
        screen.blit(text_start, (screen_width/2 - (start_rect[2]/2), 300))
        screen.blit(text_quit, (screen_width/2 - (quit_rect[2]/2), 360))
        screen.blit(text_opt, (screen_width/2 - (opt_rect[2]/2), 430))
        screen.blit(text_opts, (screen_width/2 - (opts_rect[2]/2), 500))
        screen.blit(text_opt1, (screen_width/2 - (opt1_rect[2]/2), 550))
        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("AI Based Action Selection Checkers Game")


        #Initialize the Game





#creating a module around the checkrs game and then add an API on top of the game
# so that we can use it with an AI later on

#1 setup a pygame display where we will be drawing everything onto.
#2 setup a basic event loop: this will check if we press the mouse, if we press a certain key. MAIN LOOP
#3 setup basic drawings, draw the board for the chessboard, draw the pieces

FPS = 60     #G=Frame per second

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
#WIN: a constant value. WIDTH,HEIGHT: 2 Variables we will define(in constants.py)

#set a caption
pygame.display.set_caption('Checkers Game using Minimax Agent')




#this will take the position of our mouse, and based on the position of our mouse what row and col we are in
def get_row_col_from_mouse(pos):
    x, y = pos   #this is gonna be a tuple that will have the x pos of our mouse and the y position of our mouse
    #and based on the square size we can calcu very easily which row and col we are in
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


#SEE MOUSE BUTTON DOWN
#when we press the mouse down, 
# we will get what row and col were in, we will select that piece and move that piece wherever we want to move



#define a main funcion
def main():
    #create an event loop: this will run 'x' times per second which will check everything
    run = True

    #define a clock:define our game to run at a constant frame rate.
    #the clock will make sure that the main event loop wont run too fast or too slow. 
    clock = pygame.time.Clock()

    #create a Baord obj
    #board = Board()

    #create a Game object 
    game = Game(WIN)


    #for moving the pieces
    #piece = board.get_piece(0,1)
    #board.move_pieces(piece,4, 3)

    while run:
        clock.tick(FPS)

        #FOR AI MINIMAX
        if game.turn == WHITE:
            value, new_board = minimax(game.get_board(), 3, WHITE, game)
            game.ai_move(new_board)


        #for winner
        if game.winner() != None:
            print(game.winner())
            run = False
        
        #setup the basic event loop for pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:    #this means we hit the red button on the top of the screen
                run = False
            
            if event.type ==  pygame.MOUSEBUTTONDOWN:     #This means we pressed any mouse on our mouse down
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
        
                #call the select moethod from game.py
                #if game.turn == BLUE:
                game.select(row, col)

        game.update()

        #board.draw_squares(WIN)    #from board.py file, this function is called.
        #board.draw(WIN)             #for pieces, from board.py
        #pygame.display.update()
    
    pygame.quit()
main_menu()
main()