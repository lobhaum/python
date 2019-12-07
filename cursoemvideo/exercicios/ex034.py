i = float(input('Salario atual: '))
print(f'Salario: R${i:.2f}')
if i < 1250:
    aumento = i * 0.15
    i = i + aumento
else:
    aumento = i * 0.1
    i = i + aumento
print(f'Total com reajuste: {i:.2f}')