"""
Project 02: List Comprehensions - Practice Stubs

TODO: Implement these functions using list/dict/set comprehensions
Run tests with: pytest test_solution.py -v
"""

from typing import List, Dict, Set, Generator


def filter_even_numbers(numbers: List[int]) -> List[int]:
    """
    Filter a list to return only even numbers using list comprehension.

    Example:
        >>> filter_even_numbers([1, 2, 3, 4, 5, 6])
        [2, 4, 6]
    """
    # TODO: Use list comprehension with if condition
    pass


def square_numbers(numbers: List[int]) -> List[int]:
    """
    Square all numbers in a list using list comprehension.

    Example:
        >>> square_numbers([1, 2, 3, 4])
        [1, 4, 9, 16]
    """
    # TODO: Use list comprehension to square each number
    pass


def word_lengths(words: List[str]) -> Dict[str, int]:
    """
    Create a dictionary mapping words to their lengths.

    Example:
        >>> word_lengths(['hi', 'hello', 'python'])
        {'hi': 2, 'hello': 5, 'python': 6}
    """
    # TODO: Use dict comprehension
    pass


def unique_letters(text: str) -> Set[str]:
    """
    Get unique letters from text using set comprehension.

    Example:
        >>> unique_letters("hello")
        {'h', 'e', 'l', 'o'}
    """
    # TODO: Use set comprehension
    pass


def flatten_matrix(matrix: List[List[int]]) -> List[int]:
    """
    Flatten a 2D list into 1D using nested comprehension.

    Example:
        >>> flatten_matrix([[1, 2], [3, 4], [5, 6]])
        [1, 2, 3, 4, 5, 6]
    """
    # TODO: Use nested list comprehension
    pass


def generate_squares(n: int) -> Generator[int, None, None]:
    """
    Generate squares lazily using generator expression.

    Example:
        >>> list(generate_squares(5))
        [0, 1, 4, 9, 16]
    """
    # TODO: Return generator expression (not list!)
    pass
