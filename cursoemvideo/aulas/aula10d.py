i1 = float(input('Digite a 1a nota: '))
i2 = float(input('Digite a 2a nota: '))
m = (i1 + i2)/2
print(f'A média das notas {i1} e {i2} foi: {m}')
if m < 5:
    print('Reprovado')
elif m < 7:
    print('Passou raspando')
else:
    print('Aprovado com louvor')