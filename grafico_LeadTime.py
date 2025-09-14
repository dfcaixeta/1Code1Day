import matplotlib.pyplot as plt

# Explicação sobre a métrica
explicacao = """
O Lead Time é o tempo total que leva desde o momento em que alguém faz uma solicitação 
— como pedir uma nova funcionalidade de software — até o momento em que essa entrega 
está pronta para uso. 
Ele inclui todas as etapas do processo: análise, desenvolvimento, testes e entrega final. 
Quanto menor o Lead Time, mais rápido o projeto atende às necessidades do cliente.
"""

# Criando um gráfico ilustrativo sobre Lead Time
etapas = ["Solicitação", "Análise", "Desenvolvimento", "Testes", "Entrega"]
tempos = [1, 4, 8, 2, 1]  # Exemplo fictício em dias

fig, ax = plt.subplots(figsize=(6, 6), dpi = 150, facecolor = 'none')

ax.plot(etapas, tempos, marker = 'o', color = 'black', linewidth = 2)
ax.fill_between(etapas, tempos, color = "lightgray", alpha = 0.5)

ax.set_title("Exemplo de Lead Time em um Projeto de Software", fontsize = 12, fontweight = 'bold')
ax.set_ylabel("Dias")
ax.set_xlabel("Etapas do Processo")
ax.grid(True, linestyle = "--", alpha = 0.5)

# Salvar imagem com fundo transparente
output_path = "E:/Repo_Codes/Projetos_Aprender_2025/1Code1Day/Imagens/lead_time_grafico.png"
plt.savefig(output_path, transparent = True)
plt.show()
#plt.close()



output_path, explicacao
