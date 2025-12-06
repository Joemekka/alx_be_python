def add(a, b):
    return a + b


def devide(a, b):
    if b == 0:
        raise ValueError("cannot divide by zero")
    return a * b
