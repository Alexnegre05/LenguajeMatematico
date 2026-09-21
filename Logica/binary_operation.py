
from logic_elements import Logic, Proposition, Delimeter, Operator




class Operation(Logic): # class that takes two propositions and a operation and give a value of 0 or 1


  def __init__(self, Proposition1, operator, Proposition2):

    if (isinstance(Proposition1,Proposition) == True and isinstance(operator, Operator) == True and isinstance(Proposition2,Proposition) == True): # we use the isinstance to know if it belongs to a concrete class

        self.Proposition1 = Proposition1
        self.operator = operator
        self.Proposition2 = Proposition2

    else:

      if (isinstance(Proposition1,Proposition) == True and isinstance(operator, Operator) == True and operator.operator == "¬"): # case exclusive for the negative

        self.Proposition1 = Proposition1
        self.operator = operator
        self.Proposition2 = None # we put proposition 2 as None to know that is empty




      # personal message of error
      if (isinstance(Proposition1,Proposition) == False):
        raise Exception("The first proposition introduced is not a valid proposition")

      elif (isinstance(operator, Operator) == False):
        raise Exception("the operator introduced is not a valid operator")

      elif (isinstance(Proposition2,Proposition) == False):

        if(isinstance(Proposition1,Proposition) == True and isinstance(operator, Operator) == True and operator.operator == "¬"):
          pass

        else:
          raise Exception("The second proposition introduced is not a valid proposition")

      else:
        print("porque estas aqui")









  def Result(self):

      Proposition1 = self.Proposition1.value
      Operator = self.operator.operator

      # Change to "is None" to fix AttributeError
      if (Operator == "¬" and self.Proposition2 is None):
        Proposition2 = None
      else:
        Proposition2 = self.Proposition2.value

      if (Operator == "^"): # we check one by one which operator are we using

        # we go case by case
        if (Proposition1 == 0 and Proposition2 == 0):
          return 0

        elif (Proposition1 == 1 and Proposition2 == 0):
          return 0

        elif (Proposition1 == 0 and Proposition2 == 1):
          return 0

        elif (Proposition1 == 1 and Proposition2 == 1):
          return 1

      # we do the same for the other operators
      if (Operator == "v"):


        if (Proposition1 == 0 and Proposition2 == 0):
          return 0

        elif (Proposition1 == 1 and Proposition2 == 0):
          return 1

        elif (Proposition1 == 0 and Proposition2 == 1):
          return 1

        elif (Proposition1 == 1 and Proposition2 == 1):
          return 1

      if (Operator == "-->"):


        if (Proposition1 == 0 and Proposition2 == 0):
          return 1

        elif (Proposition1 == 1 and Proposition2 == 0):
          return 0

        elif (Proposition1 == 0 and Proposition2 == 1):
          return 1

        elif (Proposition1 == 1 and Proposition2 == 1):
          return 1


      if (Operator == "<-->"):


        if (Proposition1 == 0 and Proposition2 == 0):
          return 1

        elif (Proposition1 == 1 and Proposition2 == 0):
          return 0

        elif (Proposition1 == 0 and Proposition2 == 1):
          return 0

        elif (Proposition1 == 1 and Proposition2 == 1):
          return 1

      if (Operator == "¬"): # special case, the negative

        if (Proposition1 == 0):
          return 1
        else:
          return 0