''' Projeto OneCodeOneDay
Fazendo uma tabuada com vários métodos
Dia 05 - 04.mar.2025

@utor: @pythonclcoding '''

# Método 5. Tabuada usando o método Recursão (Recursion)

# Define a função recursiva para repetição de uma tarefa
def print_table(num, times = 1): # num: número para a tabuada; times: multiplicador
    if times > 10: # Quando o times ultrapassa 10, a recursão é encerrada.
        return     # Evita chamadas infinitas.

    print(num, 'x', times, '=', (num * times)) # Exibe a multiplicação no formato tabuada.
    print_table(num, times + 1) # Chamada recursiva incrementando times em 1.

# Entrada/Input de dados
num = int(input("Entre com o número: "))

# Saída/Output dos dados processados
print_table(num)
print()

''' Resumo:
 - O código usa recursão para imprimir a tabuada do número informado pelo usuário.
- A função se repete automaticamente até atingir o multiplicador 10.
- É uma alternativa à estrutura de repetição for. '''

# EOC