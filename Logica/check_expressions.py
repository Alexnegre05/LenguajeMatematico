import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from binary_operation import Logic, Proposition, Operator, Delimeter, Operation

class Check(Logic):

 
  def check_delimeters(self):

    # we check that the delimiters have the same ( than )
    
        count_delimiters_left = 0
        count_delimiters_right = 0
    
    
        for i in range (0, len(self.array)):
          
          if (isinstance(self.array[i], Delimeter) == True):  # we check if the element is a delimeter
    
            if (self.array[i].delimeter == ")"):
              count_delimiters_right = count_delimiters_right + 1
            else:
              count_delimiters_left = count_delimiters_left + 1
            
    
        if (count_delimiters_left != count_delimiters_right): # if its not equal we raise an exception
          raise Exception("the delimiters right and left are not equal")
    
        # now we check that we do not have something like ) ( by cheking if the right deliemeters are always <= leff delimeters
    
        count_delimiters_left = 0
        count_delimiters_right = 0
        
        for i in range (0, len(self.array)):
          
          if (isinstance(self.array[i], Delimeter) == True):  # we check if the element is a delimeter
    
            if (self.array[i].delimeter == ")"):
              count_delimiters_right = count_delimiters_right + 1
            else:
              count_delimiters_left = count_delimiters_left + 1
    
            if (count_delimiters_right > count_delimiters_left):
              raise Exception("the delimiters right and left are not equal")
    


  # here we have a function that eliminates only the first and the last delimiters if we bigin with a delimiter and we finish with another one
  # examplo from (p^q) to only p^q we have also to take care of cases such as (p^q)^(pvq) because here we can not eliminate the delimeters
  def eliminate_exterior_delimiters(self):


    # here we check if we have a last ) and (, if not we return 0
    if (len(self.array) < 2 or isinstance(self.array[0], Delimeter) == False or self.array[0].delimeter != "(" or isinstance(self.array[len(self.array)-1], Delimeter) == False or self.array[len(self.array)-1].delimeter != ")"):
      return 0
    
    count_delimiters = 0
    
    for i in range(0, len(self.array)):

      if (isinstance(self.array[i],Delimeter) == True):

        if (self.array[i].delimeter == "("): # we add one when we find ( and substract one for )
          count_delimiters = count_delimiters + 1

        else:
          count_delimiters = count_delimiters - 1



      if (isinstance(self.array[i], Delimeter) == True):

        if ((i == (len(self.array) - 1)) and count_delimiters == 0 and self.array[i].delimeter == ")"): # we check that only is 0 when we are at the end and the last one is a )

          return 1

    return 0 # we return 0 if the delimeters are not at the end

  def eliminate_redundant_delimiters(self): # we will return 1 only if we have found a double delimeter
    # we go backwards
    

    value_iterator = -1
    

    for i in range(len(self.array)- 2,-1,-1): # we go up to -1 for the case of 0
          

      # we have found a double delimeter that is )) we 
      if(isinstance(self.array[i], Delimeter) == True and self.array[i].delimeter == ")"):
        if(isinstance(self.array[i + 1], Delimeter) == True and self.array[i+1].delimeter == ")"):

          value_iterator = i
          break


    # another for but we check if we have found another delimiters,
    #  the if initial is to eliminate having to do the for in case we have not found ))

    if (value_iterator != -1):

      number_of_delimeters = 0 # we use that to check if the numberis correct and know if we have or not to eliminate the delimiters
      # cases such as ((p^q)) v (( r v s)) 
      
      for i in range(value_iterator,-1,-1):

          if (isinstance(self.array[i], Delimeter) == True and self.array[i].delimeter == ")"):
            number_of_delimeters = number_of_delimeters + 1
          elif (isinstance(self.array[i], Delimeter) == True and self.array[i].delimeter == "("):
            number_of_delimeters = number_of_delimeters -1  # we substract in this case


          # here we check that everything is ok
          # the same check but for (, since we know of the elif that the last element is a ( we only have to check the one before for the ((
          # the i >0 is for i -1

          if (number_of_delimeters == 0 and i > 0):
            if(isinstance(self.array[i - 1], Delimeter) == True and i != value_iterator and self.array[i-1].delimeter == "("): 
              #we are checking that the i goes backwards so instead of i+1 is i -1
              
               # we eliminate the positions where it was a () extra
              del self.array[value_iterator + 1]
              del self.array[i - 1]

              return 1

    return 0






  def check(self): # function that checks if the array is correct it will send 0 if not 1 if its all correct

    self.check_delimeters() # we check that everything with delimeters is ok

    value = 1

    while (value == 1): # this code is to eliminate the exterior delimeters ( expresion )
    # the loop is for the case of more than one delimeter such as (( expresion ))

      value = self.eliminate_exterior_delimiters() # we eliminate if we can the exteriors delimeters, if we recibe a 1

      if (value == 1):
        self.array.pop(0) # we substract the first and the last element
        self.array.pop(len(self.array) - 1)

    

    value2 = 1
    while(value2 == 1):
      
      value2 = self.eliminate_redundant_delimiters()

    length = len(self.array)
    i = 0 # (number that holds the position of the array)

    # loop that goes for every position in the array
    while (i < length):

      # here we check that a user has put or an operator or a proposition or delimeter
      if (isinstance(self.array[i], Proposition) == False and isinstance(self.array[i], Operator) == False and isinstance(self.array[i], Delimeter) == False):
        raise Exception("the expression contains elements that are not or a proposition or an operator or a delimeter")



      # special cases the first and the last element of the array
      if (i == 0):
        # here we check if the element is a proposition by cheking the oposite
        if (isinstance(self.array[i], Proposition) == False and isinstance(self.array[i], Delimeter) == False):
          # here we know that this is a operation so nom we check if the value is not ¬

          if (self.array[i].operator != "¬"):

            return 0 # then we know that the first element is or ^... so the expression is wrong


      elif(i == (length - 1)): # the last one can only be a proposition and the one before it can only be an operation
       
        
        # CASE A: If the last element is a Proposition, we validate the previous one (Your original logic)

        if (isinstance(self.array[i], Proposition) == True):
          if (isinstance(self.array[i-1], Operator) == False):
            return 0

        # CASE B: If the last element is a Delimiter, we make sure that it is ")" and not "("

        if (isinstance(self.array[i], Delimeter) == True):
          if (self.array[i].delimeter == "("):
            return 0

        # CASE C: If it is neither a Proposition nor a Delimiter (for example, it ends in ^), it is wrong

        if (isinstance(self.array[i], Proposition) == False and isinstance(self.array[i], Delimeter) == False):
          return 0

          

        
        # special case p ¬ q if and only if i >=2 because if not i - 2 could be out of range
        if (i >= 2 and isinstance(self.array[i], Proposition) == True and isinstance(self.array[i-1], Operator) == True and self.array[i-1].operator == "¬" and isinstance(self.array[i-2], Proposition) == True):
          return 0

      else: # the general case
        # first we check that if we have a proposition that the before it is not a proposition
        if (isinstance(self.array[i], Proposition) == True and isinstance(self.array[i-1], Proposition) == True):

          return 0

        # we do the same but for operators but without the ¬ is not the expresion that we are seeing, example this is posible ^¬ because later is a p but this not ¬^

        if (isinstance(self.array[i], Operator) == True and isinstance(self.array[i-1], Operator) == True and self.array[i].operator != "¬"):

          return 0

        # here we check that we do not have the case for ¬ ¬
        if (isinstance(self.array[i], Operator) == True and isinstance(self.array[i-1], Operator) == True and self.array[i].operator == "¬" and self.array[i-1].operator == "¬"):

          return 0

        # here we check that we do not have the case for p ¬ q and we check that i > 2
        if (i >= 2 and isinstance(self.array[i], Proposition) == True and isinstance(self.array[i-1], Operator) == True and self.array[i-1].operator == "¬" and isinstance(self.array[i-2], Proposition) == True):
          return 0


        # cases of delimeters 

         # CASE 1: Prevent a binary operator right after an opening parenthesis (e.g., "( ^ p")
        if (isinstance(self.array[i-1], Delimeter) == True and self.array[i-1].delimeter == "(" and isinstance(self.array[i], Operator) == True and self.array[i].operator != "¬"):
          
          return 0

        # CASE 2: Prevent a closing parenthesis right after an operator (e.g., "p ^ )")
        if (isinstance(self.array[i-1], Operator) == True and isinstance(self.array[i], Delimeter) == True and self.array[i].delimeter == ")"):
          
          return 0

        # CASE 3: Prevent an opening parenthesis right after a proposition without an operator (e.g., "p ( q )")
        if (isinstance(self.array[i-1], Proposition) == True and isinstance(self.array[i], Delimeter) == True and self.array[i].delimeter == "("):
          
          return 0

        # CASE 4: Prevent a proposition right after a closing parenthesis without an operator (e.g., "( p ) q")
        if (isinstance(self.array[i-1], Delimeter) == True and self.array[i-1].delimeter == ")" and isinstance(self.array[i], Proposition) == True):
          
          return 0




      # at the end we always sum
      i = i + 1

    # END OF LOOP
    # at the end of the loop if we have arrived here means that everything is ok so we sent a 1

    return 1