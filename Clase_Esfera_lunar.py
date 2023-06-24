import pygame
from Imagenes_proyectiles import esfera_lunar, esfera_lunar_izquierda
ANCHO = 1000

class Esfera_lunar(pygame.sprite.Sprite):
    def __init__(self, posicion_x, posicion_y, mirando_izquierda):
        super().__init__()
        self.image = esfera_lunar[0]
        self.indice_inicial = 0
        self.rect = self.image.get_rect(center = (posicion_x,posicion_y))
        self.mirando_izquierda = mirando_izquierda
        self.velocidad_proyectil = 12
        self.velocidad_animacion = 0.2

    def animar_imagenes(self):
        if self.indice_inicial >= len(esfera_lunar):
            self.indice_inicial = 0

        if self.mirando_izquierda:
            self.image = esfera_lunar_izquierda[int(self.indice_inicial)]
        else:
            self.image = esfera_lunar[int(self.indice_inicial)]

        self.indice_inicial += self.velocidad_animacion

    def update(self, jugador):
        self.animar_imagenes()  
        if self.mirando_izquierda:
            self.rect.x -= self.velocidad_proyectil
        else:
            self.rect.x += self.velocidad_proyectil

        if jugador.rectangulo_jugador.colliderect(self) and jugador.invulnerabilidad == False:
            jugador.vida_total -= 1
            jugador.daño_recibido = True
        
        if self.rect.x > ANCHO or self.rect.x < -100:
            self.kill()


