print('=-='*15)
print('Analisador de Triangulos')
print('=-='*15)
i1 = float(input('Primeiro Segmento: '))
i2 = float(input('Segundo Segmento: '))
i3 = float(input('Terceiro Segmento: '))
if i1 < i2 + i3 and i2 < i1 + i3 and i3 < i1 + i2:
    print('Segmentos formam triangulo')
else:
    print('Segmentos não formam triangulo')