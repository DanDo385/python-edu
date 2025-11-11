"""
Project 06: Classes & Magic Methods - Practice Stubs
"""


class Vector:
    """2D vector with operator overloading."""

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, other):
        """Add two vectors: v1 + v2"""
        # TODO: Return new Vector with summed components
        pass

    def __str__(self):
        """String representation: str(v)"""
        # TODO: Return string like "Vector(3, 4)"
        pass

    def __eq__(self, other):
        """Equality: v1 == v2"""
        # TODO: Compare x and y components
        pass


class BankAccount:
    """Bank account with magic methods."""

    def __init__(self, owner: str, balance: float = 0):
        self.owner = owner
        self.balance = balance

    def __repr__(self):
        """Developer representation"""
        # TODO: Return string like "BankAccount('Alice', 100.0)"
        pass

    def __lt__(self, other):
        """Less than comparison: account1 < account2"""
        # TODO: Compare by balance
        pass


class Stack:
    """Stack with container protocol."""

    def __init__(self):
        self._items = []

    def __len__(self):
        """Length: len(stack)"""
        # TODO: Return number of items
        pass

    def __getitem__(self, index):
        """Index access: stack[0]"""
        # TODO: Return item at index
        pass

    def push(self, item):
        """Add item to stack."""
        # TODO: Implement
        pass

    def pop(self):
        """Remove and return top item."""
        # TODO: Implement
        pass


if __name__ == "__main__":
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    print(v1 + v2)
