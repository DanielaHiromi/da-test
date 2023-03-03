import pandas as pd
import seaborn as sns

gasolina_df = pd.read_csv('gasolina.csv', sep=',')

with sns.axes_style('whitegrid'):

  grafico = sns.lineplot(data=gasolina_df, x="dia", y="venda", palette="pastel")
  grafico.set(title='PREÇO MÉDIO DA GASOLINA NA CIDADE DE SÃO PAULO EM JULHO DE 2021', xlabel='DIA', ylabel='PREÇO (R$)');
  