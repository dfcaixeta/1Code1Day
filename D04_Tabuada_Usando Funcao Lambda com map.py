''' Projeto OneCodeOneDay
Fazendo uma tabuada com vários métodos
Dia 04 - 04.mar.2025

@utor: @pythonclcoding '''

# Método 4. Tabuada usando o método Função Lambda com Map ...

num = int(input("Entre com um número: "))

print()
table = list(map(lambda x: num * x, range(1, 11)))
for i in range(10):
    print(num, 'x', i + 1, '=', table[i])
print()

# EOC