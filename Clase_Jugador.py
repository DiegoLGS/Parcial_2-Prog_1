import pygame
from Imagenes_protagonista import diccionario_animaciones
from Sonidos import sonidos_jugador_herida
from Obtener_rectangulos import obtener_rectangulos
from Clase_Cuchillo import Cuchillo

class Jugador():
    def __init__(self):
        self.posicion = {"x":100,"y":570}
        self.viento = False
        self.personaje_muriendo = False
        self.muerto = False

        #caracteristicas
        self.gravedad = 0.2
        self.aumento_gravedad = 0.2
        self.potencia_salto = 0
        self.velocidad = 6
        self.velocidad_animacion = 0.2
        self.tiempo_animacion_muerte = 0

        #proyectiles
        self.grupo_cuchillos = pygame.sprite.Group()
        self.tiempo_ultimo_lanzamiento = 0
        self.tiempo_actual = 0
        self.tiempo_espera_cuchillos = 500 #milisegundos
        self.lanzando_proyecil = False

        #estados
        self.indice_inicial = 0
        self.estado_actual = "parado"
        self.mirando_izquierda = False
        self.verificar_direccion(self.estado_actual)
        self.sobre_suelo = False
        self.imagen
        self.vida_total = 4
        self.daño_recibido = False
        self.bloqueo_teclado = False

        #invulnerabilidad
        self.tiempo_control_invulnerabilidad = 0
        self.duracion_limite_invulnerabilidad = 3000
        self.invulnerabilidad = False
        self.duracion_total_invulnerabilidad = 0

        #rectangulos
        self.rectangulo_jugador = self.imagen.get_rect(topleft = (self.posicion["x"],self.posicion["y"]))
        self.rectangulos_lados = obtener_rectangulos(self.rectangulo_jugador)

        #display
        self.retrato = diccionario_animaciones["retrato"]
        self.imagen_salud = diccionario_animaciones["icono_salud"]        
        self.puntaje = 0

    def verificar_direccion(self,estado_actual):
        if self.mirando_izquierda == True:
            estado_actual = f"{self.estado_actual}_izquierda"
        self.animar_imagenes(estado_actual)                
            
    def animar_imagenes(self,estado_actual):
        if self.personaje_muriendo == False:
            if self.indice_inicial >= len(diccionario_animaciones[estado_actual]):
                self.indice_inicial = 0
            self.imagen = diccionario_animaciones[estado_actual][int(self.indice_inicial)]
            self.indice_inicial += self.velocidad_animacion

            if self.lanzando_proyecil == True and self.indice_inicial >= 3:
                self.lanzando_proyecil = False

    def deteccion_teclado(self):
        if self.personaje_muriendo == False:
            if self.bloqueo_teclado == False:
                lista_teclas = pygame.key.get_pressed()
                if self.sobre_suelo == True:
                    if lista_teclas[pygame.K_SPACE]:
                            self.potencia_salto = 28   

                    if lista_teclas[pygame.K_d]:
                        self.posicion["x"] += self.velocidad
                        self.estado_actual = "caminando"
                        self.mirando_izquierda = False
                    elif lista_teclas[pygame.K_a]:
                        self.posicion["x"] += self.velocidad * -1
                        self.estado_actual = "caminando"
                        self.mirando_izquierda = True
                    elif self.lanzando_proyecil == False:
                        if self.viento:
                            self.estado_actual = "parado_viento"
                        else:
                            self.estado_actual = "parado"
                else:
                    if lista_teclas[pygame.K_d]:
                        self.mirando_izquierda = False
                        self.posicion["x"] += self.velocidad
                    elif lista_teclas[pygame.K_a]:
                        self.mirando_izquierda = True
                        self.posicion["x"] += self.velocidad * -1

                self.tiempo_actual = pygame.time.get_ticks()

                if lista_teclas[pygame.K_j] and self.tiempo_actual - self.tiempo_ultimo_lanzamiento >= self.tiempo_espera_cuchillos:
                    self.estado_actual = "lanzando_proyectil"
                    self.grupo_cuchillos.add(self.lanzar_proyectil())
                    self.tiempo_ultimo_lanzamiento = self.tiempo_actual
                    self.lanzando_proyecil = True
        else:
            self.tiempo_animacion_muerte = pygame.time.get_ticks() - self.tiempo_actual
            self.indice_inicial = self.tiempo_animacion_muerte / 1000 
            if self.indice_inicial < len(diccionario_animaciones["muriendo"]):
                self.imagen = diccionario_animaciones["muriendo"][int(self.indice_inicial)]
            else:
                self.muerto = True
                self.puntaje = 0

    def saltar(self):
        if self.potencia_salto > 0:
            self.estado_actual = "saltando"  
            self.posicion["y"] -= self.potencia_salto
            self.potencia_salto -= self.gravedad
        elif self.potencia_salto <= 0 and self.sobre_suelo == False:
                self.estado_actual = "cayendo"
                self.lanzando_proyecil = False

    def lanzar_proyectil(self):
        return Cuchillo(self.posicion["x"],self.posicion["y"] + 14, self.mirando_izquierda)

    def aplicar_gravedad(self):
        if self.sobre_suelo == False:
            self.posicion["y"] += self.gravedad
            self.gravedad += self.aumento_gravedad
            self.rectangulo_jugador.y = self.posicion["y"]    
        else:
            self.gravedad = 1

    def detectar_daño(self):
        if self.daño_recibido == True:

            if self.vida_total < 1:
                self.bloqueo_teclado = True
                self.personaje_muriendo = True
                self.indice_inicial = 0
            else:
                sonidos_jugador_herida.play()
                self.invulnerabilidad = True
                self.tiempo_control_invulnerabilidad = pygame.time.get_ticks()
                self.duracion_total_invulnerabilidad = self.tiempo_control_invulnerabilidad + self.duracion_limite_invulnerabilidad
                self.daño_recibido = False

        if self.invulnerabilidad == True:
            self.tiempo_control_invulnerabilidad = pygame.time.get_ticks()
            if self.tiempo_control_invulnerabilidad  <= self.duracion_total_invulnerabilidad:
                self.imagen.set_alpha(150)
            else:
                self.invulnerabilidad = False
        else:
                self.imagen.set_alpha(255)

    def mostrar_salud(self, pantalla):
        x = 140
        for i in range(self.vida_total):
            pantalla.blit(self.imagen_salud,(x,50))
            x += 40

    def nivel_final(self, nivel_final):
        if nivel_final:
            self.viento = True


    def actualizar(self):
        self.deteccion_teclado()
        self.verificar_direccion(self.estado_actual)
        self.rectangulo_jugador.x = self.posicion["x"]
        self.rectangulo_jugador.y = self.posicion["y"]
        self.saltar()
        self.rectangulos_lados = obtener_rectangulos(self.rectangulo_jugador)
        self.detectar_daño()