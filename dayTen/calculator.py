from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

print(logo)

def calculator():
    num1 = input("What's the first number?: ")

    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue:

        operation_symbol = input("Pick an operation: ")
        num2 = input("What's the next number?: ")
        if num1 == "" or num2 == "":
            print("You need to enter a number.")
            calculator()
        calculation_function = operations[operation_symbol]
        answer = calculation_function(float(num1), float(num2))

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input("Type 'y' to continue calculating with {answer} or type 'n' to star a new calculation:" ) == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()
calculator()