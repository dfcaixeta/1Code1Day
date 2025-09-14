''' Projeto OneCodeOneDay
Fazendo uma tabuada com vários métodos
Dia 08 - 04.mar.2025

@utor: @pythonclcoding '''

# Método 8. Tabuada usando o f-string e join.

# Entrada de dados.
num = int(input("Entre com o número: "))

# Criando uma representação de string de tabela para a multiplicação
table = '\n'.join([f"{num} x {i} = {num * i}" for i in range(1, 11)])

# Imprimindo o resultado da multiplicação
print()
print(table)
print()

# EOC