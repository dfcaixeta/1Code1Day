import matplotlib.pyplot as plt

# Explicação sobre a métrica
explicacao = """
Produtividade em projetos ágeis é como medir a "batida do coração" do time: 
ela mostra se o trabalho está fluindo bem e em ritmo sustentável.
- Velocidade da Equipe (Scrum Velocity): é a média de pontos de história (tarefas com esforço estimado) 
  que a equipe consegue entregar a cada sprint. Ajuda a prever quanto trabalho pode ser feito no futuro.
- Throughput: é o número de itens realmente concluídos em um período (por exemplo, em uma semana ou sprint). 
  Ele mostra a quantidade de entregas finalizadas, sem olhar para o tamanho ou esforço.
"""

# Dados fictícios para o gráfico
sprints = ["Sprint 1", "Sprint 2", "Sprint 3", "Sprint 4"]
velocity = [20, 25, 22, 27]  # Pontos de história entregues
throughput = [5, 7, 6, 8]    # Itens concluídos

# Criar gráfico comparativo
fig, ax = plt.subplots(figsize = (6, 3), dpi = 150, facecolor = 'none')

ax.plot(sprints, velocity, marker ='o', label = "Velocidade (pontos)", color = "blue", linewidth = 1)
ax.plot(sprints, throughput, marker = 's', label = "Throughput (itens)", color = "red", linestyle = "--", linewidth = 1)

ax.set_title("Produtividade da Equipe (Velocity x Throughput)", fontsize = 10, fontweight='bold')
ax.set_ylabel(("Quantidade"), fontsize = 11)
ax.set_xlabel(("Sprints"), fontsize = 11)
ax.legend(fontsize = 8)
ax.grid(True, linestyle = "--", alpha = 0.6)

# Salvar com fundo transparente
output_path = "E:/Repo_Codes/Projetos_Aprender_2025/1Code1Day/Imagens/produtividade_velocity_throughput.png"
plt.savefig(output_path, transparent = True)
plt.show()
#plt.close()

output_path, explicacao
