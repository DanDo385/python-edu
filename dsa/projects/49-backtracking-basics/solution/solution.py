"""
Project 49: Backtracking Basics

This module implements fundamental backtracking algorithms including subsets generation,
combinations, combination sum, permutations, and letter combinations of phone numbers.

Key Concepts:
- Backtracking template: choose → explore → unchoose
- Decision tree traversal
- Pruning for efficiency
- Avoiding duplicates with start index
- State management and backtracking

Author: Python-Edu DSA Curriculum
"""

from typing import List


# ============================================================================
# Problem 1: Subsets (Power Set)
# ============================================================================

def subsets(nums: List[int]) -> List[List[int]]:
    """
    Generate all possible subsets (the power set) of a set of distinct integers.

    Approach: For each element, we have two choices:
    1. Include it in the current subset
    2. Exclude it from the current subset

    Decision tree for [1,2,3]:
                        []
                      /    \
                 [1]          []
                /   \        /   \
            [1,2]   [1]   [2]     []
           /  \    / \   / \     / \
      [1,2,3][1,2][1,3][1][2,3][2][3][]

    Args:
        nums: List of distinct integers

    Returns:
        List of all possible subsets (power set)

    Time Complexity: O(n × 2^n) - 2^n subsets, each takes O(n) to construct
    Space Complexity: O(n) - recursion depth

    Examples:
        >>> sorted(subsets([1, 2, 3]))
        [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
        >>> sorted(subsets([0]))
        [[], [0]]
    """
    result = []

    def backtrack(start: int, current: List[int]) -> None:
        """
        Backtracking helper function.

        Args:
            start: Index to start considering elements from
            current: Current subset being built
        """
        # Every state is a valid subset - add it
        result.append(current[:])  # Make a copy

        # Try adding each remaining element
        for i in range(start, len(nums)):
            # Choose: add nums[i] to current subset
            current.append(nums[i])

            # Explore: continue building subset with remaining elements
            backtrack(i + 1, current)

            # Unchoose: remove nums[i] (backtrack)
            current.pop()

    backtrack(0, [])
    return result


def subsets_iterative(nums: List[int]) -> List[List[int]]:
    """
    Generate subsets iteratively (alternative approach).

    Start with empty set, then for each number, add it to all existing subsets.

    Algorithm:
        Start: [[]]
        Add 1: [[], [1]]
        Add 2: [[], [1], [2], [1,2]]
        Add 3: [[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]

    Args:
        nums: List of distinct integers

    Returns:
        List of all possible subsets

    Time Complexity: O(n × 2^n)
    Space Complexity: O(1) - excluding output

    Examples:
        >>> sorted(subsets_iterative([1, 2]))
        [[], [1], [1, 2], [2]]
    """
    result = [[]]  # Start with empty set

    for num in nums:
        # For each existing subset, create a new subset by adding current number
        new_subsets = [subset + [num] for subset in result]
        result.extend(new_subsets)

    return result


# ============================================================================
# Problem 2: Combinations
# ============================================================================

def combine(n: int, k: int) -> List[List[int]]:
    """
    Generate all combinations of k numbers from range [1, n].

    Key insight: Combinations are order-independent.
    - Use start index to avoid duplicates
    - [1,2] and [2,1] are the same combination

    Decision tree for C(4, 2):
                        []
           /      /      \      \
        [1]    [2]     [3]    [4]
       / | \   /  \     |
    [1,2][1,3][1,4][2,3][2,4][3,4]

    Args:
        n: Range upper bound (inclusive)
        k: Number of elements to choose

    Returns:
        List of all k-combinations from [1, n]

    Time Complexity: O(C(n,k) × k) where C(n,k) = n!/(k!(n-k)!)
    Space Complexity: O(k) - recursion depth

    Examples:
        >>> sorted(combine(4, 2))
        [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
        >>> combine(1, 1)
        [[1]]
    """
    result = []

    def backtrack(start: int, current: List[int]) -> None:
        """
        Backtracking helper function.

        Args:
            start: Next number to consider
            current: Current combination being built
        """
        # Base case: found a complete combination
        if len(current) == k:
            result.append(current[:])  # Make a copy
            return

        # Try each number from start to n
        for i in range(start, n + 1):
            # Pruning: if remaining numbers insufficient, stop
            # Need: k - len(current) more numbers
            # Have: n - i + 1 numbers available
            if n - i + 1 < k - len(current):
                break

            # Choose: add i to combination
            current.append(i)

            # Explore: continue with next numbers
            backtrack(i + 1, current)

            # Unchoose: remove i (backtrack)
            current.pop()

    backtrack(1, [])
    return result


