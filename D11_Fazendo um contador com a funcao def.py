''' Projeto OneCodeOneDay
Esse código em Python define uma função chamada count_func que conta o número de
vezes que foi chamada. Seria um contador ...
Dia 11 - 05.mar.2025

@utor: @python.joy '''

def count_func(data=None):
#def count_func(data={}):
    if data is None:
        data = {}
    data['count'] = data.get('count', 0) + 1
    return data['count']

print(count_func())
print(count_func())
print(count_func())

# EOC