import pygame
from Obtener_rectangulos import obtener_rectangulos
from Clase_Trampa_giratoria import Trampa_giratoria
from Clase_Moneda import Moneda
from Clase_Generador_enemigos import Generador_enemigos
ANCHO = 1000
ALTO = 700

class Nivel():
    def __init__(self, coordenadas_monedas, coordenadas_trampas, imagen_escenario, imagen_plataforma, coordenadas_plataformas):
        self.generador_de_enemigos = Generador_enemigos()
        self.grupo_enemigos = pygame.sprite.Group()
        self.grupo_trampas = pygame.sprite.Group()
        self.grupo_items = pygame.sprite.Group()       
        self.desplegar_trampas(coordenadas_trampas)
        self.desplegar_monedas(coordenadas_monedas)
        self.imagen_plataforma = imagen_plataforma
        self.escenario = imagen_escenario
        self.escenario_escalado = pygame.transform.scale(self.escenario, (ANCHO, ALTO))
        self.coordenadas_plataformas = coordenadas_plataformas

        self.rectangulos_suelo = obtener_rectangulos(pygame.Rect(0, 650, ANCHO, 100))
        self.rectangulos_pared_derecha = obtener_rectangulos(pygame.Rect(980, 0, 100, 800))
        self.rectangulos_pared_izquierda = obtener_rectangulos(pygame.Rect(-80, 0, 100, 800))

        self.rectangulos_colision_vertical = [self.rectangulos_suelo["top"]]

        self.rectangulos_colision_horizontal = [self.rectangulos_pared_derecha["left"],
                                                self.rectangulos_pared_izquierda["right"]]
        
    def desplegar_monedas(self, coordenadas_monedas):
        for coordenadas in coordenadas_monedas:
            self.grupo_items.add(Moneda(coordenadas))

    def desplegar_trampas(self, coordenadas_trampas):
        for coordenadas in coordenadas_trampas:
            self.grupo_trampas.add(Trampa_giratoria(coordenadas))

    def desplegar_plataformas(self, pantalla, coordenadas_plataformas):
        for coordenadas in coordenadas_plataformas:
            pantalla.blit(self.imagen_plataforma, coordenadas)
            rectangulo_plataforma = obtener_rectangulos(self.imagen_plataforma.get_rect(topleft = coordenadas))
            self.rectangulos_colision_vertical.append(rectangulo_plataforma["top"])

    def dibujar_escenario(self, pantalla):
        pantalla.blit(self.escenario_escalado, (0, 0))        
    
    def actualizar(self, pantalla, jugador):
        self.dibujar_escenario(pantalla)
        self.desplegar_plataformas(pantalla, self.coordenadas_plataformas)
        self.grupo_enemigos.draw(pantalla)
        self.grupo_enemigos.update(pantalla ,jugador)       
        self.grupo_trampas.update(pantalla, jugador)
        self.grupo_items.update(pantalla, jugador)
        self.colision_vertical(jugador, self.grupo_enemigos)
        self.colision_horizontal(jugador, self.grupo_enemigos)

        if self.generador_de_enemigos.enemigos_creados < 4:
            self.generador_de_enemigos.generar_enemigo(self.grupo_enemigos,jugador)

    def colision_vertical(self, jugador, grupo_enemigos): 
        for rectangulos in self.rectangulos_colision_vertical:
            if rectangulos.colliderect(jugador.rectangulos_lados["bottom"]):
                jugador.sobre_suelo = True
                break
            else:
                jugador.sobre_suelo = False

        if len(grupo_enemigos) > 0:
            for enemigo in grupo_enemigos:
                for rectangulos in self.rectangulos_colision_vertical:
                    if rectangulos.colliderect(enemigo.rect):
                        enemigo.sobre_suelo = True
                        break
                    else:
                        enemigo.sobre_suelo = False
                enemigo.aplicar_gravedad()            

        jugador.aplicar_gravedad()

    def colision_horizontal(self, jugador, grupo_enemigos):
        if self.rectangulos_colision_horizontal[0].colliderect(jugador.rectangulo_jugador) and jugador.mirando_izquierda == False or self.rectangulos_colision_horizontal[1].colliderect(jugador.rectangulo_jugador) and jugador.mirando_izquierda == True:
            jugador.velocidad = 0            
        else:
            jugador.velocidad = 6

        if len(grupo_enemigos) > 0:
            for rectangulos in self.rectangulos_colision_horizontal:
                for enemigo in grupo_enemigos:                
                    if self.rectangulos_colision_horizontal[0].colliderect(enemigo.rect) and enemigo.mirando_izquierda == False:
                        enemigo.mirando_izquierda = True            
                    elif self.rectangulos_colision_horizontal[1].colliderect(enemigo.rect) and enemigo.mirando_izquierda == True:
                        enemigo.mirando_izquierda = False

