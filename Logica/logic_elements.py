# Documento donde ponemos las definiciones de los elementos que vamos a usar en la lógica

class Logica(): # clase general que controla todo lo relacionado con la lógica

  pass



class Proposicion(Logica): # clase que contiene una proposición, puede ser falsa(0) o verdadera(1)

  def __init__(self, valor):

    if (valor == 0 or valor == 1): # comprueba si el valor es correcto o no
        self.value = valor

    else:
        raise Exception("A proposition only accepts values of 0 or 1")




class Operador(Logica): # clase que define cada operador que necesitamos en la lógica

# el ¬ se hace con alt gr +, la flecha añadiendo - + > (de mayor que)

  def __init__(self, operador):

    if(operador == "^" or operador == "v" or operador == "¬" or operador == "-->" or operador == "<-->"):  # comprueba si el operador es válido
      self.operator = operador

    else:
      raise Exception("Operator not valid")

class Parentesis(Logica): # clase que define los () 

  def __init__(self, parentesis):
    
    if (parentesis == "(" or parentesis == ")"):
      self.delimeter = parentesis
    
    else:
      raise Exception("Wrong delimeters")
