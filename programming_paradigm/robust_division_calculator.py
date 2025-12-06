def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        num2 = float(denominator)

        result = num / num2
        return result

    except ZeroDivisionError:
        print("Cannot divide by zero")
    except ValueError:
        print("Error: Please enter numeric values only.")
