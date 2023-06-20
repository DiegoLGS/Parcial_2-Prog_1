import pygame
from Clase_Zombie import Zombie
from Clase_Brujo import Brujo
import random

class Generador_enemigos():
    def __init__(self):
        self.ultima_creacion = 0
        self.enemigos_creados = 0

    def generar_enemigo(self,grupo_enemigos,jugador):
        tiempo_actual = pygame.time.get_ticks()
        tiempo_transcurrido = tiempo_actual - self.ultima_creacion

        if tiempo_transcurrido >= 3000:   
            self.ultima_creacion = tiempo_actual
            numero_random = random.randint(0, 1)
            if numero_random:
                grupo_enemigos.add(Zombie())
            else:
                grupo_enemigos.add(Brujo(jugador))
            self.enemigos_creados += 1


