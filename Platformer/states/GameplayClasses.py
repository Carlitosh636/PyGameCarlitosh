import pygame as pg
import random
from pygame.constants import K_LEFT, K_RIGHT

ACC=0.75 #aceleración
FRIC=-0.12 #fricción para que el personaje tenga ímpetu
JUMPDIST = 15 #longitud de salto
FPS = 60
MAXPLATFORMS= 6
WIDTH = 480
HEIGHT = 720
VEC = pg.math.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.surf=pg.image.load("Intro_ball.gif")
        self.surf = pg.transform.scale(self.surf,(64,64)) #cambiar el tamaño
        self.rect = self.surf.get_rect() 
        self.flipImage=False
        self.pos=VEC((100,360))
        self.vel=VEC(0,0)
        self.acc=VEC(0,0)
        self.jumping = False
        self.score = 0
    def move(self,accVal,flip):
        self.acc=VEC(0,0.5) #el 0.5 añade gravedad constante
        #keys=pg.key.get_pressed() #teclas pulsadas. Contiene todas las teclas de PyGame y por cada una un valor booleano. True si se ha pulsado, False si no

        #obtener aceleración y/o saltar
        self.acc.x= ACC * accVal
        self.flipImage=flip
        #moverse
        self.acc.x += self.vel.x * FRIC #esto es lo que permite que el personaje vaya perdiendo movimiento con el tiempo si no se pulsa
        self.vel += self.acc #añadir aceleramiento a la vel
        self.pos += self.vel + 0.5 * self.acc #ecuación de aceleración. 

        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        #update
        self.rect.midbottom=self.pos
    
    def jump(self,platforms):
        hits = pg.sprite.spritecollide(self, platforms, False)
        if hits and not self.jumping: # si estoy en una plataforma y NO estoy saltando
            self.jumping= True
            self.vel.y = -17
            
    """def cancel_jump(self): #debido a que en PyGame podemos detectar cuando se suelta una tecla, podemos hacer un salto controlado donde "perdemos" momento
        if self.jumping:
            if self.vel.y < -3:
                self.vel.y = -3"""
    
 
    def update(self,platforms):
        hits = pg.sprite.spritecollide(self ,platforms, False) #devuelve el objeto con el que se ha colisionado. None en caso de no haber colisionado
        if self.vel.y > 0:        
            if hits:
                if self.pos.y < hits[0].rect.bottom: #este if se asegura de que solo se detenga en la plataforma cuando se "posa" sobre ella. sin el, una vez la bola toque la plataforma por abajo se teleporta
                    self.pos.y = hits[0].rect.top +1
                    self.vel.y = 0
                    self.jumping = False
                    self.pos.x+=hits[0].speed #hace que la bola se mueva junto a la plataforma cuando esté quieta
                    if hits[0].point == True:
                        hits[0].point = False
                        self.score +=1
            

class Platform(pg.sprite.Sprite):
    def __init__(self,vel):
        super().__init__()
        self.surf= pg.image.load("ground.png")
        self.surf = pg.transform.scale(self.surf,(180,32))
        self.rect = self.surf.get_rect(center = (random.randint(0,WIDTH-10),random.randint(0, WIDTH-30))) #crear plataforma en pos random, entre 0 (el top) y el máximo (con un margen)
        self.moving = True
        self.speed= vel*random.randint(-1,1) #puede moverse a la izquierda, a la derecha o no moverse (el 0)
        self.point =  True #para asegurarse de que no se pueden "duplicar" puntos
    def move(self):
        if self.moving:
            self.rect.move_ip(self.speed,0)
            if self.speed > 0: #si toca un borde, que se transporte al otro lado
                if self.rect.left > WIDTH:
                    self.rect.right=0
                if self.rect.right < 0:
                    self.rect.left=WIDTH
                