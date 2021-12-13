import pygame
from .base import BaseState

class Menu(BaseState):
    def __init__(self):
        super(Menu,self).__init__()
        text = ["Presiona 1 para dificultad facil","2 para media", "3 para dificil", "Salir = Q"]
        self.instructions = []
        self.instructions_rects = []
        for line in text:
            self.instructions.append(self.font.render(line,True,pygame.Color("white")))      
        self.next_state= "GAMEPLAY"

    
    
    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit=True
        elif event.type ==pygame.KEYUP: #manejamos el menu con teclado
            if event.key == pygame.K_q:              
                self.quit = True
            elif event.key == pygame.K_1:
                self.persistData = 1
                self.done = True
            elif event.key == pygame.K_2:
                self.persistData = 2
                self.done = True
            elif event.key == pygame.K_3:
                self.persistData = 3
                self.done = True
            
                
    def draw(self, surface):
        surface.fill(pygame.Color("black"))
        count=0
        for line in self.instructions:
            surface.blit(line,(100,self.screen_rect.centery+count))
            count+=30