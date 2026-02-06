"""
Project 05: Exception Handling - Tests
"""

import pytest
from solution import (
    safe_divide,
    parse_int,
    InsufficientFundsError,
    BankAccount,
    retry_operation
)


class TestSafeDivide:
    def test_normal_division(self):
        assert safe_divide(10, 2) == 5.0

    def test_divide_by_zero(self):
        with pytest.raises(ValueError):
            safe_divide(10, 0)

    def test_invalid_types(self):
        with pytest.raises(TypeError):
            safe_divide("10", 2)


class TestParseInt:
    def test_valid_int(self):
        assert parse_int("123") == 123

    def test_invalid_int(self):
        assert parse_int("abc") == -1


class TestBankAccount:
    def test_withdraw_success(self):
        account = BankAccount(100)
        account.withdraw(50)
        assert account.balance == 50

    def test_withdraw_insufficient_funds(self):
        account = BankAccount(100)
        with pytest.raises(InsufficientFundsError):
            account.withdraw(150)

    def test_withdraw_negative_amount(self):
        account = BankAccount(100)
        with pytest.raises(ValueError):
            account.withdraw(-10)


class TestRetry:
    def test_retry_success(self):
        counter = {'value': 0}

        def flaky_func():
            counter['value'] += 1
            if counter['value'] < 3:
                raise Exception("Temporary error")
            return "success"

        success, result = retry_operation(flaky_func, 3)
        assert success is True
        assert result == "success"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
