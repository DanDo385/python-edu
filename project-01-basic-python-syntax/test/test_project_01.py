"""
Tests for Project 01: Basic Python Syntax

This test suite demonstrates comprehensive testing practices including:
- Positive tests (happy path)
- Edge cases (boundary conditions, empty inputs)
- Error handling (exceptions, invalid inputs)
- Property-based tests (optional, with Hypothesis)
- Comparison tests (exercise vs solution)

Test categories:
- TestBasicTypes: Type creation and inspection
- TestArithmetic: All arithmetic operations
- TestTypeConversion: Safe and unsafe conversions
- TestStringFormatting: F-string formatting
- TestBooleanLogic: Boolean expressions and comparisons
- TestAssignment: Variable assignment and swapping
- TestComparison: Value equality vs identity
- TestBMI: Advanced BMI calculator
- TestErrorHandling: Exception raising and handling

Author: Python-50x-Minis
Date: 2025-11-16
"""

import pytest
import sys
from pathlib import Path

# Add parent directory to path to import from project
sys.path.insert(0, str(Path(__file__).parent.parent))

# Import from both exercise and solution for comparison
try:
    import exercise
except ImportError:
    exercise = None

try:
    from solution import solution
except ImportError:
    solution = None


# =============================================================================
# TEST: BASIC TYPES
# =============================================================================

class TestBasicTypes:
    """Test type creation and inspection."""

    def test_explore_types_returns_dict(self):
        """Test that explore_types returns a dictionary."""
        result = solution.explore_types()
        assert isinstance(result, dict)
        assert len(result) == 5

    def test_integer_type(self):
        """Test integer type is correctly identified."""
        result = solution.explore_types()
        assert result['an_integer'] == int

    def test_float_type(self):
        """Test float type is correctly identified."""
        result = solution.explore_types()
        assert result['a_float'] == float

    def test_string_type(self):
        """Test string type is correctly identified."""
        result = solution.explore_types()
        assert result['a_string'] == str

    def test_boolean_type(self):
        """Test boolean type is correctly identified."""
        result = solution.explore_types()
        assert result['a_boolean'] == bool

    def test_none_type(self):
        """Test None type is correctly identified."""
        result = solution.explore_types()
        assert result['a_none'] == type(None)


# =============================================================================
# TEST: ARITHMETIC OPERATIONS
# =============================================================================

class TestArithmetic:
    """Test all arithmetic operations."""

    def test_addition(self):
        """Test addition of two integers."""
        result = solution.perform_arithmetic(10, 3)
        assert result['addition'] == 13

    def test_subtraction(self):
        """Test subtraction of two integers."""
        result = solution.perform_arithmetic(10, 3)
        assert result['subtraction'] == 7

    def test_multiplication(self):
        """Test multiplication of two integers."""
        result = solution.perform_arithmetic(10, 3)
        assert result['multiplication'] == 30

    def test_division_returns_float(self):
        """Test that division always returns float."""
        result = solution.perform_arithmetic(10, 3)
        assert isinstance(result['division'], float)
        assert abs(result['division'] - 3.333333) < 1e-5

    def test_division_exact_result_still_float(self):
        """Test that even exact division returns float."""
        result = solution.perform_arithmetic(10, 5)
        assert result['division'] == 2.0
        assert isinstance(result['division'], float)

    def test_floor_division(self):
        """Test floor division rounds down."""
        result = solution.perform_arithmetic(10, 3)
        assert result['floor_division'] == 3

    def test_floor_division_negative(self):
        """Test floor division with negative numbers rounds toward -infinity."""
        result = solution.perform_arithmetic(-7, 3)
        assert result['floor_division'] == -3  # Not -2!

    def test_modulo(self):
        """Test modulo returns remainder."""
        result = solution.perform_arithmetic(10, 3)
        assert result['modulo'] == 1

    def test_modulo_property(self):
        """Test that a == (a // b) * b + (a % b)."""
        a, b = 10, 3
        result = solution.perform_arithmetic(a, b)
        floor_div = result['floor_division']
        mod = result['modulo']
        assert a == floor_div * b + mod

    def test_exponentiation(self):
        """Test exponentiation (power)."""
        result = solution.perform_arithmetic(10, 3)
        assert result['exponentiation'] == 1000

    def test_exponentiation_zero(self):
        """Test that any number to the power of 0 is 1."""
        # Note: Can't test with b=0 because perform_arithmetic also does division
        # which would raise ZeroDivisionError. Test separately.
        result = solution.perform_arithmetic(42, 1)
        # Test 42**1 = 42 instead
        assert result['exponentiation'] == 42

        # Directly test exponentiation property with 0
        assert 42 ** 0 == 1

    def test_large_numbers(self):
        """Test arithmetic with large numbers (Python handles arbitrary precision)."""
        result = solution.perform_arithmetic(10**10, 2)
        assert result['addition'] == 10**10 + 2
        assert result['multiplication'] == 2 * 10**10


