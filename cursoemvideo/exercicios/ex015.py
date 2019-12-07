# Aluguel de carro
# Escreva um programa que pergunte a quantidade de Km 
# percorridos por um carro alugado e a quantidade de dias 
# pelos quais ele foi alugado. Calcule o preço a pagar, 
# sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
km = float(input('Quantidade de Km rodado:'))
dias = float(input('Em quantos dias:'))
cdia = 60
krol = 0.15
tdia = dias * cdia
tkm = km * krol
tgeral = tdia + tkm
print(f'{km:.0f}Km rodados em {dias:.0f} dias')
print(f'Valor do consumo/dia: R${tdia}')
print(f'Valor total/km: R${tkm}')
print(f'Total a pagar: R${tgeral}')

