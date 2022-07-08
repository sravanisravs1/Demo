class calculator():
     def __init__(self,a=None,b=None):
      self.a=a 
      self.b=b
     def addition(self,a,b):
         return a+b
     def multiplication(self,a,b):
         return a*b
obj=calculator()
print(obj.addition(1,2))   
print(obj.multiplication(1,2))        
              
