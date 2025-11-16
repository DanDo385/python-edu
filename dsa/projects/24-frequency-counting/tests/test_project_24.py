"""Tests for Project 24: Frequency Counting"""

import pytest
from solution.solution import top_k_frequent, frequency_sort, find_duplicates, first_uniq_char


class TestTopKFrequent:
    def test_basic(self):
        result = top_k_frequent([1,1,1,2,2,3], 2)
        assert set(result) == {1, 2}
    
    def test_single(self):
        assert top_k_frequent([1], 1) == [1]


class TestFrequencySort:
    def test_basic(self):
        result = frequency_sort("tree")
        assert result in ["eert", "eetr"]
    
    def test_numbers(self):
        result = frequency_sort("cccaaa")
        assert result in ["cccaaa", "aaaccc"]


class TestFindDuplicates:
    def test_basic(self):
        result = find_duplicates([4,3,2,7,8,2,3,1])
        assert set(result) == {2, 3}


class TestFirstUniqChar:
    def test_basic(self):
        assert first_uniq_char("leetcode") == 0
        assert first_uniq_char("loveleetcode") == 2
    
    def test_no_unique(self):
        assert first_uniq_char("aabb") == -1
