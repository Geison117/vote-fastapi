def add(num1: int, num2: int):
    return num1 + num2

class InsufficientFundsError(Exception):
    pass

class BankAccount:
    def __init__(self, starting_balance: float= 0):
        self.balance = starting_balance

    def deposit(self, amount: float):
        self.balance += amount

    def withdraw(self, amount: float):
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds")
        self.balance -= amount    
    
    def collect_interest(self):
        self.balance *= 1.1