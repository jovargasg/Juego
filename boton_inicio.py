import pygame
from Dibujos import *
pygame.font.init()
size = (1000,700)
screen = pygame.display.set_mode(size)

class Boton_inicio:
    def __init__(self, screen):
        self.screen = screen

    def dibujar_boton(self):
        pygame.draw.rect(self.screen, RED, (310, 510, 390, 65))
