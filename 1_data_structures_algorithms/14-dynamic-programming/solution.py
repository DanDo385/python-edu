"""
Project: Introduction to Dynamic Programming - SOLUTION

This file provides solutions for classic DP problems using both
Memoization (Top-Down) and Tabulation (Bottom-Up) approaches.
"""
from typing import Dict

# --- Problem 1: Memoization (Top-Down DP) ---

def fib_memoized(n: int, memo: Dict[int, int] = None) -> int:
    """
    Calculates the n-th Fibonacci number using memoization.
    This is a "Top-Down" DP approach. We start from the top (the `n` we
    want) and break it down, caching results along the way.
    """
    # Initialize the memoization dictionary on the first call.
    if memo is None:
        memo = {}

    # Base case 1: If the result is already in our cache, return it.
    if n in memo:
        return memo[n]
    
    # Base cases for the Fibonacci sequence itself.
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Recursive step: Calculate the Fibonacci number by calling the function
    # for the two preceding numbers.
    result = fib_memoized(n - 1, memo) + fib_memoized(n - 2, memo)

    # Store the newly computed result in our cache before returning.
    memo[n] = result
    
    return result

# --- Problem 2: Tabulation (Bottom-Up DP) ---

def climb_stairs(n: int) -> int:
    """
    Calculates the number of distinct ways to climb `n` stairs, either 1 or 2
    steps at a time. This is a "Bottom-Up" DP approach. We solve the smallest
    subproblems first and build our way up to the final answer.
    """
    # Base cases for small values of n.
    if n <= 1:
        return 1
    if n == 2:
        return 2

    # Create a DP table (list) to store the number of ways to reach each step.
    # The size is n+1 to have an index for each step from 0 to n.
    dp_table = [0] * (n + 1)

    # Initialize the results for the base cases.
    dp_table[0] = 1 # 1 way to be at the ground (do nothing)
    dp_table[1] = 1 # 1 way to get to the first step (1)
    dp_table[2] = 2 # 2 ways to get to the second step ([1,1], [2])

    # Fill the DP table from the bottom up, starting from the 3rd step.
    for i in range(3, n + 1):
        # The number of ways to reach step `i` is the sum of the ways
        # to reach the previous two steps.
        dp_table[i] = dp_table[i - 1] + dp_table[i - 2]

    # The final answer is the last value in our table.
    return dp_table[n]

# --- Space-Optimized Bottom-Up ---
def climb_stairs_optimized(n: int) -> int:
    """
    A space-optimized version of the bottom-up approach. Notice that to
    calculate `dp[i]`, we only need `dp[i-1]` and `dp[i-2]`. We don't need
    the whole table. We can solve it with just two variables.
    """
    if n <= 1:
        return 1
    
    # `prev` stores ways to climb (i-2), `current` stores ways to climb (i-1)
    prev, current = 1, 1

    for _ in range(n - 1):
        # In each iteration, we calculate the ways for the next step.
        # The new `current` is the sum of the old `prev` and `current`.
        # The new `prev` is the old `current`.
        temp = current
        current = prev + current
        prev = temp
        
    return current


# --- Example Usage ---
if __name__ == "__main__":
    print("--- Fibonacci with Memoization ---")
    # This would be very slow with naive recursion
    print(f"Fibonacci(35): {fib_memoized(35)}") # Expected: 9227465

    print("\n--- Climbing Stairs (Bottom-Up DP) ---")
    print(f"Ways to climb 5 stairs: {climb_stairs(5)}") # Expected: 8
    
    print("\n--- Climbing Stairs (Space-Optimized) ---")
    print(f"Ways to climb 5 stairs (optimized): {climb_stairs_optimized(5)}") # Expected: 8