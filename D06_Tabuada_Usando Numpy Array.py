''' Projeto OneCodeOneDay
Fazendo uma tabuada com vários métodos
Dia 06 - 04.mar.2025

@utor: @pythonclcoding '''

# Método 6. Tabuada usando o método Numpy Array.

# Importando a biblioteca Numpy
import numpy as np

num = int(input("Entre com o número: "))
multiplier = np.arange(1, 11)
result = np.outer([num], multiplier)

# Imprimindo antes uma Matrix Transposta
result_transposed = result.T
print()

# Formate a saída para remover colchetes
for row in result_transposed:
    print(*row)
print()

# EOC