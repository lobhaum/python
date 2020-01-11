import pandas as pd


resultados = pd.read_csv('./data/ms.csv')
# transformando em pt_br:
# resultados.columns = ["usuarioId", "filmeId", "nota", "momento"]
# preparando a impressão dos 5 primeiros itens:
cabecalho = resultados.head()
print(cabecalho)
# valores possiveis colocados na coluna nota:
# print(resultados['1_dezena'].unique())
# imprimindo a quantidade de vezes que o numero saiu na primeira coluna:
# print(resultados['1_dezena'].value_counts())
# preparando para imprimir os numeros por colunas:
# c1 = resultados['1_dezena'].value_counts()
# c2 = resultados['2_dezena'].value_counts()
# c3 = resultados['3_dezena'].value_counts()
# c4 = resultados['4_dezena'].value_counts()
# c5 = resultados['5_dezena'].value_counts()
# c6 = resultados['6_dezena'].value_counts()
# imprimindo por colunas:
# print (f'1o-{c1} 2o-{c2} 3o-{c3} 4o-{c4} 5o-{c5} 6o-{c6}')
vetor = resultados['1_dezena', '2_dezena', '3_dezena', '4_dezena', 
                   '5_dezena', '6_dezena']
vetor.describe()
