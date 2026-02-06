"""
Tests for Project 01: Basic Python Syntax - Dynamic Typing Basics

Test categories:
- Positive tests: Happy path, expected behavior
- Edge cases: Boundary conditions, empty inputs, None handling
- Error cases: Invalid inputs, type errors
- Performance: Basic benchmarks (where relevant)

Author: Python-50x-Minis
"""

import pytest
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

# Import from both exercise and solution for comparison
# Using aliases to differentiate between exercise and solution functions
try:
    from exercise import (
        add_numbers as exercise_add_numbers,
        multiply as exercise_multiply,
        describe_type as exercise_describe_type,
        safe_divide as exercise_safe_divide,
        process_data as exercise_process_data,
    )
except ImportError:
    exercise_add_numbers = None
    exercise_multiply = None
    exercise_describe_type = None
    exercise_safe_divide = None
    exercise_process_data = None

try:
    from solution import (
        add_numbers as solution_add_numbers,
        multiply as solution_multiply,
        describe_type as solution_describe_type,
        safe_divide as solution_safe_divide,
        process_data as solution_process_data,
    )
except ImportError:
    solution_add_numbers = None
    solution_multiply = None
    solution_describe_type = None
    solution_safe_divide = None
    solution_process_data = None


# Helper to run tests against both exercise and solution if available
def run_test_against_both(test_func_name, *args, **kwargs):
    if exercise_add_numbers is not None:
        getattr(TestAddNumbers(), test_func_name)(exercise_add_numbers, *args, **kwargs)
    if solution_add_numbers is not None:
        getattr(TestAddNumbers(), test_func_name)(solution_add_numbers, *args, **kwargs)


class TestAddNumbers:
    """Test suite for add_numbers function."""

    @pytest.mark.parametrize("func", [exercise_add_numbers, solution_add_numbers])
    @pytest.mark.skipif(exercise_add_numbers is None and solution_add_numbers is None,
                        reason="add_numbers function not implemented in exercise or solution")
    def test_add_positive_integers(self, func):
        """Test adding two positive integers."""
        if func:
            assert func(5, 3) == 8

    @pytest.mark.parametrize("func", [exercise_add_numbers, solution_add_numbers])
    @pytest.mark.skipif(exercise_add_numbers is None and solution_add_numbers is None,
                        reason="add_numbers function not implemented in exercise or solution")
    def test_add_negative_integers(self, func):
        """Test adding negative integers."""
        if func:
            assert func(-5, -3) == -8

    @pytest.mark.parametrize("func", [exercise_add_numbers, solution_add_numbers])
    @pytest.mark.skipif(exercise_add_numbers is None and solution_add_numbers is None,
                        reason="add_numbers function not implemented in exercise or solution")
    def test_add_mixed_sign_integers(self, func):
        """Test adding integers with different signs."""
        if func:
            assert func(10, -3) == 7

    @pytest.mark.parametrize("func", [exercise_add_numbers, solution_add_numbers])
    @pytest.mark.skipif(exercise_add_numbers is None and solution_add_numbers is None,
                        reason="add_numbers function not implemented in exercise or solution")
    def test_add_floats(self, func):
        """Test adding floating point numbers."""
        if func:
            result = func(5.5, 2.3)
            assert abs(result - 7.8) < 0.0001  # Float comparison

    @pytest.mark.parametrize("func", [exercise_add_numbers, solution_add_numbers])
    @pytest.mark.skipif(exercise_add_numbers is None and solution_add_numbers is None,
                        reason="add_numbers function not implemented in exercise or solution")
    def test_add_int_and_float(self, func):
        """Test adding int and float (duck typing!)."""
        if func:
            assert func(5, 2.5) == 7.5

    @pytest.mark.parametrize("func", [exercise_add_numbers, solution_add_numbers])
    @pytest.mark.skipif(exercise_add_numbers is None and solution_add_numbers is None,
                        reason="add_numbers function not implemented in exercise or solution")
    def test_add_zero(self, func):
        """Test adding zero."""
        if func:
            assert func(0, 0) == 0
            assert func(5, 0) == 5


