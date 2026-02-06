"""
Project 02: Control Flow and Loops

Complete the functions below according to their docstrings.
Run pytest test.py -v to test your solutions.
"""


def is_even(number):
    """
    Check if a number is even.
    
    Args:
        number (int): The number to check
    
    Returns:
        bool: True if number is even, False otherwise
    """
    # TODO: Check if number is even using modulo operator
    return None


def get_grade(score):
    """
    Determine the letter grade based on a numerical score.
    
    Grading scale:
    - 90-100: 'A'
    - 80-89:  'B'
    - 70-79:  'C'
    - 60-69:  'D'
    - Below 60: 'F'
    
    Args:
        score (int): The numerical score (0-100)
    
    Returns:
        str: The letter grade
    """
    # TODO: Use if/elif/else to determine grade
    return None


def fizzbuzz(n):
    """
    Generate FizzBuzz sequence up to n.
    
    For each number from 1 to n:
    - If divisible by both 3 and 5: "FizzBuzz"
    - Else if divisible by 3: "Fizz"
    - Else if divisible by 5: "Buzz"
    - Otherwise: the number itself
    
    Args:
        n (int): Upper limit (inclusive)
    
    Returns:
        list: List of strings representing the FizzBuzz sequence
    """
    # TODO: Implement FizzBuzz logic
    result = []
    # Hint: Use a for loop and if/elif/else statements
    return result


def sum_numbers(n):
    """
    Calculate the sum of all numbers from 1 to n (inclusive).
    
    Args:
        n (int): Upper limit
    
Returns:
        int: Sum of numbers from 1 to n
    """
    # TODO: Use a for loop to sum numbers from 1 to n
    total = 0
    return total


def sum_even_numbers(n):
    """
    Calculate the sum of all even numbers from 1 to n (inclusive).
    
    Args:
        n (int): Upper limit
    
    Returns:
        int: Sum of even numbers from 1 to n
    """
    # TODO: Sum only even numbers
    total = 0
    return total


def find_first_even(numbers):
    """
    Find the first even number in a list.
    
    Args:
        numbers (list): List of integers
    
    Returns:
        int or None: First even number, or None if no even numbers exist
    """
    # TODO: Loop through numbers and return first even number
    # Hint: Use a for loop and return early when found
    return None


def count_occurrences(numbers, target):
    """
    Count how many times target appears in numbers.
    
    Args:
        numbers (list): List of integers
        target (int): Number to count
    
    Returns:
        int: Number of occurrences of target
    """
    # TODO: Count occurrences using a loop
    count = 0
    return count


def print_multiplication_table(n):
    """
    Print a multiplication table up to n x n.
    
    For example, if n=3, print:
    1 2 3
    2 4 6
    3 6 9
    
    Args:
        n (int): Size of multiplication table
    
    Returns:
        list: List of lists representing the multiplication table
             Each inner list is a row
    """
    # TODO: Create multiplication table using nested loops
    table = []
    # Hint: Use nested for loops
    return table


def find_maximum(numbers):
    """
    Find the maximum value in a list of numbers.
    
    Args:
        numbers (list): List of numbers (assumed non-empty)
    
    Returns:
        int or float: Maximum value in the list
    """
    # TODO: Find maximum using a loop
    # Hint: Initialize max_value with first element, then compare
    if not numbers:
        return None
    max_value = None
    return max_value


def reverse_string(text):
    """
    Reverse a string using a loop.
    
    Args:
        text (str): String to reverse
    
    Returns:
        str: Reversed string
    """
    # TODO: Reverse string by building it character by character
    reversed_text = ""
    return reversed_text


def is_prime(n):
    """
    Check if a number is prime.
    
    A prime number is greater than 1 and has no divisors other than 1 and itself.
    
    Args:
        n (int): Number to check
    
    Returns:
        bool: True if n is prime, False otherwise
    """
    # TODO: Check if n is prime
    # Hint: Check if any number from 2 to sqrt(n) divides n
    # Edge cases: n < 2 is not prime
    if n < 2:
        return False
    
    # TODO: Check for divisors
    return True


################################################################################
# LIST COMPREHENSIONS EXERCISES
################################################################################

from typing import List, Dict, Set, Generator


def filter_even_numbers_comprehension(numbers: List[int]) -> List[int]:
    """
    Filter a list to return only even numbers using list comprehension.

    Example:
        >>> filter_even_numbers_comprehension([1, 2, 3, 4, 5, 6])
        [2, 4, 6]
    """
    # TODO: Use list comprehension with if condition
    pass


def square_numbers_comprehension(numbers: List[int]) -> List[int]:
    """
    Square all numbers in a list using list comprehension.

    Example:
        >>> square_numbers_comprehension([1, 2, 3, 4])
        [1, 4, 9, 16]
    """
    # TODO: Use list comprehension to square each number
    pass


def word_lengths_comprehension(words: List[str]) -> Dict[str, int]:
    """
    Create a dictionary mapping words to their lengths.

    Example:
        >>> word_lengths_comprehension(['hi', 'hello', 'python'])
        {'hi': 2, 'hello': 5, 'python': 6}
    """
    # TODO: Use dict comprehension
    pass


def unique_letters_comprehension(text: str) -> Set[str]:
    """
    Get unique letters from text using set comprehension.

    Example:
        >>> unique_letters_comprehension("hello")
        {'h', 'e', 'l', 'o'}
    """
    # TODO: Use set comprehension
    pass


def flatten_matrix_comprehension(matrix: List[List[int]]) -> List[int]:
    """
    Flatten a 2D list into 1D using nested comprehension.

    Example:
        >>> flatten_matrix_comprehension([[1, 2], [3, 4], [5, 6]])
        [1, 2, 3, 4, 5, 6]
    """
    # TODO: Use nested list comprehension
    pass


def generate_squares_comprehension(n: int) -> Generator[int, None, None]:
    """
    Generate squares lazily using generator expression.

    Example:
        >>> list(generate_squares_comprehension(5))
        [0, 1, 4, 9, 16]
    """
    # TODO: Return generator expression (not list!)
    pass