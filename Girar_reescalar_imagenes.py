import pygame

def girar_imagenes(lista_original, flip_x, flip_y)->list:
    lista_girada = []
        
    try:
        for imagen in lista_original:
            lista_girada.append(pygame.transform.flip(imagen, flip_x, flip_y))
    except TypeError:
        print("Error, el tipo de dato pasado como parámetro es incorrecto")
    except Exception as e:
        print(f"Error inesperado: {e}")

    return lista_girada

def reescalar_imagenes(lista_imagenes, tamaño)->list:
    try:
        for i in range(len(lista_imagenes)):
            lista_imagenes[i] = pygame.transform.scale(lista_imagenes[i], tamaño)
    except TypeError:
        print("Error, el tipo de dato pasado como parámetro es incorrecto")
    except Exception as e:
        print(f"Error inesperado: {e}")

    return lista_imagenes