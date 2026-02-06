"""Test suite for Project 10: Sorting"""
import pytest
from exercise import insertion_sort, merge_sort, merge

def test_insertion_sort():
    arr = [3, 1, 4, 1, 5, 9, 2, 6]
    insertion_sort(arr)
    assert arr == [1, 1, 2, 3, 4, 5, 6, 9]

def test_merge_sort():
    arr = [3, 1, 4, 1, 5, 9, 2, 6]
    result = merge_sort(arr)
    assert result == [1, 1, 2, 3, 4, 5, 6, 9]
    assert arr == [3, 1, 4, 1, 5, 9, 2, 6]  # Original unchanged

def test_merge():
    assert merge([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge([1, 2], [3, 4]) == [1, 2, 3, 4]

