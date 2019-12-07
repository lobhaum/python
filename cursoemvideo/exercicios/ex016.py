# crie um programa que leia um número
# Real quaqleru pelo teclado e mostre
# na tela a sua porção inteira
from math import trunc
num = float(input('Digite um valor: '))
inteiro = trunc(num) 
print(f'O valor digitado foi {num} e a sua porção inteira é {inteiro}')
