''' Projeto OneCodeOneDay
Fazendo um gráfico com animação em Python
Dia XX - 03.ago.2025

@utor: @pythonclcoding '''

# Importando a biblioteca
import plotly.express as px

# Entrada/Input de dados
data = px.data.gapminder()

# Preparando o gráfico com os parâmetros de entrada
fig = px.scatter(
    data,
    x = 'gdpPercap',
    y = 'lifeExp',
    animation_frame = 'year',
    animation_group = 'country',
    size = 'pop',
    color = 'continent',
    hover_name = 'country',
    log_x = True,
    size_max = 60,
    range_x = [200, 60000],
    range_y = [20, 90],
    title = 'Animated Scatter Plot: Life Expectancy vc GDP Per Capita'
)

# Plotando o gráfico
fig.show()

# EOF
# source code --> clcoding.com