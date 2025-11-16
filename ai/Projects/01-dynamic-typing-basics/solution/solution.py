"""
Project 01: Dynamic Typing Basics

This module demonstrates Python's dynamic type system, including runtime type
checking, duck typing, type hints, and generic programming patterns essential
for modern AI/ML development.

Key Concepts:
- Dynamic typing vs static typing
- Runtime type introspection
- Duck typing (structural subtyping)
- Type hints and annotations (PEP 484)
- Generic types and TypeVar
- Optional types and Union types

Author: Python-Edu AI Curriculum
"""

from typing import Any, Dict, List, Tuple, Optional, Union, Callable, TypeVar
from io import StringIO

# Generic type variable for polymorphic functions
T = TypeVar('T')


def inspect_type(obj: Any) -> Dict[str, Any]:
    """
    Inspect and report comprehensive type information about any Python object.

    This function demonstrates Python's runtime type introspection capabilities,
    a key feature of dynamic typing. Unlike static languages, Python allows
    examining object types at runtime using built-in functions like type(),
    isinstance(), and dir().

    Algorithm:
    1. Get the type using type(obj)
    2. Extract type name from type object
    3. Determine mutability (immutable: int, str, tuple; mutable: list, dict, set)
    4. Get all methods/attributes using dir()
    5. Filter to show public methods (exclude __private__)
    6. Return structured information dictionary

    Args:
        obj: Any Python object to inspect

    Returns:
        Dictionary containing:
        - 'value': The original object
        - 'type': Type object (e.g., <class 'int'>)
        - 'type_name': String name of type (e.g., 'int')
        - 'is_mutable': Boolean indicating mutability
        - 'methods': List of public method names

    Time Complexity: O(n) where n is number of attributes
    Space Complexity: O(n) for storing methods list

    Examples:
        >>> result = inspect_type(42)
        >>> result['type_name']
        'int'
        >>> result['is_mutable']
        False

        >>> result = inspect_type([1, 2, 3])
        >>> result['type_name']
        'list'
        >>> result['is_mutable']
        True
        >>> 'append' in result['methods']
        True
    """
    # Get type information
    obj_type = type(obj)
    type_name = obj_type.__name__

    # Determine mutability based on common Python types
    # Immutable: int, float, str, tuple, frozenset, bytes, bool, NoneType
    # Mutable: list, dict, set, bytearray, and most user-defined objects
    immutable_types = (int, float, str, tuple, frozenset, bytes, bool, type(None))
    is_mutable = not isinstance(obj, immutable_types)

    # Get all attributes and methods
    all_attributes = dir(obj)

    # Filter to get public methods (exclude private/dunder methods for readability)
    # Include some useful dunder methods
    important_dunders = {
        '__init__', '__str__', '__repr__', '__len__', '__iter__',
        '__add__', '__sub__', '__mul__', '__truediv__'
    }

    public_methods = [
        attr for attr in all_attributes
        if not attr.startswith('_') or attr in important_dunders
    ]

    return {
        'value': obj,
        'type': obj_type,
        'type_name': type_name,
        'is_mutable': is_mutable,
        'methods': public_methods
    }


def count_lines(file_like: Any) -> int:
    """
    Count lines in any file-like object using duck typing.

    This demonstrates "duck typing": we don't check if the object IS a file,
    we check if it BEHAVES like a file (has readline or iteration capability).

    "If it walks like a duck and quacks like a duck, it's a duck."

    Duck typing enables:
    - Writing flexible, reusable code
    - Working with multiple types without inheritance
    - Focusing on behavior rather than type hierarchy

    Algorithm:
    1. Try to iterate over object (check for __iter__)
    2. Count each line during iteration
    3. If not iterable, raise clear error

    Args:
        file_like: Any object that supports iteration over lines
                  (file, StringIO, list of strings, etc.)

    Returns:
        Number of lines in the file-like object

    Raises:
        TypeError: If object doesn't support iteration

    Time Complexity: O(n) where n is number of lines
    Space Complexity: O(1) - only counting, not storing lines

    Examples:
        >>> from io import StringIO
        >>> count_lines(StringIO("line1\\nline2\\nline3"))
        3

        >>> count_lines(["hello", "world"])
        2

        >>> # Would work with real file too:
        >>> # with open('data.txt') as f:
        >>> #     count_lines(f)
    """
    try:
        # Duck typing: try to iterate, don't check type
        count = 0
        for _ in file_like:
            count += 1
        return count
    except TypeError as e:
        raise TypeError(
            f"Object of type {type(file_like).__name__} is not iterable. "
            f"Expected file-like object with iteration support."
        ) from e


