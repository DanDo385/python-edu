"""
Project 01: Dynamic Typing Basics - Interactive Demo

Run this to see dynamic typing in action!
"""

def demo_dynamic_typing():
    """Demonstrate Python's dynamic typing."""
    print("=" * 70)
    print("DEMO 1: Dynamic Typing Basics")
    print("=" * 70)

    # Variable can change types
    x = 42
    print(f"x = {x}, type = {type(x).__name__}")

    x = "hello"
    print(f"x = {x}, type = {type(x).__name__}")

    x = [1, 2, 3]
    print(f"x = {x}, type = {type(x).__name__}")

    print("\nIn statically-typed languages like Rust, this would be a compile error!")
    print()


def demo_duck_typing():
    """Demonstrate duck typing."""
    print("=" * 70)
    print("DEMO 2: Duck Typing")
    print("=" * 70)

    def double(x):
        """Works with any type that supports *"""
        return x * 2

    print("double(5) =", double(5))           # int
    print("double(2.5) =", double(2.5))       # float
    print("double('hi') =", double("hi"))     # str
    print("double([1,2]) =", double([1, 2]))  # list

    print("\nSame function, different behaviors - that's duck typing!")
    print()


def demo_type_hints():
    """Demonstrate type hints (but they're not enforced!)."""
    print("=" * 70)
    print("DEMO 3: Type Hints (Not Enforced)")
    print("=" * 70)

    def add(a: int, b: int) -> int:
        """Type hints are documentation, not enforcement."""
        return a + b

    print("With type hints: def add(a: int, b: int) -> int")
    print("add(5, 3) =", add(5, 3))

    # This works even though type hints say int!
    print("add('hello', 'world') =", add("hello", "world"))
    print("\nType hints are NOT enforced at runtime!")
    print()


def demo_type_checking():
    """Demonstrate explicit type checking."""
    print("=" * 70)
    print("DEMO 4: Explicit Type Checking")
    print("=" * 70)

    def safe_divide(a, b):
        """Explicitly check types."""
        if not isinstance(a, (int, float)):
            raise TypeError(f"a must be int or float, got {type(a).__name__}")
        if not isinstance(b, (int, float)):
            raise TypeError(f"b must be int or float, got {type(b).__name__}")
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    print("safe_divide(10, 2) =", safe_divide(10, 2))

    try:
        safe_divide(10, "2")
    except TypeError as e:
        print(f"safe_divide(10, '2') -> TypeError: {e}")

    try:
        safe_divide(10, 0)
    except ValueError as e:
        print(f"safe_divide(10, 0) -> ValueError: {e}")

    print("\nExplicit type checking catches errors!")
    print()


def demo_performance():
    """Demonstrate performance implications."""
    print("=" * 70)
    print("DEMO 5: Performance Trade-offs")
    print("=" * 70)

    import time

    # Pure Python (slow)
    start = time.time()
    total = sum(i * i for i in range(100_000))
    python_time = time.time() - start

    print(f"Pure Python: {python_time * 1000:.2f}ms")
    print(f"Result: {total}")

    # With NumPy (fast!)
    try:
        import numpy as np
        start = time.time()
        total = np.sum(np.arange(100_000) ** 2)
        numpy_time = time.time() - start

        print(f"NumPy (C extension): {numpy_time * 1000:.2f}ms")
        print(f"Result: {total}")
        print(f"\nSpeedup: {python_time / numpy_time:.1f}x faster with NumPy!")
    except ImportError:
        print("\n(Install NumPy to see performance comparison: pip install numpy)")

    print()


def main():
    """Run all demos."""
    print("\n")
    print("🐍" * 35)
    print("  PROJECT 01: DYNAMIC TYPING BASICS - INTERACTIVE DEMO")
    print("🐍" * 35)
    print("\n")

    demo_dynamic_typing()
    input("Press Enter to continue...")

    demo_duck_typing()
    input("Press Enter to continue...")

    demo_type_hints()
    input("Press Enter to continue...")

    demo_type_checking()
    input("Press Enter to continue...")

    demo_performance()

    print("=" * 70)
    print("DEMO COMPLETE!")
    print("=" * 70)
    print("\nKey Takeaways:")
    print("1. Variables can change types (dynamic typing)")
    print("2. Functions work with different types (duck typing)")
    print("3. Type hints are documentation, not enforcement")
    print("4. Explicit type checking is sometimes necessary")
    print("5. Python is slow, but C extensions make it fast!")
    print("\nNext: Read solution.py for line-by-line explanations!")
    print()


if __name__ == "__main__":
    main()
