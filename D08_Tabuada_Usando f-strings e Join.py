''' Projeto OneCodeOneDay
Fazendo uma tabuada com vários métodos
Dia 08 - 04.mar.2025

@utor: @pythonclcoding '''

# Método 8. Tabuada usando o método Pandas DataFrame.

num = int(input("Entre com o número: "))

# Criando uma representação de string de tabela de multiplicação
table = '\n'.join([f"{num} x {i} = {num * i}" for i in range(1, 11)])

# Imprimindo a tabela de multiplicação
print()
print(table)
print()

# EOC