# Documento donde ponemos las definiciones de los elementos que vamos a usar en la lógica

class Logic(): # clase general que controla todo lo relacionado con la lógica

  pass



class Proposition(Logic): # clase que contiene una proposición, puede ser falsa(0) o verdadera(1)

  def __init__(self, value):

    if (value == 0 or value == 1): # comprueba si el valor es correcto o no
        self.value = value

    else:
        raise Exception("A proposition only accepts values of 0 or 1")




class Operator(Logic): # clase que define cada operador que necesitamos en la lógica

# el ¬ se hace con alt gr +, la flecha añadiendo - + > (de mayor que)

  def __init__(self, operator):

    if(operator == "^" or operator == "v" or operator == "¬" or operator == "-->" or operator == "<-->"):  # comprueba si el operador es válido
      self.operator = operator

    else:
      raise Exception("Operator not valid")

class Delimeter(Logic): # clase que define los () 

  def __init__(self, delimeter):
    
    if (delimeter == "(" or delimeter == ")"):
      self.delimeter = delimeter
    
    else:
      raise Exception("Wrong delimeters")
