# Project 01: Basic Python Syntax

> Master variables, types, I/O, and arithmetic—your first Python program

**Difficulty**: ⭐ Beginner
**Phase**: I (Python & Data Structures)
**Prerequisites**: None—start here!
**Time**: 2-3 hours

---

## What You'll Learn

### Core Concepts
- **Variables & Assignment**: Binding names to values, reassignment, multiple assignment
- **Data Types**: int, float, str, bool, None, type checking
- **Type System**: Dynamic typing, duck typing, type hints
- **Arithmetic**: +, -, *, /, //, %, ** operators
- **I/O**: print(), input(), f-strings, formatting
- **Type Conversion**: int(), float(), str(), bool()
- **Operators**: Comparison, logical, identity, membership

### Technical Skills
- Writing executable Python scripts
- Using the interactive REPL
- Reading error messages (TypeError, ValueError)
- Debugging with print statements
- Understanding Python's memory model (references vs values)

### Practical Applications
- Quick calculations and data transformations
- Command-line scripts
- Data validation and sanitization
- Configuration file parsing
- Interactive tools

### Prerequisites
- **None!** This is project #1—absolute beginner-friendly
- Recommended: Installed Python 3.12+ and a text editor

---

## Why This Matters

### Python's Type System is Unique

Unlike statically-typed languages (C, Java, Rust), Python uses **dynamic typing**:

```python
# Python: Variables can change types
x = 42        # x is an int
x = "hello"   # Now x is a str (totally valid!)

# C/Java: This would be a compile error
// int x = 42;
// x = "hello";  // ERROR: incompatible types
```

**Why this matters**:
- ✅ **Faster prototyping**: No type declarations needed
- ✅ **More flexible**: Duck typing enables powerful patterns
- ❌ **Runtime errors**: Type mismatches only caught when code runs
- ❌ **Harder to debug**: No compile-time checks

**Production solution**: Use **type hints** (PEP 484) + mypy for static analysis:
```python
def add(a: int, b: int) -> int:
    return a + b
```

### Real-World Applications

1. **Data Engineering**: Type conversions when parsing CSVs, JSON, logs
   ```python
   age = int(row['age'])  # CSV fields are strings by default
   ```

2. **Web APIs**: Validating/sanitizing user input
   ```python
   user_id = int(request.args.get('id'))  # Convert query param
   ```

3. **Scientific Computing**: Numeric precision matters
   ```python
   # Float precision loss
   0.1 + 0.2 == 0.3  # False! (0.30000000000000004)
   ```

4. **DevOps**: Parsing configuration files
   ```python
   max_retries = int(os.getenv('MAX_RETRIES', '3'))
   ```

### Connections to Future Projects
- **Project 02**: Control flow uses boolean expressions from this project
- **Project 04**: Lists/tuples extend the type system
- **Project 06**: Classes define custom types
- **Project 16**: NumPy introduces array types
- **Project 32**: PyTorch tensors have GPU/CPU dtype complexity

---

## When to Use This

### Problem Indicators
You need this project's skills when:
- Starting any Python program
- Converting between data formats
- Performing calculations
- Handling user input
- Debugging type-related errors

### Anti-Patterns (When NOT to use these basics)

1. **Don't use `input()` in production web apps**
   - ❌ `name = input("Enter name: ")`  # Blocks the event loop
   - ✅ Use web frameworks (Flask, FastAPI) for HTTP requests

2. **Don't use floats for money**
   - ❌ `price = 19.99`  # Floating-point precision errors
   - ✅ Use `decimal.Decimal('19.99')` for financial calculations

3. **Don't ignore type hints in large projects**
   - ❌ `def process(data): ...`  # Unclear what `data` is
   - ✅ `def process(data: dict[str, Any]) -> list[str]: ...`

---

## Pitfalls & Gotchas

### Common Mistakes

1. **Mutable Default Arguments** (not in this project, but important)
   ```python
   # WRONG
   def add_item(item, lst=[]):  # [] created once!
       lst.append(item)
       return lst

   # RIGHT
   def add_item(item, lst=None):
       if lst is None:
           lst = []
       lst.append(item)
       return lst
   ```

2. **Integer Division Confusion**
   ```python
   5 / 2   # 2.5 (float division)
   5 // 2  # 2 (floor division)

   # In Python 2 (legacy): 5 / 2 == 2  (changed in Python 3!)
   ```

3. **Float Precision**
   ```python
   0.1 + 0.2 == 0.3  # False!
   # Use: abs(a - b) < 1e-9 for float comparisons
   ```

4. **Truthy/Falsy Values**
   ```python
   # Falsy: False, None, 0, 0.0, "", [], {}, set()
   # Everything else is truthy!

   if []:  # Empty list is falsy
       print("This never prints")
   ```

5. **Variable Shadowing**
   ```python
   list = [1, 2, 3]  # OOPS! Shadowed built-in `list()`
   x = list("abc")   # TypeError: 'list' object is not callable
   ```

### Debugging Tips

1. **Use `type()` to check types**
   ```python
   x = "42"
   print(type(x))  # <class 'str'>
   ```

