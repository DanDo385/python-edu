"""
Project 19: Gradient Descent Basics - SOLUTION

Complete solution with detailed comments explaining optimization,
gradients, and how gradient descent powers machine learning.
"""

import numpy as np


def compute_gradient_numerical(f, x, h=1e-5):
    """
    Compute gradient of function f at point x using numerical differentiation.
    
    When we don't have an analytical derivative, we can approximate it
    using finite differences. This is useful for:
    - Testing analytical gradients (gradient checking)
    - Functions where derivatives are hard to compute
    - Debugging gradient computations
    
    The central difference formula is more accurate than forward difference:
    f'(x) ≈ (f(x+h) - f(x-h)) / (2*h)
    
    This uses Taylor expansion:
    f(x+h) = f(x) + h*f'(x) + O(h²)
    f(x-h) = f(x) - h*f'(x) + O(h²)
    Subtracting: f(x+h) - f(x-h) = 2h*f'(x) + O(h³)
    So: f'(x) ≈ (f(x+h) - f(x-h)) / (2h)
    
    Args:
        f (callable): Function to differentiate
        x (float): Point at which to compute gradient
        h (float): Small step size (default 1e-5)
                  Too small: numerical errors
                  Too large: approximation errors
    
    Returns:
        float: Numerical approximation of gradient
    
    Example:
        def f(x): return x**2
        compute_gradient_numerical(f, 2.0)  # Should be ≈ 4.0 (2*2)
    """
    # Central difference formula
    # Evaluate function at x+h and x-h
    # Difference divided by 2h gives gradient approximation
    gradient = (f(x + h) - f(x - h)) / (2 * h)
    
    return gradient
    
    # Note: For multi-dimensional functions, compute gradient for each dimension
    # This is how numerical gradient checking works in neural networks


def gradient_descent_1d(f, df, initial_x, learning_rate=0.1, epochs=100):
    """
    Perform gradient descent to minimize 1D function f.
    
    Gradient descent is the optimization algorithm that powers all machine learning.
    The idea is simple but powerful:
    1. Start at a random point
    2. Compute gradient (direction of steepest increase)
    3. Move opposite to gradient (toward minimum)
    4. Repeat until converged
    
    Why it works:
    - Gradient points in direction of steepest ascent
    - Moving opposite (downhill) decreases function value
    - With small steps (learning rate), we converge to minimum
    
    Algorithm:
    x = initial_x
    for epoch in range(epochs):
        grad = df(x)              # Compute gradient
        x = x - learning_rate * grad  # Move opposite to gradient
    
    Time complexity: O(epochs) - linear in number of iterations
    Space complexity: O(1) - only stores current x
    
    Args:
        f (callable): Function to minimize (not used in algorithm, but useful for monitoring)
        df (callable): Derivative of f (gradient function)
        initial_x (float): Starting point
        learning_rate (float): Step size (how far to move each iteration)
        epochs (int): Number of iterations
    
    Returns:
        float: Approximate minimum point
    
    Example:
        def f(x): return (x-3)**2 + 4
        def df(x): return 2*(x-3)
        gradient_descent_1d(f, df, 0.0)  # Should converge to x ≈ 3
    """
    # Initialize: start at given point
    x = initial_x
    
    # Iterate for specified number of epochs
    # Each epoch is one step toward the minimum
    for epoch in range(epochs):
        # Compute gradient at current point
        # Gradient tells us which direction increases the function
        # Positive gradient = function increases going right
        # Negative gradient = function decreases going right
        grad = df(x)
        
        # Update: move opposite to gradient
        # If gradient is positive (uphill to the right), move left (subtract)
        # If gradient is negative (downhill to the right), move right (add)
        # learning_rate controls step size
        x = x - learning_rate * grad
        
        # Note: In practice, you'd also check for convergence here
        # (e.g., if |grad| < tolerance, break early)
    
    return x
    
    # This is exactly how neural networks learn!
    # Instead of minimizing f(x), they minimize loss(weights)
    # Gradient descent updates weights to reduce loss


