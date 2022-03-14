def build_flag(height):
  i = 1
  while i <= height:
    print("x "* (height - 5)+ "* " * i)
    print((height) + "* " * i)
    #creates the spacing before each star
    i = i + 1
    

def flagfunc():
  height = int(input("Enter height: "))
  build_flag(height)