from .constants import * 

class Piece:
    def __init__(self,x,y,color,size):
        self.x = x
        self.y = y
        self.size = size
        self.color = color


    def calc_pos(self):
        pass


    def draw(self,screen):
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.size)
