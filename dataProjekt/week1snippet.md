# Code Snippet


Fibonacci Sequence
```
def fib_recur(n):
  # intial 1, 1 in the fibonacci sequence
  fib_prev = 1
  print(fib_prev)
  fib = 1
  print(fib)
  counter = 2
  while counter < n:
    # storing a value to be added later to for the next fibonacci number
    k = fib
    fib = fib_prev + fib
    fib_prev = k
    print(fib)
    
    counter += 1
  return

# enter the amount of numbers to be shown in the sequence 
def fibinput():
  fib_inp = int(input("Enter fibonacci index: "))
  fib_recur(fib_inp)

if __name__ == "__main__":
  fibinput()
```
Different types of loops

```
# for loop iterates on length of InfoDb
def for_loop():
    for n in range(len(InfoDb)):
        print_data(n)

    
# while loop contains an initial n and an index incrementing statement (n += 1)
# dont need to write n = 0 because it being called in the tester
def while_loop(n):
    while n < len(InfoDb):
        print_data(n)
        n += 1
    return

# recursion simulates loop incrementing on each call (n + 1) until exit condition is met
def recursive_loop(n):
    if n < len(InfoDb):
        print_data(n)
        recursive_loop(n + 1)
    return # exit condition
```

Having a little fun with the for loop
```
# limiting the range of items to be printed
def for_loop_limit(start, end):
    for n in range(start, end+1):
        print_data(n)
```