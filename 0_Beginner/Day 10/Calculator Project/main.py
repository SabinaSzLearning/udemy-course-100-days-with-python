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
    "/": divide,
}

Num1 = int(input("Num: "))
operator = input("Operator: ")
Num2 = int(input("Num: "))



solution = operations[operator](Num1, Num2)

print(f"Solution: {solution}")