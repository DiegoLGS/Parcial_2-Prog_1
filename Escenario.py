import pygame
from Clase_Jugador import Jugador
from Obtener_rectangulos import obtener_rectangulos
from Clase_Zombie import Zombie

BLANCO = (255,255,255)
NEGRO = (0,0,0)
ROJO = (255,0,0)
AZUL = (0,0,255)
VERDE = (0,255,0)
AZUL_CLARO = (0,150,255)

ANCHO = 1000
ALTO = 700

jugador = Jugador()


escenario = pygame.image.load("Segundo parcial/Recursos/Escenarios/0.png")
escenario_escalado = pygame.transform.scale(escenario,(ANCHO,ALTO))

plataforma = pygame.image.load("Segundo parcial/Recursos/Plataformas/1.png")
posicion_plataforma_uno = (100,400)
posicion_plataforma_dos = (400,300)
posicion_plataforma_tres = (600,450)
rectangulos_plataforma = obtener_rectangulos(plataforma.get_rect(topleft = posicion_plataforma_uno ))
rectangulos_plataforma_dos = obtener_rectangulos(plataforma.get_rect(topleft = posicion_plataforma_dos))
rectangulos_plataforma_tres = obtener_rectangulos(plataforma.get_rect(topleft = posicion_plataforma_tres))

rectangulos_suelo = obtener_rectangulos(pygame.Rect(0,650,ANCHO,100))
rectangulos_pared_derecha = obtener_rectangulos(pygame.Rect(980,0,100,800))
rectangulos_pared_izquierda = obtener_rectangulos(pygame.Rect(-80,0,100,800))

rectangulos_colision_vertical = [rectangulos_suelo["top"],
                                rectangulos_plataforma["top"],
                                rectangulos_plataforma_dos["top"],
                                rectangulos_plataforma_tres["top"]]

rectangulos_colision_horizontal = [rectangulos_pared_derecha["left"],
                                rectangulos_pared_izquierda["right"]]

grupo_enemigos = pygame.sprite.Group()
grupo_enemigos.add(Zombie())

def Iniciar(PANTALLA):
    PANTALLA.blit(escenario_escalado,(0,0))
    PANTALLA.blit(plataforma,posicion_plataforma_uno)
    PANTALLA.blit(plataforma,posicion_plataforma_dos)
    PANTALLA.blit(plataforma,posicion_plataforma_tres)   

    #if jugador.estado_actual == "lanzando_proyectil":
    #    PANTALLA.blit(cuchillo,(jugador.posicion["x"],jugador.posicion["y"]))               

    # rectangulos_del_jugador = jugador.rectangulos_lados
    #for rectangulos in zombie.rectangulos_lados:
        #pygame.draw.rect(PANTALLA, ROJO, zombie.rectangulos_lados[rectangulos], 2)
    #     pygame.draw.rect(PANTALLA, ROJO, rectangulos_del_jugador[rectangulos], 2)
    #     pygame.draw.rect(PANTALLA, ROJO, rectangulos_suelo[rectangulos], 2)
    #     pygame.draw.rect(PANTALLA, AZUL_CLARO, rectangulos_pared_derecha[rectangulos], 2)
    #     pygame.draw.rect(PANTALLA, VERDE, rectangulos_pared_izquierda[rectangulos], 2)
    #     pygame.draw.rect(PANTALLA, ROJO, rectangulos_plataforma[rectangulos], 2)
    #     pygame.draw.rect(PANTALLA, ROJO, rectangulos_plataforma_dos[rectangulos], 2)
    #     pygame.draw.rect(PANTALLA, ROJO, rectangulos_plataforma_tres[rectangulos], 2)
    # for cuchillos in jugador.grupo_cuchillos:
    #     pygame.draw.rect(PANTALLA, AZUL_CLARO, cuchillos.rect, 2)

    # for zombies in grupo_enemigos:
    #     pygame.draw.rect(PANTALLA, AZUL_CLARO, zombies.rect, 2)
    

    jugador.grupo_cuchillos.update()    
    jugador.grupo_cuchillos.draw(PANTALLA)
    grupo_enemigos.update()       
    grupo_enemigos.draw(PANTALLA)
    
    jugador.actualizar()
    for zombie in grupo_enemigos:
        zombie.actualizar()
        colision_cuchillo_zombie = pygame.sprite.spritecollide(zombie, jugador.grupo_cuchillos, True)
        if colision_cuchillo_zombie:
            zombie.vida_total -= 1
            #if zombie.vida_total < 1:
            #    zombie.kill()
            
    colision_vertical()
    colision_horizontal()

    PANTALLA.blit(jugador.imagen,jugador.rectangulo_jugador)
    #PANTALLA.blit(zombie.image,zombie.rect)

    #print(zombie.rectangulo_zombie)
    #pygame.draw.rect(PANTALLA, VERDE, zombie.rectangulo_zombie, 2)
    #pygame.draw.rect(PANTALLA, VERDE,zombie.rectangulo_zombie, 2)
    PANTALLA.blit(jugador.retrato,(20,20))
    x = 140
    for i in range(jugador.vida_total):
        PANTALLA.blit(jugador.imagen_salud,(x,50))
        x += 40

def colision_vertical(): 
    for rectangulos in rectangulos_colision_vertical:
        if rectangulos.colliderect(jugador.rectangulos_lados["bottom"]):
            jugador.sobre_suelo = True
            break
        else:
            jugador.sobre_suelo = False

    if len(grupo_enemigos) > 0:
        for zombie in grupo_enemigos:
            for rectangulos in rectangulos_colision_vertical:
                if rectangulos.colliderect(zombie.rect):
                    zombie.sobre_suelo = True
                    break
                else:
                    zombie.sobre_suelo = False
        zombie.aplicar_gravedad()
        

    jugador.aplicar_gravedad()

def colision_horizontal():
    if rectangulos_colision_horizontal[0].colliderect(jugador.rectangulo_jugador) and jugador.mirando_izquierda == False or rectangulos_colision_horizontal[1].colliderect(jugador.rectangulo_jugador) and jugador.mirando_izquierda == True:
        jugador.velocidad = 0            
    else:
        jugador.velocidad = 6

    if len(grupo_enemigos) > 0:
        for rectangulos in rectangulos_colision_horizontal:
            for zombie in grupo_enemigos:                
                if rectangulos_colision_horizontal[0].colliderect(zombie.rect) and zombie.mirando_izquierda == False:
                    zombie.mirando_izquierda = True            
                elif rectangulos_colision_horizontal[1].colliderect(zombie.rect) and zombie.mirando_izquierda == True:
                    zombie.mirando_izquierda = False           
        
    