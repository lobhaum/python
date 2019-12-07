i1 = float(input('Digite um numero: '))
i2 = float(input('Digite outro numero: '))
#menor = min(i1, i2)
#maior = max(i1, i2)
#print(menor)
#print(maior)
if i1 > i2:
    print(f'O {i1} é maior que {i2}')
elif i2 > i1:
    print(f'O {i2} é maior que {i1}')
else:
    print(f'Os dois são iguais')