# leia o nome de uma cidade
# diga se ela começa com o nome
# SANTO
cidade = str(input('Digite o nome de uma cidade: '))
separa = cidade.split()
print(separa[0])
print(f'A cidade {cidade} tem a palavra SANTO como sua primeira palavra? ', end = '')
print('SANTO' in separa[0].upper())
