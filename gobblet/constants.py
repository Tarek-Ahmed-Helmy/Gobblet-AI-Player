import pygame

pygame.init()

def calculate_percentage_resolution(percentage_width, percentage_height):
    screen_info = pygame.display.Info()
    target_width = int(screen_info.current_w * (percentage_width))
    target_height = int(screen_info.current_h * (percentage_height))
    return (target_width, target_height)

# Dimensions
WIN_LEN = 1000
WIDTH, HEIGHT = calculate_percentage_resolution(WIN_LEN/1920,WIN_LEN/1080)
ROWS = 4
COLUMNS = 4
SQUARE_SIZE = WIDTH/(WIN_LEN/130)
PADDING = WIDTH/(WIN_LEN/240) 

# colors
WHITE = (255,255,255)
BLACK = (0,0,0)
ORANGE = (234,144,108)
GREY = (238,226,222)
NAVY = (43,42,76)
RED = (179,19,18)

#size of pieces
SIZE1 = WIDTH/(WIN_LEN/15)
SIZE2 = WIDTH/(WIN_LEN/30)
SIZE3 = WIDTH/(WIN_LEN/45)
SIZE4 = WIDTH/(WIN_LEN/60)