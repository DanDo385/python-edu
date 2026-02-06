"""
Project 02: Control Flow and Loops - SOLUTION

This file contains the complete solution with detailed comments explaining
each step of the implementation.
"""


def is_even(number):
    """
    Check if a number is even.
    
    An even number is divisible by 2 with no remainder.
    We use the modulo operator (%) which returns the remainder after division.
    
    Args:
        number (int): The number to check
    
    Returns:
        bool: True if number is even, False otherwise
    """
    # Modulo operator (%) returns the remainder after division
    # If number % 2 == 0, then number is divisible by 2 (even)
    # If number % 2 == 1, then number has remainder 1 (odd)
    return number % 2 == 0


def get_grade(score):
    """
    Determine the letter grade based on a numerical score.
    
    This demonstrates if/elif/else chain for multiple conditions.
    We check from highest to lowest scores.
    
    Args:
        score (int): The numerical score (0-100)
    
    Returns:
        str: The letter grade
    """
    # Check conditions from highest to lowest
    # Using >= ensures boundary values are included correctly
    
    if score >= 90:
        # 90-100: Grade A
        return 'A'
    elif score >= 80:
        # 80-89: Grade B
        # Note: We don't need to check < 90 because if we reach here,
        # the score must be < 90 (otherwise first condition would have matched)
        return 'B'
    elif score >= 70:
        # 70-79: Grade C
        return 'C'
    elif score >= 60:
        # 60-69: Grade D
        return 'D'
    else:
        # Below 60: Grade F
        # This catches all scores < 60
        return 'F'


def fizzbuzz(n):
    """
    Generate FizzBuzz sequence up to n.
    
    Classic programming problem combining conditionals and loops.
    Key insight: Check most specific condition (divisible by both) first!
    
    Args:
        n (int): Upper limit (inclusive)
    
    Returns:
        list: List of strings representing the FizzBuzz sequence
    """
    result = []
    
    # Loop through numbers from 1 to n (inclusive)
    # range(1, n+1) gives us 1, 2, 3, ..., n
    for i in range(1, n + 1):
        # IMPORTANT: Check most specific condition first!
        # If we check "divisible by 3" first, we'd catch 15 and say "Fizz"
        # before checking if it's also divisible by 5
        
        if i % 3 == 0 and i % 5 == 0:
            # Divisible by both 3 and 5: "FizzBuzz"
            result.append("FizzBuzz")
        elif i % 3 == 0:
            # Divisible by 3 only: "Fizz"
            result.append("Fizz")
        elif i % 5 == 0:
            # Divisible by 5 only: "Buzz"
            result.append("Buzz")
        else:
            # Not divisible by 3 or 5: the number itself
            # Convert to string to match other return types
            result.append(str(i))
    
    return result


def sum_numbers(n):
    """
    Calculate the sum of all numbers from 1 to n (inclusive).
    
    This demonstrates the accumulator pattern: start with 0, add each number.
    
    Args:
        n (int): Upper limit
    
    Returns:
        int: Sum of numbers from 1 to n
    """
    # Initialize accumulator to 0
    # This will hold our running total
    total = 0
    
    # Loop through numbers from 1 to n
    for i in range(1, n + 1):
        # Add current number to total
        # Equivalent to: total = total + i
        total += i
    
    return total
    
    # Note: There's a mathematical formula: n * (n + 1) / 2
    # But we're learning loops, so we use iteration!


def sum_even_numbers(n):
    """
    Calculate the sum of all even numbers from 1 to n (inclusive).
    
    Combines loop with conditional: only add numbers that meet criteria.
    
    Args:
        n (int): Upper limit
    
    Returns:
        int: Sum of even numbers from 1 to n
    """
    total = 0
    
    for i in range(1, n + 1):
        # Only add if number is even
        # Use our is_even function, or check directly: i % 2 == 0
        if i % 2 == 0:
            total += i
    
    return total


