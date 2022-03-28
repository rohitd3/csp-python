class factorial():
  
 
  def __call__(self, n):
          if n == 1 or n == 0:
            return 1
          else:
            return n * self(n-1)


fac_inp = int(input("Enter #: "))
  
fact = factorial() # object instantiation and run __init__ method
print(fact(fac_inp)) # object running __call__ method