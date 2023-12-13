import pygame
import sys
pygame.init()
def calculate_percentage_resolution(percentage_width, percentage_height):
    screen_info = pygame.display.Info()
    target_width = int(screen_info.current_w * (percentage_width))
    target_height = int(screen_info.current_h * (percentage_height))
    return (target_width, target_height)
# Dimensions 
WIDTH, HEIGHT = calculate_percentage_resolution(1000/1920,1000/1080)
print(WIDTH, HEIGHT)
ROWS=4
COLUMNS=4
SQUARE_SIZE = WIDTH/(1000/130)
PADDING= WIDTH/(1000/240) 

# colors
WHITE=(255,255,255)
BLACK=(0,0,0)
BROWN=(200,150,130)
GREY=(200,200,200)
BLUE = (0, 0, 255)
RED = (255, 0, 0)


#size of pieces
SIZE1= WIDTH/(1000/15)
SIZE2= WIDTH/(1000/30)
SIZE3= WIDTH/(1000/45)
SIZE4= WIDTH/(1000/60)


