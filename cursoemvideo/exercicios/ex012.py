# faça um algoritmo que leia o preço
# de um produto e mostre seu novo preço
# com 5% de desconto.
p = float(input('Digite o valor do produto: R$'))
c = p*0.95
print('Para pagamento à prazo R${} para pagamento à vista R${}'.format(p, c))
