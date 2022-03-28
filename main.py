# menu.py - function style menu
# Imports typically listed at top
# each import enables us to use logic that has been abstracted to other files and folders
import python.week0.keypad as keypad
import python.week0.swap as swap
import python.week0.pattern as pattern
import python.week0.tree as tree
import python.week1.listandloop as listandloop
import python.week1.clear as clear
import python.week1.fibonacci as fibonacci
import python.week2.factorial as factorial
import python.week2.mathfunc as mathfunc
import python.week2.palindrome as palindrome 

# Main list of [Prompts, Actions]
# Two styles are supported to execute abstracted logic
# 1. file names will be run by exec(open("filename.py").read())
# 2. function references will be executed directly file.function()
main_menu = []


# Submenu list of [Prompt, Action]
# Works similarly to main_menu
data_menu = [
    ["Movie List and Loop", listandloop.tester],

]


adventure_sub_menu = [
    ["Pattern", pattern.patternfunc],
    ["Swap", swap.test_swapNum],
    ["Keypad", keypad.format_tester],
    ["Tree", tree.treefunc]
]

math_menu = [
    ["Fibonacci", fibonacci.fibinput],
    ["Factorial", factorial.main],
    ["Math Func", mathfunc.main],
    ["Palindrome", palindrome.tester],
]


# Menu banner is typically defined by menu owner
border = "=" * 10
banner = f"\n{border}\nPlease Select An Option\n{border}"

# def menu
# using main_menu list:
# 1. main menu and submenu reference are created [Prompts, Actions]
# 2. menu_list is sent as parameter to menuy.menu function that has logic for menu control


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

  

# def submenu
# using sub menu list above:
# sub_menu works similarly to menu()

def buildMenu(banner, options):
    # header for menu
    
    print(banner)
    # build a dictionary from options
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    # print menu or dictionary
    for key, value in prompts.items():
        print(key, '->', value[0])

    # get user choice
    choice = input("Type your choice> ")
    clear.clearConsole()

    # validate choice and run
    # execute selection
    # convert to number
    try:
        choice = int(choice)
        if choice == 0:
            # stop
            return
        try:
            # try as function
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:  # try as playground style
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
            # end function try
        # end prompts try
    except ValueError:
        # not a number error
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        # traps all other errors
        print(f"Invalid choice: {choice}")
    # end validation try

    buildMenu(banner, options)  # recursion, start menu over again


if __name__ == "__main__":
    menu()
