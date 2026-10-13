''' Projeto OneCodeOneDay
Esta aplicação tem como objetivo gerar e exibir a tabuada de multiplicação 
de um número fornecido pelo usuário, utilizando de forma direta a estrutura da
função lâmbda como map() e range(), aplicada de forma iterativa para percorrer os valores 
do intervalo definido.

Dia 06 - 22.jan.2026

@utor: https://github.com/dfcaixeta/1Code1Day '''

# Método 2. Tabuada usando o método Função Lambda com Map - Versão enxuta (Lean Code).

# Entrada de dados.
num = int(input("Entre com um número: "))

# Imprime na tela a mensagem do número escolhido.
print(f"\nTabuada do {num}:")

# Estrutura com o uso direto da função lambda, map() e range().
list(map(lambda x: print(f"{num} x {x} = {num * x}"), range(1, 11)))

# Mensagem final de encerramento
print("\nFim da tabuada!\n")

# EoC