i = int(input('Digite um número qualquer: '))
for c in range(1, i + 1):
    # print(i % c)
    if c != 1 and c != i and i % c == 0:
        print('Este número não é primo')
        break
