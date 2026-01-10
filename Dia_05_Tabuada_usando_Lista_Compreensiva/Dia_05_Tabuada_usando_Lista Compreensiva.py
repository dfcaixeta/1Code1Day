''' Projeto OneCodeOneDay
Este código em Python tem como objetivo gerar e exibir a tabuada de multiplicação 
de um número fornecido pelo usuário, utilizando a estrutura de repetição for em 
conjunto com a função range(), aplicada de forma iterativa para percorrer os valores 
do intervalo definido.

Dia 05 - 10.jan.2026

@utor: @https://github.com/dfcaixeta '''

# Método 1. Tabuada usando o método de Lista Compreensiva (List Comprehension).

# Entrada de dados
num = int(input('Entre com um número: '))
print()

# Laço de repetição com lista compreensiva
_ = [print(num, 'x', i, '=', (num * i)) for i in range(1, 11)]

'''
- No trecho de código acima é usada uma list comprehension (compreensão de lista), 
  normalmente utilizada para criar listas de valores.
- Em vez de construir uma lista, o código aproveita o recurso para executar o print()
  em cada iteração.
- O range(1, 11) gera os números de 1 até 10.
- Para cada valor de i, o programa imprime a multiplicação num x i = resultado.
- O resultado da list comprehension é atribuído à variável _, que é usada como 
“variável descartável” (não será utilizada depois).
'''

# Mensagem final de encerramento
print("\nFim da tabuada!\n")

# EoC