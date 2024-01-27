# Gobblet-AI-Player
## Table of Contents
- [Gobblet-AI-Player](#gobblet-AI-Player)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Game Description](#game-description)
  - [Game Modes](#game-modes)
  - [Algorithms](#algorithms)
    - [Game-Palying Algorithms](#game-palying-algorithms)
    - [Heuristics](#heuristics)
  - [The GUI](#the-gui)
  - [User Manual](#user-manual)
    - [Run From Source](#run-from-source)
    - [Run From Executable](#run-from-executable)
    - [Game Manual](#game-manual)

## Introduction
In this project, we will explore the game-playing of Gobblet, Gobblet is an abstract game
played on a 4x4 grid with each of the two players having twelve pieces that can nest on
top of one another to create three stacks of four pieces.
The project is fully implemented using Python language with PyGame.

## Game Description
The goal in Gobblet is to place four of your pieces in a horizontal, vertical, or diagonal
row. Your pieces start nested off the board. On a turn, you either play one exposed
piece from your three off-the-board piles or move one piece on the board to any other
spot on the board where it fits. A larger piece can cover any smaller piece. A piece
being played from off the board may not cover an opponent's piece unless it's in a row
where your opponent has three of his color.
Your memory is tested as you try to remember which color one of your larger pieces is
covering before you move it. As soon as a player has four like-colored pieces in a row,
he wins — except in one case: If you lift your piece and reveal an opponent's piece that
finishes a four-in-a-row, you don't immediately lose; you can't return the piece to its
starting location, but if you can place it over one of the opponent's three other pieces in
that row, the game continues..

Components
16-square playing board
12 white Gobblets
12 black Gobblets

For more information about the game, please watch this video [Wikipedia](https://www.youtube.com/watch?v=aSaAjQY8_b0) 

For game rules, you can visit this [pdf](https://www.boardspace.net/gobblet/english/gobblet_rules.pdf) 

## Game Modes
The game has 3 modes with different difficulty levels:
| Game Mode |
| --- |
| Player vs Player  |
| Player vs AI |
| AI vs AI |

this mode (Player vs AI) has 2 difficulty levels:
| Difficulty Level | 
| --- |
| Easy |
| Hard |

and this mode (AI vs AI) has 4 difficulty levels:
| Difficulty Level | 
| --- |
| Easy vs Hard |
| Hard vs Easy |
| Easy vs Easy |
| Hard vs Hard |

## Algorithms

### Game-Palying Algorithms

The game algorithms used in this project are:

 The minimax algorithm: a basic search algorithm that examines all possible moves from a given position and selects the move that leads to the best outcome for the current player


### Heuristics
The heuristics used for evaluating the game state in the project are primarily based on counting the number of pieces (both in rows and columns) for each player (Navy and Red).
-Easy mode : 
The heuristic function used in this mode is, counting the number of pieces for both players in each row and column then adjusting the scores based on the interaction between rows and columns without taking their sizes in consideration (Penalises the score if there are both Navy and Red pieces in a row or column) and finally returns the difference between two scores. 
-Hard mode : 
The heuristic function used in this mode introduces a more complex scoring system based on piece sizes, interactions between rows and columns, and a penalty for mixed rows/columns. First, it counts the number of pieces for both the computer and the player in each row and column. It calculates the score for both by summing pieces weights ( assigning appropriate weight to each piece based on its size ). Stores this value in separate variables one for the player and the other for the computer, it  then checks the number of both computer pieces and player pieces for each row and column:
If the number of computer pieces is greater than zero and there aren’t any player pieces in the same row or column then multiply the number of computer pieces in this row or column by the score of the computer to add an extra score to the computer (because in this state the computer can win in this row or column).
If the number of player pieces is greater than zero and there aren’t any computer pieces in the same row or column then multiply the number of computer pieces in this row or column by the score of the player to add an extra score to the player (because in this state the player can win in this row or column).
If there exist pieces in the same row or column for both the player and the computer then subtract the multiplication of the number of player and computer pieces from the computer score to reduce the score of the computer (because in this state the computer cannot win in this row or column).

After evaluating the score of both the player and computer in the passed board state then we need to check if this state indicates a win for the player then we return - infinity while if it indicates a win for the player then it returns + infinity while if it doesn’t indicate a win for either then the function returns the difference between two scores.


## The GUI

The GUI is implemented using PyGame and includes the following main
Features: 
 - Board: Display the current game board and the current pieces on the board.
 - Move input: Allow human players to input their moves by clicking on the board .
 - Game status: Whose turn it is, and if the game is over.
 - Game options: Allow players to choose different game modes (e.g., human vs.
   human, human vs. computer, computer vs. computer), choose the AI player
   difficulty level (for each AI player), and start/restart a new game.

## User Manual

### Run From Source
1. Clone the repo

```bash
git clone https://github.com/Tarek-Ahmed-Helmy/Gobblet-AI-Player.git
```

2. Run the game

```bash
python main.py
```

### Run From Executable

 decompress the folder uploaded on lms and run .exe 
 


### Game Manual

1. Choose the game mode 
2. Choose the difficulty level if possible
3. There is a provided area that shows whose turn is it and both players' scores
4. The game has **Game Modes** & **Restart** buttons
5. At the game end, the winner is announced