2. **Use `isinstance()` for robust type checks**
   ```python
   isinstance(42, int)       # True
   isinstance(True, int)     # True (bool is subclass of int!)
   isinstance(3.14, float)   # True
   ```

3. **Read error messages bottom-up**
   ```
   Traceback (most recent call last):
     File "script.py", line 10, in <module>
       result = x + y
   TypeError: unsupported operand type(s) for +: 'int' and 'str'
                                                  ^^^^^^^^^^^^^^^^
   ```

4. **Use f-strings for debugging**
   ```python
   x = 42
   print(f"{x=}")  # x=42 (Python 3.8+)
   ```

---

## Performance Considerations

### Time Complexity

| Operation | Complexity | Notes |
|-----------|-----------|--------|
| Variable assignment | O(1) | Just binds name to object |
| Arithmetic (+, -, *, /) | O(1) | For ints/floats (not BigInts!) |
| Type conversion | O(1) to O(n) | `int("42")` is O(n) in string length |
| String formatting | O(n) | Where n = total output length |
| `print()` | O(n) | I/O-bound, system call overhead |

### Space Complexity

- **Variables**: O(1) per variable (just a reference)
- **Integers**: O(1) for small ints (-5 to 256), O(log n) for large ints
- **Floats**: O(1) always (64-bit IEEE 754)
- **Strings**: O(n) where n = number of characters

### Optimization Strategies

1. **Avoid unnecessary type conversions**
   ```python
   # SLOW: Convert every iteration
   for i in range(1000000):
       x = str(i)  # Wasteful if not needed

   # FAST: Convert once
   numbers = [str(i) for i in range(1000000)]
   ```

2. **Use f-strings over % formatting or .format()**
   ```python
   # SLOW
   name = "Alice"
   msg = "Hello, %s" % name

   # FAST (and more readable)
   msg = f"Hello, {name}"
   ```

3. **Reuse objects instead of recreating**
   ```python
   # SLOW: Creates 1M int objects
   for i in range(1000000):
       x = 0

   # FAST: Reuse same object
   x = 0
   for i in range(1000000):
       x  # Reference existing object
   ```

---

## Diagrams

### Python's Type Hierarchy

```
object (root of everything)
 ├── NoneType (None)
 ├── bool (True, False)
 ├── int (42, -17, 0)
 ├── float (3.14, -0.5, 1e10)
 ├── str ("hello", 'world')
 ├── list ([1, 2, 3])
 ├── dict ({key: value})
 └── ... (many more)
```

### Variable Assignment (Memory Model)

```
Code:  x = 42
       y = x
       x = 99

Memory:
┌─────┐      ┌─────┐
│  x  │ ───▶ │ 99  │  (new object)
└─────┘      └─────┘

┌─────┐      ┌─────┐
│  y  │ ───▶ │ 42  │  (original object)
└─────┘      └─────┘

Explanation: Reassigning `x` doesn't change `y`
             because integers are immutable.
```

### Type Conversion Flow

```
Input (str)  →  Validation  →  Conversion  →  Usage

"42"         →  is_digit()  →  int("42")   →  calculations
"3.14"       →  is_float()  →  float()     →  math operations
"true"       →  normalize   →  bool()      →  control flow
```

---

## Step-by-Step Walkthrough

### Approach: Understanding Variables & Types

#### Step 1: Variable Assignment
```python
x = 42
```
**What happens**:
1. Python creates an `int` object with value 42
2. The name `x` is bound to this object
3. No type declaration needed (dynamic typing)

**Memory**: `x` is a reference (like a pointer in C), not the value itself

#### Step 2: Type Checking
```python
type(x)       # <class 'int'>
isinstance(x, int)  # True
```

#### Step 3: Arithmetic
```python
a = 10
b = 3

a + b   # 13
a - b   # 7
a * b   # 30
a / b   # 3.333... (float division)
a // b  # 3 (floor division)
a % b   # 1 (modulo)
a ** b  # 1000 (exponentiation)
```

#### Step 4: Type Conversion
```python
x = "42"
y = int(x)  # Convert str to int

# Error handling
try:
    z = int("hello")  # ValueError!
except ValueError:
    z = 0  # Default value
```

#### Step 5: I/O
```python
# Output
print("Hello, World!")
name = "Alice"
age = 30
print(f"{name} is {age} years old")

# Input (for interactive scripts)
user_input = input("Enter a number: ")
number = int(user_input)  # Always returns string!
```

### Implementation Details

**Key decision**: When to use type hints?
- **Always** for function signatures in production code
- **Optional** for local variables (type inference works well)

```python
# Production-ready function
def calculate_area(radius: float) -> float:
    """Calculate circle area."""
    return 3.14159 * radius ** 2

# Quick script (type hints optional)
r = 5.0
area = 3.14159 * r ** 2
```

---

## How to Run

### Setup
```bash
cd project-01-basic-python-syntax
```

### Running the Exercise
```bash
# Interactive mode (REPL)
python
>>> x = 42
>>> print(x)

# Script mode
python exercise.py
```

### Running the Solution
```bash
python solution/solution.py
```

