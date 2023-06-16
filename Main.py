import pygame, sys
from Escenario import Iniciar

BLANCO = (255,255,255)
NEGRO = (0,0,0)
ROJO = (255,0,0)
AZUL = (0,0,255)
VERDE = (0,255,0)
AZUL_CLARO = (0,150,255)

FPS = 60
ANCHO = 1000
ALTO = 800

#Setup general
pygame.init()
PANTALLA = pygame.display.set_mode((ANCHO,ALTO))
clock = pygame.time.Clock()

#Fondo del juego
background = pygame.image.load("Segundo parcial/Recursos/Fondo icono/luna sangrienta.jpg")
#background = pygame.transform.scale(background, (ANCHO,ALTO))
pygame.display.set_caption("Ominous Keep")
icono = pygame.image.load("Segundo parcial/Recursos/Fondo icono/spinning-sword.png")
pygame.display.set_icon(icono)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    PANTALLA.blit(background, (0,0))    
    
    Iniciar(PANTALLA)
    
    pygame.display.update()
    clock.tick(FPS)