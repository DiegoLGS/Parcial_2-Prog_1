import pygame
from Clase_Jugador import Jugador
from Obtener_rectangulos import obtener_rectangulos

BLANCO = (255,255,255)
NEGRO = (0,0,0)
ROJO = (255,0,0)
AZUL = (0,0,255)
VERDE = (0,255,0)
AZUL_CLARO = (0,150,255)

ANCHO = 1000
ALTO = 800

jugador = Jugador()

escenario = pygame.image.load("Segundo parcial/Recursos/Escenarios/0.png")
escenario_escalado = pygame.transform.scale(escenario,(ANCHO,ALTO))

plataforma = pygame.image.load("Segundo parcial/Recursos/Plataformas/1.png")
posicion_plataforma_uno = (100,500)
posicion_plataforma_dos = (400,400)
posicion_plataforma_tres = (600,550)
rectangulos_plataforma = obtener_rectangulos(plataforma.get_rect(topleft = posicion_plataforma_uno ))
rectangulos_plataforma_dos = obtener_rectangulos(plataforma.get_rect(topleft = posicion_plataforma_dos))
rectangulos_plataforma_tres = obtener_rectangulos(plataforma.get_rect(topleft = posicion_plataforma_tres))

rectangulos_suelo = obtener_rectangulos(pygame.Rect(0,750,ANCHO,100))
rectangulos_pared_derecha = obtener_rectangulos(pygame.Rect(950,0,100,800))

rectangulos_colision_vertical = [rectangulos_suelo["top"],
                                rectangulos_plataforma["top"],
                                rectangulos_plataforma_dos["top"],
                                rectangulos_plataforma_tres["top"]]


def Iniciar(PANTALLA):
    PANTALLA.blit(escenario_escalado,(0,0))
    PANTALLA.blit(plataforma,posicion_plataforma_uno)
    PANTALLA.blit(plataforma,posicion_plataforma_dos)
    PANTALLA.blit(plataforma,posicion_plataforma_tres)   

    #if jugador.estado_actual == "lanzando_proyectil":
    #    PANTALLA.blit(cuchillo,(jugador.posicion["x"],jugador.posicion["y"]))               

    rectangulos_del_jugador = jugador.rectangulos_lados
    for rectangulos in rectangulos_del_jugador:
        pygame.draw.rect(PANTALLA, ROJO, rectangulos_del_jugador[rectangulos], 2)
        pygame.draw.rect(PANTALLA, ROJO, rectangulos_suelo[rectangulos], 2)
        pygame.draw.rect(PANTALLA, AZUL_CLARO, rectangulos_pared_derecha[rectangulos], 2)
        pygame.draw.rect(PANTALLA, ROJO, rectangulos_plataforma[rectangulos], 2)
        pygame.draw.rect(PANTALLA, ROJO, rectangulos_plataforma_dos[rectangulos], 2)
        pygame.draw.rect(PANTALLA, ROJO, rectangulos_plataforma_tres[rectangulos], 2)
    jugador.grupo_cuchillos.draw(PANTALLA)
    for cuchillos in jugador.grupo_cuchillos:
        pygame.draw.rect(PANTALLA, (255, 0, 0), cuchillos.rect, 2)
    jugador.grupo_cuchillos.update()
    
    jugador.actualizar()
    colision_vertical()

    PANTALLA.blit(jugador.imagen,jugador.rectangulo_jugador)

def colision_vertical(): 
    for rectangulos in rectangulos_colision_vertical:
        if rectangulos.colliderect(jugador.rectangulos_lados["bottom"]):
            jugador.sobre_suelo = True
            break
        else:
            jugador.sobre_suelo = False

    jugador.aplicar_gravedad()