''' Projeto OneCodeOneDay
Esse código em Python define uma função chamada count_func que conta o número de
vezes que foi chamada. Seria um contador ...
Dia 11 - 05.mar.2025

@utor: @python.joy '''

#def count_func(data = None): # Cada chamada sem argumento começa do zero e termina em 1.
def count_func(data = {}): # Com a função null, inicia em 1 e faz os incrementos.
    if data is None:
        data = {}
    data['count'] = data.get('count', 0) + 1
    return data['count']

print(count_func())
print(count_func())
print(count_func())

# EOC