def embaralha(i):
    import random
    lista = list(i)
    random.shuffle(lista)
    return ''.join(lista)


print(embaralha('cotonetes'))
