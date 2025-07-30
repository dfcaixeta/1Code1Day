''' Projeto OneCodeOneDay
Fazer um calendário usando Python.
Dia 14 - 25.mai.2025

@utor: @pythonclcoding '''

# Importando a classe TexCalendar do módulo calendar
from calendar import TextCalendar

# Solicita que o usuário digite o ano
ano = int(input('Digite o ano: '))

# Instância da classe TextCalendar que será usada para formatar o calendáro
calendario = TextCalendar()

# Imprime o calendário na tela
print(calendario.formatyear(ano, 2, 1, 8, 3))

# EOC

'''
Parâmetros do formatyear:
ano: o ano a ser exibido.
2: largura de cada mês (espaçamento horizontal entre colunas de dias).
1: número de linhas entre meses.
8: largura de cada coluna de mês.
3: número de meses por linha (layout com 3 colunas de meses por linha).
'''