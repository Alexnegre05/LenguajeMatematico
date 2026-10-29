

from Logica.operaciones import  Proposicion, Operador, Operacion
from mi_ast import AST # importamos el AST
from Logica.modelos import Logica

from Logica.simplificaciones import SimplificadorArbol



from Logica.operaciones import Proposicion, Operador, Parentesis, Operacion

class Check(Logica):

 
  def check_parentesis(self):

        balance_parentesis = 0
       
        for i in range (0, len(self.array)):
          
          if (isinstance(self.array[i], Parentesis) == True):  # comprobamos si el elemento es un delimitador
    
            if (self.array[i].parentesis == "("):
              
              balance_parentesis = balance_parentesis + 1
            else:
             
              balance_parentesis = balance_parentesis - 1

            if (balance_parentesis < 0): 
            
              raise Exception("los parentesis izquierda y derecha no son iguales")

        # comprobamos que los delimitadores tengan el mismo número de ( que de ) al final de el for

        if (balance_parentesis != 0): 

          raise Exception("los parentesis izquierda y derecha no son iguales")

    








  # aquí tenemos una función que elimina solo los delimitadores primeros y últimos si empezamos con un delimitador y terminamos con otro diferente
  # ejemplo de (p^q) a solo p^q, también tenemos que tener cuidado con casos como (p^q)^(pvq) porque aquí no podemos eliminar los delimitadores
  def eliminar_parentesis_exteriores(self):

    primero = self.array[0]
    ultimo = self.array[-1] # con esto el codigo es mas rapido, aqui no ponemos los isinstance en variables ya que solo aparecen una vez

    # aquí comprobamos si tenemos un último ) y un primer (, si no, devolvemos 0
    if (len(self.array) < 2 or isinstance(primero, Parentesis) == False or primero.parentesis != "(" or isinstance(ultimo, Parentesis) == False or ultimo.parentesis != ")"):
      return 0
    
    contador_parentesis = 1

    # dado que la primera y la ultima linea de el array ya sabemos que hay ( y hay ) 
    # el for puede empezar una posicion despues y finalizar una posicion antes
    # por eso si o si count delimeters ya empieza en 1

    for i in range(1, len(self.array) -1):

      if (isinstance(self.array[i],Parentesis) == True):

        if (self.array[i].parentesis == "("): # sumamos uno cuando encontramos ( y restamos uno para )
          contador_parentesis = contador_parentesis + 1

        else:
          contador_parentesis = contador_parentesis - 1

      # Si el contador llega a 0 ANTES del final, significa que los paréntesis no son exteriores
      # Ejemplo: (p ^ q) ^ (r v s) -> Rompe aquí en el primer ')' because no envuelve todo
       
      if contador_parentesis == 0:

        return 0

    if contador_parentesis == 1: # si ha encontrado parentesis
      return 1


    return 0 # devolvemos 0 si los delimitadores no están en los extremos





  def eliminar_parentesis_redundantes(self): # devolveremos 1 solo si hemos encontrado un delimitador doble
    # vamos hacia atrás
    
    if len(self.array) < 4: # si es menor a 4 no puede pasar que tengamos [(,(,),)]
        return 0
    
    valor_iteracion = -1
    

    for i in range(len(self.array)- 2,-1,-1): # vamos hasta -1 para el caso del 0
          

      # hemos encontrado un delimitador doble que es )) 
      if(isinstance(self.array[i], Parentesis) == True and self.array[i].parentesis == ")"):
        
        if(isinstance(self.array[i + 1], Parentesis) == True and self.array[i+1].parentesis == ")"):

          valor_iteracion = i
          break


    # otro for pero comprobamos si hemos encontrado otros delimitadores,
    # el if inicial es para evitar tener que hacer el for en caso de que no hayamos encontrado ))

    if (valor_iteracion != -1):

      numero_de_parentesis = 0 # usamos esto para comprobar si el número es correcto y saber si tenemos o no que eliminar los delimitadores
      # casos como ((p^q)) v (( r v s)) 
      
      for i in range(valor_iteracion,-1,-1):

          elemento_actual = self.array[i]

          es_parentesis = isinstance(elemento_actual, Parentesis)

          if (es_parentesis == True and elemento_actual.parentesis == ")"):
           
            numero_de_parentesis = numero_de_parentesis + 1
         
          elif (es_parentesis == True and elemento_actual.parentesis == "("):
            
            numero_de_parentesis = numero_de_parentesis -1  # restamos en este caso


          # aquí comprobamos que todo esté bien
          # la misma comprobación pero para (, ya que sabemos por el elif que el último elemento es un ( solo tenemos que comprobar el anterior para el ((
          # el i >0 es para i -1

          if (numero_de_parentesis == 0 and i > 0):

            elemento_anterior = self.array[i - 1]

            if(isinstance(elemento_anterior, Parentesis) == True and i != valor_iteracion and elemento_anterior.parentesis == "("): 
              # estamos comprobando que la i va hacia atrás, por lo que en lugar de i+1 es i - 1
              
               # eliminamos las posiciones donde había un () extra
              del self.array[valor_iteracion + 1]

              del self.array[i - 1]

              return 1

    return 0








  def check(self): # función que comprueba si el array es correcto; devolverá 0 si no lo es y 1 si está todo correcto

    self.check_parentesis() # comprobamos que todo lo relacionado con los delimitadores esté bien

    value = 1

    
    while (value == 1): # este código es para eliminar los delimitadores exteriores ( expresión )
    
    # el bucle es para el caso de más de un delimitador como (( expresión ))

      value = self.eliminar_parentesis_exteriores() # eliminamos si podemos los delimitadores exteriores, si recibimos un 1

      if (value == 1):

        self.array.pop(-1) # restamos el primer y el último elemento
        self.array.pop(0)

    

    value2 = 1

    while(value2 == 1):
      
      value2 = self.eliminar_parentesis_redundantes()

    length = len(self.array)

    if (length == 0): # Una expresión vacía tras limpiarla no es válida
      
      return 0

    i = 0 # (número que guarda la posición del array)

    # bucle que recorre cada posición del array

    while (i < length):

      valor_actual = self.array[i]

      isinstance_actual_proposicion = isinstance(valor_actual, Proposicion)
      
      isinstance_actual_operacion = isinstance(valor_actual, Operador)
      
      isinstance_actual_parentesis = isinstance(valor_actual, Parentesis)


      # aquí comprobamos que el usuario haya puesto un operador, una proposición o un delimitador
      if (isinstance_actual_proposicion == False and isinstance_actual_operacion == False and isinstance_actual_parentesis == False):
        
        raise Exception("La expresion contiene elementos que no son ni parentesis ni proposiciones ni operadores")


      # --- EXTRACTOR DE CONTEXTO (Variables del elemento anterior) ---
      # Creamos variables del elemento anterior solo si i > 0 para evitar búsquedas repetidas e innecesarias
      if (i > 0):

        valor_anterior = self.array[i - 1]
        
        ant_proposicion = isinstance(valor_anterior, Proposicion)
        
        ant_operacion = isinstance(valor_anterior, Operador)
        
        ant_parentesis = isinstance(valor_anterior, Parentesis)
      
      else:
        ant_proposicion = ant_operacion = ant_parentesis = False


      

      # 1. Validación de PROPOSICIONES
      if (isinstance_actual_proposicion == True):
        
        # Evita proposición seguida de proposición (ej: p q) o proposición tras paréntesis de cierre (ej: ) q)
        
        if (ant_proposicion == True or (ant_parentesis == True and valor_anterior.parentesis == ")")):
          return 0

      # 2. Validación de OPERADORES
      
      elif (isinstance_actual_operacion == True):
        
        # Si es un negador "¬"
        
        if (valor_actual.operador == "¬"):
          
          # Evita proposición seguida de negador directamente (ej: p ¬ q)
          
          if (ant_proposicion == True):
            return 0
        
        # Si es un operador binario (^, v, →...)
        
        else:
          # No puede ser el primer elemento (ej: ^ p) ni estar tras un operador binario (ej: p ^ v q) ni tras un "(" (ej: ( ^ p)
          if (i == 0 or (ant_operacion == True and valor_anterior.operador != "¬") or (ant_parentesis == True and valor_anterior.parentesis == "(")):
            
            return 0
          
          # No puede ser el último elemento (ej: p ^)
          if (i == length - 1):
            return 0

      # 3. Validación de PARÉNTESIS
      
      elif (isinstance_actual_parentesis == True):
        
        # Si es paréntesis de apertura "("
        
        if (valor_actual.parentesis == "("):
          
          # Evita "(" tras una proposición (ej: p ( ) o tras un ")" (ej: ) ( )
          
          if (ant_proposicion == True or (ant_parentesis == True and valor_anterior.parentesis == ")")):
            
            return 0
          
          # Evita que sea el último elemento (ej: p ^ ()
          
          if (i == length - 1):
            return 0
            
        # Si es paréntesis de cierre ")"
        else:
          
          # Evita que sea el primer elemento (ej: ) p) o que vaya tras un "(" vacío (ej: ()) o tras un operador binario (ej: p ^ ))
          
          if (i == 0 or (ant_parentesis == True and valor_anterior.parentesis == "(") or ant_operacion == True):
            return 0


      # al final siempre sumamos
      i = i + 1

    # FIN DEL BUCLE
    # al final del bucle, si hemos llegado hasta aquí significa que todo está bien, por lo que enviamos un 1

    return 1







