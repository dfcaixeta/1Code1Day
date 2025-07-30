''' Projeto OneCodeOneDay
Fazer um Gráfico Padrão Cruzado usando Python.
Dia 15 - 25.mai.2025

@utor: @pythonclcoding '''

# Importando a biblioteca matplotlib
import matplotlib.pyplot as plt

# Preparando os eixos.
size = 10
fig, ax = plt.subplots(figsize=(6, 6))

for i in range(size):
    plt.plot([i, size - 1 - i], [i, i], 'bo')
    plt.plot([i, size - 1 - i],
             [size - 1 - i, size - 1 - i], 'bo')
    
    ax.set_xlim(-1, size)
    ax.set_ylim(-1, size)

    # Gera o gráfico sem os valores dos eixos.
    #ax.set_xticks([])
    #ax.set_yticks([])

    ax.set_frame_on(True)

# Imprimindo o título do gráfico
plt.title("Gráfico com Padrão Cruzado")

# Plotando o gráfico
plt.show()

# EOF
# source code --> clcoding.com