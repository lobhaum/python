letras = []
i = 1
while i <= 10:
    letras.append(input('Letra: '))
    i += 1
i = 0
c = 0
while i <= 9:
    if letras[i] not in 'aeiou':
        c += 1
    i += 1
print(f'Foram lidos {c} consoantes')
