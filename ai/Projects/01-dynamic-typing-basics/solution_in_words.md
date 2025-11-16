# Project 01: Dynamic Typing Basics - Solution Explained

## Concept Overview

### What is Dynamic Typing?

**Dynamic typing** is a fundamental characteristic of Python's type system where type checking occurs at **runtime** rather than compile-time. This means:

1. **Variables don't have fixed types** - A variable can hold an integer, then be reassigned to a string
2. **Types are associated with values, not variables** - The value 42 is an integer, but the variable holding it isn't restricted to integers
3. **Type errors are discovered during execution** - You won't know about type mismatches until the code runs
4. **Maximum flexibility** - Rapid prototyping and less boilerplate code

### Static vs Dynamic Typing

| Aspect | Static (Java, C++) | Dynamic (Python, JavaScript) |
|--------|-------------------|------------------------------|
| **Type checking** | Compile-time | Runtime |
| **Variable declaration** | `int x = 5;` (type required) | `x = 5` (type inferred) |
| **Type changes** | Not allowed | Allowed freely |
| **Error detection** | Before running | During execution |
| **Development speed** | Slower (more upfront work) | Faster (less ceremony) |
| **Runtime safety** | Higher | Lower |
| **Refactoring** | Easier (compiler helps) | Harder (need good tests) |

**Python's Modern Approach**: Dynamic typing at runtime + optional type hints for static analysis tools (mypy, pyright). Best of both worlds!

## Core Concepts

### 1. Runtime Type Introspection

Python provides powerful tools to inspect types at runtime:

```python
x = [1, 2, 3]

# Get type information
type(x)                    # <class 'list'>
type(x).__name__           # 'list'
isinstance(x, list)        # True
dir(x)                     # All attributes/methods
hasattr(x, 'append')       # True - check for specific method
```

**Implementation in `inspect_type()`**:
- Uses `type()` to get the type object
- Extracts type name via `__name__` attribute
- Determines mutability by checking against known immutable types
- Uses `dir()` to list all methods and attributes
- Filters to show only public methods for clarity

**Why this matters for AI/ML**:
- Debug data pipelines by inspecting tensor/array types
- Validate input data at runtime
- Build flexible data processing pipelines that adapt to input types

### 2. Duck Typing

**"If it walks like a duck and quacks like a duck, it's a duck."**

Duck typing focuses on **behavior** (what methods an object has) rather than **type** (what class it is):

```python
# Traditional type checking (NOT duck typing)
def process_file(f: io.TextIOWrapper):
    if not isinstance(f, io.TextIOWrapper):
        raise TypeError("Must be a file!")
    return f.read()

# Duck typing (Pythonic)
def process_file_like(f):
    # Don't check type, just try to use it
    try:
        return f.read()
    except AttributeError:
        raise TypeError("Object doesn't support read()")
```

**Implementation in `count_lines()` and `sum_all()`**:
- Never check `isinstance()` for specific types
- Simply try to iterate (`for item in iterable`)
- If iteration fails, catch `TypeError` and provide helpful message
- Works with files, StringIO, lists, tuples, generators, etc.

**Benefits**:
- More flexible and reusable code
- Works with any object implementing the protocol
- No inheritance required
- Encourages interface-based design

**Real-world ML example**:
```python
def fit_model(data):
    # Works with numpy arrays, pandas DataFrames,
    # PyTorch tensors, or any iterable!
    for batch in data:
        process(batch)
```

### 3. Type Hints (Annotations)

Type hints are **optional** metadata added to function signatures:

```python
def greet(name: str) -> str:
    return f"Hello, {name}!"
```

**Key points**:
1. **Not enforced at runtime** - Python ignores them during execution
2. **Used by static analyzers** - Tools like mypy check types before running
3. **Improve IDE support** - Better autocomplete and error detection
4. **Self-documenting** - Clear what types are expected

**Common type hint patterns**:

```python
from typing import List, Dict, Optional, Union, Callable, Any

# Basic types
def add(a: int, b: int) -> int: ...

# Collections
def process(items: List[str]) -> Dict[str, int]: ...

# Optional (can be None)
def find(name: str) -> Optional[User]: ...

# Union (multiple possible types)
def format(value: Union[int, float, str]) -> str: ...

# Callable (function parameter)
def apply(data: List[int], func: Callable[[int], int]) -> List[int]: ...

# Any (any type allowed)
def debug(obj: Any) -> None: ...
```

**Implementation in `process_data()`**:
- Demonstrates modern type annotations
- `List[int]` - list of integers
- `Callable[[int], int]` - function taking int, returning int
- `Optional[int]` - either int or None
- `Dict[str, Union[int, float]]` - dict with str keys, int/float values

**Why type hints matter in AI/ML**:
```python
# Clear, self-documenting ML code
def train_model(
    X_train: np.ndarray,
    y_train: np.ndarray,
    model: Optional[BaseEstimator] = None,
    epochs: int = 100,
    learning_rate: float = 0.001
) -> Tuple[BaseEstimator, Dict[str, float]]:
    """Type hints make complex ML pipelines maintainable."""
    ...
```

