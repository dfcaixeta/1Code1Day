''' Projeto OneCodeOneDay
Programa em Python que cria um gráfico em rede
Dia XX - 14.set.2025

@utor: @pythonclcoding '''

# Importando a biblioteca NetworkX
import networkx as nx # É uma biblioteca usada para criar e analisar grafos/redes (ligação entre nós).
import matplotlib.pyplot as plt

# Cria um gráfico em branco
G = nx.Graph()

# Conecta os nós da rede.
G.add_edges_from([(1,2), (1,3), (2,4), (3,4)]) # Adiciona as arestas

# Desenha o gráfico com os elementos textuais
nx.draw(G, with_labels = True, node_color = 'skyblue', node_size = 1500, font_size = 12)

''' Explicação desse trecho de código:
nx.draw() --> Desenha o gráfico.
with_labels = True --> Mostra os números dos nós (1,2,3,4).
node_color = 'skyblue' --> Cor dos nós (Azul claro).
node_size = 1500 --> Tamanho dos nós.
font_size = 12 --> Tamanho da fonte dos rótulos. '''

# Plota o gráfico na tela
plt.show() # Exibe o grafo em uma janela.


'''
Esse código é uma representação visual de um grafo não direcionado (sem setas), usado
em áreas como análise de redes sociais, caminhos em grafos, mapas de conexões etc.

'''

# EOC