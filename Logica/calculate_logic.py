import sys
import os # we use this libraries only for problems with importations and ubications of folders and files

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from evaluate_expressions import Logic, Proposition, Operator, Operation, expression, Delimeter



# proves
logica = Logic()

proposicion = Proposition(1)

operador = Operator("^")
operador2 = Operator("¬")
proposicion2 = Proposition(0)
delimeter1 = Delimeter("(")
delimeter2 = Delimeter(")")

expression = expression([ proposicion, operador, proposicion, operador, proposicion2,operador,proposicion])



value = expression.evaluate()
print(value)
