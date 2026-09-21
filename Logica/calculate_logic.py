from evaluate_expressions import Logic, Proposition, Operator, Operation, expression, Delimeter

# proves
logica = Logic()

proposicion = Proposition(1)

operador = Operator("^")
operador2 = Operator("¬")
proposicion2 = Proposition(0)
delimeter1 = Delimeter("(")
delimeter2 = Delimeter(")")

expression = expression([ proposicion, operador, delimeter1, delimeter1, proposicion, operador, proposicion2, delimeter2,delimeter2,operador,proposicion])
print(len(expression.array))
value = expression.check()
print(len(expression.array))
print(value)

