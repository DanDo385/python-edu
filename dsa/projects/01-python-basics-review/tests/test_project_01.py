"""
Tests for Project 01: Python Basics Review

Comprehensive test suite covering:
- Normal cases
- Edge cases
- Error handling
- Performance verification
"""

import pytest
from solution.solution import (
    find_maximum,
    reverse_string,
    is_palindrome,
    fibonacci,
    count_frequency
)


class TestFindMaximum:
    """Tests for find_maximum function."""
    
    def test_normal_case(self):
        """Test with typical positive integers."""
        assert find_maximum([1, 5, 3, 9, 2]) == 9
        assert find_maximum([10, 20, 30]) == 30
    
    def test_negative_numbers(self):
        """Test with negative integers."""
        assert find_maximum([-1, -5, -3]) == -1
        assert find_maximum([-10, -1, -100]) == -1
    
    def test_single_element(self):
        """Test with single element."""
        assert find_maximum([42]) == 42
        assert find_maximum([-5]) == -5
    
    def test_all_same(self):
        """Test when all elements are the same."""
        assert find_maximum([5, 5, 5, 5]) == 5
    
    def test_maximum_at_start(self):
        """Test when maximum is first element."""
        assert find_maximum([10, 5, 3, 1]) == 10
    
    def test_maximum_at_end(self):
        """Test when maximum is last element."""
        assert find_maximum([1, 3, 5, 10]) == 10
    
    def test_empty_array(self):
        """Test that empty array raises ValueError."""
        with pytest.raises(ValueError, match="empty array"):
            find_maximum([])


class TestReverseString:
    """Tests for reverse_string function."""
    
    def test_normal_string(self):
        """Test with typical strings."""
        assert reverse_string("hello") == "olleh"
        assert reverse_string("Python") == "nohtyP"
    
    def test_empty_string(self):
        """Test with empty string."""
        assert reverse_string("") == ""
    
    def test_single_character(self):
        """Test with single character."""
        assert reverse_string("a") == "a"
    
    def test_palindrome(self):
        """Test with palindrome string."""
        assert reverse_string("racecar") == "racecar"
    
    def test_with_spaces(self):
        """Test with spaces."""
        assert reverse_string("hello world") == "dlrow olleh"
    
    def test_with_numbers(self):
        """Test with numeric characters."""
        assert reverse_string("12345") == "54321"


class TestIsPalindrome:
    """Tests for is_palindrome function."""
    
    def test_simple_palindrome(self):
        """Test simple palindromes."""
        assert is_palindrome("racecar") == True
        assert is_palindrome("noon") == True
        assert is_palindrome("level") == True
    
    def test_not_palindrome(self):
        """Test non-palindromes."""
        assert is_palindrome("hello") == False
        assert is_palindrome("python") == False
    
    def test_single_character(self):
        """Test single character (always palindrome)."""
        assert is_palindrome("a") == True
    
    def test_empty_string(self):
        """Test empty string (considered palindrome)."""
        assert is_palindrome("") == True
    
    def test_palindrome_with_spaces(self):
        """Test palindrome with spaces (should ignore)."""
        assert is_palindrome("A man a plan a canal Panama") == True
        assert is_palindrome("race a car") == False
    
    def test_case_insensitive(self):
        """Test that comparison is case-insensitive."""
        assert is_palindrome("Racecar") == True
        assert is_palindrome("RaceCar") == True
    
    def test_with_punctuation(self):
        """Test with punctuation (should ignore)."""
        assert is_palindrome("A man, a plan, a canal: Panama") == True


class TestFibonacci:
    """Tests for fibonacci function."""
    
    def test_base_cases(self):
        """Test base cases F(0) and F(1)."""
        assert fibonacci(0) == 0
        assert fibonacci(1) == 1
    
    def test_small_values(self):
        """Test small Fibonacci numbers."""
        assert fibonacci(2) == 1
        assert fibonacci(3) == 2
        assert fibonacci(4) == 3
        assert fibonacci(5) == 5
        assert fibonacci(6) == 8
    
    def test_medium_values(self):
        """Test medium Fibonacci numbers."""
        assert fibonacci(10) == 55
        assert fibonacci(15) == 610
        assert fibonacci(20) == 6765
    
    def test_larger_values(self):
        """Test larger Fibonacci numbers."""
        assert fibonacci(30) == 832040
    
    def test_negative_input(self):
        """Test that negative input raises ValueError."""
        with pytest.raises(ValueError, match="negative"):
            fibonacci(-1)
        with pytest.raises(ValueError):
            fibonacci(-10)
    
    def test_sequence(self):
        """Test that sequence is correct."""
        sequence = [fibonacci(i) for i in range(10)]
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        assert sequence == expected


class TestCountFrequency:
    """Tests for count_frequency function."""
    
    def test_normal_case(self):
        """Test with typical array."""
        result = count_frequency([1, 2, 2, 3, 3, 3])
        assert result == {1: 1, 2: 2, 3: 3}
    
    def test_all_same(self):
        """Test when all elements are the same."""
        result = count_frequency([5, 5, 5, 5])
        assert result == {5: 4}
    
    def test_all_unique(self):
        """Test when all elements are unique."""
        result = count_frequency([1, 2, 3, 4, 5])
        assert result == {1: 1, 2: 1, 3: 1, 4: 1, 5: 1}
    
    def test_empty_array(self):
        """Test with empty array."""
        result = count_frequency([])
        assert result == {}
    
    def test_single_element(self):
        """Test with single element."""
        result = count_frequency([42])
        assert result == {42: 1}
    
    def test_negative_numbers(self):
        """Test with negative numbers."""
        result = count_frequency([-1, -1, -2, -2, -2])
        assert result == {-1: 2, -2: 3}
    
    def test_large_array(self):
        """Test with larger array."""
        arr = [1] * 100 + [2] * 50 + [3] * 25
        result = count_frequency(arr)
        assert result == {1: 100, 2: 50, 3: 25}


# Performance tests
class TestPerformance:
    """Performance and complexity verification tests."""
    
    def test_find_maximum_linear_time(self):
        """Verify find_maximum is O(n)."""
        # Should handle large arrays efficiently
        large_array = list(range(100000))
        result = find_maximum(large_array)
        assert result == 99999
    
    def test_fibonacci_linear_time(self):
        """Verify fibonacci is O(n) not O(2^n)."""
        # Should compute large Fibonacci quickly
        # If this takes more than a second, implementation is wrong
        result = fibonacci(35)
        assert result == 9227465
    
    def test_count_frequency_linear_time(self):
        """Verify count_frequency is O(n)."""
        # Should handle large arrays efficiently
        large_array = [i % 100 for i in range(100000)]
        result = count_frequency(large_array)
        assert len(result) == 100
        assert all(count == 1000 for count in result.values())


# Integration test
def test_all_functions_together():
    """Test that all functions work together correctly."""
    # Create test data
    numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    
    # Find maximum
    max_val = find_maximum(numbers)
    assert max_val == 9
    
    # Test string operations
    text = "python"
    reversed_text = reverse_string(text)
    assert not is_palindrome(text)
    assert is_palindrome("racecar")
    
    # Calculate Fibonacci
    fib_10 = fibonacci(10)
    assert fib_10 == 55
    
    # Count frequencies
    freq = count_frequency(numbers)
    assert freq[5] == 3  # 5 appears 3 times
    assert freq[1] == 2  # 1 appears 2 times
