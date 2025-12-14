def safe_divide(numerator, denominator):
    try:
        num1 = float(numerator)
        num2 = float(denominator)

        result = print(f"The result of the division is {num1 / num2}")
        return result

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Please enter numeric values only.")
