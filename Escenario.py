import pygame
from Clase_Jugador import Jugador
from Obtener_rectangulos import obtener_rectangulos
from Clase_Zombie import Zombie
from Clase_Trampa_giratoria import Trampa_giratoria
from Generador_enemigos import Generador_enemigos
from Clase_Brujo import Brujo

BLANCO = (255,255,255)
NEGRO = (0,0,0)
ROJO = (255,0,0)
AZUL = (0,0,255)
VERDE = (0,255,0)
AZUL_CLARO = (0,150,255)

ANCHO = 1000
ALTO = 700

jugador = Jugador()
grupo_enemigos = pygame.sprite.Group()
grupo_enemigos.add(Zombie())
grupo_enemigos.add(Brujo(jugador))
generador_de_enemigos = Generador_enemigos()
grupo_trampas = pygame.sprite.Group()
grupo_trampas.add(Trampa_giratoria(710,290))
grupo_trampas.add(Trampa_giratoria(120,290))

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

def Iniciar(PANTALLA):
    PANTALLA.blit(escenario_escalado,(0,0))
    PANTALLA.blit(plataforma,posicion_plataforma_uno)
    PANTALLA.blit(plataforma,posicion_plataforma_dos)
    PANTALLA.blit(plataforma,posicion_plataforma_tres)   
    
    #generador_de_enemigos.generar_enemigo(grupo_enemigos)

    jugador.grupo_cuchillos.update()    
    jugador.grupo_cuchillos.draw(PANTALLA)    
    grupo_enemigos.update()       
    grupo_enemigos.draw(PANTALLA)
    grupo_trampas.update()       
    for trampa in grupo_trampas:
        PANTALLA.blit(trampa.imagen_girando , trampa.rect)        
    
    jugador.actualizar()
    for enemigo in grupo_enemigos:
        if enemigo.estado_actual == "muriendo" or enemigo.estado_actual == "muriendo_izquierda":
            colision_cuchillo_enemigo = pygame.sprite.spritecollide(enemigo, jugador.grupo_cuchillos, False)
        else:
            colision_cuchillo_enemigo = pygame.sprite.spritecollide(enemigo, jugador.grupo_cuchillos, True)
            if colision_cuchillo_enemigo:
                enemigo.vida_total -= 1
            
        if (jugador.rectangulo_jugador.colliderect(enemigo.rect) and jugador.invulnerabilidad == False) and (not enemigo.estado_actual == "muriendo" and not enemigo.estado_actual == "muriendo_izquierda"):
            jugador.vida_total -= 1
            jugador.daño_recibido = True

        if enemigo.nombre == "Brujo":
            enemigo.grupo_lapidas.update()
            enemigo.grupo_lapidas.draw(PANTALLA)
            for lapida in enemigo.grupo_lapidas:
                if jugador.rectangulo_jugador.colliderect(lapida) and jugador.invulnerabilidad == False:
                    jugador.vida_total -= 1
                    jugador.daño_recibido = True

    for trampa in grupo_trampas:
        if jugador.invulnerabilidad == False:
            if trampa.rect.colliderect(jugador.rectangulo_jugador):
                jugador.vida_total -= 1
                jugador.daño_recibido = True

            
    colision_vertical()
    colision_horizontal()

    PANTALLA.blit(jugador.imagen,jugador.rectangulo_jugador)

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
        for enemigo in grupo_enemigos:
            for rectangulos in rectangulos_colision_vertical:
                if rectangulos.colliderect(enemigo.rect):
                    enemigo.sobre_suelo = True
                    break
                else:
                    enemigo.sobre_suelo = False
            enemigo.aplicar_gravedad()
        

    jugador.aplicar_gravedad()

def colision_horizontal():
    if rectangulos_colision_horizontal[0].colliderect(jugador.rectangulo_jugador) and jugador.mirando_izquierda == False or rectangulos_colision_horizontal[1].colliderect(jugador.rectangulo_jugador) and jugador.mirando_izquierda == True:
        jugador.velocidad = 0            
    else:
        jugador.velocidad = 6

    if len(grupo_enemigos) > 0:
        for rectangulos in rectangulos_colision_horizontal:
            for enemigo in grupo_enemigos:                
                if rectangulos_colision_horizontal[0].colliderect(enemigo.rect) and enemigo.mirando_izquierda == False:
                    enemigo.mirando_izquierda = True            
                elif rectangulos_colision_horizontal[1].colliderect(enemigo.rect) and enemigo.mirando_izquierda == True:
                    enemigo.mirando_izquierda = False           
        
    