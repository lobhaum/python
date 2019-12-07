'''
Pedra ganha da Tesoura (a amassa e quebra)
Tesoura ganha do Papel (o corta)
Papel ganha da Pedra (a embrulha)
----
1 - pedra
2 - tesoura
3 - papel

1 and 2 == 1 wins
2 and 3 == 2 wins
3 and 1 == 3 wins
----
'''
from random import randint
from time import sleep

player = int(input('(1) Pedra | (2) Tesoura | (3) Papel : '))
android = randint(1, 3)
print('Processando...')
sleep(1)
if player == 1 and android == 2:
    print('O android jogou Tesoura')
    print('Pedra ganha da Tesoura (a amassa e quebra)')
    print('Você ganhou')
elif player == 2 and android == 2:
    print('O android jogou Tesoura')
    print('Empatou')
elif player == 3 and android == 2:
    print('O android jogou Papel')
    print('Tesoura ganha de Papel (o corta)')
    print('Você perdeu')
elif player == 1 and android == 1:
    print('O android jogou Pedra')
    print('Empatou')
elif player == 2 and android == 1:
    print('O android jogou Pedra')
    print('Pedra ganha de Tesoura (a amassa e quebra)')
    print('Você perdeu')
elif player == 3 and android == 1:
    print('O android jogou Pedra')
    print('Papel ganha da Pedra (a embrulha)')
    print('Você ganhou')
elif player == 1 and android == 3:
    print('o android jogou Papel')
    print('Papel ganha da Pedra (a embrulha)')
    print('Você perdeu')
elif player == 2 and android == 3:
    print('O android jogou Papel')
    print('Tesoura ganha de Papel ( o corta )')
    print('Você perdeu')
elif player == 3 and android == 3:
    print('O android jogou Papel')
    print('Empatou')
