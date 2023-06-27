import pygame
from Imagenes_enemigos import diccionario_animaciones_hombre_lobo
import random
from Clase_Esfera_lunar import Esfera_lunar
from Sonidos import sonido_cuchillo, sonido_hombre_lobo_saltando, sonido_hombre_lobo_regenerandose, sonido_hombre_lobo_regeneracion, sonido_hombre_lobo_ataque_garra


class Hombre_Lobo(pygame.sprite.Sprite):
    def __init__(self, jugador):
        super().__init__()
        self.jugador = jugador
        self.nombre = "Hombre Lobo"
        self.vida_total = 20
        self.velocidad = 7
        self.posicion = {"x":600 ,"y":-20}
        self.intro = True
        self.indice_intro = 0

        #caracteristicas
        self.gravedad = 1
        self.aumento_gravedad = 0.15
        self.velocidad_animacion = 0.15
        self.potencia_salto = 0

        #proyectiles
        self.grupo_esfera_lunar = pygame.sprite.Group()
        self.tiempo_actual = pygame.time.get_ticks()
        self.tiempo_ultimo_ataque = self.tiempo_actual
        self.tiempo_espera_ataque = 2000       
        self.lanzando_proyectil = False

        #estados
        self.indice_inicial = 0
        self.estado_actual = "cayendo"
        self.mirando_izquierda = True
        self.verificar_direccion(self.estado_actual)
        self.sobre_suelo = False
        self.regenerando = False

        #rectangulos
        self.image = diccionario_animaciones_hombre_lobo["intro"][0]
        self.rect = self.image.get_rect(topleft = (self.posicion["x"],self.posicion["y"]))   

        #display
        self.retrato = diccionario_animaciones_hombre_lobo["retrato"]
        self.imagen_salud = diccionario_animaciones_hombre_lobo["icono_salud"]  

    def verificar_direccion(self, estado_actual):
        if self.mirando_izquierda == True:
            estado_actual = f"{self.estado_actual}_izquierda"
        self.animar_imagenes(estado_actual)                
            
    def animar_imagenes(self, estado_actual):
        if self.indice_inicial >= len(diccionario_animaciones_hombre_lobo[estado_actual]):
            self.indice_inicial = 0
        self.image = diccionario_animaciones_hombre_lobo[estado_actual][int(self.indice_inicial)]
        self.indice_inicial += self.velocidad_animacion

        if self.lanzando_proyectil == True and self.indice_inicial >= len(diccionario_animaciones_hombre_lobo[estado_actual]):
            self.lanzando_proyectil = False

    def aplicar_gravedad(self):
        if self.sobre_suelo == False:
            self.posicion["y"] += self.gravedad
            self.gravedad += self.aumento_gravedad
            self.rect.y = self.posicion["y"]    
        else:
            self.gravedad = 1

    def caminar(self, jugador):
        if self.intro == False:
            if self.vida_total > 0 and self.lanzando_proyectil == False and self.regenerando == False:
                if self.sobre_suelo == True:
                    if self.mirando_izquierda == False:
                        self.posicion["x"] += self.velocidad
                    else:
                        self.posicion["x"] += self.velocidad * -1
                    if not self.estado_actual == "ataque_garra" and not self.estado_actual == "ataque_garra_izquierda":
                        self.estado_actual = "caminando"
                        self.velocidad = 7

                else:
                    self.estado_actual = "cayendo"
        else:
            if self.indice_intro < len(diccionario_animaciones_hombre_lobo["intro"]):
                self.image = diccionario_animaciones_hombre_lobo["intro"][int(self.indice_intro)]
                self.indice_intro += 0.02
            else:
                self.intro = False
                jugador.bloqueo_teclado = False
        


    def lanzar_proyectil(self):
        self.estado_actual = "lanzando_proyectil"
        self.lanzando_proyectil = True        
        self.indice_inicial = 0
        self.grupo_esfera_lunar.add(Esfera_lunar(self.rect.x,self.rect.y + 40, self.mirando_izquierda))

    def daño_cuchillo(self, jugador):
        if self.estado_actual == "muriendo" or self.estado_actual == "muriendo_izquierda":
            colision_cuchillo_enemigo = pygame.sprite.spritecollide(self, jugador.grupo_cuchillos, False)
        else:
            colision_cuchillo_enemigo = pygame.sprite.spritecollide(self, jugador.grupo_cuchillos, True)
            if colision_cuchillo_enemigo:
                sonido_cuchillo.play()
                self.vida_total -= 1
                if self.vida_total <= 0:
                    jugador.puntaje += 100

    def daño_contacto(self, jugador):
        if (jugador.rectangulo_jugador.colliderect(self.rect) and jugador.invulnerabilidad == False) and (not self.estado_actual == "muriendo" and not self.estado_actual == "muriendo_izquierda"):
            jugador.vida_total -= 1
            jugador.daño_recibido = True

    def verificar_direccion_ataque(self):
        if self.vida_total > 0 and self.intro == False:
            if (self.jugador.posicion["x"] - self.rect.x < 0 and self.mirando_izquierda) or (self.jugador.posicion["x"] - self.rect.x > 0 and not self.mirando_izquierda):
                self.lanzar_proyectil()

    def saltar(self):
        if self.potencia_salto > 0:
            self.estado_actual = "saltando"  
            self.posicion["y"] -= self.potencia_salto
            self.potencia_salto -= self.gravedad
            if self.mirando_izquierda == True:
                self.posicion["x"] -= 1
            else:
                self.posicion["x"] += 1
        elif self.potencia_salto <= 0 and self.sobre_suelo == False:
                self.estado_actual = "cayendo"
                self.lanzando_proyecil = False

    def regeneracion(self):
        if self.regenerando:
            self.estado_actual = "regeneracion"
            self.imagen_salud = diccionario_animaciones_hombre_lobo["icono_salud_regeneracion"]
            self.vida_total += 4


    def decidir_accion(self):
        if self.vida_total > 0 and self.intro == False:
            if self.tiempo_actual - self.tiempo_ultimo_ataque >= self.tiempo_espera_ataque:
                self.tiempo_ultimo_ataque = self.tiempo_actual
                self.regenerando = False
                accion = random.randint(0, 5)

                match accion:
                    case 0:
                        if self.jugador.posicion["x"] - self.rect.x > -200 and self.jugador.posicion["x"] - self.rect.x < 200:
                            self.potencia_salto = 30
                            sonido_hombre_lobo_saltando.play()

                    case 1:                       
                        self.verificar_direccion_ataque()

                    case 2:
                        self.velocidad = 4.5
                        self.estado_actual = "ataque_garra"
                        sonido_hombre_lobo_ataque_garra.play()
                        
                    case 3:
                        self.estado_actual = "caminando"

                    case 4:
                        self.verificar_direccion_ataque()

                    case 5:
                        self.regenerando = True
                        self.regeneracion()
                        sonido_hombre_lobo_regenerandose.play()
                        sonido_hombre_lobo_regeneracion.play()

    def muerte(self):
        if self.vida_total < 1:
            if not self.estado_actual == "muriendo" and not self.estado_actual == "muriendo_izquierda":
                self.indice_inicial = 0
            self.estado_actual = "muriendo"
            if self.indice_inicial >= len(diccionario_animaciones_hombre_lobo[self.estado_actual]):
                self.kill()

    def mostrar_salud(self, pantalla):
        x = 860
        for i in range(self.vida_total):
            pantalla.blit(self.imagen_salud,(x,150))
            x -= 40

        pantalla.blit(self.retrato,(910,120))

    def update(self, pantalla, jugador):
        self.mostrar_salud(pantalla)
        self.verificar_direccion(self.estado_actual)
        self.rect.x = self.posicion["x"]
        self.rect.y = self.posicion["y"]
        self.caminar(jugador)
        self.daño_cuchillo(jugador)
        self.daño_contacto(jugador)
        self.decidir_accion()
        self.tiempo_actual = pygame.time.get_ticks()
        self.grupo_esfera_lunar.update(jugador)
        self.grupo_esfera_lunar.draw(pantalla)
        self.saltar()
        self.muerte()