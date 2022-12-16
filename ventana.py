import pygame, sys                                              #Importar librerias
from Dibujos import *                                           #Importar la clase Dibujos para los cuadros de fondo de diseño
pygame.init()                                                   #Iniciar pygame

background = pygame.image.load("memorizan2.png").convert()      #Imagen sobre puesta

size = (1000,700)                                               #Definir tamaño de la ventana
screen = pygame.display.set_mode(size)                          #
while True:                                                     #Bucle para cerrar la ventana
    for event in pygame.event.get():                            #Evento de pygame
        if event.type == pygame.QUIT:                           #Si el evento es apretar la "x" de la ventana,
            sys.exit()                                          #Esta ventana se cierra

    dibujo = Dibujo(screen)                                     
    dibujo.dibujar_rectangulos()                                #llama a la clase que crea los cuadrados de fondo
    screen.blit(background, [250,100])                          #para mostrar la imagen         
    pygame.display.set_caption("Memoriza2")                     #Para mostrar nombre del juego 
    pygame.display.flip()                                       #Para actualizar la pantalla
