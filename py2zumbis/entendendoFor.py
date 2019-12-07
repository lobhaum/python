i = [7, 5, 20, 16, 60, 54]
b = [1, 15, 5, 20, 59, 53]

teste = [5, 7, 9, 13, 21, 27]
b = [1, 2, 3, 4, 5, 7, 9, 14, 18]

c = 0
contador = 0
andar = 0
for c in b:
    # o c está andando dentro da lista
    # print(c) o print mostrou 5 e depois o 7
    if c == teste[andar]:
        # o c anda dentro da lista b e verifica
        # se o elemento contidona posição 0 da
        # lista teste é igual ao elemento em questão
        print(f'{c} = a {teste[andar]}')
        contador = contador + 1
    andar = andar + 1
if contador > 0:
    print(f'Total de acertos: {contador}')
else:
    print('Nenhum acerto')
