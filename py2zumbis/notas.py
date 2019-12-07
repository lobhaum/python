notas = []
c = 0
while c <= 3:
    i = float(input('Digite uma nota: '))
    notas.append(i) # acrescenta itens ao final da lista
    c += 1
c = 0
m = 0
while c <= 3:
    m += notas[c] # m recebe os valores da lista e os soma
    c += 1 # c anda posições na lista até chegar na posição 3
print(f'Notas: {notas}', end='')
print(f'Média final: {m/4}')
