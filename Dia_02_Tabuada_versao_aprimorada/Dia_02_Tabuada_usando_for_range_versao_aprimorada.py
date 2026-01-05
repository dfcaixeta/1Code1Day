''' Projeto OneCodeOneDay
Esse código em Python tem como finalidade gerar e exibir a tabuada de multiplicação 
de um número informado e com o limite de cálculos fornecido pelo usuário.

Fazendo uma tabuada usando a Estrutura de repetição for ...  e com a função range()
Dia 02 - 04.jan.2026

@utor: @https://github.com/dfcaixeta'''

# Método 2.Tabuada usando loop com for ... com a função range()

# Entrada de dado (Input).
num = int(input("Entre com um número: "))

# Define o limite final para a Tabuada.
limite = int(input("Até qual número deseja calcular a tabuada?: "))

# Imprime na tela as opções escolhidas ...
print(f"\nTabuada do {num} até o {limite}:\n")

# Estrutura de repetição for ... com a função range.
for i in range(1, limite + 1):
    print(f"{num} x {i} = {num * i}")

# Mensagem final de encerramento
print("\nFim da tabuada!")
print()

# EoC