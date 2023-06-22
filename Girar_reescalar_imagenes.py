import pygame

def girar_imagenes(lista_original,flip_x,flip_y):
    lista_girada = []
        
    try:
        for imagen in lista_original:
            lista_girada.append(pygame.transform.flip(imagen, flip_x, flip_y))
    except TypeError:
        print(f"Error, tipo de dato incorrecto, ingrese una lista")

    return lista_girada

def reescalar_imagenes(lista_imagenes, tamaño):
    try:
        for i in range(len(lista_imagenes)):
            lista_imagenes[i] = pygame.transform.scale(lista_imagenes[i], tamaño)
    except TypeError:
        print(f"Error, tipo de dato incorrecto, ingrese una lista")

    return lista_imagenes