def sum_all(iterable: Any) -> float:
    """
    Sum all numeric elements in any iterable using duck typing.

    Works with lists, tuples, sets, generators, ranges, etc.
    Demonstrates how duck typing enables writing generic algorithms
    that work across many types without explicit type checking.

    Algorithm:
    1. Initialize sum to 0
    2. Try to iterate over elements
    3. Add each element to sum (converts int to float for consistency)
    4. Return total

    Args:
        iterable: Any iterable containing numeric values

    Returns:
        Sum of all elements as float

    Raises:
        TypeError: If object is not iterable or contains non-numeric values

    Time Complexity: O(n) where n is number of elements
    Space Complexity: O(1) - only storing sum

    Examples:
        >>> sum_all([1, 2, 3, 4, 5])
        15.0

        >>> sum_all((1.5, 2.5, 3.0))
        7.0

        >>> sum_all(range(10))
        45.0

        >>> sum_all({1, 2, 3})  # Even works with sets
        6.0
    """
    try:
        total = 0.0
        for item in iterable:
            total += float(item)
        return total
    except TypeError as e:
        if not hasattr(iterable, '__iter__'):
            raise TypeError(
                f"Object of type {type(iterable).__name__} is not iterable."
            ) from e
        else:
            raise TypeError(
                f"Cannot convert element to numeric value: {item}"
            ) from e


def process_data(
    numbers: List[int],
    operation: Callable[[int], int],
    default: Optional[int] = None
) -> Dict[str, Union[int, float]]:
    """
    Process a list of numbers with type-annotated parameters.

    This function demonstrates modern Python type hints:
    - List[int]: List containing integers
    - Callable[[int], int]: Function taking int, returning int
    - Optional[int]: Either int or None
    - Dict[str, Union[int, float]]: Dict with str keys, int or float values

    Type hints provide:
    1. IDE autocomplete and error detection
    2. Documentation of expected types
    3. Static type checking with mypy/pyright
    4. Better code maintainability

    Note: Type hints are NOT enforced at runtime in Python!

    Algorithm:
    1. Handle empty list case with default value
    2. Apply operation to each number
    3. Calculate statistics (sum, average, count)
    4. Return structured results

    Args:
        numbers: List of integers to process
        operation: Function to apply to each number
        default: Default value if list is empty (None uses 0)

    Returns:
        Dictionary with keys:
        - 'sum': Sum of processed numbers (int)
        - 'average': Average of processed numbers (float)
        - 'count': Number of elements processed (int)

    Time Complexity: O(n) where n is length of numbers list
    Space Complexity: O(n) for processed list

    Examples:
        >>> def double(x: int) -> int:
        ...     return x * 2
        >>> process_data([1, 2, 3, 4], double)
        {'sum': 20, 'average': 5.0, 'count': 4}

        >>> process_data([], double, default=0)
        {'sum': 0, 'average': 0.0, 'count': 0}

        >>> def square(x: int) -> int:
        ...     return x * x
        >>> process_data([2, 3, 4], square)
        {'sum': 29, 'average': 9.666666666666666, 'count': 3}
    """
    # Handle empty list case
    if not numbers:
        default_val = default if default is not None else 0
        return {
            'sum': default_val,
            'average': 0.0,
            'count': 0
        }

    # Apply operation to each number
    processed = [operation(num) for num in numbers]

    # Calculate statistics
    total = sum(processed)
    count = len(processed)
    average = total / count

    return {
        'sum': total,
        'average': average,
        'count': count
    }


def get_first_and_last(items: List[T]) -> Tuple[T, T]:
    """
    Get first and last elements from a list, preserving type with generics.

    This demonstrates generic programming with TypeVar:
    - Input type List[T] means "list of some type T"
    - Output type Tuple[T, T] means "tuple of two items of same type T"
    - Type checker can verify: get_first_and_last([1,2,3]) returns Tuple[int, int]

    Generics enable:
    1. Type-safe reusable code
    2. Better IDE support (knows return type)
    3. Catching type errors at static analysis time

    Args:
        items: List of any type (must have at least 2 elements)

    Returns:
        Tuple containing (first_element, last_element) of same type as input

    Raises:
        ValueError: If list has fewer than 2 elements

    Time Complexity: O(1) - direct index access
    Space Complexity: O(1) - only creating tuple with references

    Examples:
        >>> get_first_and_last([1, 2, 3, 4, 5])
        (1, 5)

        >>> get_first_and_last(["a", "b", "c", "d"])
        ('a', 'd')

        >>> get_first_and_last([3.14, 2.71, 1.41])
        (3.14, 1.41)
    """
    if len(items) < 2:
        raise ValueError(
            f"List must have at least 2 elements, got {len(items)}"
        )

    return (items[0], items[-1])


