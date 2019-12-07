meses = [
    'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho',
    'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'
]
i = input('Digite a sua data de nascimento no formato dd/mm/aaaa: ')
separa = i.split('/')
s = int(separa[1]) - 1
print(f'Sua data é: {separa[0]} de {meses[s]} de {separa[2]}.')
