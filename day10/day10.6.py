from art import logo

def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def mult(num1, num2):
    return num1 * num2


def div(num1, num2):
    return num1 / num2


def power(num1, num2):
    return num1 ** num2


operator = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div,
    "pow": power,
}


def calculator():
    print(logo)
    recalculate = True
    input_number1 = float(input("Whats the first number?: "))

    while recalculate:
        operator_input = input("Type the operator \n+\n-\n*\n/\npow\n ")
        input_number2 = float(input("Whats the second number?: "))

        for symbol in operator:
            if operator_input == symbol:
                calculation = (operator[symbol])
                result = calculation(input_number1, input_number2)
                break

        print(f"{input_number1} {operator_input} {input_number2} = {result}")
        input_number1 = result
        recalculate_again = input(f"Type 'y' to continue calculating with {result}, or type 'n' to exit.: ").lower()
        if recalculate_again == "n":
            recalculate = False
            calculator()


calculator()
