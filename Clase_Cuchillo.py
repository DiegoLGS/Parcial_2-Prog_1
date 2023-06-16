import pygame
from Proyectiles import cuchillo, cuchillo_derecha
ANCHO = 1000

class Cuchillo(pygame.sprite.Sprite):
    def __init__(self, posicion_x, posicion_y, mirando_izquierda):
        super().__init__()
        self.image = cuchillo[0]
        self.rect = self.image.get_rect(center = (posicion_x,posicion_y))
        self.mirando_izquierda = mirando_izquierda
        self.velocidad_cuchillo = 12

    def update(self):
        if self.mirando_izquierda:
            self.rect.x -= self.velocidad_cuchillo
        else:
            self.image = cuchillo_derecha[0]
            self.rect.x += self.velocidad_cuchillo
        
        if self.rect.x > ANCHO or self.rect.x < -100:
            self.kill()