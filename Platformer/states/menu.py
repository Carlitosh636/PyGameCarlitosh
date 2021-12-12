import pygame
from .base import BaseState

class Menu(BaseState):
    def __init__(self):
        super(Menu,self).__init__()
        self.instructions = self.font.render("Empezar = SPACE \n Salir = Q",True,pygame.Color("white"))
        self.instructions_rect = self.instructions.get_rect(center=self.screen_rect.center)
        self.next_state= "GAMEPLAY"

    
    
    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit=True
        elif event.type ==pygame.KEYUP: #manejamos el menu con teclado
            if event.key == pygame.K_SPACE:
                self.done = True
            elif event.key == pygame.K_q:
                self.quit = True
                
    def draw(self, surface):
        surface.fill(pygame.Color("black"))
        surface.blit(self.instructions,self.instructions_rect)