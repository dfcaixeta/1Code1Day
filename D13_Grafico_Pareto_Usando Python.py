''' Projeto OneCodeOneDay
Fazendo um Gráfico de Pareto usando Matplotlib.
Dia 13 - 25.mai.2025

@utor: @pythonclcoding '''

import matplotlib.pyplot as plt

# Preparando os dados de entrada (Input).
categorias = ['Categoria 1', 'Categoria 2', 'Categoria 3', 'Categoria 4']
valores = [80, 20, 50, 30]

# Parâmetros do Eixo 1
fig, eixo1 = plt.subplots()
eixo1.bar(categorias, valores, color = 'gray')
eixo1.set_ylabel('Valores', color = 'gray')
eixo1.tick_params('y', colors = 'gray')

# Parâmetros do Eixo 2
eixo2 = eixo1.twinx()
valores_acumulados = [sum(valores[:i + 1]) for i in range(len(valores))]
eixo2.plot(categorias, valores_acumulados, color = 'green', marker = 'o')
eixo2.set_ylabel('Valores Acumulados', color = 'green')
eixo2.tick_params('y', colors = 'green')

# Inserindo o título no Gráfico
plt.title('Gráfico de Pareto')

# Plotando o gráfico
plt.show()

# EOC