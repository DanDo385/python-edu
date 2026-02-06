"""
Project 09: Decorators - Interactive Demo
"""

import time
from solution import timer, repeat, cache, validate_args, debug


def demo_timer():
    print("=" * 70)
    print("DEMO 1: Timer Decorator")
    print("=" * 70)

    @timer
    def slow_function():
        time.sleep(0.5)
        return "Computation complete"

    print("Calling slow_function()...")
    result = slow_function()
    print(f"Result: {result}\n")


def demo_repeat():
    print("=" * 70)
    print("DEMO 2: Repeat Decorator")
    print("=" * 70)

    @repeat(3)
    def greet(name):
        print(f"Hello, {name}!")
        return f"Greeted {name}"

    print("Calling greet('Alice') with @repeat(3):")
    result = greet("Alice")
    print(f"Final return value: {result}\n")


def demo_cache():
    print("=" * 70)
    print("DEMO 3: Cache Decorator (Memoization)")
    print("=" * 70)

    call_count = {'value': 0}

    @cache
    def fibonacci(n):
        call_count['value'] += 1
        if n < 2:
            return n
        return fibonacci(n-1) + fibonacci(n-2)

    print("Computing fibonacci(10) with caching...")
    result = fibonacci(10)
    print(f"Result: {result}")
    print(f"Function called {call_count['value']} times (would be 177 without cache!)\n")


def demo_validate():
    print("=" * 70)
    print("DEMO 4: Validate Args Decorator")
    print("=" * 70)

    @validate_args(int, int)
    def add(a, b):
        return a + b

    print("@validate_args(int, int)")
    print("def add(a, b): return a + b")
    print()

    print("add(2, 3) =", add(2, 3), "✓")

    try:
        print("add('2', 3) =", end=" ")
        add("2", 3)
    except TypeError as e:
        print(f"TypeError: {e} ✗\n")


def demo_debug():
    print("=" * 70)
    print("DEMO 5: Debug Decorator")
    print("=" * 70)

    @debug
    def calculate(x, y, operation="add"):
        if operation == "add":
            return x + y
        elif operation == "multiply":
            return x * y
        return 0

    print("@debug decorator prints all function calls:\n")
    calculate(5, 3)
    print()
    calculate(5, 3, operation="multiply")
    print()


def demo_stacking():
    print("=" * 70)
    print("DEMO 6: Stacking Decorators")
    print("=" * 70)

    @timer
    @cache
    def expensive_function(n):
        """Simulate expensive computation."""
        time.sleep(0.1)
        return n ** 2

    print("@timer")
    print("@cache")
    print("def expensive_function(n): ...")
    print()

    print("First call (slow):")
    result1 = expensive_function(5)
    print(f"Result: {result1}\n")

    print("Second call (cached, instant):")
    result2 = expensive_function(5)
    print(f"Result: {result2}\n")


def main():
    print("\n")
    print("🎭" * 35)
    print("  PROJECT 09: DECORATORS & METAPROGRAMMING - INTERACTIVE DEMO")
    print("🎭" * 35)
    print("\n")

    demo_timer()
    input("Press Enter to continue...")

    demo_repeat()
    input("Press Enter to continue...")

    demo_cache()
    input("Press Enter to continue...")

    demo_validate()
    input("Press Enter to continue...")

    demo_debug()
    input("Press Enter to continue...")

    demo_stacking()

    print("=" * 70)
    print("DEMO COMPLETE!")
    print("=" * 70)
    print("\nKey Takeaways:")
    print("1. Decorators modify functions without changing their code")
    print("2. @decorator is syntactic sugar for func = decorator(func)")
    print("3. Decorators with arguments require a factory pattern")
    print("4. Use @wraps to preserve function metadata")
    print("5. Decorators can be stacked for combined effects")
    print("\nNext: Read solution.py for detailed explanations!")
    print()


if __name__ == "__main__":
    main()