# =============================================================================
# TEST: TYPE CONVERSION
# =============================================================================

class TestTypeConversion:
    """Test type conversion functions."""

    def test_safe_int_convert_valid_string(self):
        """Test converting valid string to int."""
        assert solution.safe_int_convert("42") == 42
        assert solution.safe_int_convert("-17") == -17
        assert solution.safe_int_convert("0") == 0

    def test_safe_int_convert_invalid_string(self):
        """Test that invalid strings return default value."""
        assert solution.safe_int_convert("hello", default=0) == 0
        assert solution.safe_int_convert("3.14", default=-1) == -1
        assert solution.safe_int_convert("", default=999) == 999

    def test_safe_int_convert_default_parameter(self):
        """Test default value defaults to 0."""
        assert solution.safe_int_convert("invalid") == 0

    def test_safe_int_convert_whitespace(self):
        """Test that whitespace is stripped."""
        assert solution.safe_int_convert("  42  ") == 42
        assert solution.safe_int_convert("\t100\n") == 100

    def test_convert_to_float_from_string(self):
        """Test converting string to float."""
        assert solution.convert_to_float("3.14") == 3.14
        assert solution.convert_to_float("-0.5") == -0.5
        assert solution.convert_to_float("1.23e-4") == 0.000123

    def test_convert_to_float_from_int(self):
        """Test converting int to float."""
        assert solution.convert_to_float(42) == 42.0
        assert isinstance(solution.convert_to_float(42), float)

    def test_convert_to_float_invalid_raises_error(self):
        """Test that invalid string raises ValueError."""
        with pytest.raises(ValueError):
            solution.convert_to_float("hello")

    def test_convert_to_float_special_values(self):
        """Test special float values."""
        import math
        assert math.isinf(solution.convert_to_float("inf"))
        assert math.isnan(solution.convert_to_float("nan"))


# =============================================================================
# TEST: STRING FORMATTING
# =============================================================================

class TestStringFormatting:
    """Test string formatting with f-strings."""

    def test_format_person_info_basic(self):
        """Test basic person info formatting."""
        result = solution.format_person_info("Alice", 30, 1.65)
        assert result == "Alice is 30 years old and 1.65 meters tall."

    def test_format_person_info_different_values(self):
        """Test formatting with different values."""
        result = solution.format_person_info("Bob", 25, 1.80)
        assert "Bob" in result
        assert "25" in result
        assert "1.8" in result or "1.80" in result

    def test_format_person_info_returns_string(self):
        """Test that result is a string."""
        result = solution.format_person_info("Charlie", 40, 1.75)
        assert isinstance(result, str)


# =============================================================================
# TEST: BOOLEAN LOGIC
# =============================================================================

class TestBooleanLogic:
    """Test boolean expressions and comparisons."""

    def test_positive_number(self):
        """Test positive number detection."""
        result = solution.check_number_properties(42)
        assert result['is_positive'] is True

    def test_negative_number(self):
        """Test negative number detection."""
        result = solution.check_number_properties(-10)
        assert result['is_positive'] is False

    def test_zero_is_not_positive(self):
        """Test that zero is not positive."""
        result = solution.check_number_properties(0)
        assert result['is_positive'] is False

    def test_even_number(self):
        """Test even number detection."""
        result = solution.check_number_properties(42)
        assert result['is_even'] is True

    def test_odd_number(self):
        """Test odd number detection."""
        result = solution.check_number_properties(43)
        assert result['is_even'] is False

    def test_large_number(self):
        """Test large number detection (> 100)."""
        result = solution.check_number_properties(150)
        assert result['is_large'] is True
        assert result['is_small'] is False

    def test_small_number(self):
        """Test small number detection (< 10)."""
        result = solution.check_number_properties(5)
        assert result['is_small'] is True
        assert result['is_large'] is False

    def test_in_range(self):
        """Test number in range [10, 100]."""
        result = solution.check_number_properties(42)
        assert result['is_in_range'] is True

    def test_out_of_range_low(self):
        """Test number below range."""
        result = solution.check_number_properties(5)
        assert result['is_in_range'] is False

    def test_out_of_range_high(self):
        """Test number above range."""
        result = solution.check_number_properties(150)
        assert result['is_in_range'] is False

    def test_boundary_values(self):
        """Test boundary values of range."""
        result_10 = solution.check_number_properties(10)
        result_100 = solution.check_number_properties(100)
        assert result_10['is_in_range'] is True
        assert result_100['is_in_range'] is True


