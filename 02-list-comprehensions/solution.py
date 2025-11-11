"""
PROJECT 02: LIST COMPREHENSIONS - PYTHON'S SUPERPOWER

List comprehensions are one of Python's most distinctive and powerful features.
They provide a concise way to create lists, often replacing multi-line loops
with a single readable expression.

WHY LIST COMPREHENSIONS?
------------------------
1. More concise than loops (1 line vs 3-4 lines)
2. Faster execution (~20-25% faster than append loops)
3. More readable (once you learn the syntax)
4. Pythonic (idiomatic Python code)

BASIC SYNTAX:
[expression for item in iterable if condition]
"""

from typing import List, Dict, Set, Generator


def filter_even_numbers(numbers: List[int]) -> List[int]:
    """Filter list to return only even numbers using list comprehension."""
    return [x for x in numbers if x % 2 == 0]
    # [x for x in numbers if x % 2 == 0]
    # │ │      │       │  │  │  │  └─ Zero (even check)
    # │ │      │       │  │  │  └─ Equality operator
    # │ │      │       │  │  └─ Modulo operator
    # │ │      │       │  └─ Condition (filter)
    # │ │      │       └─ Variable
    # │ │      └─ Source iterable
    # │ └─ Expression (what to include)
    # └─ Create new list


def square_numbers(numbers: List[int]) -> List[int]:
    """Square all numbers using list comprehension."""
    return [x ** 2 for x in numbers]
    # [x ** 2 for x in numbers]
    # │ │  │     │    └─ Source list
    # │ │  │     └─ Iterate variable
    # │ │  └─ Exponent (2)
    # │ └─ Power operator
    # └─ Expression to evaluate


def word_lengths(words: List[str]) -> Dict[str, int]:
    """Create dict mapping words to lengths using dict comprehension."""
    return {word: len(word) for word in words}
    # {word: len(word) for word in words}
    # │ │    │  │ │       │    └─ Source
    # │ │    │  │ │       └─ Iterate
    # │ │    │  │ └─ Call len() function
    # │ │    │  └─ Get length
    # │ │    └─ Key in dict
    # │ └─ Value in dict
    # └─ Create dict


def unique_letters(text: str) -> Set[str]:
    """Get unique letters using set comprehension."""
    return {char for char in text}
    # {char for char in text}
    # │ │       │    └─ Source string
    # │ │       └─ Iterate characters
    # │ └─ Expression
    # └─ Create set (automatically unique)


def flatten_matrix(matrix: List[List[int]]) -> List[int]:
    """Flatten 2D list using nested comprehension."""
    return [num for row in matrix for num in row]
    # [num for row in matrix for num in row]
    # │ │     │      │       │   │   └─ Inner list
    # │ │     │      │       │   └─ Inner loop
    # │ │     │      │       └─ Inner iteration
    # │ │     │      └─ Outer list (matrix)
    # │ │     └─ Outer loop
    # │ └─ Expression (element to include)
    # └─ Create flattened list


def generate_squares(n: int) -> Generator[int, None, None]:
    """Generate squares lazily using generator expression."""
    return (x ** 2 for x in range(n))
    # (x ** 2 for x in range(n))
    # │           └─ Note: PARENTHESES not brackets
    # │              This creates a generator, not a list
    # │              Lazy evaluation - computes values on demand
    # └─ Returns generator object


# Performance comparison:
# List:      [x**2 for x in range(1_000_000)]  # ~8MB memory
# Generator: (x**2 for x in range(1_000_000))  # ~88 bytes!

# Use generators when:
# - Processing large datasets
# - You only need to iterate once
# - Memory is a concern

# Use lists when:
# - You need to iterate multiple times
# - You need random access (list[index])
# - Dataset is small
