import pygame
from Clase_Jugador import Jugador
from Clase_Cronometro import Cronometro
from Clase_Nivel import Nivel

BLANCO = (255,255,255)
NEGRO = (0,0,0)
ROJO = (255,0,0)
AZUL = (0,0,255)
VERDE = (0,255,0)
AZUL_CLARO = (0,150,255)

ANCHO = 1000
ALTO = 700

pygame.init()

jugador = Jugador()
cronometro = Cronometro(60)
primer_nivel = Nivel(coordenadas_monedas = [(400, 580), (500, 580), (600, 580), (700, 580), (600, 400), (700, 400), (800, 400), (200, 300), (250, 200), (450, 200), (650, 200)],
                    coordenadas_trampas = [(710, 290), (120, 290)],
                    imagen_escenario = pygame.image.load("Segundo parcial/Recursos/Escenarios/0.png"),
                    imagen_plataforma = pygame.image.load("Segundo parcial/Recursos/Plataformas/1.png"),
                    coordenadas_plataformas =  [(100, 400), (400, 300), (600, 450)])

fuente = pygame.font.SysFont("garamond",30)

def Iniciar(PANTALLA):
    primer_nivel.actualizar(PANTALLA,jugador)
    jugador.grupo_cuchillos.update()    
    jugador.grupo_cuchillos.draw(PANTALLA)   
    jugador.mostrar_salud(PANTALLA)  
    jugador.actualizar()            
    display_puntuacion = fuente.render("Puntaje: " + str(jugador.puntaje),False,BLANCO)

    PANTALLA.blit(jugador.imagen,jugador.rectangulo_jugador)
    PANTALLA.blit(jugador.retrato,(20,20))
    PANTALLA.blit(display_puntuacion, (800,50))
    cronometro.actualizar()
    cronometro.mostrar_tiempo(PANTALLA)

