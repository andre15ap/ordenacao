import random

def aleatoria(tam):
    lista = []
    for i in range(tam):
        lista.append(random.randint(1,100))

    return lista

def ordenada(tam):
    lista = []
    for i in range(tam):
        lista.append(i)
    
    return lista

def inversa(tam):
    lista = []
    for i in range(tam, 0, -1):
        lista.append(i)
    
    return lista
