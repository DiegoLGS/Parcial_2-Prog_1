import pygame

def obtener_rectangulos(principal)->dict:
    diccionario = {}
    diccionario["main"] = principal
    diccionario["top"] = pygame.Rect(principal.left, principal.top, principal.width, 12)
    diccionario["bottom"]  = pygame.Rect(principal.left, principal.bottom - 6, principal.width, 6)
    diccionario["right"] = pygame.Rect(principal.right - 2, principal.top, 2, principal.height)
    diccionario["left"] = pygame.Rect(principal.left, principal.top, 2, principal.height)

    return diccionario