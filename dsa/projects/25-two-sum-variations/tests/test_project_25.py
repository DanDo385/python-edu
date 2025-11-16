"""Tests for Project 25: Two Sum Variations"""

import pytest
from solution.solution import two_sum, three_sum, four_sum, two_sum_sorted, three_sum_closest


class TestTwoSum:
    def test_basic(self):
        assert two_sum([2,7,11,15], 9) == [0, 1]


class TestThreeSum:
    def test_basic(self):
        result = three_sum([-1,0,1,2,-1,-4])
        assert len(result) == 2
        assert [-1,-1,2] in result or [-1,0,1] in result
    
    def test_empty(self):
        assert three_sum([]) == []


class TestFourSum:
    def test_basic(self):
        result = four_sum([1,0,-1,0,-2,2], 0)
        assert len(result) >= 1


class TestTwoSumSorted:
    def test_basic(self):
        assert two_sum_sorted([2,7,11,15], 9) == [1, 2]


class TestThreeSumClosest:
    def test_basic(self):
        assert three_sum_closest([-1,2,1,-4], 1) == 2
