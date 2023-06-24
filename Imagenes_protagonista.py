import pygame
from Girar_reescalar_imagenes import *

parado = [pygame.image.load("Segundo parcial/Recursos/Alucard_sprites/parado/2.png")]
parado = reescalar_imagenes(parado,(45,81))
parado_izquierda = girar_imagenes(parado,True,False)

caminando = [pygame.image.load("Segundo parcial/Recursos/Alucard_sprites/caminando/1.png"),
            pygame.image.load("Segundo parcial/Recursos/Alucard_sprites/caminando/2.png"),
            pygame.image.load("Segundo parcial/Recursos/Alucard_sprites/caminando/3.png"),
            pygame.image.load("Segundo parcial/Recursos/Alucard_sprites/caminando/4.png"),
            pygame.image.load("Segundo parcial/Recursos/Alucard_sprites/caminando/5.png"),
            pygame.image.load("Segundo parcial/Recursos/Alucard_sprites/caminando/6.png")]
caminando = reescalar_imagenes(caminando,(59,71))
caminando_izquierda = girar_imagenes(caminando,True,False)

saltando = [pygame.image.load("Segundo parcial/Recursos/Alucard_sprites/saltando/24.png"),
            pygame.image.load("Segundo parcial/Recursos/Alucard_sprites/saltando/25.png")]
saltando = reescalar_imagenes(saltando,(69,73))
saltando_izquierda = girar_imagenes(saltando,True,False)

cayendo = [pygame.image.load("Segundo parcial/Recursos/Alucard_sprites/cayendo/27.png"),
            pygame.image.load("Segundo parcial/Recursos/Alucard_sprites/cayendo/28.png")]
cayendo = reescalar_imagenes(cayendo,(74,68))
cayendo_izquierda = girar_imagenes(cayendo,True,False)

lanzando_proyectil = [pygame.image.load("Segundo parcial/Recursos/Alucard_sprites/lanzando proyectil/62.png"),
                    pygame.image.load("Segundo parcial/Recursos/Alucard_sprites/lanzando proyectil/63.png"),
                    pygame.image.load("Segundo parcial/Recursos/Alucard_sprites/lanzando proyectil/64.png"),
                    pygame.image.load("Segundo parcial/Recursos/Alucard_sprites/lanzando proyectil/63.png")]
lanzando_proyectil = reescalar_imagenes(lanzando_proyectil,(56,78))
lanzando_proyectil_izquierda = girar_imagenes(lanzando_proyectil,True,False)

parado_viento = [pygame.image.load("Segundo parcial/Recursos/Alucard_sprites/parado viento/0.png"),
                    pygame.image.load("Segundo parcial/Recursos/Alucard_sprites/parado viento/1.png"),
                    pygame.image.load("Segundo parcial/Recursos/Alucard_sprites/parado viento/2.png"),
                    pygame.image.load("Segundo parcial/Recursos/Alucard_sprites/parado viento/3.png"),
                    pygame.image.load("Segundo parcial/Recursos/Alucard_sprites/parado viento/4.png"),
                    pygame.image.load("Segundo parcial/Recursos/Alucard_sprites/parado viento/5.png"),
                    pygame.image.load("Segundo parcial/Recursos/Alucard_sprites/parado viento/6.png")]
parado_viento = reescalar_imagenes(parado_viento,(64,76))
parado_viento_izquierda = girar_imagenes(parado_viento,True,False)

muriendo = [pygame.image.load("Segundo parcial/Recursos/Alucard_sprites/muriendo/0.png"),
            pygame.image.load("Segundo parcial/Recursos/Alucard_sprites/muriendo/1.png"),
            pygame.image.load("Segundo parcial/Recursos/Alucard_sprites/muriendo/2.png"),
            pygame.image.load("Segundo parcial/Recursos/Alucard_sprites/muriendo/3.png"),
            pygame.image.load("Segundo parcial/Recursos/Alucard_sprites/muriendo/4.png"),
            pygame.image.load("Segundo parcial/Recursos/Alucard_sprites/muriendo/5.png")]
muriendo = reescalar_imagenes(muriendo,(56,78))
muriendo_izquierda = girar_imagenes(muriendo,True,False)

retrato = pygame.image.load("Segundo parcial/Recursos/Alucard_sprites/retrato/0.png")

icono_salud = pygame.image.load("Segundo parcial/Recursos/Alucard_sprites/icono salud/0.png")

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
diccionario_animaciones["retrato"] = retrato
diccionario_animaciones["icono_salud"] = icono_salud
diccionario_animaciones["parado_viento"] = parado_viento
diccionario_animaciones["parado_viento_izquierda"] = parado_viento_izquierda
diccionario_animaciones["muriendo"] = muriendo
diccionario_animaciones["muriendo_izquierda"] = muriendo_izquierda