class TestMultiply:
    """Test suite for multiply function."""

    @pytest.mark.parametrize("func", [exercise_multiply, solution_multiply])
    @pytest.mark.skipif(exercise_multiply is None and solution_multiply is None,
                        reason="multiply function not implemented in exercise or solution")
    def test_multiply_integers(self, func):
        """Test multiplying integers."""
        if func:
            assert func(5, 3) == 15

    @pytest.mark.parametrize("func", [exercise_multiply, solution_multiply])
    @pytest.mark.skipif(exercise_multiply is None and solution_multiply is None,
                        reason="multiply function not implemented in exercise or solution")
    def test_multiply_floats(self, func):
        """Test multiplying floats."""
        if func:
            assert func(2.5, 3) == 7.5

    @pytest.mark.parametrize("func", [exercise_multiply, solution_multiply])
    @pytest.mark.skipif(exercise_multiply is None and solution_multiply is None,
                        reason="multiply function not implemented in exercise or solution")
    def test_multiply_string(self, func):
        """Test string repetition (duck typing!)."""
        if func:
            assert func("hi", 3) == "hihihi"

    @pytest.mark.parametrize("func", [exercise_multiply, solution_multiply])
    @pytest.mark.skipif(exercise_multiply is None and solution_multiply is None,
                        reason="multiply function not implemented in exercise or solution")
    def test_multiply_list(self, func):
        """Test list repetition (duck typing!)."""
        if func:
            assert func([1, 2], 3) == [1, 2, 1, 2, 1, 2]

    @pytest.mark.parametrize("func", [exercise_multiply, solution_multiply])
    @pytest.mark.skipif(exercise_multiply is None and solution_multiply is None,
                        reason="multiply function not implemented in exercise or solution")
    def test_multiply_by_zero(self, func):
        """Test multiplication by zero."""
        if func:
            assert func(5, 0) == 0
            assert func("hi", 0) == ""
            assert func([1, 2], 0) == []

    @pytest.mark.parametrize("func", [exercise_multiply, solution_multiply])
    @pytest.mark.skipif(exercise_multiply is None and solution_multiply is None,
                        reason="multiply function not implemented in exercise or solution")
    def test_multiply_by_one(self, func):
        """Test multiplication by one (identity)."""
        if func:
            assert func(5, 1) == 5
            assert func("hi", 1) == "hi"
            assert func([1, 2], 1) == [1, 2]


class TestDescribeType:
    """Test suite for describe_type function."""

    @pytest.mark.parametrize("func", [exercise_describe_type, solution_describe_type])
    @pytest.mark.skipif(exercise_describe_type is None and solution_describe_type is None,
                        reason="describe_type function not implemented in exercise or solution")
    def test_describe_integer(self, func):
        """Test describing an integer."""
        if func:
            assert func(42) == "Integer: 42"

    @pytest.mark.parametrize("func", [exercise_describe_type, solution_describe_type])
    @pytest.mark.skipif(exercise_describe_type is None and solution_describe_type is None,
                        reason="describe_type function not implemented in exercise or solution")
    def test_describe_float(self, func):
        """Test describing a float."""
        if func:
            result = func(3.14)
            assert result.startswith("Float:")

    @pytest.mark.parametrize("func", [exercise_describe_type, solution_describe_type])
    @pytest.mark.skipif(exercise_describe_type is None and solution_describe_type is None,
                        reason="describe_type function not implemented in exercise or solution")
    def test_describe_string(self, func):
        """Test describing a string."""
        if func:
            assert func("hello") == "String: hello"

    @pytest.mark.parametrize("func", [exercise_describe_type, solution_describe_type])
    @pytest.mark.skipif(exercise_describe_type is None and solution_describe_type is None,
                        reason="describe_type function not implemented in exercise or solution")
    def test_describe_list(self, func):
        """Test describing a list."""
        if func:
            assert func([1, 2, 3]) == "List: [1, 2, 3]"

    @pytest.mark.parametrize("func", [exercise_describe_type, solution_describe_type])
    @pytest.mark.skipif(exercise_describe_type is None and solution_describe_type is None,
                        reason="describe_type function not implemented in exercise or solution")
    def test_describe_dict(self, func):
        """Test describing a dictionary."""
        if func:
            assert func({"key": "value"}) == "Dictionary: {'key': 'value'}"

    @pytest.mark.parametrize("func", [exercise_describe_type, solution_describe_type])
    @pytest.mark.skipif(exercise_describe_type is None and solution_describe_type is None,
                        reason="describe_type function not implemented in exercise or solution")
    def test_describe_bool(self, func):
        """Test describing a boolean."""
        if func:
            assert func(True) == "Boolean: True"

    @pytest.mark.parametrize("func", [exercise_describe_type, solution_describe_type])
    @pytest.mark.skipif(exercise_describe_type is None and solution_describe_type is None,
                        reason="describe_type function not implemented in exercise or solution")
    def test_describe_none(self, func):
        """Test describing None."""
        if func:
            assert func(None) == "None: None"


