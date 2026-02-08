"""
Project: Introduction to Dynamic Programming

Dynamic Programming (DP) is a method for solving complex problems by breaking
them down into simpler subproblems. It is applicable where subproblems overlap.
This project introduces two core DP techniques: Memoization (Top-Down) and
Tabulation (Bottom-Up).
"""
from typing import Dict

# --- Problem 1: Memoization (Top-Down DP) ---

def fib_memoized(n: int, memo: Dict[int, int] = None) -> int:
    """
    Calculates the n-th Fibonacci number using memoization.

    The Fibonacci sequence is: 0, 1, 1, 2, 3, 5, 8, ... where F(n) = F(n-1) + F(n-2).
    A naive recursive solution is very slow due to re-calculating the same
    subproblems. Memoization stores the results of expensive function calls
    and returns the cached result when the same inputs occur again.

    Args:
        n: The index in the Fibonacci sequence.
        memo: A dictionary to store the results of previous calculations.
              This is used by the recursion and should typically be left as None
              by the initial caller.

    Returns:
        The n-th Fibonacci number.
    """
    # TODO: The `memo` dictionary is used to store computed results.
    # On the first call, it should be initialized.
    pass

    # TODO: Base case: If the result for `n` is already in our memo,
    # return it immediately.
    pass

    # TODO: Base cases for the Fibonacci sequence (F(0) and F(1)).
    pass

    # TODO: Recursive step: If the result is not in the memo,
    # calculate it by making recursive calls.
    pass

    # TODO: Store the result in the memo before returning it.
    pass

    # TODO: Return the calculated result.
    pass


# --- Problem 2: Tabulation (Bottom-Up DP) ---

def climb_stairs(n: int) -> int:
    """
    Calculates the number of distinct ways you can climb to the top of a
    staircase with `n` steps. You can either climb 1 or 2 steps at a time.

    This problem has optimal substructure and overlapping subproblems, making
    it ideal for a bottom-up DP approach.

    Example:
    n = 3. Ways: [1,1,1], [1,2], [2,1]. Total = 3.
    This is the same as (ways to climb 2 steps) + (ways to climb 1 step).

    Args:
        n: The total number of stairs.

    Returns:
        The number of distinct ways to climb the stairs.
    """
    # TODO: Handle base cases: If n is 0 or 1, there's only one way
    # (do nothing or take one step). If n is 2, there are two ways ([1,1], [2]).
    pass

    # TODO: Create a DP table (a list or array) of size n+1 to store the
    # number of ways to reach each step.
    pass

    # TODO: Initialize the base cases in the DP table.
    # dp[0] = 1 (1 way to be at the ground)
    # dp[1] = 1 (1 way to climb to the first step)
    # dp[2] = 2 
    pass

    # TODO: Fill the DP table from the bottom up.
    # The number of ways to reach step `i` is the sum of the ways to reach
    # step `i-1` and step `i-2`.
    pass

    # TODO: The final answer is the value at the top of the table.
    pass

# --- Example Usage ---
# if __name__ == "__main__":
#     print("---" + " Fibonacci with Memoization ---")
#     print(f"Fibonacci(10): {fib_memoized(10)}")  # Expected: 55
#     print(f"Fibonacci(35): {fib_memoized(35)}")  # Naive recursion would be slow

#     print("\n---" + " Climbing Stairs (Bottom-Up DP) ---")
#     print(f"Ways to climb 3 stairs: {climb_stairs(3)}") # Expected: 3
#     print(f"Ways to climb 5 stairs: {climb_stairs(5)}") # Expected: 8