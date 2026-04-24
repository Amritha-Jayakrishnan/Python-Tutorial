# Simple Calculator
# Performs basic arithmetic: addition, subtraction, multiplication, division

def calculate(a, op, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            return "Error: Division by zero"
        return a / b
    else:
        return "Invalid operator"

a = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ").strip()
b = float(input("Enter second number: "))

result = calculate(a, op, b)
print(f"Result: {a} {op} {b} = {result}")
