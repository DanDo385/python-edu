"""
Project 05: Exception Handling - Practice Stubs
"""


def safe_divide(a: float, b: float) -> float:
    """
    Safely divide two numbers with exception handling.

    Raises:
        TypeError: If inputs are not numbers
        ValueError: If b is zero
    """
    # TODO: Implement with proper exception handling
    pass


def parse_int(value: str) -> int:
    """
    Parse string to int with exception handling.

    Returns -1 if parsing fails.
    """
    # TODO: Use try/except to handle ValueError
    pass


class InsufficientFundsError(Exception):
    """Custom exception for insufficient funds."""
    pass


class BankAccount:
    """Bank account with exception handling."""

    def __init__(self, balance: float = 0):
        self.balance = balance

    def withdraw(self, amount: float):
        """
        Withdraw money from account.

        Raises:
            InsufficientFundsError: If balance < amount
            ValueError: If amount < 0
        """
        # TODO: Implement with proper exception handling
        pass


def retry_operation(func, max_attempts: int = 3):
    """
    Retry a function if it raises an exception.

    Returns: (success, result) tuple
    """
    # TODO: Implement retry logic with exception handling
    pass


if __name__ == "__main__":
    print(safe_divide(10, 2))
    print(parse_int("123"))
