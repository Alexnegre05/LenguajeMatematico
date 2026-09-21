# Document where we put the definitions of the elements we are going to use in logic

class Logic(): # general class that controls everything about logic

  pass



class Proposition(Logic): # class that contains a proposition, it can be false(0) or true(1)

  def __init__(self, value):

    if (value == 0 or value == 1): # checks if the value is correct or not
        self.value = value

    else:
        raise Exception("A proposition only accepts values of 0 or 1")




class Operator(Logic): # class that defines every operator that we need in logic

# the ¬ is done by alt gr +, the arrow by adding - + > (of greater)

  def __init__(self, operator):

    if(operator == "^" or operator == "v" or operator == "¬" or operator == "-->" or operator == "<-->"):  # checks if the operator is valid
      self.operator = operator

    else:
      raise Exception("Operator not valid")

class Delimeter(Logic): # class that defines the () 

  def __init__(self, delimeter):
    
    if (delimeter == "(" or delimeter == ")"):
      self.delimeter = delimeter
    
    else:
      raise Exception("Wrong delimeters")