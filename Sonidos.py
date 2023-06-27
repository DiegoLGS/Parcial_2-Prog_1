import pygame
pygame.mixer.init()

#ITEMS
sonido_moneda = pygame.mixer.Sound("Segundo parcial/Recursos/Sonidos/Items/moneda.wav")
sonido_pocion = pygame.mixer.Sound("Segundo parcial/Recursos/Sonidos/Items/pocion.wav")

#ALUCARD
sonidos_jugador_herida = pygame.mixer.Sound("Segundo parcial/Recursos/Sonidos/Alucard/herida.wav")

#PROYECTILES
sonido_lapida = pygame.mixer.Sound("Segundo parcial/Recursos/Sonidos/Proyectiles/lapida_impacto.wav")
sonido_cuchillo = pygame.mixer.Sound("Segundo parcial/Recursos/Sonidos/Proyectiles/cuchillo_impacto.wav") 
sonido_esfera_lunar = pygame.mixer.Sound("Segundo parcial/Recursos/Sonidos/Proyectiles/esfera_lunar.wav") 
sonido_ojo_cometa = pygame.mixer.Sound("Segundo parcial/Recursos/Sonidos/Proyectiles/ojo_cometa.wav") 

#ARMAS
sonido_guadaña =  pygame.mixer.Sound("Segundo parcial/Recursos/Sonidos/Armas/guadaña_impacto.wav") 

#ENEMIGOS
sonido_hombre_lobo_saltando = pygame.mixer.Sound("Segundo parcial/Recursos/Sonidos/Boss/hombre_lobo_saltando.wav") 
sonido_hombre_lobo_regenerandose = pygame.mixer.Sound("Segundo parcial/Recursos/Sonidos/Boss/hombre_lobo_regenerandose.wav") 
sonido_hombre_lobo_regeneracion = pygame.mixer.Sound("Segundo parcial/Recursos/Sonidos/Boss/hombre_lobo_regeneracion.wav") 
sonido_hombre_lobo_ataque_garra = pygame.mixer.Sound("Segundo parcial/Recursos/Sonidos/Boss/hombre_lobo_ataque_garra.wav") 