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



    def create_ast(self, array, type, delimeter_type): # here we want to know for the array of elements 
        # if there is an element with the least precedence, that will be the first node


        # base case for recursivity
        if (len(array) == 0): # case for negative ¬ it can happen that one node is None
            return None
        else:
            if (len(array)== 1): # if for recursivity we only have one element
                return AST(array[0])

            
        position = 0 # we use position to know what was the position of the least precedence, in case of more than one we chose the one of the right

        delimeter_level = 0 # a variable that counts if we are inside one,two or more delimiters,
        # we add one when we found a ( and we substract one when we found a )
        
        self.central_node = None

        position_array = -1 # we declare this function that keeps what is the position of the array
        for i in range(len(self.precedence)-1, -1,-1):
            

            if (self.central_node == None): # this is to make less loops
                position = position + 1
                for j in range(0, len(array)):

                    # for each element we search with another for if there is a ( before thsi operator and add 1 to delimeters level
                    delimeter_level = 0 # we turn again the variable into 0
                    for k in range(0, j):

                        if (hasattr(array[k], delimeter_type) == True and getattr(array[k], delimeter_type) == "("):
                            delimeter_level = delimeter_level + 1

                        else:
                            if (hasattr(array[k], delimeter_type) == True and getattr(array[k], delimeter_type) == ")"):
                                delimeter_level = delimeter_level - 1

                    # if the element that we are looking for is inside a delimeter, 
                    # with continue we make that the for goes to the next iteraton of the loop instead of creating the node
                    # so that the central node will always be outside the delimeters

                    if (delimeter_level > 0):
                        continue

                    # since we can not use isinstance, we use hasastr for has an atribute
                    # is hasastr(object, "name of the atribute"), example hasatr(array[i], operator) for self,operator...
                    # we put this in general by working with type

                    # get atttr it gives you the atribute
                    if (hasattr(array[j], type) == True and position == self.precedence[getattr(array[j], type)]):
                    # we also check if the precedence is the same
                        self.central_node = array[j] # we put this as a central node, note that since this for will end at the last element the central node is the last element with least precedence
                        position_array = j # we keep the position where we have found the last operator


        # outside the for

        # for the delimeters

        new_array = []
        if (position_array == -1): # if its -1 then we know that we have found a delimeter since we have enter into the continue instead of what comes next
        # that is evaluating the value of position_array
            # know we want to know if inside this array that we are looking for the first element is a ( and the last one a )
            if (hasattr(array[0], delimeter_type) == True and getattr(array[0], delimeter_type) == "("):
                
                if (hasattr(array[len(array)-1], delimeter_type) == True and getattr(array[len(array)-1], delimeter_type) == ")"):

                    for i in range(1, len(array)-1): # we create a nem list that contains what is inside the delimeters
                        new_array.append(array[i])

                    # once we have created this array we call the function recursive witha return

                    return self.create_ast(new_array, type, delimeter_type)


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
        right_branch = self.create_ast(right_list, type, delimeter_type)
        left_branch = self.create_ast(left_list, type, delimeter_type)
        
        # we use the right and the left to create the AST and return it(recursivity)
        new_node = AST(self.central_node, right_branch, left_branch)
        
        return new_node



