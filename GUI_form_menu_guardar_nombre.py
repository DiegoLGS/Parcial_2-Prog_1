import pygame
from pygame.locals import *
from GUI_button import *
from GUI_slider import *
from GUI_textbox import *
from GUI_label import *
from GUI_form  import *
from GUI_button_image  import *
from GUI_form_menu_score import *

class FormMenuGuardarNombre(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border = "Black", border_size = -1, active = True):
        super().__init__(screen, x, y, w, h, color_background, color_border, border_size, active)    
        self.guardado_requerido = False
        self.nombre_guardado = False
        self.nombre_jugador = None

        self.label_ingreso_nombre = Label(self._slave, 0, 0, 900, 200, "1", "Garamond", 16, "White", "Segundo parcial/Recursos/Imagenes_interfaz/label_ingreso_nombre.jpg")
        self.txtbox = TextBox(self._slave, x, y, 270, 280, 250, 30, "Gray", "White", "Black", "Red", 2, font = "Garamond", font_size = 15, font_color = "Black")   
        self.btn_guardar = Button_Image(self._slave, x, y, 570, 270, 50, 50, "Segundo parcial/Recursos/Imagenes_interfaz/guardar.png", self.guardar_nombre, "")

        self.lista_widgets.append(self.label_ingreso_nombre)
        self.lista_widgets.append(self.txtbox)
        self.lista_widgets.append(self.btn_guardar)

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

    def render(self):
        self._slave.fill(self._color_background)

    def guardar_nombre(self, texto):
        self.nombre_jugador = self.txtbox.get_text()
        self.nombre_guardado = True

