"""
Project 06: Classes & Magic Methods - Tests
"""

import pytest
from solution import Vector, BankAccount, Stack


class TestVector:
    def test_vector_addition(self):
        v1 = Vector(1, 2)
        v2 = Vector(3, 4)
        v3 = v1 + v2
        assert v3.x == 4 and v3.y == 6

    def test_vector_subtraction(self):
        v1 = Vector(5, 7)
        v2 = Vector(2, 3)
        v3 = v1 - v2
        assert v3.x == 3 and v3.y == 4

    def test_vector_multiplication(self):
        v = Vector(2, 3)
        v2 = v * 3
        assert v2.x == 6 and v2.y == 9

    def test_vector_equality(self):
        v1 = Vector(1, 2)
        v2 = Vector(1, 2)
        v3 = Vector(2, 3)
        assert v1 == v2
        assert not (v1 == v3)

    def test_vector_str(self):
        v = Vector(1, 2)
        assert str(v) == "Vector(1, 2)"


class TestBankAccount:
    def test_bank_account_comparison(self):
        acc1 = BankAccount("Alice", 100)
        acc2 = BankAccount("Bob", 200)
        assert acc1 < acc2
        assert acc2 > acc1

    def test_bank_account_repr(self):
        acc = BankAccount("Alice", 100)
        assert repr(acc) == "BankAccount('Alice', 100)"


class TestStack:
    def test_stack_push_pop(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        assert stack.pop() == 3
        assert stack.pop() == 2

    def test_stack_len(self):
        stack = Stack()
        assert len(stack) == 0
        stack.push(1)
        stack.push(2)
        assert len(stack) == 2

    def test_stack_getitem(self):
        stack = Stack()
        stack.push(10)
        stack.push(20)
        assert stack[0] == 10
        assert stack[1] == 20


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
