import pygame
from pygame.locals import *
from GUI_button import *
from GUI_slider import *
from GUI_textbox import *
from GUI_label import *
from GUI_form  import *
from GUI_button_image  import *
from GUI_form_menu_score import *

class FormMenuSeleccionNivel(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border = "Black", border_size = -1, active = True):
        super().__init__(screen, x, y, w, h, color_background, color_border, border_size, active)       
        self.nivel_comenzado = False
        self.nivel_seleccionado = 0
        self.nivel_1_completado = False
        self.nivel_2_completado = False
        self.x = x
        self.y = y
        self.intancia_nivel = None
        
        self.label_seleccion_nivel = Label(self._slave, 0, 0, 900, 300, "1", "Garamond", 16, "White", "Segundo parcial/Recursos/Imagenes_interfaz/label_seleccion_nivel.png")

        self.btn_nivel_1 = Button_Image(self._slave, x, y, 200, 240, 50, 50, "Segundo parcial/Recursos/Imagenes_interfaz/imagen_nivel_1.png", self.btn_nivel_click, 1)         
        self.btn_nivel_2 = Button_Image(self._slave, x, y, 400, 240, 50, 50, "Segundo parcial/Recursos/Imagenes_interfaz/imagen_nivel_cerrado.png", self.btn_nivel_click)
        self.btn_nivel_3 = Button_Image(self._slave, x, y, 600, 240, 50, 50, "Segundo parcial/Recursos/Imagenes_interfaz/imagen_nivel_cerrado.png", self.btn_nivel_click)        

        self.lista_widgets.append(self.label_seleccion_nivel)
        self.lista_widgets.append(self.btn_nivel_1)
        self.lista_widgets.append(self.btn_nivel_2)
        self.lista_widgets.append(self.btn_nivel_3)

        self.render()

    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            if self.active:
                self.draw()
                self.render()
                for widget in self.lista_widgets:
                    widget.update(lista_eventos)
        else:
            self.hijo.update(lista_eventos)

    def cambiar_botones(self):
        if self.nivel_1_completado == True:
            self.btn_nivel_2 = Button_Image(self._slave, self.x, self.y, 400, 240, 50, 50, "Segundo parcial/Recursos/Imagenes_interfaz/imagen_nivel_2.png", self.btn_nivel_click, 2)
            self.btn_nivel_3 = Button_Image(self._slave, self.x, self.y, 600, 240, 50, 50, "Segundo parcial/Recursos/Imagenes_interfaz/imagen_nivel_cerrado.png", self.btn_nivel_click)

        if self.nivel_2_completado == True:
            self.btn_nivel_2 = Button_Image(self._slave, self.x, self.y, 400, 240, 50, 50, "Segundo parcial/Recursos/Imagenes_interfaz/imagen_nivel_2.png", self.btn_nivel_click, 2)
            self.btn_nivel_3 = Button_Image(self._slave, self.x, self.y, 600, 240, 50, 50, "Segundo parcial/Recursos/Imagenes_interfaz/imagen_nivel_3.png", self.btn_nivel_click, 3)   

        self.lista_widgets[2] = self.btn_nivel_2
        self.lista_widgets[3] = self.btn_nivel_3

    def render(self):
        self._slave.fill(self._color_background)

    def btn_nivel_click(self, numero_nivel):
        self.nivel_seleccionado = numero_nivel
        self.nivel_comenzado = True

