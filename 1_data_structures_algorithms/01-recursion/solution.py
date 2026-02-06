"""
Project 08: Recursion and Divide-and-Conquer - SOLUTION

Complete solution with detailed comments explaining recursion and the call stack.
"""


def factorial(n):
    """
    Calculate factorial recursively.
    
    This demonstrates basic recursion: a function calling itself.
    The key is identifying the base case (when to stop) and the
    recursive case (how to break down the problem).
    
    Recursive definition:
    - Base case: 0! = 1, 1! = 1
    - Recursive case: n! = n × (n-1)!
    
    Call stack for factorial(3):
    factorial(3)
      → calls factorial(2)
        → calls factorial(1)
          → returns 1 (base case)
        → returns 2 × 1 = 2
      → returns 3 × 2 = 6
    
    Args:
        n (int): Non-negative integer
    
    Returns:
        int: Factorial of n
    """
    # Base case: simplest problem that doesn't need recursion
    # Both 0! and 1! equal 1 by mathematical definition
    # This stops the recursion - without it, we'd recurse forever
    if n == 0 or n == 1:
        return 1
    
    # Recursive case: break problem into smaller version
    # n! = n × (n-1)!
    # We calculate (n-1)! recursively, then multiply by n
    # We "trust" that factorial(n-1) will work correctly
    return n * factorial(n - 1)


def fibonacci(n):
    """
    Calculate nth Fibonacci number recursively.
    
    Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
    Each number is the sum of the two preceding ones.
    
    Recursive definition:
    - Base cases: F(0) = 0, F(1) = 1
    - Recursive case: F(n) = F(n-1) + F(n-2)
    
    Note: This recursive implementation is inefficient (exponential time)
    because it recalculates the same values many times. A better approach
    would use memoization or iteration, but this demonstrates recursion.
    
    Args:
        n (int): Non-negative integer
    
    Returns:
        int: nth Fibonacci number
    """
    # Base case 1: F(0) = 0
    if n == 0:
        return 0
    
    # Base case 2: F(1) = 1
    if n == 1:
        return 1
    
    # Recursive case: F(n) = F(n-1) + F(n-2)
    # We need both previous Fibonacci numbers, so we make two recursive calls
    # This creates a binary tree of recursive calls
    return fibonacci(n - 1) + fibonacci(n - 2)


def gcd(a, b):
    """
    Calculate Greatest Common Divisor using Euclidean algorithm.
    
    The Euclidean algorithm is one of the oldest algorithms. It's based on
    the principle that GCD(a, b) = GCD(b, a mod b).
    
    Recursive definition:
    - Base case: GCD(a, 0) = a (when b becomes 0)
    - Recursive case: GCD(a, b) = GCD(b, a mod b)
    
    Example: GCD(48, 18)
    GCD(48, 18) → GCD(18, 48 % 18 = 12) → GCD(12, 18 % 12 = 6) → GCD(6, 12 % 6 = 0) → 6
    
    Args:
        a (int): First number
        b (int): Second number
    
    Returns:
        int: GCD of a and b
    """
    # Base case: when b becomes 0, a is the GCD
    # This happens because if b divides a evenly, GCD is b
    # When remainder becomes 0, the previous b was the GCD
    if b == 0:
        return a
    
    # Recursive case: GCD(a, b) = GCD(b, a mod b)
    # a mod b gives the remainder when a is divided by b
    # We swap the arguments: b becomes the new a, remainder becomes new b
    # This reduces the problem size each time
    return gcd(b, a % b)


def binary_search(arr, target, left=0, right=None):
    """
    Binary search using divide-and-conquer recursion.
    
    Binary search is a classic divide-and-conquer algorithm. It works by
    repeatedly dividing the search space in half. Since the array is sorted,
    we can eliminate half the elements at each step.
    
    Divide-and-conquer strategy:
    1. Divide: Find middle element
    2. Conquer: Compare with target, decide which half to search
    3. Combine: Return result (no combination needed, just return index)
    
    Time complexity: O(log n) - much better than linear search O(n)
    
    Args:
        arr (list): Sorted list of numbers
        target: Value to search for
        left (int): Left boundary of search range
        right (int): Right boundary of search range
    
    Returns:
        int: Index of target, or -1 if not found
    """
    # Initialize right boundary if not provided
    # Default parameter allows calling without specifying right
    if right is None:
        right = len(arr) - 1
    
    # Base case: search range is invalid (left > right)
    # This means we've searched everywhere and didn't find the target
    if left > right:
        return -1
    
    # Divide: find the middle index
    # Using (left + right) // 2 avoids integer overflow (though not an issue in Python)
    middle = (left + right) // 2
    
    # Check if middle element is the target
    if arr[middle] == target:
        # Found it! Return the index
        return middle
    
    # Conquer: decide which half to search
    # Since array is sorted, if target < middle element, it must be in left half
    elif target < arr[middle]:
        # Search left half: same array, target, but right boundary becomes middle-1
        return binary_search(arr, target, left, middle - 1)
    
    # Otherwise, target > middle element, so search right half
    else:
        # Search right half: left boundary becomes middle+1
        return binary_search(arr, target, middle + 1, right)


def sum_list_recursive(numbers):
    """
    Calculate sum of list recursively.
    
    This demonstrates recursion on data structures. We break the list
    into its first element and the rest of the list, then recurse on
    the rest.
    
    Recursive definition:
    - Base case: sum([]) = 0 (empty list)
    - Recursive case: sum([x, ...]) = x + sum([...])
    
    Args:
        numbers (list): List of numbers
    
    Returns:
        int or float: Sum of numbers, or 0 if empty
    """
    # Base case: empty list has sum 0
    # This stops the recursion when we've processed all elements
    if len(numbers) == 0:
        return 0
    
    # Recursive case: sum = first element + sum of rest
    # numbers[0] is the first element
    # numbers[1:] is the rest of the list (slice from index 1 to end)
    # We recurse on the smaller list (one element shorter)
    return numbers[0] + sum_list_recursive(numbers[1:])

