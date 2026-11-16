# Documento donde ponemos las definiciones de los elementos que vamos a usar en la lógica

class Logica(): # clase general que controla todo lo relacionado con la lógica
  __slots__ = () # hay que poner esto vacio sino se hereda en las otras clases el diccionario

  pass



class Proposicion(Logica): # clase que contiene una proposición, puede ser falsa(0) o verdadera(1)

  __slots__ = ("value",) # las clases tienen un diccionario dentro que consume mucha memoria 
  # ya que con .algo puedes crear nuevos atributos para las clases
  # si sabes que solo va a tener estos atributos y no quieres un diccionario que puede consumir mucha memoria usar slots

  def __init__(self, valor):

    if (valor == 0 or valor == 1): # comprueba si el valor es correcto o no
        self.value = valor

    else:
        raise Exception("A proposition only accepts values of 0 or 1")




class Operador(Logica): # clase que define cada operador que necesitamos en la lógica

# el ¬ se hace con alt gr +, la flecha añadiendo - + > (de mayor que)

  __slots__ = ("operador",)

  def __init__(self, operador):

    if(operador in ("^", "v", "¬", "-->", "<-->")):  # comprueba si el operador es válido
      self.operador = operador

    else:
      raise Exception("Operator not valid")

class Parentesis(Logica): # clase que define los () 

  __slots__ = ("parentesis",) 

  def __init__(self, parentesis):
    
    if (parentesis == "(" or parentesis == ")"):
      self.parentesis = parentesis
    
    else:
      raise Exception("Wrong delimeters")
