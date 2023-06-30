import pygame

def obtener_rectangulos(principal)->dict:
    diccionario = {}

    try:
        diccionario["main"] = principal
        diccionario["top"] = pygame.Rect(principal.left, principal.top, principal.width, 12)
        diccionario["bottom"]  = pygame.Rect(principal.left, principal.bottom - 6, principal.width, 6)
        diccionario["right"] = pygame.Rect(principal.right - 2, principal.top, 2, principal.height)
        diccionario["left"] = pygame.Rect(principal.left, principal.top, 2, principal.height)
    except TypeError as e:
        print("Error, el tipo de dato pasado como parámetro es incorrecto")
    except AttributeError as e:
        print("Error, el tipo de dato pasado no contiene los atributos requeridos")
    except Exception as e:
        print(f"Error inesperado: {e}")

    return diccionario