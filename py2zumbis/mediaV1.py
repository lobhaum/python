arr = [10, 9.7, 9.3, 4.3, 5, 6, 7, 8, 9, 10]
c = 0
m = 0
while c <= 4:
    m += arr[c]
    c = c + 1
print(f'A média das notas é {m / c :.1f}')
