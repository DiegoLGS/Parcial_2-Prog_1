import pygame
from Imagenes_enemigos import diccionario_animaciones_zombie
import random
from Sonidos import sonido_cuchillo

class Zombie(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.nombre = "Zombie"
        self.vida_total = 3
        self.velocidad = 1
        self.posicion = {"x":random.randint(100, 900) ,"y":100}

        #caracteristicas
        self.gravedad = 1
        self.aumento_gravedad = 0.2
        self.velocidad_animacion = 0.05

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
        self.image = diccionario_animaciones_zombie["cayendo"][0]
        self.rect = self.image.get_rect(topleft = (self.posicion["x"],self.posicion["y"]))        

    def verificar_direccion(self,estado_actual):
        if self.mirando_izquierda == True:
            estado_actual = f"{self.estado_actual}_izquierda"
        self.animar_imagenes(estado_actual)                
            
    def animar_imagenes(self,estado_actual):
        if self.indice_inicial >= len(diccionario_animaciones_zombie[estado_actual]):
            self.indice_inicial = 0
        self.image = diccionario_animaciones_zombie[estado_actual][int(self.indice_inicial)]
        self.indice_inicial += self.velocidad_animacion

    def aplicar_gravedad(self):
        if self.sobre_suelo == False:
            self.posicion["y"] += self.gravedad
            self.gravedad += self.aumento_gravedad
            self.rect.y = self.posicion["y"]    
        else:
            self.gravedad = 1

    def caminar(self):
        if self.vida_total > 0:
            if self.sobre_suelo == True:
                if self.mirando_izquierda == False:
                    self.posicion["x"] += self.velocidad
                else:
                    self.posicion["x"] += self.velocidad * -1
                self.estado_actual = "caminando"
            else:
                self.estado_actual = "cayendo"
    
    def daño_cuchillo(self,jugador):
        if self.estado_actual == "muriendo" or self.estado_actual == "muriendo_izquierda":
            colision_cuchillo_enemigo = pygame.sprite.spritecollide(self, jugador.grupo_cuchillos, False)
        else:
            colision_cuchillo_enemigo = pygame.sprite.spritecollide(self, jugador.grupo_cuchillos, True)
            if colision_cuchillo_enemigo:
                sonido_cuchillo.play()
                self.vida_total -= 1
                if self.vida_total <= 0:
                    jugador.puntaje += 100

    def daño_contacto(self,jugador):
        if (jugador.rectangulo_jugador.colliderect(self.rect) and jugador.invulnerabilidad == False) and (not self.estado_actual == "muriendo" and not self.estado_actual == "muriendo_izquierda"):
            jugador.vida_total -= 1
            jugador.daño_recibido = True
            
    def muerte(self):
        if self.vida_total < 1:
            if not self.estado_actual == "muriendo" and not self.estado_actual == "muriendo_izquierda":
                self.indice_inicial = 0
            self.estado_actual = "muriendo"
            if self.indice_inicial >= len(diccionario_animaciones_zombie[self.estado_actual]):
                self.kill()

    def update(self,pantalla,jugador):
        self.verificar_direccion(self.estado_actual)
        self.rect.x = self.posicion["x"]
        self.rect.y = self.posicion["y"]
        self.caminar()
        self.daño_cuchillo(jugador)
        self.daño_contacto(jugador)
        self.muerte()            
