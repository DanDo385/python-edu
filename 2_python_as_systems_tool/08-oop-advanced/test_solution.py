"""Tests for Project 08: OOP Advanced."""

from pathlib import Path
import sys

import pytest

sys.path.insert(0, str(Path(__file__).parent))

from solution import Circle, Rectangle, ShapeCollection


class TestRectangle:
    def test_area_and_perimeter(self):
        rect = Rectangle(2, 3)
        assert rect.area() == pytest.approx(6.0)
        assert rect.perimeter() == pytest.approx(10.0)

    def test_invalid_dimensions_rejected(self):
        with pytest.raises(ValueError):
            Rectangle(0, 3)


class TestCircle:
    def test_area_and_perimeter(self):
        circle = Circle(2)
        assert circle.area() == pytest.approx(12.566370614359172)
        assert circle.perimeter() == pytest.approx(12.566370614359172)

    def test_invalid_radius_rejected(self):
        with pytest.raises(ValueError):
            Circle(-1)


class TestShapeCollection:
    def test_total_area(self):
        shapes = ShapeCollection()
        shapes.add(Rectangle(2, 3))
        shapes.add(Circle(1))
        assert shapes.total_area() == pytest.approx(6 + 3.141592653589793)

    def test_largest_shape(self):
        shapes = ShapeCollection()
        rect = Rectangle(2, 3)
        circle = Circle(1)
        shapes.add(rect)
        shapes.add(circle)
        assert shapes.largest_shape() is rect

    def test_largest_shape_empty_collection(self):
        shapes = ShapeCollection()
        assert shapes.largest_shape() is None

    def test_rejects_non_shape(self):
        shapes = ShapeCollection()
        with pytest.raises(TypeError):
            shapes.add("not-a-shape")  # type: ignore[arg-type]

    def test_scale_all_mutates_shared_shape_objects(self):
        # Invariant: collection stores references; scaling mutates same objects.
        shapes = ShapeCollection()
        rect = Rectangle(2, 3)
        alias = rect

        shapes.add(rect)
        shapes.scale_all(2)

        assert alias.width == pytest.approx(4.0)
        assert alias.height == pytest.approx(6.0)
        assert rect.area() == pytest.approx(24.0)
