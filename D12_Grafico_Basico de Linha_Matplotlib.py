''' Projeto OneCodeOneDay
Fazendo um Gráfico básico de linha usando Matplotlib.
Dia 12 - 25.mai.2025

@utor: @pythonclcoding '''

# Importando a biblioteca.
import matplotlib.pyplot as plt

# Preparando os dados de entrada (Input).
x = [1, 2, 3, 4, 5] # Eixo x
y = [2, 3, 5, 7, 11] # Eixo y

# Preparando o gráfico.
plt.plot(x, y, marker = 'o', color='green') # Plota os elementos do gráfico.
plt.title('Gráfico Básico de Linha') # Plota o título do gráfico.
plt.xlabel('Eixo x') # Plota o Eixo x.
plt.ylabel('Eixo y') # Plot o Eixo y.
plt.grid(True) # Plota o grid no gráfico.

# Plotando o gráfico.
plt.show()

# EOC