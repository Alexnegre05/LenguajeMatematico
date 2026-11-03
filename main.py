from Logica.modelos import Logica, Proposicion, Operador, Parentesis
from Logica.validaciones import expresion

# pruebas
logica = Logica()

proposicion = Proposicion(1)
operador = Operador("^")
operador2 = Operador("¬")
operador3 = Operador("v")
operador4 = Operador("-->")
operador5 = Operador("<-->")
proposicion2 = Proposicion(0)

# EXPRESIÓN SIN PARÉNTESIS:
# 1 ^ ¬1 v 1 ^ 0 v 0 --> 1 ^ 1 v 0 ^ 1 v 0 --> 0 ^ 1 v 0

expresion1 = expresion([
    proposicion,
    operador,
    operador2,
    
])

# Evaluamos la expresión
value = expresion1.evaluar()
print(value)