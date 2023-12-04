import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dados_excel = pd.read_excel('C:\planilha1.xlsx') //Caminho para o arquivo

x = dados_excel['X']
y = dados_excel['Y']

indices = range(len(x))

plt.figure(figsize=(10, 6))
plt.bar(indices, x, width=0.4, label='Coluna X', color='blue')
plt.bar([i + 0.4 for i in indices], y, width=0.4, label='Coluna Y', color='green')

plt.xlabel('Índices')
plt.ylabel('Valores')
plt.title('Gráfico de Barras para Colunas X e Y')
plt.xticks([i + 0.2 for i in indices], indices)  # Posiciona os índices no meio das barras
plt.legend()
plt.show()

plt.figure(figsize=(10, 6))
sns.barplot(x=[f'Índice {i}' for i in indices], y=x, color='blue', label='Coluna X')
sns.barplot(x=[f'Índice {i}' for i in indices], y=y, color='green', label='Coluna Y', bottom=x)

plt.xlabel('Índices')
plt.ylabel('Valores')
plt.title('Gráfico de Barras para Colunas X e Y')
plt.legend()
plt.show()
