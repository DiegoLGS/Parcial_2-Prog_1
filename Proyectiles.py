import pygame
from Girar_reescalar_imagenes import *

cuchillo = [pygame.image.load("Segundo parcial/Recursos/Proyectiles/cuchillo.png")]
cuchillo = reescalar_imagenes(cuchillo,(40,25))
cuchillo_izquierda = girar_imagenes(cuchillo,True,False)

