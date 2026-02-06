"""
Project 01: Dynamic Typing Basics - Practice Stubs

TODO: Implement these functions and run tests with: pytest test_project_01.py -v
"""

from typing import Any, Union, Optional


def add_numbers(a, b):
    """
    Add two numbers together.

    This function demonstrates basic dynamic typing - it works with
    both integers and floats without explicit type declarations.

    Args:
        a: First number (int or float)
        b: Second number (int or float)

    Returns:
        Sum of a and b

    Example:
        >>> add_numbers(5, 3)
        8
        >>> add_numbers(5.5, 2.3)
        7.8
    """
    # TODO: Implement this function
    pass


def multiply(x, times):
    """
    Multiply/repeat a value.

    This function demonstrates duck typing - it works with any type
    that supports the * operator (numbers, strings, lists).

    Args:
        x: Value to multiply/repeat
        times: How many times

    Returns:
        x multiplied/repeated times

    Example:
        >>> multiply(5, 3)
        15
        >>> multiply("hi", 3)
        'hihihi'
        >>> multiply([1, 2], 3)
        [1, 2, 1, 2, 1, 2]
    """
    # TODO: Implement this function
    pass


def describe_type(value: Any) -> str:
    """
    Return a description of the value's type.

    This function demonstrates type introspection using type() and isinstance().

    Args:
        value: Any value to describe

    Returns:
        String describing the type (e.g., "Integer: 42")

    Example:
        >>> describe_type(42)
        'Integer: 42'
        >>> describe_type("hello")
        'String: hello'
        >>> describe_type([1, 2, 3])
        'List: [1, 2, 3]'
    """
    # TODO: Implement this function
    # Hint: Use isinstance() to check types
    pass


def safe_divide(a: Union[int, float], b: Union[int, float]) -> float:
    """
    Safely divide two numbers with type checking.

    This function demonstrates explicit type checking and validation.

    Args:
        a: Numerator (must be int or float)
        b: Denominator (must be int or float, cannot be zero)

    Returns:
        Result of a / b

    Raises:
        TypeError: If a or b is not int or float
        ValueError: If b is zero

    Example:
        >>> safe_divide(10, 2)
        5.0
        >>> safe_divide(10, 0)
        Traceback (most recent call last):
        ... 
        ValueError: Cannot divide by zero
    """
    # TODO: Implement this function with type checking
    # Hint: Use isinstance() to validate types
    pass


def process_data(data: Union[int, str, list]) -> Any:
    """
    Process data differently based on its type.

    This function demonstrates type-based conditional logic.

    Args:
        data: Can be int, str, or list

    Returns:
        - If int: return data * 2
        - If str: return data.upper()
        - If list: return sorted(data)
        - Otherwise: raise TypeError

    Example:
        >>> process_data(5)
        10
        >>> process_data("hello")
        'HELLO'
        >>> process_data([3, 1, 2])
        [1, 2, 3]
    """
    # TODO: Implement type-based processing
    pass


if __name__ == "__main__":
    # Test your implementations here
    print("Testing add_numbers:")
    print(add_numbers(5, 3))

    print("\nTesting multiply:")
    print(multiply(5, 3))
    print(multiply("hi", 3))

    print("\nTesting describe_type:")
    print(describe_type(42))
    print(describe_type("hello"))

    print("\nTesting safe_divide:")
    print(safe_divide(10, 2))

    print("\nTesting process_data:")
    print(process_data(5))
    print(process_data("hello"))
    print(process_data([3, 1, 2]))