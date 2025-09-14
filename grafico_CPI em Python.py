import matplotlib.pyplot as plt

# Texto explicativo sobre a métrica
explicacao = """
O Índice de Desempenho de Custos (CPI) mostra se um projeto está gastando bem o seu orçamento. 
Ele compara quanto de valor já foi realmente entregue (Valor Agregado - EV) com o quanto foi gasto até agora (Custo Real - AC).

- Se o CPI for maior que 1, significa que o projeto está gastando menos do que o previsto (bom sinal!).
- Se o CPI for menor que 1, quer dizer que o projeto está gastando mais do que deveria (alerta de problema!).
- Se for igual a 1, o gasto está exatamente como planejado.
"""

# Criando gráfico ilustrativo
valores = [0.4, 0.8, 1.2]
categorias = ["CPI < 1\nEstouro de orçamento", "CPI = 1\nDentro do previsto", "CPI > 1\nUso eficiente"]
cores = ["darkred", "yellow", "darkgreen"]

fig, ax = plt.subplots(figsize = (6, 3), dpi = 150, facecolor = 'none')
ax.bar(categorias, valores, color = cores, alpha = 0.7)

ax.set_ylim(0, 1.5)
ax.set_ylabel("CPI")
ax.set_title("Índice de Desempenho de Custos (CPI) de um Projeto em T.I", fontsize = 10, fontweight = "bold")

# Adicionando rótulos acima das barras
for i, v in enumerate(valores):
    ax.text(i, v + 0.05, str(v), ha = 'center', fontsize = 10, fontweight = "bold")

# Salvar imagem com fundo transparente
output_path = "E:/Repo_Codes/Projetos_Aprender_2025/1Code1Day/Imagens/cpi_grafico.png"
plt.savefig(output_path, transparent = True)
plt.show()
#plt.close()

output_path, explicacao