# =============================================================================
# TEST: VARIABLE ASSIGNMENT
# =============================================================================

class TestAssignment:
    """Test variable assignment and swapping."""

    def test_demonstrate_assignment_returns_tuple(self):
        """Test that function returns a tuple."""
        result = solution.demonstrate_assignment()
        assert isinstance(result, tuple)
        assert len(result) == 3

    def test_assignment_values(self):
        """Test correct values after assignment and swap."""
        a, b, c = solution.demonstrate_assignment()
        # After: a=1, b=2, c=3, then swap a<->b, then c=a+b
        # Expected: a=2, b=1, c=3
        assert a == 2
        assert b == 1
        assert c == 3


# =============================================================================
# TEST: COMPARISON AND IDENTITY
# =============================================================================

class TestComparison:
    """Test value equality vs identity."""

    def test_equal_integers(self):
        """Test equal integer values."""
        result = solution.compare_values(42, 42)
        assert result['equal_value'] is True
        assert result['same_type'] is True

    def test_different_types(self):
        """Test different types are not equal."""
        result = solution.compare_values(42, "42")
        assert result['equal_value'] is False
        assert result['same_type'] is False

    def test_same_identity_small_integers(self):
        """Test that small integers are interned."""
        result = solution.compare_values(42, 42)
        # Small integers (-5 to 256) are cached in CPython
        assert result['same_identity'] is True

    def test_different_identity_lists(self):
        """Test that separate lists have different identity."""
        a = [1, 2, 3]
        b = [1, 2, 3]
        result = solution.compare_values(a, b)
        assert result['equal_value'] is True  # Same values
        assert result['same_identity'] is False  # Different objects

    def test_none_comparison(self):
        """Test None comparison."""
        result = solution.compare_values(None, None)
        assert result['equal_value'] is True
        assert result['same_type'] is True
        assert result['same_identity'] is True  # None is singleton


# =============================================================================
# TEST: BMI CALCULATOR
# =============================================================================

class TestBMI:
    """Test BMI calculation and categorization."""

    def test_calculate_bmi_normal(self):
        """Test BMI calculation for normal weight."""
        result = solution.calculate_bmi(70, 1.75)
        assert abs(result['bmi'] - 22.86) < 0.01
        assert result['category'] == "Normal"

    def test_calculate_bmi_underweight(self):
        """Test BMI categorization: underweight."""
        result = solution.calculate_bmi(50, 1.75)
        assert result['category'] == "Underweight"

    def test_calculate_bmi_overweight(self):
        """Test BMI categorization: overweight."""
        result = solution.calculate_bmi(85, 1.75)
        assert result['category'] == "Overweight"

    def test_calculate_bmi_obese(self):
        """Test BMI categorization: obese."""
        result = solution.calculate_bmi(110, 1.75)
        assert result['category'] == "Obese"

    def test_calculate_bmi_boundary_values(self):
        """Test BMI at category boundaries."""
        # Test boundary at 18.5
        result1 = solution.calculate_bmi(56.5, 1.75)  # ~18.45
        result2 = solution.calculate_bmi(57, 1.75)    # ~18.61
        # One should be Underweight, other Normal
        assert result1['category'] == "Underweight"
        assert result2['category'] == "Normal"

    def test_bmi_rounded_to_two_decimals(self):
        """Test that BMI is rounded to 2 decimal places."""
        result = solution.calculate_bmi(70.123, 1.756)
        bmi_str = str(result['bmi'])
        decimal_part = bmi_str.split('.')[1] if '.' in bmi_str else ""
        assert len(decimal_part) <= 2

    def test_bmi_zero_weight_raises_error(self):
        """Test that zero weight raises ValueError."""
        with pytest.raises(ValueError, match="must be positive"):
            solution.calculate_bmi(0, 1.75)

    def test_bmi_negative_weight_raises_error(self):
        """Test that negative weight raises ValueError."""
        with pytest.raises(ValueError, match="must be positive"):
            solution.calculate_bmi(-70, 1.75)

    def test_bmi_zero_height_raises_error(self):
        """Test that zero height raises ValueError."""
        with pytest.raises(ValueError, match="must be positive"):
            solution.calculate_bmi(70, 0)

    def test_bmi_negative_height_raises_error(self):
        """Test that negative height raises ValueError."""
        with pytest.raises(ValueError, match="must be positive"):
            solution.calculate_bmi(70, -1.75)


