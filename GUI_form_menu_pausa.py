import pygame
from pygame.locals import *
from GUI_button import *
from GUI_slider import *
from GUI_textbox import *
from GUI_label import *
from GUI_form  import *
from GUI_button_image  import *
from GUI_form_menu_score import *
from Clase_Base_de_datos import Base_de_datos

class FormMenuPausa(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border = "Black", border_size = -1, active = True):
        super().__init__(screen, x, y, w, h, color_background, color_border, border_size, active)

        self.volumen = 0.1
        self.volumen_fx = 0.1
        self.flag_play = True

        pygame.mixer.init()

        #### CONTROLES ####################       

        self.label_volumen = Label(self._slave, 680, 195, 100, 50, "20%", "Garamond", 16, "White", "Segundo parcial/Recursos/Imagenes_interfaz/label.png")
        self.slider_volumen = Slider(self._slave, x , y, 160, 210, 500, 15, self.volumen, "Blue", "White")
        self.label_volumen_fx = Label(self._slave, 680, 285, 100, 50, "20%", "Garamond", 16, "White", "Segundo parcial/Recursos/Imagenes_interfaz/label.png")
        self.slider_volumen_fx = Slider(self._slave, x , y, 160, 300, 500, 15, self.volumen_fx, "Blue", "White")

        self.btn_ranking = Button_Image(self._slave, x, y, 390, 40, 150, 150,  "Segundo parcial/Recursos/Imagenes_interfaz/ranking.png", self.btn_ranking_click, "texto de prueba")
        ################################

        #Agrego los controles a las lista
        self.lista_widgets.append(self.label_volumen)
        self.lista_widgets.append(self.label_volumen_fx)
        self.lista_widgets.append(self.slider_volumen)
        self.lista_widgets.append(self.slider_volumen_fx)
        self.lista_widgets.append(self.btn_ranking)
        ##########################

        pygame.mixer.music.set_volume(self.volumen)        

        self.render()

    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            if self.active:
                self.draw()
                self.render()
                for widget in self.lista_widgets:
                    widget.update(lista_eventos)
                self.update_volumen(lista_eventos)
        else:
            self.hijo.update(lista_eventos)

    def render(self):
        self._slave.fill(self._color_background)
        
    def update_volumen(self, lista_eventos):
        self.volumen = self.slider_volumen.value
        self.volumen_fx = self.slider_volumen_fx.value
        self.label_volumen.set_text(f"{round(self.volumen * 100)}%")
        self.label_volumen_fx.set_text(f"{round(self.volumen_fx * 100)}%")
        pygame.mixer.music.set_volume(self.volumen)

    def btn_ranking_click(self, texto):
        base_de_datos_puntaje = Base_de_datos("Segundo parcial/puntajes.db")
        puntajes = base_de_datos_puntaje.obtener_puntajes()
                
        form_puntaje = FormMenuScore(self._master, 250, 25, 500, 550, (220, 0, 220), "White", True, "Segundo parcial/Recursos/imagenes_interfaz/recuadro.jpg", puntajes, 100, 10, 10)

        self.show_dialog(form_puntaje)
        base_de_datos_puntaje.cerrar_conexion()

