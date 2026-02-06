"""
Project 08: Recursion and Divide-and-Conquer

Complete the functions below according to their docstrings.
Run pytest test.py -v to test your solutions.
"""


def factorial(n):
    """
    Calculate factorial recursively.
    
    n! = n × (n-1) × ... × 2 × 1
    Base case: 0! = 1, 1! = 1
    
    Args:
        n (int): Non-negative integer
    
    Returns:
        int: Factorial of n
    """
    # TODO: Implement recursive factorial
    # Base case: n == 0 or n == 1
    # Recursive case: n * factorial(n-1)
    return None


def fibonacci(n):
    """
    Calculate nth Fibonacci number recursively.
    
    F(0) = 0, F(1) = 1
    F(n) = F(n-1) + F(n-2) for n > 1
    
    Args:
        n (int): Non-negative integer
    
    Returns:
        int: nth Fibonacci number
    """
    # TODO: Implement recursive Fibonacci
    # Base cases: n == 0 returns 0, n == 1 returns 1
    # Recursive case: fibonacci(n-1) + fibonacci(n-2)
    return None


def gcd(a, b):
    """
    Calculate Greatest Common Divisor using Euclidean algorithm.
    
    GCD(a, b) = GCD(b, a mod b) if b != 0
    GCD(a, 0) = a
    
    Args:
        a (int): First number
        b (int): Second number
    
    Returns:
        int: GCD of a and b
    """
    # TODO: Implement recursive GCD
    # Base case: if b == 0, return a
    # Recursive case: return gcd(b, a % b)
    return None


def binary_search(arr, target, left=0, right=None):
    """
    Binary search using divide-and-conquer recursion.
    
    Precondition: arr must be sorted
    
    Args:
        arr (list): Sorted list of numbers
        target: Value to search for
        left (int): Left boundary (default 0)
        right (int): Right boundary (default len(arr)-1)
    
    Returns:
        int: Index of target, or -1 if not found
    """
    # TODO: Initialize right if None
    # TODO: Base case: if left > right, return -1
    # TODO: Calculate middle index
    # TODO: If arr[middle] == target, return middle
    # TODO: If target < arr[middle], search left half
    # TODO: Otherwise, search right half
    return None


def sum_list_recursive(numbers):
    """
    Calculate sum of list recursively.
    
    Args:
        numbers (list): List of numbers
    
    Returns:
        int or float: Sum of numbers, or 0 if empty
    """
    # TODO: Implement recursive sum
    # Base case: if list is empty, return 0
    # Recursive case: first element + sum of rest
    return None