# =============================================================================
# TEST: ERROR HANDLING
# =============================================================================

class TestErrorHandling:
    """Test exception handling and edge cases."""

    def test_division_by_zero_raises_error(self):
        """Test that division by zero raises ZeroDivisionError."""
        with pytest.raises(ZeroDivisionError):
            solution.perform_arithmetic(10, 0)

    def test_safe_convert_handles_empty_string(self):
        """Test that empty string is handled gracefully."""
        result = solution.safe_int_convert("", default=-1)
        assert result == -1

    def test_safe_convert_handles_mixed_characters(self):
        """Test that mixed alphanumeric strings return default."""
        result = solution.safe_int_convert("12abc", default=0)
        assert result == 0


# =============================================================================
# TEST: FLOAT PRECISION
# =============================================================================

class TestFloatPrecision:
    """Test floating-point precision edge cases."""

    def test_float_precision_issue(self):
        """Test known floating-point precision issue."""
        # 0.1 + 0.2 != 0.3 in binary floating point!
        result = 0.1 + 0.2
        assert result != 0.3  # This is expected!
        # Use epsilon for comparison
        assert abs(result - 0.3) < 1e-9

    def test_division_precision(self):
        """Test division precision."""
        result = solution.perform_arithmetic(1, 3)
        division = result['division']
        # 1/3 should be ~0.333...
        assert abs(division - (1/3)) < 1e-10


# =============================================================================
# TEST: COMPARISON (Exercise vs Solution)
# =============================================================================

@pytest.mark.skipif(exercise is None, reason="Exercise not implemented")
class TestExerciseSolutionEquivalence:
    """Compare exercise and solution implementations."""

    def test_explore_types_equivalence(self):
        """Test that exercise and solution return same types."""
        if hasattr(exercise, 'explore_types'):
            ex_result = exercise.explore_types()
            sol_result = solution.explore_types()
            if ex_result and sol_result:
                assert ex_result == sol_result

    def test_arithmetic_equivalence(self):
        """Test that exercise and solution produce same arithmetic results."""
        if hasattr(exercise, 'perform_arithmetic'):
            ex_result = exercise.perform_arithmetic(10, 3)
            sol_result = solution.perform_arithmetic(10, 3)
            if ex_result and sol_result:
                assert ex_result == sol_result


# =============================================================================
# TEST: PROPERTY-BASED TESTING (Optional)
# =============================================================================

try:
    from hypothesis import given, strategies as st

    class TestProperties:
        """Property-based tests using Hypothesis."""

        @given(st.integers(min_value=-1000, max_value=1000))
        def test_arithmetic_addition_commutative(self, a):
            """Test that addition is commutative: a + b == b + a."""
            b = 5
            result1 = solution.perform_arithmetic(a, b)
            result2 = solution.perform_arithmetic(b, a)
            assert result1['addition'] == result2['addition']

        @given(st.integers(min_value=1, max_value=1000))
        def test_positive_numbers_always_positive(self, n):
            """Test that positive numbers are always detected as positive."""
            result = solution.check_number_properties(n)
            assert result['is_positive'] is True

        @given(st.integers(min_value=-1000, max_value=-1))
        def test_negative_numbers_never_positive(self, n):
            """Test that negative numbers are never positive."""
            result = solution.check_number_properties(n)
            assert result['is_positive'] is False

        @given(st.integers())
        def test_even_odd_property(self, n):
            """Test that a number is either even or odd (not both)."""
            result = solution.check_number_properties(n)
            is_even = result['is_even']
            # If even, n % 2 should be 0; if odd, n % 2 should be 1
            assert is_even == (n % 2 == 0)

        @given(
            st.floats(min_value=0.1, max_value=200),
            st.floats(min_value=0.5, max_value=2.5)
        )
        def test_bmi_always_positive(self, weight, height):
            """Test that BMI is always positive for positive inputs."""
            try:
                result = solution.calculate_bmi(weight, height)
                assert result['bmi'] > 0
            except ValueError:
                # Valid to raise error for invalid inputs
                pass

