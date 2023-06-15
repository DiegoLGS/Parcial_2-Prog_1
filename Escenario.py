import pygame
from Clase_Jugador import Jugador
from Obtener_rectangulos import obtener_rectangulos

BLANCO = (255,255,255)
NEGRO = (0,0,0)
ROJO = (255,0,0)
AZUL = (0,0,255)
VERDE = (0,255,0)
AZUL_CLARO = (0,150,255)

ANCHO = 800
ALTO = 600

jugador = Jugador()

escenario = pygame.image.load("Segundo parcial/Recursos/Escenarios/0.png")
escenario_escalado = pygame.transform.scale(escenario,(ANCHO,ALTO))

plataforma = pygame.image.load("Segundo parcial/Recursos/Plataformas/1.png")
rectangulos_plataforma = obtener_rectangulos(plataforma.get_rect(topleft = (200,400)))
rectangulos_plataforma_dos = obtener_rectangulos(plataforma.get_rect(topleft = (400,300)))
rectangulos_plataforma_tres = obtener_rectangulos(plataforma.get_rect(topleft = (150,200)))

rectangulos_suelo = obtener_rectangulos(pygame.Rect(0,500,ANCHO,100) )

rectangulos_colision_vertical = [rectangulos_suelo["top"],
                                rectangulos_plataforma["top"],
                                rectangulos_plataforma_dos["top"],
                                rectangulos_plataforma_tres["top"]]


def Iniciar(PANTALLA):
    PANTALLA.blit(escenario_escalado,(0,0))
    PANTALLA.blit(plataforma,(200,400))
    PANTALLA.blit(plataforma,(400,300))
    PANTALLA.blit(plataforma,(150,200))   

    #if jugador.estado_actual == "lanzando_proyectil":
    #    PANTALLA.blit(cuchillo,(jugador.posicion["x"],jugador.posicion["y"]))   
            

    # rectangulos_del_jugador = jugador.rectangulos_lados
    # for rectangulos in rectangulos_del_jugador:
    #     pygame.draw.rect(PANTALLA, ROJO, rectangulos_del_jugador[rectangulos], 2)
    #     pygame.draw.rect(PANTALLA, ROJO, rectangulos_suelo[rectangulos], 2)
    #     pygame.draw.rect(PANTALLA, ROJO, rectangulos_plataforma[rectangulos], 2)
    #     pygame.draw.rect(PANTALLA, ROJO, rectangulos_plataforma_dos[rectangulos], 2)
    jugador.grupo_cuchillos.draw(PANTALLA)
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