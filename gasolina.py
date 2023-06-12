import pandas as pd
import seaborn as sns

data = pd.read_csv('gasolina.csv',sep=',')

grafico = sns.lineplot(data = data, x='dia',y='venda')
fig = grafico.get_figure()
fig.savefig('gasolina.png')  

grafico.set_title("Gráfico da variação do preço da gasolina")
grafico.set_ylabel('Preço da gasolina')