import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

filmes = pd.read_csv('./data/movies.csv')
filmes.columns = ['filmeId', 'titulo', 'generos']
print(filmes.head())
