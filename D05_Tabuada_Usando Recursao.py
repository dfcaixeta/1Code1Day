''' Projeto OneCodeOneDay
Fazendo uma tabuada com vários métodos
Dia 05 - 04.mar.2025

@utor: @pythonclcoding '''

# Método 5. Tabuada usando o método Recursão (Recursion)

def print_table(num, times=1):
    if times > 10:
        return
    print(num, 'x', times, '=', num * times)
    print_table(num, times + 1)

num = int(input("Entre com o número: "))
print()
print_table(num)
print()

# EOC