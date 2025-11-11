"""
Project 03: Decorators & Metaprogramming - Practice Stubs

TODO: Implement these decorators
Run tests with: pytest test_solution.py -v
"""

import time
from functools import wraps
from typing import Callable, Any


def timer(func: Callable) -> Callable:
    """
    Decorator that prints execution time of a function.

    Example:
        @timer
        def slow_func():
            time.sleep(1)

        slow_func()  # Prints: "slow_func took 1.0023s"
    """
    # TODO: Implement timer decorator
    # Hint: Use time.time() before and after calling func
    pass


def repeat(times: int) -> Callable:
    """
    Decorator factory that repeats function execution.

    Example:
        @repeat(3)
        def greet():
            print("Hello!")

        greet()  # Prints "Hello!" 3 times
    """
    # TODO: Implement repeat decorator factory
    # Hint: This needs 3 levels - factory, decorator, wrapper
    pass


def cache(func: Callable) -> Callable:
    """
    Decorator that caches function results (memoization).

    Example:
        @cache
        def fibonacci(n):
            if n < 2:
                return n
            return fibonacci(n-1) + fibonacci(n-2)
    """
    # TODO: Implement cache decorator
    # Hint: Use a dictionary to store results
    pass


def validate_args(*types) -> Callable:
    """
    Decorator factory that validates argument types.

    Example:
        @validate_args(int, int)
        def add(a, b):
            return a + b

        add(1, 2)    # OK
        add("1", 2)  # Raises TypeError
    """
    # TODO: Implement type validation decorator
    pass


def debug(func: Callable) -> Callable:
    """
    Decorator that prints function name and arguments.

    Example:
        @debug
        def add(a, b):
            return a + b

        add(2, 3)  # Prints: "Calling add(2, 3)" then returns 5
    """
    # TODO: Implement debug decorator
    pass


if __name__ == "__main__":
    # Test your implementations
    @timer
    def test_timer():
        time.sleep(0.1)
        return "done"

    print(test_timer())

    @repeat(3)
    def test_repeat():
        print("Hello!")

    test_repeat()
