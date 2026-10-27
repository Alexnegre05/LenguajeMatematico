from Logica.modelos import Logica, Proposicion, Parentesis, Operador




class Operacion(Logica): # clase que toma dos proposiciones y una operación y devuelve un valor de 0 o 1


  def __init__(self, Proposicion1, operador, Proposicion2):

    if (isinstance(Proposicion1,Proposicion) == True and isinstance(operador, Operador) == True and isinstance(Proposicion2,Proposicion) == True): # usamos isinstance para saber si pertenece a una clase concreta

        self.proposicion1 = Proposicion1
        self.operador = operador
        self.proposicion2 = Proposicion2

    else:

      if (isinstance(Proposicion1,Proposicion) == True and isinstance(operador, Operador) == True and operador.operador == "¬"): # caso exclusivo para la negación

        self.proposicion1 = Proposicion1
        self.operador = operador
        self.proposicion2 = None # ponemos la proposición 2 como None para saber que está vacía




      # mensaje personal de error
      if (isinstance(Proposicion1,Proposicion) == False):
        
        raise Exception("The first proposition introduced is not a valid proposition")

      elif (isinstance(operador, Operador) == False):
        
        raise Exception("the operator introduced is not a valid operator")

      elif (isinstance(Proposicion2,Proposicion) == False):

        if(isinstance(Proposicion1,Proposicion) == True and isinstance(operador, Operador) == True and operador.operador == "¬"):
          pass

        else:
          raise Exception("The second proposition introduced is not a valid proposition")

      else:
        raise Exception("Ha sucedido un error")









  def Resultado(self):

      Porposicion1 = self.proposicion1.value
      Operador = self.operador.operador

      # Cambiado a "is None" para solucionar AttributeError
      if (Operador == "¬" and self.proposicion2 is None):
        Proposicion2 = None

      else:
        Proposicion2 = self.proposicion2.value

      if (Operador == "^"): # comprobamos uno por uno qué operador estamos usando

        # vamos caso por caso
        if (Porposicion1 == 0 and Proposicion2 == 0):
          return 0

        elif (Porposicion1 == 1 and Proposicion2 == 0):
          return 0

        elif (Porposicion1 == 0 and Proposicion2 == 1):
          return 0

        elif (Porposicion1 == 1 and Proposicion2 == 1):
          return 1

      # hacemos lo mismo para los otros operadores
      elif (Operador == "v"):


        if (Porposicion1 == 0 and Proposicion2 == 0):
          return 0

        elif (Porposicion1 == 1 and Proposicion2 == 0):
          return 1

        elif (Porposicion1 == 0 and Proposicion2 == 1):
          return 1

        elif (Porposicion1 == 1 and Proposicion2 == 1):
          return 1

      elif (Operador == "-->"):


        if (Porposicion1 == 0 and Proposicion2 == 0):
          return 1

        elif (Porposicion1 == 1 and Proposicion2 == 0):
          return 0

        elif (Porposicion1 == 0 and Proposicion2 == 1):
          return 1

        elif (Porposicion1 == 1 and Proposicion2 == 1):
          return 1


      elif (Operador == "<-->"):


        if (Porposicion1 == 0 and Proposicion2 == 0):
          return 1

        elif (Porposicion1 == 1 and Proposicion2 == 0):
          return 0

        elif (Porposicion1 == 0 and Proposicion2 == 1):
          return 0

        elif (Porposicion1 == 1 and Proposicion2 == 1):
          return 1

      elif (Operador == "¬"): # caso especial, la negación

        if (Porposicion1 == 0):
          return 1
        
        else:
          return 0
