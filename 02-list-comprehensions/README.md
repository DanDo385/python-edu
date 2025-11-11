# Project 02: List Comprehensions - Python's Superpower

> **Master Python's most distinctive and powerful feature**

---

## 🎯 Learning Objectives

By the end of this project, you'll understand:

1. **List Comprehensions** - Concise syntax for creating lists
2. **Dictionary Comprehensions** - Building dicts in one line
3. **Set Comprehensions** - Creating sets efficiently
4. **Generator Expressions** - Lazy evaluation for memory efficiency
5. **Nested Comprehensions** - Complex data transformations
6. **Performance Patterns** - When comprehensions beat loops
7. **Pythonic Style** - Writing readable, idiomatic Python

---

## 🚀 Why List Comprehensions?

### The Problem (Other Languages)

```python
# Traditional loop approach
evens = []
for i in range(10):
    if i % 2 == 0:
        evens.append(i)
```

### The Python Way

```python
# List comprehension - same logic, one line!
evens = [i for i in range(10) if i % 2 == 0]
```

**Benefits:**
- ✅ More concise (1 line vs 4 lines)
- ✅ Faster execution (~20% faster than append loop)
- ✅ More readable (once you learn the syntax)
- ✅ Pythonic (idiomatic Python code)

---

## 📖 Basic Syntax

### List Comprehension Structure

```python
[expression for item in iterable if condition]
 │          │        │           │
 │          │        │           └─ Filter (optional)
 │          │        └────────────── Source
 │          └─────────────────────── Variable
 └────────────────────────────────── Transform
```

### Examples

```python
# Double all numbers
doubles = [x * 2 for x in range(5)]
# [0, 2, 4, 6, 8]

# Filter evens
evens = [x for x in range(10) if x % 2 == 0]
# [0, 2, 4, 6, 8]

# Transform and filter
squares_of_evens = [x**2 for x in range(10) if x % 2 == 0]
# [0, 4, 16, 36, 64]
```

---

## 🗂️ Dictionary Comprehensions

```python
# Create dict from two lists
keys = ['a', 'b', 'c']
values = [1, 2, 3]
d = {k: v for k, v in zip(keys, values)}
# {'a': 1, 'b': 2, 'c': 3}

# Square numbers
squares = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Filter and transform
evens_squared = {x: x**2 for x in range(10) if x % 2 == 0}
# {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
```

---

## 🔢 Set Comprehensions

```python
# Unique squares
squares = {x**2 for x in range(-5, 6)}
# {0, 1, 4, 9, 16, 25}  (no duplicates!)

# Unique first letters
words = ['apple', 'banana', 'apricot', 'blueberry']
first_letters = {word[0] for word in words}
# {'a', 'b'}
```

---

## ⚡ Generator Expressions (Lazy Evaluation)

```python
# List comprehension - creates entire list in memory
squares_list = [x**2 for x in range(1_000_000)]
# Memory: ~8MB

# Generator expression - lazy evaluation
squares_gen = (x**2 for x in range(1_000_000))
# Memory: ~88 bytes!

# Use with functions that accept iterables
total = sum(x**2 for x in range(1_000_000))
# Never creates the full list!
```

**Key Difference:** `[]` creates list, `()` creates generator

---

## 🎭 Nested Comprehensions

```python
# Flatten 2D list
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [num for row in matrix for num in row]
# [1, 2, 3, 4, 5, 6]

# Create multiplication table
table = [[i * j for j in range(1, 6)] for i in range(1, 6)]
# [[1, 2, 3, 4, 5],
#  [2, 4, 6, 8, 10],
#  [3, 6, 9, 12, 15],
#  [4, 8, 12, 16, 20],
#  [5, 10, 15, 20, 25]]
```

---

## 📊 Performance Comparison

### Benchmark (1 million items)

```python
# Method 1: append in loop
result = []
for i in range(1_000_000):
    if i % 2 == 0:
        result.append(i)
# Time: ~60ms

# Method 2: List comprehension
result = [i for i in range(1_000_000) if i % 2 == 0]
# Time: ~45ms (25% faster!)

# Method 3: Generator expression
result = (i for i in range(1_000_000) if i % 2 == 0)
# Time: ~0.001ms (creation), processes lazily
```

**Why comprehensions are faster:**
- Less Python bytecode
- Optimized in C interpreter
- No repeated function calls (append)

---

## 🌍 Multi-Language Comparison

### Python

```python
evens = [x for x in range(100) if x % 2 == 0]
```

### Rust

```rust
let evens: Vec<i32> = (0..100)
    .filter(|x| x % 2 == 0)
    .collect();
```

### Go

```go
var evens []int
for i := 0; i < 100; i++ {
    if i % 2 == 0 {
        evens = append(evens, i)
    }
}
```

### JavaScript

```javascript
const evens = Array.from({length: 100}, (_, i) => i)
    .filter(x => x % 2 === 0);
```

**Python wins in readability and conciseness!**

---

## ✅ Best Practices

### DO: Use for simple transformations

```python
# Good: Clear and concise
squares = [x**2 for x in numbers]
```

### DON'T: Use for complex logic

```python
# Bad: Too complex for comprehension
result = [
    process_complex(x) if condition1(x) else fallback(x)
    for x in items
    if validate(x) and check(x)
]

# Better: Use regular loop
result = []
for x in items:
    if validate(x) and check(x):
        result.append(process_complex(x) if condition1(x) else fallback(x))
```

### DO: Use generators for large datasets

```python
# Good: Memory efficient
total = sum(x**2 for x in range(1_000_000))

# Bad: Wastes memory
total = sum([x**2 for x in range(1_000_000)])
```

---

## 🎯 Common Patterns

### 1. Filter and Transform

```python
# Get lengths of long words
long_word_lengths = [len(w) for w in words if len(w) > 5]
```

### 2. Flatten Nested Structures

```python
# Flatten list of lists
flat = [item for sublist in nested for item in sublist]
```

### 3. Cartesian Product

```python
# All combinations
pairs = [(x, y) for x in [1, 2, 3] for y in ['a', 'b']]
# [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b'), (3, 'a'), (3, 'b')]
```

### 4. Conditional Expression

```python
# Different transformation based on condition
result = [x * 2 if x > 0 else x for x in numbers]
```

---

## 🏃 Running This Project

```bash
# Interactive demo
python main.py

# Implement yourself
# Edit lib.py, then:
pytest test_solution.py -v

# Read detailed solution
cat solution.py
```

---

## 💡 When NOT to Use Comprehensions

1. **Side effects** - Use regular loops
   ```python
   # Don't: Comprehension for side effects
   [print(x) for x in items]  # Bad!

   # Do: Regular loop
   for x in items:
       print(x)
   ```

2. **Complex logic** - Readability matters
   ```python
   # Too complex
   result = [f(g(h(x))) for x in items if a(x) and b(x) or c(x)]

   # Better
   for x in items:
       if (a(x) and b(x)) or c(x):
           result.append(f(g(h(x))))
   ```

3. **Early termination** - Can't break/return
   ```python
   # Can't break early in comprehension
   # Use regular loop if you need to break
   ```

---

## 📚 The Zen of Python

> "Readability counts."
> "Flat is better than nested."
> "If the implementation is hard to explain, it's a bad idea."

Comprehensions should make code MORE readable, not less!

---

## ⏭️ Next Steps

Once you master comprehensions, move to **Project 03: Decorators** to learn Python's metaprogramming features!

---

*Remember: List comprehensions are Python's superpower - use them wisely!* 🚀
