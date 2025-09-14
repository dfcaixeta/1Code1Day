''' Projeto OneCodeOneDay
Fazendo um Gráfico básico de linha usando Matplotlib.
Dia 12 - 25.mai.2025

@utor: @pythonclcoding '''

# Importando a biblioteca.
import matplotlib.pyplot as plt

# Dados de entrada.
x = [1, 2, 3, 4, 5] # Eixo x
y = [2, 3, 5, 7, 11] # Eixo y

# Preparando o gráfico.
plt.plot(x, y, marker = 'o', color='green')
plt.title('Gráfico Básico de Linha')
plt.xlabel('Eixo x')
plt.ylabel('Eixo y')
plt.grid(True)

# Plotando o gráfico.
plt.show()

# EOC