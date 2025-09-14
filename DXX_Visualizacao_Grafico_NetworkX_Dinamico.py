# Importando as bibliotecas
import networkx as nx
import matplotlib.pyplot as plt

# Cria um grafo direcionado
G = nx.DiGraph()

# Adiciona arestas (com direção)
G.add_edges_from([(1,2), (1,3), (2,4), (3,4)])

# Desenha o grafo
pos = nx.spring_layout(G)  # Define automaticamente a posição dos nós
nx.draw(
    G, pos,
    with_labels=True,
    node_color='lightgreen',
    node_size=1500,
    font_size=12,
    arrows=True,            # Ativa as setas
    arrowsize=20,           # Tamanho das setas
    edgecolors="black"
)

# Exibe o grafo
plt.title("Exemplo de Grafo Direcionado", fontsize=14, fontweight="bold")
plt.show()
