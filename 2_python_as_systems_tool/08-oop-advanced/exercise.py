"""
Project 08: OOP Advanced

Implement inheritance + polymorphism for geometric shapes.
Run: pytest test_solution.py -v
"""

from abc import ABC, abstractmethod
from typing import Optional


class Shape(ABC):
    """Abstract shape contract."""

    @abstractmethod
    def area(self) -> float:
        """Return area of the shape."""

    @abstractmethod
    def perimeter(self) -> float:
        """Return perimeter of the shape."""

    @abstractmethod
    def scale(self, factor: float) -> None:
        """Scale shape dimensions in-place by factor."""


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        # TODO: Validate positive dimensions and store them.
        pass

    def area(self) -> float:
        # TODO: Return rectangle area.
        pass

    def perimeter(self) -> float:
        # TODO: Return rectangle perimeter.
        pass

    def scale(self, factor: float) -> None:
        # TODO: Validate factor > 0 and scale width/height in-place.
        pass


class Circle(Shape):
    def __init__(self, radius: float):
        # TODO: Validate positive radius and store it.
        pass

    def area(self) -> float:
        # TODO: Return circle area.
        pass

    def perimeter(self) -> float:
        # TODO: Return circle circumference.
        pass

    def scale(self, factor: float) -> None:
        # TODO: Validate factor > 0 and scale radius in-place.
        pass


class ShapeCollection:
    """Container for Shape objects."""

    def __init__(self):
        # TODO: Initialize empty storage.
        pass

    def add(self, shape: Shape) -> None:
        # TODO: Validate and append shape.
        pass

    def total_area(self) -> float:
        # TODO: Sum area() across all shapes.
        pass

    def largest_shape(self) -> Optional[Shape]:
        # TODO: Return shape with largest area, or None if empty.
        pass

    def scale_all(self, factor: float) -> None:
        # TODO: Scale all shapes in-place.
        pass


if __name__ == "__main__":
    shapes = ShapeCollection()
    shapes.add(Rectangle(2, 3))
    shapes.add(Circle(1))
    print(shapes.total_area())
