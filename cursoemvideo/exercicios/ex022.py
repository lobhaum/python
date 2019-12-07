# leia o nome completo;
# - transforme todas as letras em maiusculas
# - transforme todas as letras em minusculas
# - conte todas as letras sem os espaços
# - conte a quantia de letras do primeiro nome
nome = input('Digite seu nome completo: ')
print(nome)
maiuscula = nome.upper()
print(maiuscula)
minuscula = nome. lower()
print(minuscula)
countZero = len(nome.replace(' ',''))
print(nome.replace(' ',''))
print(countZero)
dividir = nome.split()
print(dividir)
print(len(dividir[0]))
