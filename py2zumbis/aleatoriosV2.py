def aleatorios(x, y):
    from random import randint
    lista = []
    for c in range(15):
        lista.append(randint(x, y))
    return print(lista)


aleatorios(10, 100)
