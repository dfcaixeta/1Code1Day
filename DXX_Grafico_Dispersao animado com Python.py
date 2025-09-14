''' Projeto OneCodeOneDay
Fazendo um gráfico de dispersão animado com Python
Dia XX - 03.ago.2025

@utor: @pythonclcoding '''

# Importando as bibliotecas
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Preparando o ambiente para os gráficos
num_points = 100
x, y = np.random.rand(2, num_points) * 10
colors = np.random.rand(num_points)
sizes = np.random.rand(num_points) * 1000

# Preparando o gráfico
fig, ax = plt.subplots()
scat = ax.scatter(x, y, c = colors, s = sizes, alpha = 0.7, cmap = 'viridis')
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# definindo a classe Animação
def animate(i):

    new_x = x + np.random.randn(num_points) * 0.1
    new_y = y + np.random.randn(num_points) * 0.1
    scat.set_offsets(np.c_[new_x, new_y])
    return scat,

ani = animation.FuncAnimation(fig, animate, frames = 100, interval = 50)

# Plotando o gráfico
plt.show()

# EOF
# source code --> clcoding.com