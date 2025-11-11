"""
Project 01: Dynamic Typing Basics - Comprehensive Test Suite

Run with: pytest test_solution.py -v
Run with coverage: pytest test_solution.py --cov=solution -v
"""

import pytest
from solution import (
    add_numbers,
    multiply,
    describe_type,
    safe_divide,
    process_data,
)


class TestAddNumbers:
    """Test suite for add_numbers function."""

    def test_add_positive_integers(self):
        """Test adding two positive integers."""
        assert add_numbers(5, 3) == 8

    def test_add_negative_integers(self):
        """Test adding negative integers."""
        assert add_numbers(-5, -3) == -8

    def test_add_mixed_sign_integers(self):
        """Test adding integers with different signs."""
        assert add_numbers(10, -3) == 7

    def test_add_floats(self):
        """Test adding floating point numbers."""
        result = add_numbers(5.5, 2.3)
        assert abs(result - 7.8) < 0.0001  # Float comparison

    def test_add_int_and_float(self):
        """Test adding int and float (duck typing!)."""
        assert add_numbers(5, 2.5) == 7.5

    def test_add_zero(self):
        """Test adding zero."""
        assert add_numbers(0, 0) == 0
        assert add_numbers(5, 0) == 5


class TestMultiply:
    """Test suite for multiply function."""

    def test_multiply_integers(self):
        """Test multiplying integers."""
        assert multiply(5, 3) == 15

    def test_multiply_floats(self):
        """Test multiplying floats."""
        assert multiply(2.5, 3) == 7.5

    def test_multiply_string(self):
        """Test string repetition (duck typing!)."""
        assert multiply("hi", 3) == "hihihi"

    def test_multiply_list(self):
        """Test list repetition (duck typing!)."""
        assert multiply([1, 2], 3) == [1, 2, 1, 2, 1, 2]

    def test_multiply_by_zero(self):
        """Test multiplication by zero."""
        assert multiply(5, 0) == 0
        assert multiply("hi", 0) == ""
        assert multiply([1, 2], 0) == []

    def test_multiply_by_one(self):
        """Test multiplication by one (identity)."""
        assert multiply(5, 1) == 5
        assert multiply("hi", 1) == "hi"
        assert multiply([1, 2], 1) == [1, 2]


class TestDescribeType:
    """Test suite for describe_type function."""

    def test_describe_integer(self):
        """Test describing an integer."""
        assert describe_type(42) == "Integer: 42"

    def test_describe_float(self):
        """Test describing a float."""
        result = describe_type(3.14)
        assert result.startswith("Float:")

    def test_describe_string(self):
        """Test describing a string."""
        assert describe_type("hello") == "String: hello"

    def test_describe_list(self):
        """Test describing a list."""
        assert describe_type([1, 2, 3]) == "List: [1, 2, 3]"

    def test_describe_dict(self):
        """Test describing a dictionary."""
        assert describe_type({"key": "value"}) == "Dictionary: {'key': 'value'}"

    def test_describe_bool(self):
        """Test describing a boolean."""
        assert describe_type(True) == "Boolean: True"

    def test_describe_none(self):
        """Test describing None."""
        assert describe_type(None) == "None: None"


