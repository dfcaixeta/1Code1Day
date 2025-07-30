''' Projeto OneCodeOneDay
Fazendo uma tabuada com o método Numpy Array.
Dia 06 - 04.mar.2025

@utor: @pythonclcoding '''

# Método 6. Tabuada usando o método Numpy Array.
''' Esse código em Python utiliza a biblioteca NumPy para calcular e exibir a
tabuada de um número fornecido pelo usuário, usando conceitos de arrays, 
multiplicação vetorial e matriz transposta. '''

# Importando a biblioteca Numpy
import numpy as np

# Entrada/Input de dados
num = int(input("Entre com o número: "))

# Criação de um vetor multiplicador de 1 a 10 (inclusive) que será o multiplicado
# da tabuada
multiplicador = np.arange (1, 11)

# Cálculo da tabuada
resultado = np.outer([num], multiplicador)

''' Explicando o techo acima:
 - np.outer(a, b) calcula o produto externo entre dois vetores.
 - O resultado será uma matriz 1 x 10 (array 2D - bidimensional). '''

# Transportando o resultado para uma matriz transposta
resultado_transposta = resultado.T

# Formatando a saída/output para remoção dos colchetes da matriz
for row in resultado_transposta:
    print(*row)

print()

''' Resumo do código:
 - Recebe um número.
 - Gera a tabuada de 1 a 10 usando NumPy.
 - Organiza o resultado como uma matriz transposta.
 - Imprime os valores da tabuada em formato limpo, um número por linha.'''

# EOC