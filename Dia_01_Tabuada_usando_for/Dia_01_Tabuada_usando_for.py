''' Projeto OneCodeOneDay
Esse código em Python tem como finalidade gerar e exibir a tabuada de multiplicação 
de um número informado pelo usuário utilizando a estrutura de repetição for ... e a função range()

Dia 01 - 04.jan.2026

@utor: @https://github.com/dfcaixeta'''

# Método 1.Tabuada usando loop com for ...

# Entrada de dado
num = int(input("Entre com um número: "))

# Estrutura de repetição for ... com a função range.
for i in range (1, 11):
    print (num, 'x', i, '=', (num * i))
print()

# EoC
