import pygame
from Girar_reescalar_imagenes import *

cuchillo = [pygame.image.load("Segundo parcial/Recursos/Proyectiles/cuchillo.png")]
cuchillo = reescalar_imagenes(cuchillo,(40,25))
cuchillo_derecha = girar_imagenes(cuchillo,True,False)

lapida = [pygame.image.load("Segundo parcial/Recursos/Proyectiles/lapida 1.png"),
        pygame.image.load("Segundo parcial/Recursos/Proyectiles/lapida 2.png"),
        pygame.image.load("Segundo parcial/Recursos/Proyectiles/lapida 3.png")]
#lapida = reescalar_imagenes(lapida,(40,25))
#lapida_derecha = girar_imagenes(lapida,True,False)

