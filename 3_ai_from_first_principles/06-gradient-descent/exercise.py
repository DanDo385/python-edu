"""
Project 19: Gradient Descent Basics

Complete the functions below according to their docstrings.
Run pytest test.py -v to test your solutions.
"""

import numpy as np


def compute_gradient_numerical(f, x, h=1e-5):
    """
    Compute gradient of function f at point x using numerical differentiation.
    
    Numerical gradient uses finite differences:
    f'(x) ≈ (f(x+h) - f(x-h)) / (2*h)
    
    Args:
        f (callable): Function to differentiate
        x (float): Point at which to compute gradient
        h (float): Small step size for numerical differentiation
    
    Returns:
        float: Numerical approximation of gradient
    """
    # TODO: Compute gradient using finite differences
    # Formula: (f(x+h) - f(x-h)) / (2*h)
    return None


def gradient_descent_1d(f, df, initial_x, learning_rate=0.1, epochs=100):
    """
    Perform gradient descent to minimize 1D function f.
    
    Algorithm:
    1. Start at initial_x
    2. For each epoch:
       a. Compute gradient: grad = df(x)
       b. Update: x = x - learning_rate * grad
    3. Return final x
    
    Args:
        f (callable): Function to minimize
        df (callable): Derivative of f (gradient function)
        initial_x (float): Starting point
        learning_rate (float): Step size (default 0.1)
        epochs (int): Number of iterations (default 100)
    
    Returns:
        float: Approximate minimum point
    """
    # TODO: Implement gradient descent
    # Initialize x = initial_x
    # Loop for epochs:
    #   Compute gradient = df(x)
    #   Update x = x - learning_rate * gradient
    # Return final x
    x = initial_x
    return x


def gradient_descent_with_history(f, df, initial_x, learning_rate=0.1, epochs=100):
    """
    Perform gradient descent and return history of x values.
    
    Useful for visualizing the optimization path.
    
    Args:
        f (callable): Function to minimize
        df (callable): Derivative of f
        initial_x (float): Starting point
        learning_rate (float): Step size
        epochs (int): Number of iterations
    
    Returns:
        tuple: (final_x, history) where history is list of (x, f(x)) pairs
    """
    # TODO: Implement gradient descent with history tracking
    # Track x and f(x) at each step
    x = initial_x
    history = []
    return x, history


def find_minimum_quadratic(a, b, c, initial_x, learning_rate=0.1, epochs=100):
    """
    Find minimum of quadratic function f(x) = ax² + bx + c using gradient descent.
    
    Analytical minimum is at x = -b/(2a), but we'll find it with gradient descent.
    
    Args:
        a (float): Coefficient of x² (must be > 0 for minimum to exist)
        b (float): Coefficient of x
        c (float): Constant term
        initial_x (float): Starting point
        learning_rate (float): Step size
        epochs (int): Number of iterations
    
    Returns:
        float: Approximate minimum point
    """
    # TODO: Define quadratic function and its derivative
    # f(x) = a*x² + b*x + c
    # f'(x) = 2*a*x + b
    # Use gradient_descent_1d to find minimum
    return None


def check_convergence(gradient, tolerance=1e-6):
    """
    Check if gradient descent has converged.
    
    Convergence: gradient is close to zero (we're at a minimum).
    
    Args:
        gradient (float): Current gradient value
        tolerance (float): Convergence threshold
    
    Returns:
        bool: True if converged (|gradient| < tolerance)
    """
    # TODO: Check if absolute value of gradient is less than tolerance
    return None




