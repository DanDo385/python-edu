"""
Project 02: List Comprehensions - Test Suite
"""

import pytest
from solution import (
    filter_even_numbers,
    square_numbers,
    word_lengths,
    unique_letters,
    flatten_matrix,
    generate_squares,
)


class TestFilterEvenNumbers:
    def test_basic(self):
        assert filter_even_numbers([1, 2, 3, 4, 5, 6]) == [2, 4, 6]

    def test_empty(self):
        assert filter_even_numbers([]) == []

    def test_all_odd(self):
        assert filter_even_numbers([1, 3, 5]) == []

    def test_all_even(self):
        assert filter_even_numbers([2, 4, 6]) == [2, 4, 6]


class TestSquareNumbers:
    def test_basic(self):
        assert square_numbers([1, 2, 3, 4]) == [1, 4, 9, 16]

    def test_empty(self):
        assert square_numbers([]) == []

    def test_negative(self):
        assert square_numbers([-2, -1, 0, 1, 2]) == [4, 1, 0, 1, 4]


class TestWordLengths:
    def test_basic(self):
        result = word_lengths(['hi', 'hello', 'python'])
        assert result == {'hi': 2, 'hello': 5, 'python': 6}

    def test_empty(self):
        assert word_lengths([]) == {}


class TestUniqueLetters:
    def test_basic(self):
        assert unique_letters("hello") == {'h', 'e', 'l', 'o'}

    def test_empty(self):
        assert unique_letters("") == set()


class TestFlattenMatrix:
    def test_basic(self):
        assert flatten_matrix([[1, 2], [3, 4], [5, 6]]) == [1, 2, 3, 4, 5, 6]

    def test_empty(self):
        assert flatten_matrix([]) == []


class TestGenerateSquares:
    def test_basic(self):
        assert list(generate_squares(5)) == [0, 1, 4, 9, 16]

    def test_is_generator(self):
        result = generate_squares(5)
        assert hasattr(result, '__next__')


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
