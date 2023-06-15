import pygame
from Imagenes_protagonista import diccionario_animaciones
from Obtener_rectangulos import obtener_rectangulos
from Clase_Cuchillo import Cuchillo

class Jugador():
    def __init__(self):
        self.posicion = {"x":200,"y":300}
        #caracteristicas
        self.gravedad = 0.2
        self.aumento_gravedad = 0.2
        self.potencia_salto = 0
        self.velocidad = 4
        self.velocidad_animacion = 0.2

        #estados
        self.indice_inicial = 0
        self.estado_actual = "parado"
        self.mirando_izquierda = False
        self.verificar_direccion(self.estado_actual)
        self.sobre_suelo = False
        self.imagen
        self.grupo_cuchillos = pygame.sprite.Group()

        #rectangulos
        self.rectangulo_jugador = self.imagen.get_rect(topleft = (self.posicion["x"],self.posicion["y"]))
        self.rectangulos_lados = obtener_rectangulos(self.rectangulo_jugador)

    def verificar_direccion(self,estado_actual):
        if self.mirando_izquierda == True:
            estado_actual = f"{self.estado_actual}_izquierda"
        self.animar_imagenes(estado_actual)                
            
    def animar_imagenes(self,estado_actual):
        if self.indice_inicial >= len(diccionario_animaciones[estado_actual]):
            self.indice_inicial = 0
        self.imagen = diccionario_animaciones[estado_actual][int(self.indice_inicial)]
        self.indice_inicial += self.velocidad_animacion

    def deteccion_teclado(self):
        lista_teclas = pygame.key.get_pressed()
        if self.sobre_suelo == True:
            if lista_teclas[pygame.K_SPACE]:
                    self.potencia_salto = 20         

            if lista_teclas[pygame.K_d]:
                self.posicion["x"] += self.velocidad
                self.estado_actual = "caminando"
                self.mirando_izquierda = False
            elif lista_teclas[pygame.K_a]:
                self.posicion["x"] += self.velocidad * -1
                self.estado_actual = "caminando"
                self.mirando_izquierda = True
            else:
                self.estado_actual = "parado"
        else:
            if lista_teclas[pygame.K_d]:
                self.mirando_izquierda = False
                self.posicion["x"] += self.velocidad
            elif lista_teclas[pygame.K_a]:
                self.mirando_izquierda = True
                self.posicion["x"] += self.velocidad * -1

        if lista_teclas[pygame.K_j]:
            self.estado_actual = "lanzando_proyectil"
            self.grupo_cuchillos.add(self.tirar_cuchillo())

    def saltar(self):
        if self.potencia_salto > 0:
            self.estado_actual = "saltando"  
            self.posicion["y"] -= self.potencia_salto
            self.potencia_salto -= self.gravedad
        elif self.potencia_salto <= 0 and self.sobre_suelo == False:
                self.estado_actual = "cayendo"

    def tirar_cuchillo(self):
        return Cuchillo(self.posicion["x"],self.posicion["y"] + 14, self.mirando_izquierda)

    def aplicar_gravedad(self):
        if self.sobre_suelo == False:
            self.posicion["y"] += self.gravedad
            self.gravedad += self.aumento_gravedad
            self.rectangulo_jugador.y = self.posicion["y"]    
        else:
            self.gravedad = 1

    def actualizar(self):
        self.deteccion_teclado()
        self.verificar_direccion(self.estado_actual)
        self.rectangulo_jugador.x = self.posicion["x"]
        self.rectangulo_jugador.y = self.posicion["y"]
        self.saltar()
        self.rectangulos_lados = obtener_rectangulos(self.rectangulo_jugador)
