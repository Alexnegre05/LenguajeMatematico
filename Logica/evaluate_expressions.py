import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from binary_operation import Logic, Proposition, Operator, Delimeter, Operation
from my_ast import AST #we import the AST

from check_expressions import Check

class expression(Check): # class that we use to define when we are working with multiple propositions and operations

  def __init__(self, array):


    if (array is not None and len(array) > 1 and isinstance(array[len(array) -1], Operator) == False): 
      # we want the array to have more than one argument and that the last one is not an operator
      self.array = array
    else:
      if (array is None or len(array) == 1):
        raise Exception("there are not sufiecient elements in the expression")
      else:
        raise Exception("You can not end with a operator")





  def binary_operation(self, operation): # recives the string and the operation you want to solve and gives and answer

      copy_array = []
      i = 0
      while (i < len(self.array)):

        if ((isinstance(self.array[i], Operator) == True) and self.array[i].operator == operation):
            result = Operation(self.array[i-1], self.array[i], self.array[i + 1])

            value = result.Result()
            p = Proposition(value)

            copy_array.pop() # we substract the last proposition since now its part of the operation that we want to solve, we use pop for that
            copy_array.append(p)

            i = i + 2

        else:
          copy_array.append(self.array[i])
          i = i + 1

      self.array = copy_array

      return self.array


  # function that evaluates a node of teh AST and calculates a value
  def evaluate_node(self,node):

    if (node == None): # if its null we reurn null
      return None

    # this if is the case of having the end of a branch of the tree

    if (node.right_node == None and node.left_node == None):

      return node.central_node

    # if it is an operator we evaluate left and right on the function

    right = self.evaluate_node(node.right_node)
    left = self.evaluate_node(node.left_node)

    # now we know that we have an operator we calculate the operation, we have to separate the case of ¬ from the other ones
    if (node.central_node.operator == "¬"):

      operation = Operation(right, node.central_node, None)
    else:
      operation = Operation(left, node.central_node, right)

    result = operation.Result()

    # we have to put the result into a new proposition
    p = Proposition(result)

    return p # we return the p



  def simplify_double_negation(self, actual_node):


    node_null = False # if we find that a node is null we stop searching 

    while (node_null == False):
    
          if (actual_node.central_node == None): # we exit the while
    
            node_null = True
    
          else:
    
            if ((isinstance(actual_node.central_node, Operator) == True) and actual_node.central_node.operator == "¬"): # if the node is an operation and its ¬
              
              # we check if its have sons, its and  and if the operator is ¬
              node = actual_node.right_node # we put this into node so tahat we don't have to worry aboiut to much node.node. ...
    
              if ((isinstance(node.central_node, Operator) == True) and node.central_node != None and node.central_node.operator == "¬"):
    
                node = actual_node.right_node.right_node

                if (node.central_node != None and isinstance(node.central_node, Proposition) == True):
                  pass 
                # if its have another node and is a p
                  # here we make the change
                
                else:
                  node_null = True
              else:
                node_null = True
            else:
              node_null = True

    return actual_node # we return the tree


    

  def simplify_tree(self, tree): # funcion que se encarga de simplificar el arbol
  # we are only going to program those functions that simplify the tree

    # first simplification ¬ ¬ p == p

    if (tree.right_node != None): # if the ones bellow thsi node are not null we call this function again(the simplify tree)
   
        tree.right_node = self.simplify_tree(tree.right_node)
   
    if (tree.left_node != None):
        
        tree.left_node = self.simplify_tree(tree.left_node)

    tree = self.simplify_double_negation(tree) # here we recibe the first node 

    
  
  
    return tree # at the end we return the tree # once we are done with the recursive
 




  def evaluate(self): # function that evaluates the expresion after we have checked that the sintaxis is correct

    value = self.check()

    if (value == 0):
      raise Exception("Se ha introducido una expresion erronea")
    else:

      ast = AST(None)
      tree = ast.create_ast(self.array, "operator", "delimeter")

      # we will begin evaluating only the ¬ because have more precendent than the other expresions

      tree = self.simplify_tree(tree)

      result = self.evaluate_node(tree)

      return result.value # we return the result
      