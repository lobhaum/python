def aleatorio(x, y):
    from random import randint
    c = 0
    while c < 15:
        i = randint(x, y)
        c = c + 1
        print(i)


print(aleatorio(10, 100))
