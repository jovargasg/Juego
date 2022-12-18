import pygame, sys, math, random, time
from Dibujos import *
from boton_inicio import *
from iniciar_juego import *
pygame.init()                           #Para iniciar pygame
pygame.font.init()                      #Para iniciar las fuentes con pygame
pygame.mixer.init()                     #Para iniciar los sonidos con pygame
puede_jugar = True
inicio_juego = False


background = pygame.image.load("memorizan2.png").convert()
inicio = pygame.draw.rect(screen, RED, (310, 510, 390, 65))


size = (1000,700)
screen = pygame.display.set_mode(size)
fuente = pygame.font.Font(None, 48)
texto = fuente.render("Empezar juego",1, (0,0,0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and puede_jugar:             #Detecta el click sobre el boton para iniciar el juego
            xinicio ,yinicio = event.pos
            if inicio.collidepoint(event.pos):
                if not juego_iniciado:
                    iniciar_juego()
            else:
                if not juego_iniciado:
                    continue
    
    #mouse_pos = pygame.mouse.get_pos()                        #Para ver la posicion del mouse
    #print(mouse_pos)                                          #Para que imprima la posicion del mouse

    dibujo = Dibujo(screen)
    dibujo.dibujar_rectangulos()                                #llama a la clase que crea los cuadrados de fondo
    screen.blit(background, [250,100])                          #para mostrar la imagen      
    pygame.display.set_caption("Memoriza2")                     #Para mostrar nombre del juego
    boton = Boton_inicio(screen)
    boton.dibujar_boton()
    screen.blit(texto,(390,530))
    pygame.display.flip()                                       #Para actualizar la pantalla 
