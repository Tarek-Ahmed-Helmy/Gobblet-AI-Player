import pygame
from .constants import *
from .board import Board
from .gameStatus import *
from .button import Button

class Game:
    def __init__(self,Screen) -> None:
        self.turn=NAVY
        self.board=Board()
        self.board.create_board()
        self.Screen=Screen
        self.winner=None
        self.cur_score = 0, 0
        self.status = "running"
        self.restart_button=None
    
    def insert_text(self, text, font_size, text_color):
        font = pygame.font.Font(None, font_size)  # You can also specify a font file if you have one
        text_surface = font.render(text, True, text_color)
        
        return text_surface
        
        
    def updateScreen(self,Screen):
        pygame.font.init()
        score1 = self.insert_text(f"RED: {self.cur_score[1]}", 36, (0, 0, 0))
        score2 = self.insert_text('-'*10, 36, (0, 0, 0))
        score3 = self.insert_text(f"NAVY: {self.cur_score[0]}", 36, (0, 0, 0))
        player_turn1 = self.insert_text("Player Turn", 36, (0, 0, 0))
        if self.turn == RED:
            player_turn2 = self.insert_text("RED", 36, self.turn)
        else:
            player_turn2 = self.insert_text("NAVY", 36, self.turn)
        self.restart_button = Button(2, 25, 100, 40, RED, "Restart", Screen)
        self.board.draw_squares(Screen)
        self.board.draw_pieces(Screen)
        Screen.blit(score1, (20, WIDTH/(WIN_LEN/362.5)))
        Screen.blit(score2, (20, WIDTH/(WIN_LEN/487.5)))
        Screen.blit(score3, (20, WIDTH/(WIN_LEN/612.5)))
        Screen.blit(player_turn1, (650, WIDTH/(WIN_LEN/425)))
        Screen.blit(player_turn2, (680, WIDTH/(WIN_LEN/487.5)))
        self.restart_button.draw()
        pygame.display.update()
    
    def get_square_position(self,pos ,posSquare, color):
        if color != None:
            rowG,colG=self.get_row_col_from_click_onGobblet(pos,color)
        else:
            rowG,colG=self.get_row_col_from_click_onBoard(pos)

        rowS,colS=self.get_row_col_from_click_onBoard(posSquare)
        return rowG, colG, rowS, colS

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
    
    def change_turn(self):
        if self.turn == NAVY:
            self.turn = RED
        else:
            self.turn = NAVY

    def set_winner(self):
        winner = check_winner(self.board.board)
        if winner == (43, 42, 76):
            self.winner = "NAVY wins"
        elif winner == (179, 19, 18):
            self.winner = "RED wins"

    def move(self, Screen, pos, color):
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
                        rowG, colG, rowS, colS = self.get_square_position(pos, posSquare, color)
                        if(color == None):
                            is_moved = self.board.put_piece(rowG,colG,rowS,colS,Screen)
                            if is_moved:
                                self.set_winner()
                            self.change_turn()
                        else:
                            if can_play(self.board.board, rowS, colS, color):
                                is_moved = self.board.put_piece(rowG,colG,rowS,colS,Screen)
                                if is_moved:
                                    self.set_winner()
                                    self.change_turn()
                            else:
                                print("Cannot Play")

    def movePiece(self, pos, clicked_color, Screen):
        if self.turn != clicked_color:
            return
        if self.is_within_board(pos) and (clicked_color == RED or clicked_color == NAVY):
            self.move( Screen, pos, None)    

        elif not(self.is_within_board(pos)) and clicked_color == RED:
            self.move( Screen, pos, RED)
            
        elif not(self.is_within_board(pos)) and clicked_color == NAVY:
            self.move( Screen, pos, NAVY)
            
        else:
            pass
        

    def computer_move(self):
        self.set_winner()
        self.change_turn()