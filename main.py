import threading
from tkinter import *
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

def show_winner(winner):
    root = Tk()
    label = Label(root, text=winner, font=("Helvetica", 16))
    label.pack(padx=50, pady=50)
    root.mainloop()

def main():
    in_game = True
    NAVY_player = 0
    Red_player = 0
    start = True
    while in_game:
        if start:
            pass
        else:
            if game.winner == "NAVY wins":
                NAVY_player+=1
            elif game.winner == "RED wins":
                Red_player+=1

        print("NAVY: " + str(NAVY_player))
        print("Red: " + str(Red_player))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                in_game = False
        run = True
        clock = pygame.time.Clock()
        game = Game(Screen)
        winner_shown = False
        start = False
        while run:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    in_game = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    clicked_color = get_color_at_position(pos)
                    game.movePiece(pos, clicked_color, Screen)

            game.updateScreen(Screen)
            if game.winner and not winner_shown:
                winner_shown = True
                # Start the Tkinter thread
                tkinter_thread = threading.Thread(target=show_winner(game.winner))
                tkinter_thread.start()
                run = False

    pygame.quit()   

main()
