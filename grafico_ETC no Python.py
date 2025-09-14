import matplotlib.pyplot as plt

# Explicação sobre a métrica
explicacao = """
O ETC (Estimate To Complete) é a estimativa de quanto ainda será necessário gastar 
para concluir um projeto. Em outras palavras, é o valor previsto para terminar tudo 
o que falta, considerando os recursos, prazos e custos planejados. 
Ele ajuda gestores a responder a pergunta: 'Quanto ainda precisamos investir para 
chegar até o fim do projeto?'.
"""

# Criando um gráfico ilustrativo sobre ETC
etapas = ["Início", "Planejamento", "Execução", "Controle", "Encerramento"]
custo_previsto = [0, 20000, 50000, 70000, 100000]  # valores fictícios
custo_real = [0, 25000, 57000, 80000, None]  # até o momento
etc_estimado = [None, None, None, None, 30000]  # valor necessário para concluir

fig, ax = plt.subplots(figsize = (6, 3), dpi = 150, facecolor = 'none')

# Plotando custos
ax.plot(etapas, custo_previsto, marker = 'o', label = "Custo Previsto", color = "black")
ax.plot(etapas[:-1], custo_real[:-1], marker = 'o', linestyle = "--", label = "Custo Real", color = "blue")

# Representando ETC no ponto final
ax.bar("Encerramento", etc_estimado[-1], bottom = 75000, color = "lightgreen", alpha = 0.7, label = "ETC Estimado")

ax.set_title("Exemplo de ETC (Estimate To Complete)", fontsize = 10, fontweight = 'bold')
ax.set_ylabel("Custo (R$)")
ax.grid(True, linestyle = "--", alpha = 0.5)
ax.legend(fontsize = 8)

# Salvar imagem com fundo transparente
output_path = "E:/Repo_Codes/Projetos_Aprender_2025/1Code1Day/Imagens/etc_grafico.png"
plt.savefig(output_path, transparent = True)
plt.show()
#plt.close()

output_path, explicacao
