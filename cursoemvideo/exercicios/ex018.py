# leia um angulo qualquer e mostre
# na tela o valor do seno, cosseno e tangente
# desse angulo
from math import tan, radians, cos, sin
an = float (input('Digite o angulo que vc deseja: '))
seno = sin(radians(an))
print(f'O angulo de {an} tem o SENO de {seno :.2f}.')
cosseno = cos(radians(an))
print(f'O angulo de {an} tem o COSSENO de {cosseno :.2f}.')
tangente = tan(radians(an))
print(f'O angulo de {an} tem a TANGENTE de {tangente :.2f}.')
