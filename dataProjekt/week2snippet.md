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

Sub menus
```py
def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["data", data_submenu])
    menu_list.append(["Math", math_submenu])
    menu_list.append(["adventure", adventure_submenu ])
    buildMenu(title, menu_list)

def data_submenu():
    title = "Function Submenu" + banner
    buildMenu(title, data_menu)

def math_submenu():
    title = "Function Submenu" + banner
    buildMenu(title, math_menu)

def adventure_submenu():
    title = "Function Submenu" + banner
    buildMenu(title, adventure_sub_menu)
```