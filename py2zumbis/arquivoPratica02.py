import random

f = open('arquivoPratica02.txt', 'w')
for l in range(1, 100):
    r = random.randrange(100)
    f.write(f'O número randomico foi {r} \n')
f.close()
