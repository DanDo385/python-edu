"""
Project 03: Functions and Modular Programming

Complete the functions below according to their docstrings.
Run pytest test.py -v to test your solutions.
"""


def greet(name):
    """
    Return a greeting message.
    
    Args:
        name (str): Person's name
    
    Returns:
        str: Greeting message "Hello, {name}!"
    """
    # TODO: Return formatted greeting
    return None


def add_numbers(a, b):
    """
    Add two numbers together.
    
    Args:
        a (int or float): First number
        b (int or float): Second number
    
    Returns:
        int or float: Sum of a and b
    """
    # TODO: Return sum of a and b
    return None


def calculate_factorial(n):
    """
    Calculate the factorial of n (n!).
    
    Factorial: n! = n × (n-1) × ... × 2 × 1
    Special case: 0! = 1
    
    Args:
        n (int): Non-negative integer
    
    Returns:
        int: Factorial of n, or None if n is negative
    """
    # TODO: Calculate factorial iteratively
    # Hint: Use a loop to multiply numbers from 1 to n
    if n < 0:
        return None
    
    result = 1
    # TODO: Complete the loop
    return result


def is_prime(n):
    """
    Check if a number is prime.
    
    A prime number is greater than 1 and has no divisors other than 1 and itself.
    
    Args:
        n (int): Number to check
    
    Returns:
        bool: True if n is prime, False otherwise
    """
    # TODO: Implement prime checking
    # Hint: Check if any number from 2 to sqrt(n) divides n
    if n < 2:
        return False
    
    # TODO: Check for divisors
    return True


def get_maximum(a, b, c):
    """
    Find the maximum of three numbers.
    
    Args:
        a (int or float): First number
        b (int or float): Second number
        c (int or float): Third number
    
    Returns:
        int or float: Maximum of the three numbers
    """
    # TODO: Find and return maximum
    # Hint: Compare numbers pairwise
    return None


def calculate_circle_area(radius):
    """
    Calculate the area of a circle.
    
    Formula: area = π × radius²
    
    Args:
        radius (float): Radius of the circle
    
    Returns:
        float: Area of the circle, or None if radius is negative
    """
    # TODO: Import math module and calculate area
    # Hint: Use math.pi for π
    import math
    
    if radius < 0:
        return None
    
    # TODO: Calculate and return area
    return None


def format_name(first_name, last_name, middle_name=None):
    """
    Format a person's full name.
    
    If middle_name is provided: "First Middle Last"
    Otherwise: "First Last"
    
    Args:
        first_name (str): First name
        last_name (str): Last name
        middle_name (str, optional): Middle name
    
    Returns:
        str: Formatted full name
    """
    # TODO: Format name based on whether middle_name is provided
    # Hint: Use if/else to check if middle_name is None
    return None


def sum_list(numbers):
    """
    Calculate the sum of all numbers in a list.
    
    Args:
        numbers (list): List of numbers
    
    Returns:
        int or float: Sum of all numbers, or 0 if list is empty
    """
    # TODO: Sum all numbers in the list
    total = 0
    return total


def count_vowels(text):
    """
    Count the number of vowels in a string.
    
    Vowels are: a, e, i, o, u (case-insensitive)
    
    Args:
        text (str): Input string
    
    Returns:
        int: Number of vowels in text
    """
    # TODO: Count vowels
    # Hint: Convert to lowercase and check each character
    vowels = "aeiou"
    count = 0
    return count


def power(base, exponent):
    """
    Calculate base raised to the power of exponent.
    
    Args:
        base (int or float): Base number
        exponent (int): Exponent (non-negative)
    
    Returns:
        int or float: base^exponent, or None if exponent is negative
    """
    # TODO: Calculate power
    # Hint: Use a loop or ** operator
    if exponent < 0:
        return None
    
    # TODO: Calculate power
    return None

