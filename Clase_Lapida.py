import pygame
from Imagenes_proyectiles import lapida
import math
import random
from Sonidos import sonido_lapida
ANCHO = 1000

class Lapida(pygame.sprite.Sprite):
    def __init__(self, posicion_x, posicion_y, mirando_izquierda, jugador_posicion_x, jugador_posicion_y):
        super().__init__()
        self.image = lapida[random.randint(0, 2)]
        self.rect = self.image.get_rect(center = (posicion_x,posicion_y))
        self.mirando_izquierda = mirando_izquierda
        self.velocidad_proyectil = 7
        self.jugador_posicion_x = jugador_posicion_x
        self.jugador_posicion_y = jugador_posicion_y
        self.tiempo_vida = 1500
        self.tiempo_actual = pygame.time.get_ticks()
        self.sonido = sonido_lapida

    def update(self,jugador):
        if self.mirando_izquierda:
            self.rect.x -= self.velocidad_proyectil
        else:
            self.rect.x += self.velocidad_proyectil

        direccion_x = self.jugador_posicion_x - self.rect.x
        direccion_y = self.jugador_posicion_y - self.rect.y

        magnitud = math.sqrt(direccion_x**2 + direccion_y**2)
        if magnitud != 0:
            direccion_x /= magnitud
            direccion_y /= magnitud

        self.rect.x += direccion_x * self.velocidad_proyectil
        self.rect.y += direccion_y * self.velocidad_proyectil

        if jugador.rectangulo_jugador.colliderect(self) and jugador.invulnerabilidad == False:
            self.sonido.play()
            jugador.vida_total -= 1
            jugador.daño_recibido = True

        if self.rect.x > ANCHO or self.rect.x < -100 or pygame.time.get_ticks() - self.tiempo_actual >= self.tiempo_vida:
            self.kill()

