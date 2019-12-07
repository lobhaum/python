casa = float(input('Qual é o valor da casa: R$'))
salario = float(input('Qual é o salario do comprador: R$'))
tempo = int(input('Tempo total de anos do emprestimo: '))
# calcular o valor da casa / tempo em meses:
tempo = tempo * 12
#print(f'{tempo}')
casa_mes_bruto = casa / tempo
teto_parcela = salario * .3
#print(teto_parcela)
if teto_parcela < casa_mes_bruto:
    print('\033[31m Emprestimo Negado\033[m')
else:
    print('\033[32m Emprestimo aprovado\033[m')
    print(f'Valor da parcela: {teto_parcela}')
#print(casa_mes_bruto)
#100.000,00 / 5 anos (5*12 meses) 