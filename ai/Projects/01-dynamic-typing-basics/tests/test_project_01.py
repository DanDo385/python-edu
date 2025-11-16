"""
Tests for Project 01: Dynamic Typing Basics

Comprehensive test suite covering:
- Type introspection and runtime type checking
- Duck typing implementations
- Type annotations and hints
- Generic functions
- Dynamic type flexibility
- Edge cases and error handling
"""

import pytest
from io import StringIO
from typing import List
from solution.solution import (
    inspect_type,
    count_lines,
    sum_all,
    process_data,
    get_first_and_last,
    safe_divide,
    demonstrate_type_flexibility,
    compare_type_systems,
    demonstrate_duck_typing_polymorphism
)


class TestInspectType:
    """Tests for inspect_type function - runtime type introspection."""

    def test_inspect_integer(self):
        """Test type inspection of integer."""
        result = inspect_type(42)
        assert result['value'] == 42
        assert result['type'] == int
        assert result['type_name'] == 'int'
        assert result['is_mutable'] is False
        assert '__add__' in result['methods']

    def test_inspect_string(self):
        """Test type inspection of string."""
        result = inspect_type("hello")
        assert result['value'] == "hello"
        assert result['type'] == str
        assert result['type_name'] == 'str'
        assert result['is_mutable'] is False
        assert 'upper' in result['methods']
        assert 'lower' in result['methods']

    def test_inspect_list(self):
        """Test type inspection of mutable list."""
        result = inspect_type([1, 2, 3])
        assert result['value'] == [1, 2, 3]
        assert result['type'] == list
        assert result['type_name'] == 'list'
        assert result['is_mutable'] is True
        assert 'append' in result['methods']
        assert 'extend' in result['methods']

    def test_inspect_dict(self):
        """Test type inspection of mutable dictionary."""
        data = {'a': 1, 'b': 2}
        result = inspect_type(data)
        assert result['value'] == data
        assert result['type'] == dict
        assert result['type_name'] == 'dict'
        assert result['is_mutable'] is True
        assert 'keys' in result['methods']
        assert 'values' in result['methods']

    def test_inspect_tuple(self):
        """Test type inspection of immutable tuple."""
        result = inspect_type((1, 2, 3))
        assert result['type'] == tuple
        assert result['type_name'] == 'tuple'
        assert result['is_mutable'] is False

    def test_inspect_set(self):
        """Test type inspection of mutable set."""
        result = inspect_type({1, 2, 3})
        assert result['type'] == set
        assert result['type_name'] == 'set'
        assert result['is_mutable'] is True
        assert 'add' in result['methods']

    def test_inspect_none(self):
        """Test type inspection of None."""
        result = inspect_type(None)
        assert result['value'] is None
        assert result['type'] == type(None)
        assert result['type_name'] == 'NoneType'
        assert result['is_mutable'] is False

    def test_inspect_float(self):
        """Test type inspection of float."""
        result = inspect_type(3.14)
        assert result['type'] == float
        assert result['type_name'] == 'float'
        assert result['is_mutable'] is False

    def test_inspect_boolean(self):
        """Test type inspection of boolean."""
        result = inspect_type(True)
        assert result['type'] == bool
        assert result['type_name'] == 'bool'
        assert result['is_mutable'] is False


class TestCountLines:
    """Tests for count_lines function - duck typing with file-like objects."""

    def test_count_lines_stringio(self):
        """Test counting lines in StringIO object."""
        file_obj = StringIO("line1\nline2\nline3")
        assert count_lines(file_obj) == 3

    def test_count_lines_stringio_single(self):
        """Test with single line."""
        file_obj = StringIO("single line")
        assert count_lines(file_obj) == 1

    def test_count_lines_stringio_empty(self):
        """Test with empty StringIO."""
        file_obj = StringIO("")
        assert count_lines(file_obj) == 0

    def test_count_lines_list(self):
        """Test counting lines in list (duck typing)."""
        lines = ["hello", "world", "python"]
        assert count_lines(lines) == 3

    def test_count_lines_tuple(self):
        """Test counting lines in tuple."""
        lines = ("first", "second", "third", "fourth")
        assert count_lines(lines) == 4

    def test_count_lines_empty_list(self):
        """Test with empty list."""
        assert count_lines([]) == 0

    def test_count_lines_generator(self):
        """Test counting lines from generator."""
        def line_generator():
            yield "line 1"
            yield "line 2"
            yield "line 3"

        assert count_lines(line_generator()) == 3

    def test_count_lines_non_iterable(self):
        """Test that non-iterable raises TypeError."""
        with pytest.raises(TypeError, match="not iterable"):
            count_lines(42)

    def test_count_lines_multiline_stringio(self):
        """Test with multiple newlines."""
        file_obj = StringIO("line1\nline2\n\nline4\nline5")
        # StringIO splits on newlines, empty line counts as a line
        result = count_lines(file_obj)
        assert result == 5


