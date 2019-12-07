f = open('arquivoPratica01.txt', 'w')
f.write('Gravando uma única linha no arquivo')
for l in range(1, 101):
    f.write(f'Gravando a linha {l} \n')
f.close()
