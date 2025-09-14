import matplotlib.pyplot as plt

# Explicação sobre a métrica
explicacao = """
O EAC (Estimate At Completion) é uma estimativa de quanto o projeto deve custar 
quando for finalizado. Ele considera os custos já realizados até o momento e 
projeta quanto ainda será necessário gastar para concluir todas as atividades. 
É como olhar para o futuro do orçamento e responder: 
'Se continuarmos nesse ritmo, quanto vai custar o projeto inteiro ao final?'.
"""

# Criando gráfico ilustrativo sobre EAC
etapas = ["Planejado", "Custo Atual", "Projeção Final"]
valores = [60000, 40000, 100000]  # Exemplo fictício em R$

fig, ax = plt.subplots(figsize = (6, 3), dpi = 150, facecolor = 'none')

bars = ax.bar(etapas, valores, color = ["green", "blue", "orange"])
ax.set_title("Exemplo de EAC (Estimate At Completion)", fontsize = 10, fontweight = 'bold')
ax.set_ylabel("Custos (R$)")

# Definir limites dos eixos
ax.set_ylim(0, 120000)  # Eixo Y: de 0 até 120 mil
ax.set_xlim(-0.5, len(etapas) - 0.5)  # Eixo X: dá uma margem visual nas categorias

# Adicionar rótulos nas barras
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'R$ {height:,}'.replace(",", "."),
                xy = (bar.get_x() + bar.get_width() / 2, height),
                xytext = (0, 5),
                textcoords = "offset points",
                ha = 'center', va = 'bottom', fontsize = 8)

# Salvar imagem com fundo transparente
output_path = "E:/Repo_Codes/Projetos_Aprender_2025/1Code1Day/Imagens/eac_grafico.png"
plt.savefig(output_path, transparent = True)
plt.show()
#plt.close()

output_path, explicacao