# ============================================================================
# Problem 3: Combination Sum
# ============================================================================

def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    """
    Find all unique combinations where candidate numbers sum to target.

    Key differences from regular combinations:
    - Can reuse same number unlimited times
    - Must sum to target (not fixed length)
    - Need pruning when sum exceeds target

    Decision tree for [2,3,6,7], target=7:
                        []
              /    /    \    \
           [2]  [3]   [6]  [7] ← target!
          / | \  |     |
      [2,2][2,3]...[3,3][6,?]
        / |
    [2,2,2][2,2,3] ← target!
      /
   [2,2,2,2] ← exceeded

    Args:
        candidates: List of distinct positive integers
        target: Target sum

    Returns:
        List of all unique combinations that sum to target

    Time Complexity: O(N^(T/M)) where N=len(candidates), T=target, M=min(candidates)
    Space Complexity: O(T/M) - maximum recursion depth

    Examples:
        >>> sorted(combination_sum([2, 3, 6, 7], 7))
        [[2, 2, 3], [7]]
        >>> sorted(combination_sum([2, 3, 5], 8))
        [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    """
    result = []

    def backtrack(start: int, current: List[int], current_sum: int) -> None:
        """
        Backtracking helper with sum tracking.

        Args:
            start: Index to start considering candidates from
            current: Current combination being built
            current_sum: Sum of current combination
        """
        # Base case: found a valid combination
        if current_sum == target:
            result.append(current[:])  # Make a copy
            return

        # Pruning: exceeded target, no point continuing
        if current_sum > target:
            return

        # Try each candidate from start onward
        for i in range(start, len(candidates)):
            # Pruning optimization: if sorted and current candidate too large, stop
            # (This assumes candidates are sorted, which we could do in parent function)

            # Choose: add candidates[i] to combination
            current.append(candidates[i])

            # Explore: can reuse same number, so pass i (not i+1)
            backtrack(i, current, current_sum + candidates[i])

            # Unchoose: remove candidates[i] (backtrack)
            current.pop()

    backtrack(0, [], 0)
    return result


# ============================================================================
# Problem 4: Permutations
# ============================================================================

def permute(nums: List[int]) -> List[List[int]]:
    """
    Generate all permutations of distinct integers.

    This is a review problem from Project 48.
    Uses swap-based backtracking approach.

    Decision tree for [1,2,3]:
                        [1,2,3]
                      /    |    \
              [1,2,3]  [2,1,3]  [3,2,1]
               /  \     /  \     /  \
         [1,2,3][1,3,2][2,1,3][2,3,1][3,2,1][3,1,2]

    Args:
        nums: List of distinct integers

    Returns:
        List of all permutations

    Time Complexity: O(n! × n)
    Space Complexity: O(n) - recursion depth

    Examples:
        >>> sorted(permute([1, 2, 3]))
        [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        >>> sorted(permute([0, 1]))
        [[0, 1], [1, 0]]
    """
    result = []

    def backtrack(start: int) -> None:
        """
        Backtracking helper using in-place swapping.

        Args:
            start: Current position to fill
        """
        # Base case: filled all positions
        if start == len(nums):
            result.append(nums[:])  # Make a copy
            return

        # Try each element from start to end at position start
        for i in range(start, len(nums)):
            # Choose: swap element i to position start
            nums[start], nums[i] = nums[i], nums[start]

            # Explore: recursively permute remaining elements
            backtrack(start + 1)

            # Unchoose: swap back (backtrack)
            nums[start], nums[i] = nums[i], nums[start]

    backtrack(0)
    return result


# ============================================================================
# Problem 5: Letter Combinations of Phone Number
# ============================================================================

