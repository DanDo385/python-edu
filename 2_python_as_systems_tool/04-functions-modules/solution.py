"""
Project 04: Functions and Modules - SOLUTION

Reference implementation with explicit decomposition:
- one function for unit conversion,
- one function for average calculation,
- one orchestration function for final reporting.
"""

from collections.abc import Iterable
from math import fsum
from typing import Tuple


def to_celsius(value: float, unit: str) -> float:
    """Convert one temperature to Celsius after validating inputs."""
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        raise TypeError("value must be an int or float")

    if not isinstance(unit, str):
        raise TypeError("unit must be a string")

    normalized_unit = unit.upper()
    if normalized_unit not in {"C", "F"}:
        raise ValueError("unit must be 'C' or 'F'")

    # Choosing an explicit branch keeps the conversion rule easy to inspect.
    if normalized_unit == "C":
        return float(value)

    return (float(value) - 32.0) * (5.0 / 9.0)


def stable_mean(values: Iterable[float]) -> float:
    """
    Compute an arithmetic mean using fsum for better floating-point stability.

    Design choice:
    - We materialize the iterable once so we can validate, count, and sum
      without consuming a generator multiple times.
    """
    collected = list(values)
    if not collected:
        raise ValueError("values cannot be empty")

    for item in collected:
        if not isinstance(item, (int, float)) or isinstance(item, bool):
            raise TypeError("all values must be numeric")

    return fsum(collected) / len(collected)


def build_temperature_report(
    readings: Iterable[float],
    unit: str = "C",
) -> Tuple[int, float, float, float]:
    """
    Convert readings to Celsius and return:
    (count, min_celsius, max_celsius, average_celsius)
    """
    if isinstance(readings, (str, bytes)):
        raise TypeError("readings must be an iterable of numbers, not a string")

    converted = [to_celsius(value, unit) for value in readings]
    if not converted:
        raise ValueError("readings cannot be empty")

    # Single responsibility for each helper:
    # - to_celsius handles representation conversion
    # - stable_mean handles numerical aggregation
    count = len(converted)
    minimum = min(converted)
    maximum = max(converted)
    average = stable_mean(converted)

    return (count, minimum, maximum, average)


if __name__ == "__main__":
    sample = [68.0, 77.0, 50.0]
    print(build_temperature_report(sample, unit="F"))
