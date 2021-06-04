#Make another file inside checkers, call this game.py: this file is responsible for actually handling the game.
# Whose turn is it?, did we select the piece? Can the piece move here or there?
#Game class: this class will allow us to interface with the board, the pieces in which i used few simple methods.
#this is not depending on anything


import pygame
from .constants import RED, WHITE, BLUE, GREEN, SQUARE_SIZE
from checkers.board import Board



class Game:
    def __init__(self, win):          #win:window we want to draw this game on
        self._init()
        self.win = win

    
    #update method to update the pygame display
    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    
    #this is essentially initializing the game. This method is private but only sees the rest method.
    def _init(self):
        self.selected = None        #which piece is selected by someone whose playing the game
        self.board = Board() 
        #this line is used because, from main() we will not make a board object but a Game
        #the Game will control the board for us, so rather having to get the piece or move the piece all this will use the game.

        self.turn = BLUE
        #self.turn = RED
        self.valid_moves = {}    #this will tell what the current valid moves are for whatever player is playing

    def winner(self):
        return self.board.winner()

    #reset method to reset the game
    def reset_game(self):
       self._init()

    
    #slect method to select the row and column. 
    def select(self, row, col):   #this will tell the row and col we have selected 
        #based on the selected row and column 
        if self.selected:
            result = self._move(row, col)
            if not result:        #If selected an invalid move then this will call the main select method again to reste
                self.selected = None
                self.select(row, col)
                
        piece = self.board.get_piece(row, col)
        #If we're not selecting an emptypiece, we are actually selecting RED or WHITE
        if piece != 0 and piece.color == self.turn:     
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True      #If the selection is valid, then return True

        return False         #else if not valid move selected return False.


            
    #This is a private method, when the user selects the piece it calls the select piece.
    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            #piece = 0 that is an empty place, if its !=0 then there is a piece in that place.
            self.board.move_pieces(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()    #call the change_turn method
            
        else:
            return False
        return True

    #if its RED it will go to WHITE or WHITE then itll go to RED
    def change_turn(self):
        self.valid_moves = {}
        if self.turn == BLUE:
            self.turn = WHITE
        else:
            self.turn = BLUE


    #for JUMP. draw the valid moves
    def draw_valid_moves(self, moves):       #all "moves" are dictionary  
        for move in moves:                   #this loops through all the keys of the dictioanry
            row, col = move
            pygame.draw.circle(self.win, GREEN, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 15)

                                        #FOR AI MINIMAX
    
    def get_board(self):
        return self.board

    #when the AI makes a moves then this will return to us the new board after its move
    def ai_move(self, board):
        self.board = board
        self.change_turn()

