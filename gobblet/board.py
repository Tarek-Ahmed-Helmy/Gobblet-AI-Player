import pygame
from .constants import *
from .piece import Piece

class Board:
    def __init__(self):
        self.board = []

    def draw_squares(self,screen):
        screen.fill(GREY)
        for row in range(ROWS):
            for col in range(COLUMNS):
              #  pygame.draw.rect(screen, BROWN, (col * (WIDTH / COLUMNS), row * (HEIGHT / ROWS), WIDTH / COLUMNS - PADDING, HEIGHT / ROWS - PADDING))
               # pygame.draw.rect(screen, BLACK, (col * (WIDTH / COLUMNS), row * (HEIGHT / ROWS), WIDTH / COLUMNS - PADDING, HEIGHT / ROWS - PADDING), 2)
                pygame.draw.rect(screen,BROWN,(row*SQUARE_WIDTH+PADDING,col*SQUARE_HEIGHT+PADDING,SQUARE_WIDTH,SQUARE_HEIGHT))
                pygame.draw.rect(screen, BLACK,(row*SQUARE_WIDTH+PADDING, col*SQUARE_HEIGHT+PADDING,SQUARE_WIDTH,SQUARE_HEIGHT),1)

    def draw(self,screen):
        for red in [1, 2, 3]:
            piece = Piece(red*243,100,RED,SIZE4)
            piece.draw(screen)  
        for blue in [1, 2, 3]:
             piece = Piece(blue*243,900,BLUE,SIZE4)
             piece.draw(screen)
        

