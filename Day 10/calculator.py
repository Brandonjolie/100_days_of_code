from art import logo


def add(n1, n2):
    return n1+n2


def subtract(n1, n2):
    return n1-n2


def multiply(n1, n2):
    return n1*n2


def divide(n1, n2):
    return n1/n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(logo)

    num1 = float(input('What\'s the first number?: '))

    for symbol in operations:
        print(symbol)
    _running = True
    while _running:
        operation_symbol = input('Pick an operation: ')
        calc_func = operations[operation_symbol]
        num2 = float(input('What\'s the next number?: '))
        answer = calc_func(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        running = input(
            f'Type \'y\' to continue calculating with {answer}, or type \'n\' to exit.:').lower()
        num1 = answer
        if running == 'y':
            _running = True
        if running == 'n':
            _running = False
            calculator()


calculator()
