"""
Project 01: Basic Python Syntax - SOLUTION

Full implementation with detailed inline comments demonstrating production-quality
documentation standards for the Python-50x-Minis curriculum.

This solution demonstrates:
- Comprehensive docstrings with examples and complexity analysis
- Line-by-line implementation comments explaining the "why" not just "what"
- Type hints for all function signatures
- Error handling with detailed explanations
- Multiple implementation approaches where relevant
- Cross-references to Python internals and best practices

WHAT YOU'LL LEARN:
- Python's dynamic type system and how it differs from static typing
- Variable assignment is name binding (references, not values)
- Arithmetic operators and their precedence
- Type conversion with error handling
- String formatting using f-strings
- Boolean logic and comparison operators
- Memory model: immutability, object identity, interning

WHY THIS MATTERS:
Every Python program uses these fundamentals. Understanding the type system
deeply helps you:
1. Debug type-related errors efficiently
2. Write more robust code with proper type hints
3. Avoid common pitfalls (float precision, integer division, mutability)
4. Understand how high-level frameworks (NumPy, PyTorch) work under the hood

TIME INVESTMENT: 2-3 hours to understand all nuances
PREREQUISITE: None—this is the starting point!

Author: Python-50x-Minis
Date: 2025-11-16
"""

from typing import Union, Optional, Any
import sys


# =============================================================================
# PART 1: BASIC TYPES
# =============================================================================

def explore_types() -> dict[str, type]:
    """
    Create variables of different types and return their types.

    This demonstrates Python's dynamic typing system where variables
    can hold any type without declaration.

    Algorithm:
    ----------
    1. Create one variable of each basic type
    2. Use type() built-in to get the type object
    3. Return dictionary mapping name → type

    Returns:
        dict[str, type]: Mapping of variable names to their type objects

    Examples:
        >>> result = explore_types()
        >>> result['an_integer']
        <class 'int'>
        >>> result['a_float']
        <class 'float'>

    Time Complexity:
        O(1) - Creating variables and dictionary is constant time

    Space Complexity:
        O(1) - Fixed number of variables regardless of input

    Notes:
        - type() returns the type object, not a string
        - All types inherit from 'object' (Python's root type)
        - NoneType is a singleton: there's only one None object in memory
    """
    # INTEGER: Whole numbers (positive, negative, or zero)
    # Python 3 has arbitrary precision: can represent numbers larger than C's long
    an_integer = 42

    # FLOAT: Floating-point numbers (64-bit IEEE 754 double precision)
    # Stored as: sign bit + 11 exponent bits + 52 mantissa bits
    # Max value: ~1.8 × 10^308, Min positive: ~2.2 × 10^-308
    a_float = 3.14

    # STRING: Immutable sequence of Unicode characters
    # In Python 3, all strings are Unicode by default (unlike Python 2)
    # Stored as: pointer to char array + length + hash (for dictionary lookups)
    a_string = "hello"

    # BOOLEAN: Subclass of int! True == 1, False == 0
    # This means you can do arithmetic: True + True == 2
    # Historical reason: compatibility with C's bool type
    a_boolean = True

    # NONE: Python's null/nil value
    # NoneType has exactly one instance: None
    # Common uses: default arguments, missing values, initialization
    a_none = None

    # type() is a built-in function that returns the type object
    # Alternative: isinstance(42, int) returns bool instead of type object
    return {
        'an_integer': type(an_integer),  # <class 'int'>
        'a_float': type(a_float),        # <class 'float'>
        'a_string': type(a_string),      # <class 'str'>
        'a_boolean': type(a_boolean),    # <class 'bool'>
        'a_none': type(a_none),          # <class 'NoneType'>
    }


# =============================================================================
# PART 2: ARITHMETIC OPERATIONS
# =============================================================================