class TestSumAll:
    """Tests for sum_all function - duck typing with iterables."""

    def test_sum_all_list(self):
        """Test summing list of integers."""
        assert sum_all([1, 2, 3, 4, 5]) == 15.0

    def test_sum_all_tuple(self):
        """Test summing tuple of floats."""
        assert sum_all((1.5, 2.5, 3.0)) == 7.0

    def test_sum_all_range(self):
        """Test summing range object."""
        assert sum_all(range(10)) == 45.0

    def test_sum_all_set(self):
        """Test summing set (unordered but works)."""
        result = sum_all({1, 2, 3})
        assert result == 6.0

    def test_sum_all_mixed_types(self):
        """Test summing mixed int/float."""
        assert sum_all([1, 2.5, 3, 4.5]) == 11.0

    def test_sum_all_empty(self):
        """Test summing empty iterable."""
        assert sum_all([]) == 0.0

    def test_sum_all_single(self):
        """Test summing single element."""
        assert sum_all([42]) == 42.0

    def test_sum_all_negative(self):
        """Test summing negative numbers."""
        assert sum_all([-1, -2, -3]) == -6.0

    def test_sum_all_generator(self):
        """Test summing generator expression."""
        gen = (x * 2 for x in range(5))
        assert sum_all(gen) == 20.0

    def test_sum_all_non_iterable(self):
        """Test that non-iterable raises TypeError."""
        with pytest.raises(TypeError, match="not iterable"):
            sum_all(42)

    def test_sum_all_non_numeric(self):
        """Test that non-numeric values raise TypeError."""
        with pytest.raises(TypeError):
            sum_all(["a", "b", "c"])


class TestProcessData:
    """Tests for process_data function - type annotations demonstration."""

    def test_process_data_double(self):
        """Test processing with doubling operation."""
        def double(x: int) -> int:
            return x * 2

        result = process_data([1, 2, 3, 4], double)
        assert result['sum'] == 20
        assert result['average'] == 5.0
        assert result['count'] == 4

    def test_process_data_square(self):
        """Test processing with squaring operation."""
        def square(x: int) -> int:
            return x * x

        result = process_data([2, 3, 4], square)
        assert result['sum'] == 29  # 4 + 9 + 16
        assert abs(result['average'] - 9.666666666666666) < 0.0001
        assert result['count'] == 3

    def test_process_data_identity(self):
        """Test processing with identity operation."""
        def identity(x: int) -> int:
            return x

        result = process_data([5, 10, 15], identity)
        assert result['sum'] == 30
        assert result['average'] == 10.0
        assert result['count'] == 3

    def test_process_data_empty_with_default(self):
        """Test processing empty list with default value."""
        def double(x: int) -> int:
            return x * 2

        result = process_data([], double, default=0)
        assert result['sum'] == 0
        assert result['average'] == 0.0
        assert result['count'] == 0

    def test_process_data_empty_without_default(self):
        """Test processing empty list without explicit default."""
        def double(x: int) -> int:
            return x * 2

        result = process_data([], double)
        assert result['sum'] == 0  # Uses default 0
        assert result['average'] == 0.0
        assert result['count'] == 0

    def test_process_data_negative_numbers(self):
        """Test processing negative numbers."""
        def negate(x: int) -> int:
            return -x

        result = process_data([1, 2, 3], negate)
        assert result['sum'] == -6
        assert result['average'] == -2.0
        assert result['count'] == 3

    def test_process_data_single_element(self):
        """Test processing single element."""
        def triple(x: int) -> int:
            return x * 3

        result = process_data([7], triple)
        assert result['sum'] == 21
        assert result['average'] == 21.0
        assert result['count'] == 1

    def test_process_data_lambda(self):
        """Test processing with lambda function."""
        result = process_data([1, 2, 3], lambda x: x + 10)
        assert result['sum'] == 33  # 11 + 12 + 13
        assert result['average'] == 11.0
        assert result['count'] == 3


