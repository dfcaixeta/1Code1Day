''' Projeto OneCodeOneDay
Calculando IMC com POO
Dia XX - 29.jul.2025

@utor: @pythonclcoding '''

'''Crie uma classe chamada Pessoa que possui 3 (três) atributos: 'nome', 'peso' e 'altura'.
Estes atributos devem receber valores na instanciação da classe. Esta classe deve possuir um
método chamado 'imc' que retorna o valor do IMC (Índice de Massa Corpórea) desta pessoa.
                                   IMC = Peso / (altura ** 2)
Por fim, peça que o usuário digite nome, peso e altura, crie um objeto pessoa e exiba a 
seguinte mensagem:
'O IMC de <nome> é <imc>.' '''

# Definições das classes
class Pessoa:
    def __init__(self, nome, peso, altura):
        self.nome = nome
        self.peso = peso
        self.altura = altura

    def imc(self):
        imc = self.peso / (self.altura ** 2) # Fórmula do IMC.
        return round(imc, 2) # Arredonda para duas casas decimais.

# Entrada/Input dos dados
print()    
nome = input(f'Nome: ')
peso = float(input(f'Peso (kg): '))
altura = float(input(f'Altura (mt): '))

pessoa = Pessoa(nome, peso, altura)

# Saída/Output
print(f'\nO IMC de {pessoa.nome} é {pessoa.imc()}.')
print()

# EOC