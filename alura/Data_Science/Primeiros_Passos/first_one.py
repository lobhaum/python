import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

notas = pd.read_csv('./data/ratings.csv')
# transformando em pt_br:
notas.columns = ["usuarioId", "filmeId", "nota", "momento"]
# preparando a impressão dos 5 primeiros itens:
cabecalho = notas.head()
print(cabecalho)
# valores possiveis colocados na coluna nota:
# print(notas['nota'].unique())
notas.nota.plot(kind='hist')
sns.boxplot(notas.nota)
plt.show()
