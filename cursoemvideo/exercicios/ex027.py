# escreva o nome de uma pessoa
# mostrando em seguida o primeiro
# e o ultimo nome.
# Ex: Ana Maria de Souza
# primeiro= Ana
# ultimo = Souza
i = input('Digite o nome completo: ')
s = i.split()
print(f'primeiro = {s[0]}')
print(f'ultimo = {s[-1]}')
