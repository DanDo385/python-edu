# Project 03: Decorators & Metaprogramming

> **Modify functions without changing their code**

## 🎯 Learning Objectives

1. **Function Decorators** - @decorator syntax
2. **Decorator Factories** - Decorators with arguments
3. **functools.wraps** - Preserving function metadata
4. **Multiple Decorators** - Stacking decorators
5. **Real-world Uses** - Logging, timing, caching, authentication

## 🔥 What Are Decorators?

```python
@timer
def slow_function():
    time.sleep(1)
    return "Done"

# Equivalent to: slow_function = timer(slow_function)
```

## 🏃 Running This Project

```bash
python main.py              # Interactive demo
pytest test_solution.py -v  # Test your solution
cat solution.py             # Read explanations
```

**Status:** ✅ Complete with tests!
