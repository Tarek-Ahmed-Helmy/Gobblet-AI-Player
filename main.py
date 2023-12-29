import pygame
from gobblet.constants import *
from gobblet.game import Game
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
    
    game=Game(Screen)
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clicked_color = get_color_at_position(pos)
                
                game.movePiece(pos,clicked_color,Screen)

        game.updateScreen(Screen)

        
    pygame.quit()


main()
