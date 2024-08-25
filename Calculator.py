#Calculator

def addition(x, y):
    return x+y
def subtraction(x, y):
    return x - y
def multiply(x, y):
    return x*y
def divide(x, y):
    return x/y

def Calculator(x,y, choice):
    if choice == "+":
        return addition(x, y)
    elif choice == "-":
        return subtraction(x, y)
    elif choice == "*":
        return multiply(x, y)
    elif choice == "/":
        return divide(x, y)
    
super_base = True
base = True
while super_base:
    print(""" 
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|

              """)
    n1 = float(input("What's the first number?: "))
    while base:
        
        print("+\n-\n*\n/")
        choice = input("Pick one operation: ")
        n2 = float(input("What's the other number?: "))
        result = Calculator(n1, n2, choice)
        print(f"{n1} {choice} {n2} = {result}")
        
        proceed = input(f'Type "y" to continue calculating with {result}, or type "n" to start new calculation: ').lower()
        
        if proceed == "y":
            n1 = result
            base = True
            super_base = False
        elif proceed == 'n':
            print(""" 
     _____________________
    |  _________________  |
    | | JO           0. | |
    | |_________________| |
    |  ___ ___ ___   ___  |
    | | 7 | 8 | 9 | | + | |
    | |___|___|___| |___| |
    | | 4 | 5 | 6 | | - | |
    | |___|___|___| |___| |
    | | 1 | 2 | 3 | | x | |
    | |___|___|___| |___| |
    | | . | 0 | = | | / | |
    | |___|___|___| |___| |
    |_____________________|

                  """)
            n1 = float(input("What's the first number?: "))
            
            base = True
            super_base = False
           
        
    
    
        