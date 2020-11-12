#Calculator
# Step-1: Create functions for each operation that the calculator does
# Step-2: Create a dictionary called 'operations' that stores all the operation functions
# Step-3: Create two variables, num1 and num2, that store the result of asking the user to input two numbers
# Step-4: Loop through the operations dictionary and print out each symbol
# Step-5: Create a variable called 'operation_symbol' that stores the input of asking the user to 'Pick an operation from the line above: '

#*****************
from replit import clear 
from art import logo


#Add
def add(n1, n2):
    return n1 + n2

#Substract
def substract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : substract,
    "*" : multiply,
    "/" : divide
}

def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' a new calculation: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()


    

