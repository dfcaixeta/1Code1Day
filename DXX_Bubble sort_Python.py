''' Projeto OneCodeOneDay
Script em python que usa a Estruturação de Dados Bubble sort
Dia XX - 03.ago.2025

@utor: @pythonclcoding '''

# Definindo a classe

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

# Entrada/Input de dados
arr = [64, 34, 25, 12, 22, 11, 90]
print('\nArranjo original:', arr)

# Saída/Output de dados
bubble_sort(arr)
print('Arranjo organizado:', arr)

print()

# EOF
# source code --> clcoding.com