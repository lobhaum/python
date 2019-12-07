# leia uma frase:
# quantas vezes aparece a letra "A"
# em que posição ela aparece na primeira vez
# em que posição ela aparece a ultima vez
i = input('Digite uma frase com pelo menos 5 palavras: ')
print('A letra \'A\' aparece ', end = '')
print(i.upper().count('A'), ' vezes.')
print('A primeira vez que aparece a letra \'A\' é: ', end = '')
print(i.upper().find('A'))
print('A ultima vez que aparece a letra \'A\' é: ', end = '')
print(i.upper().rfind('A'))
