print('*'* 33)
print('Bem vindo no jogo de Adivinhação!')
print('*'* 33)
numero_secreto = 42
chute = int(input('Digite um número inteiro exemplo: 14: '))
print(f'Voce digitou: {chute}')
if(numero_secreto == chute):
    print(f'Você acertou o número secreto: {chute}')
else:
    print(f'Você errou o número secreto, tente novamente mais tarde')