def perform_arithmetic(a: int, b: int) -> dict[str, Union[int, float]]:
    """
    Perform all basic arithmetic operations on two integers.

    Demonstrates Python's arithmetic operators and their behavior,
    including the important distinction between / and //.

    Algorithm:
    ----------
    1. Apply each arithmetic operator to inputs
    2. Return results in dictionary for easy inspection

    Args:
        a: First integer operand
        b: Second integer operand

    Returns:
        dict[str, Union[int, float]]: Results of all arithmetic operations
            - Most operations return int
            - Division (/) always returns float (even for whole results)

    Examples:
        >>> perform_arithmetic(10, 3)
        {
            'addition': 13,
            'subtraction': 7,
            'multiplication': 30,
            'division': 3.3333333333333335,
            'floor_division': 3,
            'modulo': 1,
            'exponentiation': 1000
        }

    Time Complexity:
        O(1) for small integers
        O(log n) for very large integers (exponentiation with big numbers)

    Space Complexity:
        O(1) - Dictionary size is constant

    Notes:
        OPERATOR PRECEDENCE (highest to lowest):
        1. ** (exponentiation)
        2. *, /, //, % (multiplication, division, floor div, modulo)
        3. +, - (addition, subtraction)

        GOTCHAS:
        - Division (/) ALWAYS returns float, even for 10/5
        - Floor division (//) rounds toward negative infinity, not zero
          Example: -7 // 3 == -3 (not -2!)
        - Modulo sign matches divisor: -7 % 3 == 2 (not -1!)
    """
    # ADDITION: a + b
    # Integer addition is exact (no overflow in Python 3!)
    # Example: 10 + 3 = 13
    addition = a + b

    # SUBTRACTION: a - b
    # Order matters: subtraction is not commutative
    # Example: 10 - 3 = 7, but 3 - 10 = -7
    subtraction = a - b

    # MULTIPLICATION: a * b
    # For integers, result is exact (arbitrary precision)
    # Example: 10 * 3 = 30
    multiplication = a * b

    # DIVISION: a / b (FLOAT DIVISION)
    # ALWAYS returns float, even if result is a whole number
    # Example: 10 / 3 = 3.333..., but also 10 / 5 = 2.0 (float!)
    # This changed in Python 3; in Python 2, 10 / 3 == 3 (integer division)
    division = a / b

    # FLOOR DIVISION: a // b (INTEGER DIVISION)
    # Returns largest integer <= result of true division
    # Example: 10 // 3 = 3 (rounds down to nearest int)
    # IMPORTANT: Rounds toward -∞, not toward 0!
    #   -7 // 3 = -3 (not -2, because -2.333... rounds down to -3)
    floor_division = a // b

    # MODULO: a % b (REMAINDER)
    # Returns remainder after floor division
    # Property: a == (a // b) * b + (a % b) always holds
    # Example: 10 % 3 = 1 because 10 = 3*3 + 1
    # GOTCHA: Sign matches divisor (b), not dividend (a)
    #   -7 % 3 = 2 (not -1!) because -7 = 3*(-3) + 2
    modulo = a % b

    # EXPONENTIATION: a ** b (POWER)
    # a raised to the power of b
    # Example: 10 ** 3 = 1000
    # For large exponents, this can be slow: O(log b) multiplications
    # Alternative for modular exponentiation: pow(a, b, m) for (a^b) % m
    exponentiation = a ** b

    # Return dictionary with descriptive keys
    # Using dict literal syntax (Python 3.6+: insertion order is preserved)
    return {
        'addition': addition,
        'subtraction': subtraction,
        'multiplication': multiplication,
        'division': division,
        'floor_division': floor_division,
        'modulo': modulo,
        'exponentiation': exponentiation,
    }


# =============================================================================
# PART 3: TYPE CONVERSION
# =============================================================================

