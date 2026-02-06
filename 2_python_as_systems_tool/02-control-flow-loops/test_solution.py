"""
Test suite for Project 02: Control Flow and Loops

Run with: pytest test.py -v
"""

import pytest
from exercise import (
    is_even,
    get_grade,
    fizzbuzz,
    sum_numbers,
    sum_even_numbers,
    find_first_even,
    count_occurrences,
    print_multiplication_table,
    find_maximum,
    reverse_string,
    is_prime,
)


class TestIsEven:
    """Test even number checking."""
    
    def test_even_number(self):
        assert is_even(4) is True
        assert is_even(0) is True
        assert is_even(-2) is True
    
    def test_odd_number(self):
        assert is_even(3) is False
        assert is_even(1) is False
        assert is_even(-1) is False


class TestGetGrade:
    """Test grade calculation."""
    
    def test_grade_a(self):
        assert get_grade(95) == 'A'
        assert get_grade(90) == 'A'
        assert get_grade(100) == 'A'
    
    def test_grade_b(self):
        assert get_grade(85) == 'B'
        assert get_grade(80) == 'B'
        assert get_grade(89) == 'B'
    
    def test_grade_c(self):
        assert get_grade(75) == 'C'
        assert get_grade(70) == 'C'
        assert get_grade(79) == 'C'
    
    def test_grade_d(self):
        assert get_grade(65) == 'D'
        assert get_grade(60) == 'D'
        assert get_grade(69) == 'D'
    
    def test_grade_f(self):
        assert get_grade(59) == 'F'
        assert get_grade(0) == 'F'
        assert get_grade(30) == 'F'


class TestFizzBuzz:
    """Test FizzBuzz implementation."""
    
    def test_fizzbuzz_small(self):
        result = fizzbuzz(15)
        expected = [
            '1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz',
            '11', 'Fizz', '13', '14', 'FizzBuzz'
        ]
        assert result == expected
    
    def test_fizzbuzz_fizz(self):
        result = fizzbuzz(6)
        assert result[2] == 'Fizz'  # 3
        assert result[5] == 'Fizz'  # 6
    
    def test_fizzbuzz_buzz(self):
        result = fizzbuzz(10)
        assert result[4] == 'Buzz'  # 5
        assert result[9] == 'Buzz'  # 10
    
    def test_fizzbuzz_both(self):
        result = fizzbuzz(30)
        assert result[14] == 'FizzBuzz'  # 15
        assert result[29] == 'FizzBuzz'  # 30


class TestSumNumbers:
    """Test number summing."""
    
    def test_sum_small(self):
        assert sum_numbers(5) == 15  # 1+2+3+4+5
    
    def test_sum_one(self):
        assert sum_numbers(1) == 1
    
    def test_sum_large(self):
        assert sum_numbers(100) == 5050  # Formula: n*(n+1)/2
    
    def test_sum_zero(self):
        assert sum_numbers(0) == 0


class TestSumEvenNumbers:
    """Test even number summing."""
    
    def test_sum_even_small(self):
        assert sum_even_numbers(10) == 30  # 2+4+6+8+10
    
    def test_sum_even_one(self):
        assert sum_even_numbers(1) == 0  # No even numbers
    
    def test_sum_even_odd_limit(self):
        assert sum_even_numbers(9) == 20  # 2+4+6+8


class TestFindFirstEven:
    """Test finding first even number."""
    
    def test_find_first_even(self):
        assert find_first_even([1, 3, 4, 5, 6]) == 4
    
    def test_first_is_even(self):
        assert find_first_even([2, 3, 5]) == 2
    
    def test_no_even(self):
        assert find_first_even([1, 3, 5, 7]) is None
    
    def test_empty_list(self):
        assert find_first_even([]) is None


class TestCountOccurrences:
    """Test counting occurrences."""
    
    def test_count_basic(self):
        assert count_occurrences([1, 2, 3, 2, 4, 2], 2) == 3
    
    def test_count_none(self):
        assert count_occurrences([1, 3, 5], 2) == 0
    
    def test_count_all(self):
        assert count_occurrences([5, 5, 5], 5) == 3
    
    def test_count_empty(self):
        assert count_occurrences([], 1) == 0


class TestMultiplicationTable:
    """Test multiplication table."""
    
    def test_table_three(self):
        result = print_multiplication_table(3)
        expected = [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
        assert result == expected
    
    def test_table_one(self):
        result = print_multiplication_table(1)
        assert result == [[1]]
    
    def test_table_five(self):
        result = print_multiplication_table(5)
        assert len(result) == 5
        assert result[0] == [1, 2, 3, 4, 5]
        assert result[4][4] == 25


class TestFindMaximum:
    """Test finding maximum value."""
    
    def test_find_max_basic(self):
        assert find_maximum([3, 1, 4, 1, 5, 9, 2, 6]) == 9
    
    def test_find_max_single(self):
        assert find_maximum([42]) == 42
    
    def test_find_max_negative(self):
        assert find_maximum([-5, -2, -10]) == -2
    
    def test_find_max_mixed(self):
        assert find_maximum([-5, 0, 5, -10]) == 5


class TestReverseString:
    """Test string reversal."""
    
    def test_reverse_basic(self):
        assert reverse_string("hello") == "olleh"
    
    def test_reverse_single(self):
        assert reverse_string("a") == "a"
    
    def test_reverse_empty(self):
        assert reverse_string("") == ""
    
    def test_reverse_palindrome(self):
        assert reverse_string("racecar") == "racecar"


class TestIsPrime:
    """Test prime number checking."""
    
    def test_prime_numbers(self):
        assert is_prime(2) is True
        assert is_prime(3) is True
        assert is_prime(5) is True
        assert is_prime(7) is True
        assert is_prime(11) is True
        assert is_prime(13) is True
    
    def test_non_prime_numbers(self):
        assert is_prime(4) is False
        assert is_prime(6) is False
        assert is_prime(8) is False
        assert is_prime(9) is False
        assert is_prime(10) is False
    
    def test_edge_cases(self):
        assert is_prime(1) is False
        assert is_prime(0) is False
        assert is_prime(-5) is False
    
    def test_larger_primes(self):
        assert is_prime(17) is True
        assert is_prime(19) is True
        assert is_prime(23) is True

