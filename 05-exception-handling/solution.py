"""
PROJECT 05: EXCEPTION HANDLING

Exception handling is critical for writing robust Python programs.
"""


def safe_divide(a: float, b: float) -> float:
    """Safely divide with exception handling."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Arguments must be numbers")

    if b == 0:
        raise ValueError("Cannot divide by zero")

    return a / b


def parse_int(value: str) -> int:
    """Parse string to int, return -1 on failure."""
    try:
        return int(value)
    except ValueError:
        return -1


class InsufficientFundsError(Exception):
    """Custom exception for banking operations."""
    pass


class BankAccount:
    """Bank account with exception handling."""

    def __init__(self, balance: float = 0):
        self.balance = balance

    def withdraw(self, amount: float):
        """Withdraw money with validation."""
        if amount < 0:
            raise ValueError("Amount cannot be negative")

        if amount > self.balance:
            raise InsufficientFundsError(
                f"Insufficient funds: balance={self.balance}, requested={amount}"
            )

        self.balance -= amount


def retry_operation(func, max_attempts: int = 3):
    """Retry function with exception handling."""
    for attempt in range(max_attempts):
        try:
            result = func()
            return (True, result)
        except Exception as e:
            if attempt == max_attempts - 1:
                return (False, str(e))
    return (False, "Max attempts reached")


# EXCEPTION HIERARCHY:
# BaseException
#  ├─ SystemExit
#  ├─ KeyboardInterrupt
#  └─ Exception
#      ├─ ValueError
#      ├─ TypeError
#      ├─ AttributeError
#      └─ ... (many more)