### Running Tests
```bash
# All tests
pytest test/test_project_01.py -v

# Specific test class
pytest test/test_project_01.py::TestPositiveCases -v

# With output
pytest test/test_project_01.py -v -s
```

### Expected Output
```
============================= test session starts ==============================
collected 15 items

test/test_project_01.py::TestBasicTypes::test_integer_type PASSED        [  6%]
test/test_project_01.py::TestBasicTypes::test_float_type PASSED          [ 13%]
test/test_project_01.py::TestBasicTypes::test_string_type PASSED         [ 20%]
test/test_project_01.py::TestArithmetic::test_addition PASSED            [ 26%]
test/test_project_01.py::TestArithmetic::test_division PASSED            [ 33%]
...

========================== 15 passed in 0.12s ===============================
```

---

## Cross-Language Comparison

### Python
```python
# Dynamic typing, no declarations
x = 42
x = "hello"  # Totally fine

# Type hints (optional, not enforced)
def add(a: int, b: int) -> int:
    return a + b
```

### Rust
```rust
// Static typing, strict compiler
let x: i32 = 42;
// x = "hello";  // ERROR: expected i32, found &str

fn add(a: i32, b: i32) -> i32 {
    a + b
}
```

### C
```c
// Static typing, manual memory
int x = 42;
// x = "hello";  // ERROR: incompatible types

int add(int a, int b) {
    return a + b;
}
```

### JavaScript
```javascript
// Dynamic typing (like Python)
let x = 42;
x = "hello";  // Totally fine

// TypeScript adds optional static typing
function add(a: number, b: number): number {
    return a + b;
}
```

### Go
```go
// Static typing with type inference
x := 42  // Type inferred as int
// x = "hello"  // ERROR: cannot use string as int

func add(a int, b int) int {
    return a + b
}
```

**Key insight**: Python's flexibility comes with runtime risk. Use type hints + mypy for best of both worlds.

---

## Advanced Challenges

1. **Challenge 1: Numeric Precision**
   - Write a function that accurately sums 0.1 ten times
   - Explore why `sum([0.1] * 10) != 1.0`
   - Solution: Use `decimal.Decimal`

2. **Challenge 2: Type Validator**
   - Create a function that validates input matches expected type
   - Handle nested types (e.g., `list[int]`, `dict[str, float]`)
   - Use `typing.get_args()` and `typing.get_origin()`

3. **Challenge 3: Calculator REPL**
   - Build an interactive calculator that:
     - Accepts expressions like "2 + 3 * 4"
     - Handles variables: "x = 10", "y = x + 5"
     - Validates input and catches errors
   - Extension: Support functions like "sin(45)", "sqrt(16)"

4. **Challenge 4: Type Inference**
   - Write a function that infers the most specific type from a string
   - "42" → int, "3.14" → float, "true" → bool, "hello" → str
   - Handle edge cases: "042" (octal?), "0x2A" (hex?), "1e10" (scientific)

5. **Challenge 5: Memory Profiler**
   - Measure memory usage of different types
   - Use `sys.getsizeof()` to compare int, float, str, list
   - Explore integer interning (`id(256) == id(256)` but `id(257) != id(257)`)

---

## References

### Official Documentation
- [Python Tutorial: An Informal Introduction](https://docs.python.org/3/tutorial/introduction.html)
- [Built-in Types](https://docs.python.org/3/library/stdtypes.html)
- [PEP 484: Type Hints](https://peps.python.org/pep-0484/)

### Books
- *Fluent Python* (Ramalho) — Chapter 1: The Python Data Model
- *Python Cookbook* (Beazley) — Chapter 2: Strings and Text

### Internal Resources
- [DSA Primer](../../DSA_PRIMER.md) — Big-O complexity basics
- [PYTHON_BASICS.md](../../PYTHON_BASICS.md) — Quick syntax reference

### External Resources
- [Real Python: Basic Data Types](https://realpython.com/python-data-types/)
- [Python Type Checking Guide](https://realpython.com/python-type-checking/)

---

## Related Projects

- **Next**: [Project 02: Control Flow & Loops](../project-02-control-flow-loops/) — Use variables in if/for/while
- **Related**: [Project 03: Functions & Modules](../project-03-functions-modules/) — Package code into reusable units
- **Advanced**: [Project 06: OOP Basics](../project-06-oop-basics/) — Define custom types

---

## Notes for Instructors

### Common Student Struggles
1. **"Why do I need type hints if Python doesn't enforce them?"**
   - Answer: Documentation, IDE autocomplete, catching bugs with mypy

2. **"When should I use `int()` vs `float()` vs `str()`?"**
   - Answer: Depends on what you need to do next (math? formatting? comparison?)

3. **"Why does `5 / 2` give `2.5` but `5 // 2` give `2`?"**
   - Answer: `/` is true division (always float), `//` is floor division (rounds down)

### Teaching Tips
- Start with REPL for instant feedback
- Show error messages and how to read them
- Emphasize that variables are references, not boxes
- Use `id()` to demonstrate object identity

---

Last updated: 2025-11-16
