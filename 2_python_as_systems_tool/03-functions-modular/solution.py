"""
Project: Functions and Modularity - SOLUTION

This file provides the complete and correct solutions for the functions and
modularity project. The key lesson is how a larger problem can be solved by
composing smaller, well-defined functions.
"""

# The text we will be analyzing.
TEXT_BLOCK = """
Python is an interpreted, high-level, general-purpose programming language.
Created by Guido van Rossum and first released in 1991, Python's design
philosophy emphasizes code readability with its notable use of significant
whitespace. Its language constructs and object-oriented approach aim to help
programmers write clear, logical code for small and large-scale projects.
"""

def count_words(text: str) -> int:
    """
    Counts the number of words in a given string.
    A word is defined as a sequence of characters separated by whitespace.

    Args:
        text (str): The text to analyze.

    Returns:
        int: The number of words.
    """
    # The `split()` method, when called without arguments, splits the string
    # by any sequence of whitespace and discards empty strings.
    words = text.split()
    return len(words)


def count_lines(text: str) -> int:
    """
    Counts the number of lines in a given string.
    A line is defined as a sequence of characters separated by a newline
    character ('\n').

    Args:
        text (str): The text to analyze.

    Returns:
        int: The number of lines.
    """
    # The `splitlines()` method is perfect for this. It splits the string
    # at line breaks and returns a list of the lines.
    lines = text.splitlines()
    return len(lines)


def calculate_average_word_length(text: str) -> float:
    """
    Calculates the average length of words in a given string.
    Punctuation that is part of a word should be included in its length.

    Args:
        text (str): The text to analyze.

    Returns:
        float: The average word length. Returns 0.0 if there are no words.
    """
    words = text.split()
    
    # Defensive programming: handle the edge case of empty text.
    if not words:
        return 0.0

    # We can use a generator expression to get the length of each word.
    total_length = sum(len(word) for word in words)
    word_count = len(words)

    # Perform the division to get the average.
    return total_length / word_count


def generate_text_statistics(text: str) -> dict:
    """
    Generates a dictionary of statistics for a given block of text.

    This function calls the other functions to build a dictionary containing
    the statistics, demonstrating function composition.

    Args:
        text (str): The text to analyze.

    Returns:
        dict: A dictionary with the calculated statistics.
    """
    # Call the helper functions to get the required values.
    # This makes the logic clear and compartmentalized. If we need to change
    # how we count words, we only have to change the `count_words` function.
    word_count_stat = count_words(text)
    line_count_stat = count_lines(text)
    avg_word_len_stat = calculate_average_word_length(text)

    # The character count is simple enough to calculate directly.
    char_count_stat = len(text)

    # Assemble the results into a dictionary.
    stats = {
        'word_count': word_count_stat,
        'line_count': line_count_stat,
        'character_count': char_count_stat,
        'average_word_length': avg_word_len_stat,
    }
    return stats


if __name__ == "__main__":
    stats = generate_text_statistics(TEXT_BLOCK)
    
    print("Text Statistics:")
    print(f"  - Word Count: {stats.get('word_count')}")
    print(f"  - Line Count: {stats.get('line_count')}")
    print(f"  - Character Count: {stats.get('character_count')}")
    print(f"  - Average Word Length: {stats.get('average_word_length'):.2f}")
