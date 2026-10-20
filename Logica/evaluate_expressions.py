import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from binary_operation import Logic, Proposition, Operator, Delimeter, Operation
from my_ast import AST # importamos el AST

from check_expressions import Check
from simplify_tree import TreeSimplification


class expression(Check): # clase que usamos para definir cuándo estamos trabajando con múltiples proposiciones y operaciones

  def __init__(self, array):


    if (array is not None and len(array) > 1 and isinstance(array[-1], Operator) == False): 
      # queremos que el array tenga más de un argumento y que el último no sea un operador
      self.array = array

    else:
      
      if (array is None or len(array) == 1):
        raise Exception("there are not sufiecient elements in the expression")
      
      else:
        raise Exception("You can not end with a operator")





  def binary_operation(self, operation): # recibe la cadena y la operación que quieres resolver y devuelve una respuesta

      copy_array = []
      i = 0

      while (i < len(self.array)):

        if ((isinstance(self.array[i], Operator) == True) and self.array[i].operator == operation):
            result = Operation(self.array[i-1], self.array[i], self.array[i + 1])

            value = result.Result()
            p = Proposition(value)

            copy_array.pop() # restamos la última proposición ya que ahora forma parte de la operación que queremos resolver, usamos pop para ello
            copy_array.append(p)

            i = i + 2

        else:
          copy_array.append(self.array[i])
          i = i + 1

      self.array = copy_array

      return self.array





  # función que evalúa un nodo del AST y calcula un valor
  def evaluate_node(self,node):

    if (node == None): # si es nulo devolvemos nulo
      return None

    # este if es para el caso en el que tenemos el final de una rama del árbol

    if (node.right_node == None and node.left_node == None):

      return node.central_node

    # si es un operador evaluamos la izquierda y la derecha en la función

    right = self.evaluate_node(node.right_node)
    
    left = self.evaluate_node(node.left_node)

    # ahora que sabemos que tenemos un operador calculamos la operación, tenemos que separar el caso de ¬ de los demás
    if (node.central_node.operator == "¬"):

      operation = Operation(right, node.central_node, None)
    else:
      operation = Operation(left, node.central_node, right)

    result = operation.Result()

    # tenemos que poner el resultado dentro de una nueva proposición
    p = Proposition(result)

    return p # devolvemos la p








  def evaluate(self): # función que evalúa la expresión después de haber comprobado que la sintaxis es correcta

    value = self.check()

    if (value == 0):
      raise Exception("Se ha introducido una expresion erronea")
    
    else:

      ast = AST(None)
      tree = ast.create_ast(self.array, "operator", "delimeter")

      # comenzaremos evaluando solo la ¬ porque tiene más precedencia que las otras expresiones

      simplificator = TreeSimplification()
      
      tree = simplificator.simplify(tree)

      result = self.evaluate_node(tree)

      return result.value # devolvemos el resultado
