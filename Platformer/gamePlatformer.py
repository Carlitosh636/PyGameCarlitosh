import pygame

class Game(object):
    def __init__(self,screen,states,iniState):
        self.done = False #ha terminado el juego?
        self.screen = screen
        self.states= states
        self.state_name = iniState
        self.clock = pygame.time.Clock()
        self.fps = 60 #caparemos a 60 fps
        self.state= self.states[self.state_name] #objeto del estado inicial
    
    def event_loop(self): #para manejar eventos en el estado actual
        for event in pygame.event.get():
            self.state.get_event(event)
    
    def flip_state(self): #cambiar de estado
        current_state= self.state_name
        next_state = self.state.next_state
        self.state.done=False
        self.state_name=next_state
        persistentData = self.state.persistData #datos que se pasan entre estados
        self.state = self.states[self.state_name]
        self.state.startup(persistentData) #comienza el nuevo estado con los datos persistentes.
    
    def update(self,dt): # comprobar si el juego debería finalizar o cambiar.
        if self.state.quit:
            self.done=True
        elif self.state.done:
            self.flip_state()
        self.state.update(dt)

    def draw(self): #renderizado
        self.state.draw(self.screen)

    def run(self): #loop principal
        while not self.done:
            dt = self.clock.tick(self.fps)
            self.event_loop()
            self.update(dt)
            self.draw() #por cada frame recoge los eventos, chequea si se ha terminado y renderiza los sprites.
            pygame.display.update()
