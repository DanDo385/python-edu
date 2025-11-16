"""
Project 01: Basic Python Syntax - EXERCISE

Learn Python fundamentals: variables, types, I/O, and arithmetic.

Learning objectives:
- Understand dynamic typing and variable assignment
- Work with basic types: int, float, str, bool, None
- Perform arithmetic operations
- Convert between types
- Handle input/output with print() and input()
- Debug type-related errors

Author: Python-50x-Minis
Date: 2025-11-16
"""

from typing import Union, Optional, Any


# =============================================================================
# THINK BEFORE CODING
# =============================================================================
# 1. What is the problem asking?
# 2. What are the inputs and outputs?
# 3. What are the edge cases (empty, None, negative, zero)?
# 4. What types should I use?
# 5. How do I handle errors?


# =============================================================================
# PART 1: BASIC TYPES
# =============================================================================

def explore_types() -> dict[str, type]:
    """
    Create variables of different types and return their types.

    TODO: Create the following variables:
    - an_integer: any integer (e.g., 42)
    - a_float: any float (e.g., 3.14)
    - a_string: any string (e.g., "hello")
    - a_boolean: True or False
    - a_none: the None value

    Then return a dictionary mapping variable names to their types.

    Returns:
        dict mapping variable names (str) to their types (type objects)
        Example: {'an_integer': <class 'int'>, ...}

    Hint:
        Use type() to get the type of a value
        Example: type(42) returns <class 'int'>

    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    # TODO: Create variables of each type
    an_integer = None  # Replace None with an integer
    a_float = None     # Replace None with a float
    a_string = None    # Replace None with a string
    a_boolean = None   # Replace None with True or False
    a_none = None      # This one is already correct!

    # TODO: Create and return dictionary mapping names to types
    # Hint: Use type() function
    return {
        # TODO: fill this in
    }


# =============================================================================
# PART 2: ARITHMETIC OPERATIONS
# =============================================================================

def perform_arithmetic(a: int, b: int) -> dict[str, Union[int, float]]:
    """
    Perform all basic arithmetic operations on two integers.

    Args:
        a: First integer
        b: Second integer

    Returns:
        Dictionary with results of: addition, subtraction, multiplication,
        division, floor_division, modulo, exponentiation

    Example:
        >>> perform_arithmetic(10, 3)
        {
            'addition': 13,
            'subtraction': 7,
            'multiplication': 30,
            'division': 3.333...,
            'floor_division': 3,
            'modulo': 1,
            'exponentiation': 1000
        }

    Hint:
        Operators: +, -, *, /, //, %, **

    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    # TODO: Calculate each operation
    addition = None         # a + b
    subtraction = None      # a - b
    multiplication = None   # a * b
    division = None         # a / b (float division)
    floor_division = None   # a // b (integer division)
    modulo = None          # a % b (remainder)
    exponentiation = None  # a ** b (a to the power of b)

    # TODO: Return dictionary with all results
    return {
        # TODO: fill this in
    }


# =============================================================================
# PART 3: TYPE CONVERSION
# =============================================================================

def safe_int_convert(value: str, default: int = 0) -> int:
    """
    Convert a string to an integer, returning default if conversion fails.

    Args:
        value: String to convert
        default: Value to return if conversion fails

    Returns:
        Integer conversion of value, or default if ValueError occurs

    Examples:
        >>> safe_int_convert("42")
        42
        >>> safe_int_convert("hello", default=0)
        0
        >>> safe_int_convert("3.14", default=-1)
        -1

    Hint:
        Use try/except to catch ValueError
        int("42") works, but int("hello") raises ValueError

    Time Complexity: O(n) where n = length of string
    Space Complexity: O(1)
    """
    # TODO: Implement safe conversion with error handling
    # Hint: Use try/except block
    pass


