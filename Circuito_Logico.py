import schemdraw
import schemdraw.logic as logic

# Criando o desenho
with schemdraw.Drawing() as d:
    d.config(unit=2.5) # Define o tamanho dos elementos

    # Porta AND
    and_gate = d.add(logic.And().label('AND', loc='bottom'))

    # Porta OR, posicionada à direita da AND
    or_gate = d.add(logic.Or().right().at(and_gate.out).label('OR', loc='bottom'))

    # Entradas da porta AND
    d.add(logic.Line().left().at(and_gate.in1).length(2).label('A', 'left'))
    d.add(logic.Line().left().at(and_gate.in2).length(2).label('B', 'left'))

    # Entrada adicional para a porta OR
    d.add(logic.Line().left().at(or_gate.in2).length(2).label('C', 'left'))

    # Saída final do circuito
    d.add(logic.Line().right().at(or_gate.out).length(2).label('Saída', 'right'))

# Exibe o desenho

d.draw()