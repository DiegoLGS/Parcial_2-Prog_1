import pygame

class Trampa_escondida(pygame.sprite.Sprite):
    def __init__(self, coordenadas):
        super().__init__()
        self.lista_imagenes = [pygame.image.load("Segundo parcial/Recursos/Trampas/Escondida/0.png"),
                            pygame.image.load("Segundo parcial/Recursos/Trampas/Escondida/1.png"),
                            pygame.image.load("Segundo parcial/Recursos/Trampas/Escondida/2.png"),
                            pygame.image.load("Segundo parcial/Recursos/Trampas/Escondida/3.png"),
                            pygame.image.load("Segundo parcial/Recursos/Trampas/Escondida/4.png"),
                            pygame.image.load("Segundo parcial/Recursos/Trampas/Escondida/5.png"),
                            pygame.image.load("Segundo parcial/Recursos/Trampas/Escondida/6.png"),
                            pygame.image.load("Segundo parcial/Recursos/Trampas/Escondida/7.png"),
                            pygame.image.load("Segundo parcial/Recursos/Trampas/Escondida/8.png")]
        self.image = self.lista_imagenes[0]
        self.coordenadas = coordenadas
        self.rect = self.image.get_rect(topleft = (self.coordenadas))
        self.indice_inicial = 0
        self.tiempo_actual = pygame.time.get_ticks()
        self.tiempo_ultima_activacion = self.tiempo_actual
        self.tiempo_espera_activacion = 3000
        self.trampa_activa = False  
        self.velocidad_animacion = 0.2        

    def update(self, pantalla, jugador):             
        if self.tiempo_actual - self.tiempo_ultima_activacion >= self.tiempo_espera_activacion:
            self.tiempo_ultima_activacion = self.tiempo_actual
            self.trampa_activa = True
            
        if self.trampa_activa == True:            
            if self.indice_inicial >= len(self.lista_imagenes):
                self.indice_inicial = 0
                self.trampa_activa = False
            self.image = self.lista_imagenes[int(self.indice_inicial)]
            self.indice_inicial += self.velocidad_animacion

        pantalla.blit(self.image, self.rect)
        self.tiempo_actual = pygame.time.get_ticks()

        if not jugador.invulnerabilidad and self.trampa_activa == True:
            if self.rect.colliderect(jugador.rectangulo_jugador):
                jugador.vida_total -= 1
                jugador.daño_recibido = True