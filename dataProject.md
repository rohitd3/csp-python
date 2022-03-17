{% include navbar.html %}

# Data Structures Project

### Replit

{% include replitembed.html %}


# Code Snippet
Menu:
```
main_menu = [
    ["American Flag", americanflag.flagfunc],
    ["Swap", swap.test_swapNum],
    ["Keypad", keypad.format_tester],
    ["Tree", tree.treefunc],
    ["Pattern", pattern.patternfunc],
]
```
Building menu choices:
```
for op in options:
        index = len(prompts)
        prompts[index] = op
```
Tree height changes and the bottom is the same lenght of the height:
```
def build_tree(height):
  i = 1
  while i <= height:
    print(" " * (height - i) + "* " * i)
    #creates the spacing before each star
    i = i + 1
  print(" " * (height - 2) + "{}{}{}")
```
