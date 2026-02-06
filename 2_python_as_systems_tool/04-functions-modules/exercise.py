"""
Project 04: Functions and Modules

Implement a small temperature-report pipeline using helper functions.
Run: pytest test_solution.py -v
"""

from collections.abc import Iterable
from typing import Tuple


def to_celsius(value: float, unit: str) -> float:
    """
    Convert one temperature reading to Celsius.

    Args:
        value: Numeric temperature value.
        unit: Either "C" or "F" (case-insensitive).

    Returns:
        Temperature converted to Celsius.

    Raises:
        TypeError: If value is not numeric or unit is not a string.
        ValueError: If unit is not "C" or "F".
    """
    # TODO: Validate inputs and convert F -> C with (value - 32) * 5 / 9.
    pass


def stable_mean(values: Iterable[float]) -> float:
    """
    Compute arithmetic mean for numeric values.

    Args:
        values: Iterable of numbers.

    Returns:
        Mean value as float.

    Raises:
        TypeError: If any element is non-numeric.
        ValueError: If values is empty.
    """
    # TODO: Convert iterable to a list, validate non-empty, and compute mean.
    pass


def build_temperature_report(
    readings: Iterable[float],
    unit: str = "C",
) -> Tuple[int, float, float, float]:
    """
    Build a summary tuple for temperature readings.

    The report is:
        (count, min_celsius, max_celsius, average_celsius)

    Args:
        readings: Iterable of raw readings.
        unit: Unit of all readings ("C" or "F").

    Returns:
        4-tuple: count, min, max, average (all in Celsius).

    Raises:
        TypeError: If readings is not an iterable of numbers.
        ValueError: If readings is empty.
    """
    # TODO: Validate readings, convert each reading to Celsius, and summarize.
    pass


if __name__ == "__main__":
    sample = [68.0, 77.0, 50.0]
    print(build_temperature_report(sample, unit="F"))
