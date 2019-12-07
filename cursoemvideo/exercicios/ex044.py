from time import sleep

print('+-----------------------------------------+')
print('|   LOJA VENDE TUDO E OUTRAS COISAS MAIS  |')
print('+-----------------------------------------+')
quantidade = float(input('Quantidade: '))
produto = str(input('Produto: '))
vlunit = float(input('Valor unitário: R$'))
bruto = (quantidade * vlunit)
dinheiro = bruto * .9
cartao = bruto * .95
parc2 = bruto / 2
parc3 = bruto * 1.2 / 3
print('+----------------------------------------+')
print('| OPÇÕES DE PAGAMENTO:                   |')
print('+----------------------------------------+')
print(f'| À vista: R${bruto} com 10% desc R${dinheiro:.2f}')
print('+----------------------------------------+')
print(f'| À vista no CC com 5% desc R${cartao:.2f}')
print('+----------------------------------------+')
print(f'| CC em 2x à parcela de R${parc2:.2f} ')
print('+----------------------------------------|')
print(
    f'| CC em 3x c/ juros de 20% parc de \n| R$ {parc3:.2f}                               |'
)
print('+----------------------------------------+')
sleep(3)
print('| Escolha a forma de pagamento:          |')
print('+------------+--------------+------------+')
print('| 1) À vista | 2) À vist CC | 3) Parc 2x |')
print('| 4) Parc 3x |              |            |')
print('+------------+--------------+------------+')
i = int(input('Digite o código > '))
print('Processando...')
sleep(2)
print('+----------------------------------------+')
if i == 1:
    print(f'| À vista: R${bruto} com 10% desc R${dinheiro:.2f}')
elif i == 2:
    print(f'| À vista no CC R${bruto} c/ 5% desc R${cartao:.2f}')
elif i == 3:
    print(f'| CC em 2x R${bruto} e parc(s) de R${parc2:.2f}')
elif i == 4:
    print(
        f'| CC em 3x R${bruto} e Juros de \nR${bruto*0.2:.2f} e parc de R${parc3:.2f}'
    )
print('| Volte Sempre e Boas Festas            |')
print('+---------------------------------------+')
