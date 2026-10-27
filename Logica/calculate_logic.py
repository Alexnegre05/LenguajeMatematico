import sys
import os # usamos esta libreria por tema de problemas de importaciones entre librerias

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from evaluate_expressions import Logica, Proposicion, Operador, Operacion, expresion, Parentesis



# proves
logica = Logica()

proposicion = Proposicion(1)

operador = Operador("^")
operador2 = Operador("¬")
proposicion2 = Proposicion(0)
delimeter1 = Parentesis("(")
delimeter2 = Parentesis(")")

expresion = expresion([ proposicion, operador,delimeter1, proposicion, operador, proposicion,operador,proposicion, delimeter2])



value = expresion.evaluar()
print(value)
