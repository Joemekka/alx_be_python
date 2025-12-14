def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        num2 = float(denominator)

        result = num / num2
        return print(f"The result of the division is {result}")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Please enter numeric values only.")
