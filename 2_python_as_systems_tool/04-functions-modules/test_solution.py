"""Tests for Project 04: Functions and Modules."""

from pathlib import Path
import sys

import pytest

sys.path.insert(0, str(Path(__file__).parent))

from solution import build_temperature_report, stable_mean, to_celsius


class TestToCelsius:
    def test_celsius_input_is_identity(self):
        # Invariant: converting C -> C should not change numeric meaning.
        assert to_celsius(25, "C") == 25.0

    def test_fahrenheit_conversion(self):
        assert to_celsius(212, "F") == pytest.approx(100.0)

    def test_rejects_bad_unit(self):
        with pytest.raises(ValueError):
            to_celsius(10, "K")

    def test_rejects_non_numeric_value(self):
        with pytest.raises(TypeError):
            to_celsius("10", "C")


class TestStableMean:
    def test_mean_basic(self):
        assert stable_mean([10, 20, 30]) == pytest.approx(20.0)

    def test_mean_rejects_empty(self):
        with pytest.raises(ValueError):
            stable_mean([])

    def test_mean_rejects_bad_element(self):
        with pytest.raises(TypeError):
            stable_mean([1, "x", 3])


class TestBuildTemperatureReport:
    def test_report_for_celsius_inputs(self):
        report = build_temperature_report([10, 15, 20], "C")
        assert report == (3, 10.0, 20.0, 15.0)

    def test_report_for_fahrenheit_inputs(self):
        # Invariant: all report values are normalized to Celsius.
        report = build_temperature_report([32, 68, 212], "F")
        assert report[0] == 3
        assert report[1] == pytest.approx(0.0)
        assert report[2] == pytest.approx(100.0)
        assert report[3] == pytest.approx(40.0)

    def test_rejects_empty_readings(self):
        with pytest.raises(ValueError):
            build_temperature_report([], "C")

    def test_rejects_string_as_readings_iterable(self):
        # Guardrail: a string is iterable but semantically wrong for readings.
        with pytest.raises(TypeError):
            build_temperature_report("123", "C")
