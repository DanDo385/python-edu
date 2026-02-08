"""
Project: Object-Oriented Programming (OOP) Basics

This project introduces the basics of OOP in Python. You will create a class
to model a real-world concept, encapsulating its data (attributes) and
behaviors (methods).
"""

class BankAccount:
    """
    A class to represent a simple bank account.
    """

    def __init__(self, owner_name, initial_balance=0.0):
        """
        The constructor for the BankAccount class.
        This method is called automatically when a new object is created.

        Args:
            owner_name (str): The name of the account owner.
            initial_balance (float): The starting balance of the account.
        
        Attributes:
            owner_name (str): Stores the owner's name.
            balance (float): Stores the current account balance. Should not be
                             directly accessed from outside the class.
        """
        # TODO: Initialize the `owner_name` and `balance` attributes.
        # For the balance, it's a common convention to use a single
        # leading underscore (e.g., self._balance) to indicate that it is
        # intended for internal use.
        pass

    def deposit(self, amount):
        """
        Adds a specified amount to the account balance.

        Args:
            amount (float): The amount to deposit. Must be a positive number.

        Returns:
            bool: True if the deposit was successful, False otherwise.
        """
        # TODO: Implement the deposit logic.
        # 1. Validate that the amount is positive. If not, do nothing and
        #    return False.
        # 2. If the amount is valid, add it to the balance and return True.
        pass

    def withdraw(self, amount):
        """
        Subtracts a specified amount from the account balance.

        Args:
            amount (float): The amount to withdraw. Must be a positive number.

        Returns:
            bool: True if the withdrawal was successful, False otherwise.
        """
        # TODO: Implement the withdrawal logic.
        # 1. Validate that the amount is positive.
        # 2. Validate that the account has sufficient funds.
        # 3. If the withdrawal is valid, subtract the amount from the balance.
        # 4. Return True for a successful withdrawal, False otherwise.
        pass

    def get_balance(self):
        """
        A "getter" method to safely retrieve the account balance.
        """
        # TODO: Return the current balance.
        pass

    def __str__(self):
        """
        The "string representation" method.
        This is called when you use `print()` or `str()` on an object.

        Returns:
            str: A user-friendly string describing the account.
        
        Example:
            "Account Owner: John Doe, Balance: $100.00"
        """
        # TODO: Implement the string representation.
        # Use an f-string to format the owner's name and balance.
        # The balance should be formatted to two decimal places.
        pass


# Example Usage (you can uncomment this to test your implementation)
# if __name__ == "__main__":
#     # Create a new account
#     my_account = BankAccount("John Doe", 100.0)
#     print(my_account)  # Expected: Account Owner: John Doe, Balance: $100.00

#     # Test deposit
#     print("\nDepositing $50.55...")
#     my_account.deposit(50.55)
#     print(my_account)  # Expected: Balance: $150.55

#     print("\nAttempting to deposit a negative amount...")
#     my_account.deposit(-20)
#     print(my_account)  # Expected: Balance should remain $150.55

#     # Test withdrawal
#     print("\nWithdrawing $80...")
#     my_account.withdraw(80)
#     print(my_account)  # Expected: Balance: $70.55

#     print("\nAttempting to withdraw more than the balance...")
#     my_account.withdraw(100)
#     print(my_account)  # Expected: Balance should remain $70.55