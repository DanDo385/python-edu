"""
Project 48: Recursion Fundamentals

This module implements fundamental recursive algorithms including factorial, power,
GCD, Tower of Hanoi, parentheses generation, and permutations. Each problem demonstrates
core recursion principles and includes both recursive and iterative approaches where applicable.

Key Concepts:
- Base cases and recursive cases
- Call stack management
- Tail recursion
- Divide and conquer (fast exponentiation)
- Backtracking (permutations, parentheses)
- Euclidean algorithm (GCD)

Author: Python-Edu DSA Curriculum
"""

from typing import List, Tuple


# ============================================================================
# Problem 1: Factorial
# ============================================================================

def factorial_recursive(n: int) -> int:
    """
    Compute n! recursively.

    Factorial is defined as:
    - n! = n × (n-1) × (n-2) × ... × 2 × 1
    - 0! = 1 (by definition)

    Recursive relation:
    - factorial(n) = n × factorial(n-1)
    - Base case: factorial(0) = 1

    Args:
        n: Non-negative integer

    Returns:
        n! (factorial of n)

    Time Complexity: O(n) - n recursive calls
    Space Complexity: O(n) - call stack depth

    Examples:
        >>> factorial_recursive(5)
        120
        >>> factorial_recursive(0)
        1
        >>> factorial_recursive(10)
        3628800
    """
    # Base case: 0! = 1
    if n == 0:
        return 1

    # Recursive case: n! = n × (n-1)!
    return n * factorial_recursive(n - 1)


def factorial_iterative(n: int) -> int:
    """
    Compute n! iteratively.

    This is more efficient than the recursive version:
    - No call stack overhead
    - No risk of stack overflow
    - Better performance

    Args:
        n: Non-negative integer

    Returns:
        n! (factorial of n)

    Time Complexity: O(n) - n iterations
    Space Complexity: O(1) - constant extra space

    Examples:
        >>> factorial_iterative(5)
        120
        >>> factorial_iterative(0)
        1
    """
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# ============================================================================
# Problem 2: Power Function
# ============================================================================

def power_recursive(x: float, n: int) -> float:
    """
    Compute x^n recursively using naive approach.

    Recursive relation:
    - power(x, n) = x × power(x, n-1)
    - Base case: power(x, 0) = 1
    - Handle negative exponents: power(x, -n) = 1 / power(x, n)

    Args:
        x: Base number
        n: Exponent (can be negative)

    Returns:
        x raised to the power n

    Time Complexity: O(n) - n recursive calls
    Space Complexity: O(n) - call stack depth

    Examples:
        >>> power_recursive(2, 10)
        1024.0
        >>> power_recursive(2, -2)
        0.25
        >>> power_recursive(2, 0)
        1.0
    """
    # Handle negative exponent
    if n < 0:
        return 1.0 / power_recursive(x, -n)

    # Base case: x^0 = 1
    if n == 0:
        return 1.0

    # Recursive case: x^n = x × x^(n-1)
    return x * power_recursive(x, n - 1)


def power_iterative(x: float, n: int) -> float:
    """
    Compute x^n iteratively using naive approach.

    Args:
        x: Base number
        n: Exponent (can be negative)

    Returns:
        x raised to the power n

    Time Complexity: O(n) - n iterations
    Space Complexity: O(1) - constant extra space

    Examples:
        >>> power_iterative(2, 10)
        1024.0
        >>> power_iterative(2, -2)
        0.25
    """
    # Handle negative exponent
    if n < 0:
        x = 1.0 / x
        n = -n

    result = 1.0
    for _ in range(n):
        result *= x

    return result


