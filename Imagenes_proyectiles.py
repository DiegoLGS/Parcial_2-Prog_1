import pygame
from Girar_reescalar_imagenes import *

cuchillo = [pygame.image.load("Segundo parcial/Recursos/Proyectiles/cuchillo.png")]
cuchillo = reescalar_imagenes(cuchillo,(40,25))
cuchillo_derecha = girar_imagenes(cuchillo,True,False)

lapida = [pygame.image.load("Segundo parcial/Recursos/Proyectiles/lapida_1.png"),
        pygame.image.load("Segundo parcial/Recursos/Proyectiles/lapida_2.png"),
        pygame.image.load("Segundo parcial/Recursos/Proyectiles/lapida_3.png")]

ojo_cometa = [pygame.image.load("Segundo parcial/Recursos/Proyectiles/ojo_cometa_1.png"),
        pygame.image.load("Segundo parcial/Recursos/Proyectiles/ojo_cometa_2.png"),
        pygame.image.load("Segundo parcial/Recursos/Proyectiles/ojo_cometa_3.png"),
        pygame.image.load("Segundo parcial/Recursos/Proyectiles/ojo_cometa_4.png"),
        pygame.image.load("Segundo parcial/Recursos/Proyectiles/ojo_cometa_5.png"),
        pygame.image.load("Segundo parcial/Recursos/Proyectiles/ojo_cometa_6.png"),
        pygame.image.load("Segundo parcial/Recursos/Proyectiles/ojo_cometa_7.png")]
ojo_cometa = girar_imagenes(ojo_cometa , False, True)

