import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from binary_operation import Logica, Proposicion, Operador, Parentesis, Operacion

class Check(Logica):

 
  def check_parentesis(self):

    
    

        contador_parentesis_izquierda = 0
       
        contador_parentesis_derecha = 0
       
        for i in range (0, len(self.array)):
          
          if (isinstance(self.array[i], Parentesis) == True):  # comprobamos si el elemento es un delimitador
    
            if (self.array[i].parentesis == ")"):
              
              contador_parentesis_derecha = contador_parentesis_derecha + 1
            else:
             
              contador_parentesis_izquierda = contador_parentesis_izquierda + 1

            if (contador_parentesis_derecha > contador_parentesis_izquierda): 
            
              raise Exception("the delimiters right and left are not equal")

        # comprobamos que los delimitadores tengan el mismo número de ( que de ) al final de el for

        if contador_parentesis_izquierda != contador_parentesis_derecha: 

          raise Exception("the delimiters right and left are not equal")
    








  # aquí tenemos una función que elimina solo los delimitadores primeros y últimos si empezamos con un delimitador y terminamos con otro diferente
  # ejemplo de (p^q) a solo p^q, también tenemos que tener cuidado con casos como (p^q)^(pvq) porque aquí no podemos eliminar los delimitadores
  def eliminar_parentesis_exteriores(self):


    # aquí comprobamos si tenemos un último ) y un primer (, si no, devolvemos 0
    if (len(self.array) < 2 or isinstance(self.array[0], Parentesis) == False or self.array[0].parentesis != "(" or isinstance(self.array[-1], Parentesis) == False or self.array[-1].delimiter != ")"):
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

          if (isinstance(self.array[i], Parentesis) == True and self.array[i].parentesis == ")"):
           
            numero_de_parentesis = numero_de_parentesis + 1
         
          elif (isinstance(self.array[i], Parentesis) == True and self.array[i].parentesis == "("):
            
            numero_de_parentesis = numero_de_parentesis -1  # restamos en este caso


          # aquí comprobamos que todo esté bien
          # la misma comprobación pero para (, ya que sabemos por el elif que el último elemento es un ( solo tenemos que comprobar el anterior para el ((
          # el i >0 es para i -1

          if (numero_de_parentesis == 0 and i > 0):
            
            if(isinstance(self.array[i - 1], Parentesis) == True and i != valor_iteracion and self.array[i-1].parentesis == "("): 
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
        self.array.pop(0) # restamos el primer y el último elemento
        self.array.pop(-1)

    

    value2 = 1
    while(value2 == 1):
      
      value2 = self.eliminar_parentesis_redundantes()

    length = len(self.array)
    i = 0 # (número que guarda la posición del array)

    # bucle que recorre cada posición del array
    while (i < length):

      # aquí comprobamos que el usuario haya puesto un operador, una proposición o un delimitador
      if (isinstance(self.array[i], Proposicion) == False and isinstance(self.array[i], Operador) == False and isinstance(self.array[i], Parentesis) == False):
        
        raise Exception("the expression contains elements that are not or a proposition or an operator or a delimeter")



      # casos especiales: el primer y el último elemento del array
      if (i == 0):
        
        # aquí comprobamos si el elemento es una proposición verificando lo opuesto
        if (isinstance(self.array[i], Proposicion) == False and isinstance(self.array[i], Parentesis) == False):
          
          # aquí sabemos que esto es una operación, así que ahora comprobamos si el valor no es ¬

          if (self.array[i].operador != "¬"):

            return 0 # entonces sabemos que el primer elemento es ^... por lo que la expresión es incorrecta


      elif(i == (length - 1)): # el último solo puede ser una proposición y el anterior a este solo puede ser una operación
       
        
        # CASO A: Si el último elemento es una Proposición, validamos el anterior (Tu lógica original)

        if (isinstance(self.array[i], Proposicion) == True):
          if (isinstance(self.array[i-1], Operador) == False):
            return 0

        # CASO B: Si el último elemento es un Delimitador, nos aseguramos de que sea ")" y no "("

        if (isinstance(self.array[i], Parentesis) == True):
          
          if (self.array[i].parentesis == "("):
            return 0

        # CASO C: Si no es ni una Proposición ni un Delimitador (por ejemplo, termina en ^), es incorrecto

        if (isinstance(self.array[i], Proposicion) == False and isinstance(self.array[i], Parentesis) == False):
          return 0

          

        
        # caso especial p ¬ q si y solo si i >= 2 porque si no i - 2 podría estar fuera de rango
        if (i >= 2 and isinstance(self.array[i], Proposicion) == True and isinstance(self.array[i-1], Operador) == True and self.array[i-1].operador == "¬" and isinstance(self.array[i-2], Proposicion) == True):
          return 0

      else: # el caso general
        
        # primero comprobamos que si tenemos una proposición, la anterior no sea una proposición
        if (isinstance(self.array[i], Proposicion) == True and isinstance(self.array[i-1], Proposicion) == True):

          return 0

        # hacemos lo mismo pero para los operadores, pero sin el ¬ no es la expresión que estamos viendo, ejemplo: esto es posible ^¬ porque luego va una p, pero esto no ¬^

        if (isinstance(self.array[i], Operador) == True and isinstance(self.array[i-1], Operador) == True and self.array[i].operador != "¬"):

          return 0

        # aquí comprobamos que no tengamos el caso de ¬ ¬
        if (isinstance(self.array[i], Operador) == True and isinstance(self.array[i-1], Operador) == True and self.array[i].operador == "¬" and self.array[i-1].operador == "¬"):

          return 0

        # aquí comprobamos que no tengamos el caso de p ¬ q y verificamos que i > 2
        if (i >= 2 and isinstance(self.array[i], Proposicion) == True and isinstance(self.array[i-1], Operador) == True and self.array[i-1].operador == "¬" and isinstance(self.array[i-2], Proposicion) == True):
          return 0


        # casos de delimitadores 

         # CASO 1: Evitar un operador binario justo después de un paréntesis de apertura ej: ( ^ p)
        if (isinstance(self.array[i-1], Parentesis) == True and self.array[i-1].parentesis == "(" and isinstance(self.array[i], Operador) == True and self.array[i].operador != "¬"):
          
          return 0

        # CASO 2: Evitar un paréntesis de cierre justo después de un operador ej: (p ^ )
        if (isinstance(self.array[i-1], Operador) == True and isinstance(self.array[i], Parentesis) == True and self.array[i].parentesis == ")"):
          
          return 0

        # CASO 3: Evitar un paréntesis de apertura justo después de una proposición sin un operador ej: p ( q )
        if (isinstance(self.array[i-1], Proposicion) == True and isinstance(self.array[i], Parentesis) == True and self.array[i].parentesis == "("):
          
          return 0

        # CASO 4: Evitar una proposición justo después de un paréntesis de cierre sin un operador ej: ( p ) q
        if (isinstance(self.array[i-1], Parentesis) == True and self.array[i-1].parentesis == ")" and isinstance(self.array[i], Proposicion) == True):
          
          return 0




      # al final siempre sumamos
      i = i + 1

    # FIN DEL BUCLE
    # al final del bucle, si hemos llegado hasta aquí significa que todo está bien, por lo que enviamos un 1

    return 1

