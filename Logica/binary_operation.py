from logic_elements import Logica, Proposicion, Parentesis, Operador




class Operation(Logica): # clase que toma dos proposiciones y una operación y devuelve un valor de 0 o 1


  def __init__(self, Proposition1, operator, Proposition2):

    if (isinstance(Proposition1,Proposicion) == True and isinstance(operator, Operador) == True and isinstance(Proposition2,Proposicion) == True): # usamos isinstance para saber si pertenece a una clase concreta

        self.Proposition1 = Proposition1
        self.operator = operator
        self.Proposition2 = Proposition2

    else:

      if (isinstance(Proposition1,Proposicion) == True and isinstance(operator, Operador) == True and operator.operator == "¬"): # caso exclusivo para la negación

        self.Proposition1 = Proposition1
        self.operator = operator
        self.Proposition2 = None # ponemos la proposición 2 como None para saber que está vacía




      # mensaje personal de error
      if (isinstance(Proposition1,Proposicion) == False):
        
        raise Exception("The first proposition introduced is not a valid proposition")

      elif (isinstance(operator, Operador) == False):
        
        raise Exception("the operator introduced is not a valid operator")

      elif (isinstance(Proposition2,Proposicion) == False):

        if(isinstance(Proposition1,Proposicion) == True and isinstance(operator, Operador) == True and operator.operator == "¬"):
          pass

        else:
          raise Exception("The second proposition introduced is not a valid proposition")

      else:
        raise Exception("Ha sucedido un error")









  def Result(self):

      Proposition1 = self.Proposition1.value
      Operator = self.operator.operator

      # Cambiado a "is None" para solucionar AttributeError
      if (Operator == "¬" and self.Proposition2 is None):
        Proposition2 = None

      else:
        Proposition2 = self.Proposition2.value

      if (Operator == "^"): # comprobamos uno por uno qué operador estamos usando

        # vamos caso por caso
        if (Proposition1 == 0 and Proposition2 == 0):
          return 0

        elif (Proposition1 == 1 and Proposition2 == 0):
          return 0

        elif (Proposition1 == 0 and Proposition2 == 1):
          return 0

        elif (Proposition1 == 1 and Proposition2 == 1):
          return 1

      # hacemos lo mismo para los otros operadores
      elif (Operator == "v"):


        if (Proposition1 == 0 and Proposition2 == 0):
          return 0

        elif (Proposition1 == 1 and Proposition2 == 0):
          return 1

        elif (Proposition1 == 0 and Proposition2 == 1):
          return 1

        elif (Proposition1 == 1 and Proposition2 == 1):
          return 1

      elif (Operator == "-->"):


        if (Proposition1 == 0 and Proposition2 == 0):
          return 1

        elif (Proposition1 == 1 and Proposition2 == 0):
          return 0

        elif (Proposition1 == 0 and Proposition2 == 1):
          return 1

        elif (Proposition1 == 1 and Proposition2 == 1):
          return 1


      elif (Operator == "<-->"):


        if (Proposition1 == 0 and Proposition2 == 0):
          return 1

        elif (Proposition1 == 1 and Proposition2 == 0):
          return 0

        elif (Proposition1 == 0 and Proposition2 == 1):
          return 0

        elif (Proposition1 == 1 and Proposition2 == 1):
          return 1

      elif (Operator == "¬"): # caso especial, la negación

        if (Proposition1 == 0):
          return 1
        else:
          return 0
