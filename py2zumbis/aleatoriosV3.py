from random import randint

lista = []
while len(lista) < 15:
    x = randint(10, 100)
    if x not in lista:
        lista.append(x)
lista.sort()
print(lista)
