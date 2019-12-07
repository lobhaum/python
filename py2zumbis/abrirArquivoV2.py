f = open('numeros.txt', 'r')
for linha in f.readlines():
    print(linha.rstrip())
f.close()
