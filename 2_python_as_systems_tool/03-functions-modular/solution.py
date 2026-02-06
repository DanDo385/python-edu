"""
Project 03: Functions and Modular Programming - SOLUTION

This file contains the complete solution with detailed comments explaining
each step of the implementation.
"""


def greet(name):
    """
    Return a greeting message.
    
    This demonstrates a simple function with one parameter and a return value.
    The function takes input, processes it, and returns a formatted string.
    
    Args:
        name (str): Person's name
    
    Returns:
        str: Greeting message "Hello, {name}!"
    """
    # Use f-string to format the greeting
    # This is cleaner than concatenation: "Hello, " + name + "!"
    return f"Hello, {name}!"


def add_numbers(a, b):
    """
    Add two numbers together.
    
    Simple function demonstrating basic arithmetic and return.
    
    Args:
        a (int or float): First number
        b (int or float): Second number
    
    Returns:
        int or float: Sum of a and b
    """
    # Simply return the sum
    # Python handles type promotion automatically (int + float = float)
    return a + b


def calculate_factorial(n):
    """
    Calculate the factorial of n (n!).
    
    Factorial is the product of all positive integers up to n.
    This uses an iterative approach (loop-based).
    
    Args:
        n (int): Non-negative integer
    
    Returns:
        int: Factorial of n, or None if n is negative
    """
    # Handle invalid input
    if n < 0:
        return None
    
    # Base case: 0! = 1 (by mathematical definition)
    if n == 0:
        return 1
    
    # Initialize result to 1 (multiplicative identity)
    result = 1
    
    # Multiply by each number from 1 to n
    # range(1, n+1) gives us: 1, 2, 3, ..., n
    for i in range(1, n + 1):
        result *= i  # Equivalent to: result = result * i
    
    return result
    
    # Example trace for n=5:
    # i=1: result = 1 * 1 = 1
    # i=2: result = 1 * 2 = 2
    # i=3: result = 2 * 3 = 6
    # i=4: result = 6 * 4 = 24
    # i=5: result = 24 * 5 = 120
    # Return 120


def is_prime(n):
    """
    Check if a number is prime.
    
    A prime number is greater than 1 and has no divisors other than 1 and itself.
    We check for divisors from 2 to sqrt(n) for efficiency.
    
    Args:
        n (int): Number to check
    
    Returns:
        bool: True if n is prime, False otherwise
    """
    # Numbers less than 2 are not prime
    if n < 2:
        return False
    
    # Check for divisors from 2 to sqrt(n)
    # We only need to check up to sqrt(n) because if n has a divisor
    # greater than sqrt(n), it must also have one less than sqrt(n)
    # Example: 16 = 4 * 4, so checking up to 4 is sufficient
    
    # int(n ** 0.5) + 1 ensures we check up to sqrt(n)
    # +1 because range is exclusive on the right
    for i in range(2, int(n ** 0.5) + 1):
        # If n is divisible by i (no remainder), it's not prime
        if n % i == 0:
            return False
    
    # If we get here, no divisors were found, so n is prime
    return True


def get_maximum(a, b, c):
    """
    Find the maximum of three numbers.
    
    Compares numbers pairwise to find the largest.
    
    Args:
        a (int or float): First number
        b (int or float): Second number
        c (int or float): Third number
    
    Returns:
        int or float: Maximum of the three numbers
    """
    # Compare a and b first, then compare result with c
    # This is clearer than nested if statements
    
    # Find max of a and b
    max_ab = a if a > b else b
    
    # Compare with c
    return max_ab if max_ab > c else c
    
    # Alternative approach using built-in max():
    # return max(a, b, c)
    # But we're learning to write our own logic!


def calculate_circle_area(radius):
    """
    Calculate the area of a circle.
    
    Demonstrates importing and using a module (math).
    Formula: area = π × radius²
    
    Args:
        radius (float): Radius of the circle
    
    Returns:
        float: Area of the circle, or None if radius is negative
    """
    # Import math module to access mathematical constants and functions
    # We could import at top of file, but importing here shows it's possible
    import math
    
    # Validate input: radius cannot be negative
    if radius < 0:
        return None
    
    # Calculate area using formula: π × r²
    # math.pi gives us the value of π (approximately 3.14159...)
    # radius ** 2 squares the radius
    area = math.pi * (radius ** 2)
    
    return area


def format_name(first_name, last_name, middle_name=None):
    """
    Format a person's full name.
    
    Demonstrates optional parameters with default values.
    None is used to indicate "not provided".
    
    Args:
        first_name (str): First name
        last_name (str): Last name
        middle_name (str, optional): Middle name
    
    Returns:
        str: Formatted full name
    """
    # Check if middle_name was provided (not None)
    # None is the default value, so if it's still None, it wasn't provided
    if middle_name is not None:
        # Include middle name: "First Middle Last"
        return f"{first_name} {middle_name} {last_name}"
    else:
        # No middle name: "First Last"
        return f"{first_name} {last_name}"


def sum_list(numbers):
    """
    Calculate the sum of all numbers in a list.
    
    Demonstrates iterating over a collection and accumulating values.
    Uses the accumulator pattern.
    
    Args:
        numbers (list): List of numbers
    
    Returns:
        int or float: Sum of all numbers, or 0 if list is empty
    """
    # Initialize accumulator to 0 (additive identity)
    total = 0
    
    # Iterate through each number in the list
    for number in numbers:
        # Add current number to running total
        total += number
    
    return total
    
    # Note: Python has built-in sum() function: sum(numbers)
    # But we're learning to implement it ourselves!


def count_vowels(text):
    """
    Count the number of vowels in a string.
    
    Demonstrates string iteration and membership testing.
    Vowels: a, e, i, o, u (case-insensitive).
    
    Args:
        text (str): Input string
    
    Returns:
        int: Number of vowels in text
    """
    # Define vowels as a string
    # We'll check if each character is in this string
    vowels = "aeiou"
    
    # Initialize counter
    count = 0
    
    # Iterate through each character in the text
    for char in text:
        # Convert to lowercase for case-insensitive comparison
        # This ensures 'A' and 'a' are both counted
        char_lower = char.lower()
        
        # Check if character is a vowel
        # The 'in' operator checks membership in a string
        if char_lower in vowels:
            count += 1
    
    return count


def power(base, exponent):
    """
    Calculate base raised to the power of exponent.
    
    Can be implemented using ** operator or with a loop.
    We'll use a loop to demonstrate iteration.
    
    Args:
        base (int or float): Base number
        exponent (int): Exponent (non-negative)
    
    Returns:
        int or float: base^exponent, or None if exponent is negative
    """
    # Validate input
    if exponent < 0:
        return None
    
    # Base case: any number to the power of 0 is 1
    if exponent == 0:
        return 1
    
    # Initialize result to base (we'll multiply exponent times)
    result = base
    
    # Multiply result by base (exponent - 1) more times
    # We already have one factor (initial result = base)
    # So we need exponent - 1 more multiplications
    for _ in range(exponent - 1):
        result *= base
    
    return result
    
    # Example trace for base=2, exponent=3:
    # result = 2 (initial)
    # _=0: result = 2 * 2 = 4
    # _=1: result = 4 * 2 = 8
    # Return 8
    
    # Note: Python's ** operator does this: base ** exponent
    # But we're learning to implement it ourselves!

