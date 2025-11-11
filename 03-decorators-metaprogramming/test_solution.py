"""
Project 03: Decorators - Test Suite

Run with: pytest test_solution.py -v
"""

import pytest
import time
from io import StringIO
import sys
from solution import timer, repeat, cache, validate_args, debug


class TestTimer:
    """Test timer decorator."""

    def test_timer_measures_time(self, capsys):
        @timer
        def slow_function():
            time.sleep(0.1)
            return "done"

        result = slow_function()

        assert result == "done"
        captured = capsys.readouterr()
        assert "slow_function took" in captured.out
        assert "0.1" in captured.out or "0.0" in captured.out

    def test_timer_preserves_return_value(self):
        @timer
        def add(a, b):
            return a + b

        assert add(2, 3) == 5

    def test_timer_works_with_args(self, capsys):
        @timer
        def multiply(a, b):
            return a * b

        result = multiply(3, 4)
        assert result == 12

        captured = capsys.readouterr()
        assert "multiply took" in captured.out


class TestRepeat:
    """Test repeat decorator factory."""

    def test_repeat_executes_multiple_times(self, capsys):
        @repeat(3)
        def print_hello():
            print("Hello")

        print_hello()

        captured = capsys.readouterr()
        assert captured.out.count("Hello") == 3

    def test_repeat_returns_last_result(self):
        counter = {'value': 0}

        @repeat(5)
        def increment():
            counter['value'] += 1
            return counter['value']

        result = increment()
        assert result == 5
        assert counter['value'] == 5

    def test_repeat_once(self):
        counter = {'value': 0}

        @repeat(1)
        def increment():
            counter['value'] += 1
            return counter['value']

        result = increment()
        assert result == 1


class TestCache:
    """Test cache decorator."""

    def test_cache_stores_results(self):
        call_count = {'value': 0}

        @cache
        def expensive_function(n):
            call_count['value'] += 1
            return n * 2

        # First call - should compute
        result1 = expensive_function(5)
        assert result1 == 10
        assert call_count['value'] == 1

        # Second call with same arg - should use cache
        result2 = expensive_function(5)
        assert result2 == 10
        assert call_count['value'] == 1  # Not incremented!

        # Different arg - should compute again
        result3 = expensive_function(10)
        assert result3 == 20
        assert call_count['value'] == 2

    def test_cache_with_fibonacci(self):
        @cache
        def fibonacci(n):
            if n < 2:
                return n
            return fibonacci(n-1) + fibonacci(n-2)

        # Without cache, fib(30) would take forever
        # With cache, it's instant
        result = fibonacci(30)
        assert result == 832040


class TestValidateArgs:
    """Test validate_args decorator."""

    def test_validate_correct_types(self):
        @validate_args(int, int)
        def add(a, b):
            return a + b

        result = add(2, 3)
        assert result == 5

    def test_validate_raises_on_wrong_type(self):
        @validate_args(int, int)
        def add(a, b):
            return a + b

        with pytest.raises(TypeError):
            add("2", 3)

        with pytest.raises(TypeError):
            add(2, "3")

    def test_validate_multiple_types(self):
        @validate_args(str, int, float)
        def process(name, age, score):
            return f"{name}: {age} years, {score} points"

        result = process("Alice", 30, 95.5)
        assert result == "Alice: 30 years, 95.5 points"

        with pytest.raises(TypeError):
            process(123, 30, 95.5)


class TestDebug:
    """Test debug decorator."""

    def test_debug_prints_call_info(self, capsys):
        @debug
        def add(a, b):
            return a + b

        result = add(2, 3)

        assert result == 5

        captured = capsys.readouterr()
        assert "Calling add(2, 3)" in captured.out
        assert "add returned 5" in captured.out

    def test_debug_with_kwargs(self, capsys):
        @debug
        def greet(name, greeting="Hello"):
            return f"{greeting}, {name}!"

        result = greet("Alice", greeting="Hi")

        assert result == "Hi, Alice!"

        captured = capsys.readouterr()
        assert "Calling greet" in captured.out
        assert "Alice" in captured.out


class TestDecoratorCombinations:
    """Test stacking multiple decorators."""

    def test_timer_and_cache(self, capsys):
        @timer
        @cache
        def slow_fibonacci(n):
            if n < 2:
                return n
            time.sleep(0.001)  # Simulate slow computation
            return slow_fibonacci(n-1) + slow_fibonacci(n-2)

        # First call - slow
        result1 = slow_fibonacci(10)
        assert result1 == 55

        # Second call - should be instant (cached)
        result2 = slow_fibonacci(10)
        assert result2 == 55

        captured = capsys.readouterr()
        assert "took" in captured.out


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
