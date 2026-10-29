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

# EXPRESIÓN ADAPTADA: p ^ 0
expresion1= expresion([
    delimeter1,
    operador2,
    proposicion, 
    operador,
    proposicion,
    delimeter2
])

# Evaluamos la expresión
value = expresion1.evaluar()
print(value)  # Debería dar 0 tras pasar por tu SimplificadorArbol
