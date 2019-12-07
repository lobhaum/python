from random import randint

lista = []
i = int(input('Quantos números aleatórios: '))
baixo = int(input('Qual é o número mais baixo para o jogo: '))
cima = int(input('Qual é o número mais alto para o jogo: '))
for c in range(i):
    lista.append(randint(baixo, cima))
print(f'Seus números da sorte são: {lista}')
