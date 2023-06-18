import pygame
from Girar_reescalar_imagenes import *

#ZOMBIE
zombie_caminando = [pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Zombie/caminando/0.png"),
            pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Zombie/caminando/1.png"),
            pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Zombie/caminando/2.png"),
            pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Zombie/caminando/3.png"),
            pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Zombie/caminando/4.png")]
zombie_caminando = reescalar_imagenes(zombie_caminando,(70,70))
zombie_caminando_izquierda = girar_imagenes(zombie_caminando,True,False)

zombie_cayendo = [pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Zombie/cayendo/0.png")]
zombie_cayendo = reescalar_imagenes(zombie_cayendo,(70,70))
zombie_cayendo_izquierda = girar_imagenes(zombie_cayendo,True,False)

zombie_muriendo = [pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Zombie/muriendo/0.png"),
            pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Zombie/muriendo/1.png"),
            pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Zombie/muriendo/2.png"),
            pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Zombie/muriendo/3.png")]
zombie_muriendo = reescalar_imagenes(zombie_muriendo,(70,70))
zombie_muriendo_izquierda = girar_imagenes(zombie_muriendo,True,False)

diccionario_animaciones_zombie = {}
diccionario_animaciones_zombie["caminando"] = zombie_caminando
diccionario_animaciones_zombie["caminando_izquierda"] = zombie_caminando_izquierda
diccionario_animaciones_zombie["cayendo"] = zombie_cayendo
diccionario_animaciones_zombie["cayendo_izquierda"] = zombie_cayendo_izquierda
diccionario_animaciones_zombie["muriendo"] = zombie_muriendo
diccionario_animaciones_zombie["muriendo_izquierda"] = zombie_muriendo_izquierda