class TestGetFirstAndLast:
    """Tests for get_first_and_last function - generic types."""

    def test_get_first_and_last_integers(self):
        """Test with list of integers."""
        result = get_first_and_last([1, 2, 3, 4, 5])
        assert result == (1, 5)

    def test_get_first_and_last_strings(self):
        """Test with list of strings."""
        result = get_first_and_last(["apple", "banana", "cherry", "date"])
        assert result == ("apple", "date")

    def test_get_first_and_last_floats(self):
        """Test with list of floats."""
        result = get_first_and_last([3.14, 2.71, 1.41, 1.73])
        assert result == (3.14, 1.73)

    def test_get_first_and_last_two_elements(self):
        """Test with exactly two elements (minimum)."""
        result = get_first_and_last([10, 20])
        assert result == (10, 20)

    def test_get_first_and_last_mixed_types(self):
        """Test with mixed types (Python allows this)."""
        result = get_first_and_last([1, "two", 3.0, True, "five"])
        assert result == (1, "five")

    def test_get_first_and_last_one_element(self):
        """Test that single element raises ValueError."""
        with pytest.raises(ValueError, match="at least 2 elements"):
            get_first_and_last([42])

    def test_get_first_and_last_empty(self):
        """Test that empty list raises ValueError."""
        with pytest.raises(ValueError, match="at least 2 elements"):
            get_first_and_last([])

    def test_get_first_and_last_large_list(self):
        """Test with large list (performance check)."""
        large_list = list(range(10000))
        result = get_first_and_last(large_list)
        assert result == (0, 9999)


class TestSafeDivide:
    """Tests for safe_divide function - Union and Optional types."""

    def test_safe_divide_normal(self):
        """Test normal division."""
        assert safe_divide(10, 2) == 5.0

    def test_safe_divide_float_result(self):
        """Test division with non-integer result."""
        result = safe_divide(7, 3)
        assert abs(result - 2.333333333333333) < 0.0001

    def test_safe_divide_zero_denominator(self):
        """Test division by zero returns None."""
        assert safe_divide(5, 0) is None

    def test_safe_divide_zero_numerator(self):
        """Test zero divided by non-zero."""
        assert safe_divide(0, 5) == 0.0

    def test_safe_divide_both_floats(self):
        """Test division with both floats."""
        assert safe_divide(7.5, 2.5) == 3.0

    def test_safe_divide_mixed_types(self):
        """Test division with int and float."""
        assert safe_divide(10, 2.5) == 4.0
        assert safe_divide(7.5, 2) == 3.75

    def test_safe_divide_negative_numbers(self):
        """Test division with negative numbers."""
        assert safe_divide(-10, 2) == -5.0
        assert safe_divide(10, -2) == -5.0
        assert safe_divide(-10, -2) == 5.0

    def test_safe_divide_large_numbers(self):
        """Test division with large numbers."""
        result = safe_divide(1000000, 3)
        assert abs(result - 333333.333333333) < 0.001

    def test_safe_divide_small_numbers(self):
        """Test division with small numbers."""
        result = safe_divide(0.001, 0.0001)
        assert abs(result - 10.0) < 0.0001


class TestDemonstrateTypeFlexibility:
    """Tests for demonstrate_type_flexibility function."""

    def test_returns_list_of_tuples(self):
        """Test that function returns list of tuples."""
        result = demonstrate_type_flexibility()
        assert isinstance(result, list)
        assert len(result) > 0
        assert all(isinstance(item, tuple) for item in result)

    def test_tuple_structure(self):
        """Test that each tuple has correct structure."""
        result = demonstrate_type_flexibility()
        for item in result:
            assert len(item) == 3
            assert isinstance(item[0], str)  # example code
            assert isinstance(item[1], str)  # type name
            assert isinstance(item[2], str)  # explanation

    def test_contains_type_change_example(self):
        """Test that result includes type change example."""
        result = demonstrate_type_flexibility()
        # First example should show variable type changing
        assert result[0][1] == 'int'
        assert 'int' in result[0][2] and 'str' in result[0][2]

    def test_contains_mutable_example(self):
        """Test that result includes mutable type example."""
        result = demonstrate_type_flexibility()
        # Second example should be about list (mutable)
        assert result[1][1] == 'list'
        assert 'mutable' in result[1][2]

    def test_contains_immutable_example(self):
        """Test that result includes immutable type example."""
        result = demonstrate_type_flexibility()
        # Third example should be about string (immutable)
        assert result[2][1] == 'str'
        assert 'immutable' in result[2][2]

    def test_minimum_examples(self):
        """Test that there are multiple examples."""
        result = demonstrate_type_flexibility()
        assert len(result) >= 3


class TestCompareTypeSystems:
    """Tests for compare_type_systems educational function."""

    def test_returns_dict(self):
        """Test that function returns dictionary."""
        result = compare_type_systems()
        assert isinstance(result, dict)

    def test_has_python_and_java(self):
        """Test that comparison includes Python and Java."""
        result = compare_type_systems()
        assert 'python_dynamic' in result
        assert 'java_static' in result

    def test_python_characteristics(self):
        """Test Python characteristics are correct."""
        result = compare_type_systems()
        python = result['python_dynamic']
        assert python['type_checking'] == 'Runtime'
        assert 'Optional' in python['type_declaration']
        assert python['flexibility'] == 'High'

    def test_java_characteristics(self):
        """Test Java characteristics are correct."""
        result = compare_type_systems()
        java = result['java_static']
        assert java['type_checking'] == 'Compile-time'
        assert java['type_declaration'] == 'Required'
        assert java['flexibility'] == 'Lower'


