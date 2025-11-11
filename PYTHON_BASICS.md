# Python Basics - Quick Syntax Reference

> **A fast reference guide for Python fundamentals**

This document provides a quick reference for Python syntax. For in-depth explanations, see the individual projects!

---

## Table of Contents

- [Variables & Data Types](#variables--data-types)
- [Operators](#operators)
- [Control Flow](#control-flow)
- [Functions](#functions)
- [Data Structures](#data-structures)
- [Classes](#classes)
- [Imports](#imports)
- [Common Patterns](#common-patterns)

---

## Variables & Data Types

### Variable Assignment

```python
# Python uses dynamic typing - no type declaration needed
x = 42              # int
name = "Alice"      # str
price = 19.99       # float
is_active = True    # bool
items = None        # NoneType
```

### Type Checking

```python
type(42)            # <class 'int'>
isinstance(42, int) # True

# Multiple type check
isinstance(x, (int, float))  # True if x is int OR float
```

### Type Conversion

```python
int("42")           # String to int: 42
float("3.14")       # String to float: 3.14
str(42)             # Int to string: "42"
bool(1)             # Truthy conversion: True
bool(0)             # Falsy conversion: False
list("abc")         # String to list: ['a', 'b', 'c']
```

### Numeric Types

```python
# Integers (unlimited precision!)
big_num = 123456789012345678901234567890

# Floats
pi = 3.14159
scientific = 1.5e-10  # Scientific notation

# Complex numbers
z = 3 + 4j
```

### Strings

```python
# String creation
s1 = 'single quotes'
s2 = "double quotes"
s3 = """triple quotes
for multi-line strings"""

# String operations
"hello" + " world"      # Concatenation: "hello world"
"ha" * 3                # Repetition: "hahaha"
"hello"[0]              # Indexing: 'h'
"hello"[1:4]            # Slicing: 'ell'
"hello"[::-1]           # Reverse: 'olleh'

# String methods
"HELLO".lower()         # 'hello'
"hello".upper()         # 'HELLO'
"  hi  ".strip()        # 'hi'
"a,b,c".split(",")      # ['a', 'b', 'c']
",".join(['a','b','c']) # 'a,b,c'
"hello".replace('l', 'L') # 'heLLo'

# String formatting
name = "Alice"
age = 30
f"My name is {name} and I'm {age}"  # f-strings (preferred!)
"My name is {} and I'm {}".format(name, age)
"My name is %s and I'm %d" % (name, age)  # Old style
```

---

## Operators

### Arithmetic

```python
10 + 3      # Addition: 13
10 - 3      # Subtraction: 7
10 * 3      # Multiplication: 30
10 / 3      # Division (float): 3.333...
10 // 3     # Floor division: 3
10 % 3      # Modulo (remainder): 1
10 ** 3     # Exponentiation: 1000
```

### Comparison

```python
10 == 10    # Equal: True
10 != 5     # Not equal: True
10 > 5      # Greater than: True
10 < 5      # Less than: False
10 >= 10    # Greater or equal: True
10 <= 5     # Less or equal: False
```

### Logical

```python
True and False  # False
True or False   # True
not True        # False

# Short-circuit evaluation
x = 5
x > 3 and x < 10  # True (both conditions evaluated)
x > 10 or x < 3   # False (both evaluated since first is False)
```

### Identity & Membership

```python
# Identity (same object in memory)
x is y          # True if x and y are the same object
x is not y      # True if x and y are different objects

# Membership
'a' in "apple"  # True
5 in [1,2,3]    # False
'x' not in "hello"  # True
```

---

## Control Flow

### If/Elif/Else

```python
x = 10

if x > 10:
    print("Greater than 10")
elif x == 10:
    print("Equal to 10")
else:
    print("Less than 10")

# Ternary operator
result = "even" if x % 2 == 0 else "odd"
```

### For Loops

```python
# Iterate over sequence
for item in [1, 2, 3]:
    print(item)

# Iterate with index
for i, item in enumerate(['a', 'b', 'c']):
    print(f"{i}: {item}")

# Range-based loop
for i in range(5):        # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 5):     # 2, 3, 4
    print(i)

for i in range(0, 10, 2): # 0, 2, 4, 6, 8 (step=2)
    print(i)
```

### While Loops

```python
count = 0
while count < 5:
    print(count)
    count += 1

# While with break
while True:
    if some_condition:
        break  # Exit loop
```

### Break, Continue, Pass

```python
for i in range(10):
    if i == 3:
        continue  # Skip to next iteration
    if i == 7:
        break     # Exit loop
    print(i)

# Pass (do nothing - placeholder)
if condition:
    pass  # TODO: implement later
```

---

## Functions

### Basic Function

```python
def greet(name):
    """Function docstring"""
    return f"Hello, {name}!"

result = greet("Alice")
```

### Default Arguments

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

greet("Alice")              # "Hello, Alice!"
greet("Bob", "Hi")          # "Hi, Bob!"
```

### Variable Arguments

```python
# *args - variable positional arguments (tuple)
def sum_all(*args):
    return sum(args)

sum_all(1, 2, 3)  # 6

# **kwargs - variable keyword arguments (dict)
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30)
```

### Lambda Functions

```python
# Anonymous functions
square = lambda x: x ** 2
square(5)  # 25

# Often used with map, filter
squares = list(map(lambda x: x**2, [1, 2, 3]))  # [1, 4, 9]
evens = list(filter(lambda x: x%2==0, [1,2,3,4]))  # [2, 4]
```

### Type Hints (Optional)

```python
def add(a: int, b: int) -> int:
    return a + b

from typing import List, Dict, Optional

def process_items(items: List[int]) -> Dict[str, int]:
    return {"count": len(items)}

def find_user(user_id: int) -> Optional[str]:
    # Returns str or None
    return None
```

---

## Data Structures

### Lists (Mutable, Ordered)

```python
# Creation
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]

# Indexing & Slicing
fruits[0]       # "apple" (first item)
fruits[-1]      # "cherry" (last item)
fruits[1:3]     # ["banana", "cherry"] (slice)
fruits[:2]      # ["apple", "banana"] (first 2)
fruits[2:]      # ["cherry"] (from index 2)

# Methods
fruits.append("orange")         # Add to end
fruits.insert(1, "mango")       # Insert at index
fruits.remove("banana")         # Remove by value
fruits.pop()                    # Remove & return last
fruits.pop(0)                   # Remove & return at index
fruits.clear()                  # Remove all
len(fruits)                     # Length
fruits.count("apple")           # Count occurrences
fruits.index("cherry")          # Find index
fruits.sort()                   # Sort in-place
fruits.reverse()                # Reverse in-place
sorted(fruits)                  # Return sorted copy
```

### Tuples (Immutable, Ordered)

```python
# Creation
point = (10, 20)
single = (42,)  # Note the comma!

# Unpacking
x, y = point
a, b, c = (1, 2, 3)

# Named tuples
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
p.x  # 10
```

### Sets (Mutable, Unordered, Unique)

```python
# Creation
numbers = {1, 2, 3, 4, 5}
empty_set = set()  # {} creates an empty dict!

# Operations
numbers.add(6)          # Add element
numbers.remove(3)       # Remove (error if not found)
numbers.discard(3)      # Remove (no error if not found)
numbers.clear()         # Remove all

# Set operations
a = {1, 2, 3}
b = {3, 4, 5}
a | b           # Union: {1, 2, 3, 4, 5}
a & b           # Intersection: {3}
a - b           # Difference: {1, 2}
a ^ b           # Symmetric difference: {1, 2, 4, 5}
```

### Dictionaries (Mutable, Key-Value)

```python
# Creation
person = {"name": "Alice", "age": 30}
empty_dict = {}

# Access
person["name"]          # "Alice"
person.get("name")      # "Alice"
person.get("city", "NYC")  # Default if not found

# Methods
person["age"] = 31      # Update
person["city"] = "NYC"  # Add new key
del person["age"]       # Delete key
person.pop("name")      # Remove & return value
person.keys()           # dict_keys(['name', 'age'])
person.values()         # dict_values(['Alice', 30])
person.items()          # dict_items([('name', 'Alice'), ...])

# Iteration
for key in person:
    print(key, person[key])

for key, value in person.items():
    print(key, value)
```

---

## Classes

### Basic Class

```python
class Person:
    """Person class with name and age"""

    def __init__(self, name, age):
        """Constructor"""
        self.name = name
        self.age = age

    def greet(self):
        """Instance method"""
        return f"Hi, I'm {self.name}"

    @staticmethod
    def species():
        """Static method (no self)"""
        return "Homo sapiens"

    @classmethod
    def from_birth_year(cls, name, birth_year):
        """Class method (alternative constructor)"""
        age = 2025 - birth_year
        return cls(name, age)

# Usage
p = Person("Alice", 30)
p.greet()  # "Hi, I'm Alice"
Person.species()  # "Homo sapiens"
```

### Inheritance

```python
class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)  # Call parent constructor
        self.employee_id = employee_id

    def greet(self):
        """Override parent method"""
        return f"Hi, I'm {self.name}, ID: {self.employee_id}"
```

### Magic Methods

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        """String representation (str(obj))"""
        return f"Point({self.x}, {self.y})"

    def __repr__(self):
        """Developer representation (repr(obj))"""
        return f"Point(x={self.x}, y={self.y})"

    def __add__(self, other):
        """Addition operator (+)"""
        return Point(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        """Equality operator (==)"""
        return self.x == other.x and self.y == other.y
```

---

## Imports

### Import Styles

```python
# Import entire module
import math
math.sqrt(16)

# Import specific items
from math import sqrt, pi
sqrt(16)

# Import with alias
import numpy as np
np.array([1, 2, 3])

from datetime import datetime as dt
now = dt.now()

# Import all (NOT recommended!)
from math import *
```

### Module Structure

```python
# mymodule.py
def helper():
    pass

def main():
    pass

if __name__ == "__main__":
    # Only runs if script is executed directly
    main()
```

---

## Common Patterns

### List Comprehensions

```python
# Basic
squares = [x**2 for x in range(10)]

# With condition
evens = [x for x in range(10) if x % 2 == 0]

# Nested
matrix = [[i*j for j in range(3)] for i in range(3)]
```

### Dictionary Comprehensions

```python
# Basic
squares = {x: x**2 for x in range(5)}

# From two lists
keys = ['a', 'b', 'c']
values = [1, 2, 3]
d = {k: v for k, v in zip(keys, values)}
```

### Generator Expressions

```python
# Lazy evaluation (doesn't create list in memory)
squares_gen = (x**2 for x in range(1000000))

# Use with functions that accept iterables
sum(x**2 for x in range(1000))
```

### Context Managers

```python
# File handling
with open('file.txt', 'r') as f:
    content = f.read()
# File automatically closed

# Multiple resources
with open('in.txt') as f_in, open('out.txt', 'w') as f_out:
    f_out.write(f_in.read())
```

### Exception Handling

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
else:
    print("No exception occurred")
finally:
    print("Always executes")
```

### Enumerate & Zip

```python
# Enumerate (index + value)
for i, item in enumerate(['a', 'b', 'c']):
    print(f"{i}: {item}")

# Zip (combine iterables)
names = ['Alice', 'Bob']
ages = [30, 25]
for name, age in zip(names, ages):
    print(f"{name} is {age}")
```

### Unpacking

```python
# List/tuple unpacking
a, b, c = [1, 2, 3]

# Extended unpacking
first, *middle, last = [1, 2, 3, 4, 5]
# first=1, middle=[2,3,4], last=5

# Dictionary unpacking
def func(a, b, c):
    pass

kwargs = {'a': 1, 'b': 2, 'c': 3}
func(**kwargs)
```

---

## Python Idioms

### Swap Variables

```python
# Python way
a, b = b, a

# Other languages
temp = a
a = b
b = temp
```

### Check Empty

```python
# Pythonic
if not my_list:
    print("List is empty")

# Not Pythonic
if len(my_list) == 0:
    print("List is empty")
```

### Iterate with Index

```python
# Pythonic
for i, item in enumerate(items):
    print(i, item)

# Not Pythonic
for i in range(len(items)):
    print(i, items[i])
```

### Dictionary Default

```python
# Using get() with default
count = counts.get(key, 0) + 1

# Using setdefault()
counts.setdefault(key, 0)
counts[key] += 1

# Using defaultdict
from collections import defaultdict
counts = defaultdict(int)
counts[key] += 1
```

---

## Next Steps

This is just a quick reference! For in-depth learning:

1. **[Start Project 1](./01-dynamic-typing-basics/)** - Dynamic typing deep dive
2. **[Read main README](./README.md)** - Full learning paths
3. **[Check projects](./PROJECT_SUMMARY.md)** - See all available projects

**Remember:** The best way to learn Python is to write Python! 🐍

---

*Last updated: 2025-11-11*
