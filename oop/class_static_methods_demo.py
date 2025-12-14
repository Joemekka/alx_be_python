class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static method: does not depend on class or instance data.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class method: accesses class-level data using cls.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
