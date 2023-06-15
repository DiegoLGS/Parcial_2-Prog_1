import pygame
from Girar_reescalar_imagenes import girar_imagenes


parado = [pygame.image.load("Segundo parcial/Recursos/Alucard_sprites/parado/2.png")]

parado_izquierda = girar_imagenes(parado,True,False)

caminando = [pygame.image.load("Segundo parcial/Recursos/Alucard_sprites/caminando/1.png"),
            pygame.image.load("Segundo parcial/Recursos/Alucard_sprites/caminando/2.png"),
            pygame.image.load("Segundo parcial/Recursos/Alucard_sprites/caminando/3.png"),
            pygame.image.load("Segundo parcial/Recursos/Alucard_sprites/caminando/4.png"),
            pygame.image.load("Segundo parcial/Recursos/Alucard_sprites/caminando/5.png"),
            pygame.image.load("Segundo parcial/Recursos/Alucard_sprites/caminando/6.png")]

caminando_izquierda = girar_imagenes(caminando,True,False)

saltando = [pygame.image.load("Segundo parcial/Recursos/Alucard_sprites/saltando/24.png"),
            pygame.image.load("Segundo parcial/Recursos/Alucard_sprites/saltando/25.png")]

saltando_izquierda = girar_imagenes(saltando,True,False)

cayendo = [pygame.image.load("Segundo parcial/Recursos/Alucard_sprites/cayendo/27.png"),
            pygame.image.load("Segundo parcial/Recursos/Alucard_sprites/cayendo/28.png")]

cayendo_izquierda = girar_imagenes(cayendo,True,False)

lanzando_proyectil = [pygame.image.load("Segundo parcial/Recursos/Alucard_sprites/lanzando proyectil/62.png"),
                    pygame.image.load("Segundo parcial/Recursos/Alucard_sprites/lanzando proyectil/63.png"),
                    pygame.image.load("Segundo parcial/Recursos/Alucard_sprites/lanzando proyectil/64.png")]

lanzando_proyectil_izquierda = girar_imagenes(lanzando_proyectil,True,False)

diccionario_animaciones = {}
diccionario_animaciones["parado"] = parado
diccionario_animaciones["parado_izquierda"] = parado_izquierda
diccionario_animaciones["caminando"] = caminando
diccionario_animaciones["caminando_izquierda"] = caminando_izquierda
diccionario_animaciones["saltando"] = saltando
diccionario_animaciones["saltando_izquierda"] = saltando_izquierda
diccionario_animaciones["cayendo"] = cayendo
diccionario_animaciones["cayendo_izquierda"] = cayendo_izquierda
diccionario_animaciones["lanzando_proyectil"] = lanzando_proyectil
diccionario_animaciones["lanzando_proyectil_izquierda"] = lanzando_proyectil_izquierda