import pygame, sys
from Dibujos import *
pygame.init()

#Fondo imagen
background = pygame.image.load("memorizan2.png").convert()

#Ventana y para cerrar
size = (1000,700)
screen = pygame.display.set_mode(size)
while True:                                                     #Bucle para cerrar
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    dibujo = Dibujo(screen)                                     
    dibujo.dibujar_rectangulos()                                #llama a la clase que crea los cuadrados de fondo
    screen.blit(background, [250,100])                          #para mostrar la imagen         
    pygame.display.set_caption("Memoriza2")                     #Para mostrar nombre del juego 
    pygame.display.flip()                                       #Para actualizar la pantalla
