s = 0
for c in range(0, 6):
    i = int(input(f'Digite o {c+1}o. número: '))
    if i % 2 == 0:
        s += i
print(f'A soma dos números pares digitados é: {s}')
