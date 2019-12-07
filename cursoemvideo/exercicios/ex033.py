# faça um programa que leia tres numeros
# mostre qual é o maior
# mostre qual é o menor

i1 = int(input('Primeiro: '))
i2 = int(input('Segundo: '))
i3 = int(input('Terceiro: '))
print(f'1 - {i1} 2 - {i2} 3 - {i3}')
menor = min( i1, i2, i3)
maior = max(  i1, i2, i3)
print(f'Menor é: {menor}')
print(f'Maior é: {maior}')
