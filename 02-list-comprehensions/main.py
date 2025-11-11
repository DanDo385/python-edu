"""
Project 02: List Comprehensions - Interactive Demo
"""

def demo_list_comprehensions():
    print("=" * 70)
    print("DEMO 1: List Comprehensions")
    print("=" * 70)

    # Traditional loop
    print("\nTraditional loop:")
    evens = []
    for i in range(10):
        if i % 2 == 0:
            evens.append(i)
    print(f"evens = {evens}")

    # List comprehension
    print("\nList comprehension:")
    evens = [i for i in range(10) if i % 2 == 0]
    print(f"evens = {evens}")
    print("Same result, more concise!")
    print()


def demo_dict_comprehensions():
    print("=" * 70)
    print("DEMO 2: Dictionary Comprehensions")
    print("=" * 70)

    words = ['apple', 'banana', 'cherry']
    word_lengths = {word: len(word) for word in words}
    print(f"word_lengths = {word_lengths}")

    squares = {x: x**2 for x in range(5)}
    print(f"squares = {squares}")
    print()


def demo_set_comprehensions():
    print("=" * 70)
    print("DEMO 3: Set Comprehensions")
    print("=" * 70)

    numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    unique = {x for x in numbers}
    print(f"unique = {unique}")

    squares = {x**2 for x in range(-5, 6)}
    print(f"unique squares = {squares}")
    print()


def demo_generators():
    print("=" * 70)
    print("DEMO 4: Generator Expressions (Lazy Evaluation)")
    print("=" * 70)

    import sys

    # List - all in memory
    squares_list = [x**2 for x in range(1000)]
    print(f"List size: {sys.getsizeof(squares_list)} bytes")

    # Generator - lazy
    squares_gen = (x**2 for x in range(1000))
    print(f"Generator size: {sys.getsizeof(squares_gen)} bytes")
    print(f"\nGenerator is {sys.getsizeof(squares_list) // sys.getsizeof(squares_gen)}x smaller!")
    print()


def demo_nested():
    print("=" * 70)
    print("DEMO 5: Nested Comprehensions")
    print("=" * 70)

    # Flatten matrix
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flat = [num for row in matrix for num in row]
    print(f"matrix = {matrix}")
    print(f"flat = {flat}")

    # Cartesian product
    pairs = [(x, y) for x in [1, 2] for y in ['a', 'b']]
    print(f"\npairs = {pairs}")
    print()


def main():
    print("\n")
    print("🐍" * 35)
    print("  PROJECT 02: LIST COMPREHENSIONS - INTERACTIVE DEMO")
    print("🐍" * 35)
    print("\n")

    demo_list_comprehensions()
    input("Press Enter to continue...")

    demo_dict_comprehensions()
    input("Press Enter to continue...")

    demo_set_comprehensions()
    input("Press Enter to continue...")

    demo_generators()
    input("Press Enter to continue...")

    demo_nested()

    print("=" * 70)
    print("DEMO COMPLETE!")
    print("=" * 70)
    print("\nKey Takeaways:")
    print("1. List comprehensions are more concise than loops")
    print("2. Dict/set comprehensions work similarly")
    print("3. Generators are memory-efficient for large datasets")
    print("4. Nested comprehensions can flatten or create complex structures")
    print("\nNext: Read solution.py for line-by-line explanations!")
    print()


if __name__ == "__main__":
    main()
