import pygame
from gobblet.constants import *
from gobblet.game import Game
from gobblet.board import Board
from gobblet.gameStatus import *

# clock ticks
FPS = 60

Screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gobblet")

# Function to convert get color
def get_color_at_position(mouse_pos):
    color = Screen.get_at(mouse_pos)
    return color


def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(Screen)
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clicked_color = get_color_at_position(pos)
                game.movePiece(pos, clicked_color, Screen)

        game.updateScreen(Screen)

    pygame.quit()

main()
