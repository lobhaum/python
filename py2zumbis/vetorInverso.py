i = 0
vetor = []
while i <= 9:
    r = int(input('Digite um numero: '))
    vetor.append(r)
    i += 1
## print('Vetor contem', vetor[::-1])
i = 9
while i >= 0:
    print(vetor[i])
    i -= 1
