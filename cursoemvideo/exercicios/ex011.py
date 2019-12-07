# Faça um programa que leia a largura e altura
# de uma parede em metros, calcule a sua área
# e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta, pinta uma
# área de 2m².
l = float(input('Largura: '))
a = float(input('Altura: '))
c = l * a
t = 2
p = c / 2
print(
    'Sua parede tem {}m largura x {}m altura. Como total de área de {:.1f}m²'.
    format(l, a, c))
print('São necessário {:.1f}l de tinta para uma mão de pintura'.format(p))