def safe_int_convert(value: str, default: int = 0) -> int:
    """
    Convert a string to an integer, returning default if conversion fails.

    This demonstrates defensive programming with try/except error handling,
    essential for parsing user input or external data.

    Algorithm:
    ----------
    1. Attempt conversion with int()
    2. If ValueError raised, catch and return default
    3. Return successfully converted value

    Args:
        value: String to convert (e.g., "42", "-17", "0xFF")
        default: Fallback value if conversion fails (default: 0)

    Returns:
        int: Converted value or default on error

    Examples:
        >>> safe_int_convert("42")
        42
        >>> safe_int_convert("hello", default=0)
        0
        >>> safe_int_convert("3.14", default=-1)
        -1

    Time Complexity:
        O(n) where n = length of string
        int() must parse each character

    Space Complexity:
        O(1) - conversion creates single int object

    Notes:
        WHY THIS PATTERN?
        - User input is always strings: input() returns str
        - Config files (JSON, YAML) may have string values
        - CSV parsing: all fields are initially strings

        ALTERNATIVE APPROACHES:
        1. Check with str.isdigit() first (but doesn't handle negatives!)
        2. Use regex: re.match(r'^-?\\d+$', value)
        3. Let it raise and handle at call site (EAFP: "Easier to Ask
           Forgiveness than Permission")

        int() ACCEPTS:
        - "42", "-17", "0" (decimal)
        - "0xFF", "0x2A" (hexadecimal with base 16)
        - "0o52", "0b101010" (octal, binary)

        int() REJECTS (raises ValueError):
        - "3.14" (use float() first, then int())
        - "hello", "12.34abc"
        - "" (empty string)
    """
    try:
        # Attempt conversion
        # int() strips leading/trailing whitespace automatically
        # int("  42  ") == 42
        return int(value)
    except ValueError:
        # ValueError raised when string doesn't represent a valid integer
        # Examples: "hello", "3.14", "", "12abc"
        # We catch this exception and return the default value instead
        # This is EAFP: "Easier to Ask Forgiveness than Permission"
        return default


def convert_to_float(value: Union[str, int]) -> float:
    """
    Convert an integer or string to a float.

    Unlike safe_int_convert(), this function lets exceptions propagate
    to demonstrate different error handling strategies.

    Args:
        value: Integer or string to convert

    Returns:
        float: Float representation of value

    Raises:
        ValueError: If string cannot be converted to float
        TypeError: If value is not str or int (e.g., list, dict)

    Examples:
        >>> convert_to_float("3.14")
        3.14
        >>> convert_to_float(42)
        42.0
        >>> convert_to_float("1.23e-4")
        0.000123
        >>> convert_to_float("hello")
        Traceback (most recent call last):
        ValueError: could not convert string to float: 'hello'

    Time Complexity:
        O(n) for strings (must parse)
        O(1) for integers (just wraps in float object)

    Space Complexity:
        O(1) - single float object created

    Notes:
        DESIGN DECISION: Why not catch the exception?
        - Sometimes it's better to let exceptions propagate
        - Caller can decide how to handle errors
        - Avoids hiding bugs (silent failures are dangerous!)

        FLOAT REPRESENTATION:
        - 64-bit IEEE 754 double precision
        - 1 sign bit, 11 exponent bits, 52 mantissa bits
        - Special values: float('inf'), float('-inf'), float('nan')

        PRECISION GOTCHA:
        - 0.1 + 0.2 != 0.3 in binary floating point!
        - Always use abs(a - b) < epsilon for float comparisons
        - For exact decimal: use decimal.Decimal("0.1")

        float() ACCEPTS:
        - "3.14", "-0.5", "1e10" (scientific notation)
        - "inf", "-inf", "nan" (special values)
        - int values: 42 → 42.0

        float() REJECTS:
        - "hello", "", "12.34.56"
    """
    # Simply call float() and let any exceptions propagate
    # This follows LBYL (Look Before You Leap) principle
    # Alternative: Check type first with isinstance()
    return float(value)


# =============================================================================
# PART 4: STRING FORMATTING
# =============================================================================

def format_person_info(name: str, age: int, height: float) -> str:
    """
    Create a formatted string with person information.

    Demonstrates f-strings (PEP 498), the modern way to format strings
    in Python 3.6+. Much faster and more readable than % formatting or
    .format() method.

    Args:
        name: Person's name
        age: Person's age in years
        height: Person's height in meters

    Returns:
        str: Formatted string with person details

    Examples:
        >>> format_person_info("Alice", 30, 1.65)
        'Alice is 30 years old and 1.65 meters tall.'

        >>> format_person_info("Bob", 25, 1.80)
        'Bob is 25 years old and 1.8 meters tall.'

    Time Complexity:
        O(n) where n = total length of output string

    Space Complexity:
        O(n) for the output string

    Notes:
        F-STRING FEATURES:
        - Expressions inside {}: f"{2 + 2}" → "4"
        - Format specs: f"{pi:.2f}" → "3.14"
        - Debug syntax (3.8+): f"{x=}" → "x=42"
        - Multiline: Works across multiple lines

        ALTERNATIVE METHODS (older, slower):
        1. % formatting: "%s is %d years old" % (name, age)
        2. .format(): "{} is {} years old".format(name, age)
        3. Template strings: Template("$name is $age").substitute(...)

        PERFORMANCE:
        f-strings are ~2x faster than .format() and ~1.5x faster than %

        FORMATTING SYNTAX:
        f"{value:width.precision type}"
        - {x:10} - right-align in 10 chars
        - {x:<10} - left-align
        - {x:^10} - center
        - {x:.2f} - 2 decimal places
        - {x:,} - thousand separators: 1,000,000
    """
    # F-string: f"..." allows {expression} interpolation
    # Evaluated at runtime, not compile time
    # Much more efficient than concatenation: "str" + var + "str"
    return f"{name} is {age} years old and {height} meters tall."


