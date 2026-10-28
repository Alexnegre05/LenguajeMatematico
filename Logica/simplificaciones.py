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
                    
                    nodo = nodo_actual.nodo_derecha # we put this into node so tahat we don't have to worry aboiut to much node.node. ...
            
                    if (nodo != None and (isinstance(nodo.nodo_central, Operador) == True) and nodo.nodo_central.operador == "¬"):
            
                        # ARREGLO 1: Cambiamos 'nodo_actual.nodo_derecha.nodo_derecha' por 'nodo.nodo_derecha'
                        # Como ya guardaste 'nodo_actual.nodo_derecha' en la variable 'nodo', el nieto está en 'nodo.nodo_derecha'
                        nieto = nodo.nodo_derecha 

                        if (nieto != None and nieto.nodo_central != None and isinstance(nieto.nodo_central, Proposicion) == True):

                            # we write ¬¬p = p

                            # ARREGLO 2: Cambiamos 'nodo_actual = nodo.nodo_central' por 'nodo_actual = nieto'
                            # Debes devolver el objeto AST completo (nieto) para que la estructura del árbol no se rompa
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

        if (hasattr(arbol, 'nodo_derecho') and arbol.nodo_derecho != None): # if the ones bellow this node are not null we call this function again(the simplify tree)
        
            arbol.nodo_derecho = self.simplificar(arbol.nodo_derecho)
        
        if (hasattr(arbol, 'nodo_izquierdo') and arbol.nodo_izquierdo != None):
                
            arbol.nodo_izquierdo = self.simplificar(arbol.nodo_izquierdo)

        
        arbol = self.simplificar_doble_negacion(arbol) # here we recibe the first node 

            
           
        
        return arbol # at the end we return the tree # once we are done with the recursive
