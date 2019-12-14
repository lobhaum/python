# coding: utf-8
frutas= ['Banana', 'Maça', 'Pera', 'Uva', 'Melancia', 'Jamelão']
frutas_pedidas = input('Qual é a fruta que deseja consultar? ')
if(frutas_pedidas in frutas):
    print('Sim, temos a fruta!')
else:
    print('Não temos a fruta! sniff...')