# =============================================================================
# PART 5: BOOLEAN LOGIC
# =============================================================================

def check_number_properties(n: int) -> dict[str, bool]:
    """
    Check various properties of a number.

    Demonstrates boolean expressions and comparison operators.

    Args:
        n: Integer to check

    Returns:
        dict[str, bool]: Boolean results for various properties

    Examples:
        >>> check_number_properties(42)
        {
            'is_positive': True,
            'is_even': True,
            'is_large': False,
            'is_small': False,
            'is_in_range': True
        }

        >>> check_number_properties(150)
        {
            'is_positive': True,
            'is_even': True,
            'is_large': True,
            'is_small': False,
            'is_in_range': False
        }

    Time Complexity:
        O(1) - All comparisons are constant time for integers

    Space Complexity:
        O(1) - Dictionary size is fixed

    Notes:
        COMPARISON OPERATORS:
        - > < >= <= : Numeric comparison
        - == != : Value equality
        - is, is not : Identity (same object in memory)

        LOGICAL OPERATORS:
        - and, or, not : Boolean logic
        - Short-circuit evaluation: 'a and b' doesn't evaluate b if a is False

        CHAINED COMPARISONS:
        - 10 <= n <= 100 is valid Python! (not all languages support this)
        - Equivalent to: (10 <= n) and (n <= 100)

        TRUTHY/FALSY VALUES:
        Falsy: False, None, 0, 0.0, "", [], {}, set()
        Truthy: Everything else (True, 1, "non-empty", [1, 2], ...)

        GOTCHA: == vs is
        - == compares values: [1,2] == [1,2] is True
        - is compares identity: [1,2] is [1,2] is False (different objects)
        - Exception: Small integers (-5 to 256) are interned
          id(42) == id(42) is True (same object!)
    """
    # Positive: Greater than zero
    # Could also check: n > 0 or n >= 1 (equivalent for integers)
    is_positive = n > 0

    # Even: Divisible by 2 with no remainder
    # Modulo operator: n % 2 returns 0 for even, 1 for odd
    # Alternative: (n & 1) == 0 (bitwise AND, but less readable)
    is_even = n % 2 == 0

    # Large: Greater than 100
    # This is arbitrary threshold for demonstration
    is_large = n > 100

    # Small: Less than 10
    # Note: Could be negative! -5 is "small"
    is_small = n < 10

    # In range: Between 10 and 100 (inclusive)
    # Python allows chained comparisons: 10 <= n <= 100
    # This is syntactic sugar for: (10 <= n) and (n <= 100)
    # More readable than: n >= 10 and n <= 100
    is_in_range = 10 <= n <= 100

    return {
        'is_positive': is_positive,
        'is_even': is_even,
        'is_large': is_large,
        'is_small': is_small,
        'is_in_range': is_in_range,
    }


# =============================================================================
# PART 6: VARIABLE ASSIGNMENT
# =============================================================================