### 4. Generic Types with TypeVar

Generics allow writing type-safe reusable functions:

```python
from typing import TypeVar, List, Tuple

T = TypeVar('T')  # "T can be any type"

def get_first_and_last(items: List[T]) -> Tuple[T, T]:
    return (items[0], items[-1])

# Type checker knows:
result1 = get_first_and_last([1, 2, 3])      # Tuple[int, int]
result2 = get_first_and_last(["a", "b"])     # Tuple[str, str]
```

**How it works**:
- `T` is a placeholder for "some type"
- Type checker infers `T` from the input
- Ensures output type matches input type
- All without runtime overhead!

**Implementation in `get_first_and_last()`**:
- Uses `TypeVar('T')` to represent generic type
- Input is `List[T]` - list of some type
- Output is `Tuple[T, T]` - tuple of that same type
- Type checker validates consistency

### 5. Union and Optional Types

**Union** - value can be one of several types:
```python
def process(value: Union[int, float]) -> float:
    return float(value)
```

**Optional** - shorthand for `Union[T, None]`:
```python
# These are equivalent:
def find(name: str) -> Optional[User]: ...
def find(name: str) -> Union[User, None]: ...
```

**Implementation in `safe_divide()`**:
- Parameters: `Union[int, float]` - accept both numeric types
- Return: `Optional[float]` - returns float or None (on division by zero)
- Demonstrates safe error handling without exceptions

## Problem-Solving Approach

### Problem 1: Type Inspection

**Challenge**: Inspect any Python object's type at runtime

**Approach**:
1. Use `type()` to get type object
2. Extract human-readable type name
3. Classify mutability (immutable: int, str, tuple; mutable: list, dict, set)
4. Enumerate methods using `dir()`
5. Filter for useful public methods

**Key insight**: Python's introspection capabilities enable building debugging tools, validators, and type-aware utilities.

### Problem 2: Duck Typing

**Challenge**: Write functions that work with any compatible type

**Approach**:
1. Don't check types - check capabilities
2. Try to use the object's interface
3. Catch exceptions gracefully
4. Provide clear error messages

**Key insight**: Focus on "can it iterate?" not "is it a list?". This makes code more reusable.

### Problem 3: Type Annotations

**Challenge**: Document expected types without breaking dynamic typing

**Approach**:
1. Add type hints to function signatures
2. Use descriptive types (`List[int]`, not just `list`)
3. Use `Optional` for nullable values
4. Use `Union` when multiple types are valid
5. Use `Callable` for function parameters

**Key insight**: Type hints are documentation + static checking, not runtime enforcement.

### Problem 4: Generic Functions

**Challenge**: Write type-safe reusable functions

**Approach**:
1. Define `TypeVar` for placeholder type
2. Use TypeVar in function signature
3. Let type checker infer concrete types
4. Maintain type consistency (input type = output type)

**Key insight**: Generics provide type safety without sacrificing reusability.

### Problem 5: Type Flexibility

**Challenge**: Demonstrate dynamic typing advantages and pitfalls

**Approach**:
1. Show variable type changes (dynamic)
2. Demonstrate mutable vs immutable behavior
3. Show how type determines operations (+ means different things)
4. Illustrate duck typing with different types

**Key insight**: Dynamic typing offers flexibility but requires discipline and testing.

## Best Practices

### 1. When to Use Type Hints

**DO use type hints for**:
- Public API functions
- Complex function signatures
- Functions with many parameters
- Large codebases with multiple developers
- ML pipelines with complex data flows

**DON'T over-annotate**:
- Simple, obvious functions
- Internal helper functions
- Variables (usually inferred)
- One-off scripts

### 2. Choosing Between isinstance() and Duck Typing

**Use `isinstance()`** when:
- You need specific type behavior
- Type affects algorithm choice
- Safety is critical

**Use duck typing** when:
- You want maximum flexibility
- You're defining protocols/interfaces
- You want to work with any compatible type

### 3. Modern Type Hint Syntax (Python 3.9+)

```python
# Old style (Python 3.5-3.8)
from typing import List, Dict, Tuple
def process(items: List[int]) -> Dict[str, int]:
    ...

# New style (Python 3.9+)
def process(items: list[int]) -> dict[str, int]:
    ...

# Use lowercase built-in types!
```

### 4. Handling Optional Values

```python
# Bad - unclear
def find_user(id: int):
    ...

# Good - explicit about None
def find_user(id: int) -> Optional[User]:
    ...

# Usage with type narrowing
user = find_user(123)
if user is not None:
    # Type checker knows user is User here
    print(user.name)
```

## Common Pitfalls

### 1. Assuming Type Hints Are Enforced

```python
def add(a: int, b: int) -> int:
    return a + b

# This still works! Type hints not enforced at runtime
add("hello", "world")  # Returns "helloworld"
```

