# leia o nome de uma pessoa
# diga se tem SILVA no nome

i = str(input('Digite seu nome completo: '))
print('Você tem SILVA no nome: ', end = '')
print('SILVA' in i.upper())
