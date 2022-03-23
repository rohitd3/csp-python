def fib_recur(n):
  fib_prev = 0
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


def fibinput():
  fib_inp = int(input("Enter # of fibonacci terms: "))
  fib_recur(fib_inp)

if __name__ == "__main__":
  fibinput()