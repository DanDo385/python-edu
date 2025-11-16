"""
Project 01: Python Basics Review

This module implements fundamental Python operations and introduces
Big-O complexity analysis for algorithm efficiency.

Author: Python-Edu DSA Curriculum
Time Complexity: O(n) for most operations
Space Complexity: O(1) to O(n) depending on the function
"""

from typing import List, Dict


def find_maximum(arr: List[int]) -> int:
    """
    Find the maximum element in an array.
    
    This is a fundamental operation that demonstrates:
    - Array iteration
    - Comparison operations
    - Edge case handling
    
    Algorithm:
    1. Handle edge case (empty array)
    2. Initialize max_val with first element
    3. Iterate through remaining elements
    4. Update max_val when larger element found
    5. Return max_val
    
    Args:
        arr: List of integers (may be empty)
        
    Returns:
        Maximum integer in the list
        
    Raises:
        ValueError: If array is empty
        
    Time Complexity: O(n) where n is length of array
    Space Complexity: O(1) - only using a single variable
    
    Examples:
        >>> find_maximum([1, 5, 3, 9, 2])
        9
        >>> find_maximum([-1, -5, -3])
        -1
        >>> find_maximum([42])
        42
    """
    if not arr:
        raise ValueError("Cannot find maximum of empty array")
    
    # Initialize with first element
    max_val = arr[0]
    
    # Compare with remaining elements
    for num in arr[1:]:  # O(n) iteration
        if num > max_val:
            max_val = num
    
    return max_val


def reverse_string(s: str) -> str:
    """
    Reverse a string using Python slicing.
    
    Demonstrates:
    - String immutability in Python
    - Slice notation [::-1]
    - Alternative: two-pointer technique
    
    Args:
        s: Input string
        
    Returns:
        Reversed string
        
    Time Complexity: O(n) where n is length of string
    Space Complexity: O(n) - new string created
    
    Examples:
        >>> reverse_string("hello")
        'olleh'
        >>> reverse_string("Python")
        'nohtyP'
        >>> reverse_string("")
        ''
    """
    # Python's slice notation: [start:end:step]
    # [::-1] means start=beginning, end=end, step=-1 (backwards)
    return s[::-1]


def is_palindrome(s: str) -> bool:
    """
    Check if a string is a palindrome (reads same forwards/backwards).
    
    This implementation:
    - Ignores spaces and case
    - Uses two-pointer technique
    - Only compares alphanumeric characters
    
    Algorithm:
    1. Clean string: remove spaces, convert to lowercase
    2. Use two pointers (left and right)
    3. Compare characters while moving pointers inward
    4. Return False if mismatch found, True if all match
    
    Args:
        s: Input string
        
    Returns:
        True if palindrome (ignoring spaces/case), False otherwise
        
    Time Complexity: O(n) where n is length of string
    Space Complexity: O(n) for cleaned string
    
    Examples:
        >>> is_palindrome("racecar")
        True
        >>> is_palindrome("hello")
        False
        >>> is_palindrome("A man a plan a canal Panama")
        True
    """
    # Clean the string: remove spaces and convert to lowercase
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    
    # Two-pointer approach
    left, right = 0, len(cleaned) - 1
    
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    
    return True


def fibonacci(n: int) -> int:
    """
    Return the nth Fibonacci number using iterative approach.
    
    Fibonacci sequence: F(0)=0, F(1)=1, F(n)=F(n-1)+F(n-2)
    Sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89...
    
    This implementation uses iteration (not recursion) for efficiency:
    - Recursive: O(2^n) - exponential time, very slow
    - Iterative: O(n) - linear time, much faster
    
    Algorithm:
    1. Handle base cases (n=0, n=1)
    2. Initialize prev=0, curr=1
    3. Iterate n-1 times, updating values
    4. Return current value
    
    Args:
        n: Position in Fibonacci sequence (0-indexed)
        
    Returns:
        nth Fibonacci number
        
    Raises:
        ValueError: If n is negative
        
    Time Complexity: O(n) - single loop
    Space Complexity: O(1) - only two variables
    
    Examples:
        >>> fibonacci(0)
        0
        >>> fibonacci(1)
        1
        >>> fibonacci(10)
        55
        >>> fibonacci(20)
        6765
    """
    if n < 0:
        raise ValueError("Fibonacci not defined for negative numbers")
    
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # Iterative approach: track previous two values
    prev, curr = 0, 1
    
    for _ in range(2, n + 1):
        # Calculate next Fibonacci number
        prev, curr = curr, prev + curr
    
    return curr


