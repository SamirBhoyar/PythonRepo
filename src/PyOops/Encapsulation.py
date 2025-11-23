class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self.__owner = owner  # Private attribute
        self.__balance = initial_balance # Private attribute

    def get_owner(self):
        return self.__owner

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

# Usage
account = BankAccount("Alice", 1000)
print(f"Account owner: {account.get_owner()}")
print(f"Current balance: {account.get_balance()}")

account.deposit(500)
account.withdraw(200)
account.withdraw(1500) # This will fail due to insufficient funds