from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
android = randint(0, 2)
print('''
Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA
''')
player = int(input('Qual é a sua jogada: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('-=' * 15)
print(f'Você jogou: {itens[player]}')
print(f'Android escolheu: {itens[android]}')
print('-=' * 15)
if android == 0:  # jogou pedra
    if player == 0:  # jogou pedra
        print('Empatou')
    elif player == 1:  # jogou papel
        print('Você ganhou (papel embrulha pedra)')
    elif player == 2:  # jogou tesoura
        print('Android ganhou (pedra quebra tesoura)')
    else:
        print('JOGADA INVALIDA')
elif android == 1:  # jogou papel
    if player == 0:  # pedra
        print('Você perdeu (papel embrulha pedra)')
    elif player == 1:  # papel
        print('Empatou')
    elif player == 2:  # tesoura
        print('VocÊ ganhou (tesoura corta papel)')
    else:
        print('JOGADA INVÁLIDA')
elif android == 2:  # jogou tesoura
    if player == 0:  # pedra
        print('Você ganhou (pedra quebra tesoura)')
    elif player == 1:  # papel
        print('Você perdeu (tesoura corta papel)')
    elif player == 2:  # tesoura
        print('Empatou')
    else:
        print('JOGADA INVALIDA')