def convert_to_float(value: Union[str, int]) -> float:
    """
    Convert an integer or string to a float.

    Args:
        value: Integer or string to convert

    Returns:
        Float representation of value

    Raises:
        ValueError: If value cannot be converted to float

    Examples:
        >>> convert_to_float("3.14")
        3.14
        >>> convert_to_float(42)
        42.0
        >>> convert_to_float("hello")
        ValueError: could not convert string to float: 'hello'

    Time Complexity: O(n) for strings, O(1) for integers
    Space Complexity: O(1)
    """
    # TODO: Convert to float using float() function
    # Note: This should raise ValueError for invalid inputs (that's intentional!)
    pass


# =============================================================================
# PART 4: STRING FORMATTING
# =============================================================================

def format_person_info(name: str, age: int, height: float) -> str:
    """
    Create a formatted string with person information.

    Args:
        name: Person's name
        age: Person's age in years
        height: Person's height in meters

    Returns:
        Formatted string using f-string syntax

    Example:
        >>> format_person_info("Alice", 30, 1.65)
        "Alice is 30 years old and 1.65 meters tall."

    Hint:
        Use f-strings: f"text {variable} more text"

    Time Complexity: O(n) where n = total length of output string
    Space Complexity: O(n)
    """
    # TODO: Create formatted string using f-string
    # Format: "{name} is {age} years old and {height} meters tall."
    pass


# =============================================================================
# PART 5: BOOLEAN LOGIC
# =============================================================================

def check_number_properties(n: int) -> dict[str, bool]:
    """
    Check various properties of a number.

    Args:
        n: Integer to check

    Returns:
        Dictionary with boolean results for:
        - is_positive: n > 0
        - is_even: n is even
        - is_large: n > 100
        - is_small: n < 10
        - is_in_range: 10 <= n <= 100

    Example:
        >>> check_number_properties(42)
        {
            'is_positive': True,
            'is_even': True,
            'is_large': False,
            'is_small': False,
            'is_in_range': True
        }

    Hint:
        Even numbers: n % 2 == 0
        Comparison operators: >, <, >=, <=, ==

    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    # TODO: Calculate each property
    is_positive = None   # n > 0
    is_even = None       # n % 2 == 0
    is_large = None      # n > 100
    is_small = None      # n < 10
    is_in_range = None   # 10 <= n <= 100

    # TODO: Return dictionary
    return {
        # TODO: fill this in
    }


# =============================================================================
# PART 6: VARIABLE ASSIGNMENT
# =============================================================================

def demonstrate_assignment() -> tuple[int, int, int]:
    """
    Demonstrate multiple assignment and swapping.

    Returns:
        Tuple of (a, b, c) after:
        1. a, b, c = 1, 2, 3 (multiple assignment)
        2. a, b = b, a (swap a and b)
        3. c = a + b (update c)

    Example:
        >>> demonstrate_assignment()
        (2, 1, 3)

        Explanation:
        - Start: a=1, b=2, c=3
        - After swap: a=2, b=1, c=3
        - After update: a=2, b=1, c=3 (2+1=3)

    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    # TODO: Implement multiple assignment
    a, b, c = None, None, None  # Set to 1, 2, 3

    # TODO: Swap a and b (Python's tuple unpacking makes this easy!)
    # Hint: a, b = b, a

    # TODO: Update c to be sum of a and b

    return (a, b, c)


# =============================================================================
# PART 7: COMPARISON AND IDENTITY
# =============================================================================

def compare_values(x: Any, y: Any) -> dict[str, bool]:
    """
    Compare two values using different comparison methods.

    Args:
        x: First value
        y: Second value

    Returns:
        Dictionary with results of:
        - equal_value: x == y (same value?)
        - same_type: type(x) == type(y)
        - same_identity: x is y (same object in memory?)

    Example:
        >>> compare_values(42, 42)
        {'equal_value': True, 'same_type': True, 'same_identity': True}

        >>> compare_values(42, "42")
        {'equal_value': False, 'same_type': False, 'same_identity': False}

    Note:
        == checks value equality
        is checks object identity (same memory location)

    Time Complexity: O(1) for simple types, O(n) for strings/lists
    Space Complexity: O(1)
    """
    # TODO: Implement comparisons
    equal_value = None     # x == y
    same_type = None       # type(x) == type(y)
    same_identity = None   # x is y

    return {
        # TODO: fill this in
    }


