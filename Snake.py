import sys, random, pygame as pg

pg.init()

"""TO DO: Consumable que aumenta la puntuación de los azules, tener varios azules (opcional) y sonidos para la serpiente y consumables"""
class Entity():
    def __init__(self, rect) -> None:
        self.rect = rect

    def move_entity(self, screen, position, color):
        self.rect = pg.Rect(position[0], position[1], 25, 25)
        pg.draw.rect(screen, color, self.rect)


class Consumable(Entity):
    def __init__(self, rect, points):
        self.rect = rect
        self.points = points
    def consumableEffect(self,list,body):
        newPart = SnakePart(pg.Rect(body.rect.left, body.rect.top, 25, 25))
        list.append(newPart)


class SnakePart(Entity):
    def __init__(self, rect):
        super().__init__(rect)


class Wall(Entity):
    def __init__(self, rect):
        super().__init__(rect)

def calculate_pos_consum():
    x = random.randint(-15, 15) * 25
    y = random.randint(-15, 15) * 25
    """se sale algunas veces y por consecuencia aparece demasiado en el borde. Probar las tecnicas de try catch que vienen en las diapos de clase a ver si es mejor."""
    if x < 0:
        x = 25
    if x > 720:
        x = 720
    if y < 0:
        y = 25
    if y > 720:
        y = 720
    return [x, y]

RED = (255, 0, 0)
GREY = (128, 128, 128)
BLUE = (0, 0, 255)
screen = pg.display.set_mode((800, 800))
import sys, random, pygame as pg

pg.init()

"""TO DO: Consumable que aumenta la puntuación de los azules, tener varios azules (opcional) y sonidos para la serpiente y consumables"""


class Entity():
    def __init__(self, rect) -> None:
        self.rect = rect

    def move_entity(self, screen, position, color):
        self.rect = pg.Rect(position[0], position[1], 25, 25)
        pg.draw.rect(screen, color, self.rect)


class Consumable(Entity):
    def __init__(self, rect, points):
        self.rect = rect
        self.points = points

    def consumableEffect(self, list, body):
        newPart = SnakePart(pg.Rect(body.rect.left, body.rect.top, 25, 25))
        list.append(newPart)


class SnakePart(Entity):
    def __init__(self, rect):
        super().__init__(rect)


class Wall(Entity):
    def __init__(self, rect):
        super().__init__(rect)


def calculate_pos_consum():
    x = random.randint(-15, 15) * 25
    y = random.randint(-15, 15) * 25
    """se sale algunas veces y por consecuencia aparece demasiado en el borde. Probar las tecnicas de try catch que vienen en las diapos de clase a ver si es mejor."""
    if x < 0:
        x = 25
    if x > 720:
        x = 720
    if y < 0:
        y = 25
    if y > 720:
        y = 720
    return [x, y]


RED = (255, 0, 0)
GREY = (128, 128, 128)
BLUE = (0, 0, 255)
screen = pg.display.set_mode((745, 745)) #(anchura,altura)
position = [200, 50]
amount = 5
movementDict = {"w": (0, -5), "a": (-5, 0), "s": (0, 5), "d": (5, 0)}
run = True
'''posicion x, posicion y,anchura, altura'''
head = SnakePart(pg.Rect(position[0], position[1], 25, 25))
body = SnakePart(pg.Rect(position[0] - 25, position[1], 25, 25))
body1 = SnakePart(pg.Rect(position[0] - 50, position[1], 25, 25))
body2 = SnakePart(pg.Rect(position[0] - 75, position[1], 25, 25))
tail = SnakePart(pg.Rect(position[0] - 100, position[1], 25, 25))

wall1 = Wall(pg.Rect(0, 0, 720, 25))
wall2 = Wall(pg.Rect(0, 0, 25, 720))
wall3 = Wall(pg.Rect(0, 700, 720, 25))
wall4 = Wall(pg.Rect(720, 0, 25, 720))
walls = [wall1, wall2, wall3, wall4]
consum1Position = [225, 100]
consum1 = Consumable(pg.Rect(consum1Position[0], consum1Position[1], 25, 25), 1)
consum2 = Consumable(pg.Rect(consum1Position[0] + 120, consum1Position[1] + 60, 25, 25), 1)
consumables = [consum1, consum2]
"""Añadir un consumable verde que suba el valor del consumable azul por 2"""

prevPositions = []

snake = [head, body, body1, body2, tail]
canMove = False


def calculate_pos_consum():
    x = random.randint(-15, 15) * 25
    y = random.randint(-15, 15) * 25
    """se sale algunas veces y por consecuencia aparece demasiado en el borde. 
    Probar las tecnicas de try catch que vienen en las diapos de clase a ver si es mejor."""
    if x < 0:
        x = 25
    if x > 720:
        x = 720
    if y < 0:
        y = 25
    if y > 720:
        y = 720
    return [x, y]


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
                    canMove = True
                    prevPositions.clear()
                    prevPositions.append(position)
                    testRect = pg.Rect(position[0], position[1], 25, 25)
                    """Si toca un consumable, añade 1 pieza a la serpiente. Cambiarlo para que la cantidad de piezas añadidas dependa del atributo points de la clase Consumable"""
                    collidedConsum = testRect.collidelist(consumables)
                    if collidedConsum != -1:
                        consumables[collidedConsum].consumableEffect(snake, body)
                        consum1Position = calculate_pos_consum()
                        consumables[collidedConsum].rect.left = consum1Position[
                            0]  # cambia la pos del consumable tomado
                        consumables[collidedConsum].rect.top = consum1Position[1]

                    if testRect.colliderect(consum1.rect):
                        newPart = SnakePart(pg.Rect(body.rect.left, body.rect.top, 25, 25))
                        snake.append(newPart)
                        consum1Position = calculate_pos_consum()

                    """Mirar que no choque consigo mismo. Collidelist devuelve el index del objeto tocado."""
                    if testRect.collidelist(snake) != -1:
                        canMove = False
                        break

                    snakeAux = snake[:len(snake)]  # todos los elementos menos el último
                    for part in snakeAux:
                        prevPositions.append([part.rect.left, part.rect.top])

            except ValueError:
                print(
                    'input no valido')  # por ahora esto se queda como try catch para no dar error. hay que incluir soporte para las flechas, que no tienen chr
    """prevPositions es una lista que guarda la NUEVA posición a la que deberán moverse todas las partes, la cual es la que ocupaba la anterior antes excepto head, que tomará
    de nueva posición el input. Importante separar el obtener las posiciones del renderizado."""

    """Renderizado donde se dibuja"""
    screen.fill((0, 0, 0))
    count = 0
    for consum in consumables:
        consum.move_entity(screen, consum.rect, BLUE)

    if canMove:
        for part in snake:
            part.move_entity(screen, prevPositions[count], RED)
            count += 1
    else:
        for part in snake:
            pg.draw.rect(screen, RED, part.rect)
    for wall in walls:
        pg.draw.rect(screen, GREY, wall.rect)
    pg.display.flip()
