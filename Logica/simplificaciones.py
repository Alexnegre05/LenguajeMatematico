from Logica.modelos import  Operador, Proposicion



class SimplificadorArbol:
    
    def __init__(self):
        pass

    
    def simplificar_doble_negacion(self, nodo_actual): # function that simplify the double negation


        nodo_nulo = False # if we find that a node is null we stop searching 

        while (nodo_nulo == False):
        
            if (nodo_actual == None or nodo_actual.nodo_central == None): # we exit the while
        
                nodo_nulo = True
        
            else:
        
                if ((isinstance(nodo_actual.nodo_central, Operador) == True) and nodo_actual.nodo_central.operador == "¬"): # if the node is an operation and its ¬
                
                    # we check if its have sons, its and  and if the operator is ¬
                    
                    # Verificamos si en la izquierda se quedó atrapado el otro operador "¬"
                    nodo_izq = nodo_actual.nodo_izquierda
            
                    if (nodo_izq != None and (isinstance(nodo_izq.nodo_central, Operador) == True) and nodo_izq.nodo_central.operador == "¬"):
            
                        # En la estructura plana sin paréntesis, la proposición real está a la derecha de la raíz
                        
                        nieto = nodo_actual.nodo_derecha 

                        if (nieto != None and nieto.nodo_central != None and isinstance(nieto.nodo_central, Proposicion) == True):

                            # we write ¬¬p = p

                            # Reemplazamos la raíz completa por el nodo de la proposición pura
                            nodo_actual = nieto 

                            nodo_actual.nodo_derecha = None 

                            nodo_actual.nodo_izquierda = None
                           
                            nodo_nulo = True
                        
                        else:
                            nodo_nulo = True
                    else:
                        # Si no estaba a la izquierda, aplicamos el caso estándar para cuando viene con paréntesis
                        nodo_der = nodo_actual.nodo_derecha
                        
                        if (nodo_der != None and (isinstance(nodo_der.nodo_central, Operador) == True) and nodo_der.nodo_central.operador == "¬"):
                           
                            
                            nieto = nodo_der.nodo_derecha
                            
                            if (nieto != None and nieto.nodo_central != None and isinstance(nieto.nodo_central, Proposicion) == True):
                                nodo_actual = nieto
                                
                                nodo_actual.nodo_derecha = None
                                
                                nodo_actual.nodo_izquierda = None
                                
                                nodo_nulo = True
                            
                            else:
                                nodo_nulo = True
                                
                        else:
                            nodo_nulo = True
                else:
                    nodo_nulo = True

        return nodo_actual # we return the tree







    def simplificar_general(self, arbol): # funcion que se encarga unicamente de comprovar si al llamar a las funciones que simplifican el arbol si se ha simplificado o no, si no lo ha hecho salimos

        numero_nodos = 0
        
        numero_actual_nodos = - 1  # otra variable que va a ir cambiando que va a ser los nodos despues de ver si se puede simplificar
        
        while(numero_nodos != numero_actual_nodos):

            if (arbol != None):
                numero_nodos = arbol.contar_nodos_ast(arbol) # esta funcion nos dice el numero de nodos de un AST

                arbol = self.simplificar(arbol)


                numero_actual_nodos = arbol.contar_nodos_ast(arbol)

            else:
                numero_actual_nodos = numero_nodos # si el arbol es none por algun error ponemos que los nodos sean iguales para salir de el bucle

            print("nodos al inicio: ", numero_nodos)
            print("nodos al simplificar", numero_actual_nodos)
            
        return arbol # devolvemos el arbol simplificado





    def simplificar(self, arbol): # function that simplifies the tree
    # we are only going to program those functions that simplify the tree

        if (arbol == None):
            return None

        # first simplification ¬ ¬ p == p

        if (hasattr(arbol, 'nodo_derecha') and arbol.nodo_derecha != None): 
        
            arbol.nodo_derecha = self.simplificar(arbol.nodo_derecha)
        
        if (hasattr(arbol, 'nodo_izquierda') and arbol.nodo_izquierda != None): 
                
            arbol.nodo_izquierda = self.simplificar(arbol.nodo_izquierda)

        
        arbol = self.simplificar_doble_negacion(arbol) # here we recibe the first node 

            
           
        
        return arbol # at the end we return the tree # once we are done with the recursive
