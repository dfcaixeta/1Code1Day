''' Projeto OneCodeOneDay
Fazendo um gráfico padrão Escala de Peixe (Fish Scale)
Dia 09 - 18.jul.2025

@utor: @pythonclcoding '''

# Importando as bibliotecas
import numpy as np
import matplotlib.pyplot as plt

# Preparando o gráfico
rows, cols = 10, 10
radius = 1
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim (0, cols * radius)
ax.set_ylim (0, (rows + 0.5) * (radius / 2))
ax.set_aspect('equal')
ax.axis('off')
colors = ['#6FA3EF', '#3D7A9E', '#F4C542', '#E96A64', '#9C5E7F']

for row in range(rows):
    for col in range(cols):
        x = col * radius
        y = row * (radius / 2)
        if row % 2 == 1:
            x = radius / 2
        semicircle = plt.Circle((x, y), radius, color = np.random.choice(colors), clip_on= False)
        ax.add_patch(semicircle)

# Inserindo o título do gráfico
plt.title('Fish Scale Patter', fontsize=16, fontweight='bold', color='navy', pad=15)

# Plotando o gráfico
plt.show()


# EOC