def count_frequency(arr: List[int]) -> Dict[int, int]:
    """
    Count frequency of each element in an array.
    
    Demonstrates:
    - Hash table (dictionary) usage
    - O(1) average-case lookup/insert
    - Counting pattern (very common in interviews)
    
    Algorithm:
    1. Initialize empty dictionary
    2. Iterate through array
    3. For each element, increment its count
    4. Return frequency map
    
    Args:
        arr: List of integers
        
    Returns:
        Dictionary mapping each element to its frequency
        
    Time Complexity: O(n) where n is length of array
    Space Complexity: O(k) where k is number of unique elements
    
    Examples:
        >>> count_frequency([1, 2, 2, 3, 3, 3])
        {1: 1, 2: 2, 3: 3}
        >>> count_frequency([5, 5, 5, 5])
        {5: 4}
        >>> count_frequency([])
        {}
    """
    frequency = {}
    
    for num in arr:
        # Get current count (default to 0), then increment
        frequency[num] = frequency.get(num, 0) + 1
        
        # Alternative using setdefault:
        # frequency.setdefault(num, 0)
        # frequency[num] += 1
    
    return frequency


# Additional helper function to demonstrate Big-O concepts
def demonstrate_big_o():
    """
    Demonstrate different Big-O complexities.
    
    This is educational - showing how different algorithms scale.
    """
    # O(1) - Constant time
    def constant_time_operation(arr: List[int]) -> int:
        """Always takes same time, regardless of input size."""
        return arr[0] if arr else None
    
    # O(log n) - Logarithmic time
    def binary_search(arr: List[int], target: int) -> int:
        """Halves search space each iteration."""
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    
    # O(n) - Linear time
    def linear_search(arr: List[int], target: int) -> int:
        """May need to check every element."""
        for i, num in enumerate(arr):
            if num == target:
                return i
        return -1
    
    # O(n²) - Quadratic time
    def bubble_sort(arr: List[int]) -> List[int]:
        """Nested loops, each running n times."""
        arr = arr.copy()
        n = len(arr)
        for i in range(n):
            for j in range(n - 1 - i):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr
    
    print("Big-O Complexity Demonstration")
    print("=" * 50)
    print("O(1):     Constant   - Array access")
    print("O(log n): Logarithmic - Binary search")
    print("O(n):     Linear     - Linear search")
    print("O(n²):    Quadratic  - Bubble sort")
    print("O(2^n):   Exponential - Recursive Fibonacci (naive)")


if __name__ == "__main__":
    # Test the functions
    print("Testing Python Basics Review")
    print("=" * 50)
    
    # Test find_maximum
    print("\n1. Find Maximum:")
    print(f"   [1,5,3,9,2] -> {find_maximum([1, 5, 3, 9, 2])}")
    
    # Test reverse_string
    print("\n2. Reverse String:")
    print(f"   'hello' -> '{reverse_string('hello')}'")
    
    # Test is_palindrome
    print("\n3. Is Palindrome:")
    print(f"   'racecar' -> {is_palindrome('racecar')}")
    print(f"   'hello' -> {is_palindrome('hello')}")
    
    # Test fibonacci
    print("\n4. Fibonacci:")
    print(f"   F(10) -> {fibonacci(10)}")
    
    # Test count_frequency
    print("\n5. Count Frequency:")
    print(f"   [1,2,2,3,3,3] -> {count_frequency([1, 2, 2, 3, 3, 3])}")
    
    print("\n" + "=" * 50)
    demonstrate_big_o()
