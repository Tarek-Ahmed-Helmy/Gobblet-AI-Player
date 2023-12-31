import threading
import pygame
from tkinter import *
from gobblet.constants import *
from gobblet.game import Game
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
                value, new_board = minimax(game.board, 2, True)
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
                value, new_board = minimax(game.board, 1, True)
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
                value, new_board = minimax(game.board, 1, False)
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
                value, new_board = minimax(game.board, 1, True)
                game.board = new_board
                game.computer_move()
            elif game.turn == NAVY:
                value, new_board = minimax(game.board, 1, False)
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