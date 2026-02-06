"""Test suite for Project 24: Autodiff"""
import pytest
import numpy as np
from exercise import Tensor, Add, Mul


def test_tensor_creation():
    t = Tensor(5.0, requires_grad=True)
    assert t.data == 5.0
    assert t.grad is None


def test_addition():
    a = Tensor(3.0, requires_grad=True)
    b = Tensor(2.0, requires_grad=True)
    c = a + b
    c.backward()
    assert c.data == 5.0
    assert a.grad == 1.0
    assert b.grad == 1.0


def test_multiplication():
    a = Tensor(3.0, requires_grad=True)
    b = Tensor(2.0, requires_grad=True)
    c = a * b
    c.backward()
    assert c.data == 6.0
    assert a.grad == 2.0  # d(3*2)/d3 = 2
    assert b.grad == 3.0  # d(3*2)/d2 = 3


def test_chain_rule():
    # Test: z = (x * y) + y
    x = Tensor(2.0, requires_grad=True)
    y = Tensor(3.0, requires_grad=True)
    z = (x * y) + y
    z.backward()
    # dLoss/dx = y = 3
    # dLoss/dy = x + 1 = 3
    assert abs(x.grad - 3.0) < 0.001
    assert abs(y.grad - 3.0) < 0.001




