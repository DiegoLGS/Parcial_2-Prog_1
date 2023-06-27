import pygame
from Imagenes_items import pocion_chica
from Sonidos import sonido_pocion

class Pocion_chica(pygame.sprite.Sprite):
    def __init__(self, coordenadas):
        super().__init__()
        self.image = pocion_chica[0]
        self.coordenadas = coordenadas
        self.rect = self.image.get_rect(center = (self.coordenadas))
        self.sonido = sonido_pocion

    def update(self, pantalla, jugador):
        pantalla.blit(self.image, self.coordenadas)

        if jugador.rectangulo_jugador.colliderect(self.rect):
            jugador.vida_total += 1
            self.sonido.play()
            self.kill()