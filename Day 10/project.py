def clear():
    from subprocess import call
    import os

    from art import logo

    _ = call('clear' if os.name =='posix' else 'cls')
    print(logo)

def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 != 0:
        return n1 / n2
    return None

operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}

def calculator():
    clear()

    num1 = float(input("What's the first number? "))
    for operation in operations:
        print(operation)
    more_ops = True
    while more_ops:
        op = input("Which operation would you like to perform? ")
        num2 = float(input("What's the next number? "))

        operation = operations[op]
        result = operation(num1, num2)

        print(f"{num1} {op} {num2} = {result}")

        if input(f"Do you want to perform another operation with {result}? Type 'y' or 'n' to start again: ") == 'y':
            num1 = result
        else:
            more_ops = False
            calculator()


calculator()