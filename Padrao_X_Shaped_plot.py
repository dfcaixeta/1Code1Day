import matplotlib.pyplot as plt

size = 10
fig, ax = plt.subplots(figsize=(6, 6))

for i in range(size):
    plt.plot([i, size - 1 - i], [i, i], 'bo')
    plt.plot([i, size - 1 - i],
             [size - 1 - i, size - 1 - i], 'bo')
    
    ax.set_xlim(-1, size)
    ax.set_ylim(-1, size)

    #ax.set_xticks([])
    #ax.set_yticks([])
    ax.set_frame_on(True)

plt.title("Gráfico com Padrão Cruzado")
plt.show()

# EOF
# source code --> clcoding.com