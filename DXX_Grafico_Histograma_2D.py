''' Projeto OneCodeOneDay
Fazendo um gráfico de Histograma 2D com Python
Dia XX - 03.ago.2025

@utor: @pythonclcoding '''

# Importando as bibliotecas
import numpy as np
import matplotlib.pyplot as plt

# Organizando os eixos
x = np.random.randn(1000)
y = np.random.randn(1000)

# Organizando o gráfico
plt.hist2d(x, y, bins = 30, cmap = 'plasma')
plt.colorbar(label = 'Frequência')
plt.title('Histograma 2D')
plt.xlabel('Eixo x')
plt.ylabel('Eixo y')

# Plotando o gráfico
plt.show()

# EOF
# source code --> clcoding.com