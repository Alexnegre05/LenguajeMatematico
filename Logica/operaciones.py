from Logica.modelos import Logica, Proposicion, Operador, Parentesis




class Operacion(Logica): # clase que toma dos proposiciones y una operación y devuelve un valor de 0 o 1

  __slots__ = ("proposicion1", "operador", "proposicion2")
  
  def __init__(self, Proposicion1, operador, Proposicion2):

    # mensaje personal de error
    if (isinstance(Proposicion1, Proposicion) == False):
      
      raise Exception("la primera proposicion no es valida")

    if (isinstance(operador, Operador) == False):
      
      raise Exception("el operador introducido no es valido")

    if (operador.operador == "¬"): # caso exclusivo para la negación

      self.proposicion1 = Proposicion1

      self.operador = operador

      self.proposicion2 = None # ponemos la proposición 2 como None para saber que está vacía

    else:

      if (isinstance(Proposicion2, Proposicion) == False):

        raise Exception("la segunda proposicion no es valida")

      self.proposicion1 = Proposicion1

      self.operador = operador

      self.proposicion2 = Proposicion2









  def Resultado(self):

      Proposicion1 = self.proposicion1.value

      Operador = self.operador.operador

      # Cambiado a "is None" para solucionar AttributeError

      if (Operador == "¬" and self.proposicion2 is None):

        return 1 - Proposicion1 

      Proposicion2 = self.proposicion2.value

      #Optimizacion usar las funciones nativas de C es mas rapido que usar las tablas de verdad
      if Operador == "^": 
          return Proposicion1 & Proposicion2

      elif Operador == "v": 
          return Proposicion1 | Proposicion2

      elif Operador == "-->": 
          return (1 - Proposicion1) | Proposicion2  # Equivalente a: ¬p1 v p2 que equivale a p -->q
           # si el valor es 1 1-1 = 0, si es 0 1-0 = 1, se te niega el resultado

      elif Operador == "<-->": 
          return 1 if Proposicion1 == Proposicion2 else 0
