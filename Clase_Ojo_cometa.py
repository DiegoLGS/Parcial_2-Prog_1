import pygame
from Imagenes_proyectiles import ojo_cometa
from Sonidos import sonido_ojo_cometa
ALTO = 700

class Ojo_cometa(pygame.sprite.Sprite):
    def __init__(self, jugador_posicion_x):
        super().__init__()
        self.image = ojo_cometa[0]
        self.indice_inicial = 0
        self.rect = self.image.get_rect(center = (jugador_posicion_x, 0))
        self.velocidad_proyectil = 7
        self.velocidad_animacion = 0.2
        self.sonido = sonido_ojo_cometa
        self.sonido.play()

    def animar_imagenes(self):
        if self.indice_inicial >= len(ojo_cometa):
            self.indice_inicial = 0
        self.image = ojo_cometa[int(self.indice_inicial)]
        self.indice_inicial += self.velocidad_animacion

    def update(self,jugador):
        self.animar_imagenes()       
        self.rect.y += self.velocidad_proyectil
        
        if jugador.rectangulo_jugador.colliderect(self) and jugador.invulnerabilidad == False:
            jugador.vida_total -= 1
            jugador.daño_recibido = True
        
        if self.rect.y > ALTO or self.rect.x < -100:
            self.kill()


