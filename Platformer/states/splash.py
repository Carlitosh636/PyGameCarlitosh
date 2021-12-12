import pygame
from .base import BaseState

class Splash(BaseState):
    def __init__(self):
        super(Splash,self).__init__()
        self.title = self.font.render("Amazing platformer",True,pygame.Color("green"))
        self.title_rect = self.title.get_rect(center = self.screen_rect.center) #centrar el titulo en la pantalla
        self.next_state = "MENU"
        self.time_active = 0 #tiempo que aparece
    
    def update(self,dt):
        self.time_active+=dt
        if self.time_active >= 2500:
            self.done= True #si pasa un valor determinado de tiempo, pasa al siguiente.
    
    def draw(self,surface):
        surface.fill(pygame.Color("black"))
        surface.blit(self.title,self.title_rect)