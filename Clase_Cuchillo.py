import pygame
from Proyectiles import cuchillo
from Obtener_rectangulos import obtener_rectangulos

class Cuchillo(pygame.sprite.Sprite):
    def __init__(self, posicion_x, posicion_y, mirando_izquierda):
        super().__init__()
        self.image = cuchillo[0]
        self.rect = self.image.get_rect(center = (posicion_x,posicion_y))
        self.rectangulos_lados = obtener_rectangulos(self.rect)
        self.mirando_izquierda = mirando_izquierda

    def update(self):
        if self.mirando_izquierda:
            self.rect.x -= 5
        else:
            self.rect.x += 5
        
        if self.rect.x > 800 or self.rect.x < -800:
            self.kill()