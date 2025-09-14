import matplotlib.pyplot as plt

metricas = ["Defeitos por Entrega", "Taxa de Retrabalho"]
valores = [7, 21]  # exemplo fictício: 7 defeitos e 21% de retrabalho

fig, ax = plt.subplots(figsize = (6, 3), dpi = 150, facecolor = 'none')

bars = ax.bar(metricas, valores, color = "gray", edgecolor = "black")
ax.set_title("Exemplo de Métricas de Qualidade", fontsize = 10, fontweight = "bold")
ax.set_ylabel("Quantidade / Percentual")

# Definir limites dos eixos
ax.set_ylim(0, 40)  # Eixo Y: de 0 até 40%
ax.set_xlim(-0.5, len(metricas) - 0.5)  # Eixo X: dá uma margem visual nas categorias

# adicionando valores em cima das barras
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2., height + 0.5,
            f'{height}', ha = 'center', fontsize = 8, fontweight = "bold", va = 'bottom')

# Salvar imagem com fundo transparente
output_path = "E:/Repo_Codes/Projetos_Aprender_2025/1Code1Day/Imagens/metricas_qualidade.png"
plt.savefig(output_path, transparent = True)
plt.show()
#plt.close()

