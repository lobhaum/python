i = input('Qual é seu nome? ')
if i == 'Jully':
    print('Que nome bonito!')
elif i == 'Pedro' or i == 'Maria' or i == 'Paulo':
    print('Seu nome é bem comum no Brasil')
elif i in 'Ana Cláudia Jessica Juliana':
    print('Belo nome para moças')
else:
    print('Que nome normal')
print(f'Tenha um bom dia {i}')