def demonstrate_assignment() -> tuple[int, int, int]:
    """
    Demonstrate multiple assignment and swapping.

    Shows Python's tuple unpacking feature, which enables elegant
    simultaneous assignments and swaps.

    Returns:
        tuple[int, int, int]: Values of (a, b, c) after operations

    Examples:
        >>> demonstrate_assignment()
        (2, 1, 3)

    Time Complexity:
        O(1) - All assignments are constant time

    Space Complexity:
        O(1) - Three integer objects

    Notes:
        MULTIPLE ASSIGNMENT:
        a, b, c = 1, 2, 3 is "tuple unpacking"
        Right side creates tuple (1, 2, 3), left side unpacks it

        HOW SWAPPING WORKS:
        a, b = b, a
        1. Evaluate right side: creates tuple (b, a)
        2. Unpack to left side: assign b to a, assign a to b
        3. No temp variable needed! (Unlike C, Java)

        EQUIVALENT C CODE:
        int temp = a;
        a = b;
        b = temp;

        MEMORY MODEL:
        Variables are names, not boxes!
        a = 42 doesn't put 42 "in" a
        It binds the name 'a' to the integer object 42

        GOTCHA: Unpacking counts must match!
        a, b = 1, 2, 3  # ValueError: too many values to unpack
        a, b, c = 1, 2  # ValueError: not enough values to unpack
    """
    # Multiple assignment using tuple unpacking
    # Creates three integer objects: 1, 2, 3
    # Binds names a, b, c to these objects respectively
    a, b, c = 1, 2, 3

    # Swap a and b using tuple unpacking
    # Right side: Creates tuple (b, a) = (2, 1)
    # Left side: Unpacks to a=2, b=1
    # This is atomic: both assignments happen simultaneously
    # No temporary variable needed!
    a, b = b, a

    # Update c to sum of a and b
    # After swap: a=2, b=1, so c=3
    # Note: += operator also exists: c += a is equivalent to c = c + a
    c = a + b

    # Return as tuple
    # Parentheses are optional: (a, b, c) and a, b, c are equivalent
    return (a, b, c)


# =============================================================================
# PART 7: COMPARISON AND IDENTITY
# =============================================================================

def compare_values(x: Any, y: Any) -> dict[str, bool]:
    """
    Compare two values using different comparison methods.

    Demonstrates the crucial difference between == (value equality)
    and is (identity equality).

    Args:
        x: First value (any type)
        y: Second value (any type)

    Returns:
        dict[str, bool]: Results of different comparison methods

    Examples:
        >>> compare_values(42, 42)
        {'equal_value': True, 'same_type': True, 'same_identity': True}

        >>> compare_values(42, "42")
        {'equal_value': False, 'same_type': False, 'same_identity': False}

        >>> a = [1, 2, 3]
        >>> b = [1, 2, 3]
        >>> compare_values(a, b)
        {'equal_value': True, 'same_type': True, 'same_identity': False}

    Time Complexity:
        O(1) for simple types (int, float, bool)
        O(n) for strings and containers (must compare elements)

    Space Complexity:
        O(1) - No new objects created

    Notes:
        == vs is:
        - == checks VALUE equality (calls __eq__ method)
        - is checks IDENTITY (same object in memory)

        EXAMPLES:
        a = [1, 2]
        b = [1, 2]
        a == b  # True (same values)
        a is b  # False (different objects)

        c = a
        a is c  # True (same object, c is alias for a)

        SMALL INTEGER CACHING (CPython optimization):
        Integers from -5 to 256 are cached (interned)
        a = 42
        b = 42
        a is b  # True! Both reference same cached object

        But:
        a = 257
        b = 257
        a is b  # False (not cached, separate objects)

        WHEN TO USE is:
        - Comparing with None: if x is None
        - Comparing with True/False (but usually not needed)
        - Checking object identity (rarely needed)

        WHEN TO USE ==:
        - Almost everything else!
        - Comparing values, not identities
    """
    # Value equality: Do they have the same value?
    # Calls x.__eq__(y) under the hood
    # For lists: [1,2] == [1,2] is True
    # For different types: 42 == "42" is False
    equal_value = x == y

    # Type equality: Are they the same type?
    # type(x) returns the type object (e.g., <class 'int'>)
    # Note: isinstance() is usually better for type checking
    #   isinstance(42, int) handles subclasses correctly
    #   type(True) == int is False, but isinstance(True, int) is True
    same_type = type(x) == type(y)

    # Identity: Are they the same object in memory?
    # Compares memory addresses (id(x) == id(y))
    # For immutable types (int, str), Python may intern values:
    #   a = "hello"
    #   b = "hello"
    #   a is b  # May be True! (string interning optimization)
    # For mutable types (list, dict), almost always False unless aliased
    same_identity = x is y

    return {
        'equal_value': equal_value,
        'same_type': same_type,
        'same_identity': same_identity,
    }


# =============================================================================
# PART 8: ADVANCED CHALLENGE
# =============================================================================

