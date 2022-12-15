import pygame
import sys

pygame.init()
pygame.font.init()
pygame.mixer.init()
color_blanco = (255, 255, 255)

ventana = pygame.display.set_mode((1000,700))
ventana.fill(color_blanco)
pygame.display.set_caption("Memorizan2")


while True:
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:   
            pygame.quit()              
            sys.exit()              

    pygame.display.flip()         
