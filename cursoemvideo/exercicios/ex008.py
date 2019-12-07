# escreva um programa que leia um valor em metros e o exiba convetido
# em centímetros e milimetros
metro = float(input('Digite a metragem: '))
cent = metro*100
mili = metro*1000
print('O valor digitado foi {}. Ele convetido: {} centimetros e {} milimetros'.format(metro, cent, mili))
