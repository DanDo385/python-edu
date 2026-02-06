"""Test suite for Project 19: Gradient Descent"""
import pytest
import numpy as np
from exercise import (
    compute_gradient_numerical,
    gradient_descent_1d,
    gradient_descent_with_history,
    find_minimum_quadratic,
    check_convergence,
)


def test_compute_gradient_numerical():
    def f(x):
        return x**2
    
    grad = compute_gradient_numerical(f, 2.0)
    # f'(x) = 2x, so f'(2) = 4
    assert abs(grad - 4.0) < 0.01


def test_gradient_descent_1d():
    def f(x):
        return (x - 3)**2 + 4
    
    def df(x):
        return 2 * (x - 3)
    
    result = gradient_descent_1d(f, df, 0.0, learning_rate=0.1, epochs=100)
    # Minimum is at x = 3
    assert abs(result - 3.0) < 0.1


def test_gradient_descent_with_history():
    def f(x):
        return x**2
    
    def df(x):
        return 2 * x
    
    final_x, history = gradient_descent_with_history(f, df, 5.0, learning_rate=0.1, epochs=10)
    assert len(history) == 10
    assert history[0][0] == 5.0  # Starting point


def test_find_minimum_quadratic():
    # f(x) = x² - 4x + 3 = (x-2)² - 1
    # Minimum at x = 2
    result = find_minimum_quadratic(1, -4, 3, 0.0, learning_rate=0.1, epochs=100)
    assert abs(result - 2.0) < 0.1


def test_check_convergence():
    assert check_convergence(0.0001, tolerance=1e-3) == True
    assert check_convergence(0.01, tolerance=1e-3) == False
    assert check_convergence(-0.0001, tolerance=1e-3) == True




