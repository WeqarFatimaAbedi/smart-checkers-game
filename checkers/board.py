
#Put a class named "Board": This class will represent a checkers board.
#This class will handle all the different pieces moving, leading specific pieves, deleting specific pieces, rawing itself on the screen.

import pygame
from .constants import BLACK, ROWS, RED, SQUARE_SIZE, COLS, WHITE, BLUE, GREEN
from .piece import Piece


class Board:
    def __init__(self):

        #Attributes

        #1. Internal representation of the board
        self.board = []   #creating a 2D list
        #Whose turn is it
        #self.selected_piece = None  #have we selected a piece yet, or not
        self.red_left = self.white_left = 12 #keeps track of how many red, how many white pieces we have.
        self.red_kings = self.white_kings = 0
        self.create_board()



    #A surface/window to draw the red and black cubes on in a checkerboard pattern
    def draw_squares(self, win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, RED,(row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE
                ))    #Drawing the red rectangle starting from the top left 




    #for moving the pieces
    #sel, piece=which piece we want to move it to, row, col=on which row and col we want to move it to
    def move_pieces(self, piece, row, col):
        #move the piece within the list, also chenge the piece itself
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        #swapping is happening by reversing

        piece.move_pieces(row, col)

        #Checking: if the piece hits the last row or first col, then making that piece as a king.
        if row == ROWS -1 or row == 0:
            piece.King_piece()   #King_piece(): from piece file, this will make the piece a king

            if piece.color == WHITE:
                self.white_kings += 1

            else:
                self.red_kings += 1

    #giving the baord object a row and col, and it wll give a piece back
    def get_piece(self, row, col):
        return self.board[row][col]




    #PIECES, creating the actual internal representation of the board and we will add a bunch of pieces to the list
    #A new class "piece.py"
    def create_board(self):
        for row in range(ROWS):
            self.board.append([])    #empty list: interior list for each row, 
                                     #a list that represents what each row is going to have inside of it
            for col in range(COLS):

                #if the current column tha we are one, if its divisble by if that equals to row+1, so we are on row 1
                if col % 2 == ((row + 1) % 2):   #part 2 3mins

                    #draw when we are in a certain row. 
                    # if row < 3, 0 1 2 are the first 3 rows, we want to draw the white pieces in
                    if row < 3:
                        self.board[row].append(Piece(row, col, WHITE))

                    #if row>4, if irow is 5 6 7, then  we want to draw the red pieces
                    elif row > 4:
                        self.board[row].append(Piece(row, col, BLUE))
                    
                    #when no piece, add a zero
                    else:
                        # this will be a blank piece
                        self.board[row].append(0)  
                #when we dont add a piece, add a zero
                else:
                    self.board[row].append(0)

    #This will draw the board, this will draw all of the pieces and the squares.
    def draw(self, win):
        self.draw_squares(win)   #we will draw the sqaures on the window

        #Loop throuhout the pieces and draw those
        for row in range(ROWS):
            for col in range(COLS):

                #loop through the board
                piece = self.board[row][col]
                if piece != 0:     #if piece is 0, we will not draw anything
                    piece.draw_piece(win)    # draw the oiece on the window


    def remove(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.color == BLUE:
                    self.red_left -=1
                else:
                    self.white_left -= 1

    def winner(self):      #This will return the color if they won
        if self.red_left <= 0:
            return WHITE
        elif self.white_left <= 0:
            return BLUE

        return None

    def get_valid_moves(self, piece):
        moves = {}     #store the move as the key, so what place we could potentially move to as a row 
        
        #these are the diagonals (left or right)
        left = piece.col - 1   #we are moving left one
        right = piece.col + 1
        row = piece.row

        #checking whether we can move up or we can move down based on the color and based on if the piece is a KING
        if piece.color == BLUE or piece.king:
            moves.update(self._traverse_left(row -1, max(row-3, -1), -1, piece.color, left))
            moves.update(self._traverse_right(row -1, max(row-3, -1), -1, piece.color, right))

        if piece.color == WHITE or piece.king:
            moves.update(self._traverse_left(row +1, min(row+3, ROWS), 1, piece.color, left))
            moves.update(self._traverse_right(row +1, min(row+3, ROWS), 1, piece.color, right))

        return moves

    #This function will look at the left diagonals for us.
    def _traverse_left(self, start, stop, step, color, left, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break   #when we are at the edge of the board on the left side then no further cols we have
            
            current = self.board[r][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] = last + skipped

                else:
                    moves[(r, left)] = last

                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, ROWS)

                    moves.update(self._traverse_left(r+step, row, step, color, left-1, skipped=last))
                    moves.update(self._traverse_right(r+step, row, step, color, left+1, skipped=last))
                break

            elif current.color == color:
                break
            else:
                last = [current]

            left -= 1

        return moves

    #WHY USE THESE PARAMETERS:
    #start, stop, step is going to be for the for loops we're going to put inside of here
    #step: very imp, becuase it tells us, we go up? or down? when im traversing thro the rows for the diagonals
    #skipped: this will tell us, have we skipped any pieces yet? if yes, we can only move to squares when we skip another piece

    #This method will move to the right
    #right: where are we starting in terms of col, when were traversing to the left
    def _traverse_right(self, start, stop, step, color, right, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= COLS:
                break   #when we are at the edge of the board on the left side then no further cols we have
            
            current = self.board[r][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, right)] = last + skipped

                else:
                    moves[(r, right)] = last

                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, ROWS)

                    moves.update(self._traverse_left(r+step, row, step, color, right-1, skipped=last))
                    moves.update(self._traverse_right(r+step, row, step, color, right+1, skipped=last))
                break

            elif current.color == color:
                break
            else:
                last = [current]

            right += 1

        return moves

                                        #FOR AI MINIMAX 
    #The evaluate(): this method will tell us given the state of this board what is its score?
    def evaluate(self):   #This will take into account hwo many kings we have? and how many pieces we have?
        return self.white_left - self.red_left + (self.white_kings * 0.5 - self.red_kings * 0.5) 
        #Thsi will give us another value. 
    
    #This method will return to us all the pieces of a certain color. so we can use the board 
    def get_all_pieces(self, color):
        pieces = []
        for row in self.board:
            for piece in row:
                if piece != 0 and piece.color == color:
                    pieces.append(piece)
        return pieces

    
