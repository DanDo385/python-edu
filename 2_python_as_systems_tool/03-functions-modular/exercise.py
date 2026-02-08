"""
Project: Functions and Modularity

This project challenges you to break down a larger task into smaller,
manageable, and reusable functions. This is a core principle of good
software design.
"""

# The text we will be analyzing.
TEXT_BLOCK = """
Python is an interpreted, high-level, general-purpose programming language.
Created by Guido van Rossum and first released in 1991, Python's design
philosophy emphasizes code readability with its notable use of significant
whitespace. Its language constructs and object-oriented approach aim to help
programmers write clear, logical code for small and large-scale projects.
"""

def count_words(text):
    """
    Counts the number of words in a given string.
    A word is defined as a sequence of characters separated by whitespace.

    Args:
        text (str): The text to analyze.

    Returns:
        int: The number of words.
    """
    # TODO: Implement this function.
    # Hint: The `split()` string method will be very useful here.
    pass


def count_lines(text):
    """
    Counts the number of lines in a given string.
    A line is defined as a sequence of characters separated by a newline
    character ('\n').

    Args:
        text (str): The text to analyze.

    Returns:
        int: The number of lines.
    """
    # TODO: Implement this function.
    # Hint: The `splitlines()` string method is designed for this.
    pass


def calculate_average_word_length(text):
    """
    Calculates the average length of words in a given string.
    Punctuation that is part of a word should be included in its length.
    For example, "programmers." is a word of length 11.

    Args:
        text (str): The text to analyze.

    Returns:
        float: The average word length. Returns 0.0 if there are no words.
    """
    # TODO: Implement this function.
    # Hint: You'll need to get all the words first. Then, for each word,
    # find its length. Finally, calculate the average. Watch out for
    # division by zero if the text is empty!
    pass


def generate_text_statistics(text):
    """
    Generates a dictionary of statistics for a given block of text.

    This function should call the other functions you've written to build
    a dictionary containing the following keys:
    - 'word_count'
    - 'line_count'
    - 'character_count'
    - 'average_word_length'

    Args:
        text (str): The text to analyze.

    Returns:
        dict: A dictionary with the calculated statistics.
    """
    # TODO: Implement this function.
    # You will need to call your other functions from here.
    # For 'character_count', you can simply use the `len()` function.
    pass


# To test your implementation, you can run this file and print the result.
if __name__ == "__main__":
    stats = generate_text_statistics(TEXT_BLOCK)
    print("Text Statistics:")
    print(f"  - Word Count: {stats.get('word_count')}")
    print(f"  - Line Count: {stats.get('line_count')}")
    print(f"  - Character Count: {stats.get('character_count')}")
    print(f"  - Average Word Length: {stats.get('average_word_length'):.2f}")