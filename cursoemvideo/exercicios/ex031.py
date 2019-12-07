i = float(input('Total de Km do trajeto: '))
b1 = 0.5
b2 = 0.45
if i <= 200:
    c = i * b1
    print(f'Total do custo do trajeto: R${c}')
else:
    c = i * b2
    print(f'Total do custo do trajeto: R${c}')
