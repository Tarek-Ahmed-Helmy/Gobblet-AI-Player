from copy import deepcopy
import random
import pygame
from .constants import *
from .piece import Piece
from .stack import Stack
from .gameStatus import *

class Board:
    def __init__(self):
        self.board = []

    def draw_squares(self,screen):
        screen.fill(GREY)
        for row in range(ROWS):
            for col in range(COLUMNS):
                pygame.draw.rect(screen, ORANGE,(row*SQUARE_SIZE+PADDING,col*SQUARE_SIZE+PADDING,SQUARE_SIZE,SQUARE_SIZE))
                pygame.draw.rect(screen, BLACK,(row*SQUARE_SIZE+PADDING, col*SQUARE_SIZE+PADDING,SQUARE_SIZE,SQUARE_SIZE),1)

    def draw_pieces(self,screen):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j].isEmpty() == False:
                    self.board[i][j].peek().draw(screen)

    # still no Need
    def identify_empty_squares(self):
        empty_squares = []
        for row_idx, row in enumerate(self.board):
            for col_idx, col in enumerate(row):
                if col.isEmpty():
                    empty_squares.append((row_idx, col_idx))
        return empty_squares

    # gobblet is the start, screen is the destination
    def put_piece(self,rowG,colG,rowS,colS,screen):
        if not(self.board[rowG][colG].isEmpty()):
            if self.board[rowS][colS].isEmpty() or self.board[rowG][colG].peek().size > self.board[rowS][colS].peek().size:
                piece = self.board[rowG][colG].pop()
                piece.x = colS * SQUARE_SIZE + PADDING + SQUARE_SIZE // 2
                piece.y = (rowS-1) * SQUARE_SIZE + PADDING + SQUARE_SIZE // 2
                self.board[rowS][colS].push(piece)
                self.draw_pieces(screen)
                return True
        return False

    def create_board(self):
        gobblet_sizes=[SIZE1, SIZE2, SIZE3, SIZE4]
        stack1 = Stack()
        stack2 = Stack()
        stack3 = Stack()
        stack4 = Stack()
        stack5 = Stack()
        stack6 = Stack()
        player1 = [stack1, stack2, stack3]
        player2 = [stack4, stack5, stack6]
        self.board.append(player2)
        self.board.append([Stack(), Stack(), Stack(), Stack()])
        self.board.append([Stack(), Stack(), Stack(), Stack()])
        self.board.append([Stack(), Stack(), Stack(), Stack()])
        self.board.append([Stack(), Stack(), Stack(), Stack()])
        self.board.append(player1)

        for i in range(len(player2)):
            for size in gobblet_sizes:
                player2[i].push(Piece((i+1)*WIDTH/(WIN_LEN/250),HEIGHT/(WIN_LEN/100),RED,size))

        for i in range(len(player1)):
            for size in gobblet_sizes:
                player1[i].push(Piece((i+1)*WIDTH/(WIN_LEN/250),HEIGHT/(WIN_LEN/900),NAVY,size))


    def get_all_pieces(self, color):
        pieces = []
        for row, list in enumerate(self.board):
            for col, item in enumerate(list):
                if not item.isEmpty() and item.peek().color == color:
                    pieces.append([row, col, item.peek()])

        return pieces
    

    def get_valid_moves(self, piece):
        valid_moves = []
        board = self.board[1:5]
        if piece[0] in [0,5]:
            for row, list in enumerate(board):
                for col, item in enumerate(list):
                    if item.isEmpty():
                        valid_moves.append([row+1, col])
                    else:
                        if can_play(self.board, row+1, col, piece[2].color):
                            if piece[2].size > item.peek().size:
                                valid_moves.append([row+1, col])
        else:
            for row, list in enumerate(board):
                for col, item in enumerate(list):
                    if item.isEmpty() or piece[2].size > item.peek().size:
                        valid_moves.append([row+1, col])

        return valid_moves

    # we need to implement evaluate function not rand
    def evaluate(self):
        board = self.board[1:5]
        Navy = 0
        Red = 0
        NavyNum = 0
        RedNum = 0
        for row in board:
            for col in row:
                if not (col.isEmpty()) and col.peek().color == NAVY:
                    Navy += col.peek().size / 12;
                    NavyNum += 1
                elif not (col.isEmpty()) and col.peek().color == RED:
                    Red += col.peek().size / 12;
                    RedNum += 1
            if NavyNum > 0 and RedNum == 0:
                Navy *= NavyNum
            elif RedNum > 0 and NavyNum == 0:
                Red *= RedNum
            elif NavyNum > 0 and RedNum > 0:
                Navy -= NavyNum
                Red -= RedNum
            NavyNum = 0
            RedNum = 0
        for col in range(len(self.board[1])):
            columnArray = [self.board[row][col] for row in range(1,5)]
            for row in columnArray:
                if not (row.isEmpty()) and row.peek().color == NAVY:
                    Navy += row.peek().size / 12;
                    Red -= row.peek().size / 12;
                    NavyNum += 1;
                elif not (row.isEmpty()) and row.peek().color == RED:
                    Red += row.peek().size / 12;
                    Navy -= row.peek().size / 12;
                    RedNum += 1;
            if NavyNum > 0 and RedNum == 0:
                Navy *= NavyNum
            elif RedNum > 0 and NavyNum == 0:
                Red *= RedNum
            elif NavyNum > 0 and RedNum > 0:
                Navy -= NavyNum
                Red -= RedNum
            NavyNum = 0
            RedNum = 0
        if check_winner(self.board) == RED:
            return 80
        elif check_winner(self.board) == NAVY:
            return -80
        else:
            return Red - Navy
    def print_board(self):
        printed_board = deepcopy(self.board)
        for row, list in enumerate(printed_board):
            for col, item in enumerate(list):
                if not item.isEmpty():
                    printed_board[row][col] = item.peek().color, item.peek().size
                else:
                    printed_board[row][col] = 0

            print(printed_board[row])