# =============================================================================
# PART 8: ADVANCED CHALLENGE (Optional)
# =============================================================================

def calculate_bmi(weight_kg: float, height_m: float) -> dict[str, Union[float, str]]:
    """
    Calculate Body Mass Index and categorize it.

    Args:
        weight_kg: Weight in kilograms
        height_m: Height in meters

    Returns:
        Dictionary with:
        - bmi: Calculated BMI (weight / height^2)
        - category: "Underweight", "Normal", "Overweight", or "Obese"
            - Underweight: BMI < 18.5
            - Normal: 18.5 <= BMI < 25
            - Overweight: 25 <= BMI < 30
            - Obese: BMI >= 30

    Example:
        >>> calculate_bmi(70, 1.75)
        {'bmi': 22.86, 'category': 'Normal'}

    Raises:
        ValueError: If weight or height is <= 0

    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    # TODO: Validate inputs (raise ValueError if <= 0)

    # TODO: Calculate BMI = weight / (height ** 2)

    # TODO: Determine category based on BMI ranges
    # Hint: Use if/elif/else (from Project 02, but you can figure it out!)

    pass


# =============================================================================
# MAIN (for testing)
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("Project 01: Basic Python Syntax - EXERCISE")
    print("=" * 60)

    # Test Part 1: Types
    print("\n--- Part 1: Types ---")
    try:
        types_dict = explore_types()
        print(f"Types: {types_dict}")
    except Exception as e:
        print(f"Error: {e}")

    # Test Part 2: Arithmetic
    print("\n--- Part 2: Arithmetic ---")
    try:
        results = perform_arithmetic(10, 3)
        print(f"10 + 3 = {results.get('addition')}")
        print(f"10 / 3 = {results.get('division')}")
        print(f"10 // 3 = {results.get('floor_division')}")
        print(f"10 % 3 = {results.get('modulo')}")
    except Exception as e:
        print(f"Error: {e}")

    # Test Part 3: Type Conversion
    print("\n--- Part 3: Type Conversion ---")
    try:
        print(f"safe_int_convert('42') = {safe_int_convert('42')}")
        print(f"safe_int_convert('hello', -1) = {safe_int_convert('hello', -1)}")
        print(f"convert_to_float('3.14') = {convert_to_float('3.14')}")
    except Exception as e:
        print(f"Error: {e}")

    # Test Part 4: String Formatting
    print("\n--- Part 4: String Formatting ---")
    try:
        info = format_person_info("Alice", 30, 1.65)
        print(info)
    except Exception as e:
        print(f"Error: {e}")

    # Test Part 5: Boolean Logic
    print("\n--- Part 5: Boolean Logic ---")
    try:
        props = check_number_properties(42)
        print(f"Properties of 42: {props}")
    except Exception as e:
        print(f"Error: {e}")

    # Test Part 6: Assignment
    print("\n--- Part 6: Assignment ---")
    try:
        a, b, c = demonstrate_assignment()
        print(f"After operations: a={a}, b={b}, c={c}")
    except Exception as e:
        print(f"Error: {e}")

    # Test Part 7: Comparison
    print("\n--- Part 7: Comparison ---")
    try:
        comp1 = compare_values(42, 42)
        comp2 = compare_values(42, "42")
        print(f"compare_values(42, 42): {comp1}")
        print(f"compare_values(42, '42'): {comp2}")
    except Exception as e:
        print(f"Error: {e}")

    # Test Part 8: Challenge
    print("\n--- Part 8: Challenge (BMI Calculator) ---")
    try:
        bmi_result = calculate_bmi(70, 1.75)
        print(f"BMI Result: {bmi_result}")
    except Exception as e:
        print(f"Error: {e}")

    print("\n" + "=" * 60)
    print("Exercise complete! Check test/test_project_01.py to verify.")
    print("=" * 60)
