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
primer_nivel = Nivel(1,
                    coordenadas_monedas = [(400, 580), (500, 580), (600, 580), (700, 580), (600, 400), (700, 400), (800, 400), (200, 300), (250, 200), (450, 200), (650, 200)],
                    coordenadas_pocion_chica = [(170, 220), (550, 250)],
                    coordenadas_trampas = [(710, 290), (120, 290)],
                    imagen_escenario = pygame.image.load("Segundo parcial/Recursos/Escenarios/0.png"),
                    imagen_plataforma = pygame.image.load("Segundo parcial/Recursos/Plataformas/1.png"),
                    coordenadas_plataformas = [(100, 400), (400, 300), (600, 450)])

segundo_nivel = Nivel(2,
                    coordenadas_monedas = [(350, 480), (350, 380), (350, 240), (500, 180), (600, 500), (700, 400), (800, 180), (200, 200), (250, 250), (500, 300), (600, 300)],
                    coordenadas_pocion_chica = [(900, 600), (700, 250), (180, 100)],
                    coordenadas_trampas = [(560, 300), (350, 600)],
                    imagen_escenario = pygame.image.load("Segundo parcial/Recursos/Escenarios/1.png"),
                    imagen_plataforma = pygame.image.load("Segundo parcial/Recursos/Plataformas/0.png"),
                    coordenadas_plataformas = [(280, 280), (490, 350), (600, 550)])

nivel_final = Nivel(3,
                    coordenadas_monedas = [],
                    coordenadas_pocion_chica = [],
                    coordenadas_trampas = [],
                    imagen_escenario = pygame.image.load("Segundo parcial/Recursos/Escenarios/2.png"),
                    imagen_plataforma = pygame.image.load("Segundo parcial/Recursos/Plataformas/0.png"),
                    coordenadas_plataformas = [])

fuente = pygame.font.SysFont("garamond",30)
jugador.nivel_final(True)

def Iniciar(PANTALLA):
    #primer_nivel.actualizar(PANTALLA, jugador)
    #segundo_nivel.actualizar(PANTALLA, jugador)
    nivel_final.actualizar(PANTALLA, jugador)
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