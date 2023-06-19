import pygame
import math

class Trampa_giratoria(pygame.sprite.Sprite):
    def __init__(self,posicion_x,posicion_y):
        super().__init__()
        self.posicion = {"x":posicion_x ,"y":posicion_y}
        self.image = pygame.image.load("Segundo parcial/Recursos/Trampas/0.png")
        self.rect = self.image.get_rect(topleft=(self.posicion["x"],self.posicion["y"]))
        self.angulo = 0

    def update(self):       
        self.superficie_actual = pygame.transform.rotate(self.image, self.angulo)
        self.rect = self.superficie_actual.get_rect(center = self.rect.center)
        self.imagen_girando = pygame.transform.rotate(self.image, self.angulo)
        self.angulo -= 4