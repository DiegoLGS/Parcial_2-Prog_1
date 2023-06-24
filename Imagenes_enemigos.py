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
brujo_caminando_izquierda = girar_imagenes(brujo_caminando,True,False)

brujo_cayendo = [pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Brujo/cayendo/0.png"),
                pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Brujo/cayendo/1.png"),
                pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Brujo/cayendo/2.png")]
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
brujo_muriendo_izquierda = girar_imagenes(brujo_muriendo,True,False)

brujo_lanzando_proyectil = [pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Brujo/lanzando proyectil/7.png"),
                pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Brujo/lanzando proyectil/8.png"),
                pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Brujo/lanzando proyectil/9.png")]
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

#ESPECTRO
espectro_caminando = [pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Espectro/caminando/0.png"),
            pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Espectro/caminando/1.png"),
            pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Espectro/caminando/2.png"),
            pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Espectro/caminando/3.png"),
            pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Espectro/caminando/4.png")]

espectro_cayendo = [pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Espectro/cayendo/0.png")]

espectro_muriendo = [pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Espectro/muriendo/0.png"),
            pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Espectro/muriendo/1.png"),
            pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Espectro/muriendo/2.png"),
            pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Espectro/muriendo/3.png"),
            pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Espectro/muriendo/4.png")]

espectro_lanzando_proyectil = [pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Espectro/lanzando proyectil/0.png"),
                pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Espectro/lanzando proyectil/1.png"),
                pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Espectro/lanzando proyectil/2.png"),
                pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Espectro/lanzando proyectil/3.png"),
                pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Espectro/lanzando proyectil/4.png")]

diccionario_animaciones_espectro = {}
diccionario_animaciones_espectro["caminando"] = espectro_caminando
diccionario_animaciones_espectro["cayendo"] = espectro_cayendo
diccionario_animaciones_espectro["muriendo"] = espectro_muriendo
diccionario_animaciones_espectro["lanzando_proyectil"] = espectro_lanzando_proyectil

#PARCA
parca_caminando_izquierda = [pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Parca/caminando/0.png"),
                pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Parca/caminando/1.png"),
                pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Parca/caminando/2.png"),
                pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Parca/caminando/3.png"),
                pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Parca/caminando/4.png"),
                pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Parca/caminando/5.png")]
parca_caminando = girar_imagenes(parca_caminando_izquierda,True,False)

parca_cayendo_izquierda = [pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Parca/cayendo/0.png")]
parca_cayendo = girar_imagenes(parca_cayendo_izquierda,True,False)

parca_muriendo_izquierda = [pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Parca/muriendo/0.png"),
            pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Parca/muriendo/1.png"),
            pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Parca/muriendo/2.png"),
            pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Parca/muriendo/3.png"),
            pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Parca/muriendo/4.png")]
parca_muriendo = girar_imagenes(parca_muriendo_izquierda,True,False)

parca_atacando_izquierda = [pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Parca/atacando/0.png"),
                pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Parca/atacando/1.png"),
                pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Parca/atacando/2.png"),
                pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Parca/atacando/3.png"),
                pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Parca/atacando/4.png"),
                pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Parca/atacando/5.png"),
                pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Parca/atacando/6.png"),
                pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Parca/atacando/7.png"),
                pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Parca/atacando/8.png"),
                pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Parca/atacando/9.png")]
parca_atacando = girar_imagenes(parca_atacando_izquierda,True,False)

diccionario_animaciones_parca = {}
diccionario_animaciones_parca["caminando"] = parca_caminando
diccionario_animaciones_parca["caminando_izquierda"] = parca_caminando_izquierda
diccionario_animaciones_parca["cayendo"] = parca_cayendo
diccionario_animaciones_parca["cayendo_izquierda"] = parca_cayendo_izquierda
diccionario_animaciones_parca["muriendo"] = parca_muriendo
diccionario_animaciones_parca["muriendo_izquierda"] = parca_muriendo_izquierda
diccionario_animaciones_parca["atacando"] = parca_atacando
diccionario_animaciones_parca["atacando_izquierda"] = parca_atacando_izquierda

#HOMBRE LOBO
hombre_lobo_intro = [pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Hombre Lobo/intro/3.png"),
                pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Hombre Lobo/intro/4.png"),
                pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Hombre Lobo/intro/5.png"),
                pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Hombre Lobo/intro/6.png"),
                pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Hombre Lobo/intro/7.png"),
                pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Hombre Lobo/intro/8.png"),
                pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Hombre Lobo/intro/9.png"),
                pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Hombre Lobo/intro/10.png"),
                pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Hombre Lobo/intro/11.png"),
                pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Hombre Lobo/intro/12.png")]
hombre_lobo_intro = girar_imagenes(hombre_lobo_intro, True, False)
hombre_lobo_intro = reescalar_imagenes(hombre_lobo_intro,(143, 147))

hombre_lobo_caminando = [pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Hombre Lobo/caminando/0.png"),
            pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Hombre Lobo/caminando/1.png"),
            pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Hombre Lobo/caminando/2.png"),
            pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Hombre Lobo/caminando/3.png")]
hombre_lobo_caminando = reescalar_imagenes(hombre_lobo_caminando,(152, 144))
hombre_lobo_caminando_izquierda = girar_imagenes(hombre_lobo_caminando, True, False)

hombre_lobo_cayendo = [pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Hombre Lobo/cayendo/0.png"),
                pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Hombre Lobo/cayendo/1.png"),
                pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Hombre Lobo/cayendo/2.png"),
                pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Hombre Lobo/cayendo/3.png")]
hombre_lobo_cayendo = reescalar_imagenes(hombre_lobo_cayendo,(152, 144))
hombre_lobo_cayendo_izquierda = girar_imagenes(hombre_lobo_cayendo,True, False)

hombre_lobo_muriendo = [pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Hombre Lobo/muriendo/0.png"),
            pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Hombre Lobo/muriendo/1.png"),
            pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Hombre Lobo/muriendo/2.png"),
            pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Hombre Lobo/muriendo/3.png"),
            pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Hombre Lobo/muriendo/4.png"),
            pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Hombre Lobo/muriendo/5.png"),
            pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Hombre Lobo/muriendo/6.png"),
            pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Hombre Lobo/muriendo/7.png"),
            pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Hombre Lobo/muriendo/8.png"),
            pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Hombre Lobo/muriendo/9.png"),
            pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Hombre Lobo/muriendo/10.png"),
            pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Hombre Lobo/muriendo/11.png"),
            pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Hombre Lobo/muriendo/12.png"),
            pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Hombre Lobo/muriendo/13.png"),
            pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Hombre Lobo/muriendo/14.png"),
            pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Hombre Lobo/muriendo/15.png"),
            pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Hombre Lobo/muriendo/16.png"),
            pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Hombre Lobo/muriendo/17.png"),
            pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Hombre Lobo/muriendo/18.png"),
            pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Hombre Lobo/muriendo/19.png")]
hombre_lobo_muriendo = reescalar_imagenes(hombre_lobo_muriendo,(152,144))
hombre_lobo_muriendo_izquierda = girar_imagenes(hombre_lobo_muriendo,True,False)

hombre_lobo_lanzando_proyectil = [pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Hombre Lobo/lanzando proyectil/0.png"),
                pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Hombre Lobo/lanzando proyectil/1.png"),
                pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Hombre Lobo/lanzando proyectil/2.png"),
                pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Hombre Lobo/lanzando proyectil/3.png"),
                pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Hombre Lobo/lanzando proyectil/4.png")]
hombre_lobo_lanzando_proyectil = reescalar_imagenes(hombre_lobo_lanzando_proyectil,(152, 144))
hombre_lobo_lanzando_proyectil_izquierda = girar_imagenes(hombre_lobo_lanzando_proyectil,True, False)

hombre_lobo_saltando = [pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Hombre Lobo/saltando/0.png"),
                pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Hombre Lobo/saltando/1.png")]
hombre_lobo_saltando = reescalar_imagenes(hombre_lobo_saltando,(152, 144))
hombre_lobo_saltando_izquierda = girar_imagenes(hombre_lobo_saltando,True, False)

hombre_lobo_ataque_garra = [pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Hombre Lobo/ataque_garra/0.png"),
                pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Hombre Lobo/ataque_garra/1.png"),
                pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Hombre Lobo/ataque_garra/2.png"),
                pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Hombre Lobo/ataque_garra/3.png"),
                pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Hombre Lobo/ataque_garra/4.png"),
                pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Hombre Lobo/ataque_garra/5.png")]
hombre_lobo_ataque_garra = reescalar_imagenes(hombre_lobo_ataque_garra,(152, 144))
hombre_lobo_ataque_garra_izquierda = girar_imagenes(hombre_lobo_ataque_garra,True, False)

hombre_lobo_regeneracion = [pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Hombre Lobo/regeneracion/0.png"),
                    pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Hombre Lobo/regeneracion/1.png")]
hombre_lobo_regeneracion = reescalar_imagenes(hombre_lobo_regeneracion,(152, 144))
hombre_lobo_regeneracion_izquierda = girar_imagenes(hombre_lobo_regeneracion,True, False)

retrato = pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Hombre Lobo/retrato/0.png")

icono_salud = pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Hombre Lobo/icono salud/0.png")

icono_salud_regeneracion = pygame.image.load("Segundo parcial/Recursos/Enemigos_sprites/Hombre Lobo/icono salud/1.png")

diccionario_animaciones_hombre_lobo = {}
diccionario_animaciones_hombre_lobo["intro"] = hombre_lobo_intro
diccionario_animaciones_hombre_lobo["caminando"] = hombre_lobo_caminando
diccionario_animaciones_hombre_lobo["caminando_izquierda"] = hombre_lobo_caminando_izquierda
diccionario_animaciones_hombre_lobo["cayendo"] = hombre_lobo_cayendo
diccionario_animaciones_hombre_lobo["cayendo_izquierda"] = hombre_lobo_cayendo_izquierda
diccionario_animaciones_hombre_lobo["muriendo"] = hombre_lobo_muriendo
diccionario_animaciones_hombre_lobo["muriendo_izquierda"] = hombre_lobo_muriendo_izquierda
diccionario_animaciones_hombre_lobo["lanzando_proyectil"] = hombre_lobo_lanzando_proyectil
diccionario_animaciones_hombre_lobo["lanzando_proyectil_izquierda"] = hombre_lobo_lanzando_proyectil_izquierda
diccionario_animaciones_hombre_lobo["saltando"] = hombre_lobo_saltando
diccionario_animaciones_hombre_lobo["saltando_izquierda"] = hombre_lobo_saltando_izquierda
diccionario_animaciones_hombre_lobo["ataque_garra"] = hombre_lobo_ataque_garra
diccionario_animaciones_hombre_lobo["ataque_garra_izquierda"] = hombre_lobo_ataque_garra_izquierda
diccionario_animaciones_hombre_lobo["regeneracion"] = hombre_lobo_regeneracion
diccionario_animaciones_hombre_lobo["regeneracion_izquierda"] = hombre_lobo_regeneracion_izquierda
diccionario_animaciones_hombre_lobo["retrato"] = retrato
diccionario_animaciones_hombre_lobo["icono_salud"] = icono_salud
diccionario_animaciones_hombre_lobo["icono_salud_regeneracion"] = icono_salud_regeneracion
