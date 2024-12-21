# Encapsulation.py with Getter and Setter Methods

class BankAccount:
    def __init__(self, account_holder, balance=0):
        """
        Constructor method that initializes the account holder's name and balance.
        The balance is private, and access to it is controlled through getter and setter methods.
        """
        self.account_holder = account_holder
        # Private attribute with double underscore (cannot be accessed directly outside the class)
        self.__balance = balance

    # Getter method to access the balance
    def get_balance(self):
        """
        This getter method allows external code to access the value of the private __balance attribute.
        It ensures controlled access to the balance.
        """
        return self.__balance

    # Setter method to update the balance
    def set_balance(self, balance):
        """
        This setter method allows external code to modify the value of the private __balance attribute.
        It can include validation or checks to ensure the new value is valid.
        """
        if balance >= 0:
            self.__balance = balance
            print(f"Balance updated to {self.__balance}.")
        else:
            print("Balance cannot be negative.")

    # Public method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance is {self.__balance}.")
        else:
            print("Deposit amount must be positive.")

    # Public method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance is {self.__balance}.")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

# Creating an object of BankAccount
account = BankAccount("Alice", 500)

# Accessing balance using the getter method
print(f"Initial Balance: {account.get_balance()}")

# Using setter method to update the balance directly
account.set_balance(1000)  # Valid update
account.set_balance(-500)  # Invalid update (balance cannot be negative)

# Making a deposit
account.deposit(200)

# Making a withdrawal
account.withdraw(100)

# Accessing the balance again using getter method
print(f"Final Balance: {account.get_balance()}")
