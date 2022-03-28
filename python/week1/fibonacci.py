def fib_while(n):
  fib_prev = 1
  print(fib_prev)
  fib = 1
  print(fib)
  counter = 2
  while counter < n:
    k = fib
    fib = fib_prev + fib
    fib_prev = k
    print(fib)
    
    counter += 1
  return


def fib_for(n):
  fib_prev = 1
  print(fib_prev)
  fib = 1
  print(fib)
  for x in range(2, n):
    k = fib
    fib = fib_prev + fib
    fib_prev = k
    print(fib)

# def fib_recur(n):
    # if n == 1 or n == 0:
    #     return 1
    # else:
    #     return n * recur_factorial(n-1)
  
  
  
def fibinput():
  fib_inp = int(input("Enter # of fibonacci terms: "))
  print("Print Using While")
  fib_while(fib_inp)
  print("Print Using For")
  fib_for(fib_inp)




if __name__ == "__main__":
  fibinput()