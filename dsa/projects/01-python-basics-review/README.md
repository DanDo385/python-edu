# Project 01: Python Basics Review

## Overview

This project reviews essential Python concepts and introduces Big-O complexity analysis—the foundation for all DSA work.

## Learning Objectives

- Review Python fundamentals (lists, loops, functions)
- Understand time and space complexity
- Learn Big-O notation
- Practice writing efficient code

## Problems

Implement the following functions in `solution/solution.py`:

### Problem 1: Find Maximum (Easy)
```python
def find_maximum(arr: List[int]) -> int:
    """
    Find the maximum element in an array.
    
    Args:
        arr: List of integers
        
    Returns:
        Maximum integer in the list
        
    Time Complexity: O(?)
    Space Complexity: O(?)
    """
```

**Examples:**
```python
find_maximum([1, 5, 3, 9, 2]) # Returns 9
find_maximum([-1, -5, -3]) # Returns -1
find_maximum([42]) # Returns 42
```

### Problem 2: Reverse String (Easy)
```python
def reverse_string(s: str) -> str:
    """
    Reverse a string.
    
    Args:
        s: Input string
        
    Returns:
        Reversed string
        
    Time Complexity: O(?)
    Space Complexity: O(?)
    """
```

**Examples:**
```python
reverse_string("hello") # Returns "olleh"
reverse_string("Python") # Returns "nohtyP"
reverse_string("") # Returns ""
```

### Problem 3: Is Palindrome (Easy)
```python
def is_palindrome(s: str) -> bool:
    """
    Check if a string is a palindrome (reads same forwards/backwards).
    
    Args:
        s: Input string
        
    Returns:
        True if palindrome, False otherwise
        
    Time Complexity: O(?)
    Space Complexity: O(?)
    """
```

**Examples:**
```python
is_palindrome("racecar") # Returns True
is_palindrome("hello") # Returns False
is_palindrome("A man a plan a canal Panama") # Returns True (ignoring spaces/case)
```

### Problem 4: Fibonacci (Medium)
```python
def fibonacci(n: int) -> int:
    """
    Return the nth Fibonacci number.
    F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2)
    
    Args:
        n: Position in Fibonacci sequence
        
    Returns:
        nth Fibonacci number
        
    Time Complexity: O(?) - aim for O(n)
    Space Complexity: O(?)
    """
```

**Examples:**
```python
fibonacci(0) # Returns 0
fibonacci(1) # Returns 1
fibonacci(10) # Returns 55
fibonacci(20) # Returns 6765
```

### Problem 5: Count Frequency (Medium)
```python
def count_frequency(arr: List[int]) -> Dict[int, int]:
    """
    Count frequency of each element in an array.
    
    Args:
        arr: List of integers
        
    Returns:
        Dictionary mapping each element to its frequency
        
    Time Complexity: O(?)
    Space Complexity: O(?)
    """
```

**Examples:**
```python
count_frequency([1, 2, 2, 3, 3, 3]) # Returns {1: 1, 2: 2, 3: 3}
count_frequency([5, 5, 5, 5]) # Returns {5: 4}
count_frequency([]) # Returns {}
```

## Big-O Complexity Reference

| Notation | Name | Example |
|----------|------|---------|
| O(1) | Constant | Array access by index |
| O(log n) | Logarithmic | Binary search |
| O(n) | Linear | Linear search, single loop |
| O(n log n) | Linearithmic | Merge sort, heap sort |
| O(n²) | Quadratic | Nested loops, bubble sort |
| O(2ⁿ) | Exponential | Recursive Fibonacci (naive) |

## Constraints

- For all problems: 0 ≤ array/string length ≤ 10,000
- All integers fit in 32-bit signed integer range

## Testing

```bash
pytest tests/ -v
```

## Tips

1. **Start simple**: Get it working first, optimize later
2. **Edge cases**: Always test with empty inputs
3. **Complexity**: Analyze your solution's Big-O
4. **Practice**: These fundamentals appear everywhere in DSA

## Next Steps

After completing this project, you'll be ready for:
- Project 02: Array Operations
- Project 03: Two Pointer Technique
