import pygame
from .constants import *
from .piece import Piece

class Board:
    def __init__(self):
        self.board = [[],[]]

    def draw_squares(self,screen):
        screen.fill(WHITE)
        for row in range(ROWS):
            for col in range(COLUMNS):
              #  pygame.draw.rect(screen, BROWN, (col * (WIDTH / COLUMNS), row * (HEIGHT / ROWS), WIDTH / COLUMNS - PADDING, HEIGHT / ROWS - PADDING))
               # pygame.draw.rect(screen, BLACK, (col * (WIDTH / COLUMNS), row * (HEIGHT / ROWS), WIDTH / COLUMNS - PADDING, HEIGHT / ROWS - PADDING), 2)
                pygame.draw.rect(screen,BROWN,(row*SQUARE_WIDTH+PADDING,col*SQUARE_HEIGHT+PADDING,SQUARE_WIDTH,SQUARE_HEIGHT))
                pygame.draw.rect(screen, BLACK,(row*SQUARE_WIDTH+PADDING, col*SQUARE_HEIGHT+PADDING,SQUARE_WIDTH,SQUARE_HEIGHT),1)

    def draw(self,screen):
        for black in [2,6,10]:
            piece = Piece(60+black*60,60,BLACK,SIZE4)
            piece.draw(screen)  
        for white in [2,6,10]:
             piece = Piece(60+white*60,580,GREY,SIZE4)
             piece.draw(screen)
