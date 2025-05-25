''' Projeto OneCodeOneDay
Fazendo uma tabuada com vários métodos
Dia 07 - 04.mar.2025

@utor: @pythonclcoding '''

# Método 7.Tabuada usando o método Pandas DataFrame.

# Importando a biblioteca Numpy
import pandas as pd

num = int(input("Entre com o número: "))
multiplier = list(range(1, 11))

print()

# Criando um DataFrame sem as especificações dos labels da coluna
df = pd.DataFrame({num: [num * i for i in multiplier]})

# Imprimindo o DataFrame sem os labels da coluna
print(df.to_string(header=False, index=False))
print()

# EOC