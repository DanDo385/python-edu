"""
Tests for Project 48: Recursion Fundamentals

Comprehensive test suite covering:
- Factorial (recursive and iterative)
- Power functions (recursive, iterative, fast)
- GCD (recursive and iterative)
- Tower of Hanoi
- Generate parentheses
- Permutations
- Edge cases and complexity verification
"""

import pytest
from solution.solution import (
    factorial_recursive,
    factorial_iterative,
    power_recursive,
    power_iterative,
    power_fast,
    gcd_recursive,
    gcd_iterative,
    tower_of_hanoi,
    generate_parentheses,
    permute,
    permute_with_used,
)


class TestFactorial:
    """Tests for factorial functions (recursive and iterative)."""

    def test_factorial_base_case(self):
        """Test 0! = 1 (base case)."""
        assert factorial_recursive(0) == 1
        assert factorial_iterative(0) == 1

    def test_factorial_one(self):
        """Test 1! = 1."""
        assert factorial_recursive(1) == 1
        assert factorial_iterative(1) == 1

    def test_factorial_small(self):
        """Test factorial of small numbers."""
        assert factorial_recursive(5) == 120
        assert factorial_iterative(5) == 120

        assert factorial_recursive(3) == 6
        assert factorial_iterative(3) == 6

    def test_factorial_medium(self):
        """Test factorial of medium numbers."""
        assert factorial_recursive(10) == 3628800
        assert factorial_iterative(10) == 3628800

    def test_factorial_consistency(self):
        """Verify recursive and iterative give same results."""
        for n in range(21):
            assert factorial_recursive(n) == factorial_iterative(n)

    def test_factorial_known_values(self):
        """Test against known factorial values."""
        known = {
            0: 1,
            1: 1,
            2: 2,
            3: 6,
            4: 24,
            5: 120,
            6: 720,
            7: 5040,
            8: 40320,
            9: 362880,
            10: 3628800,
        }
        for n, expected in known.items():
            assert factorial_recursive(n) == expected
            assert factorial_iterative(n) == expected


class TestPower:
    """Tests for power functions (recursive, iterative, fast)."""

    def test_power_base_case(self):
        """Test x^0 = 1 for all x."""
        for x in [2, 3, 5, 10]:
            assert power_recursive(x, 0) == 1.0
            assert power_iterative(x, 0) == 1.0
            assert power_fast(x, 0) == 1.0

    def test_power_exponent_one(self):
        """Test x^1 = x."""
        for x in [2, 3, 5, 10]:
            assert power_recursive(x, 1) == float(x)
            assert power_iterative(x, 1) == float(x)
            assert power_fast(x, 1) == float(x)

    def test_power_positive_exponent(self):
        """Test positive integer exponents."""
        assert power_recursive(2, 10) == 1024.0
        assert power_iterative(2, 10) == 1024.0
        assert power_fast(2, 10) == 1024.0

        assert power_recursive(3, 5) == 243.0
        assert power_iterative(3, 5) == 243.0
        assert power_fast(3, 5) == 243.0

    def test_power_negative_exponent(self):
        """Test negative exponents."""
        assert abs(power_recursive(2, -2) - 0.25) < 1e-9
        assert abs(power_iterative(2, -2) - 0.25) < 1e-9
        assert abs(power_fast(2, -2) - 0.25) < 1e-9

        assert abs(power_recursive(2, -3) - 0.125) < 1e-9
        assert abs(power_iterative(2, -3) - 0.125) < 1e-9
        assert abs(power_fast(2, -3) - 0.125) < 1e-9

    def test_power_fractional_base(self):
        """Test fractional base."""
        assert abs(power_recursive(0.5, 2) - 0.25) < 1e-9
        assert abs(power_iterative(0.5, 2) - 0.25) < 1e-9
        assert abs(power_fast(0.5, 2) - 0.25) < 1e-9

    def test_power_consistency(self):
        """Verify all three implementations give same results."""
        test_cases = [
            (2, 0), (2, 1), (2, 10), (2, -2),
            (3, 5), (5, 3), (10, 2),
        ]
        for x, n in test_cases:
            rec = power_recursive(x, n)
            iter = power_iterative(x, n)
            fast = power_fast(x, n)
            assert abs(rec - iter) < 1e-9
            assert abs(rec - fast) < 1e-9

    def test_power_large_exponent(self):
        """Test fast exponentiation with large exponent."""
        # Fast should handle this efficiently
        result = power_fast(2, 100)
        assert result == 2 ** 100

    def test_power_known_values(self):
        """Test against known power values."""
        known = [
            (2, 0, 1),
            (2, 1, 2),
            (2, 5, 32),
            (2, 10, 1024),
            (3, 3, 27),
            (5, 2, 25),
        ]
        for x, n, expected in known:
            assert power_recursive(x, n) == float(expected)
            assert power_iterative(x, n) == float(expected)
            assert power_fast(x, n) == float(expected)


