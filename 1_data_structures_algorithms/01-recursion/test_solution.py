"""Test suite for Project 08: Recursion"""
import pytest
from exercise import factorial, fibonacci, gcd, binary_search, sum_list_recursive

def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(7) == 5040

def test_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(5) == 5
    assert fibonacci(10) == 55

def test_gcd():
    assert gcd(48, 18) == 6
    assert gcd(17, 13) == 1
    assert gcd(100, 25) == 25

def test_binary_search():
    arr = [1, 3, 5, 7, 9, 11, 13]
    assert binary_search(arr, 7) == 3
    assert binary_search(arr, 1) == 0
    assert binary_search(arr, 13) == 6
    assert binary_search(arr, 4) == -1

def test_sum_list_recursive():
    assert sum_list_recursive([1, 2, 3, 4, 5]) == 15
    assert sum_list_recursive([]) == 0
    assert sum_list_recursive([10]) == 10

