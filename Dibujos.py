import pygame

BLACK					=			(  0,   0,   0)
DARK_BLUE				=			(  0,   0, 100)
BLUE					=			(  0,   0, 255)
DARK_GREEN			    =			(  0, 100,   0)
GREENISH_BLUE			=			(  0, 100, 100)
LIGHT_TURQUOISE		    =			(  0, 100, 255)
GREEN					=			(  0, 255,   0)
WATERY_GREEN			=			(  0, 255, 100)
CYAN					=			(  0, 255, 255)

RED						=			(255,   0,   0)
DARK_PINK				=			(255,   0, 100)
PINK					=			(255,   0, 255)
ORANGE				    =			(255, 100,   0)
RED_PINK				=			(255, 100, 100)
MAGENT				    =			(255, 100, 255)
YELLOW					=			(255, 255,   0)
LIGHT_YELLOW			=			(255, 255, 100)
WHITE					=			(255, 255, 255)

REDDISH_BROWN		    =			(100,   0,   0)
PURPLE					=			(100,   0, 100)
MUSTARD				    =			(100,   0, 255)
GREENISH_BROWN		    =			(100, 100,   0)
GREY					=			(100, 100, 100)
LIGHT_GREY              =           (200, 200, 200) 
TURQUOISE				=			(100, 100, 255)

size = (1000,700)
screen = pygame.display.set_mode(size)
class Dibujo:
    def __init__(self, screen):
        self.screen = screen

    def dibujar_rectangulos(self):
        #Cuadros primera fila
        for i in range(10):
            x = i*200
            pygame.draw.rect(self.screen, GREY, (x,0, 100, 100))
        for i in range(10):
            y = i*200+100
            pygame.draw.rect(self.screen, LIGHT_GREY, (y,0, 100, 100))
        
        
        #Cuadros segunda fila
        for i in range(10):
            x = i*200
            pygame.draw.rect(self.screen, LIGHT_GREY, (x,100, 100, 100))
        for i in range(10):
            y = i*200+100
            pygame.draw.rect(self.screen, GREY, (y,100, 100, 100))
        

        #Cuadros tercera fila
        for i in range(10):
            x = i*200
            pygame.draw.rect(self.screen, GREY, (x,200, 100, 100))
        for i in range(10):
            y = i*200+100
            pygame.draw.rect(self.screen, LIGHT_GREY, (y,200, 100, 100))
        

        #Cuadros cuarta fila
        for i in range(10):
            x = i*200
            pygame.draw.rect(self.screen, LIGHT_GREY, (x,300, 100, 100))
        for i in range(10):
            y = i*200+100
            pygame.draw.rect(self.screen, GREY, (y,300, 100, 100))
        

        #Cuadros quinta fila
        for i in range(10):
            x = i*200
            pygame.draw.rect(self.screen, GREY, (x,400, 100, 100))
        for i in range(10):
            y = i*200+100
            pygame.draw.rect(self.screen, LIGHT_GREY, (y,400, 100, 100))
        
        #Cuadros sexta fila
        for i in range(10):
            x = i*200
            pygame.draw.rect(self.screen, LIGHT_GREY, (x,500, 100, 100))
        for i in range(10):
            y = i*200+100
            pygame.draw.rect(self.screen, GREY, (y,500, 100, 100))
        

        #Cuadros Septima fila
        for i in range(10):
            x = i*200
            pygame.draw.rect(self.screen, GREY, (x,600, 100, 100))
        for i in range(10):
            y = i*200+100
            pygame.draw.rect(self.screen, LIGHT_GREY, (y,600, 100, 100))