class TestGCD:
    """Tests for GCD (Euclidean algorithm)."""

    def test_gcd_basic(self):
        """Test basic GCD cases."""
        assert gcd_recursive(48, 18) == 6
        assert gcd_iterative(48, 18) == 6

        assert gcd_recursive(100, 50) == 50
        assert gcd_iterative(100, 50) == 50

    def test_gcd_coprime(self):
        """Test coprime numbers (GCD = 1)."""
        assert gcd_recursive(7, 13) == 1
        assert gcd_iterative(7, 13) == 1

        assert gcd_recursive(17, 19) == 1
        assert gcd_iterative(17, 19) == 1

    def test_gcd_with_zero(self):
        """Test GCD when one number is zero."""
        assert gcd_recursive(0, 5) == 5
        assert gcd_iterative(0, 5) == 5

        assert gcd_recursive(5, 0) == 5
        assert gcd_iterative(5, 0) == 5

    def test_gcd_same_numbers(self):
        """Test GCD of identical numbers."""
        assert gcd_recursive(42, 42) == 42
        assert gcd_iterative(42, 42) == 42

    def test_gcd_one_divides_other(self):
        """Test when one number divides the other."""
        assert gcd_recursive(100, 10) == 10
        assert gcd_iterative(100, 10) == 10

        assert gcd_recursive(10, 100) == 10
        assert gcd_iterative(10, 100) == 10

    def test_gcd_consistency(self):
        """Verify recursive and iterative give same results."""
        test_cases = [
            (48, 18), (100, 50), (7, 13), (0, 5), (5, 0),
            (12, 8), (24, 36), (1071, 462), (270, 192),
        ]
        for a, b in test_cases:
            assert gcd_recursive(a, b) == gcd_iterative(a, b)

    def test_gcd_large_numbers(self):
        """Test GCD with large numbers."""
        assert gcd_recursive(123456789, 987654321) == gcd_iterative(123456789, 987654321)
        # GCD(123456789, 987654321) = 9

    def test_gcd_commutative(self):
        """Test that gcd(a, b) = gcd(b, a)."""
        test_cases = [(48, 18), (100, 50), (7, 13)]
        for a, b in test_cases:
            assert gcd_recursive(a, b) == gcd_recursive(b, a)
            assert gcd_iterative(a, b) == gcd_iterative(b, a)


class TestTowerOfHanoi:
    """Tests for Tower of Hanoi."""

    def test_hanoi_single_disk(self):
        """Test with single disk."""
        moves = tower_of_hanoi(1, 'A', 'C', 'B')
        assert moves == [('A', 'C')]
        assert len(moves) == 1

    def test_hanoi_two_disks(self):
        """Test with two disks."""
        moves = tower_of_hanoi(2, 'A', 'C', 'B')
        assert len(moves) == 3
        expected = [('A', 'B'), ('A', 'C'), ('B', 'C')]
        assert moves == expected

    def test_hanoi_three_disks(self):
        """Test with three disks."""
        moves = tower_of_hanoi(3, 'A', 'C', 'B')
        assert len(moves) == 7
        expected = [
            ('A', 'C'), ('A', 'B'), ('C', 'B'),
            ('A', 'C'),
            ('B', 'A'), ('B', 'C'), ('A', 'C')
        ]
        assert moves == expected

    def test_hanoi_move_count(self):
        """Verify move count is 2^n - 1."""
        for n in range(1, 10):
            moves = tower_of_hanoi(n, 'A', 'C', 'B')
            assert len(moves) == 2 ** n - 1

    def test_hanoi_validity(self):
        """Verify moves are valid (simulate the puzzle)."""
        def simulate_hanoi(n, moves):
            """Simulate Tower of Hanoi and check if solution is valid."""
            pegs = {'A': list(range(n, 0, -1)), 'B': [], 'C': []}

            for from_peg, to_peg in moves:
                # Check that from_peg has disks
                if not pegs[from_peg]:
                    return False

                # Move top disk
                disk = pegs[from_peg].pop()

                # Check that we're not placing larger on smaller
                if pegs[to_peg] and pegs[to_peg][-1] < disk:
                    return False

                pegs[to_peg].append(disk)

            # Check final state: all disks on C
            return pegs['A'] == [] and pegs['B'] == [] and pegs['C'] == list(range(n, 0, -1))

        for n in range(1, 7):
            moves = tower_of_hanoi(n, 'A', 'C', 'B')
            assert simulate_hanoi(n, moves), f"Invalid solution for n={n}"

    def test_hanoi_different_pegs(self):
        """Test with different peg names."""
        moves = tower_of_hanoi(2, 'X', 'Z', 'Y')
        assert len(moves) == 3
        assert all(move[0] in ['X', 'Y', 'Z'] and move[1] in ['X', 'Y', 'Z'] for move in moves)


