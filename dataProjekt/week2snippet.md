{% include navbar.html %}

# Code Snippet Week 2

Factorial class

```py
class Factorial:
    def __init__(self):
        self.factor = [0, 1]
    def __call__(self, n):
        num = 1
        
        for i in range(1,n+1):
        	num = num * i

        return num
```

Math Func (GCD) class

```py
class GCD:
  def __init__(self):
        self.factor = [0, 1]
  def __call__(self, num1, num2):
      if num1 == 0:
          return num1
      while num2 != 0:
          if num1 > num2:
              num1 = num1 - num2
          else:
              num2 = num2 - num1
      return num1
```