import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dados_excel = pd.read_excel('C:\planilha1.xlsx')

print(dados_excel.head())

x = dados_excel['X']
y = dados_excel['Y']

dados_combinados = pd.concat([x, y], axis=1)

dados_para_pizza = dados_combinados.iloc[0]

plt.figure(figsize=(8, 6))
plt.pie(dados_para_pizza, labels=dados_para_pizza.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('husl'))
plt.title('Gráfico de pizza para colunas X e Y')

plt.show()


