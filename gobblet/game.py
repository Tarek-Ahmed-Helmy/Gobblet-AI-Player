import pygame
from .constants import *
from .board import Board
from .gameStatus import *

class Game:
    def __init__(self,Screen) -> None:
        self.turn=NAVY  
        self.board=Board()
        self.board.create_board()
        self.Screen=Screen

    def updateScreen(self,Screen):
        self.board.draw_squares(Screen)
        self.board.draw_pieces(Screen)
        pygame.display.update()
    

    # Function to check if the click is within the board
    def is_within_board(self,pos):
        x,y=pos
        return PADDING <= x < ROWS*SQUARE_SIZE+PADDING and PADDING <= y < COLUMNS*SQUARE_SIZE+PADDING

    # Function to convert square coordinates to board indices
    def get_row_col_from_click_onBoard(self,position):
        x,y = position
        # Calculate relative position within the board area (excluding padding)
        relative_x = x - PADDING
        relative_y = y - PADDING
        # Calculate row and column indices
        col = relative_x // SQUARE_SIZE
        row = (relative_y // SQUARE_SIZE)+1
        return int(row), int(col)

    # Function to convert gobblet coordinates to board indices
    def get_row_col_from_click_onGobblet(self,position,color):
        x,y = position
        # Calculate row and column indices
        col_temp = ((x * (WIN_LEN/250) / WIDTH)-1)
        if(color==RED):
            row = 0
        elif(color == NAVY):
            row = 5
        col = round(col_temp)
        return int(row), int(col)

    def movePiece(self,pos,clicked_color,Screen):
        if self.is_within_board(pos) and (clicked_color == RED or clicked_color == NAVY):
                    # Wait for the second click
                    second_click = False
                    while not second_click:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                run=False
                            elif event.type == pygame.MOUSEBUTTONDOWN :
                                second_click=True
                                posSquare = pygame.mouse.get_pos()
                                if not(self.self.is_within_board(posSquare)):
                                    pass
                                elif self.self.is_within_board(posSquare):
                                # Get the square position
                                    rowS,colS=self.get_row_col_from_click_onBoard(posSquare)
                                    rowG,colG=self.get_row_col_from_click_onBoard(pos)
                                    self.board.put_piece(rowG,colG,rowS,colS,Screen)
                                    pygame.display.update()
                                    print(check_winner(self.board))

        elif not(self.is_within_board(pos)) and clicked_color == RED:
                    # Wait for the second click
                    second_click = False
                    while not second_click:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                run=False
                            elif event.type == pygame.MOUSEBUTTONDOWN :
                                second_click=True
                                posSquare = pygame.mouse.get_pos()
                                if not(self.is_within_board(posSquare)):
                                    pass
                                elif self.is_within_board(posSquare):
                                # Get the square position
                                    rowS,colS=self.get_row_col_from_click_onBoard(posSquare)
                                    rowG,colG=self.get_row_col_from_click_onGobblet(pos,RED)
                                    if can_play(self.board, rowS, colS, RED):
                                        self.board.put_piece(rowG,colG,rowS,colS,Screen)
                                        pygame.display.update()
                                        print(check_winner(self.board))
                                    else:
                                        print("Cannot Play")

        elif not(self.is_within_board(pos)) and clicked_color == NAVY:
            # Wait for the second click
            second_click = False
            while not second_click:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        run=False
                    elif event.type == pygame.MOUSEBUTTONDOWN :
                        second_click=True
                        posSquare = pygame.mouse.get_pos()
                        if not(self.is_within_board(posSquare)):
                            pass
                        elif self.is_within_board(posSquare):
                            # Get the square position
                            rowS,colS=self.get_row_col_from_click_onBoard(posSquare)
                            rowG,colG=self.get_row_col_from_click_onGobblet(pos,NAVY)
                            if can_play(self.board, rowS, colS,NAVY):
                                self.board.put_piece(rowG,colG,rowS,colS,Screen)
                                pygame.display.update()
                                print(check_winner(self.board))
                            else:
                                print("Cannot Play")
        else:
            pass
        