def letter_combinations(digits: str) -> List[str]:
    """
    Generate all letter combinations from phone number digits.

    Phone keyboard mapping:
        2: abc, 3: def, 4: ghi, 5: jkl,
        6: mno, 7: pqrs, 8: tuv, 9: wxyz

    Decision tree for "23":
                    ""
                /   |   \
              a     b     c
            / | \  / | \ / | \
          ad ae af bd be bf cd ce cf

    Args:
        digits: String of digits from '2' to '9'

    Returns:
        List of all possible letter combinations

    Time Complexity: O(4^n × n) where n = len(digits)
    Space Complexity: O(n) - recursion depth

    Examples:
        >>> sorted(letter_combinations("23"))
        ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
        >>> letter_combinations("")
        []
        >>> sorted(letter_combinations("2"))
        ['a', 'b', 'c']
    """
    if not digits:
        return []

    # Phone keyboard mapping
    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }

    result = []

    def backtrack(index: int, current: str) -> None:
        """
        Backtracking helper function.

        Args:
            index: Current position in digits string
            current: Current letter combination being built
        """
        # Base case: processed all digits
        if index == len(digits):
            result.append(current)
            return

        # Get letters for current digit
        letters = phone_map[digits[index]]

        # Try each letter
        for letter in letters:
            # Choose: add letter to current combination
            # Explore: continue with next digit
            backtrack(index + 1, current + letter)
            # Unchoose: automatic (string is immutable, no need to undo)

    backtrack(0, '')
    return result


# ============================================================================
# Additional Helper Functions
# ============================================================================

def print_decision_tree(problem: str, nums: List[int], k: int = None, target: int = None):
    """
    Print decision tree visualization for educational purposes.

    Args:
        problem: Problem type ('subsets', 'combinations', 'combination_sum')
        nums: Input array
        k: For combinations, number of elements to choose
        target: For combination_sum, target sum
    """
    print(f"\n{problem.upper()} Decision Tree for {nums}")
    print("=" * 50)

    if problem == 'subsets':
        result = subsets(nums)
        print(f"Total subsets: {len(result)}")
        print(f"Subsets: {sorted(result)}")

    elif problem == 'combinations' and k is not None:
        result = combine(max(nums), k)
        print(f"Total combinations: {len(result)}")
        print(f"Combinations: {sorted(result)}")

    elif problem == 'combination_sum' and target is not None:
        result = combination_sum(nums, target)
        print(f"Total combinations: {len(result)}")
        print(f"Combinations: {sorted(result)}")


# ============================================================================
# Demonstration
# ============================================================================

if __name__ == "__main__":
    print("Backtracking Basics")
    print("=" * 70)

    # Test 1: Subsets
    print("\n1. Subsets (Power Set):")
    test_arrays = [[1, 2, 3], [0], [1, 2]]
    for arr in test_arrays:
        result = subsets(arr)
        print(f"   {arr}: {len(result)} subsets")
        if len(arr) <= 2:
            print(f"   {sorted(result)}")

    # Test 2: Combinations
    print("\n2. Combinations:")
    test_cases = [(4, 2), (1, 1), (5, 3)]
    for n, k in test_cases:
        result = combine(n, k)
        print(f"   C({n},{k}): {len(result)} combinations")
        if n <= 4:
            print(f"   {sorted(result)}")

    # Test 3: Combination Sum
    print("\n3. Combination Sum:")
    test_cases = [
        ([2, 3, 6, 7], 7),
        ([2, 3, 5], 8),
        ([2], 1),
    ]
    for candidates, target in test_cases:
        result = combination_sum(candidates, target)
        print(f"   {candidates}, target={target}: {sorted(result)}")

    # Test 4: Permutations
    print("\n4. Permutations:")
    test_arrays = [[1], [1, 2], [1, 2, 3]]
    for arr in test_arrays:
        result = permute(arr)
        print(f"   {arr}: {len(result)} permutations")
        if len(arr) <= 2:
            print(f"   {sorted(result)}")

    # Test 5: Letter Combinations
    print("\n5. Letter Combinations of Phone Number:")
    test_digits = ["", "2", "23", "234"]
    for digits in test_digits:
        result = letter_combinations(digits)
        print(f"   '{digits}': {len(result)} combinations")
        if len(digits) <= 2 and digits:
            print(f"   {sorted(result)}")

    print("\n" + "=" * 70)
    print("All backtracking basics demonstrated!")
