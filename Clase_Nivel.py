import pygame
from Obtener_rectangulos import obtener_rectangulos
from Clase_Trampa_giratoria import Trampa_giratoria
from Clase_Moneda import Moneda
from Clase_Generador_enemigos import Generador_enemigos
from Clase_Pocion_chica import Pocion_chica
from Clase_Trampa_escondida import Trampa_escondida
from Clase_Cronometro import Cronometro

ANCHO = 1000
ALTO = 700

class Nivel():
    def __init__(self, nivel, coordenadas_monedas, coordenadas_pocion_chica, coordenadas_trampas, imagen_escenario, imagen_plataforma, coordenadas_plataformas, musica):
        self.numero = nivel
        self.generador_de_enemigos = Generador_enemigos()
        self.coordenadas_plataformas = coordenadas_plataformas
        self.cronometro = Cronometro(60)
        self.nivel_finalizado = False

        #musica
        # pygame.mixer.init()
        self.musica = musica        
        self.reproduciendo_musica = False
        # pygame.mixer.music.load(self.musica)
        # pygame.mixer.music.play()       

        #grupos
        self.grupo_enemigos = pygame.sprite.Group()
        self.grupo_trampas = pygame.sprite.Group()
        self.grupo_items = pygame.sprite.Group()       

        #mostrar elementos
        self.desplegar_trampas(coordenadas_trampas)
        self.desplegar_items(coordenadas_monedas, coordenadas_pocion_chica)        

        #imagenes
        self.imagen_plataforma = imagen_plataforma
        self.imagen_escenario_escalado = pygame.transform.scale(imagen_escenario, (ANCHO, ALTO))

        #rectangulos default
        self.rectangulos_suelo = obtener_rectangulos(pygame.Rect(0, 650, ANCHO, 100))
        self.rectangulos_pared_derecha = obtener_rectangulos(pygame.Rect(980, 0, 100, 800))
        self.rectangulos_pared_izquierda = obtener_rectangulos(pygame.Rect(-80, 0, 100, 800))
        self.rectangulos_colision_vertical = [self.rectangulos_suelo["top"]]
        self.rectangulos_colision_horizontal = [self.rectangulos_pared_derecha["left"],
                                                self.rectangulos_pared_izquierda["right"]]
        
    def cargar_musica(self):
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.load(self.musica)
        pygame.mixer.music.play()
        
    def desplegar_items(self, coordenadas_monedas, coordenadas_pocion_chica):
        for coordenadas in coordenadas_monedas:
            self.grupo_items.add(Moneda(coordenadas))

        for coordenadas in coordenadas_pocion_chica:
            self.grupo_items.add(Pocion_chica(coordenadas))

    def desplegar_trampas(self, coordenadas_trampas):
        for coordenadas in coordenadas_trampas:
            match self.numero:
                case 1:
                    self.grupo_trampas.add(Trampa_giratoria(coordenadas))

                case 2:
                    self.grupo_trampas.add(Trampa_escondida(coordenadas))            

    def desplegar_plataformas(self, pantalla, coordenadas_plataformas):
        for coordenadas in coordenadas_plataformas:
            pantalla.blit(self.imagen_plataforma, coordenadas)
            rectangulo_plataforma = obtener_rectangulos(self.imagen_plataforma.get_rect(topleft = coordenadas))
            self.rectangulos_colision_vertical.append(rectangulo_plataforma["top"])

    def dibujar_escenario(self, pantalla):
        pantalla.blit(self.imagen_escenario_escalado, (0, 0))        
        self.desplegar_plataformas(pantalla, self.coordenadas_plataformas)

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
    
    def actualizar(self, pantalla, jugador, tiempo_espera_enemigos):
        self.dibujar_escenario(pantalla)
        self.grupo_enemigos.draw(pantalla)
        self.grupo_enemigos.update(pantalla ,jugador)       
        self.grupo_trampas.update(pantalla, jugador)
        self.grupo_items.update(pantalla, jugador)
        self.colision_vertical(jugador, self.grupo_enemigos)
        self.colision_horizontal(jugador, self.grupo_enemigos)

        if self.generador_de_enemigos.enemigos_creados < 6:
            self.generador_de_enemigos.generar_enemigo(self.numero, self.grupo_enemigos, jugador, tiempo_espera_enemigos)