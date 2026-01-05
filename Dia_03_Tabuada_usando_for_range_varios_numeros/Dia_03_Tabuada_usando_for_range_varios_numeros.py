''' Projeto OneCodeOneDay
Esse código em Python tem como finalidade gerar e exibir variás tabuadas de multiplicação 
de números informados e com o limite de cálculos fornecido pelo usuário.

Tabuada usando a Estrutura de repetição for ...  e com a função range()
Dia 03 - 04.jan.2026

@utor: @https://github.com/dfcaixeta'''

# Método 3. Várias tabuada usando loop com for ... com a função range()

# Entrada de dados múltiplos (Input).
num = input("Digite os números de entradas separados por vírgula: ")

# Define o limite final para a Tabuada.
limite = int(input("Até qual número deseja calcular a tabuada?: "))

# Transformar a string em lista de inteiros
lista_num = [int(n.strip()) for n in num.split(",")]

print("\nGerando as tabuadas ...")

# Laço externo que percorre cada número da lista
for num in lista_num:
    print(f"\nTabuada do {num} até o {limite}")
    for i in range(1, limite + 1):
        print(f"{num} x {i} = {num * i}")
    print("-" * 30) # Separador visual

# Mensagem final de encerramento
print("\nFim da tabuada!\n")

# EoC