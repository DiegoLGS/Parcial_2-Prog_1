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

#BRUJO
brujo_caminando = [pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Brujo/caminando/0.png"),
            pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Brujo/caminando/1.png"),
            pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Brujo/caminando/2.png")]
#brujo_caminando = reescalar_imagenes(brujo_caminando,(70,70))
brujo_caminando_izquierda = girar_imagenes(brujo_caminando,True,False)

brujo_cayendo = [pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Brujo/cayendo/0.png"),
                pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Brujo/cayendo/1.png"),
                pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Brujo/cayendo/2.png")]
#brujo_cayendo = reescalar_imagenes(brujo_cayendo,(70,70))
brujo_cayendo_izquierda = girar_imagenes(brujo_cayendo,True,False)

brujo_muriendo = [pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Brujo/muriendo/12.png"),
            pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Brujo/muriendo/13.png"),
            pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Brujo/muriendo/14.png"),
            pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Brujo/muriendo/15.png"),
            pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Brujo/muriendo/16.png"),
            pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Brujo/muriendo/17.png"),
            pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Brujo/muriendo/18.png"),
            pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Brujo/muriendo/19.png"),
            pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Brujo/muriendo/20.png"),
            pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Brujo/muriendo/21.png"),]
#brujo_muriendo = reescalar_imagenes(brujo_muriendo,(70,70))
brujo_muriendo_izquierda = girar_imagenes(brujo_muriendo,True,False)

brujo_lanzando_proyectil = [pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Brujo/lanzando proyectil/7.png"),
                pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Brujo/lanzando proyectil/8.png"),
                pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Brujo/lanzando proyectil/9.png")]
#brujo_lanzando_proyectil = reescalar_imagenes(brujo_lanzando_proyectil,(70,70))
brujo_lanzando_proyectil_izquierda = girar_imagenes(brujo_lanzando_proyectil,True,False)

diccionario_animaciones_brujo = {}
diccionario_animaciones_brujo["caminando"] = brujo_caminando
diccionario_animaciones_brujo["caminando_izquierda"] = brujo_caminando_izquierda
diccionario_animaciones_brujo["cayendo"] = brujo_cayendo
diccionario_animaciones_brujo["cayendo_izquierda"] = brujo_cayendo_izquierda
diccionario_animaciones_brujo["muriendo"] = brujo_muriendo
diccionario_animaciones_brujo["muriendo_izquierda"] = brujo_muriendo_izquierda
diccionario_animaciones_brujo["lanzando_proyectil"] = brujo_lanzando_proyectil
diccionario_animaciones_brujo["lanzando_proyectil_izquierda"] = brujo_lanzando_proyectil_izquierda