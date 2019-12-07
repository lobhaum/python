i = input('Digite uma palavra: ')
ii = i[::-1]
if i == ii:
    print(f'{i} é palindrome de {ii}')
else:
    print(f'{i} não é palindrome de {ii}')