except ImportError:
    # Hypothesis not installed, skip property tests
    pass


# =============================================================================
# TEST: PERFORMANCE (Optional)
# =============================================================================

@pytest.mark.slow
class TestPerformance:
    """Basic performance tests."""

    def test_arithmetic_operations_performance(self, benchmark):
        """Benchmark arithmetic operations."""
        # pytest-benchmark required
        if benchmark:
            benchmark(solution.perform_arithmetic, 12345, 67)

    def test_type_conversion_performance(self, benchmark):
        """Benchmark type conversion."""
        if benchmark:
            benchmark(solution.safe_int_convert, "12345", 0)


# =============================================================================
# FIXTURES
# =============================================================================

@pytest.fixture
def sample_arithmetic_data():
    """Provide sample data for arithmetic tests."""
    return [
        (10, 3, {'addition': 13, 'subtraction': 7}),
        (100, 10, {'addition': 110, 'subtraction': 90}),
        (0, 5, {'addition': 5, 'subtraction': -5}),
    ]


@pytest.fixture
def sample_bmi_data():
    """Provide sample BMI test cases."""
    return [
        (50, 1.75, "Underweight"),
        (70, 1.75, "Normal"),
        (85, 1.75, "Overweight"),
        (110, 1.75, "Obese"),
    ]


# =============================================================================
# PARAMETRIZED TESTS
# =============================================================================

class TestParametrized:
    """Parametrized tests for multiple test cases."""

    @pytest.mark.parametrize("a,b,expected_sum", [
        (1, 2, 3),
        (10, 20, 30),
        (-5, 5, 0),
        (5, 10, 15),  # Changed from (0, 0, 0) to avoid division by zero
    ])
    def test_addition_parametrized(self, a, b, expected_sum):
        """Test addition with multiple parameter sets."""
        result = solution.perform_arithmetic(a, b)
        assert result['addition'] == expected_sum

    @pytest.mark.parametrize("n,expected_even", [
        (0, True),
        (1, False),
        (2, True),
        (-2, True),
        (-3, False),
    ])
    def test_even_detection_parametrized(self, n, expected_even):
        """Test even number detection with multiple cases."""
        result = solution.check_number_properties(n)
        assert result['is_even'] == expected_even

    @pytest.mark.parametrize("string,expected", [
        ("42", 42),
        ("-17", -17),
        ("0", 0),
        ("  100  ", 100),
    ])
    def test_safe_int_convert_valid_parametrized(self, string, expected):
        """Test safe_int_convert with valid strings."""
        assert solution.safe_int_convert(string) == expected

    @pytest.mark.parametrize("string,default,expected", [
        ("hello", 0, 0),
        ("3.14", -1, -1),
        ("", 999, 999),
        ("abc123", 42, 42),
    ])
    def test_safe_int_convert_invalid_parametrized(self, string, default, expected):
        """Test safe_int_convert with invalid strings."""
        assert solution.safe_int_convert(string, default) == expected


# =============================================================================
# TEST SUMMARY
# =============================================================================

def test_all_functions_exist():
    """Verify all required functions exist in solution."""
    required_functions = [
        'explore_types',
        'perform_arithmetic',
        'safe_int_convert',
        'convert_to_float',
        'format_person_info',
        'check_number_properties',
        'demonstrate_assignment',
        'compare_values',
        'calculate_bmi',
    ]

    for func_name in required_functions:
        assert hasattr(solution, func_name), f"Missing function: {func_name}"
        assert callable(getattr(solution, func_name)), f"{func_name} is not callable"


if __name__ == "__main__":
    # Run tests with: pytest test_project_01.py -v
    pytest.main([__file__, "-v", "--tb=short"])