def calculate_bmi(weight_kg: float, height_m: float) -> dict[str, Union[float, str]]:
    """
    Calculate Body Mass Index and categorize it.

    This advanced function combines input validation, arithmetic,
    and conditional logic (from Project 02, but introduced here as a challenge).

    Args:
        weight_kg: Weight in kilograms (must be positive)
        height_m: Height in meters (must be positive)

    Returns:
        dict with keys:
            'bmi': Calculated BMI value (float)
            'category': Health category (str)

    Raises:
        ValueError: If weight or height is <= 0

    Examples:
        >>> calculate_bmi(70, 1.75)
        {'bmi': 22.86, 'category': 'Normal'}

        >>> calculate_bmi(90, 1.75)
        {'bmi': 29.39, 'category': 'Overweight'}

        >>> calculate_bmi(0, 1.75)
        Traceback (most recent call last):
        ValueError: Weight and height must be positive

    Time Complexity:
        O(1) - Arithmetic and comparisons are constant time

    Space Complexity:
        O(1) - Fixed-size dictionary

    Notes:
        BMI FORMULA:
        BMI = weight (kg) / height² (m²)

        WHO CATEGORIES:
        - Underweight: BMI < 18.5
        - Normal weight: 18.5 <= BMI < 25
        - Overweight: 25 <= BMI < 30
        - Obese: BMI >= 30

        LIMITATIONS OF BMI:
        - Doesn't account for muscle mass
        - Not accurate for athletes, elderly, children
        - Different standards for different populations

        FLOATING-POINT PRECISION:
        - BMI calculation may have tiny rounding errors
        - For this use case, precision loss is acceptable
        - For financial calculations, use decimal.Decimal
    """
    # Input validation: Ensure positive values
    # This is "defensive programming": validate inputs before processing
    # Alternative: Use assert (but those can be disabled with python -O)
    if weight_kg <= 0 or height_m <= 0:
        # Raise ValueError with descriptive message
        # ValueError is appropriate for invalid argument values
        # (TypeError would be for wrong types, e.g., passing a string)
        raise ValueError("Weight and height must be positive")

    # Calculate BMI using formula: weight / height²
    # Using ** for exponentiation: height_m ** 2 is height_m²
    # Alternative: height_m * height_m (but ** is more explicit)
    bmi = weight_kg / (height_m ** 2)

    # Determine category using if/elif/else (from Project 02)
    # Ordered from specific to general: check lowest threshold first
    # Note: Once a condition matches, remaining elif/else are skipped
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        # This implicitly means 18.5 <= bmi < 25
        # because bmi < 18.5 was already checked above
        category = "Normal"
    elif bmi < 30:
        # Implicitly: 25 <= bmi < 30
        category = "Overweight"
    else:
        # Implicitly: bmi >= 30
        category = "Obese"

    # Return results as dictionary
    # Round BMI to 2 decimal places for readability
    # round(x, 2) returns float with 2 decimal places
    return {
        'bmi': round(bmi, 2),
        'category': category,
    }


# =============================================================================
# BONUS: ALTERNATIVE IMPLEMENTATIONS
# =============================================================================

def format_person_info_old_style(name: str, age: int, height: float) -> str:
    """
    Alternative implementation using % formatting (old style).

    Included for educational purposes to show evolution of Python string
    formatting. DO NOT USE THIS in new code—use f-strings instead!

    Args:
        name: Person's name
        age: Person's age
        height: Person's height

    Returns:
        str: Formatted string

    Example:
        >>> format_person_info_old_style("Alice", 30, 1.65)
        'Alice is 30 years old and 1.65 meters tall.'

    Notes:
        % FORMATTING (Python 2 style):
        - %s : string
        - %d : integer
        - %f : float
        - %.2f : float with 2 decimal places

        PROBLEMS:
        - Less readable than f-strings
        - Slower (creates temporary tuple)
        - Error-prone (easy to mismatch types)

        HISTORICAL NOTE:
        Borrowed from C's printf()
        Still used in logging: logger.debug("x=%d", x)
    """
    # % formatting creates a tuple on the right side
    # Then formats according to % specifiers on the left
    return "%s is %d years old and %s meters tall." % (name, age, height)