class TestGenerateParentheses:
    """Tests for generate parentheses."""

    def test_parentheses_n1(self):
        """Test n=1: only () is valid."""
        result = generate_parentheses(1)
        assert sorted(result) == ['()']

    def test_parentheses_n2(self):
        """Test n=2."""
        result = generate_parentheses(2)
        expected = ['(())', '()()']
        assert sorted(result) == sorted(expected)

    def test_parentheses_n3(self):
        """Test n=3."""
        result = generate_parentheses(3)
        expected = ['((()))', '(()())', '(())()', '()(())', '()()()']
        assert sorted(result) == sorted(expected)

    def test_parentheses_count(self):
        """Verify count matches Catalan numbers."""
        # Catalan numbers: C_n = (2n)! / ((n+1)! * n!)
        catalan = [1, 1, 2, 5, 14, 42, 132]
        for n in range(1, 7):
            result = generate_parentheses(n)
            assert len(result) == catalan[n], f"Expected {catalan[n]} combinations for n={n}"

    def test_parentheses_validity(self):
        """Verify all generated combinations are valid."""
        def is_valid(s):
            """Check if parentheses string is valid."""
            count = 0
            for char in s:
                if char == '(':
                    count += 1
                else:
                    count -= 1
                if count < 0:
                    return False
            return count == 0

        for n in range(1, 6):
            result = generate_parentheses(n)
            for combo in result:
                assert is_valid(combo), f"Invalid combination: {combo}"
                assert len(combo) == 2 * n, f"Wrong length: {combo}"

    def test_parentheses_no_duplicates(self):
        """Verify no duplicate combinations."""
        for n in range(1, 6):
            result = generate_parentheses(n)
            assert len(result) == len(set(result)), f"Duplicates found for n={n}"

    def test_parentheses_complete(self):
        """Verify all possible valid combinations are generated."""
        # For n=3, manually verify all 5 combinations are present
        result = set(generate_parentheses(3))
        expected = {'((()))', '(()())', '(())()', '()(())', '()()()'}
        assert result == expected


