import sys, pygame as pg

pg.init()

class Consumable():
    def __init__(self,rect,points):
        self.rect=rect
        self.points=points

class SnakePart():
    def __init__(self,rect):
        self.rect=rect
    def move_part(self,screen,position):
        self.rect=pg.Rect(position[0],position[1],30,30)
        pg.draw.rect(screen,(255,0,0),self.rect)
        

    
screen = pg.display.set_mode((720,720))
position = [200,50]
amount = 6
movementDict = {"w" : (0,-5),"a" : (-5,0),"s" : (0,5),"d" : (5,0)}
run = True

head= SnakePart(pg.Rect(position[0],position[1],30,30)) 
body= SnakePart(pg.Rect(position[0]-30,position[1],30,30))
body1= SnakePart(pg.Rect(position[0]-60,position[1],30,30))
body2= SnakePart(pg.Rect(position[0]-90,position[1],30,30))
tail= SnakePart(pg.Rect(position[0]-120,position[1],30,30))

consum1=Consumable(pg.Rect(290,50,30,30),1)
drawConsum=True
prevPositions=[]

snake=[head,body,body1,body2,tail]
canMove=False

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT: sys - exit()
        """Obtener Input"""
        if event.type == pg.KEYDOWN:
            try:
                key = chr(event.key)                            
                if key in movementDict.keys():
                    position[0] = head.rect.left + movementDict[key][0] * amount
                    position[1] = head.rect.top + movementDict[key][1] * amount                    
                    canMove=True
                    prevPositions.clear()            
                    prevPositions.append(position)
                    testRect=pg.Rect(position[0],position[1],30,30)
                    """Si toca un consumable, añade 1 pieza a la serpiente. Cambiarlo para que la cantidad de piezas añadidas dependa del atributo points de la clase Consumable"""
                    if drawConsum:
                        if testRect.colliderect(consum1.rect):                      
                            newPart= SnakePart(pg.Rect(body.rect.left,body.rect.top,30,30))
                            snake.append(newPart)
                            drawConsum=False
                            
                    snakeAux=snake[:len(snake)] #todos los elementos menos el último
                    for part in snakeAux:
                        """Malo de narices pero no he encontrado forma de chequear si puede hacer un solo heck de 'si hay un objeto x en esta posicion', tengo que hacerlo en un for
                        y ya que está este aquí obligatorio, al menos aprovecho este en vez de crear otro."""
                        if testRect.colliderect(part.rect): 
                            canMove=False     
                            break
                        prevPositions.append([part.rect.left,part.rect.top])
                    
            except ValueError:
                print('input no valido') #por ahora esto se queda como try catch para no dar error. hay que incluir soporte para las flechas, que no tienen chr
    """prevPositions es una lista que guarda la NUEVA posición a la que deberán moverse todas las partes, la cual es la que ocupaba la anterior antes excepto head, que tomará
    de nueva posición el input. Importante separar el obtener las posiciones del renderizado."""

    """Renderizado"""
    screen.fill((0,0,0))
    count = 0
    if drawConsum:
        pg.draw.rect(screen,(0,0,255),consum1.rect)
    if canMove:        
        for part in snake:
            part.move_part(screen,prevPositions[count])
            count+=1                   
    else:
        for part in snake:
            pg.draw.rect(screen,(255,0,0),part.rect)
        
    
    pg.display.flip()