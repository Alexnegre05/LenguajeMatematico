# un AST es una clase que transforms la lista de operaciones en un árbol facilitando la evaluación de los elementos
# debido a que el AST se utilizará en más de una carpeta, vamos a colocar este archivo fuera de todas las carpetas


class AST():

    # precedence es un diccionario que contiene cómo funciona la operación (la precedencia)
    precedencia = {
        "¬":5,
        "^":4,
        "v":3,
        "-->":2,
        "<-->":1,

    }

    
    def __init__(self, nodo_central, nodo_derecha = None, nodo_izquierda = None): # necesita un nodo central y dos hijos que pueden ser nulos

        self.nodo_central = nodo_central
        self.nodo_derecha = nodo_derecha
        self.nodo_izquierda = nodo_izquierda



    def crear_ast(self, lista, tipo, tipo_parentesis): # aquí queremos saber, para el array de elementos, 
        
        # si hay un elemento con la menor precedencia; ese será el primer nodo


        # caso base para la recursividad
        if (len(lista) == 0): # caso para el negativo ¬; puede ocurrir que un nodo sea None
            
            return None
       
        else:
         
            if (len(lista)== 1): # si por recursividad solo tenemos un elemento
              
                return AST(lista[0]) # devolvemos el AST solo con ese nodo, sera el primero 

            
        posicion = 0 # usamos position para saber cuál fue la posición de menor precedencia; en caso de haber más de una, elegimos la de la derecha

        nodo_central_detectado = None # ARREGLO CLAVE: Usamos una variable local en lugar de self.nodo_central para no destruir la raíz en la recursión

        posicion_lista = -1 # declaramos esta función que guarda cuál es la posición del array
        
        #  Buscamos la menor precedencia usando el concepto de supremo, inf es siempre mayor a cualquier numero, sera siempre la precedencia para comparar---
        menor_precedencia_encontrada = float('inf')

        # Llevamos el conteo del nivel de delimitadores en una sola pasada hacia atrás para romper empates a la derecha
        profundidad_parentesis = 0 
        
        for j in range(len(lista) - 1, -1, -1):

            # Si el elemento actual es un ')' aumentamos el nivel ANTES de evaluar (yendo hacia atrás)
            if (hasattr(lista[j], tipo_parentesis) == True and getattr(lista[j], tipo_parentesis) == ")"):
               
                profundidad_parentesis = profundidad_parentesis + 1
                continue # Pasamos al siguiente elemento

           
            # Si el elemento actual es un '(' reducimos el nivel DESPUÉS de evaluar (yendo hacia atrás)
            if (hasattr(lista[j], tipo_parentesis) == True and getattr(lista[j], tipo_parentesis) == "("):
               
                profundidad_parentesis = profundidad_parentesis - 1
                continue # Pasamos al siguiente elemento

            # si el elemento que estamos buscando está dentro de un delimitador, pasamos de largo
            
            if (profundidad_parentesis > 0):
                continue

            # dado que no podemos usar isinstance, usamos hasattr para verificar si tiene un atributo
            # es hasattr(objeto, "nombre del atributo"), ejemplo hasattr(array[i], operador) para self.operator...
            # ponemos esto de forma general trabajando con type

            # getattr te devuelve el atributo
            
            if (hasattr(lista[j], tipo) == True):

                precedencia_actual = self.precedencia[getattr(lista[j], tipo)]
            
                # Comprobamos si la precedencia actual es menor que nuestra cota superior (supremo)
                if (precedencia_actual < menor_precedencia_encontrada):

                    menor_precedencia_encontrada = precedencia_actual

                    nodo_central_detectado = lista[j] # colocamos esto como nodo central detectado localmente

                    posicion_lista = j # guardamos la posición donde hemos encontrado el último operador


        # fuera del for

        # para los delimitadores

        nueva_lista = []

        if (posicion_lista == -1): # si es -1 sabemos que hemos encontrado un delimitador ya que entramos en el continue en lugar de lo siguiente
        
        # que es evaluar el valor de position_array
           
            # ahora queremos saber si dentro de este array que estamos buscando el primer elemento es un ( y el último un )
            if (hasattr(lista[0], tipo_parentesis) == True and getattr(lista[0], tipo_parentesis) == "("):
                
                
                if (hasattr(lista[-1], tipo_parentesis) == True and getattr(lista[-1], tipo_parentesis) == ")"):

                    for i in range(1, len(lista)-1): # creamos una lista nueva que contenga lo que está dentro de los delimitadores
                        nueva_lista.append(lista[i])

                    # una vez que hemos creado este array, llamamos a la función recursiva con un return

                    return self.crear_ast(nueva_lista, tipo, tipo_parentesis)


        lista_derecha = []

        lista_izquierda = []

        # cambiamos un for manual por slicing
        
        lista_izquierda = lista[0:posicion_lista]
        lista_derecha = lista[posicion_lista + 1:len(lista)]
        
        # ahora usamos recursividad y llamamos de nuevo a la misma función pero para cada array
        branca_derecha = self.crear_ast(lista_derecha, tipo, tipo_parentesis)
        
        branca_izquierda = self.crear_ast(lista_izquierda, tipo, tipo_parentesis)
        
        # usamos la derecha y la izquierda para crear el AST y devolverlo (recursividad)
        nuevo_nodo = AST(nodo_central_detectado, branca_derecha, branca_izquierda) # Pasamos el operador detectado correctamente
        
        return nuevo_nodo

    

    def contar_nodos_ast(self, nodo): # necesitamos una funcion que nos diga cuantos nodos hay, es muy util para saber si hay que simplificar o no

        contar_nodos = 0

        if (nodo != None): # si el central no es none
            contar_nodos = contar_nodos + 1

        else: # si el actual es None devolvemos el resultado 
            return contar_nodos

        if (nodo.nodo_derecha != None): # si el derecha no esta vacio
            contar_nodos = contar_nodos + self.contar_nodos_ast(nodo.nodo_derecha) # llmamamos a contar nodos recursivamente

        if (nodo.nodo_izquierda != None):
            contar_nodos = contar_nodos + self.contar_nodos_ast(nodo.nodo_izquierda)

        return contar_nodos # si el derecha o izquierda es None no van a hacer recursividad y tenemos que devolver el valor
