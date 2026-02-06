"""
Project 08: OOP Advanced - SOLUTION

Reference implementation focused on:
- abstract base classes,
- inheritance,
- polymorphic dispatch,
- in-place mutation via shared object references.
"""

from abc import ABC, abstractmethod
import math
from typing import Optional


class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        raise NotImplementedError

    @abstractmethod
    def perimeter(self) -> float:
        raise NotImplementedError

    @abstractmethod
    def scale(self, factor: float) -> None:
        raise NotImplementedError


def _validate_positive_number(name: str, value: float) -> float:
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        raise TypeError(f"{name} must be numeric")
    if value <= 0:
        raise ValueError(f"{name} must be > 0")
    return float(value)


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = _validate_positive_number("width", width)
        self.height = _validate_positive_number("height", height)

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2.0 * (self.width + self.height)

    def scale(self, factor: float) -> None:
        factor = _validate_positive_number("factor", factor)
        # In-place mutation: all aliases to this Rectangle see updated dimensions.
        self.width *= factor
        self.height *= factor


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = _validate_positive_number("radius", radius)

    def area(self) -> float:
        return math.pi * (self.radius ** 2)

    def perimeter(self) -> float:
        return 2.0 * math.pi * self.radius

    def scale(self, factor: float) -> None:
        factor = _validate_positive_number("factor", factor)
        self.radius *= factor


class ShapeCollection:
    def __init__(self):
        self._shapes: list[Shape] = []

    def __len__(self) -> int:
        return len(self._shapes)

    def __iter__(self):
        return iter(self._shapes)

    def add(self, shape: Shape) -> None:
        if not isinstance(shape, Shape):
            raise TypeError("shape must implement Shape")
        self._shapes.append(shape)

    def total_area(self) -> float:
        return sum(shape.area() for shape in self._shapes)

    def largest_shape(self) -> Optional[Shape]:
        if not self._shapes:
            return None
        return max(self._shapes, key=lambda shape: shape.area())

    def scale_all(self, factor: float) -> None:
        # Polymorphism: each concrete shape decides how to scale itself.
        for shape in self._shapes:
            shape.scale(factor)


if __name__ == "__main__":
    shapes = ShapeCollection()
    shapes.add(Rectangle(2, 3))
    shapes.add(Circle(1))
    print(shapes.total_area())
