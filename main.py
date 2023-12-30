import threading
from tkinter import *
import pygame
from gobblet.constants import *
from gobblet.game import Game
from gobblet.board import Board
from gobblet.gameStatus import *

# clock ticks
FPS = 60

NAVY_player = 0
Red_player = 0
# Function to convert get color
def get_color_at_position(mouse_pos, Screen):
    color = Screen.get_at(mouse_pos)
    return color

def show_winner(winner):
    root = Tk()
    label = Label(root, text=winner, font=("Helvetica", 16))
    label.pack(padx=50, pady=50)
    root.mainloop()

def player_vs_player():
    global NAVY_player
    global Red_player
    Screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Gobblet")
    in_game = True
    start = True
    while in_game:
        if start:
            pass
        else:
            if game.winner == "NAVY wins":
                NAVY_player+=1
            elif game.winner == "RED wins":
                Red_player+=1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                in_game = False
        run = True
        clock = pygame.time.Clock()
        game = Game(Screen)
        game.cur_score = (NAVY_player, Red_player)
        winner_shown = False
        start = False
        while run:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    in_game = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if game.restart_button.rect.collidepoint(event.pos):
                        pygame.quit()
                        player_vs_player()
                    pos = pygame.mouse.get_pos()
                    clicked_color = get_color_at_position(pos, Screen)
                    game.movePiece(pos, clicked_color, Screen)

            game.updateScreen(Screen)
            if game.winner and not winner_shown:
                winner_shown = True
                # Start the Tkinter thread
                tkinter_thread = threading.Thread(target=show_winner(game.winner))
                tkinter_thread.start()
                run = False

    pygame.quit()

def startGame(game_mode, mainWindow):
    if game_mode == 1:
        mainWindow.destroy()   
        player_vs_player()
    

def chooseLevel(mainWindow):
    mainWindow.destroy()
    chooseWindow = Tk()
    button = Button(chooseWindow, text="Easy", command=lambda: startGame(2, mainWindow))
    button.pack()
    button = Button(chooseWindow, text="Hard", command=lambda: startGame(3, mainWindow))
    button.pack()
    chooseWindow.mainloop()

def chooseLevel_AI(mainWindow):
    mainWindow.destroy()
    chooseWindow = Tk()
    button = Button(chooseWindow, text="Easy vs Hard", command=lambda: startGame(4, mainWindow))
    button.pack()
    button = Button(chooseWindow, text="Hard vs Easy", command=lambda: startGame(5, mainWindow))
    button.pack()
    button = Button(chooseWindow, text="Easy vs Easy", command=lambda: startGame(6, mainWindow))
    button.pack()
    button = Button(chooseWindow, text="Hard vs Hard", command=lambda: startGame(7, mainWindow))
    button.pack()
    chooseWindow.mainloop()
    

def main():
    mainWindow = Tk()
    button = Button(mainWindow, text="Player vs Player", command=lambda: startGame(1, mainWindow))
    button.pack()
    button = Button(mainWindow, text="Player vs AI", command=lambda: chooseLevel(2, mainWindow))
    button.pack()
    button = Button(mainWindow, text="AI vs AI", command=lambda: startGame(3, mainWindow))
    button.pack()

    mainWindow.mainloop()
    

main()
