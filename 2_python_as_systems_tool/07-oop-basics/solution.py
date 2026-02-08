"""
Project: Object-Oriented Programming (OOP) Basics - SOLUTION

This file contains the complete and correct implementation of the BankAccount
class, demonstrating core OOP principles like encapsulation, state, and
behavior.
"""

class BankAccount:
    """
    A class to represent a simple bank account, encapsulating its data
    (attributes) and behaviors (methods).
    """

    def __init__(self, owner_name, initial_balance=0.0):
        """
        The constructor for the BankAccount class. It sets up the object's
        initial state.

        Args:
            owner_name (str): The name of the account owner.
            initial_balance (float): The starting balance of the account.
        """
        # Attributes are variables that belong to an object.
        # `self` refers to the specific instance of the class being created.
        self.owner_name = owner_name

        # The leading underscore in `_balance` is a strong convention in Python.
        # It signals to other developers: "This attribute is for internal use;
        # please don't modify it directly." This is a key part of encapsulation.
        # It encourages using methods (like deposit/withdraw) to manage state.
        self._balance = float(initial_balance)

    def deposit(self, amount):
        """
        Adds a specified amount to the account balance, after validation.

        Args:
            amount (float): The amount to deposit. Must be a positive number.

        Returns:
            bool: True if the deposit was successful, False otherwise.
        """
        # --- Input Validation ---
        # A core responsibility of a method is to ensure that state changes
        # are valid. We protect the integrity of our object's state.
        if amount <= 0:
            print("Deposit amount must be positive.")
            return False
        
        # If validation passes, we modify the object's state.
        self._balance += amount
        print(f"Successfully deposited ${amount:.2f}.")
        return True

    def withdraw(self, amount):
        """
        Subtracts a specified amount from the account balance, after validation.

        Args:
            amount (float): The amount to withdraw. Must be a positive number.

        Returns:
            bool: True if the withdrawal was successful, False otherwise.
        """
        # --- Input and State Validation ---
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        
        if amount > self._balance:
            print("Withdrawal failed: Insufficient funds.")
            return False

        # If all checks pass, modify the state.
        self._balance -= amount
        print(f"Successfully withdrew ${amount:.2f}.")
        return True

    def get_balance(self):
        """
        A "getter" method to safely retrieve the account balance.

        This provides read-only access to the internal `_balance` attribute,
        upholding the principle of encapsulation. Users of the class don't
        need to know the internal name `_balance`; they just use `get_balance()`.
        """
        return self._balance

    def __str__(self):
        """
        The "string representation" method, a special "dunder" method.
        It provides a human-readable description of the object.

        Returns:
            str: A user-friendly string describing the account.
        """
        # Using an f-string to create a formatted, clean output.
        # The `:.2f` format specifier ensures the balance is always shown
        # with two decimal places, like currency.
        return f"Account Owner: {self.owner_name}, Balance: ${self._balance:.2f}"


# The `if __name__ == "__main__"` block allows this file to be both a
# runnable script for testing and an importable module without running
# the test code automatically.
if __name__ == "__main__":
    # 1. Create an instance of the BankAccount class.
    #    This calls the `__init__` method.
    my_account = BankAccount("John Doe", 100.0)
    
    # 2. `print(my_account)` calls the `__str__` method.
    print(my_account)

    # 3. Call the `deposit` method.
    print("\nDepositing $50.55...")
    my_account.deposit(50.55)
    
    # 4. Check the state again.
    print(my_account)

    # 5. Test validation rule in `deposit`.
    print("\nAttempting to deposit a negative amount...")
    my_account.deposit(-20)
    print(my_account)  # Balance should be unchanged.

    # 6. Call the `withdraw` method.
    print("\nWithdrawing $80...")
    my_account.withdraw(80)
    print(my_account)

    # 7. Test validation rule in `withdraw`.
    print("\nAttempting to withdraw more than the balance...")
    my_account.withdraw(100)
    print(my_account)  # Balance should be unchanged.

    # 8. Use the getter method.
    current_balance = my_account.get_balance()
    print(f"\nFinal balance retrieved via get_balance(): ${current_balance:.2f}")