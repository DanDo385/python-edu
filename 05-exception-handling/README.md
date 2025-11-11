# Project 05: Exception Handling

> **Graceful error handling and recovery**

## 🎯 What You'll Learn

- try/except/else/finally blocks
- Exception hierarchy
- Custom exceptions
- Raising and catching exceptions
- Best practices

## 📚 Example

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("Cleanup code here")
```

## 🏃 Run

```bash
python main.py              # Demo
pytest test_solution.py -v  # Test
```

**Status:** ✅ Complete!
