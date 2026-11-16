from Logica.modelos import  Operador, Proposicion



class SimplificadorArbol:
    
    def __init__(self):
        pass

    
    def simplificar_doble_negacion(self, nodo_actual): # funcion que simplifica la doble negacion

        

        # 1. Caso sin paréntesis: el otro "¬" quedó atrapado en la rama izquierda
        nodo_izq = nodo_actual.nodo_izquierda

        if (nodo_izq is not None and isinstance(nodo_izq.nodo_central, Operador) == True and nodo_izq.nodo_central.operador == "¬"):
            
            nieto = nodo_actual.nodo_derecha

            if (nieto is not None and nieto.nodo_central is not None):

                return nieto

        # 2. Caso estándar con paréntesis: el otro "¬" está en la rama derecha
        nodo_der = nodo_actual.nodo_derecha

        if (nodo_der is not None and isinstance(nodo_der.nodo_central, Operador) == True and nodo_der.nodo_central.operador == "¬"):
            
            nieto = nodo_der.nodo_derecha

            if (nieto is not None and nieto.nodo_central is not None):

                return nieto

        return nodo_actual






    def simplificar_py0(self, nodo_actual):

            

            nodo_izq = nodo_actual.nodo_izquierda
            nodo_der = nodo_actual.nodo_derecha

            # Caso p ^ 0 = 0 (funciona tanto si p es una letra como si es un subárbol con paréntesis)
            if (nodo_der is not None and (isinstance(nodo_der.nodo_central, Proposicion) == True) and nodo_der.nodo_central.value == 0):
                return nodo_der

            # Caso 0 ^ p = 0 (la inversa)
            if (nodo_izq is not None and (isinstance(nodo_izq.nodo_central, Proposicion) == True) and nodo_izq.nodo_central.value == 0):
                return nodo_izq

            return nodo_actual


    def simplificar_py1(self, nodo_actual): # lo mismo pero ahora devolvemos p

       

        nodo_izq = nodo_actual.nodo_izquierda

        nodo_der = nodo_actual.nodo_derecha

        # Caso p ^ 1 = p (devolvemos el nodo izquierdo completo, conservando sus hijos si es un subárbol)
        if (nodo_der is not None and (isinstance(nodo_der.nodo_central, Proposicion) == True) and nodo_der.nodo_central.value == 1):

            return nodo_izq

        # Caso 1 ^ p = p (la inversa)
        if (nodo_izq is not None and (isinstance(nodo_izq.nodo_central, Proposicion) == True) and nodo_izq.nodo_central.value == 1):

            return nodo_der

        return nodo_actual





    
    def simplificar_pyp(self, nodo_actual):

        nodo_izq = nodo_actual.nodo_izquierda

        nodo_der = nodo_actual.nodo_derecha

        if (nodo_izq is not None and (isinstance(nodo_izq.nodo_central, Proposicion) == True)):

            if (nodo_der is not None and (isinstance(nodo_der.nodo_central, Proposicion) == True)):

                if (nodo_der.nodo_central.value == nodo_izq.nodo_central.value):

                    nodo_actual.nodo_central = nodo_der.nodo_central
                    nodo_actual.nodo_izquierda = None
                    nodo_actual.nodo_derecha = None

        return nodo_actual




    def simplificar_pynop(self, nodo_actual):

        nodo_izq = nodo_actual.nodo_izquierda

        nodo_der = nodo_actual.nodo_derecha

        # caso p ^ ¬p

        if (nodo_izq is not None and isinstance(nodo_izq.nodo_central, Proposicion) == True):

            if (nodo_der is not None and isinstance(nodo_der.nodo_central, Operador) == True and nodo_der.nodo_central.operador == "¬"):

                nieto_der = nodo_der.nodo_derecha

                if (nieto_der is not None and isinstance(nieto_der.nodo_central, Proposicion) == True):

                    if (nieto_der.nodo_central.value == nodo_izq.nodo_central.value):

                        nodo_actual.nodo_central = Proposicion(0)

                        nodo_actual.nodo_derecha = None

                        nodo_actual.nodo_izquierda = None

        # caso ¬p ^ p

        elif (nodo_izq is not None and isinstance(nodo_izq.nodo_central, Operador) == True and nodo_izq.nodo_central.operador == "¬"):

            if (nodo_der is not None and isinstance(nodo_der.nodo_central, Proposicion) == True):

                nieto_izq = nodo_izq.nodo_derecha

                if (nieto_izq is not None and isinstance(nieto_izq.nodo_central, Proposicion) == True):

                    if (nieto_izq.nodo_central.value == nodo_der.nodo_central.value):

                        nodo_actual.nodo_central = Proposicion(0)

                        nodo_actual.nodo_derecha = None

                        nodo_actual.nodo_izquierda = None

        return nodo_actual



    


    def simplificar_po0(self, nodo_actual):

        nodo_izq = nodo_actual.nodo_izquierda

        nodo_der = nodo_actual.nodo_derecha

        if (nodo_izq is not None and (isinstance(nodo_izq.nodo_central, Proposicion) == True)):

            if (nodo_der is not None and (isinstance(nodo_der.nodo_central, Proposicion) == True)):

                if (nodo_der.nodo_central.value == 0):

                    nodo_actual.nodo_central = nodo_izq.nodo_central
                    nodo_actual.nodo_izquierda = None
                    nodo_actual.nodo_derecha = None

        # caso 0 v p, la inversa

        elif (nodo_der is not None and (isinstance(nodo_der.nodo_central, Proposicion) == True)):

            if (nodo_izq is not None and (isinstance(nodo_izq.nodo_central, Proposicion) == True)):

                if (nodo_izq.nodo_central.value == 0):

                    nodo_actual.nodo_central = nodo_der.nodo_central
                    nodo_actual.nodo_izquierda = None
                    nodo_actual.nodo_derecha = None

        return nodo_actual




    def simplificar_po1(self, nodo_actual): # lo mismo pero ahora devolvemos 1

        nodo_izq = nodo_actual.nodo_izquierda

        nodo_der = nodo_actual.nodo_derecha

        if (nodo_izq is not None and (isinstance(nodo_izq.nodo_central, Proposicion) == True)):

            if (nodo_der is not None and (isinstance(nodo_der.nodo_central, Proposicion) == True)):

                if (nodo_der.nodo_central.value == 1):

                    nodo_actual.nodo_central = nodo_der.nodo_central
                    nodo_actual.nodo_izquierda = None
                    nodo_actual.nodo_derecha = None

        # caso 1 v p, la inversa

        elif (nodo_der is not None and (isinstance(nodo_der.nodo_central, Proposicion) == True)):

            if (nodo_izq is not None and (isinstance(nodo_izq.nodo_central, Proposicion) == True)):

                if (nodo_izq.nodo_central.value == 1):

                    nodo_actual.nodo_central = nodo_izq.nodo_central
                    nodo_actual.nodo_izquierda = None
                    nodo_actual.nodo_derecha = None

        return nodo_actual



    def simplificar_pop(self, nodo_actual):

        nodo_izq = nodo_actual.nodo_izquierda

        nodo_der = nodo_actual.nodo_derecha

        if (nodo_izq is not None and (isinstance(nodo_izq.nodo_central, Proposicion) == True)):

            if (nodo_der is not None and (isinstance(nodo_der.nodo_central, Proposicion) == True)):

                if (nodo_der.nodo_central.value == nodo_izq.nodo_central.value):

                    nodo_actual.nodo_central = nodo_der.nodo_central
                    nodo_actual.nodo_izquierda = None
                    nodo_actual.nodo_derecha = None

        return nodo_actual




    def simplificar_ponop(self, nodo_actual):

        nodo_izq = nodo_actual.nodo_izquierda

        nodo_der = nodo_actual.nodo_derecha

        # caso p v ¬p

        if (nodo_izq is not None and isinstance(nodo_izq.nodo_central, Proposicion) == True):

            if (nodo_der is not None and isinstance(nodo_der.nodo_central, Operador) == True and nodo_der.nodo_central.operador == "¬"):

                nieto_der = nodo_der.nodo_derecha

                if (nieto_der is not None and isinstance(nieto_der.nodo_central, Proposicion) == True):

                    if (nieto_der.nodo_central.value == nodo_izq.nodo_central.value):

                        nodo_actual.nodo_central = Proposicion(1)
                        nodo_actual.nodo_derecha = None
                        nodo_actual.nodo_izquierda = None

        # caso ¬p v p

        elif (nodo_izq is not None and isinstance(nodo_izq.nodo_central, Operador) == True and nodo_izq.nodo_central.operador == "¬"):

            if (nodo_der is not None and isinstance(nodo_der.nodo_central, Proposicion) == True):

                nieto_izq = nodo_izq.nodo_derecha

                if (nieto_izq is not None and isinstance(nieto_izq.nodo_central, Proposicion) == True):

                    if (nieto_izq.nodo_central.value == nodo_der.nodo_central.value):

                        nodo_actual.nodo_central = Proposicion(1)
                        nodo_actual.nodo_derecha = None
                        nodo_actual.nodo_izquierda = None

        return nodo_actual



        # ley que simplifica el caso 0 --> p = 1
    def simplificar_cond0(self, nodo_actual):

        nodo_izq = nodo_actual.nodo_izquierda

        if (nodo_izq is not None and isinstance(nodo_izq.nodo_central, Proposicion) == True):

            if (nodo_izq.nodo_central.value == 0):

                nodo_actual.nodo_central = Proposicion(1)
                nodo_actual.nodo_izquierda = None
                nodo_actual.nodo_derecha = None

        return nodo_actual




    # ley que simplifica el caso p --> 1 = 1
    def simplificar_cond1(self, nodo_actual):

        nodo_der = nodo_actual.nodo_derecha

        if (nodo_der is not None and isinstance(nodo_der.nodo_central, Proposicion) == True):

            if (nodo_der.nodo_central.value == 1):

                nodo_actual.nodo_central = Proposicion(1)
                nodo_actual.nodo_izquierda = None
                nodo_actual.nodo_derecha = None

        return nodo_actual






        
        






    def simplificar_general(self, arbol): # funcion que se encarga unicamente de comprovar si al llamar a las funciones que simplifican el arbol si se ha simplificado o no, si no lo ha hecho salimos

        if (arbol is None):
            return None
        
        cambios = True  # si es true el while continua en caso contrario el while se detiene

        while(cambios == True):

            numero_nodos = arbol.contar_nodos_ast(arbol) # esta funcion nos dice el numero de nodos de un AST

                
            arbol = self.simplificar(arbol)

            if (arbol is None): # si el arbol es none salimos de aqui, nos ahorramos el if else
                break
                
            
            numero_actual_nodos = arbol.contar_nodos_ast(arbol)
            
            
            print(numero_nodos)
            print(numero_actual_nodos)

            if (numero_actual_nodos == numero_nodos): # si no se ha simplificado cambios es false

                cambios = False

          
            
        return arbol # devolvemos el arbol simplificado








    def simplificar(self, arbol): # funcion que simplifica el arbol
    # solo vamos a programar aquellas funciones que simplifican el arbol

        if (arbol == None):
            return None

        # primera simplificacion ¬ ¬ p == p

        derecha = arbol.nodo_derecha

        izquierda = arbol.nodo_izquierda

        central = arbol.nodo_central


        if (hasattr(arbol, 'nodo_derecha') and derecha != None): 
        
            arbol.nodo_derecha = self.simplificar(derecha)
        
        if (hasattr(arbol, 'nodo_izquierda') and izquierda != None): 
                
            arbol.nodo_izquierda = self.simplificar(izquierda)

        # Si el nodo central no tiene un operador válido no hay nada que simplificar
        if central is None or hasattr(central, 'operador') == False:
            return arbol

        operador = central.operador # comprovamos antes el operador

        if (operador == "¬"):
        
            arbol = self.simplificar_doble_negacion(arbol) # aqui recibimos el primer nodo 

            
        if (operador == "^"):

            arbol = self.simplificar_py0(arbol)

        if (operador == "^"):
            
            arbol = self.simplificar_py1(arbol)

        if (operador == "^"):
            
            arbol = self.simplificar_pyp(arbol)

        if (operador == "^"):
            
            arbol = self.simplificar_pynop(arbol)

        if (operador == "v"):
            arbol = self.simplificar_po0(arbol)

        if (operador == "v"):
            
            arbol = self.simplificar_po1(arbol)

        if (operador == "v"):

            arbol = self.simplificar_pop(arbol)

        if (operador == "v"):

            arbol = self.simplificar_ponop(arbol)

        if (operador == "-->"):
            arbol = self.simplificar_cond0(arbol)

        if (operador == "-->"):
            arbol = self.simplificar_cond1(arbol)

        return arbol # al final devolvemos el arbol # una vez que hemos terminado con la recursividad
