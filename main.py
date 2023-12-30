import threading
from tkinter import *
from tkinter import ttk
import pygame
from gobblet.constants import *
from gobblet.game import Game
from gobblet.board import Board
from gobblet.gameStatus import *
from minimax.algorithm import *

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

def player_vs_ai_easy():
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
            if game.turn == RED:
                value, new_board = minimax(game.board, 1, True)
                game.board = new_board
                game.computer_move()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    in_game = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if game.restart_button.rect.collidepoint(event.pos):
                        pygame.quit()
                        player_vs_ai_easy()
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

def player_vs_ai_hard():
    pass

def ai_ez_vs_ai_hd():
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
        game.updateScreen(Screen)
        while run:
            clock.tick(FPS)
            if game.turn == RED:
                value, new_board = minimax(game.board, 2, True)
                game.board = new_board
                game.computer_move()
            elif game.turn == NAVY:
                value, new_board = minimax(game.board, 2, False)
                game.board = new_board
                game.computer_move()

            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    in_game = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if game.restart_button.rect.collidepoint(event.pos):
                        pygame.quit()
                        ai_ez_vs_ai_ez()

            game.updateScreen(Screen)
            if game.winner and not winner_shown:
                winner_shown = True
                # Start the Tkinter thread
                tkinter_thread = threading.Thread(target=show_winner(game.winner))
                tkinter_thread.start()
                run = False

    pygame.quit()

def ai_hd_vs_ai_ez():
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
        game.updateScreen(Screen)
        while run:
            clock.tick(FPS)
            if game.turn == RED:
                value, new_board = minimax(game.board, 2, True)
                game.board = new_board
                game.computer_move()
            elif game.turn == NAVY:
                value, new_board = minimax(game.board, 2, False)
                game.board = new_board
                game.computer_move()

            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    in_game = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if game.restart_button.rect.collidepoint(event.pos):
                        pygame.quit()
                        ai_ez_vs_ai_ez()

            game.updateScreen(Screen)
            if game.winner and not winner_shown:
                winner_shown = True
                # Start the Tkinter thread
                tkinter_thread = threading.Thread(target=show_winner(game.winner))
                tkinter_thread.start()
                run = False

    pygame.quit()

def ai_ez_vs_ai_ez():
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
        game.updateScreen(Screen)
        while run:
            clock.tick(FPS)
            if game.turn == RED:
                value, new_board = minimax(game.board, 2, True)
                game.board = new_board
                game.computer_move()
            elif game.turn == NAVY:
                value, new_board = minimax(game.board, 2, False)
                game.board = new_board
                game.computer_move()

            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    in_game = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if game.restart_button.rect.collidepoint(event.pos):
                        pygame.quit()
                        ai_ez_vs_ai_ez()

            game.updateScreen(Screen)
            if game.winner and not winner_shown:
                winner_shown = True
                # Start the Tkinter thread
                tkinter_thread = threading.Thread(target=show_winner(game.winner))
                tkinter_thread.start()
                run = False

    pygame.quit()

def ai_hd_vs_ai_hd():
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
        game.updateScreen(Screen)
        while run:
            clock.tick(FPS)
            if game.turn == RED:
                value, new_board = minimax(game.board, 2, True)
                game.board = new_board
                game.computer_move()
            elif game.turn == NAVY:
                value, new_board = minimax(game.board, 2, False)
                game.board = new_board
                game.computer_move()

            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    in_game = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if game.restart_button.rect.collidepoint(event.pos):
                        pygame.quit()
                        ai_ez_vs_ai_ez()

            game.updateScreen(Screen)
            if game.winner and not winner_shown:
                winner_shown = True
                # Start the Tkinter thread
                tkinter_thread = threading.Thread(target=show_winner(game.winner))
                tkinter_thread.start()
                run = False

    pygame.quit()

def startGame(game_mode, mainWindow):
    mainWindow.destroy()
    if game_mode == 1:   
        player_vs_player()
    elif game_mode == 2:
        player_vs_ai_easy()
    elif game_mode == 3:
        player_vs_ai_hard()
    elif game_mode == 4:
        ai_ez_vs_ai_hd()
    elif game_mode == 5:
        ai_hd_vs_ai_ez()
    elif game_mode == 6:
        ai_ez_vs_ai_ez()
    elif game_mode == 7:
        ai_hd_vs_ai_hd()
    

    

def chooseLevel(mainWindow):
    mainWindow.destroy()
    chooseWindow = Tk()
    chooseWindow.geometry("400x300+590+290")
    label = ttk.Label(chooseWindow, text="Choose Level of Difficulty", font=('helvetica', 16))
    label.pack()
    button = ttk.Button(chooseWindow, text="Easy", command=lambda: startGame(2, chooseWindow))
    button.pack()
    button = ttk.Button(chooseWindow, text="Hard", command=lambda: startGame(3, chooseWindow))
    button.pack()
    style = ttk.Style()
    style.configure("TButton", padding=10, font=("Helvetica", 12))
    chooseWindow.mainloop()

def chooseLevel_AI(mainWindow):
    mainWindow.destroy()
    chooseWindow = Tk()
    chooseWindow.geometry("400x300+590+290")
    label = ttk.Label(chooseWindow, text="Choose Level of Difficulty for the two AI_s", font=('helvetica', 14))
    label.pack()
    button = ttk.Button(chooseWindow, text="Easy vs Hard", command=lambda: startGame(4, chooseWindow))
    button.pack()
    button = ttk.Button(chooseWindow, text="Hard vs Easy", command=lambda: startGame(5, chooseWindow))
    button.pack()
    button = ttk.Button(chooseWindow, text="Easy vs Easy", command=lambda: startGame(6, chooseWindow))
    button.pack()
    button = ttk.Button(chooseWindow, text="Hard vs Hard", command=lambda: startGame(7, chooseWindow))
    button.pack()
    style = ttk.Style()
    style.configure("TButton", padding=10, font=("Helvetica", 12))
    chooseWindow.mainloop()
    

def main():
    mainWindow = Tk()
    mainWindow.geometry("400x300+590+290")
    label = ttk.Label(mainWindow, text="Game Mode", font=('helvetica', 16))
    label.pack()
    button = ttk.Button(mainWindow, text="Player vs Player", command=lambda: startGame(1, mainWindow))
    button.pack()
    button = ttk.Button(mainWindow, text="Player vs AI", command=lambda: chooseLevel(mainWindow))
    button.pack()
    button = ttk.Button(mainWindow, text="AI vs AI", command=lambda: chooseLevel_AI(mainWindow))
    button.pack()
    style = ttk.Style()
    style.configure("TButton", padding=10, font=("Helvetica", 12))
    mainWindow.mainloop()
    

main()