class expresion(Check): # clase que usamos para definir cuándo estamos trabajando con múltiples proposiciones y operaciones

  def __init__(self, array):


    if (array is not None and len(array) > 1 and isinstance(array[-1], Operador) == False): 
      # queremos que el array tenga más de un argumento y que el último no sea un operador
      self.array = array

    else:
      
      if (array is None or len(array) == 1):
        raise Exception("there are not sufiecient elements in the expression")
      
      else:
        raise Exception("You can not end with a operator")





  # función que evalúa un nodo del AST y calcula un valor
  
  def evaluar_nodo(self,node):

    if (node == None): # si es nulo devolvemos nulo
      return None

    # este if es para el caso en el que tenemos el final de una rama del árbol

    if (node.nodo_derecha == None and node.nodo_izquierda == None):

      return node.nodo_central

    # si es un operador evaluamos la izquierda y la derecha en la función

    right = self.evaluar_nodo(node.nodo_derecha)
    
    left = self.evaluar_nodo(node.nodo_izquierda)

    # ahora que sabemos que tenemos un operador calculamos la operación, tenemos que separar el caso de ¬ de los demás
    if (node.nodo_central.operador == "¬"):

      operation = Operacion(right, node.nodo_central, None)
      
      # Si hay un operador atrapado en la rama izquierda debido al slicing, lo ejecutamos sobre el resultado
      if (left != None and hasattr(left, 'operador') == True and left.operador == "¬"):
        
        result_intermedio = operation.Resultado()
        
        p_intermedia = Proposicion(result_intermedio)
        
        operation = Operacion(p_intermedia, left, None)
    else:

      operation = Operacion(left, node.nodo_central, right)

    result = operation.Resultado()

    # tenemos que poner el resultado dentro de una nueva proposición
    p = Proposicion(result)

    return p # devolvemos la p










  def evaluar(self): # función que evalúa la expresión después de haber comprobado que la sintaxis es correcta

    value = self.check()

    if (value == 0):
      raise Exception("Se ha introducido una expresion erronea")
    
    else:

      ast = AST(None)
      tree = ast.crear_ast(self.array, "operador", "parentesis")

      # comenzaremos evaluando solo la ¬ porque tiene más precedencia que las otras expresiones

      simplificator = SimplificadorArbol()
      
      tree = simplificator.simplificar_general(tree)

      result = self.evaluar_nodo(tree)

      return result.value # devolvemos el resultado
