from tkinter import *
from tkinter import ttk
from gobblet.constants import *
from gobblet.gameStatus import *
from minimax.algorithm import *
from gobblet.game_modes import *


def startGame(game_mode, mainWindow):
    mainWindow.destroy()
    returned = 0
    if game_mode == 1:   
        returned = player_vs_player()
    elif game_mode == 2:
        returned = player_vs_ai_easy()
    elif game_mode == 3:
        returned = player_vs_ai_hard()
    elif game_mode == 4:
        returned = ai_ez_vs_ai_hd()
    elif game_mode == 5:
        returned = ai_hd_vs_ai_ez()
    elif game_mode == 6:
        returned = ai_ez_vs_ai_ez()
    elif game_mode == 7:
        returned = ai_hd_vs_ai_hd()
    if returned == "game modes":
        main()

def chooseLevel(mainWindow):
    mainWindow.destroy()
    chooseWindow = Tk()
    chooseWindow.title("Gobblet")
    chooseWindow.geometry("400x300+590+250")
    label = ttk.Label(chooseWindow, text="Choose Level of Difficulty", font=('helvetica', 16))
    label.pack()
    button = ttk.Button(chooseWindow, text="Easy", command=lambda: startGame(2, chooseWindow))
    button.pack(pady=5,padx=5)
    button = ttk.Button(chooseWindow, text="Hard", command=lambda: startGame(3, chooseWindow))
    button.pack(pady=5,padx=5)
    button = ttk.Button(chooseWindow, text="Back", command=lambda: main(chooseWindow), padding=(10, 5))
    button.pack(pady=20, padx=50)
    style = ttk.Style()
    style.configure("TButton", padding=10, font=("Helvetica", 12))
    chooseWindow.mainloop()

def chooseLevel_AI(mainWindow):
    mainWindow.destroy()
    chooseWindow = Tk()
    chooseWindow.title("Gobblet")
    chooseWindow.geometry("500x400+550+220")
    label = ttk.Label(chooseWindow, text="Choose Level of Difficulty for the two AI_s", font=('helvetica', 14))
    label.pack(pady=5,padx=5)
    button = ttk.Button(chooseWindow, text="Easy vs Hard", command=lambda: startGame(4, chooseWindow))
    button.pack(pady=5,padx=5)
    button = ttk.Button(chooseWindow, text="Hard vs Easy", command=lambda: startGame(5, chooseWindow))
    button.pack(pady=5,padx=5)
    button = ttk.Button(chooseWindow, text="Easy vs Easy", command=lambda: startGame(6, chooseWindow))
    button.pack(pady=5,padx=5)
    button = ttk.Button(chooseWindow, text="Hard vs Hard", command=lambda: startGame(7, chooseWindow))
    button.pack(pady=5,padx=5)
    button = ttk.Button(chooseWindow, text="Back", command=lambda: main(chooseWindow), padding=(10, 5))
    button.pack(pady=30, padx=30)
    style = ttk.Style()
    style.configure("TButton", padding=10, font=("Helvetica", 12))
    chooseWindow.mainloop()

def main(chooseWindow=None):
    if chooseWindow:
        chooseWindow.destroy()
    mainWindow = Tk()
    mainWindow.title("Gobblet")
    mainWindow.geometry("400x300+590+250")
    label = ttk.Label(mainWindow, text="Choose Game Mode", font=('helvetica', 16))
    label.pack(padx=10,pady=10)
    button = ttk.Button(mainWindow, text="Player vs Player", command=lambda: startGame(1, mainWindow))
    button.pack(padx=10,pady=10)
    button = ttk.Button(mainWindow, text="Player vs AI", command=lambda: chooseLevel(mainWindow))
    button.pack(padx=10,pady=10)
    button = ttk.Button(mainWindow, text="AI vs AI", command=lambda: chooseLevel_AI(mainWindow))
    button.pack(padx=10,pady=10)
    style = ttk.Style()
    style.configure("TButton", padding=10, font=("Helvetica", 12))
    mainWindow.mainloop()

main()