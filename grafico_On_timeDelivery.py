import matplotlib.pyplot as plt

# Explicação sobre a métrica
explicacao = """
O indicador *On-Time Delivery Rate* mostra qual é o percentual de entregas concluídas dentro do prazo combinado.
Na prática, ele ajuda a responder a pergunta: 'Estamos conseguindo entregar no tempo que prometemos?'
Quanto maior esse percentual, maior a confiança dos clientes e a eficiência da equipe em cumprir compromissos.
"""

# Criando gráfico ilustrativo
periodos = ["Jan", "Fev", "Mar", "Abr", "Mai"]
percentuais = [62, 35, 27, 78, 94]  # Exemplo fictício

fig, ax = plt.subplots(figsize = (6, 3), dpi = 150, facecolor = 'none')

ax.plot(periodos, percentuais, marker = 'o', color = 'black', linewidth = 2)
ax.fill_between(periodos, percentuais, color = "lightgray", alpha = 0.5)

ax.set_title("On-Time Delivery Rate (%) - Percentual de entregas [...]", fontsize = 10, fontweight = 'bold')
ax.set_ylabel("Percentual (%)")
ax.set_xlabel("Período")
ax.set_ylim(0, 100)
ax.grid(True, linestyle = "--", alpha = 0.5)

# Salvar imagem com fundo transparente
output_path = "E:/Repo_Codes/Projetos_Aprender_2025/1Code1Day/Imagens/on_time_delivery_rate.png"
plt.savefig(output_path, transparent = True)
plt.show()
#plt.close()

output_path, explicacao
