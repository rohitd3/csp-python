class Factorial:
  
  def __call__(self, n):
          if n == 1 or n == 0:
            return 1
          else:
            return n * self(n-1)
            
def main():
  b = int(input("Choose a number:"))
  fibo_of = Factorial() # object instantiation and run __init__ method
  print(fibo_of(b)) # object running __call__ method

if __name__ == "__main__":
  main()