class TestPermutations:
    """Tests for permutation generation."""

    def test_permute_single_element(self):
        """Test permutations of single element."""
        result = permute([1])
        assert result == [[1]]

    def test_permute_two_elements(self):
        """Test permutations of two elements."""
        result = permute([1, 2])
        expected = [[1, 2], [2, 1]]
        assert sorted(result) == sorted(expected)

    def test_permute_three_elements(self):
        """Test permutations of three elements."""
        result = permute([1, 2, 3])
        expected = [
            [1, 2, 3], [1, 3, 2],
            [2, 1, 3], [2, 3, 1],
            [3, 1, 2], [3, 2, 1]
        ]
        assert sorted(result) == sorted(expected)

    def test_permute_count(self):
        """Verify permutation count is n!."""
        factorial_values = [1, 1, 2, 6, 24, 120]
        for n in range(1, 6):
            nums = list(range(n))
            result = permute(nums)
            assert len(result) == factorial_values[n]

    def test_permute_no_duplicates(self):
        """Verify no duplicate permutations."""
        for n in range(1, 5):
            nums = list(range(n))
            result = permute(nums)
            # Convert to tuples for set comparison
            result_set = set(tuple(perm) for perm in result)
            assert len(result) == len(result_set), f"Duplicates found for n={n}"

    def test_permute_all_elements_present(self):
        """Verify each permutation contains all original elements."""
        nums = [1, 2, 3, 4]
        result = permute(nums)
        for perm in result:
            assert sorted(perm) == sorted(nums)

    def test_permute_with_used_consistency(self):
        """Verify swap and used-set approaches give same results."""
        for n in range(1, 5):
            nums = list(range(n))
            result1 = sorted(permute(nums))
            result2 = sorted(permute_with_used(nums))
            assert result1 == result2

    def test_permute_different_values(self):
        """Test with different integer values."""
        result = permute([0, 1])
        expected = [[0, 1], [1, 0]]
        assert sorted(result) == sorted(expected)

        result = permute([5, 7, 3])
        assert len(result) == 6
        for perm in result:
            assert sorted(perm) == [3, 5, 7]

    def test_permute_negative_numbers(self):
        """Test with negative numbers."""
        result = permute([-1, 0, 1])
        assert len(result) == 6
        for perm in result:
            assert sorted(perm) == [-1, 0, 1]


class TestComplexityAndEdgeCases:
    """Tests for edge cases and complexity verification."""

    def test_factorial_edge_cases(self):
        """Test factorial edge cases."""
        # 0! = 1
        assert factorial_recursive(0) == 1
        assert factorial_iterative(0) == 1

        # 1! = 1
        assert factorial_recursive(1) == 1
        assert factorial_iterative(1) == 1

        # 20! is within bounds
        assert factorial_recursive(20) == factorial_iterative(20)

    def test_power_edge_cases(self):
        """Test power function edge cases."""
        # 0^0 is typically 1 in programming
        # (mathematically undefined)

        # x^0 = 1
        assert power_fast(0, 0) == 1.0

        # 1^n = 1
        for n in [0, 1, 5, 10]:
            assert power_fast(1, n) == 1.0

    def test_gcd_edge_cases(self):
        """Test GCD edge cases."""
        # gcd(0, 0) is undefined, but typically returns 0
        # gcd(a, 0) = a
        assert gcd_recursive(5, 0) == 5
        assert gcd_iterative(5, 0) == 5

        # gcd(a, 1) = 1
        assert gcd_recursive(100, 1) == 1
        assert gcd_iterative(100, 1) == 1

    def test_hanoi_efficiency(self):
        """Verify Hanoi generates minimal moves."""
        for n in range(1, 10):
            moves = tower_of_hanoi(n, 'A', 'C', 'B')
            # Optimal solution has exactly 2^n - 1 moves
            assert len(moves) == 2 ** n - 1

    def test_parentheses_efficiency(self):
        """Verify parentheses generation doesn't produce duplicates."""
        for n in range(1, 7):
            result = generate_parentheses(n)
            # Check uniqueness
            assert len(result) == len(set(result))

    def test_permutations_efficiency(self):
        """Verify permutations are generated without duplicates."""
        for n in range(1, 6):
            nums = list(range(n))
            result = permute(nums)
            # Check uniqueness
            result_tuples = [tuple(perm) for perm in result]
            assert len(result_tuples) == len(set(result_tuples))


class TestRecursionProperties:
    """Tests for general recursion properties."""

    def test_recursion_termination(self):
        """Verify recursive functions terminate."""
        # These should all complete without infinite recursion
        factorial_recursive(10)
        power_recursive(2, 10)
        gcd_recursive(48, 18)
        tower_of_hanoi(5, 'A', 'C', 'B')
        generate_parentheses(4)
        permute([1, 2, 3, 4])

    def test_base_cases(self):
        """Verify base cases work correctly."""
        # Factorial base case
        assert factorial_recursive(0) == 1

        # Power base case
        assert power_recursive(5, 0) == 1.0

        # GCD base case
        assert gcd_recursive(42, 0) == 42

        # Tower of Hanoi base case
        assert len(tower_of_hanoi(1, 'A', 'C', 'B')) == 1

        # Parentheses base case
        assert generate_parentheses(1) == ['()']

        # Permutations base case
        assert permute([1]) == [[1]]


if __name__ == "__main__":
    pytest.main([__file__, '-v'])