def find_first_even(numbers):
    """
    Find the first even number in a list.
    
    Demonstrates early return pattern: exit as soon as we find what we need.
    
    Args:
        numbers (list): List of integers
    
    Returns:
        int or None: First even number, or None if no even numbers exist
    """
    # Loop through each number in the list
    for num in numbers:
        # Check if current number is even
        if num % 2 == 0:
            # Found it! Return immediately (early exit)
            # No need to check remaining numbers
            return num
    
    # If we get here, we didn't find any even numbers
    # Return None to indicate "not found"
    return None


def count_occurrences(numbers, target):
    """
    Count how many times target appears in numbers.
    
    Demonstrates conditional accumulation: increment counter when condition met.
    
    Args:
        numbers (list): List of integers
        target (int): Number to count
    
    Returns:
        int: Number of occurrences of target
    """
    # Initialize counter to 0
    count = 0
    
    # Loop through each number
    for num in numbers:
        # If current number matches target, increment counter
        if num == target:
            count += 1
    
    return count


def print_multiplication_table(n):
    """
    Print a multiplication table up to n x n.
    
    Demonstrates nested loops: outer loop for rows, inner loop for columns.
    
    Args:
        n (int): Size of multiplication table
    
    Returns:
        list: List of lists representing the multiplication table
    """
    table = []
    
    # Outer loop: rows (1 to n)
    for i in range(1, n + 1):
        # Create a new row
        row = []
        
        # Inner loop: columns (1 to n)
        for j in range(1, n + 1):
            # Multiply row number by column number
            # This gives us the value at position (i, j)
            row.append(i * j)
        
        # Add completed row to table
        table.append(row)
    
    return table
    
    # Example for n=3:
    # i=1: row = [1*1, 1*2, 1*3] = [1, 2, 3]
    # i=2: row = [2*1, 2*2, 2*3] = [2, 4, 6]
    # i=3: row = [3*1, 3*2, 3*3] = [3, 6, 9]


def find_maximum(numbers):
    """
    Find the maximum value in a list of numbers.
    
    Demonstrates finding extremum: compare each element to current best.
    
    Args:
        numbers (list): List of numbers (assumed non-empty)
    
    Returns:
        int or float: Maximum value in the list
    """
    # Handle empty list edge case
    if not numbers:
        return None
    
    # Initialize max_value with first element
    # This ensures we have a valid starting point
    max_value = numbers[0]
    
    # Loop through remaining elements (skip first since we already have it)
    # Could also loop through all: for num in numbers[1:]
    for i in range(1, len(numbers)):
        # If current number is greater than current max, update max
        if numbers[i] > max_value:
            max_value = numbers[i]
    
    return max_value
    
    # Alternative approach: loop through all elements
    # for num in numbers:
    #     if num > max_value:
    #         max_value = num


def reverse_string(text):
    """
    Reverse a string using a loop.
    
    Builds new string by prepending characters from original string.
    
    Args:
        text (str): String to reverse
    
    Returns:
        str: Reversed string
    """
    reversed_text = ""
    
    # Loop through each character in the original string
    for char in text:
        # Prepend current character to reversed_text
        # This builds the reversed string character by character
        # Example: "hello" -> "o" -> "lo" -> "llo" -> "ello" -> "hello"
        reversed_text = char + reversed_text
    
    return reversed_text
    
    # Alternative: Use slicing (but we're learning loops!)
    # return text[::-1]


def is_prime(n):
    """
    Check if a number is prime.
    
    A prime number is greater than 1 and has no divisors other than 1 and itself.
    We check if any number from 2 to sqrt(n) divides n evenly.
    
    Args:
        n (int): Number to check
    
    Returns:
        bool: True if n is prime, False otherwise
    """
    # Edge cases: numbers less than 2 are not prime
    if n < 2:
        return False
    
    # Check for divisors from 2 to sqrt(n)
    # We only need to check up to sqrt(n) because if n has a divisor
    # greater than sqrt(n), it must also have one less than sqrt(n)
    # Example: 16 = 4 * 4, so if we check up to 4, we'll find it
    
    # Use int(n ** 0.5) + 1 to ensure we check up to sqrt(n)
    # +1 because range is exclusive on the right
    for i in range(2, int(n ** 0.5) + 1):
        # If n is divisible by i (no remainder), it's not prime
        if n % i == 0:
            return False
    
    # If we get here, no divisors were found, so n is prime
    return True

