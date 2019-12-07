# escreva um programa
# leia velocidade do carro
# se ultrapassar 80km/h
# multa de R$7,00/km excedido
from math import ceil

i = float(input('Velocidade registra: '))
m = 7
l = 80
if i > l:
    r = ceil((i - l) * m)
    print('Excedeu a velocidade em {:.2f}Km/h, multa registrada de R$ {:.2f}.'.
          format(i - l, r))
else:
    print(f'Velocidade dentro do limite')
