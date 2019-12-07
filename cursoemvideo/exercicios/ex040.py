i1 = float(input('1a nota: '))
i2 = float(input('2a nota: '))
media = (i1 + i2) / 2
if media < 5.0:
    print('REPROVADO')
elif media >= 5.0 and media < 6.9:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')