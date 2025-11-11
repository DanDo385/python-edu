"""
Project 04: Context Managers - Practice Stubs

TODO: Implement these context managers
Run tests with: pytest test_solution.py -v
"""

from contextlib import contextmanager
from typing import Any


class FileManager:
    """
    Context manager for file operations.

    Example:
        with FileManager('file.txt', 'r') as f:
            content = f.read()
    """

    def __init__(self, filename: str, mode: str):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        # TODO: Open file and return file object
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        # TODO: Close file
        # Return False to propagate exceptions
        pass


class Timer:
    """
    Context manager that measures execution time.

    Example:
        with Timer() as t:
            # some code
            pass
        print(t.elapsed)
    """

    def __init__(self):
        self.start = None
        self.end = None
        self.elapsed = None

    def __enter__(self):
        # TODO: Record start time
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        # TODO: Calculate elapsed time
        pass


@contextmanager
def temporary_value(obj, attr, value):
    """
    Context manager that temporarily changes an attribute.

    Example:
        class Config:
            debug = False

        config = Config()
        with temporary_value(config, 'debug', True):
            print(config.debug)  # True
        print(config.debug)  # False
    """
    # TODO: Implement using @contextmanager decorator
    # Hint: Save old value, set new value, yield, restore old value
    pass


if __name__ == "__main__":
    print("Test your implementations:")

    with Timer() as t:
        import time
        time.sleep(0.1)
    print(f"Elapsed: {t.elapsed:.2f}s")
