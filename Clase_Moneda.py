import pygame
from Imagenes_items import moneda

class Moneda(pygame.sprite.Sprite):
    def __init__(self, coordenadas):
        super().__init__()
        self.image = moneda[0]
        self.coordenadas = coordenadas
        self.rect = self.image.get_rect(center = (self.coordenadas))

    def update(self, pantalla, jugador):
        pantalla.blit(self.image, self.coordenadas)

        if jugador.rectangulo_jugador.colliderect(self.rect):
            jugador.puntaje += 100
            self.kill()