def format_person_info_format_method(name: str, age: int, height: float) -> str:
    """
    Alternative implementation using .format() method (Python 2.6+).

    More powerful than % formatting, but slower than f-strings.

    Args:
        name: Person's name
        age: Person's age
        height: Person's height

    Returns:
        str: Formatted string

    Example:
        >>> format_person_info_format_method("Alice", 30, 1.65)
        'Alice is 30 years old and 1.65 meters tall.'

    Notes:
        .format() FEATURES:
        - Positional: "{} {}".format(a, b)
        - Named: "{name} {age}".format(name="Alice", age=30)
        - Indexed: "{0} {1} {0}".format(a, b)
        - Format specs: "{:.2f}".format(3.14159)

        ADVANTAGE OVER %:
        - More readable, flexible

        DISADVANTAGE VS F-STRINGS:
        - Slower (method call overhead)
        - Less concise
    """
    return "{} is {} years old and {} meters tall.".format(name, age, height)


# =============================================================================
# USAGE EXAMPLES
# =============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("Project 01: Basic Python Syntax - SOLUTION")
    print("=" * 70)

    # Example 1: Types
    print("\n--- Example 1: Basic Types ---")
    types_dict = explore_types()
    for var_name, var_type in types_dict.items():
        print(f"{var_name:15} → {var_type}")

    # Example 2: Arithmetic
    print("\n--- Example 2: Arithmetic Operations ---")
    results = perform_arithmetic(10, 3)
    print(f"10 + 3  = {results['addition']}")
    print(f"10 - 3  = {results['subtraction']}")
    print(f"10 * 3  = {results['multiplication']}")
    print(f"10 / 3  = {results['division']:.4f}")
    print(f"10 // 3 = {results['floor_division']}")
    print(f"10 % 3  = {results['modulo']}")
    print(f"10 ** 3 = {results['exponentiation']}")

    # Example 3: Type Conversion
    print("\n--- Example 3: Type Conversion ---")
    print(f"safe_int_convert('42') = {safe_int_convert('42')}")
    print(f"safe_int_convert('hello', -1) = {safe_int_convert('hello', -1)}")
    print(f"convert_to_float('3.14') = {convert_to_float('3.14')}")
    print(f"convert_to_float(42) = {convert_to_float(42)}")

    # Example 4: String Formatting
    print("\n--- Example 4: String Formatting ---")
    info = format_person_info("Alice", 30, 1.65)
    print(info)

    # Example 5: Boolean Logic
    print("\n--- Example 5: Boolean Properties ---")
    for n in [5, 42, 150, -10]:
        props = check_number_properties(n)
        print(f"\nProperties of {n}:")
        for prop, value in props.items():
            print(f"  {prop:15} : {value}")

    # Example 6: Assignment & Swapping
    print("\n--- Example 6: Variable Assignment ---")
    a, b, c = demonstrate_assignment()
    print(f"After operations: a={a}, b={b}, c={c}")

    # Example 7: Comparison
    print("\n--- Example 7: Value vs Identity ---")
    test_cases = [
        (42, 42),
        (42, "42"),
        (257, 257),  # Not interned (> 256)
    ]
    for x, y in test_cases:
        comp = compare_values(x, y)
        print(f"\ncompare_values({x!r}, {y!r}):")
        for key, value in comp.items():
            print(f"  {key:20} : {value}")

    # Example 8: BMI Calculator
    print("\n--- Example 8: BMI Calculator ---")
    test_weights = [50, 70, 90, 110]
    height = 1.75
    for weight in test_weights:
        result = calculate_bmi(weight, height)
        print(f"Weight: {weight:3}kg, Height: {height}m → "
              f"BMI: {result['bmi']:5.2f} ({result['category']})")

    # Example 9: Error Handling
    print("\n--- Example 9: Error Handling ---")
    try:
        calculate_bmi(-70, 1.75)
    except ValueError as e:
        print(f"Caught error: {e}")

    # Example 10: Memory & Identity
    print("\n--- Example 10: Integer Interning ---")
    a = 256
    b = 256
    print(f"a = {a}, b = {b}")
    print(f"a == b : {a == b}")
    print(f"a is b : {a is b}  (cached)")

    a = 257
    b = 257
    print(f"\na = {a}, b = {b}")
    print(f"a == b : {a == b}")
    print(f"a is b : {a is b}  (not cached)")

    print("\n" + "=" * 70)
    print("All examples completed successfully!")
    print("Run tests with: pytest test/test_project_01.py -v")
    print("=" * 70)