class TestSafeDivide:
    """Test suite for safe_divide function."""

    @pytest.mark.parametrize("func", [exercise_safe_divide, solution_safe_divide])
    @pytest.mark.skipif(exercise_safe_divide is None and solution_safe_divide is None,
                        reason="safe_divide function not implemented in exercise or solution")
    def test_divide_positive_integers(self, func):
        """Test dividing positive integers."""
        if func:
            assert func(10, 2) == 5.0

    @pytest.mark.parametrize("func", [exercise_safe_divide, solution_safe_divide])
    @pytest.mark.skipif(exercise_safe_divide is None and solution_safe_divide is None,
                        reason="safe_divide function not implemented in exercise or solution")
    def test_divide_returns_float(self, func):
        """Test that division always returns float."""
        if func:
            result = func(10, 2)
            assert isinstance(result, float)

    @pytest.mark.parametrize("func", [exercise_safe_divide, solution_safe_divide])
    @pytest.mark.skipif(exercise_safe_divide is None and solution_safe_divide is None,
                        reason="safe_divide function not implemented in exercise or solution")
    def test_divide_with_remainder(self, func):
        """Test division with remainder."""
        if func:
            assert func(10, 3) == pytest.approx(3.333333, rel=1e-5)

    @pytest.mark.parametrize("func", [exercise_safe_divide, solution_safe_divide])
    @pytest.mark.skipif(exercise_safe_divide is None and solution_safe_divide is None,
                        reason="safe_divide function not implemented in exercise or solution")
    def test_divide_floats(self, func):
        """Test dividing floats."""
        if func:
            assert func(10.5, 2.5) == pytest.approx(4.2)

    @pytest.mark.parametrize("func", [exercise_safe_divide, solution_safe_divide])
    @pytest.mark.skipif(exercise_safe_divide is None and solution_safe_divide is None,
                        reason="safe_divide function not implemented in exercise or solution")
    def test_divide_negative_numbers(self, func):
        """Test dividing negative numbers."""
        if func:
            assert func(-10, 2) == -5.0
            assert func(10, -2) == -5.0
            assert func(-10, -2) == 5.0

    @pytest.mark.parametrize("func", [exercise_safe_divide, solution_safe_divide])
    @pytest.mark.skipif(exercise_safe_divide is None and solution_safe_divide is None,
                        reason="safe_divide function not implemented in exercise or solution")
    def test_divide_by_zero_raises_value_error(self, func):
        """Test that dividing by zero raises ValueError."""
        if func:
            with pytest.raises(ValueError, match="Cannot divide by zero"):
                func(10, 0)

    @pytest.mark.parametrize("func", [exercise_safe_divide, solution_safe_divide])
    @pytest.mark.skipif(exercise_safe_divide is None and solution_safe_divide is None,
                        reason="safe_divide function not implemented in exercise or solution")
    def test_divide_non_numeric_raises_type_error(self, func):
        """Test that non-numeric arguments raise TypeError."""
        if func:
            with pytest.raises(TypeError):
                func("10", 2)

            with pytest.raises(TypeError):
                func(10, "2")

            with pytest.raises(TypeError):
                func([10], 2)


