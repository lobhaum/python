from random import randint
print('-='*9)
print('Mão na massa game')
print('-='*9)
android = randint(1, 1000)
# print (android)
# Definindo regras:

shoot = int(input('Digite um número entre 1 e 1000: '))
acertou = shoot == android
maior = shoot > android
menor = shoot < android
if (acertou):
    print('Parabéns Campeão, você deveria jogar na mega, pois acertou')
elif (maior):
    print('Que pena, não foi desta vez, seu palpite foi maior que o meu número')
    print(f'Joguei :{android}')
else:
    print('Vixi, nem chegou perto, faltou feijão, seu palpite foi menor que o meu número')
    print(f'Joguei :{android}')
