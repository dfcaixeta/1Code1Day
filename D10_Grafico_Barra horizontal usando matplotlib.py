''' Projeto OneCodeOneDay
Fazendo um gráfico de barra horizontal usando a biblioteca Matplotlib
Dia 10 - 05.mar.2025

@utor: @pythonclcoding '''

# Importando as bibliotecas ...
import numpy as np
import matplotlib.pyplot as plt

# Preparando os dados
categorias = ['A', 'B', 'C', 'D']
valores = [3, 7, 1, 5]

# Preparando os dados e plotando o gráfico
plt.barh(categorias, valores, color='purple')
plt.ylabel('Categorias')
plt.xlabel('Valores')

plt.show()

# EOC