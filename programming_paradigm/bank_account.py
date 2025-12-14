class BankAccount:
    def __init__(self, balance=0):
        self.account_balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            return False
        if amount > self.account_balance:
            return False

        self.account_balance -= amount
        return True

    def display_balance(self):
        print(f"Current Balance: ${float(self.account_balance)}0")
