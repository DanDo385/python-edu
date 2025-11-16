"""Tests for Project 13: Monotonic Stack"""

import pytest
from solution.solution import (
    next_greater_element,
    largest_rectangle_histogram,
    daily_temperatures,
    stock_span
)


class TestNextGreaterElement:
    def test_basic(self):
        assert next_greater_element([4, 5, 2, 10]) == [5, 10, 10, -1]

    def test_decreasing(self):
        assert next_greater_element([5, 4, 3, 2, 1]) == [-1, -1, -1, -1, -1]


class TestLargestRectangle:
    def test_basic(self):
        assert largest_rectangle_histogram([2, 1, 5, 6, 2, 3]) == 10

    def test_single(self):
        assert largest_rectangle_histogram([5]) == 5


class TestDailyTemperatures:
    def test_basic(self):
        result = daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73])
        assert result == [1, 1, 4, 2, 1, 1, 0, 0]


class TestStockSpan:
    def test_basic(self):
        result = stock_span([100, 80, 60, 70, 60, 75, 85])
        assert result == [1, 1, 1, 2, 1, 4, 6]
