def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        num2 = float(denominator)

        result = num / num2
        print(f"The result of the division is 6.0")
        return result

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Please enter numeric values only.")
