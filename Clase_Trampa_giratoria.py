import pygame

class Trampa_giratoria(pygame.sprite.Sprite):
    def __init__(self, coordenadas):
        super().__init__()
        self.image = pygame.image.load("Segundo parcial/Recursos/Trampas/Giratoria/0.png")
        self.coordenadas = coordenadas
        self.rect = self.image.get_rect(topleft = (self.coordenadas))
        self.angulo = 0

    def update(self, pantalla, jugador):       
        self.superficie_actual = pygame.transform.rotate(self.image, self.angulo)
        self.rect = self.superficie_actual.get_rect(center = self.rect.center)
        self.imagen_girando = pygame.transform.rotate(self.image, self.angulo)
        self.angulo -= 4
        pantalla.blit(self.imagen_girando , self.rect)

        if jugador.invulnerabilidad == False:
            if self.rect.colliderect(jugador.rectangulo_jugador):
                jugador.vida_total -= 1
                jugador.daño_recibido = True