class TestSafeDivide:
    """Test suite for safe_divide function."""

    def test_divide_positive_integers(self):
        """Test dividing positive integers."""
        assert safe_divide(10, 2) == 5.0

    def test_divide_returns_float(self):
        """Test that division always returns float."""
        result = safe_divide(10, 2)
        assert isinstance(result, float)

    def test_divide_with_remainder(self):
        """Test division with remainder."""
        assert safe_divide(10, 3) == pytest.approx(3.333333, rel=1e-5)

    def test_divide_floats(self):
        """Test dividing floats."""
        assert safe_divide(10.5, 2.5) == pytest.approx(4.2)

    def test_divide_negative_numbers(self):
        """Test dividing negative numbers."""
        assert safe_divide(-10, 2) == -5.0
        assert safe_divide(10, -2) == -5.0
        assert safe_divide(-10, -2) == 5.0

    def test_divide_by_zero_raises_value_error(self):
        """Test that dividing by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            safe_divide(10, 0)

    def test_divide_non_numeric_raises_type_error(self):
        """Test that non-numeric arguments raise TypeError."""
        with pytest.raises(TypeError):
            safe_divide("10", 2)

        with pytest.raises(TypeError):
            safe_divide(10, "2")

        with pytest.raises(TypeError):
            safe_divide([10], 2)


class TestProcessData:
    """Test suite for process_data function."""

    def test_process_integer(self):
        """Test processing an integer (should double it)."""
        assert process_data(5) == 10
        assert process_data(0) == 0
        assert process_data(-3) == -6

    def test_process_string(self):
        """Test processing a string (should uppercase it)."""
        assert process_data("hello") == "HELLO"
        assert process_data("Python") == "PYTHON"
        assert process_data("") == ""

    def test_process_list(self):
        """Test processing a list (should sort it)."""
        assert process_data([3, 1, 2]) == [1, 2, 3]
        assert process_data([5, 2, 8, 1]) == [1, 2, 5, 8]
        assert process_data([]) == []

    def test_process_list_of_strings(self):
        """Test sorting a list of strings."""
        assert process_data(["c", "a", "b"]) == ["a", "b", "c"]

    def test_process_invalid_type_raises_error(self):
        """Test that invalid types raise TypeError."""
        with pytest.raises(TypeError):
            process_data(3.14)  # float not supported

        with pytest.raises(TypeError):
            process_data({"key": "value"})  # dict not supported

        with pytest.raises(TypeError):
            process_data(None)


class TestTypeIntrospection:
    """Test type checking and introspection features."""

    def test_type_function(self):
        """Test using type() to get type information."""
        assert type(42) == int
        assert type(3.14) == float
        assert type("hello") == str
        assert type([1, 2]) == list

    def test_isinstance_single_type(self):
        """Test isinstance with a single type."""
        assert isinstance(42, int)
        assert isinstance(3.14, float)
        assert isinstance("hello", str)
        assert not isinstance(42, str)

    def test_isinstance_multiple_types(self):
        """Test isinstance with multiple types (tuple)."""
        assert isinstance(42, (int, float))
        assert isinstance(3.14, (int, float))
        assert not isinstance("hello", (int, float))


class TestDuckTyping:
    """Test duck typing principles."""

    def test_duck_typing_with_multiply(self):
        """Test that multiply works with anything supporting *."""

        # Numbers
        assert multiply(5, 2) == 10

        # Strings
        assert multiply("x", 3) == "xxx"

        # Lists
        assert multiply([1], 4) == [1, 1, 1, 1]

        # Tuples
        assert multiply((1, 2), 2) == (1, 2, 1, 2)

    def test_operations_on_different_types(self):
        """Test that same operation works differently on different types."""

        # + operator
        assert 5 + 3 == 8              # int addition
        assert "hello" + " world" == "hello world"  # string concat
        assert [1, 2] + [3, 4] == [1, 2, 3, 4]      # list concat

        # * operator
        assert 5 * 3 == 15              # int multiplication
        assert "hi" * 3 == "hihihi"     # string repetition
        assert [1] * 3 == [1, 1, 1]     # list repetition


class TestPerformanceImplications:
    """Test and document performance implications."""

    def test_large_dataset_performance(self):
        """Test with larger datasets to show dynamic typing overhead."""
        # This test passes but is slower than static languages
        large_list = list(range(10000))
        result = [x * 2 for x in large_list]
        assert len(result) == 10000
        assert result[0] == 0
        assert result[-1] == 19998

        # NOTE: In Rust, this would be ~100x faster
        # But Python code is ~10x faster to write!


# Performance benchmark (not a test, just documentation)
def test_benchmark_comparison(benchmark_info=True):
    """
    Document performance benchmarks.

    Python (dynamic): ~30ms for 1M additions
    Rust (static):    ~0.01ms for 1M additions
    Speedup:          3000x

    BUT: Python code took 30 seconds to write
         Rust code took 5 minutes to write

    For most applications, developer time > CPU time!
    """
    import time

    # Python benchmark
    start = time.time()
    total = sum(range(10000))
    python_time = time.time() - start

    # This is slower than compiled languages, but faster to write!
    assert total == 49995000  # Verify correctness
    assert python_time < 1.0   # Should be subsecond


if __name__ == "__main__":
    # Run tests with: python test_solution.py
    # Or better: pytest test_solution.py -v
    pytest.main([__file__, "-v"])
