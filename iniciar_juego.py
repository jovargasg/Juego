import pygame, random

class Cuadro:
    def __init__(self, fuente_imagen):
        self.mostrar = True
        self.descubierto = False
        self.fuente_imagen = fuente_imagen
        self.imagen_real = pygame.image.load(fuente_imagen)

cuadros = [
    [Cuadro("carta 10.png"),Cuadro("carta 10.png"),
    Cuadro("carta 10.png"),Cuadro("carta 10.png")],
]

def ocular_cuadros():
    for fila in cuadros:
        for cuadro in fila:
            cuadro.mostrar = False
            cuadro.descubierto = False

def randomizar():
    cantidad_filas = len(cuadros)
    cantidad_columnas = len(cuadros[0])
    for y in range(cantidad_filas):
        for x in range(cantidad_columnas):
            x_aleatorio = random.randint(0, cantidad_columnas -1)
            y_aleatorio = random.randint(0, cantidad_filas -1)
            Cuadro_temporal = cuadros[y][x]
            cuadros[y][x] = cuadros[y_aleatorio][x_aleatorio]
            cuadros[y_aleatorio][x_aleatorio] = Cuadro_temporal

def determinar_si_gana():
    if gana():
        #musica de ganador
        reinicio()

def gana():
    for fila in cuadros:
        for cuadro in fila:
            if not cuadro.descubierto:
                return False
    return True

def reinicio():
    global juego_iniciado
    juego_iniciado = False

def iniciar_juego():
    #juego de empezar
    global juego_iniciado
    for i in range(3):
        randomizar()
    ocular_cuadros()
    juego_iniciado = True
