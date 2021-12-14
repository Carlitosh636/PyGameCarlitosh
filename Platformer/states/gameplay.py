import pygame as pg
import random
from .base import BaseState
from .GameplayClasses import Player,Platform

WIDTH = 480
HEIGHT = 720
MAXPLATFORMS= 6
class Gameplay(BaseState):
    def __init__(self):
        super(Gameplay, self).__init__()
        
        self.next_state = "GAME_OVER"
        self.platSpeed = 0
        self.moveDir = 0
        self.playerFlip = False

    def check_plat_collision(self,platform,group):
        if pg.sprite.spritecollideany(platform,group): #función que nos permite ver si x sprite colisiona con alguno de los del grupo
            return True
        else:
            #return False valdría, pero sigue existiendo el problema de que quedan demasiado juntas. Para ello haremos:
            for pl in group:
                if pl ==  platform:
                    continue
                if (abs(platform.rect.top - pl.rect.bottom) < 50) and (abs(platform.rect.bottom - pl.rect.top) < 50): #si se coloca en una distancia menor a 50, se cuenta como "mala" y retorna true
                    return True
            C = False

    def platform_generation(self):
        while len(self.platforms) < MAXPLATFORMS:
            pl = Platform(self.platSpeed)
            C = True
            while C: #solo sale del while si la plataforma no choca con alguna de las existentes
                pl= Platform(self.platSpeed)
                pl.rect.center = (random.randrange(0,WIDTH-10),random.randrange(0,50))
                C = self.check_plat_collision(pl,self.platforms)
            self.platforms.add(pl)
     
    def startup(self, persistent):
        self.player = Player()
        self.platSpeed = persistent
        self.ground = Platform(self.platSpeed)
        self.player.rect = self.player.surf.get_rect(center=(WIDTH-100,HEIGHT-300))
        self.ground.surf=pg.transform.scale(self.ground.surf,(360,64))
        self.ground.rect = self.ground.surf.get_rect(center = (WIDTH/2,HEIGHT-250))
        self.ground.point= False
        self.ground.speed= 0
        self.platforms= pg.sprite.Group()
        self.platforms.add(self.ground)
        
        count = random.randint(MAXPLATFORMS-2,MAXPLATFORMS-1)

        while count > 0:
            C = True
            pl = Platform(self.platSpeed)
            while C:
                pl = Platform(self.platSpeed)
                C = self.check_plat_collision(pl,self.platforms)
            self.platforms.add(pl)
            count-=1

    def get_event(self, event):
        if event.type == pg.QUIT:
            self.quit = True
        elif event.type == pg.KEYDOWN:                     
            if event.key == pg.K_LEFT:
                self.moveDir = -1
                self.playerFlip = False
            if event.key == pg.K_RIGHT:
                self.moveDir = 1
                self.playerFlip = True
            if event.key == pg.K_SPACE:
                self.player.jump(self.platforms)
        elif event.type == pg.KEYUP:
            if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                self.moveDir = 0  

    def update(self, dt):
        if self.player.rect.top > HEIGHT:
            self.persistData = self.player.score
            self.done = True
        if self.player.rect.top <= HEIGHT / 4: # si pasa del pto determinado
            self.player.pos.y += abs(self.player.vel.y) #actualiza la pos del jugador
            for pl in self.platforms: #actualiza la pos de las plataformas (se quedan abajo ya que no se mueven, a diferencia del jugador)
                pl.rect.y += abs(self.player.vel.y)
                if pl.rect.top >= HEIGHT:
                    pl.kill() #quita las plataformas que desaparecen de la pantalla por abajo.

        self.player.move(self.moveDir,self.playerFlip)
        self.player.update(self.platforms)
        self.platform_generation()
        for platform in self.platforms:
            platform.move()
        

    def draw(self, surface):
        surface.fill(pg.Color("black")) #nota importante, hay que cambiar el bg cada vez que cambia de estado, por eso siempre ponemos esta linea
        #pg.draw.rect(surface, pg.Color("blue"), self.rect)
        surface.blit(pg.transform.flip(self.player.surf,self.player.flipImage,False),self.player.rect)
        for pl in self.platforms:
            surface.blit(pl.surf,pl.rect)
        pointsText= self.font.render(str(self.player.score),True,(0,255,255)) #el render debe estar aqui pues va a cambiar constantemente no como el otro texto
        surface.blit(pointsText,(WIDTH/2,10))