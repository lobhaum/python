from random import randint

lista = []
i = int(input('Quantos números aleatórios: '))
baixo = int(input('Qual é o número mais baixo para o jogo: '))
cima = int(input('Qual é o número mais alto para o jogo: '))
for c in range(i):
    geraNumero = randint(baixo, cima)
    if geraNumero not in lista:
        lista.append(geraNumero)
lista.sort()
print(f'Seus números da sorte são: {lista}')
