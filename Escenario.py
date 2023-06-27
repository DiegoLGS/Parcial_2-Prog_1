import pygame
from Clase_Jugador import Jugador
from Clase_Nivel import Nivel

BLANCO = (255,255,255)
NEGRO = (0,0,0)
ROJO = (255,0,0)
AZUL = (0,0,255)
VERDE = (0,255,0)
AZUL_CLARO = (0,150,255)

ANCHO = 1000
ALTO = 700

pygame.init()

jugador = Jugador()

niveles = [
    Nivel(1,
        coordenadas_monedas = [(400, 580), (500, 580), (600, 580), (700, 580), (600, 400), (700, 400), (800, 400), (200, 300), (250, 200), (450, 200), (650, 200)],
        coordenadas_pocion_chica = [(170, 220), (550, 250)],
        coordenadas_trampas = [(710, 290), (120, 290)],
        imagen_escenario = pygame.image.load("Segundo parcial/Recursos/Escenarios/0.png"),
        imagen_plataforma = pygame.image.load("Segundo parcial/Recursos/Plataformas/1.png"),
        coordenadas_plataformas = [(100, 400), (400, 300), (600, 450),],
        musica = "Segundo parcial/Recursos/Musica/Bloody_tears.mp3"
    ),
    Nivel(2,
        coordenadas_monedas = [(350, 480), (350, 380), (350, 240), (500, 180), (600, 500), (700, 400), (800, 180), (200, 200), (250, 250), (500, 300), (600, 300)],
        coordenadas_pocion_chica = [(900, 600), (700, 250), (180, 100)],
        coordenadas_trampas = [(660, 300), (350, 600)],
        imagen_escenario = pygame.image.load("Segundo parcial/Recursos/Escenarios/1.png"),
        imagen_plataforma = pygame.image.load("Segundo parcial/Recursos/Plataformas/0.png"),
        coordenadas_plataformas = [(280, 280), (590, 350), (750, 550)],
        musica = "Segundo parcial/Recursos/Musica/Reincarnated_souls.mp3"
    ),
    Nivel(3,
        coordenadas_monedas = [(300, 600), (400, 600),(500, 600), (600, 600) ],
        coordenadas_pocion_chica = [(300, 400), (700, 400)],
        coordenadas_trampas = [(420,500)],
        imagen_escenario = pygame.image.load("Segundo parcial/Recursos/Escenarios/2.png"),
        imagen_plataforma = pygame.image.load("Segundo parcial/Recursos/Plataformas/0.png"),
        coordenadas_plataformas = [],
        musica = "Segundo parcial/Recursos/Musica/Dominate.mp3"
    )
]
fuente = pygame.font.SysFont("garamond",30)

nivel_actual = 2

def Iniciar(PANTALLA):
    global nivel_actual
    nivel = niveles[nivel_actual]


    if nivel.numero < len(niveles):
        nivel.actualizar(PANTALLA, jugador, 3000)
    else:        
        nivel.actualizar(PANTALLA, jugador, 0)
        jugador.nivel_final(True)        
    
        if nivel.numero == len(niveles) and nivel.cronometro.tiempo_restante == 60 and jugador.bloqueo_teclado == False: 
            jugador.bloqueo_teclado = True
            jugador.estado_actual = "parado"
            jugador.mirando_izquierda = False
            aullido = pygame.mixer.Sound("Segundo parcial/Recursos/Sonidos/Boss/aullido_lobo.mp3")
            aullido.play()

    if nivel.reproduciendo_musica == False:
        nivel.cargar_musica()
        nivel.reproduciendo_musica = True

    if nivel.generador_de_enemigos.enemigos_creados >= 6 and len(nivel.grupo_enemigos) == 0 and not nivel.nivel_finalizado:
        nivel.cronometro.detenido = True
        nivel.nivel_finalizado = True
        print("NIVEL", nivel.numero, "FINALIZADO")
        print(f"Tiempo restante: {nivel.cronometro.tiempo_restante}")
        jugador.puntaje += nivel.cronometro.tiempo_restante * 100
        jugador.posicion = {"x": 100, "y": 570}
        if nivel.numero < len(niveles):
            nivel_actual += 1 
            
    
    nivel.cronometro.actualizar()
    nivel.cronometro.mostrar_tiempo(PANTALLA)
    jugador.grupo_cuchillos.update()    
    jugador.grupo_cuchillos.draw(PANTALLA)   
    jugador.mostrar_salud(PANTALLA)  
    jugador.actualizar()            
    display_puntuacion = fuente.render("Puntaje: " + str(jugador.puntaje), False, BLANCO)
    PANTALLA.blit(jugador.imagen, jugador.rectangulo_jugador)
    PANTALLA.blit(jugador.retrato, (20, 20))
    PANTALLA.blit(display_puntuacion, (800, 50))

    for numero_canal in range(pygame.mixer.get_num_channels()):
                    canal = pygame.mixer.Channel(numero_canal)
                    canal.set_volume(0.2)

