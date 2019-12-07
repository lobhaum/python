from datetime import date

i = int(input('Digite o ano: '))
if i == 0:
    i = date.today().year
if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
    print(f'O ano {i} é BISSEXTO')
else:
    print(f'O ano {i} não é BISSEXTO')