def gradient_descent_with_history(f, df, initial_x, learning_rate=0.1, epochs=100):
    """
    Perform gradient descent and return history of x values.
    
    This version tracks the optimization path, which is useful for:
    - Visualizing how gradient descent converges
    - Debugging optimization issues
    - Understanding learning rate effects
    - Creating plots showing the descent path
    
    Args:
        f (callable): Function to minimize
        df (callable): Derivative of f
        initial_x (float): Starting point
        learning_rate (float): Step size
        epochs (int): Number of iterations
    
    Returns:
        tuple: (final_x, history)
               final_x: Final x value
               history: List of (x, f(x)) tuples for each epoch
    
    Example:
        def f(x): return x**2
        def df(x): return 2*x
        x, history = gradient_descent_with_history(f, df, 5.0)
        # history contains [(5.0, 25.0), (4.0, 16.0), ...]
    """
    x = initial_x
    history = []
    
    for epoch in range(epochs):
        # Record current position and function value
        # This lets us visualize the optimization path later
        history.append((x, f(x)))
        
        # Compute gradient and update (same as before)
        grad = df(x)
        x = x - learning_rate * grad
    
    # Record final position
    history.append((x, f(x)))
    
    return x, history


def find_minimum_quadratic(a, b, c, initial_x, learning_rate=0.1, epochs=100):
    """
    Find minimum of quadratic function f(x) = ax² + bx + c using gradient descent.
    
    Quadratic functions are important because:
    - They're simple but demonstrate gradient descent well
    - Many loss functions are approximately quadratic near minimum
    - They have analytical solution: x = -b/(2a) (when a > 0)
    
    We'll use gradient descent to find the minimum, even though we know
    the analytical solution. This demonstrates the algorithm.
    
    Derivative: f'(x) = 2ax + b
    Setting to zero: 2ax + b = 0 → x = -b/(2a)
    
    Args:
        a (float): Coefficient of x² (must be > 0 for minimum to exist)
        b (float): Coefficient of x
        c (float): Constant term
        initial_x (float): Starting point
        learning_rate (float): Step size
        epochs (int): Number of iterations
    
    Returns:
        float: Approximate minimum point
    
    Example:
        # f(x) = x² - 4x + 3 = (x-2)² - 1
        # Minimum at x = 2
        find_minimum_quadratic(1, -4, 3, 0.0)  # Should converge to x ≈ 2
    """
    # Define the quadratic function
    def quadratic(x):
        return a * x**2 + b * x + c
    
    # Define the derivative (gradient)
    # f(x) = ax² + bx + c
    # f'(x) = 2ax + b
    def quadratic_derivative(x):
        return 2 * a * x + b
    
    # Use gradient descent to find minimum
    # Analytical solution is x = -b/(2a), but we'll find it iteratively
    minimum = gradient_descent_1d(quadratic, quadratic_derivative, initial_x, learning_rate, epochs)
    
    return minimum


def check_convergence(gradient, tolerance=1e-6):
    """
    Check if gradient descent has converged.
    
    Convergence means we've reached a minimum (or maximum). At a minimum:
    - Gradient is zero (flat point)
    - Function can't decrease further by moving
    
    In practice, we check if gradient is close to zero (within tolerance).
    This accounts for numerical precision issues.
    
    Args:
        gradient (float): Current gradient value
        tolerance (float): Convergence threshold
                          If |gradient| < tolerance, we consider it converged
    
    Returns:
        bool: True if converged (|gradient| < tolerance), False otherwise
    
    Example:
        check_convergence(0.0001, tolerance=1e-3)  # True (converged)
        check_convergence(0.01, tolerance=1e-3)     # False (not converged)
    """
    # Check if absolute value of gradient is less than tolerance
    # We use absolute value because gradient can be positive or negative
    # At minimum, gradient should be zero (or very close to zero)
    return abs(gradient) < tolerance
    
    # In practice, you might also check:
    # - Change in x is small: |x_new - x_old| < tolerance
    # - Change in function value is small: |f_new - f_old| < tolerance
    # - Maximum iterations reached




