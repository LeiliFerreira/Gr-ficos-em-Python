import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dados_excel = pd.read_excel('C:\planilha1.xlsx') //Caminho para o arquivo

print(dados_excel.head())

x = dados_excel['X']
y = dados_excel['Y']

plt.figure(figsize=(8, 6))
plt.plot(x, label='Dados da Coluna X', linestyle='-', color='blue', linewidth=2)
plt.plot(y, label='Dados da Coluna Y', linestyle='--', color='green', linewidth=2)

plt.xlabel('Índice')
plt.ylabel('Valores')
plt.title('Gráfico de linhas para colunas X e Y')

plt.legend()
plt.grid(True)
plt.show()
