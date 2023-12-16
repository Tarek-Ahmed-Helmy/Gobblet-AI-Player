import pygame
from gobblet.constants import *
from gobblet.board import Board
from gobblet.gameStatus import *
#clock ticks
FPS=60

Screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Gobblet')


# Function to check if the click is within the board
def is_within_board(pos):
    x,y=pos
    return PADDING <= x < ROWS*SQUARE_SIZE+PADDING and PADDING <= y < COLUMNS*SQUARE_SIZE+PADDING


# Function to convert square coordinates to board indices
def get_row_col_from_click_onBoard(position):
    x,y = position
    # Calculate relative position within the board area (excluding padding)
    relative_x = x - PADDING
    relative_y = y - PADDING
    # Calculate row and column indices
    col = relative_x // SQUARE_SIZE
    row = (relative_y // SQUARE_SIZE)+1

    return int(row), int(col)


# Function to convert get color 
def get_color_at_position(mouse_pos):
    color=Screen.get_at(mouse_pos)
    return color

# Function to convert gobblet coordinates to board indices
def get_row_col_from_click_onGobblet(position,color):
    x,y = position
    # Calculate row and column indices
    col_temp = ((x * (WIN_LEN/250) / WIDTH)-1)
    if(color==RED):
        row = 0
    elif(color == NAVY):
        row = 5
    col = round(col_temp)
    return int(row), int(col)





def main():
    run=True
    clock=pygame.time.Clock()
    board=Board()
    board.create_board()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clicked_color = get_color_at_position(pos)

                if is_within_board(pos) and (clicked_color == RED or clicked_color == NAVY):
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
                                if not(is_within_board(posSquare)):
                                    pass
                                elif is_within_board(posSquare):
                                 # Get the square position
                                    rowS,colS=get_row_col_from_click_onBoard(posSquare)
                                    rowG,colG=get_row_col_from_click_onBoard(pos)
                                    board.put_piece(rowG,colG,rowS,colS,Screen)
                                    pygame.display.update()
                                    print(check_winner(board.board))

                elif not(is_within_board(pos)) and clicked_color == RED:
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
                                if not(is_within_board(posSquare)):
                                    pass
                                elif is_within_board(posSquare):
                                 # Get the square position
                                    rowS,colS=get_row_col_from_click_onBoard(posSquare)
                                    rowG,colG=get_row_col_from_click_onGobblet(pos,RED)
                                    board.put_piece(rowG,colG,rowS,colS,Screen)
                                    pygame.display.update()
                                    print(check_winner(board.board))

                elif not(is_within_board(pos)) and clicked_color == NAVY:
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
                                if not(is_within_board(posSquare)):
                                    pass
                                elif is_within_board(posSquare):
                                 # Get the square position
                                    rowS,colS=get_row_col_from_click_onBoard(posSquare)
                                    rowG,colG=get_row_col_from_click_onGobblet(pos,NAVY)
                                    board.put_piece(rowG,colG,rowS,colS,Screen)
                                    pygame.display.update()
                                    print(check_winner(board.board))

                else:
                    pass

        board.draw_squares(Screen)
        board.draw_pieces(Screen)
        pygame.display.update()
    pygame.quit()


main()
