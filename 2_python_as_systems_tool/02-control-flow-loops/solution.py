"""
Project: Control Flow and Loops - SOLUTION

This file contains the complete and correct solutions for the exercises in
the Control Flow and Loops project.
"""

def fizzbuzz_extended(n, rules):
    """
    Implement a more advanced version of the classic FizzBuzz problem.

    Args:
        n (int): The upper bound of the range of numbers (inclusive).
        rules (dict): A dictionary where keys are integers (divisors) and
                      values are strings (the output string).

    Returns:
        list: A list of strings with the FizzBuzz results.
    """
    results = []
    # Sort the rule keys to ensure a consistent, ordered output.
    # For example, for a multiple of 2 and 3, we always want "AB", not "BA".
    sorted_divisors = sorted(rules.keys())

    # Use a for loop to iterate through the numbers from 1 to n.
    for i in range(1, n + 1):
        output = ""
        # For each number, check it against each rule.
        for divisor in sorted_divisors:
            # The modulo operator (%) gives the remainder of a division.
            # If the remainder is 0, the number is a multiple of the divisor.
            if i % divisor == 0:
                output += rules[divisor]

        # If after all checks the output string is still empty, it means
        # the number was not a multiple of any of the divisors.
        if not output:
            # In this case, we just use the string representation of the number.
            results.append(str(i))
        else:
            # Otherwise, we use the concatenated string.
            results.append(output)

    return results


def validate_password(password):
    """
    Validate a password based on a set of rules.

    A valid password must meet all the following criteria:
    1. It must be at least 8 characters long.
    2. It must contain at least one uppercase letter.
    3. It must contain at least one lowercase letter.
    4. It must contain at least one digit.

    Args:
        password (str): The password string to validate.

    Returns:
        bool: True if the password is valid, False otherwise.
    """
    # --- System 1: Using Boolean Flags ---
    # This is a very explicit and readable way to solve the problem.

    # First, check the length requirement. `len()` is an O(1) operation.
    if len(password) < 8:
        return False

    # Initialize boolean flags to track if each condition is met.
    has_uppercase = False
    has_lowercase = False
    has_digit = False

    # Iterate through each character of the password.
    for char in password:
        # The `isupper()`, `islower()`, and `isdigit()` methods return True
        # if the character meets the condition.
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True

    # After the loop, all three flags must be True for the password to be valid.
    # The `and` operator ensures this.
    return has_uppercase and has_lowercase and has_digit

    # --- System 2: More "Pythonic" version ---
    # This version is more concise but might be less readable for a beginner.
    # It demonstrates the power of generator expressions and the `any()` function.
    #
    # if len(password) < 8:
    #     return False
    #
    # has_uppercase = any(c.isupper() for c in password)
    # has_lowercase = any(c.islower() for c in password)
    # has_digit = any(c.isdigit() for c in password)
    #
    # return has_uppercase and has_lowercase and has_digit