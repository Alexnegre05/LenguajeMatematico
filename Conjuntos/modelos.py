class Conjunto_General(): # clase general que sirve como controlador y etsa vacia

    __slots__ = ()

    pass

class Conjunto(Conjunto_General): 

    __slots__ = ("nombre", "elementos")

    def __init__(self, nombre, elementos):

        self.nombre = nombre
        
        repite_elemento = 0 # variable para saber si un elemento esta o no repetido 

        lista_limpia = [] # lista donde se guarda los no duplicados

        for i in range(0, len(elementos)): # eliminamos elementos duplicados

            for j in range(0, len(elementos)): 

                if (elementos[i] == elementos[j] and i != j and j < i): # se repite elemento, 

                    # el j < i es para solo mirar si hay duplicado de los elementos anteriores

                    repite_elemento = 1

            if (repite_elemento == 1):

                repite_elemento = 0

            else:
                lista_limpia.append(elementos[i]) # si no se repite se añade


        # al final la lista de elementos sera la nueva lista limpia

        self.elementos = lista_limpia
            



    def __str__(self): # cada vez que alguien haga print en un conjunto

        return f"{self.nombre} = {{{self.elementos}}}" # necesitamos 3 llaves 1 para el f string otra para indicar que printee {} y otra para indicarle 
    # que seguimos en f string



class Operador(Conjunto_General):
  
   # 

  __slots__ = ("operador",)

  def __init__(self, operador):

    if(operador in ("∈", "∉", "∪", "∩", "-", "⊆", "⊈", "Δ")):  # comprueba si el operador es válido
      self.operador = operador

    else:
      raise Exception("Operator not valid")


  def __str__(self):
       
    return self.operador


    
   
class Parentesis(Conjunto_General): # clase que define los () 

  __slots__ = ("parentesis",) 

  def __init__(self, parentesis):
    
    if (parentesis == "(" or parentesis == ")"):
      self.parentesis = parentesis
    
    else:
      raise Exception("Wrong delimeters")