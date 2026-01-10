''' Projeto OneCodeOneDay
Esse código em Python tem como finalidade gerar e exibir a tabuada de multiplicação 
de um número informado pelo usuário utilizando a estrutura de repetição while.

Fazendo uma tabuada usando o método while ... loop ...
Dia 04 - 10.jan.2026

@utor: @https://github.com/dfcaixeta '''

# Método 1. Tabuada usando o Estrutura de repetição (loop) while ...

# Entrada/Input de dado
num = int(input('Entre com um número: '))
i = 1 # Inicializa o contador.

# Estrutura de repetição com while.
while i <= 10:
    print(num, 'x', i, '=', (num * i))
    i += 1

print()

# EOC