from Logica.modelos import Logica, Proposicion, Operador, Parentesis
from Logica.validaciones import expresion

# pruebas
logica = Logica()

proposicion = Proposicion(1)
operador = Operador("^")
operador2 = Operador("¬")
operador3 = Operador("v")
proposicion2 = Proposicion(0)
delimeter1 = Parentesis("(")
delimeter2 = Parentesis(")")

# EXPRESIÓN: (1 ^ ¬1) v (1 ^ 0)
expresion1 = expresion([
    delimeter1,
    proposicion,
    operador,
    operador2,
    proposicion,
    delimeter2,
    operador3,
    delimeter1,
    proposicion,
    operador,
    proposicion2,
    delimeter2
])

# Evaluamos la expresión
value = expresion1.evaluar()
print(value)  # Debería dar 0