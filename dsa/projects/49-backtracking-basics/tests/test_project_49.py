"""
Tests for Project 49: Backtracking Basics

Comprehensive test suite for:
- Subsets (power set)
- Combinations
- Combination sum
- Permutations
- Letter combinations of phone number
"""

import pytest
from solution.solution import (
    subsets,
    subsets_iterative,
    combine,
    combination_sum,
    permute,
    letter_combinations,
)


class TestSubsets:
    """Tests for subsets (power set) generation."""

    def test_subsets_basic(self):
        """Test basic subset generation."""
        result = subsets([1, 2, 3])
        assert len(result) == 8  # 2^3
        assert [] in result
        assert [1, 2, 3] in result

    def test_subsets_single_element(self):
        """Test with single element."""
        result = subsets([0])
        assert sorted([sorted(s) for s in result]) == [[], [0]]

    def test_subsets_two_elements(self):
        """Test with two elements."""
        result = subsets([1, 2])
        assert len(result) == 4  # 2^2
        expected = [[], [1], [2], [1, 2]]
        assert sorted([sorted(s) for s in result]) == sorted([sorted(e) for e in expected])

    def test_subsets_count(self):
        """Verify subset count is 2^n."""
        for n in range(1, 6):
            nums = list(range(n))
            result = subsets(nums)
            assert len(result) == 2 ** n

    def test_subsets_iterative_consistency(self):
        """Verify recursive and iterative give same results."""
        for n in range(1, 5):
            nums = list(range(n))
            result1 = sorted([sorted(s) for s in subsets(nums)])
            result2 = sorted([sorted(s) for s in subsets_iterative(nums)])
            assert result1 == result2

    def test_subsets_no_duplicates(self):
        """Verify no duplicate subsets."""
        result = subsets([1, 2, 3])
        result_tuples = [tuple(sorted(s)) for s in result]
        assert len(result_tuples) == len(set(result_tuples))


