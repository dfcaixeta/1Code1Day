''' Projeto OneCodeOneDay
Fazendo uma tabuada com vários métodos
Dia 03 - 04.mar.2025

@utor: @pythonclcoding '''

# Método 3. Tabuada usando o método de Lista Compreensiva (List Comprehension)

# Entrada/Input de dados
num = int(input('Entre com um número: '))

# Estrutura de repetição usando for ... e range em lista compreensiva
_ = [print(num, 'x', i, '=', (num * i)) for i in range(1, 11)]

print()

# EOC