# Project 01: Dynamic Typing Basics

> **Understanding Python's flexible type system and when it's powerful**

---

## 🎯 Learning Objectives

By the end of this project, you'll understand:

1. **Dynamic Typing** - Variables can change types at runtime
2. **Duck Typing** - "If it quacks like a duck, it's a duck"
3. **Type Hints** - Optional type annotations for clarity
4. **Type Checking** - Runtime vs compile-time type checking
5. **Performance Trade-offs** - Flexibility vs speed
6. **When to use Python** - And when to choose statically-typed languages

---

## 🐍 What is Dynamic Typing?

### The Basics

In Python, you don't declare variable types:

```python
# Python (dynamically typed)
x = 42          # x is an int
x = "hello"     # Now x is a string! No error.
x = [1, 2, 3]   # Now x is a list! Still no error.
```

Compare to statically-typed languages:

```rust
// Rust (statically typed)
let x: i32 = 42;
x = "hello";    // ERROR: expected i32, found &str
```

```typescript
// TypeScript (statically typed)
let x: number = 42;
x = "hello";    // ERROR: Type 'string' is not assignable to type 'number'
```

### Why Dynamic Typing?

**Pros:**
- ✅ Faster to write code (no type declarations)
- ✅ More flexible (one function can handle multiple types)
- ✅ Great for prototyping and scripting
- ✅ Less boilerplate code

**Cons:**
- ❌ Errors caught at runtime, not compile-time
- ❌ Slower execution (runtime type checking overhead)
- ❌ Can be harder to understand large codebases
- ❌ Refactoring is riskier without type safety

---

## 🦆 Duck Typing

> "If it walks like a duck and quacks like a duck, it's a duck"

Python doesn't care about the **type** of an object, only its **behavior**:

```python
def double(x):
    return x * 2

# Works with different types!
double(5)        # 10 (int multiplication)
double(2.5)      # 5.0 (float multiplication)
double("hi")     # "hihi" (string repetition)
double([1, 2])   # [1, 2, 1, 2] (list repetition)
```

### Real-World Example

```python
# Any object with a .write() method works
def save_data(file_like_object, data):
    file_like_object.write(data)

# Works with real files
with open('output.txt', 'w') as f:
    save_data(f, "Hello")

# Also works with StringIO (in-memory file)
from io import StringIO
buffer = StringIO()
save_data(buffer, "Hello")

# And custom objects!
class CustomLogger:
    def write(self, data):
        print(f"LOG: {data}")

save_data(CustomLogger(), "Hello")
```

All these work because they "quack" the same way (have a `.write()` method)!

---

## 🏷️ Type Hints (Python 3.5+)

Type hints are **optional** annotations that document expected types:

```python
def add(a: int, b: int) -> int:
    return a + b
```

**Important:** Type hints are **not enforced** at runtime!

```python
def add(a: int, b: int) -> int:
    return a + b

result = add("hello", "world")  # NO ERROR! Returns "helloworld"
```

### Why Use Type Hints?

1. **Better IDE support** - Autocomplete, error detection
2. **Self-documentation** - Clear function contracts
3. **Static analysis tools** - mypy, pylint can catch errors
4. **Easier refactoring** - IDEs can track type changes

### Type Checking with mypy

```bash
# Install mypy
pip install mypy

# Check your code
mypy your_script.py
```

---

## 📊 Performance Implications

### Dynamic Typing is Slower

```python
# Python must check types at runtime
def add(a, b):
    return a + b  # Runtime: Check if a and b support +

# Rust knows types at compile time
fn add(a: i32, b: i32) -> i32 {
    a + b  // Compiles to direct CPU instructions
}
```

**Benchmark** (1 million additions):
- Python: ~30ms
- Rust: ~0.01ms (3000x faster!)

### But Python Has a Secret Weapon

```python
# Pure Python: Slow
total = 0
for i in range(1_000_000):
    total += i * i
# ~100ms

# NumPy (C extension): Fast!
import numpy as np
total = np.sum(np.arange(1_000_000) ** 2)
# ~5ms (20x faster!)
```

**Lesson:** Python is slow, but **Python + C extensions = Fast enough!**

---

## 🎯 When to Use Python vs Static Languages

### ✅ Choose Python When:

- **Rapid development** is priority (startups, prototypes)
- **Data science** (NumPy/Pandas ecosystem)
- **Automation scripts** (quick one-offs)
- **Web backends** (Django/Flask handle thousands of requests/sec)
- **Machine learning** (PyTorch/TensorFlow)
- **Glue code** (connecting different systems)

### ❌ Avoid Python For:

- **High-frequency trading** (microsecond latency matters)
- **Game engines** (60 FPS rendering)
- **Embedded systems** (limited resources)
- **Mobile apps** (use Swift/Kotlin)
- **Operating systems** (need low-level control)
- **Real-time systems** (predictable timing required)

---

## 💡 Key Concepts in This Project

### 1. Type Flexibility

```python
# The same function works with multiple types
def process(x):
    return x * 2

process(5)       # int
process(3.14)    # float
process("hi")    # str
process([1, 2])  # list
```

### 2. Type Checking at Runtime

```python
def safe_divide(a, b):
    if not isinstance(a, (int, float)):
        raise TypeError("a must be int or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be int or float")
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

### 3. Type Hints for Documentation

```python
from typing import List, Dict, Optional

def find_user(user_id: int) -> Optional[Dict[str, str]]:
    """
    Find a user by ID.

    Returns None if user not found.
    """
    # Implementation
    pass
```

---

## 🏃 Running This Project

### Try the Interactive Demo

```bash
python main.py
```

### Implement It Yourself

Edit `lib.py` and implement the TODO functions. Then run:

```bash
pytest test_solution.py -v
```

### Read the Detailed Solution

```bash
cat solution.py
```

Every single line is explained!

---

## 🧪 Practice Exercises

### Exercise 1: Type Flexibility

Write a function `triple(x)` that works with:
- Numbers (returns x * 3)
- Strings (returns x repeated 3 times)
- Lists (returns list repeated 3 times)

### Exercise 2: Type Checking

Write `safe_add(a, b)` that:
- Only accepts int or float
- Raises TypeError for other types
- Returns the sum

### Exercise 3: Duck Typing

Write `save_to_file(writable, data)` that works with:
- Real files
- StringIO
- Any object with a `.write()` method

---

## 📚 Further Reading

- [PEP 484 - Type Hints](https://www.python.org/dev/peps/pep-0484/)
- [mypy Documentation](http://mypy-lang.org/)
- [The Zen of Python](https://www.python.org/dev/peps/pep-0020/)

---

## ⏭️ Next Project

Once you understand dynamic typing, move to **Project 02: List Comprehensions** - Python's superpower for data transformation!

---

*Remember: Dynamic typing is about flexibility and developer productivity. It's not about being lazy with types - it's about moving fast while building!*
