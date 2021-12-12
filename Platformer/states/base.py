import pygame

class BaseState(object):
    def __init__(self):
        self.done = False
        self.quit = False
        self.next_state = None #cada estado sabrá cual es el siguiente
        self.screen_rect = pygame.display.get_surface().get_rect()
        self.persistData = {}
        self.font = pygame.font.SysFont('Verdana',20)
    
    def startup(self,persistent):
        self.persistData = persistent
    #las funciones de abajo se implementan en cada clase hija
    def get_event(self,event):
        pass
    def update(self,dt):
        pass
    def draw(self,surface):
        pass