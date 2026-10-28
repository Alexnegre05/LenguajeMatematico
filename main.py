

from Logica.modelos import Logica, Proposicion, Operador, Parentesis
from Logica.validaciones import expresion



# proves
logica = Logica()

proposicion = Proposicion(1)

operador = Operador("^")
operador2 = Operador("¬")
proposicion2 = Proposicion(0)
delimeter1 = Parentesis("(")
delimeter2 = Parentesis(")")

expresion = expresion([operador2, operador2, proposicion2])



value = expresion.evaluar()
print(value)
