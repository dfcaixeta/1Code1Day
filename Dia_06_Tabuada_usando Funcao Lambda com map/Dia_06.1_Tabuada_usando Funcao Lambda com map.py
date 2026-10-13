''' Projeto OneCodeOneDay
Esta aplicação tem como objetivo gerar e exibir a tabuada de multiplicação 
de um número fornecido pelo usuário, utilizando a estrutura de repetição for em 
conjunto com a função lâmbda como map() e range(), aplicada de forma iterativa para percorrer os valores 
do intervalo definido.

Dia 06 - 22.jan.2026 
       - 10.out.2026 (Modificado)

@utor: https://github.com/dfcaixeta/1Code1Day '''

# Método 1. Tabuada usando o método Função Lambda com Map ...

# Entrada de dados.
num = int(input("Entre com um número: "))

# Estrutura utilizando a função lambda e range().
tabela = list(map(lambda x: num * x, range(1, 11)))

'''
No trecho do código acima, a função tem uma lista de valores. Explicando cada
comando:

    - range(1, 11) gera os números de 1 até 10.
    - lambda x: num * x define uma função anônima que multiplica o número digitado (num)
      por cada valor x do intervalo.
    - map(...) aplica essa função a todos os valores do range.
    - list(...) transforma o resultado em uma lista chamada table, que contém os 
      produtos da tabuada.
        ➡️ Exemplo: se num = 7, então table = [7, 14, 21, ..., 70]
'''

# Estrutura de repetição for e range().
for i in range(10):
    print(num, 'x', i + 1, '=', tabela[i])

''' Explicando o trecho de código acima:
    - O laço percorre os índices de 0 a 9 (10 elementos).
    - Em cada repetição:
        - i + 1 representa o incremento multiplicador (de 1 a 10).
        - table[i] acessa o resultado correspondente da lista. '''

# Mensagem final de encerramento
print("\nFim da tabuada!\n")

# EoC