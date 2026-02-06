"""
Test suite for Project 03: Functions and Modular Programming

Run with: pytest test.py -v
"""

import pytest
from exercise import (
    greet,
    add_numbers,
    calculate_factorial,
    is_prime,
    get_maximum,
    calculate_circle_area,
    format_name,
    sum_list,
    count_vowels,
    power,
)


class TestGreet:
    """Test greeting function."""
    
    def test_greet_basic(self):
        assert greet("Alice") == "Hello, Alice!"
    
    def test_greet_different_name(self):
        assert greet("Bob") == "Hello, Bob!"


class TestAddNumbers:
    """Test addition function."""
    
    def test_add_integers(self):
        assert add_numbers(5, 3) == 8
    
    def test_add_floats(self):
        assert abs(add_numbers(3.5, 2.5) - 6.0) < 0.001
    
    def test_add_negative(self):
        assert add_numbers(-5, 3) == -2


class TestFactorial:
    """Test factorial calculation."""
    
    def test_factorial_zero(self):
        assert calculate_factorial(0) == 1
    
    def test_factorial_one(self):
        assert calculate_factorial(1) == 1
    
    def test_factorial_small(self):
        assert calculate_factorial(5) == 120
    
    def test_factorial_medium(self):
        assert calculate_factorial(7) == 5040
    
    def test_factorial_negative(self):
        assert calculate_factorial(-1) is None


class TestIsPrime:
    """Test prime checking."""
    
    def test_prime_numbers(self):
        assert is_prime(2) is True
        assert is_prime(3) is True
        assert is_prime(5) is True
        assert is_prime(7) is True
        assert is_prime(11) is True
    
    def test_non_prime_numbers(self):
        assert is_prime(4) is False
        assert is_prime(6) is False
        assert is_prime(9) is False
        assert is_prime(15) is False
    
    def test_edge_cases(self):
        assert is_prime(1) is False
        assert is_prime(0) is False
        assert is_prime(-5) is False


class TestGetMaximum:
    """Test maximum finding."""
    
    def test_maximum_basic(self):
        assert get_maximum(1, 2, 3) == 3
        assert get_maximum(3, 2, 1) == 3
        assert get_maximum(2, 3, 1) == 3
    
    def test_maximum_negative(self):
        assert get_maximum(-5, -2, -10) == -2
    
    def test_maximum_floats(self):
        assert get_maximum(1.5, 2.7, 1.9) == 2.7


class TestCalculateCircleArea:
    """Test circle area calculation."""
    
    def test_circle_area_basic(self):
        import math
        result = calculate_circle_area(1.0)
        expected = math.pi
        assert abs(result - expected) < 0.001
    
    def test_circle_area_larger(self):
        import math
        result = calculate_circle_area(5.0)
        expected = math.pi * 25
        assert abs(result - expected) < 0.001
    
    def test_circle_area_negative(self):
        assert calculate_circle_area(-1.0) is None


class TestFormatName:
    """Test name formatting."""
    
    def test_format_without_middle(self):
        assert format_name("John", "Doe") == "John Doe"
    
    def test_format_with_middle(self):
        assert format_name("John", "Doe", "Middle") == "John Middle Doe"
    
    def test_format_different_names(self):
        assert format_name("Alice", "Smith") == "Alice Smith"
        assert format_name("Bob", "Jones", "Q") == "Bob Q Jones"


class TestSumList:
    """Test list summing."""
    
    def test_sum_basic(self):
        assert sum_list([1, 2, 3, 4, 5]) == 15
    
    def test_sum_empty(self):
        assert sum_list([]) == 0
    
    def test_sum_single(self):
        assert sum_list([42]) == 42
    
    def test_sum_negative(self):
        assert sum_list([-5, 10, -3]) == 2


class TestCountVowels:
    """Test vowel counting."""
    
    def test_count_vowels_basic(self):
        assert count_vowels("hello") == 2
    
    def test_count_vowels_uppercase(self):
        assert count_vowels("HELLO") == 2
    
    def test_count_vowels_mixed(self):
        assert count_vowels("Python") == 1
    
    def test_count_vowels_all_vowels(self):
        assert count_vowels("aeiou") == 5
    
    def test_count_vowels_none(self):
        assert count_vowels("bcdfg") == 0


class TestPower:
    """Test power calculation."""
    
    def test_power_basic(self):
        assert power(2, 3) == 8
    
    def test_power_zero_exponent(self):
        assert power(5, 0) == 1
    
    def test_power_one_exponent(self):
        assert power(7, 1) == 7
    
    def test_power_large(self):
        assert power(2, 10) == 1024
    
    def test_power_negative_exponent(self):
        assert power(2, -1) is None

