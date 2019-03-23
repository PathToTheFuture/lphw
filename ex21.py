def add(a, b):
    print(f"Adding: {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"Subtract {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"Mutiplying: {a} * {b}")
    return a * b

def divide(a, b):
    print(f"Dividing {a} / {b}")
    return a / b

print("Let's do some math with just functions")

age = subtract(30, 7)
height = multiply(32, 2)
hours_worked = divide(88, 8)
total = add((age + height), hours_worked)

print(f"""
Age: {age}
Height: {height}
Hour I Work: {hours_worked}
Total: {total}
""")
