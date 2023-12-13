import pygame
from .constants import *
from .piece import Piece
from collections import deque

class Board:
    def __init__(self):
        self.board = []

    def draw_squares(self,screen):
        screen.fill(GREY)
        for row in range(ROWS):
            for col in range(COLUMNS):
                pygame.draw.rect(screen,BROWN,(row*SQUARE_SIZE+PADDING,col*SQUARE_SIZE+PADDING,SQUARE_SIZE,SQUARE_SIZE))
                pygame.draw.rect(screen, BLACK,(row*SQUARE_SIZE+PADDING, col*SQUARE_SIZE+PADDING,SQUARE_SIZE,SQUARE_SIZE),1)

    def draw(self,screen):
        for i in range(len(self.board)):
            for j in range(self.board[i]):
                if self.board[i][j]!=0:
                    self.board[i][j].draw(screen)
        
    def create_board(self):
        gobblet_sizes=[SIZE1, SIZE2, SIZE3, SIZE4]
        stack1 = deque()
        stack2 = deque()
        stack3 = deque()
        stack4 = deque()
        stack5 = deque()
        stack6 = deque()
        shelf1 = [stack1, stack2, stack3]
        shelf2 = [stack4, stack5, stack6]
        self.board.append(shelf1)
        self.board.append([deque(), deque(), deque(), deque()])
        self.board.append([0, 0, 0, 0])
        self.board.append([0, 0, 0, 0])
        self.board.append([0, 0, 0, 0])
        self.board.append(shelf2)

        for i in range(len(shelf1)):
            for size in gobblet_sizes:
                shelf1[i].append(Piece((i+1)*243,100,RED,size))

        for i in range(len(shelf2)):
            for size in gobblet_sizes:
                shelf2[i].append(Piece((i+1)*243,900,BLUE,size))

        
            
        

# board = Board()
# board.create_board()