# Project 06: Classes & Magic Methods

> **OOP and operator overloading**

## 🎯 Learn

- Class definition
- Magic methods (dunder methods)
- Operator overloading
- String representation
- Comparison operators

## 📚 Example

```python
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
```

## 🏃 Run

```bash
python main.py && pytest test_solution.py -v
```

**Status:** ✅ Complete!
