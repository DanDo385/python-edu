"""Test suite for Project 09: Searching"""
import pytest
from exercise import linear_search, binary_search_iterative, find_first_occurrence, search_in_range

def test_linear_search():
    assert linear_search([1, 2, 3, 4, 5], 3) == 2
    assert linear_search([1, 2, 3, 4, 5], 6) == -1
    assert linear_search([], 1) == -1

def test_binary_search_iterative():
    arr = [1, 3, 5, 7, 9, 11]
    assert binary_search_iterative(arr, 7) == 3
    assert binary_search_iterative(arr, 1) == 0
    assert binary_search_iterative(arr, 12) == -1

def test_find_first_occurrence():
    arr = [1, 2, 2, 2, 3, 4]
    assert find_first_occurrence(arr, 2) == 1
    assert find_first_occurrence(arr, 3) == 4

def test_search_in_range():
    arr = [1, 2, 3, 4, 5, 6, 7]
    assert search_in_range(arr, 3, 0, 4) == 2
    assert search_in_range(arr, 6, 0, 4) == -1

