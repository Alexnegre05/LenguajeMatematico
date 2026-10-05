import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from logic_elements import Logic, Operator, Proposition, Delimeter
from my_ast import AST


class TreeSimplification:
    
    def __init__(self):
        pass

    def simplify_double_negation(self, actual_node): # function that simplify the double negation


        node_null = False # if we find that a node is null we stop searching 

        while (node_null == False):
        
            if (actual_node.central_node == None): # we exit the while
        
                node_null = True
        
            else:
        
                if ((isinstance(actual_node.central_node, Operator) == True) and actual_node.central_node.operator == "¬"): # if the node is an operation and its ¬
                
                    # we check if its have sons, its and  and if the operator is ¬
                    node = actual_node.right_node # we put this into node so tahat we don't have to worry aboiut to much node.node. ...
            
                    if ((isinstance(node.central_node, Operator) == True) and node.central_node != None and node.central_node.operator == "¬"):
            
                        node = actual_node.right_node.right_node

                        if (node.central_node != None and isinstance(node.central_node, Proposition) == True):

                            # we write ¬¬p = p
                            actual_node = node.central_node
                            actual_node.right_node = None 
                            actual_node.left_node = None
                            node_null = True
                        
                        else:
                            node_null = True
                    else:
                        node_null = True
                else:
                    node_null = True

        return actual_node # we return the tree


    

    def simplify(self, tree): # function that simplifies the tree
    # we are only going to program those functions that simplify the tree

        # first simplification ¬ ¬ p == p

        if (tree.right_node != None): # if the ones bellow thsi node are not null we call this function again(the simplify tree)
    
            tree.right_node = self.simplify(tree.right_node)
    
        if (tree.left_node != None):
            
            tree.left_node = self.simplify(tree.left_node)

        tree = self.simplify_double_negation(tree) # here we recibe the first node 

        
    
    
        return tree # at the end we return the tree # once we are done with the recursive
    