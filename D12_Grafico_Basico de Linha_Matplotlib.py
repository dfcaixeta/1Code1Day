''' Projeto OneCodeOneDay
Fazendo um Gráfico Básico de Linha usando Matplotlib.
Dia 12 - 25.mai.2025

@utor: @pythonclcoding '''

# Importando a biblioteca
import matplotlib.pyplot as plt

# Amostra de dados
x = [1, 2, 3, 4, 5] # Eixo x
y = [2, 3, 5, 7, 11] # Eixo y

# Plotando o Gráfico de Linha
plt.plot(x, y, marker = 'o', color='green')
plt.title('Gráfico Básico de Linha')
plt.xlabel('Eixo x')
plt.ylabel('Eixo y')
plt.grid(True)
plt.show()

# EOC