"""
PROJECT 06: CLASSES & MAGIC METHODS

Magic methods (dunder methods) are special methods with double underscores
that allow you to define how your objects behave with Python operators.
"""


class Vector:
    """2D vector with operator overloading."""

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, other):
        """Vector addition."""
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """Vector subtraction."""
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        """Scalar multiplication."""
        return Vector(self.x * scalar, self.y * scalar)

    def __str__(self):
        """User-friendly string representation."""
        return f"Vector({self.x}, {self.y})"

    def __repr__(self):
        """Developer representation."""
        return f"Vector(x={self.x}, y={self.y})"

    def __eq__(self, other):
        """Equality comparison."""
        return self.x == other.x and self.y == other.y


class BankAccount:
    """Bank account with comparison magic methods."""

    def __init__(self, owner: str, balance: float = 0):
        self.owner = owner
        self.balance = balance

    def __repr__(self):
        return f"BankAccount('{self.owner}', {self.balance})"

    def __str__(self):
        return f"{self.owner}'s account: ${self.balance:.2f}"

    def __lt__(self, other):
        """Less than comparison by balance."""
        return self.balance < other.balance

    def __le__(self, other):
        return self.balance <= other.balance

    def __gt__(self, other):
        return self.balance > other.balance

    def __ge__(self, other):
        return self.balance >= other.balance


class Stack:
    """Stack with container protocol."""

    def __init__(self):
        self._items = []

    def __len__(self):
        """Return number of items."""
        return len(self._items)

    def __getitem__(self, index):
        """Get item by index."""
        return self._items[index]

    def __repr__(self):
        return f"Stack({self._items})"

    def push(self, item):
        """Add item to top."""
        self._items.append(item)

    def pop(self):
        """Remove and return top item."""
        return self._items.pop()

    def is_empty(self):
        return len(self._items) == 0


# COMMON MAGIC METHODS:
# --------------------
# __init__     Constructor
# __str__      str(obj) - user-friendly
# __repr__     repr(obj) - developer-friendly
# __add__      obj1 + obj2
# __sub__      obj1 - obj2
# __mul__      obj1 * obj2
# __eq__       obj1 == obj2
# __lt__       obj1 < obj2
# __len__      len(obj)
# __getitem__  obj[key]
# __setitem__  obj[key] = value
# __call__     obj()
