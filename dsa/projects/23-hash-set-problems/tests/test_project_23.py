"""Tests for Project 23: Hash Set Problems"""

import pytest
from solution.solution import contains_duplicate, intersection, is_happy, is_isomorphic


class TestContainsDuplicate:
    def test_has_duplicate(self):
        assert contains_duplicate([1,2,3,1]) == True
    
    def test_no_duplicate(self):
        assert contains_duplicate([1,2,3,4]) == False


class TestIntersection:
    def test_basic(self):
        assert set(intersection([1,2,2,1], [2,2])) == {2}
        assert set(intersection([4,9,5], [9,4,9,8,4])) == {4,9}


class TestIsHappy:
    def test_happy(self):
        assert is_happy(19) == True
        assert is_happy(1) == True
    
    def test_not_happy(self):
        assert is_happy(2) == False


class TestIsIsomorphic:
    def test_isomorphic(self):
        assert is_isomorphic("egg", "add") == True
        assert is_isomorphic("paper", "title") == True
    
    def test_not_isomorphic(self):
        assert is_isomorphic("foo", "bar") == False