def safe_divide(
    a: Union[int, float],
    b: Union[int, float]
) -> Optional[float]:
    """
    Safely divide two numbers, returning None on division by zero.

    Demonstrates:
    - Union[int, float]: Parameter can be either int or float
    - Optional[float]: Return value is either float or None
    - Safe operations avoiding exceptions

    This pattern is common in production code where you want to handle
    errors gracefully without exceptions.

    Args:
        a: Numerator (int or float)
        b: Denominator (int or float)

    Returns:
        Result of a/b as float, or None if b is zero

    Time Complexity: O(1) - single division operation
    Space Complexity: O(1) - only storing result

    Examples:
        >>> safe_divide(10, 2)
        5.0

        >>> safe_divide(7, 3)
        2.3333333333333335

        >>> safe_divide(5, 0)

        >>> safe_divide(7.5, 2.5)
        3.0
    """
    if b == 0:
        return None
    return float(a) / float(b)


def demonstrate_type_flexibility() -> List[Tuple[str, str, str]]:
    """
    Demonstrate Python's dynamic typing flexibility.

    Shows how Python variables can:
    1. Change type during execution (dynamic typing)
    2. Be reassigned to different types
    3. Behave differently based on their current type

    This is a key difference from static languages like Java/C++ where
    variables have fixed types.

    Returns:
        List of tuples, each containing:
        (example_code, initial_type, explanation)

    Time Complexity: O(1) - fixed number of examples
    Space Complexity: O(1) - fixed size return list

    Examples:
        >>> examples = demonstrate_type_flexibility()
        >>> len(examples) > 0
        True
        >>> examples[0][1]  # Check type name in first example
        'int'
    """
    examples = []

    # Example 1: Variable type can change
    x = 5
    initial_type = type(x).__name__
    x = "hello"
    new_type = type(x).__name__
    examples.append((
        'x = 5, then x = "hello"',
        initial_type,
        f'Variable changed from {initial_type} to {new_type}'
    ))

    # Example 2: Mutable types can be modified
    y = [1, 2]
    initial_type = type(y).__name__
    y.append(3)
    examples.append((
        'y = [1, 2]; y.append(3)',
        initial_type,
        f'{initial_type} is mutable, modified in-place to {y}'
    ))

    # Example 3: Immutable types create new objects
    z = "hello"
    initial_type = type(z).__name__
    z_upper = z.upper()
    examples.append((
        'z = "hello"; z.upper()',
        initial_type,
        f'{initial_type} is immutable, upper() creates new string "{z_upper}"'
    ))

    # Example 4: Type determines available operations
    a = 5
    b = "5"
    examples.append((
        'a = 5 (int), b = "5" (str)',
        f'{type(a).__name__} vs {type(b).__name__}',
        f'a + a = {a + a}, but b + b = {b + b} (different operations!)'
    ))

    # Example 5: Duck typing with different types
    items = [
        [1, 2, 3],      # list
        (4, 5, 6),      # tuple
        {7, 8, 9},      # set
        range(10, 13)   # range
    ]
    type_names = [type(item).__name__ for item in items]
    examples.append((
        'for item in [list, tuple, set, range]',
        'various',
        f'All iterable despite different types: {type_names}'
    ))

    return examples


# Additional educational functions