def power_fast(x: float, n: int) -> float:
    """
    Compute x^n using fast exponentiation (exponentiation by squaring).

    This is a divide-and-conquer approach:
    - x^n = (x^(n/2))^2         if n is even
    - x^n = x × (x^((n-1)/2))^2 if n is odd

    Key insight: We can compute x^10 as:
    - x^10 = (x^5)^2
    - x^5 = x × (x^2)^2
    - x^2 = (x^1)^2

    This reduces multiplications from 10 to ~4 (log₂10).

    Args:
        x: Base number
        n: Exponent (can be negative)

    Returns:
        x raised to the power n

    Time Complexity: O(log n) - halving each recursive call
    Space Complexity: O(log n) - call stack depth

    Examples:
        >>> power_fast(2, 10)
        1024.0
        >>> power_fast(2, -2)
        0.25
        >>> abs(power_fast(2.0, -3) - 0.125) < 1e-9
        True
    """
    # Handle negative exponent
    if n < 0:
        return 1.0 / power_fast(x, -n)

    # Base case
    if n == 0:
        return 1.0

    # Recursive case: divide and conquer
    # Compute x^(n/2) once and square it
    half = power_fast(x, n // 2)

    if n % 2 == 0:
        # Even exponent: x^n = (x^(n/2))^2
        return half * half
    else:
        # Odd exponent: x^n = x × (x^(n/2))^2
        return x * half * half


# ============================================================================
# Problem 3: Greatest Common Divisor (GCD)
# ============================================================================

def gcd_recursive(a: int, b: int) -> int:
    """
    Compute GCD of a and b using Euclidean algorithm (recursive).

    The Euclidean algorithm is based on the principle:
    - gcd(a, b) = gcd(b, a mod b)
    - gcd(a, 0) = a

    Why this works:
    - Any divisor of both a and b also divides (a mod b)
    - Any divisor of both b and (a mod b) also divides a

    Example: gcd(48, 18)
    - gcd(48, 18) = gcd(18, 12)  [48 mod 18 = 12]
    - gcd(18, 12) = gcd(12, 6)   [18 mod 12 = 6]
    - gcd(12, 6) = gcd(6, 0)     [12 mod 6 = 0]
    - gcd(6, 0) = 6

    Args:
        a: First non-negative integer
        b: Second non-negative integer

    Returns:
        Greatest common divisor of a and b

    Time Complexity: O(log(min(a, b))) - proven by Lamé's theorem
    Space Complexity: O(log(min(a, b))) - call stack depth

    Examples:
        >>> gcd_recursive(48, 18)
        6
        >>> gcd_recursive(100, 50)
        50
        >>> gcd_recursive(7, 13)
        1
        >>> gcd_recursive(0, 5)
        5
    """
    # Base case: gcd(a, 0) = a
    if b == 0:
        return a

    # Recursive case: gcd(a, b) = gcd(b, a mod b)
    return gcd_recursive(b, a % b)


def gcd_iterative(a: int, b: int) -> int:
    """
    Compute GCD of a and b using Euclidean algorithm (iterative).

    Same algorithm as recursive version but using a loop.
    More efficient in practice due to no call stack overhead.

    Args:
        a: First non-negative integer
        b: Second non-negative integer

    Returns:
        Greatest common divisor of a and b

    Time Complexity: O(log(min(a, b)))
    Space Complexity: O(1) - constant extra space

    Examples:
        >>> gcd_iterative(48, 18)
        6
        >>> gcd_iterative(100, 50)
        50
    """
    while b != 0:
        # Replace (a, b) with (b, a mod b)
        a, b = b, a % b

    return a


# ============================================================================
# Problem 4: Tower of Hanoi
# ============================================================================

def tower_of_hanoi(n: int, source: str, destination: str, auxiliary: str) -> List[Tuple[str, str]]:
    """
    Solve the Tower of Hanoi puzzle.

    Problem: Move n disks from source to destination using auxiliary peg.
    Rules:
    1. Only one disk can be moved at a time
    2. A larger disk cannot be placed on a smaller disk
    3. Only the top disk of a stack can be moved

    Recursive strategy:
    1. Move n-1 disks from source to auxiliary (using destination as spare)
    2. Move the largest disk from source to destination
    3. Move n-1 disks from auxiliary to destination (using source as spare)

    Why this works:
    - After step 1, all small disks are on auxiliary
    - The largest disk can now move freely to destination
    - Then we move the small disks on top of it

    Args:
        n: Number of disks
        source: Source peg name
        destination: Destination peg name
        auxiliary: Auxiliary peg name

    Returns:
        List of moves as (from_peg, to_peg) tuples

    Time Complexity: O(2^n) - exactly 2^n - 1 moves
    Space Complexity: O(n) - call stack depth

    Examples:
        >>> tower_of_hanoi(1, 'A', 'C', 'B')
        [('A', 'C')]
        >>> tower_of_hanoi(2, 'A', 'C', 'B')
        [('A', 'B'), ('A', 'C'), ('B', 'C')]
        >>> len(tower_of_hanoi(3, 'A', 'C', 'B'))
        7
    """
    moves = []

    def hanoi_helper(n: int, source: str, destination: str, auxiliary: str) -> None:
        """Recursive helper function that appends moves to the moves list."""
        if n == 1:
            # Base case: move single disk directly
            moves.append((source, destination))
            return

        # Step 1: Move n-1 disks from source to auxiliary (using destination)
        hanoi_helper(n - 1, source, auxiliary, destination)

        # Step 2: Move the largest disk from source to destination
        moves.append((source, destination))

        # Step 3: Move n-1 disks from auxiliary to destination (using source)
        hanoi_helper(n - 1, auxiliary, destination, source)

    hanoi_helper(n, source, destination, auxiliary)
    return moves


# ============================================================================
# Problem 5: Generate Parentheses
# ============================================================================

def generate_parentheses(n: int) -> List[str]:
    """
    Generate all valid combinations of n pairs of parentheses.

    A valid combination has:
    1. Equal number of '(' and ')'
    2. At any point, number of ')' ≤ number of '('

    Backtracking approach:
    - Track count of open '(' and close ')' parentheses used
    - Add '(' if we haven't used all n open parentheses
    - Add ')' if close < open (ensures validity)
    - Base case: when we've used all 2n characters

    Decision tree for n=2:
                        ""
                       /
                      (
                    /   \
                  ((     ()
                 /        \
               (()        ()(
              /            \
            (())          ()()

    Args:
        n: Number of pairs of parentheses

    Returns:
        List of all valid parentheses combinations

    Time Complexity: O(4^n / √n) - Catalan number C_n
    Space Complexity: O(n) - call stack depth

    Examples:
        >>> sorted(generate_parentheses(1))
        ['()']
        >>> sorted(generate_parentheses(2))
        ['(())', '()()']
        >>> sorted(generate_parentheses(3))
        ['((()))', '(()())', '(())()', '()(())', '()()()']
    """
    result = []

    def backtrack(current: str, open_count: int, close_count: int) -> None:
        """
        Backtracking helper function.

        Args:
            current: Current string being built
            open_count: Number of '(' used so far
            close_count: Number of ')' used so far
        """
        # Base case: used all 2n characters
        if len(current) == 2 * n:
            result.append(current)
            return

        # Option 1: Add '(' if we haven't used all n
        if open_count < n:
            backtrack(current + '(', open_count + 1, close_count)

        # Option 2: Add ')' if it maintains validity (close < open)
        if close_count < open_count:
            backtrack(current + ')', open_count, close_count + 1)

    backtrack('', 0, 0)
    return result


# ============================================================================
# Problem 6: All Permutations
# ============================================================================

def permute(nums: List[int]) -> List[List[int]]:
    """
    Generate all permutations of a list of distinct integers.

    Backtracking approach using swapping:
    1. For each position i, try each element from i to end
    2. Swap element to position i
    3. Recursively permute remaining elements
    4. Backtrack: swap back to restore original order

    Decision tree for [1,2,3]:
                    [1,2,3]
                   /   |   \
          [1,2,3] [2,1,3] [3,2,1]
           /  \    /  \    /  \
      [1,2,3][1,3,2][2,1,3][2,3,1][3,2,1][3,1,2]

    Alternative approach: Use a "used" set to track which elements
    are already in the current permutation.

    Args:
        nums: List of distinct integers

    Returns:
        List of all permutations

    Time Complexity: O(n! × n) - n! permutations, each takes O(n) to construct
    Space Complexity: O(n) - call stack depth (excluding output)

    Examples:
        >>> sorted(permute([1, 2, 3]))
        [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        >>> sorted(permute([0, 1]))
        [[0, 1], [1, 0]]
        >>> permute([1])
        [[1]]
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

            # Unchoose (backtrack): swap back
            nums[start], nums[i] = nums[i], nums[start]

    backtrack(0)
    return result


def permute_with_used(nums: List[int]) -> List[List[int]]:
    """
    Generate all permutations using "used" set approach.

    Alternative implementation that's easier to understand but uses more space.

    Args:
        nums: List of distinct integers

    Returns:
        List of all permutations

    Time Complexity: O(n! × n)
    Space Complexity: O(n) - call stack + current permutation + used set

    Examples:
        >>> sorted(permute_with_used([1, 2]))
        [[1, 2], [2, 1]]
    """
    result = []

    def backtrack(current: List[int], used: set) -> None:
        """
        Backtracking helper using used set.

        Args:
            current: Current permutation being built
            used: Set of indices already used in current permutation
        """
        # Base case: permutation complete
        if len(current) == len(nums):
            result.append(current[:])  # Make a copy
            return

        # Try adding each unused element
        for i in range(len(nums)):
            if i not in used:
                # Choose: add nums[i] to current permutation
                current.append(nums[i])
                used.add(i)

                # Explore: continue building permutation
                backtrack(current, used)

                # Unchoose (backtrack): remove nums[i]
                current.pop()
                used.remove(i)

    backtrack([], set())
    return result


# ============================================================================
# Demonstration
# ============================================================================

if __name__ == "__main__":
    print("Recursion Fundamentals")
    print("=" * 70)

    # Test 1: Factorial
    print("\n1. Factorial:")
    for n in [0, 5, 10]:
        rec = factorial_recursive(n)
        iter = factorial_iterative(n)
        print(f"   {n}! = {rec} (recursive), {iter} (iterative)")

    # Test 2: Power
    print("\n2. Power Function:")
    test_cases = [(2, 10), (2, -2), (3, 5)]
    for x, n in test_cases:
        rec = power_recursive(x, n)
        iter = power_iterative(x, n)
        fast = power_fast(x, n)
        print(f"   {x}^{n} = {rec:.4f} (rec), {iter:.4f} (iter), {fast:.4f} (fast)")

    # Test 3: GCD
    print("\n3. Greatest Common Divisor:")
    test_cases = [(48, 18), (100, 50), (7, 13)]
    for a, b in test_cases:
        rec = gcd_recursive(a, b)
        iter = gcd_iterative(a, b)
        print(f"   gcd({a}, {b}) = {rec} (recursive), {iter} (iterative)")

    # Test 4: Tower of Hanoi
    print("\n4. Tower of Hanoi:")
    for n in [1, 2, 3]:
        moves = tower_of_hanoi(n, 'A', 'C', 'B')
        print(f"   {n} disk(s): {len(moves)} moves")
        if n <= 2:
            print(f"   Moves: {moves}")

    # Test 5: Generate Parentheses
    print("\n5. Generate Parentheses:")
    for n in [1, 2, 3]:
        parens = generate_parentheses(n)
        print(f"   n={n}: {sorted(parens)}")

    # Test 6: Permutations
    print("\n6. Permutations:")
    test_cases = [[1], [1, 2], [1, 2, 3]]
    for nums in test_cases:
        perms = permute(nums)
        print(f"   {nums}: {len(perms)} permutations")
        if len(nums) <= 2:
            print(f"   {sorted(perms)}")

    print("\n" + "=" * 70)
    print("All recursion fundamentals demonstrated!")
