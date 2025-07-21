class Calculator :
    
    def add(self,a,b):
        if (type(a)==int or type(a) == float) and (type(b)==int or type(b) == float):
            return a+b
        else:
            return "Error: the input must be numbers"
    def subtract(self,a,b):
        if (type(a)==int or type(a) == float) and (type(b)==int or type(b) == float):
            return a-b
        else:
            return "Error: the input must be numbers"
    def multiply(self,a,b):
        if (type(a)==int or type(a) == float) and (type(b)==int or type(b) == float):
            return a*b
        else:
            return "Error: the input must be numbers"
    def divide(self,a,b):
        if (type(a)==int or type(a) == float) and (type(b)==int or type(b) == float):
            if b==0:
                 return "Error: cannot divide by zero"
            else :    
                 return a/b
        else :
            return "Error: the input must be numbers"
           
        

calc= Calculator()
print(calc.add(5,3)) 
print(calc.subtract(5,3))
print(calc.multiply(5,3))
print(calc.divide(5,0))