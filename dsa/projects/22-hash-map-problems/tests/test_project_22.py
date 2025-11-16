"""Tests for Project 22: Hash Map Problems"""

import pytest
from solution.solution import two_sum, group_anagrams, longest_consecutive, subarray_sum


class TestTwoSum:
    def test_basic(self):
        assert two_sum([2,7,11,15], 9) == [0, 1]
        assert two_sum([3,2,4], 6) == [1, 2]
    
    def test_edge_cases(self):
        assert two_sum([3,3], 6) == [0, 1]
        assert two_sum([1,2], 10) == []


class TestGroupAnagrams:
    def test_basic(self):
        result = group_anagrams(["eat","tea","tan","ate","nat","bat"])
        assert len(result) == 3
        assert sorted([''.join(sorted(group[0])) for group in result]) == ['abt', 'ant', 'aet']
    
    def test_single(self):
        assert group_anagrams([""]) == [[""]]


class TestLongestConsecutive:
    def test_basic(self):
        assert longest_consecutive([100,4,200,1,3,2]) == 4
        assert longest_consecutive([0,3,7,2,5,8,4,6,0,1]) == 9
    
    def test_empty(self):
        assert longest_consecutive([]) == 0


class TestSubarraySum:
    def test_basic(self):
        assert subarray_sum([1,1,1], 2) == 2
        assert subarray_sum([1,2,3], 3) == 2
    
    def test_negative(self):
        assert subarray_sum([1,-1,0], 0) == 3
