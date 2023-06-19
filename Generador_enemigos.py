import pygame
from Clase_Zombie import Zombie

class Generador_enemigos():
    def __init__(self):
        self.ultima_creacion = 0

    def generar_enemigo(self,grupo_enemigos):
        tiempo_actual = pygame.time.get_ticks()
        tiempo_transcurrido = tiempo_actual - self.ultima_creacion

        if tiempo_transcurrido >= 4000:   
            self.ultima_creacion = tiempo_actual
            grupo_enemigos.add(Zombie())

