print('{:=^40}'.format('LOJAS GUANABARA'))
preco = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] À Vista dinheiro
[ 2 ] À Vista cartão de crédito
[ 3 ] 2x cartão de crédito
[ 4 ] 3x ou mais no cartão de credito ''')
opcao = int(input('Opção de pagamento: '))
if opcao == 1:
    total = preco * .90
elif opcao == 2:
    total = preco * .95
elif opcao == 3:
    total = preco
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f}')
elif opcao == 4:
    total = preco * 1.2
    total_parcelas = int(input('Quantas parcelas ? '))
    parcela = total / total_parcelas
    print(f'Sua compra será parceladas em {total_parcelas} de R${parcela:.2f}')
else:
    total = preco
    print('OPÇÃO INVÁLIDA DE PAGAMENTO. TENTE NOVAMENTE')
print(f'Sua compra de R${preco:.2f} vai custar R${total:.2f}')
