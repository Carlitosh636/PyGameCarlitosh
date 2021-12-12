import pygame


import pygame
from .base import BaseState

class GameOver(BaseState):
    def __init__(self):
        super(GameOver,self).__init__()
        self.font = pygame.font.SysFont('Comic Sans',30)
        self.text = self.font.render("Game Over!",True,pygame.Color("white"))
        self.text_Rect = self.text.get_rect(center = self.screen_rect.center)    
        self.time_active = 0 #tiempo que aparece
    
    def update(self,dt):
        self.time_active+=dt
        if self.time_active >= 2500:
            self.quit= True
    
    def draw(self,surface):
        surface.fill(pygame.Color("red"))
        surface.blit(self.text,self.text_Rect)