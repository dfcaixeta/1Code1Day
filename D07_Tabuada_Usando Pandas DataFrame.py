''' Projeto OneCodeOneDay
Fazendo uma tabuada com o método Pandas DataFrame
Dia 07 - 04.mar.2025

@utor: @pythonclcoding '''

# Método 7.Tabuada usando o método Pandas DataFrame.

# Importando a biblioteca Numpy
import pandas as pd

# Entrada de dados (Input data)
num = int(input("Entre com o número: "))
print()

# Preparando a lista de números para a multiplicação
mult = list(range(1, 11))

# Criando um DataFrame sem as especificações dos labels da coluna
df = pd.DataFrame({num: [num * i for i in mult]})

# Imprimindo o DataFrame sem os labels da coluna
print(df.to_string(header=False, index=False))
print()

# EOC