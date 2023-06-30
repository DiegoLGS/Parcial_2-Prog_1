import pygame
BLANCO = (255,255,255)

class Cronometro:
    def __init__(self, tiempo_inicial):
        self.tiempo_restante = tiempo_inicial
        self.fuente = pygame.font.SysFont("garamond", 30)
        self.reloj = pygame.time.Clock()
        self.tiempo_actual = pygame.time.get_ticks()
        self.detenido = False

    def actualizar(self):
        if self.detenido == False:
            tiempo_transcurrido = pygame.time.get_ticks() - self.tiempo_actual
            if tiempo_transcurrido >= 1000: 
                self.tiempo_actual = pygame.time.get_ticks()
                if self.tiempo_restante > 0:
                    self.tiempo_restante -= 1    

    def mostrar_tiempo(self, pantalla):
        display_tiempo = self.fuente.render(str(self.tiempo_restante), False, BLANCO)
        pantalla.blit(display_tiempo, (500, 50))
