import pygame
from .constants import *
class Button:
    def __init__(self, x, y, width, height, color, text, Screen):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.Screen = Screen

    def draw(self):
        pygame.draw.rect(self.Screen, self.color, self.rect)
        font = pygame.font.Font(None, 27)
        text = font.render(self.text, True, WHITE)
        text_rect = text.get_rect(center=self.rect.center)
        self.Screen.blit(text, text_rect)