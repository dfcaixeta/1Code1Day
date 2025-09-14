import matplotlib.pyplot as plt

# Explicação sobre a métrica
explicacao = """
O Cycle Time é o tempo que uma tarefa leva para ser concluída a partir do momento em que começa a ser trabalhada
até sua finalização. Imagine que você pediu para um time de desenvolvimento corrigir um bug. O Cycle Time começa
no instante em que o desenvolvedor inicia o trabalho e termina quando a correção está pronta e entregue.
Quanto menor o Cycle Time, mais ágil é o processo de produção.
"""

# Criar dados para gráfico
fases = ["Início do trabalho", "Desenvolvimento", "Testes", "Entrega"]
tempos = [0, 7, 4, 2]  # valores fictícios representando dias

# Criar gráfico
fig, ax = plt.subplots(figsize = (6, 3), dpi = 150, facecolor = 'none')
ax.plot(fases, tempos, marker = 'o', color ='black', linewidth = 2)
ax.fill_between(fases, tempos, alpha = 0.1, color = 'lightgray')

# Ajustes de estilo
ax.set_title("Cycle Time - Corrindo um bug [...]", fontsize = 12, fontweight = 'bold')
ax.set_ylabel("Dias")
ax.set_xlabel("Etapas")
ax.grid(True, linestyle='--', alpha=0.5)

# Salvar com fundo transparente
output_path = 'E:/Repo_Codes/Projetos_Aprender_2025/1Code1Day/cycle_time_grafico.png'
plt.savefig(output_path, transparent = True)
plt.show()
#plt.close()

output_path, explicacao
