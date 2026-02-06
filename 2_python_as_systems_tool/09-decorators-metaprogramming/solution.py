"""
PROJECT 09: DECORATORS & METAPROGRAMMING

Decorators are a powerful Python feature that allows you to modify or enhance
functions and classes without changing their source code.

WHAT IS A DECORATOR?
-------------------
A decorator is a function that takes another function and extends its behavior
without explicitly modifying it.

Basic pattern:
    @decorator
    def func():
        pass

    # Is equivalent to:
    func = decorator(func)

WHY DECORATORS?
--------------
- Separate concerns (timing, logging, etc. from business logic)
- Reusable functionality
- Clean, readable code
- DRY principle (Don't Repeat Yourself)
"""

import time
from functools import wraps
from typing import Callable, Any


def timer(func: Callable) -> Callable:
    """
    Decorator that measures and prints execution time.

    This demonstrates the basic decorator pattern.
    """
    @wraps(func)  # Preserves original function's metadata
    def wrapper(*args, **kwargs):
        # Record start time
        start = time.time()

        # Call the original function
        result = func(*args, **kwargs)

        # Record end time
        end = time.time()

        # Print timing info
        print(f"{func.__name__} took {end - start:.4f}s")

        return result

    return wrapper


def repeat(times: int) -> Callable:
    """
    Decorator factory that repeats function execution.

    This is a decorator that takes arguments, requiring 3 levels:
    1. Factory function (takes arguments)
    2. Decorator function (takes the function to decorate)
    3. Wrapper function (replaces the original function)
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


def cache(func: Callable) -> Callable:
    """
    Decorator that caches function results (memoization).

    Stores results in a dictionary keyed by function arguments.
    Great for expensive computations with repeated inputs.
    """
    cached_results = {}

    @wraps(func)
    def wrapper(*args):
        # Use args as dictionary key
        if args not in cached_results:
            # Compute and cache result
            cached_results[args] = func(*args)

        # Return cached result
        return cached_results[args]

    return wrapper


def validate_args(*types) -> Callable:
    """
    Decorator factory that validates argument types.

    Example:
        @validate_args(int, int)
        def add(a, b):
            return a + b
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Check each argument's type
            for arg, expected_type in zip(args, types):
                if not isinstance(arg, expected_type):
                    raise TypeError(
                        f"Expected {expected_type.__name__}, "
                        f"got {type(arg).__name__}"
                    )

            return func(*args, **kwargs)

        return wrapper
    return decorator


def debug(func: Callable) -> Callable:
    """
    Decorator that prints function calls with arguments.

    Useful for debugging and understanding program flow.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Format arguments
        args_str = ", ".join(repr(a) for a in args)
        kwargs_str = ", ".join(f"{k}={v!r}" for k, v in kwargs.items())
        all_args = ", ".join(filter(None, [args_str, kwargs_str]))

        print(f"Calling {func.__name__}({all_args})")

        result = func(*args, **kwargs)

        print(f"{func.__name__} returned {result!r}")

        return result

    return wrapper


# DECORATOR PATTERN BREAKDOWN:
# ---------------------------
#
# 1. Simple decorator (no arguments):
#    @decorator
#    def func():
#        pass
#
# 2. Decorator with arguments (factory):
#    @decorator(arg)
#    def func():
#        pass
#
# 3. Class decorator:
#    @decorator
#    class MyClass:
#        pass

# REAL-WORLD EXAMPLES:
# -------------------

# 1. Flask routing:
#    @app.route('/users')
#    def get_users():
#        pass

# 2. Property decorator:
#    class Person:
#        @property
#        def age(self):
#            return self._age

# 3. functools.lru_cache:
#    @lru_cache(maxsize=128)
#    def fibonacci(n):
#        pass