class TestDemonstrateDuckTypingPolymorphism:
    """Tests for duck typing polymorphism demonstration."""

    def test_returns_string(self):
        """Test that function returns string."""
        result = demonstrate_duck_typing_polymorphism()
        assert isinstance(result, str)

    def test_mentions_duck_typing(self):
        """Test that result mentions duck typing."""
        result = demonstrate_duck_typing_polymorphism()
        assert 'duck typing' in result.lower() or 'Duck typing' in result

    def test_mentions_polymorphism(self):
        """Test that result mentions polymorphism."""
        result = demonstrate_duck_typing_polymorphism()
        assert 'polymorphism' in result.lower()

    def test_non_empty(self):
        """Test that result is not empty."""
        result = demonstrate_duck_typing_polymorphism()
        assert len(result) > 0


# Integration Tests
class TestIntegration:
    """Integration tests combining multiple functions."""

    def test_type_inspection_workflow(self):
        """Test complete type inspection workflow."""
        # Create various objects
        objects = [42, "hello", [1, 2, 3], {"key": "value"}, (1, 2)]

        # Inspect each
        for obj in objects:
            info = inspect_type(obj)
            assert 'type_name' in info
            assert 'is_mutable' in info
            assert isinstance(info['methods'], list)

    def test_duck_typing_workflow(self):
        """Test duck typing with various iterables."""
        # Different iterables, same interface
        iterables = [
            [1, 2, 3, 4, 5],
            (1, 2, 3, 4, 5),
            range(1, 6),
            {1, 2, 3, 4, 5}
        ]

        for iterable in iterables:
            result = sum_all(iterable)
            assert result == 15.0

    def test_generic_function_workflow(self):
        """Test generic functions with different types."""
        # Test with integers
        int_list = [1, 2, 3, 4, 5]
        int_result = get_first_and_last(int_list)
        assert int_result == (1, 5)

        # Test with strings
        str_list = ["first", "middle", "last"]
        str_result = get_first_and_last(str_list)
        assert str_result == ("first", "last")

    def test_type_annotation_workflow(self):
        """Test type-annotated function workflow."""
        operations = [
            (lambda x: x * 2, [1, 2, 3], 12),
            (lambda x: x + 5, [0, 5, 10], 30),
            (lambda x: x ** 2, [1, 2, 3], 14)
        ]

        for operation, data, expected_sum in operations:
            result = process_data(data, operation)
            assert result['sum'] == expected_sum


# Performance Tests
class TestPerformance:
    """Performance and edge case tests."""

    def test_inspect_type_performance(self):
        """Test type inspection with large object."""
        large_list = list(range(10000))
        result = inspect_type(large_list)
        assert result['type_name'] == 'list'
        assert result['is_mutable'] is True

    def test_sum_all_performance(self):
        """Test summing large iterable."""
        large_range = range(100000)
        result = sum_all(large_range)
        assert result == 4999950000.0

    def test_count_lines_performance(self):
        """Test counting many lines."""
        many_lines = ["line"] * 10000
        result = count_lines(many_lines)
        assert result == 10000

    def test_process_data_performance(self):
        """Test processing large dataset."""
        large_data = list(range(1000))
        result = process_data(large_data, lambda x: x * 2)
        assert result['count'] == 1000
        assert result['sum'] == sum(range(1000)) * 2


# Edge Cases
class TestEdgeCases:
    """Test edge cases and boundary conditions."""

    def test_inspect_type_complex_object(self):
        """Test inspecting complex nested object."""
        complex_obj = {
            'list': [1, 2, 3],
            'dict': {'nested': True},
            'tuple': (4, 5, 6)
        }
        result = inspect_type(complex_obj)
        assert result['type_name'] == 'dict'

    def test_safe_divide_float_precision(self):
        """Test safe divide with floating point precision."""
        result = safe_divide(1, 3)
        assert result is not None
        assert abs(result - 0.333333333333333) < 0.0001

    def test_sum_all_zero_values(self):
        """Test summing list of zeros."""
        assert sum_all([0, 0, 0, 0]) == 0.0

    def test_get_first_and_last_same_values(self):
        """Test with all same values."""
        result = get_first_and_last([5, 5, 5, 5])
        assert result == (5, 5)

    def test_process_data_all_zeros(self):
        """Test processing all zeros."""
        result = process_data([0, 0, 0], lambda x: x)
        assert result['sum'] == 0
        assert result['average'] == 0.0
