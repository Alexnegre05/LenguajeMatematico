from Logica.modelos import Logica, Proposicion, Operador, Parentesis
from Logica.validaciones import expresion

# pruebas
logica = Logica()

proposicion = Proposicion(1)      # p
operador = Operador("^")          # ^
operador2 = Operador("¬")
proposicion2 = Proposicion(0)     # 0
delimeter1 = Parentesis("(")
delimeter2 = Parentesis(")")

# EXPRESIÓN ADAPTADA: p ^ 0
expresion_p_0 = expresion([
    proposicion, 
    operador, 
    proposicion
])

# Evaluamos la expresión
value = expresion_p_0.evaluar()
print(value)  # Debería dar 0 tras pasar por tu SimplificadorArbol
