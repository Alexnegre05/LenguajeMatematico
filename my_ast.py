# an AST is a class that transforms the list of operations into a tree making more easy the evaluation of the elements
# because the AST will be used by more than one folder,we are going to put this file outside every folder
class AST():

    # precedence is a dictionary that contains how the operation works(the precedence)
    precedence = {
        "¬":5,
        "^":4,
        "v":3,
        "-->":2,
        "<-->":1

    }

    
    def __init__(self, central_node, right_node = None, left_node = None): # it needs a central node and two childs that can be none

        self.central_node = central_node
        self.right_node = right_node
        self.left_node = left_node



    def create_ast(self, array, type): # here we want to know for the array of elements 
        # if there is an element with the least precedence, that will be the first node


        # base case for recursivity
        if (len(array) == 0): # case for negative ¬ it can happen that one node is None
            return None
        else:
            if (len(array)== 1): # if for recursivity we only have one element
                return AST(array[0])

            
        position = 0 # we use position to know what was the position of the least precedence, in case of more than one we chose the one of the right
        # reversed is used so that the iteration in the for goes backwards
        
        self.central_node = None

        for operator in reversed(self.precedence):
            

            if (self.central_node == None): # this is to make less loops
                position = position + 1
                for i in range(0, len(array)):

                    # since we can not use isinstance, we use hasastr for has an atribute
                    # is hasastr(object, "name of the atribute"), example hasatr(array[i], operator) for self,operator...
                    # we put this in general by working with type

                    # get atttr it gives you the atribute
                    if (hasattr(array[i], type) == True and position == self.precedence[getattr(array[i], type)]):
                    # we also check if the precedence is the same
                        self.central_node = array[i] # we put this as a central node, note that since this for will end at the last element the central node is the last element with least precedence
                        position_array = i # we keep the position where we have found the last operator


        # outside the for
        right_list = []
        left_list = []
        
        for i in range(0, len(array)): # another for but now to create the 2 lists that will be the right and left node,
            # we use the position array element to know if it will be on the right or on the left
                   
        
            if(i < position_array):
                left_list.append(array[i])
                            
        
            else:
                if (i > position_array):
                    right_list.append(array[i])
        
        # now we use recursivity and we call the same function again but for each array
        right_branch = self.create_ast(right_list, type)
        left_branch = self.create_ast(left_list, type)
        
        # we use the right and the left to create the AST and return it(recursivity)
        new_node = AST(self.central_node, right_branch, left_branch)
        
        return new_node



