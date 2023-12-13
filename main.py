import pygame
from gobblet.constants import *
from gobblet.board import Board

#clock ticks
FPS=60

Screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Gobblet')


def main():
    run=True
    clock=pygame.time.Clock()
    board=Board()
    board.create_board()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
        board.draw_squares(Screen)
        board.draw(Screen)
        pygame.display.update()
    pygame.quit()


main()
