''' Projeto OneCodeOneDay
Fazendo uma tabuada usando a Estrutura de repetição for ... (loop)
Dia 01 - 05.fev.2025

@utor: @pythonclcoding '''

# Método 1.Tabuada usando loop com for ...

# Entrada/Input de dados
num = int(input("Entre com um número: "))

# Estrutura de repetição for ... com a função range.
for i in range (1, 11):
    print (num, 'x', i, '=', (num * i))
print()

# EOC