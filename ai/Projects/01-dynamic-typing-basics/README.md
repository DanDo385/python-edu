# Project 01: Dynamic Typing Basics

[![Difficulty](https://img.shields.io/badge/Difficulty-Beginner-green.svg)](../../README.md)
[![Concepts](https://img.shields.io/badge/Concepts-Dynamic%20Typing%2C%20Type%20Hints-blue.svg)](../../README.md)

## 🎯 Overview

**Dynamic Typing** is one of Python's most powerful and distinctive features. Unlike statically-typed languages (C++, Java), Python determines variable types at runtime, offering flexibility and rapid development at the cost of some type safety. This project explores Python's type system fundamentals, critical for modern AI/ML development where type hints improve code quality and enable better tooling (type checkers, IDEs, documentation generators).

## 🎓 Learning Objectives

By completing this project, you will:
- Understand dynamic vs static typing trade-offs
- Master Python's runtime type system and introspection
- Use type hints effectively (PEP 484, 585, 604)
- Implement duck typing patterns
- Write generic, reusable functions
- Debug type-related issues
- Apply best practices for type annotations in AI/ML code

## 📚 Background

### What is Dynamic Typing?

**Dynamic Typing**: Type checking happens at **runtime**, not compile-time.
- Variables don't have fixed types—they can hold any type
- Type errors discovered during execution
- More flexible, but less safe than static typing

**Static Typing** (C++, Java, Rust): Type checking at **compile-time**.
- Variables have fixed types declared upfront
- Type errors caught before running
- Less flexible, but safer

**Python's Approach**: Dynamic typing + optional static type hints (best of both worlds!)

### Type System Concepts

1. **Duck Typing**: "If it walks like a duck and quacks like a duck, it's a duck"
   - Focus on behavior (methods/attributes) rather than explicit type
   - Enables polymorphism without inheritance

2. **Type Inference**: Determining types from context/usage
   - Modern type checkers (mypy, pyright) can infer types
   - Reduces need for explicit annotations

3. **Type Hints (Annotations)**: Optional type information
   - Added in Python 3.5+ (PEP 484)
   - Checked by external tools (mypy), not runtime
   - Improves IDE autocomplete, documentation, debugging

4. **Generic Types**: Types parameterized by other types
   - `List[int]`, `Dict[str, float]`, `Optional[str]`
   - Enables writing reusable, type-safe code

## 💻 Problems

Implement the following functions in `solution/solution.py`:

### Problem 1: Type Checker at Runtime

Create a function that inspects and reports variable types at runtime.

```python
def inspect_type(obj: Any) -> Dict[str, Any]
```

**Examples:**
```python
inspect_type(42)
# Returns: {
#     'value': 42,
#     'type': <class 'int'>,
#     'type_name': 'int',
#     'is_mutable': False,
#     'methods': ['__add__', '__sub__', ...]
# }

inspect_type([1, 2, 3])
# Returns: {
#     'value': [1, 2, 3],
#     'type': <class 'list'>,
#     'type_name': 'list',
#     'is_mutable': True,
#     'methods': ['append', 'extend', ...]
# }
```

**Requirements:**
- Return type information as a dictionary
- Include: value, type object, type name, mutability, available methods
- Handle any Python object

---

### Problem 2: Duck Typing Implementation

Demonstrate duck typing by creating functions that work with any "file-like" or "iterable" object.

```python
def count_lines(file_like: Any) -> int
def sum_all(iterable: Any) -> float
```

**Examples:**
```python
# Works with real file
with open('data.txt') as f:
    count_lines(f)  # Returns number of lines

# Works with StringIO (file-like)
from io import StringIO
count_lines(StringIO("line1\nline2\nline3"))  # Returns 3

# Works with list, tuple, set, generator...
sum_all([1, 2, 3])        # Returns 6
sum_all((1.5, 2.5, 3.5))  # Returns 7.5
sum_all(range(10))        # Returns 45
```

**Requirements:**
- Use duck typing (check behavior, not type)
- Work with any object that has the right interface
- Gracefully handle objects without required interface

---

### Problem 3: Type Annotation Examples

Create properly type-annotated functions demonstrating modern Python typing.

```python
def process_data(
    numbers: List[int],
    operation: Callable[[int], int],
    default: Optional[int] = None
) -> Dict[str, Union[int, float]]
```

**Examples:**
```python
def double(x: int) -> int:
    return x * 2

result = process_data([1, 2, 3, 4], double)
# Returns: {'sum': 20, 'average': 5.0, 'count': 4}

result = process_data([], double, default=0)
# Returns: {'sum': 0, 'average': 0.0, 'count': 0}
```

**Requirements:**
- Use modern type hints: `List`, `Dict`, `Optional`, `Union`, `Callable`
- Handle edge cases (empty input, None values)
- Return structured data with statistics

---

### Problem 4: Generic Functions

Create generic functions that work with multiple types while preserving type safety.

```python
def get_first_and_last(items: List[T]) -> Tuple[T, T]
def safe_divide(a: Union[int, float], b: Union[int, float]) -> Optional[float]
```

**Examples:**
```python
get_first_and_last([1, 2, 3, 4, 5])
# Returns: (1, 5)

get_first_and_last(["a", "b", "c"])
# Returns: ("a", "c")

safe_divide(10, 2)     # Returns: 5.0
safe_divide(5, 0)      # Returns: None
safe_divide(7.5, 2.5)  # Returns: 3.0
```

**Requirements:**
- Use `TypeVar` for generic types
- Handle different numeric types (`int`, `float`)
- Safe operations (no crashes on division by zero)

---

### Problem 5: Type Inference Demonstration

Create a function that demonstrates how Python infers types dynamically.

```python
def demonstrate_type_flexibility() -> List[Tuple[str, str, str]]
```

**Examples:**
```python
result = demonstrate_type_flexibility()
# Returns list of tuples showing:
# [
#     ('x = 5', 'int', 'x = "hello" changes to str'),
#     ('y = [1, 2]', 'list', 'y.append(3) modifies list'),
#     ...
# ]
```

**Requirements:**
- Show how variables can change type
- Demonstrate mutable vs immutable types
- Return explanatory examples as data

## 🧪 Testing

Run the comprehensive test suite:

```bash
# Run all tests
pytest tests/test_project_01.py -v

# Run specific test class
pytest tests/test_project_01.py::TestInspectType -v

# Run with type checking (if mypy installed)
mypy solution/solution.py

# Run with coverage
pytest tests/test_project_01.py --cov=solution --cov-report=html
```

## 📊 Type System Comparison

| Feature | Python (Dynamic) | Java (Static) | TypeScript |
|---------|-----------------|---------------|------------|
| Type checking | Runtime | Compile-time | Compile-time |
| Type annotations | Optional | Required | Required |
| Variable rebinding | Any type | Same type only | Same type |
| Duck typing | Yes | No (interfaces) | Structural |
| Development speed | Fast | Slower | Medium |
| Runtime safety | Lower | Higher | Medium |
| Best for | Prototyping, ML/AI | Enterprise, Android | Web frontend |

## 💡 Real-World Applications

### AI/ML Context

Dynamic typing is **essential** in modern AI/ML:

1. **Flexible Data Pipelines**: Handle various input formats (arrays, tensors, dataframes)
2. **Rapid Prototyping**: Quickly test ideas without boilerplate
3. **Type Hints for Large Projects**: Teams use type hints for maintainability
4. **Tool Integration**: Type checkers catch bugs in complex ML pipelines

Example from ML:
```python
# Type hints make ML code more maintainable
def train_model(
    X: np.ndarray,
    y: np.ndarray,
    model: Optional[BaseEstimator] = None,
    **kwargs: Any
) -> BaseEstimator:
    """Train ML model with type-safe interface."""
    ...
```

## 🔍 Key Concepts

### 1. Runtime Type Checking
```python
# Type determined at runtime
x = 5          # int
x = "hello"    # Now str - perfectly valid!

# Check types dynamically
if isinstance(x, str):
    print(x.upper())
```

### 2. Type Hints Don't Enforce at Runtime
```python
def add(a: int, b: int) -> int:
    return a + b

# This still works! Type hints are just hints
add("hello", "world")  # Returns "helloworld"
```

### 3. Duck Typing in Action
```python
# Works with anything iterable
def process(items):
    for item in items:  # Duck typing: has __iter__?
        print(item)

process([1, 2, 3])        # list
process("abc")            # str
process(range(5))         # range
process({1, 2, 3})        # set
```

## 📝 Best Practices

1. **Use Type Hints in Public APIs**: Helps users understand expected types
2. **Don't Over-Annotate**: Internal variables often don't need hints
3. **Use `mypy` or `pyright`**: Catch type errors before runtime
4. **Prefer `list[int]` over `List[int]`**: Modern Python 3.9+ syntax
5. **Use `Optional[T]` for nullable values**: Makes None explicit
6. **Document complex types**: Use TypeAlias for readability

## 🔗 Related Concepts

- **Static Analysis** (Project 02)
- **Protocol Classes** (Project 08)
- **Decorators & Metaclasses** (Projects 12-13)
- **Type Narrowing** (Project 15)

## 📖 References

- [PEP 484 - Type Hints](https://www.python.org/dev/peps/pep-0484/)
- [PEP 585 - Type Hinting Generics](https://www.python.org/dev/peps/pep-0585/)
- [Python typing module docs](https://docs.python.org/3/library/typing.html)
- [mypy Documentation](https://mypy.readthedocs.io/)

---

**Estimated Time:** 2-3 hours
**Difficulty:** ⭐ Beginner
**Prerequisites:** Basic Python syntax, functions, data structures
