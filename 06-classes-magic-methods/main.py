"""
Project 06: Classes & Magic Methods - Demo
"""

from solution import Vector, BankAccount, Stack


def demo_vector():
    print("=" * 70)
    print("DEMO 1: Vector with Operator Overloading")
    print("=" * 70)

    v1 = Vector(1, 2)
    v2 = Vector(3, 4)

    print(f"v1 = {v1}")
    print(f"v2 = {v2}")
    print(f"v1 + v2 = {v1 + v2}")
    print(f"v1 - v2 = {v1 - v2}")
    print(f"v1 * 3 = {v1 * 3}")
    print(f"v1 == v2: {v1 == v2}")
    print()


def demo_bank_account():
    print("=" * 70)
    print("DEMO 2: BankAccount with Comparison Methods")
    print("=" * 70)

    alice = BankAccount("Alice", 100)
    bob = BankAccount("Bob", 200)

    print(f"alice = {alice}")
    print(f"bob = {bob}")
    print(f"alice < bob: {alice < bob}")
    print(f"bob > alice: {bob > alice}")
    print()


def demo_stack():
    print("=" * 70)
    print("DEMO 3: Stack with Container Protocol")
    print("=" * 70)

    stack = Stack()
    print("Pushing 1, 2, 3...")
    stack.push(1)
    stack.push(2)
    stack.push(3)

    print(f"Stack length: {len(stack)}")
    print(f"Stack[0]: {stack[0]}")
    print(f"Pop: {stack.pop()}")
    print(f"Pop: {stack.pop()}")
    print()


def main():
    print("\n🎭" * 35)
    print("  PROJECT 06: CLASSES & MAGIC METHODS")
    print("🎭" * 35)
    print()

    demo_vector()
    demo_bank_account()
    demo_stack()

    print("=" * 70)
    print("Key Takeaways:")
    print("1. Magic methods define operator behavior")
    print("2. __str__ for users, __repr__ for developers")
    print("3. Comparison methods enable sorting")
    print("4. Container protocol: __len__, __getitem__")
    print()


if __name__ == "__main__":
    main()
