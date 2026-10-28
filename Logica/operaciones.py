from Logica.modelos import Logica, Proposicion, Parentesis, Operador




class Operacion(Logica): # clase que toma dos proposiciones y una operación y devuelve un valor de 0 o 1

  
  def __init__(self, Proposicion1, operador, Proposicion2):

    instance_proposicion1 = isinstance(Proposicion1,Proposicion)
    instance_proposicion2 = isinstance(Proposicion2,Proposicion) # hacemos esto para no calcular tantas veces el isinstance
    instance_operador =  isinstance(operador, Operador) == True

    if (instance_proposicion1 == True and instance_operador == True and instance_proposicion2 == True): # usamos isinstance para saber si pertenece a una clase concreta

        self.proposicion1 = Proposicion1
        self.operador = operador
        self.proposicion2 = Proposicion2

    else:

      if (instance_proposicion1 == True and instance_operador == True and operador.operador == "¬"): # caso exclusivo para la negación

        self.proposicion1 = Proposicion1
        self.operador = operador
        self.proposicion2 = None # ponemos la proposición 2 como None para saber que está vacía




      # mensaje personal de error
      if (instance_proposicion1 == False):
        
        raise Exception("la primera proposicion no es valida")

      elif (instance_operador == False):
        
        raise Exception("el operador introducido no es valido")

      elif (instance_proposicion2 == False):

        if(instance_proposicion1 == True and instance_operador == True and operador.operador == "¬"):
          pass

        else:
          raise Exception("la segunda proposicion no es valida")

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
