#!/usr/bin/python3

import pandas as pd # importando pandas como pd
import matplotlib.pyplot as plt # gera o grafico plotado
import seaborn as sns # importando seaborn como sns

notas = pd.read_csv('./data/ratings.csv') # falando para o pd ler o arquivo .csv

# transformando colunas em pt-br:
notas.columns = ['usuarioId', 'filmeId', 'nota', 'momento' ]

cabecalho = notas.head() # mostra os 5 primeiros elementos

print(cabecalho) # imprimindo cabecalho Panda DataFrame
print(notas['nota']) # panda series
print(notas['nota'].unique()) # panda series valores unicos da coluna
print(notas['nota'].value_counts()) # panda series valores unicos e qntidade
print(notas['nota'].mean()) # panda series total de média da coluna nota 
print('Aula: Visualizando dados com histograma e boxplot:')
print(notas.nota.head())
print(notas.nota.plot(kind='hist'))
print(f'Media: {notas.nota.mean()}')
print(f'Mediana: {notas.nota.median()}')
plt.show()
print(notas.nota.describe())
sns.boxplot(notas.nota)
plt.show()
