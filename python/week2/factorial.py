# class factorial():
  
#   def __call__(self, n):
#           if n == 1 or n == 0:
#             return 1
#           else:
#             return n * self(n-1)

# fac_inp = int(input("Enter #: "))
# fact = factorial() # object instantiation and run __init__ method
# print(fact(fac_inp)) # object running __call__ method

# if __name__ == "__main__":
#   fac_inp()

class Factorial:
    def __init__(self):
        self.factor = [0, 1]
    def __call__(self, n):
        num = 1
        
        for i in range(1,n+1):
        	num = num * i

        return num
      
def main():
  b = int(input("Choose a number:"))
  fibo_of = Factorial() # object instantiation and run __init__ method
  print(fibo_of(b)) # object running __call__ method

if __name__ == "__main__":
  main()