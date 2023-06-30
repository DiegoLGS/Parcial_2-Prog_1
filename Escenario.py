import pygame, sys
from Clase_Jugador import Jugador
from Clase_Nivel import Nivel
from GUI_form_menu_pausa import FormMenuPausa
from GUI_form_menu_seleccion_nivel import FormMenuSeleccionNivel
from GUI_form_menu_guardar_nombre import FormMenuGuardarNombre
from Clase_Base_de_datos import Base_de_datos


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
pantalla = pygame.display.set_mode((ANCHO, ALTO))

menu_pausa = FormMenuPausa(pantalla, 50, 100, 900, 350, "Black", "Red", 5, True)
menu_nivel = FormMenuSeleccionNivel(pantalla, 50, 100, 900, 350, "Black", "Red", 5, True)
menu_guardar_nombre = FormMenuGuardarNombre(pantalla, 50, 100, 900, 350, "Black", "Blue", 5, True)

fuente = pygame.font.SysFont("garamond",30)

def Iniciar(PANTALLA):
    while menu_nivel.nivel_comenzado == False:
        pygame.mixer.music.stop()
        eventos = pygame.event.get()
        for event in eventos:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()                   

        menu_nivel.update(eventos)     
        pygame.display.update()

        match menu_nivel.nivel_seleccionado:
            case 1:
                menu_nivel.intancia_nivel = Nivel(1,
                coordenadas_monedas = [(400, 580), (500, 580), (600, 580), (700, 580), (600, 400), (700, 400), (800, 400), (200, 300), (250, 200), (450, 200),  (650, 200)],
                coordenadas_pocion_chica = [(170, 220), (550, 250)],
                coordenadas_trampas = [(710, 290), (120, 290)],
                imagen_escenario = pygame.image.load("Segundo parcial/Recursos/Escenarios/0.png"),
                imagen_plataforma = pygame.image.load("Segundo parcial/Recursos/Plataformas/1.png"),
                coordenadas_plataformas = [(100, 400), (400, 300), (600, 450),],
                musica = "Segundo parcial/Recursos/Musica/Bloody_tears.mp3")
                
            case 2:
                menu_nivel.intancia_nivel = Nivel(2,
                coordenadas_monedas = [(350, 480), (350, 380), (350, 240), (500, 180), (600, 500), (700, 400), (800, 180), (200, 200), (250, 250), (500, 300), (600, 300)],
                coordenadas_pocion_chica = [(900, 600), (700, 250), (180, 100)],
                coordenadas_trampas = [(660, 300), (350, 600)],
                imagen_escenario = pygame.image.load("Segundo parcial/Recursos/Escenarios/1.png"),
                imagen_plataforma = pygame.image.load("Segundo parcial/Recursos/Plataformas/0.png"),
                coordenadas_plataformas = [(280, 280), (590, 350), (720, 550)],
                musica = "Segundo parcial/Recursos/Musica/Reincarnated_souls.mp3")
                
            case 3:
                menu_nivel.intancia_nivel = Nivel(3,
                coordenadas_monedas = [(300, 600), (400, 600),(500, 600), (600, 600) ],
                coordenadas_pocion_chica = [(300, 400), (700, 400)],
                coordenadas_trampas = [(420,500)],
                imagen_escenario = pygame.image.load("Segundo parcial/Recursos/Escenarios/2.png"),
                imagen_plataforma = pygame.image.load("Segundo parcial/Recursos/Plataformas/0.png"),
                coordenadas_plataformas = [],
                musica = "Segundo parcial/Recursos/Musica/Dominate.mp3")         

    if menu_nivel.intancia_nivel.numero < 3:
        menu_nivel.intancia_nivel.actualizar(PANTALLA, jugador, 3000)
    else:        
        menu_nivel.intancia_nivel.actualizar(PANTALLA, jugador, 0)
        jugador.nivel_final(True)        
    
        if menu_nivel.intancia_nivel.numero == 3 and menu_nivel.intancia_nivel.cronometro.tiempo_restante == 70 and jugador.bloqueo_teclado == False: 
            jugador.potencia_salto = 0
            jugador.estado_actual = "parado"
            jugador.posicion = {"x": 100, "y": 570}
            jugador.mirando_izquierda = False
            jugador.bloqueo_teclado = True
            aullido = pygame.mixer.Sound("Segundo parcial/Recursos/Sonidos/Boss/aullido_lobo.mp3")
            aullido.play()

    if menu_nivel.intancia_nivel.reproduciendo_musica == False:
        menu_nivel.intancia_nivel.cargar_musica()
        menu_nivel.intancia_nivel.reproduciendo_musica = True    

    if menu_nivel.intancia_nivel.generador_de_enemigos.enemigos_creados >= menu_nivel.intancia_nivel.limite_generador_enemigos and len(menu_nivel.intancia_nivel.grupo_enemigos) == 0 and not menu_nivel.intancia_nivel.nivel_finalizado:
        menu_nivel.intancia_nivel.cronometro.detenido = True
        menu_nivel.intancia_nivel.nivel_finalizado = True
        jugador.posicion = {"x": 100, "y": 570}
        if menu_nivel.nivel_seleccionado == 1:
            menu_nivel.nivel_1_completado = True
            jugador.puntaje += menu_nivel.intancia_nivel.cronometro.tiempo_restante * 100
        elif menu_nivel.nivel_seleccionado == 2:
            menu_nivel.nivel_2_completado = True
            jugador.puntaje += menu_nivel.intancia_nivel.cronometro.tiempo_restante * 100
        else:
            jugador.puntaje += menu_nivel.intancia_nivel.cronometro.tiempo_restante * 100    
            menu_guardar_nombre.guardado_requerido = True        

        menu_nivel.cambiar_botones()
        menu_nivel.nivel_comenzado = False    

    menu_nivel.intancia_nivel.cronometro.actualizar()
    menu_nivel.intancia_nivel.cronometro.mostrar_tiempo(PANTALLA)
    jugador.grupo_cuchillos.update()    
    jugador.grupo_cuchillos.draw(PANTALLA)   
    jugador.mostrar_salud(PANTALLA)  
    jugador.actualizar()            
    display_puntuacion = fuente.render("Puntaje: " + str(jugador.puntaje), False, BLANCO)
    PANTALLA.blit(jugador.imagen, jugador.rectangulo_jugador)
    PANTALLA.blit(jugador.retrato, (20, 20))
    PANTALLA.blit(display_puntuacion, (800, 50))    

    if menu_nivel.intancia_nivel.cronometro.tiempo_restante <= 0:
        jugador.vida_total = 0
        jugador.personaje_muriendo = True

    if menu_guardar_nombre.guardado_requerido == True:
        menu_guardar_nombre.guardado_requerido = False

        while menu_guardar_nombre.nombre_guardado == False:
            pygame.mixer.music.stop()
            eventos = pygame.event.get()
            for event in eventos:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()            
                
            menu_guardar_nombre.update(eventos)     
            pygame.display.update()  

        base_de_datos_puntaje = Base_de_datos("Segundo parcial/puntajes.db")        
        base_de_datos_puntaje.ingresar_puntaje(menu_guardar_nombre.nombre_jugador, jugador.puntaje)
        base_de_datos_puntaje.cerrar_conexion()
        menu_guardar_nombre.nombre_guardado = False

    for numero_canal in range(pygame.mixer.get_num_channels()):
        canal = pygame.mixer.Channel(numero_canal)
        canal.set_volume(menu_pausa.volumen_fx)

    if jugador.muerto == True:        
        menu_nivel.nivel_comenzado = False
        jugador.vida_total = 5
        jugador.muerto = False
        jugador.personaje_muriendo = False
        jugador.posicion = {"x": 100, "y": 570}        
        jugador.bloqueo_teclado = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                menu_nivel.intancia_nivel.nivel_pausado = not menu_nivel.intancia_nivel.nivel_pausado
                pygame.mixer.music.pause()

    while menu_nivel.intancia_nivel.nivel_pausado == True:
        eventos = pygame.event.get()
        for event in eventos:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    menu_nivel.intancia_nivel.nivel_pausado = not menu_nivel.intancia_nivel.nivel_pausado
                    pygame.mixer.music.unpause()

        menu_pausa.update(eventos)

        pygame.display.update()        