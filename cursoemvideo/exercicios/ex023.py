# - leia um numero de 0 a 9999
#   mostre na tela cada um dos digitos separados
num = int(input('Digite um numero: '))
converter = '0000' + str(num)
print(f'Milhar: {converter[-4]}')
print(f'Centena: {converter[-3]}')
print(f'Dezena: {converter[-2]}')
print(f'Unidade: {converter[-1]}')






