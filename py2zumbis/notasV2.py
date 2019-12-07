c = 0
n = []
s = 0
m = s / 4
while c <= 3:
    r = float(input('Digite uma nota: '))
    n.append(r)
    s += r
    c += 1
print(f'As notas foram {n[:]} e a média foi: {s / 4}')
