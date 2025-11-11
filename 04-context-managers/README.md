# Project 04: Context Managers

> **Resource management with 'with' statement**

## 🎯 What You'll Learn

- `with` statement for resource management
- `__enter__` and `__exit__` magic methods
- `contextlib.contextmanager` decorator
- Exception handling in context managers

## 📚 Quick Example

```python
with open('file.txt', 'r') as f:
    content = f.read()
# File automatically closed!
```

## 🏃 Run

```bash
python main.py              # Demo
pytest test_solution.py -v  # Test your solution
```

**Status:** ✅ Complete with tests!
