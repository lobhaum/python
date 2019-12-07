vogais = 'aeiou'
i = 'Cotonetes'
for c in len(i):
    if i[c] in vogais:
        troca = troca + '*'
    else:
        troca = troca + i[c]
    c += 1
print(i)
