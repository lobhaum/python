# crie um programa que leia quanto dinheiro uma pessoa tem
# na carteira e mostre quantos dólares ela pode comprar
# cambio US$1,00 == R$3,27
real = float(input('Digite a quantidade de REAL(R$): '))
dolar = 3.27
cambio = real/dolar
print('Você tem: R${} e o câmbio de hoje é: US${}, portanto caso queira comprar, você receberá: US${:.2f} pelo seu montante em BRL'.format(real, dolar, cambio))