class TestCombinations:
    """Tests for combinations generation."""

    def test_combine_basic(self):
        """Test basic combinations."""
        result = combine(4, 2)
        expected = [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
        assert sorted(result) == sorted(expected)

    def test_combine_single(self):
        """Test C(1,1)."""
        result = combine(1, 1)
        assert result == [[1]]

    def test_combine_all_elements(self):
        """Test C(n,n)."""
        result = combine(3, 3)
        assert result == [[1, 2, 3]]

    def test_combine_count(self):
        """Verify combination count matches C(n,k) formula."""
        import math
        test_cases = [(4,2), (5,3), (6,2), (6,4)]
        for n, k in test_cases:
            result = combine(n, k)
            expected_count = math.comb(n, k) if hasattr(math, 'comb') else \
                            math.factorial(n) // (math.factorial(k) * math.factorial(n-k))
            assert len(result) == expected_count

    def test_combine_order_independent(self):
        """Verify combinations are order-independent (no [2,1] if [1,2] exists)."""
        result = combine(4, 2)
        for combo in result:
            assert combo == sorted(combo)  # Should be in ascending order

    def test_combine_no_duplicates(self):
        """Verify no duplicate combinations."""
        result = combine(5, 3)
        result_tuples = [tuple(c) for c in result]
        assert len(result_tuples) == len(set(result_tuples))


class TestCombinationSum:
    """Tests for combination sum."""

    def test_combination_sum_basic(self):
        """Test basic combination sum."""
        result = combination_sum([2, 3, 6, 7], 7)
        expected = [[2, 2, 3], [7]]
        assert sorted([sorted(c) for c in result]) == sorted([sorted(e) for e in expected])

    def test_combination_sum_multiple_uses(self):
        """Test that same number can be used multiple times."""
        result = combination_sum([2, 3, 5], 8)
        expected = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
        assert sorted([sorted(c) for c in result]) == sorted([sorted(e) for e in expected])

    def test_combination_sum_no_solution(self):
        """Test when no combination sums to target."""
        result = combination_sum([2], 1)
        assert result == []

    def test_combination_sum_single_element(self):
        """Test with single candidate that equals target."""
        result = combination_sum([7], 7)
        assert result == [[7]]

    def test_combination_sum_all_valid(self):
        """Verify all returned combinations sum to target."""
        candidates = [2, 3, 5]
        target = 8
        result = combination_sum(candidates, target)
        for combo in result:
            assert sum(combo) == target

    def test_combination_sum_no_duplicates(self):
        """Verify no duplicate combinations."""
        result = combination_sum([2, 3, 6, 7], 7)
        result_tuples = [tuple(sorted(c)) for c in result]
        assert len(result_tuples) == len(set(result_tuples))


class TestPermutations:
    """Tests for permutations generation."""

    def test_permute_basic(self):
        """Test basic permutations."""
        result = permute([1, 2, 3])
        expected = [
            [1, 2, 3], [1, 3, 2],
            [2, 1, 3], [2, 3, 1],
            [3, 1, 2], [3, 2, 1]
        ]
        assert sorted(result) == sorted(expected)

    def test_permute_single(self):
        """Test with single element."""
        result = permute([1])
        assert result == [[1]]

    def test_permute_two_elements(self):
        """Test with two elements."""
        result = permute([1, 2])
        expected = [[1, 2], [2, 1]]
        assert sorted(result) == sorted(expected)

    def test_permute_count(self):
        """Verify permutation count is n!."""
        import math
        for n in range(1, 6):
            nums = list(range(n))
            result = permute(nums)
            assert len(result) == math.factorial(n)

    def test_permute_all_elements_present(self):
        """Verify each permutation contains all elements."""
        nums = [1, 2, 3, 4]
        result = permute(nums)
        for perm in result:
            assert sorted(perm) == sorted(nums)

    def test_permute_no_duplicates(self):
        """Verify no duplicate permutations."""
        result = permute([1, 2, 3])
        result_tuples = [tuple(p) for p in result]
        assert len(result_tuples) == len(set(result_tuples))


class TestLetterCombinations:
    """Tests for letter combinations of phone number."""

    def test_letter_combinations_basic(self):
        """Test basic letter combinations."""
        result = letter_combinations("23")
        expected = ["ad","ae","af","bd","be","bf","cd","ce","cf"]
        assert sorted(result) == sorted(expected)

    def test_letter_combinations_empty(self):
        """Test with empty string."""
        result = letter_combinations("")
        assert result == []

    def test_letter_combinations_single_digit(self):
        """Test with single digit."""
        result = letter_combinations("2")
        assert sorted(result) == ['a', 'b', 'c']

    def test_letter_combinations_count(self):
        """Verify combination count."""
        # Digit 2-6,8,9 have 3 letters, 7 has 4
        assert len(letter_combinations("2")) == 3
        assert len(letter_combinations("23")) == 9  # 3 * 3
        assert len(letter_combinations("234")) == 27  # 3 * 3 * 3

    def test_letter_combinations_with_7_and_9(self):
        """Test digits 7 and 9 which have 4 letters."""
        result = letter_combinations("7")
        assert sorted(result) == ['p', 'q', 'r', 's']

        result = letter_combinations("9")
        assert sorted(result) == ['w', 'x', 'y', 'z']

    def test_letter_combinations_all_correct_length(self):
        """Verify all combinations have correct length."""
        digits = "234"
        result = letter_combinations(digits)
        for combo in result:
            assert len(combo) == len(digits)

    def test_letter_combinations_no_duplicates(self):
        """Verify no duplicate combinations."""
        result = letter_combinations("23")
        assert len(result) == len(set(result))


class TestBacktrackingProperties:
    """Tests for general backtracking properties."""

    def test_all_functions_terminate(self):
        """Verify all backtracking functions terminate."""
        subsets([1, 2, 3])
        combine(5, 3)
        combination_sum([2, 3, 5], 8)
        permute([1, 2, 3])
        letter_combinations("234")

    def test_empty_or_minimal_inputs(self):
        """Test with edge case inputs."""
        assert subsets([1]) == [[], [1]]
        assert combine(1, 1) == [[1]]
        assert combination_sum([2], 1) == []
        assert permute([1]) == [[1]]
        assert letter_combinations("") == []

    def test_result_immutability(self):
        """Verify results don't share references."""
        result = subsets([1, 2])
        # Modify one subset
        if result:
            result[0].append(999)
        # Verify others aren't affected
        fresh_result = subsets([1, 2])
        assert 999 not in str(fresh_result)


if __name__ == "__main__":
    pytest.main([__file__, '-v'])
