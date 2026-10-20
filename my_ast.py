# un AST es una clase que transforma la lista de operaciones en un árbol facilitando la evaluación de los elementos
# debido a que el AST se utilizará en más de una carpeta, vamos a colocar este archivo fuera de todas las carpetas
class AST():

    # precedence es un diccionario que contiene cómo funciona la operación (la precedencia)
    precedence = {
        "¬":5,
        "^":4,
        "v":3,
        "-->":2,
        "<-->":1

    }

    
    def __init__(self, central_node, right_node = None, left_node = None): # necesita un nodo central y dos hijos que pueden ser nulos

        self.central_node = central_node
        self.right_node = right_node
        self.left_node = left_node



    def create_ast(self, array, type, delimeter_type): # aquí queremos saber, para el array de elementos, 
        # si hay un elemento con la menor precedencia; ese será el primer nodo


        # caso base para la recursividad
        if (len(array) == 0): # caso para el negativo ¬; puede ocurrir que un nodo sea None
            return None
        else:
            if (len(array)== 1): # si por recursividad solo tenemos un elemento
                return AST(array[0])

            
        position = 0 # usamos position para saber cuál fue la posición de menor precedencia; en caso de haber más de una, elegimos la de la derecha

        delimeter_level = 0 # una variable que cuenta si estamos dentro de uno, dos o más delimitadores,
        # sumamos uno cuando encontramos un ( y restamos uno cuando encontramos un )
        
        self.central_node = None

        position_array = -1 # declaramos esta función que guarda cuál es la posición del array
        for i in range(len(self.precedence)-1, -1,-1):
            

            if (self.central_node == None): # esto sirve para hacer menos bucles
                position = position + 1
                for j in range(0, len(array)):

                    # para cada elemento buscamos con otro for si hay un ( antes de este operador y sumamos 1 al nivel de delimitadores
                    delimeter_level = 0 # volvemos a poner la variable en 0
                    for k in range(0, j):

                        if (hasattr(array[k], delimeter_type) == True and getattr(array[k], delimeter_type) == "("):
                            delimeter_level = delimeter_level + 1

                        else:
                            if (hasattr(array[k], delimeter_type) == True and getattr(array[k], delimeter_type) == ")"):
                                delimeter_level = delimeter_level - 1

                    # si el elemento que estamos buscando está dentro de un delimitador,
                    # con continue hacemos que el for pase a la siguiente iteración del bucle en lugar de crear el nodo
                    # para que el nodo central siempre quede fuera de los delimitadores

                    if (delimeter_level > 0):
                        continue

                    # dado que no podemos usar isinstance, usamos hasattr para verificar si tiene un atributo
                    # es hasattr(objeto, "nombre del atributo"), ejemplo hasattr(array[i], operador) para self.operator...
                    # ponemos esto de forma general trabajando con type

                    # getattr te devuelve el atributo
                    if (hasattr(array[j], type) == True and position == self.precedence[getattr(array[j], type)]):
                    # también comprobamos si la precedencia es la misma
                        self.central_node = array[j] # colocamos esto como nodo central; nota que como este for terminará en el último elemento, el nodo central será el último elemento con menor precedencia
                        position_array = j # guardamos la posición donde hemos encontrado el último operador


        # fuera del for

        # para los delimitadores

        new_array = []
        if (position_array == -1): # si es -1 sabemos que hemos encontrado un delimitador ya que entramos en el continue en lugar de lo siguiente
        # que es evaluar el valor de position_array
            # ahora queremos saber si dentro de este array que estamos buscando el primer elemento es un ( y el último un )
            if (hasattr(array[0], delimeter_type) == True and getattr(array[0], delimeter_type) == "("):
                
                if (hasattr(array[len(array)-1], delimeter_type) == True and getattr(array[len(array)-1], delimeter_type) == ")"):

                    for i in range(1, len(array)-1): # creamos una lista nueva que contenga lo que está dentro de los delimitadores
                        new_array.append(array[i])

                    # una vez que hemos creado este array, llamamos a la función recursiva con un return

                    return self.create_ast(new_array, type, delimeter_type)


        right_list = []
        left_list = []


        for i in range(0, len(array)): # otro for pero ahora para crear las 2 listas que serán el nodo derecho e izquierdo,
            # usamos el elemento position_array para saber si estará a la derecha o a la izquierda
                   
        
            if(i < position_array):
                left_list.append(array[i])
                            
        
            else:
                if (i > position_array):
                    right_list.append(array[i])
        
        # ahora usamos recursividad y llamamos de nuevo a la misma función pero para cada array
        right_branch = self.create_ast(right_list, type, delimeter_type)
        left_branch = self.create_ast(left_list, type, delimeter_type)
        
        # usamos la derecha y la izquierda para crear el AST y devolverlo (recursividad)
        new_node = AST(self.central_node, right_branch, left_branch)
        
        return new_node
