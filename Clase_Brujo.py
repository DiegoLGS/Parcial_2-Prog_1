import pygame
from Imagenes_enemigos import diccionario_animaciones_brujo
import random
from Clase_Lapida import Lapida

class Brujo(pygame.sprite.Sprite):
    def __init__(self, jugador):
        super().__init__()
        self.jugador = jugador
        self.nombre = "Brujo"
        self.vida_total = 2
        self.velocidad = 1
        self.posicion = {"x":random.randint(100, 900) ,"y":100}

        #caracteristicas
        self.gravedad = 1
        self.aumento_gravedad = 0.15
        self.velocidad_animacion = 0.1

        #proyectiles
        self.grupo_lapidas = pygame.sprite.Group()
        self.tiempo_actual = pygame.time.get_ticks()
        self.tiempo_ultimo_lanzamiento = self.tiempo_actual
        self.tiempo_espera_proyectil = 2000       
        self.lanzando_proyectil = False

        #estados
        self.indice_inicial = 0
        self.estado_actual = "cayendo"
        if random.randint(0,1) == 1:
            self.mirando_izquierda = False
        else:
            self.mirando_izquierda = True
        self.verificar_direccion(self.estado_actual)
        self.sobre_suelo = False

        #rectangulos
        self.image = diccionario_animaciones_brujo["cayendo"][0]
        self.rect = self.image.get_rect(topleft = (self.posicion["x"],self.posicion["y"]))   

    def verificar_direccion(self, estado_actual):
        if self.mirando_izquierda == True:
            estado_actual = f"{self.estado_actual}_izquierda"
        self.animar_imagenes(estado_actual)                
            
    def animar_imagenes(self, estado_actual):
        if self.indice_inicial >= len(diccionario_animaciones_brujo[estado_actual]):
            self.indice_inicial = 0
        self.image = diccionario_animaciones_brujo[estado_actual][int(self.indice_inicial)]
        self.indice_inicial += self.velocidad_animacion

        if self.lanzando_proyectil == True and self.indice_inicial >= len(diccionario_animaciones_brujo[estado_actual]):
            self.lanzando_proyectil = False

    def aplicar_gravedad(self):
        if self.sobre_suelo == False:
            self.posicion["y"] += self.gravedad
            self.gravedad += self.aumento_gravedad
            self.rect.y = self.posicion["y"]    
        else:
            self.gravedad = 1

    def caminar(self):
        if self.vida_total > 0 and self.lanzando_proyectil == False:
            if self.sobre_suelo == True :
                if self.mirando_izquierda == False:
                    self.posicion["x"] += self.velocidad
                else:
                    self.posicion["x"] += self.velocidad * -1
                self.estado_actual = "caminando"
            else:
                self.estado_actual = "cayendo"

    def lanzar_proyectil(self):
        self.estado_actual = "lanzando_proyectil"
        self.lanzando_proyectil = True
        self.indice_inicial = 0
        self.grupo_lapidas.add(Lapida(self.rect.x,self.rect.y + 58, self.mirando_izquierda, self.jugador.posicion["x"], self.jugador.posicion["y"]))

    def daño_cuchillo(self, jugador):
        if self.estado_actual == "muriendo" or self.estado_actual == "muriendo_izquierda":
            colision_cuchillo_enemigo = pygame.sprite.spritecollide(self, jugador.grupo_cuchillos, False)
        else:
            colision_cuchillo_enemigo = pygame.sprite.spritecollide(self, jugador.grupo_cuchillos, True)
            if colision_cuchillo_enemigo:
                self.vida_total -= 1
                if self.vida_total <= 0:
                    jugador.puntaje += 100

    def daño_contacto(self, jugador):
        if (jugador.rectangulo_jugador.colliderect(self.rect) and jugador.invulnerabilidad == False) and (not self.estado_actual == "muriendo" and not self.estado_actual == "muriendo_izquierda"):
            jugador.vida_total -= 1
            jugador.daño_recibido = True

    def verificar_direccion_ataque(self):
        if self.vida_total > 0:
            if (self.tiempo_actual - self.tiempo_ultimo_lanzamiento >= self.tiempo_espera_proyectil) and ((self.jugador.posicion["x"] - self.rect.x < 0 and self.mirando_izquierda) or (self.jugador.posicion["x"] - self.rect.x > 0 and not self.mirando_izquierda)):
                self.lanzar_proyectil()
                self.tiempo_ultimo_lanzamiento = self.tiempo_actual
            
    def muerte(self):
        if self.vida_total < 1:
            if not self.estado_actual == "muriendo" and not self.estado_actual == "muriendo_izquierda":
                self.indice_inicial = 0
            self.estado_actual = "muriendo"
            if self.indice_inicial >= len(diccionario_animaciones_brujo[self.estado_actual]):
                self.kill()

    def update(self, pantalla, jugador):
        self.verificar_direccion(self.estado_actual)
        self.rect.x = self.posicion["x"]
        self.rect.y = self.posicion["y"]
        self.caminar()
        self.daño_cuchillo(jugador)
        self.daño_contacto(jugador)
        self.verificar_direccion_ataque()
        self.tiempo_actual = pygame.time.get_ticks()
        self.grupo_lapidas.update(jugador)
        self.grupo_lapidas.draw(pantalla)
        self.muerte()