def compare_type_systems() -> Dict[str, Dict[str, str]]:
    """
    Compare dynamic vs static typing characteristics.

    Educational function showing key differences between type systems.
    Not part of main problems, but useful for understanding concepts.

    Returns:
        Dictionary comparing Python (dynamic) vs Java (static)
    """
    return {
        'python_dynamic': {
            'type_checking': 'Runtime',
            'type_declaration': 'Optional (type hints)',
            'variable_rebinding': 'Any type allowed',
            'flexibility': 'High',
            'safety': 'Lower (runtime errors)',
            'development_speed': 'Fast',
            'refactoring': 'Harder (no compile-time checks)',
            'best_for': 'Prototyping, ML/AI, scripting'
        },
        'java_static': {
            'type_checking': 'Compile-time',
            'type_declaration': 'Required',
            'variable_rebinding': 'Same type only',
            'flexibility': 'Lower',
            'safety': 'Higher (compile-time checks)',
            'development_speed': 'Slower',
            'refactoring': 'Easier (compiler catches errors)',
            'best_for': 'Enterprise, large systems, Android'
        }
    }


def demonstrate_duck_typing_polymorphism() -> str:
    """
    Demonstrate polymorphism through duck typing.

    Shows how different objects can be used interchangeably if they
    have the same interface (methods), without sharing inheritance.
    """
    # Different classes with same interface (no inheritance!)
    class FileLogger:
        def write(self, message: str) -> None:
            # In real code, would write to file
            print(f"[FILE] {message}")

    class ConsoleLogger:
        def write(self, message: str) -> None:
            print(f"[CONSOLE] {message}")

    class NetworkLogger:
        def write(self, message: str) -> None:
            # In real code, would send over network
            print(f"[NETWORK] {message}")

    # Function works with ANY object that has write() method
    def log_message(logger: Any, message: str) -> None:
        """Duck typing: we don't care about the TYPE, just that it has write()."""
        logger.write(message)

    # All three work, despite being different types!
    result = "Duck typing allows polymorphism without inheritance:\n"
    result += "- FileLogger().write() works\n"
    result += "- ConsoleLogger().write() works\n"
    result += "- NetworkLogger().write() works\n"
    result += "All have write() method, so all work with log_message()"

    return result


if __name__ == "__main__":
    # Demonstration of dynamic typing concepts
    print("=" * 70)
    print("Dynamic Typing Basics - Demonstrations")
    print("=" * 70)

    # 1. Type Inspection
    print("\n1. Type Inspection:")
    print("-" * 70)
    int_info = inspect_type(42)
    print(f"   Integer 42: type={int_info['type_name']}, mutable={int_info['is_mutable']}")

    list_info = inspect_type([1, 2, 3])
    print(f"   List [1,2,3]: type={list_info['type_name']}, mutable={list_info['is_mutable']}")
    print(f"   List methods include: {list_info['methods'][:5]}...")

    # 2. Duck Typing
    print("\n2. Duck Typing:")
    print("-" * 70)
    from io import StringIO

    lines_str = StringIO("line1\nline2\nline3")
    print(f"   Lines in StringIO: {count_lines(lines_str)}")

    lines_list = ["hello", "world", "python"]
    print(f"   Lines in list: {count_lines(lines_list)}")

    print(f"   Sum of [1,2,3,4,5]: {sum_all([1, 2, 3, 4, 5])}")
    print(f"   Sum of range(10): {sum_all(range(10))}")

    # 3. Type Annotations
    print("\n3. Type Annotations:")
    print("-" * 70)

    def triple(x: int) -> int:
        return x * 3

    result = process_data([1, 2, 3, 4], triple)
    print(f"   Triple [1,2,3,4]: {result}")

    result_empty = process_data([], triple, default=0)
    print(f"   Triple empty list: {result_empty}")

    # 4. Generic Functions
    print("\n4. Generic Functions:")
    print("-" * 70)
    int_result = get_first_and_last([10, 20, 30, 40])
    print(f"   First and last of [10,20,30,40]: {int_result}")

    str_result = get_first_and_last(["apple", "banana", "cherry"])
    print(f"   First and last of fruits: {str_result}")

    print(f"   10 / 3 = {safe_divide(10, 3)}")
    print(f"   5 / 0 = {safe_divide(5, 0)} (safely returns None)")

    # 5. Type Flexibility
    print("\n5. Dynamic Type Flexibility:")
    print("-" * 70)
    examples = demonstrate_type_flexibility()
    for code, type_name, explanation in examples[:3]:
        print(f"   {code}")
        print(f"      → {explanation}")

    # 6. Duck Typing Polymorphism
    print("\n6. Duck Typing for Polymorphism:")
    print("-" * 70)
    demo = demonstrate_duck_typing_polymorphism()
    for line in demo.split('\n'):
        print(f"   {line}")

    print("\n" + "=" * 70)
    print("All demonstrations complete!")
    print("=" * 70)
