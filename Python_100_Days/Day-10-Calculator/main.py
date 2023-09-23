from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def divide(n1, n2):
    return n1 / n2

def multiply(n1, n2):
    return n1 * n2

def calculate(n1, n2, symbol):
    ans = operations[symbol](n1, n2)
    return ans

operations = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply
}



def calculator():
    print(logo)
    continue_calculation = True
    num1 = float(input("What's the first number : "))

    while continue_calculation:
        for operation in operations.keys():
            print(operation)
        operation_input = input("Which operation to perform : ")
        num2 = float(input("What's the next number : "))
        result = calculate(num1, num2, operation_input)
        print(f'{num1} {operation_input} {num2} = {result}')

        restart = input(f"Type 'y' to continue calculating with {result}, Type 'c' to restart, Type 'n' to exit : ")
        if restart == 'y':
            num1 = result
        elif restart == 'c':
            continue_calculation = False
            calculator()
        else:
            continue_calculation = False
            print('Goodbye')

calculator()