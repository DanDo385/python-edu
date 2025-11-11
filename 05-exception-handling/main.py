"""
Project 05: Exception Handling - Demo
"""

from solution import safe_divide, parse_int, BankAccount, InsufficientFundsError, retry_operation


def demo_basic():
    print("=" * 70)
    print("DEMO 1: Basic Exception Handling")
    print("=" * 70)

    try:
        result = safe_divide(10, 0)
    except ValueError as e:
        print(f"Caught ValueError: {e}")

    print()


def demo_custom():
    print("=" * 70)
    print("DEMO 2: Custom Exceptions")
    print("=" * 70)

    account = BankAccount(100)
    print(f"Balance: ${account.balance}")

    try:
        account.withdraw(150)
    except InsufficientFundsError as e:
        print(f"Transaction failed: {e}")

    print()


def demo_retry():
    print("=" * 70)
    print("DEMO 3: Retry Logic")
    print("=" * 70)

    attempts = {'count': 0}

    def flaky_operation():
        attempts['count'] += 1
        print(f"  Attempt {attempts['count']}")
        if attempts['count'] < 3:
            raise Exception("Temporary failure")
        return "Success!"

    success, result = retry_operation(flaky_operation, 3)
    print(f"Result: {result}\n")


def main():
    print("\n🚨" * 35)
    print("  PROJECT 05: EXCEPTION HANDLING")
    print("🚨" * 35)
    print()

    demo_basic()
    demo_custom()
    demo_retry()

    print("=" * 70)
    print("Key Takeaways:")
    print("1. Use specific exception types")
    print("2. Create custom exceptions for domain logic")
    print("3. Always clean up in finally blocks")
    print("4. Don't catch exceptions you can't handle")
    print()


if __name__ == "__main__":
    main()