class TestProcessData:
    """Test suite for process_data function."""

    @pytest.mark.parametrize("func", [exercise_process_data, solution_process_data])
    @pytest.mark.skipif(exercise_process_data is None and solution_process_data is None,
                        reason="process_data function not implemented in exercise or solution")
    def test_process_integer(self, func):
        """Test processing an integer (should double it)."""
        if func:
            assert func(5) == 10
            assert func(0) == 0
            assert func(-3) == -6

    @pytest.mark.parametrize("func", [exercise_process_data, solution_process_data])
    @pytest.mark.skipif(exercise_process_data is None and solution_process_data is None,
                        reason="process_data function not implemented in exercise or solution")
    def test_process_string(self, func):
        """Test processing a string (should uppercase it)."""
        if func:
            assert func("hello") == "HELLO"
            assert func("Python") == "PYTHON"
            assert func("") == ""

    @pytest.mark.parametrize("func", [exercise_process_data, solution_process_data])
    @pytest.mark.skipif(exercise_process_data is None and solution_process_data is None,
                        reason="process_data function not implemented in exercise or solution")
    def test_process_list(self, func):
        """Test processing a list (should sort it)."""
        if func:
            assert func([3, 1, 2]) == [1, 2, 3]
            assert func([5, 2, 8, 1]) == [1, 2, 5, 8]
            assert func([]) == []

    @pytest.mark.parametrize("func", [exercise_process_data, solution_process_data])
    @pytest.mark.skipif(exercise_process_data is None and solution_process_data is None,
                        reason="process_data function not implemented in exercise or solution")
    def test_process_list_of_strings(self, func):
        """Test sorting a list of strings."""
        if func:
            assert func(["c", "a", "b"]) == ["a", "b", "c"]

    @pytest.mark.parametrize("func", [exercise_process_data, solution_process_data])
    @pytest.mark.skipif(exercise_process_data is None and solution_process_data is None,
                        reason="process_data function not implemented in exercise or solution")
    def test_process_invalid_type_raises_error(self, func):
        """Test that invalid types raise TypeError."""
        if func:
            with pytest.raises(TypeError):
                func(3.14)  # float not supported

            with pytest.raises(TypeError):
                func({"key": "value"})  # dict not supported

            with pytest.raises(TypeError):
                func(None)


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

    @pytest.mark.parametrize("func", [exercise_multiply, solution_multiply])
    @pytest.mark.skipif(exercise_multiply is None and solution_multiply is None,
                        reason="multiply function not implemented in exercise or solution")
    def test_duck_typing_with_multiply(self, func):
        """Test that multiply works with anything supporting *."""
        if func:
            # Numbers
            assert func(5, 2) == 10

            # Strings
            assert func("x", 3) == "xxx"

            # Lists
            assert func([1], 4) == [1, 1, 1, 1]

            # Tuples
            assert func((1, 2), 2) == (1, 2, 1, 2)

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

    @pytest.mark.parametrize("func", [exercise_process_data, solution_process_data]) # using process_data for a testable function
    @pytest.mark.skipif(exercise_process_data is None and solution_process_data is None,
                        reason="process_data function not implemented in exercise or solution")
    def test_large_dataset_performance(self, func):
        """Test with larger datasets to show dynamic typing overhead."""
        if func:
            # This test passes but is slower than static languages
            large_list = list(range(10000))
            result = [func(x) for x in large_list if isinstance(x, int)] # only ints, assuming it's for int processing
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
    pytest.main([__file__, "-v"])
