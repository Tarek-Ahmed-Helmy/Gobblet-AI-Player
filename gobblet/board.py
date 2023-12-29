import pygame
from .constants import *
from .piece import Piece
from .stack import Stack

class Board:
    def __init__(self):
        self.board = []

    def draw_squares(self,screen):
        screen.fill(GREY)
        for row in range(ROWS):
            for col in range(COLUMNS):
                pygame.draw.rect(screen,ORANGE,(row*SQUARE_SIZE+PADDING,col*SQUARE_SIZE+PADDING,SQUARE_SIZE,SQUARE_SIZE))
                pygame.draw.rect(screen, BLACK,(row*SQUARE_SIZE+PADDING, col*SQUARE_SIZE+PADDING,SQUARE_SIZE,SQUARE_SIZE),1)

    def draw_pieces(self,screen):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j].isEmpty() == False:
                    self.board[i][j].peek().draw(screen)




     # still no Need
    def identify_empty_squares(self):
        empty_squares = []
        for row_idx, row in enumerate(self.board):
            for col_idx, col in enumerate(row):
                if col.isEmpty():
                    empty_squares.append((row_idx, col_idx))
        return empty_squares


    # gobblet is the start, screen is the destination
    def put_piece(self,rowG,colG,rowS,colS,screen):
        if not(self.board[rowG][colG].isEmpty()):
            if self.board[rowS][colS].isEmpty() or self.board[rowG][colG].peek().size > self.board[rowS][colS].peek().size:
                piece = self.board[rowG][colG].pop()
                piece.x = colS * SQUARE_SIZE + PADDING + SQUARE_SIZE // 2
                piece.y = (rowS-1) * SQUARE_SIZE + PADDING + SQUARE_SIZE // 2
                self.board[rowS][colS].push(piece)
                self.draw_pieces(screen)
            
            
       
    def create_board(self):
        gobblet_sizes=[SIZE1, SIZE2, SIZE3, SIZE4]
        stack1 = Stack()
        stack2 = Stack()
        stack3 = Stack()
        stack4 = Stack()
        stack5 = Stack()
        stack6 = Stack()
        player1 = [stack1, stack2, stack3]
        player2 = [stack4, stack5, stack6]
        self.board.append(player2)
        self.board.append([Stack(), Stack(), Stack(), Stack()])
        self.board.append([Stack(), Stack(), Stack(), Stack()])
        self.board.append([Stack(), Stack(), Stack(), Stack()])
        self.board.append([Stack(), Stack(), Stack(), Stack()])
        self.board.append(player1)

        for i in range(len(player2)):
            for size in gobblet_sizes:
                player2[i].push(Piece((i+1)*WIDTH/(WIN_LEN/250),HEIGHT/(WIN_LEN/100),RED,size))

        for i in range(len(player1)):
            for size in gobblet_sizes:
                player1[i].push(Piece((i+1)*WIDTH/(WIN_LEN/250),HEIGHT/(WIN_LEN/900),NAVY,size))