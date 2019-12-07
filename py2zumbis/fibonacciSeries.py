a, b = 0, 1
# for a in range(10):
while a < 10000:
    print(a, end=' ')
    a, b = b, a + b
