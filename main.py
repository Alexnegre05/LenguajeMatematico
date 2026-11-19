from Logica.modelos import Logica, Proposicion, Operador, Parentesis
from Logica.validaciones import expresion

from Conjuntos.modelos import Conjunto_General, Conjunto, Operador, Parentesis

# pruebas
logica = Logica()

conjunto_general = Conjunto_General()

conjunto = Conjunto("x", [1,1,2,3])

print(conjunto)
