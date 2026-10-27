import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Logica.modelos import  Operador, Proposicion



class SimplificadorArbol:
    
    def __init__(self):
        pass

    def simplificar_doble_negacion(self, nodo_actual): # function that simplify the double negation


        nodo_nulo = False # if we find that a node is null we stop searching 

        while (nodo_nulo == False):
        
            if (nodo_actual.nodo_central == None): # we exit the while
        
                nodo_nulo = True
        
            else:
        
                if ((isinstance(nodo_actual.nodo_central, Operador) == True) and nodo_actual.nodo_central.operador == "¬"): # if the node is an operation and its ¬
                
                    # we check if its have sons, its and  and if the operator is ¬
                    
                    nodo = nodo_actual.nodo_derecho # we put this into node so tahat we don't have to worry aboiut to much node.node. ...
            
                    if ((isinstance(nodo.nodo_central, Operador) == True) and nodo.nodo_central != None and nodo.nodo_central.operador == "¬"):
            
                        nodo = nodo_actual.nodo_derecho.nodo_derecho 

                        if (nodo.nodo_central != None and isinstance(nodo.nodo_central, Proposicion) == True):

                            # we write ¬¬p = p

                            nodo_actual = nodo.nodo_central

                            nodo_actual.nodo_derecho = None 

                            nodo_actual.nodo_izquierdo = None
                            nodo_nulo = True
                        
                        else:
                            nodo_nulo = True
                    else:
                        nodo_nulo = True
                else:
                    nodo_nulo = True

        return nodo_actual # we return the tree





    def simplificar(self, arbol): # function that simplifies the tree
    # we are only going to program those functions that simplify the tree

        # first simplification ¬ ¬ p == p

        if (arbol.nodo_derecha != None): # if the ones bellow this node are not null we call this function again(the simplify tree)
    
            arbol.nodo_derecha = self.simplificar(arbol.nodo_derecha)
    
        if (arbol.nodo_izquierda != None):
            
            arbol.nodo_izquierda = self.simplificar(arbol.nodo_izquierda)

        arbol = self.simplificar_doble_negacion(arbol) # here we recibe the first node 

        
    
    
        return arbol # at the end we return the tree # once we are done with the recursive