**Solution**: Use mypy or pyright for static type checking

### 2. Over-Specifying Types

```python
# Too specific - limits reusability
def process_list(items: list) -> None:
    for item in items:
        print(item)

# Better - works with any iterable
from typing import Iterable
def process_items(items: Iterable) -> None:
    for item in items:
        print(item)
```

### 3. Mutable Default Arguments

```python
# DANGEROUS - list is shared across calls!
def add_item(item: int, items: List[int] = []) -> List[int]:
    items.append(item)
    return items

# Safe - use None and create new list
def add_item(item: int, items: Optional[List[int]] = None) -> List[int]:
    if items is None:
        items = []
    items.append(item)
    return items
```

### 4. Type Confusion with Numeric Types

```python
# Division always returns float in Python 3
x: int = 10 / 2  # Type error! Result is 5.0 (float)

# Use floor division for int
x: int = 10 // 2  # OK! Result is 5 (int)
```

## Complexity Analysis

### Time Complexity

| Function | Time Complexity | Explanation |
|----------|----------------|-------------|
| `inspect_type()` | O(n) | n = number of attributes/methods |
| `count_lines()` | O(n) | n = number of lines |
| `sum_all()` | O(n) | n = number of elements |
| `process_data()` | O(n) | n = length of input list |
| `get_first_and_last()` | O(1) | Direct index access |
| `safe_divide()` | O(1) | Single arithmetic operation |
| `demonstrate_type_flexibility()` | O(1) | Fixed number of examples |

### Space Complexity

| Function | Space Complexity | Explanation |
|----------|-----------------|-------------|
| `inspect_type()` | O(n) | Stores list of n methods |
| `count_lines()` | O(1) | Only counter variable |
| `sum_all()` | O(1) | Only sum accumulator |
| `process_data()` | O(n) | Creates processed list |
| `get_first_and_last()` | O(1) | Only tuple with references |
| `safe_divide()` | O(1) | Only result value |
| `demonstrate_type_flexibility()` | O(1) | Fixed-size list |

## Real-World Applications in AI/ML

### 1. Flexible Data Pipelines

```python
def preprocess(data: Union[np.ndarray, pd.DataFrame, List]) -> np.ndarray:
    """Works with multiple input formats."""
    if isinstance(data, pd.DataFrame):
        return data.values
    elif isinstance(data, list):
        return np.array(data)
    return data
```

### 2. Generic Model Training

```python
from typing import TypeVar, Protocol

T = TypeVar('T')

class Model(Protocol):
    def fit(self, X, y) -> None: ...
    def predict(self, X) -> np.ndarray: ...

def train_and_evaluate(
    model: Model,
    X_train: np.ndarray,
    y_train: np.ndarray,
    X_test: np.ndarray
) -> Dict[str, float]:
    """Works with any model implementing fit/predict."""
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    return compute_metrics(predictions, y_test)
```

### 3. Type-Safe Configuration

```python
from typing import Dict, Any, Optional
from dataclasses import dataclass

@dataclass
class ModelConfig:
    learning_rate: float
    epochs: int
    batch_size: int
    optimizer: str = 'adam'
    early_stopping: Optional[int] = None

def load_config(path: str) -> ModelConfig:
    """Type-safe config loading."""
    data: Dict[str, Any] = json.load(open(path))
    return ModelConfig(**data)
```

## Key Takeaways

1. **Dynamic typing offers flexibility** - Variables can change types, enabling rapid prototyping

2. **Type hints improve maintainability** - Use them in public APIs and complex codebases

3. **Duck typing enables reusability** - Focus on behavior, not type hierarchy

4. **Generics provide type safety** - Write once, use with many types

5. **Runtime introspection is powerful** - Build debugging and validation tools

6. **Balance flexibility and safety** - Use type hints + mypy for large projects, embrace dynamic typing for scripts

7. **Modern Python = dynamic + static** - Get runtime flexibility AND compile-time checking

8. **Critical for AI/ML** - Type hints make complex data pipelines maintainable and debuggable

## Further Reading

- [PEP 484 - Type Hints](https://www.python.org/dev/peps/pep-0484/)
- [PEP 585 - Type Hinting Generics](https://www.python.org/dev/peps/pep-0585/)
- [PEP 604 - Union Types (X | Y)](https://www.python.org/dev/peps/pep-0604/)
- [mypy Documentation](https://mypy.readthedocs.io/)
- [Python typing module](https://docs.python.org/3/library/typing.html)
- [Real Python: Type Checking](https://realpython.com/python-type-checking/)

## Next Steps

After mastering dynamic typing basics, explore:

- **Project 02**: Static analysis with mypy/pyright
- **Project 08**: Protocol classes (structural subtyping)
- **Project 12**: Decorators and type preservation
- **Project 15**: Type narrowing and type guards
- **Advanced topics**: TypedDict, Literal types, overload, ParamSpec
