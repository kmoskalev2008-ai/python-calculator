def calculator(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return a / b
    else:
        return "Unknown Operation"


a = float(input("First number: "))
operation = input("Operation (+, -, *, /): ")
b = float(input("Second number: "))

result = calculator(a, b, operation)

print("Result:", result)