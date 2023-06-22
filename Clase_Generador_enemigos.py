import pygame
from Clase_Zombie import Zombie
from Clase_Brujo import Brujo
from Clase_Espectro import Espectro
from Clase_Parca import Parca
import random

class Generador_enemigos():
    def __init__(self):
        self.ultima_creacion = 0
        self.enemigos_creados = 0

    def generar_enemigo(self, nivel, grupo_enemigos, jugador):
        tiempo_actual = pygame.time.get_ticks()
        tiempo_transcurrido = tiempo_actual - self.ultima_creacion

        if tiempo_transcurrido >= 3000:   
            self.ultima_creacion = tiempo_actual
            match nivel:
                case 1:
                    grupo_enemigos.add(Zombie())
                    grupo_enemigos.add(Brujo(jugador))

                case 2:
                    grupo_enemigos.add(Parca())
                    grupo_enemigos.add(Espectro(jugador))

            self.enemigos_creados += 1


