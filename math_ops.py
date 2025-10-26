# 7. 🔢 Create a module named math_ops.py with add, subtract, multiply, divide — and import it in another file.

def add(a, b):
    # total = 0
    # for sublist in vars:
    #     for num in sublist:
    #         total += num
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return (a * b)

def divide(a, b):
    if b != 0:
        return int(a/b)
